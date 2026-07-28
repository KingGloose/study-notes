#!/usr/bin/env python3
"""抓取指定视频的字幕并输出为纯文本。

用法:
  python get_transcript.py <bvid或视频URL> [--json] [--asr] [--model <名>]
                           [--hotword 术语]... [--hotword-speaker 人名]...

  --hotword / --hotword-speaker 仅在走 --asr 时生效，用于降低专名误识。
  人名务必用 --hotword-speaker（实测人名要进"我是…"句式才纠得对）。

策略（降级）:
  1. 拿视频基本信息（标题/UP主/分区/简介/分P）
  2. 逐个分P取 CC/AI 字幕（L0 白拿：平台已生成好的文字，无需 ASR）
  3. 有字幕 → 输出纯文本；无字幕 → 默认仅标注，加 --asr 则下音频调底层库本地转写（L1）

默认输出人类可读文本到 stdout；加 --json 输出结构化 JSON。
"""
import asyncio
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from curl_cffi import requests as cffi_requests
from bilibili_api import video, sync
from _common import load_credential, select_http_client, eprint


def extract_bvid(s: str) -> str:
    m = re.search(r"(BV[0-9A-Za-z]{10})", s)
    if m:
        return m.group(1)
    sys.exit(f"[错误] 无法从 '{s}' 解析出 BV 号")


async def fetch_subtitle_json(url: str) -> dict:
    if url.startswith("//"):
        url = "https:" + url
    # 字幕 JSON 是普通静态资源，用 curl_cffi 同步取即可（放线程池避免阻塞事件循环）
    def _get():
        try:
            r = cffi_requests.get(
                url,
                headers={"Referer": "https://www.bilibili.com"},
                impersonate="chrome",
                timeout=30,
            )
            r.raise_for_status()
            return r.json()
        except Exception as e:
            eprint(f"[warn] 字幕下载失败({type(e).__name__})，该分P将无字幕: {e}")
            return {}

    return await asyncio.to_thread(_get)


async def get_transcript(bvid: str):
    select_http_client()
    cred = load_credential()
    v = video.Video(bvid=bvid, credential=cred)

    info = await v.get_info()
    pages = await v.get_pages()

    result = {
        "bvid": bvid,
        "title": info.get("title", ""),
        "author": info.get("owner", {}).get("name", ""),
        "tname": info.get("tname", ""),
        "desc": (info.get("desc") or "").strip(),
        "url": f"https://www.bilibili.com/video/{bvid}",
        "pages": [],
        "has_subtitle": False,
    }

    for idx, p in enumerate(pages):
        cid = p.get("cid")
        part_title = p.get("part") or info.get("title", "")
        sub_meta = await v.get_subtitle(cid=cid)
        subs = (sub_meta or {}).get("subtitles", []) or []

        page_entry = {"page": idx + 1, "part": part_title, "cid": cid, "text": "", "lan": ""}
        if subs:
            # 优先中文字幕，其次第一个
            chosen = next((s for s in subs if "zh" in (s.get("lan") or "")), subs[0])
            sub_url = chosen.get("subtitle_url") or ""
            if sub_url:
                data = await fetch_subtitle_json(sub_url)
                lines = [item.get("content", "") for item in data.get("body", [])]
                page_entry["text"] = "\n".join(lines).strip()
                page_entry["lan"] = chosen.get("lan", "")
                if page_entry["text"]:
                    result["has_subtitle"] = True
        result["pages"].append(page_entry)

    return result


def to_text(r: dict) -> str:
    head = [
        f"标题: {r['title']}",
        f"UP主: {r['author']}",
        f"分区: {r['tname']}",
        f"链接: {r['url']}",
        f"简介: {r['desc']}",
        "",
    ]
    if not r["has_subtitle"] and not r.get("asr_text"):
        head.append("[!] 该视频没有可用字幕（CC/AI）。可加 --asr 下音频本地转写。")
        return "\n".join(head)

    if r.get("asr_text"):
        head.append(f"─── 本地 ASR 转写（{r.get('asr_backend', '?')}，可能有识别误差）───")
        head.append(r["asr_text"])
        return "\n".join(head)

    for pg in r["pages"]:
        if len(r["pages"]) > 1:
            head.append(f"\n===== P{pg['page']}: {pg['part']} =====")
        if pg["text"]:
            head.append(pg["text"])
        else:
            head.append(f"[P{pg['page']} 无字幕]")
    return "\n".join(head)


