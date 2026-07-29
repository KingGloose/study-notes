#!/usr/bin/env python3
"""YouTube 视频摄入：优先白拿官方/自动字幕（L0），无字幕才本地 ASR（L1）。

用法:
  python ingest_video.py <YouTube链接或视频ID>
  python ingest_video.py <链接> --lang zh-Hans,en    # 指定字幕语言优先级
  python ingest_video.py <链接> --asr                # 强制走本地转写（不用字幕）
  python ingest_video.py <链接> --stdout             # 只预览不落盘

策略:
  1. yt-dlp 拿元信息（标题/频道/时长/简介/上传日期）
  2. 按语言优先级**逐个**尝试字幕（人工字幕优先于自动字幕）
     注意：一次请求多语言易触发 YouTube 429 限流，故逐个试、拿到就停
  3. 有字幕 → 清理 VTT（去内联时间标签/去重复行）输出纯文本
     无字幕或 --asr → 下音频，调底层库 media_to_text 本地转写
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

# 库根：优先 KG_VAULT 环境变量 / ~/.config/kg-wiki/config.json，
# 否则从 cwd 或本文件位置向上找（含 AGENTS.md + wiki/ 的目录）
from media_to_text import find_vault
REPO_ROOT = find_vault(__file__)
RAW_DIR = REPO_ROOT / "raw"

# 默认字幕语言优先级：中文 → 英文 → 英文自动翻译
DEFAULT_LANGS = ["zh-Hans", "zh-CN", "zh", "en", "en-orig"]


def eprint(*a, **k):
    print(*a, file=sys.stderr, **k)


def sanitize(name: str) -> str:
    name = re.sub(r"[\\/:*?\"<>|\n\r\t]", "_", name).strip()
    return name[:60] or "video"


def require_ytdlp() -> None:
    if not shutil.which("yt-dlp"):
        sys.exit("[错误] 需要 yt-dlp：uv pip install -r requirements/asr-mac.txt（或 asr-linux.txt）")


def fmt_duration(sec) -> str:
    try:
        sec = int(sec)
    except (TypeError, ValueError):
        return ""
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def get_info(url: str) -> dict:
    """用 yt-dlp --dump-json 拿元信息（不下载）。"""
    proc = subprocess.run(
        ["yt-dlp", "--dump-json", "--skip-download", "--no-warnings", url],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        eprint(proc.stderr[-500:])
        sys.exit("[错误] 获取视频信息失败（链接无效/视频私有/需登录/受地区限制）。")
    try:
        d = json.loads(proc.stdout.splitlines()[0])
    except (json.JSONDecodeError, IndexError) as e:
        sys.exit(f"[错误] 解析视频信息失败: {e}")

    upload = d.get("upload_date") or ""
    if len(upload) == 8:
        upload = f"{upload[:4]}-{upload[4:6]}-{upload[6:]}"
    return {
        "id": d.get("id", ""),
        "title": d.get("title", ""),
        "channel": d.get("channel") or d.get("uploader", ""),
        "duration": fmt_duration(d.get("duration")),
        "duration_sec": d.get("duration") or 0,
        "upload_date": upload,
        "url": d.get("webpage_url") or url,
        "description": (d.get("description") or "").strip(),
        "view_count": d.get("view_count"),
        "subtitles": sorted((d.get("subtitles") or {}).keys()),
        "auto_captions": sorted((d.get("automatic_captions") or {}).keys()),
    }


def clean_vtt(vtt: str) -> str:
    """VTT → 纯文本。处理 YouTube 自动字幕的两个特性：
    1. 内联时间标签 <00:00:19.039><c>word</c>
    2. 滚动字幕导致的大量重复行
    """
    lines_out: list[str] = []
    for raw in vtt.splitlines():
        line = raw.strip()
        if not line or line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        if "-->" in line:  # 时间轴行
            continue
        if re.fullmatch(r"\d+", line):  # 序号行
            continue
        # 去内联时间标签与 <c> 标签
        line = re.sub(r"<\d{2}:\d{2}:\d{2}\.\d{3}>", "", line)
        line = re.sub(r"</?c[^>]*>", "", line)
        line = re.sub(r"<[^>]+>", "", line).strip()
        if not line:
            continue
        # 去连续重复（滚动字幕会把同句重复输出）
        if lines_out and lines_out[-1] == line:
            continue
        # 去“上一行是本行前缀”的滚动残留
        if lines_out and line.startswith(lines_out[-1]):
            lines_out[-1] = line
            continue
        lines_out.append(line)
    return "\n".join(lines_out).strip()


def try_subtitles(url: str, langs: list[str]) -> tuple[str, str] | None:
    """按优先级逐个尝试字幕。返回 (纯文本, 实际语言标记) 或 None。

    逐个而非一次多语言：一次请求多个语言容易触发 YouTube 429 限流（实测）。
    每种语言先试人工字幕(--write-subs)，再试自动字幕(--write-auto-subs)。
    """
    tmpdir = Path(tempfile.mkdtemp(prefix="yt-sub-"))
    try:
        for lang in langs:
            for auto_flag, tag in (("--write-subs", "人工"), ("--write-auto-subs", "自动")):
                proc = subprocess.run(
                    ["yt-dlp", auto_flag, "--sub-langs", lang, "--sub-format", "vtt",
                     "--skip-download", "--no-warnings",
                     "-o", str(tmpdir / "%(id)s"), url],
                    capture_output=True, text=True,
                )
                files = list(tmpdir.glob("*.vtt"))
                if files:
                    text = clean_vtt(files[0].read_text(encoding="utf-8", errors="ignore"))
                    if text:
                        return text, f"{lang}({tag})"
                    for f in files:
                        f.unlink(missing_ok=True)
                if "429" in (proc.stderr or ""):
                    eprint(f"[warn] {lang} 触发 YouTube 限流(429)，跳过该语言")
                    break
        return None
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def run_asr(url: str, model: str | None) -> tuple[str, str]:
    """无字幕兜底：yt-dlp 抽音轨 → 底层库转写。"""
    tmpdir = Path(tempfile.mkdtemp(prefix="yt-asr-"))
    try:
        eprint("[..] yt-dlp 下载音频（-x 仅抽音轨）")
        proc = subprocess.run(
            ["yt-dlp", "-x", "--audio-format", "mp3", "--no-warnings",
             "-o", str(tmpdir / "audio.%(ext)s"), url],
            capture_output=True, text=True,
        )
        if proc.returncode != 0:
            eprint(proc.stderr[-400:])
            sys.exit("[错误] 音频下载失败。")
        audio = next(tmpdir.glob("audio.*"), None)
        if not audio:
            sys.exit("[错误] 未找到下载的音频文件。")
        eprint(f"[ok] 音频 {audio.stat().st_size / 1048576:.1f} MB，开始本地转写")
        try:
            from media_to_text import to_text
        except ImportError:
            sys.exit("[错误] 未安装底层库：cd skills && uv pip install -e ./kg-media-to-text")
        res = to_text(audio, model=model)
        return res.text, res.backend
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def build_markdown(info: dict, body: str, source_tag: str) -> str:
    lines = [
        f"# {info['title']}",
        "",
        f"- 频道: {info['channel']}",
        f"- 时长: {info['duration']}",
        f"- 上传日期: {info['upload_date']}",
        f"- 链接: {info['url']}",
        f"- 文本来源: {source_tag}",
        f"- 摄入日期: {datetime.now().strftime('%Y-%m-%d')}",
    ]
    if info.get("view_count"):
        lines.insert(4, f"- 播放量: {info['view_count']}")
    lines += ["", "---", "", "## 简介", "", info["description"] or "（无简介）",
              "", "---", "", f"## 正文（{source_tag}）", "", body]
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url", help="YouTube 链接或视频 ID")
    ap.add_argument("--lang", default=None,
                    help=f"字幕语言优先级，逗号分隔。默认: {','.join(DEFAULT_LANGS)}")
    ap.add_argument("--asr", action="store_true", help="跳过字幕，直接本地转写")
    ap.add_argument("--model", default=None, help="指定 ASR 模型")
    ap.add_argument("--stdout", action="store_true", help="只打到 stdout，不落盘")
    ap.add_argument("--out", default=None, help="自定义输出路径")
    args = ap.parse_args()

    require_ytdlp()
    url = args.url
    if not url.startswith("http") and re.fullmatch(r"[\w-]{11}", url):
        url = f"https://www.youtube.com/watch?v={url}"

    eprint(f"[..] 获取视频信息 {url}")
    info = get_info(url)
    eprint(f"[ok] 《{info['title']}》| {info['channel']} | {info['duration']}")
    eprint(f"[i] 人工字幕语言: {', '.join(info['subtitles'][:8]) or '无'}"
           f" | 自动字幕: {len(info['auto_captions'])} 种")

    body, source_tag = "", ""
    if not args.asr:
        langs = [x.strip() for x in args.lang.split(",")] if args.lang else DEFAULT_LANGS
        eprint(f"[..] 尝试字幕（优先级: {', '.join(langs)}）")
        got = try_subtitles(url, langs)
        if got:
            body, lang_tag = got
            source_tag = f"字幕 {lang_tag}"
            eprint(f"[ok] 拿到字幕 {len(body)} 字符 — {lang_tag}（L0 白拿，未消耗算力）")
        else:
            eprint("[i] 未取到可用字幕")

    if not body:
        if not args.asr:
            eprint("[..] 降级到本地 ASR")
        text, backend = run_asr(url, args.model)
        body, source_tag = text, f"本地 ASR（{backend}，可能有识别误差）"
        eprint(f"[ok] 转写完成 {len(body)} 字符 via {backend}")

    if not body.strip():
        eprint("[错误] 未获得任何文本内容。")
        return 3

    content = build_markdown(info, body, source_tag)

    if args.stdout:
        sys.stdout.write(content)
        return 0

    out = Path(args.out).expanduser() if args.out else (
        RAW_DIR / f"yt-{info['id']}-{sanitize(info['title'])}.md"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    eprint(f"[ok] 已写入 {out}")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
