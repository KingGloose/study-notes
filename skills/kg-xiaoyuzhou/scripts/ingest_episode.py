#!/usr/bin/env python3
"""小宇宙播客单集摄入：解析元信息 + shownotes（白拿），可选下载音频本地转写。

用法:
  # 阶段1：只拿元信息 + shownotes（快，零 ASR）
  python ingest_episode.py <小宇宙链接>

  # 阶段2：连带下载音频、本地 ASR 转写逐字稿（慢，需 asr 依赖 + ffmpeg）
  python ingest_episode.py <链接> --transcribe

  # 只预览不落盘
  python ingest_episode.py <链接> --stdout

说明:
  - 单集公开页面无需登录（安全）。官方逐字稿 API 需鉴权且带封号风险，本脚本不使用。
  - 转写走底层库 media_to_text，自动按平台选 ASR 后端（Mac=mlx / Linux=faster）。
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
from datetime import datetime
from pathlib import Path

from curl_cffi import requests as cffi
from bs4 import BeautifulSoup

# 库根：优先 KG_VAULT 环境变量 / ~/.config/kg-wiki/config.json，
# 否则从 cwd 或本文件位置向上找（含 AGENTS.md + wiki/ 的目录）
from media_to_text import find_vault
REPO_ROOT = find_vault(__file__)
RAW_DIR = REPO_ROOT / "raw"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def eprint(*a, **k):
    print(*a, file=sys.stderr, **k)


def sanitize(name: str) -> str:
    name = re.sub(r"[\\/:*?\"<>|\n\r\t]", "_", name).strip()
    return name[:60] or "episode"


def fmt_duration(sec) -> str:
    try:
        sec = int(sec)
    except (TypeError, ValueError):
        return ""
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def _find_episode(obj):
    """在 __NEXT_DATA__ 里递归定位 episode 对象。"""
    if isinstance(obj, dict):
        if "title" in obj and ("enclosure" in obj or "duration" in obj):
            return obj
        for v in obj.values():
            r = _find_episode(v)
            if r:
                return r
    elif isinstance(obj, list):
        for v in obj:
            r = _find_episode(v)
            if r:
                return r
    return None


def fetch_episode(url: str) -> dict:
    try:
        r = cffi.get(url, headers={"User-Agent": UA}, impersonate="chrome", timeout=30)
        r.raise_for_status()
    except Exception as e:
        sys.exit(f"[错误] 请求页面失败（{type(e).__name__}）: {e}\n"
                 f"       检查网络、链接是否有效，或该单集是否已下线/需权限。")
    html = r.text
    m = re.search(
        r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, re.S
    )
    if not m:
        sys.exit("[错误] 未找到 __NEXT_DATA__，页面结构可能已变化。")
    try:
        payload = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        sys.exit(f"[错误] __NEXT_DATA__ 解析失败（页面结构可能已变）: {e}")
    ep = _find_episode(payload)
    if not ep:
        sys.exit("[错误] 未能在页面数据中定位单集信息。")

    shownotes_html = ep.get("shownotes") or ""
    shownotes_text = ""
    if shownotes_html:
        soup = BeautifulSoup(shownotes_html, "lxml")
        # 保留换行结构：块级元素之间插入换行
        for br in soup.find_all("br"):
            br.replace_with("\n")
        for p in soup.find_all(["p", "div", "li"]):
            p.append("\n")
        shownotes_text = re.sub(r"\n{3,}", "\n\n", soup.get_text()).strip()

    return {
        "eid": ep.get("eid", ""),
        "title": ep.get("title", ""),
        "podcast": (ep.get("podcast") or {}).get("title", ""),
        "duration": ep.get("duration"),
        "pub_date": (ep.get("pubDate") or "")[:10],
        "audio_url": (ep.get("enclosure") or {}).get("url", ""),
        "description": (ep.get("description") or "").strip(),
        "shownotes": shownotes_text,
        "url": url,
    }


def download_audio(audio_url: str, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    ext = ".mp3" if ".mp3" in audio_url else ".m4a"
    dest = dest_dir / f"audio{ext}"
    eprint(f"[..] 下载音频 {audio_url[:70]}...")
    # 注：curl_cffi 的 Response 不支持 context manager，不能用 with
    r = cffi.get(audio_url, headers={"User-Agent": UA}, impersonate="chrome",
                 timeout=900, stream=True)
    try:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=1 << 20):
                f.write(chunk)
    finally:
        r.close()
    mb = dest.stat().st_size / 1048576
    eprint(f"[ok] 音频已下载 {mb:.1f} MB -> {dest}")
    return dest


def build_markdown(info: dict, transcript: str | None, asr_backend: str | None) -> str:
    lines = [
        f"# {info['title']}",
        "",
        f"- 播客: {info['podcast']}",
        f"- 时长: {fmt_duration(info['duration'])}",
        f"- 发布日期: {info['pub_date']}",
        f"- 原文链接: {info['url']}",
        f"- 音频: {info['audio_url']}",
        f"- 摄入日期: {datetime.now().strftime('%Y-%m-%d')}",
    ]
    if transcript:
        lines.append(f"- 逐字稿: 本地 ASR ({asr_backend})")
    else:
        lines.append("- 逐字稿: 未转写（如需请加 --transcribe）")
    lines += ["", "---", "", "## Shownotes", ""]
    lines.append(info["shownotes"] or info["description"] or "（本集无 shownotes）")

    if transcript:
        lines += ["", "---", "", "## 逐字稿（本地 ASR 生成，可能有识别误差）", "", transcript]
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url", help="小宇宙单集链接")
    ap.add_argument("--transcribe", action="store_true", help="下载音频并本地 ASR 转写")
    ap.add_argument("--model", default=None, help="指定 ASR 模型")
    ap.add_argument("--stdout", action="store_true", help="只打到 stdout，不落盘")
    ap.add_argument("--out", default=None, help="自定义输出路径")
    ap.add_argument("--keep-audio", action="store_true", help="转写后保留音频文件")
    ap.add_argument("--hotword", action="append", default=None, metavar="词",
                    help="补充 ASR 热词（书名/机构/术语），可重复传。shownotes 会自动抽，"
                         "这里只补它抽不到的（例：--hotword Connect --hotword 斯坦福商学院）")
    ap.add_argument("--hotword-speaker", action="append", default=None, metavar="人名",
                    help="主播/嘉宾姓名热词。**人名必须用这个参数**，不要用 --hotword："
                         "实测人名必须放进“我是…”句式才能纠对（例：--hotword-speaker 携隐Melody）")
    args = ap.parse_args()

    if "xiaoyuzhoufm.com" not in args.url:
        eprint("[warn] URL 不像小宇宙链接，仍尝试解析")

    eprint(f"[..] 解析 {args.url}")
    info = fetch_episode(args.url)
    eprint(f"[ok] 《{info['title']}》| {info['podcast']} | {fmt_duration(info['duration'])}"
           f" | shownotes {len(info['shownotes'])} 字")

    transcript = None
    backend = None
    if args.transcribe:
        if not info["audio_url"]:
            eprint("[错误] 未取到音频直链，无法转写。")
            return 2
        tmpdir = Path(tempfile.mkdtemp(prefix="xyz-"))
        try:
            audio = download_audio(info["audio_url"], tmpdir)
        except Exception as e:
            # 下载失败也要清理临时目录，否则 /tmp 会积半成品音频
            shutil.rmtree(tmpdir, ignore_errors=True)
            eprint(f"[错误] 音频下载失败（{type(e).__name__}）: {e}")
            return 2
        eprint("[..] 本地转写中（长音频较慢，请耐心等）")
        try:
            from media_to_text import to_text, extract_hotwords

            # 热词：把已知专名送进 ASR，降低专名误识。
            # 分类传很关键（实测）：节目名要进“欢迎来到…”、人名要进“我是…”，
            # 堆成一串列表无效。shownotes 绝不能裸塞（会超 prompt 上限把模型搞崩）。
            topics = extract_hotwords(text=info["shownotes"] or info["description"], limit=10)
            hot = {
                "channel": [info["podcast"]] if info["podcast"] else [],
                "speakers": args.hotword_speaker or [],
                "topics": (args.hotword or []) + topics,
            }
            n = len(hot["channel"]) + len(hot["speakers"]) + len(hot["topics"])
            eprint(f"[i] 热词 {n} 个（节目={hot['channel']}，人名={hot['speakers']}）")
            r = to_text(audio, model=args.model, language="zh", hotwords=hot)
            transcript, backend = r.text, r.backend
            eprint(f"[ok] 转写完成 {len(transcript)} 字 via {backend}")
        except Exception as e:
            eprint(f"[错误] 转写失败: {e}")
            return 3
        finally:
            if args.keep_audio:
                eprint(f"[i] 音频已保留: {audio}")
            else:
                shutil.rmtree(tmpdir, ignore_errors=True)

    content = build_markdown(info, transcript, backend)

    if args.stdout:
        sys.stdout.write(content)
        return 0

    out = Path(args.out).expanduser() if args.out else (
        RAW_DIR / f"xyz-{info['pub_date']}-{sanitize(info['title'])}.md"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    eprint(f"[ok] 已写入 {out}")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