def run_asr(
    bvid: str,
    model: str | None = None,
    hotwords: dict | None = None,
) -> tuple[str, str]:
    """无字幕兜底：yt-dlp 下音频 → 底层库 media_to_text 转写。

    本函数只负责“把音频搞到本地”；转写能力（平台适配/模型选择）完全委派底层库。
    返回 (文本, 后端名)。
    """
    if not shutil.which("yt-dlp"):
        sys.exit("[错误] 需要 yt-dlp：uv pip install -r requirements/asr-mac.txt（或 asr-linux.txt）")

    tmpdir = Path(tempfile.mkdtemp(prefix="bili-asr-"))
    url = f"https://www.bilibili.com/video/{bvid}"
    eprint(f"[..] yt-dlp 下载音频 {bvid}（-x 仅抽音轨，不下整片）")
    proc = subprocess.run(
        ["yt-dlp", "-x", "--audio-format", "mp3",
         "-o", str(tmpdir / "audio.%(ext)s"), url],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        eprint(proc.stderr[-400:])
        sys.exit("[错误] yt-dlp 下载失败（B 站部分格式需登录或受风控影响）。")

    audio = next(tmpdir.glob("audio.*"), None)
    if not audio:
        sys.exit("[错误] 未找到下载的音频文件。")
    eprint(f"[ok] 音频 {audio.stat().st_size / 1048576:.1f} MB，开始本地转写")

    try:
        from media_to_text import to_text as m2t
    except ImportError:
        sys.exit("[错误] 未安装底层库：cd skills && uv pip install -e ./kg-media-to-text")

    try:
        res = m2t(audio, model=model, language="zh", hotwords=hotwords)
    finally:
        # 无论转写成败都清理下载的音频，避免 /tmp 堆积
        shutil.rmtree(tmpdir, ignore_errors=True)
    return res.text, res.backend


def main():
    if len(sys.argv) < 2:
        eprint(__doc__)
        sys.exit(1)
    argv = sys.argv[2:]
    want_json = "--json" in argv
    want_asr = "--asr" in argv
    model = None
    if "--model" in argv:
        i = argv.index("--model")
        if i + 1 < len(argv):
            model = argv[i + 1]

    # 人工补充热词（可重复）：--hotword 术语，--hotword-speaker 人名
    extra_topics = [argv[i + 1] for i, a in enumerate(argv)
                    if a == "--hotword" and i + 1 < len(argv)]
    extra_speakers = [argv[i + 1] for i, a in enumerate(argv)
                      if a == "--hotword-speaker" and i + 1 < len(argv)]

    bvid = extract_bvid(sys.argv[1])
    eprint(f"[..] 抓取 {bvid} 字幕中")
    r = sync(get_transcript(bvid))
    eprint(f"[ok] has_subtitle={r['has_subtitle']}  分P数={len(r['pages'])}")

    # 降级：无字幕且显式要求 ASR 时，下音频本地转写
    if not r["has_subtitle"] and want_asr:
        # 热词：UP主名当"说话人"，标题+简介抽专名当 topics。
        # 分类很关键（实测）：人名必须进"我是…"句式才能纠对，堆成列表无效。
        hot = None
        try:
            from media_to_text import extract_hotwords
            topics = extract_hotwords(
                text=f"{r.get('title','')}\n{r.get('desc','')}", limit=10
            )
            hot = {
                "channel": [],
                "speakers": extra_speakers + ([r["author"]] if r.get("author") else []),
                "topics": extra_topics + topics,
            }
            eprint(f"[i] 热词：UP主={hot['speakers']}，专名 {len(hot['topics'])} 个")
        except ImportError:
            pass  # 底层库缺失的报错交给 run_asr 统一处理
        text, backend = run_asr(bvid, model, hot)
        r["asr_text"] = text
        r["asr_backend"] = backend
        eprint(f"[ok] ASR 完成 {len(text)} 字 via {backend}")

    if want_json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print(to_text(r))


if __name__ == "__main__":
    main()
