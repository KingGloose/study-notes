#!/usr/bin/env python3
"""抓取指定视频的字幕并输出为纯文本。

用法:
  python get_transcript.py <bvid或视频URL> [--json]

策略:
  1. 拿视频基本信息（标题/UP主/分区/简介/分P）
  2. 逐个分P取 CC/AI 字幕（B 站字幕是一个 JSON URL，内含带时间戳的文本）
  3. 有字幕 → 输出纯文本；无字幕 → 明确标注 no_subtitle（Whisper 兜底后续再加）

默认输出人类可读文本到 stdout；加 --json 输出结构化 JSON。
"""
import asyncio
import json
import re
import sys

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
        r = cffi_requests.get(
            url,
            headers={"Referer": "https://www.bilibili.com"},
            impersonate="chrome",
            timeout=30,
        )
        r.raise_for_status()
        return r.json()

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
    if not r["has_subtitle"]:
        head.append("[!] 该视频没有可用字幕（CC/AI）。如需内容需后续接入 Whisper 兜底转写。")
        return "\n".join(head)
    for pg in r["pages"]:
        if len(r["pages"]) > 1:
            head.append(f"\n===== P{pg['page']}: {pg['part']} =====")
        if pg["text"]:
            head.append(pg["text"])
        else:
            head.append(f"[P{pg['page']} 无字幕]")
    return "\n".join(head)


def main():
    if len(sys.argv) < 2:
        eprint(__doc__)
        sys.exit(1)
    want_json = "--json" in sys.argv[2:]
    bvid = extract_bvid(sys.argv[1])
    eprint(f"[..] 抓取 {bvid} 字幕中")
    r = sync(get_transcript(bvid))
    eprint(f"[ok] has_subtitle={r['has_subtitle']}  分P数={len(r['pages'])}")
    if want_json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print(to_text(r))


if __name__ == "__main__":
    main()
