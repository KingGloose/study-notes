#!/usr/bin/env python3
"""按关键词搜索 B 站视频，输出 JSON（字段与 list_videos.py 一致，便于统一处理）。

用法:
  python search_videos.py <关键词> [选项]

选项:
  --order <方式>    排序：totalrank(综合,默认) / click(播放多) / pubdate(最新)
                          / dm(弹幕多) / stow(收藏多) / scores(评论多)
  --page <N>        第几页，默认 1
  --limit <N>       最多返回几条（默认 20，从结果里截取）
  --days <N>        只要最近 N 天内发布的（客户端过滤）
  --min-min <N>     最短时长（分钟），过滤太短的没肉视频
  --max-min <N>     最长时长（分钟）
  --json            仅输出 JSON（默认就是 JSON，此参数保留兼容）

示例:
  python search_videos.py "Rust 异步" --order click --limit 10
  python search_videos.py "前端性能优化" --days 180 --min-min 8
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta

from bilibili_api import search, sync
from bilibili_api.search import SearchObjectType, OrderVideo
from _common import load_credential, select_http_client, eprint

ORDER_MAP = {
    "totalrank": OrderVideo.TOTALRANK,   # 综合排序
    "click": OrderVideo.CLICK,           # 播放多
    "pubdate": OrderVideo.PUBDATE,       # 最新发布
    "dm": OrderVideo.DM,                 # 弹幕多
    "stow": OrderVideo.STOW,             # 收藏多
    "scores": OrderVideo.SCORES,         # 评论多
}


def strip_em(s: str) -> str:
    """B 站搜索结果的标题带 <em class="keyword"> 高亮标签，去掉。"""
    return re.sub(r"</?em[^>]*>", "", s or "").strip()


def fmt_duration(dur) -> tuple[str, int]:
    """B 站搜索返回的 duration 是 'MM:SS' 或 'HH:MM:SS' 字符串。返回 (显示值, 总秒数)。"""
    if isinstance(dur, (int, float)):
        total = int(dur)
    else:
        parts = [int(p) for p in str(dur).split(":") if p.strip().isdigit()]
        total = 0
        for p in parts:
            total = total * 60 + p
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    disp = f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"
    return disp, total


async def do_search(cred, keyword: str, order: str, page: int) -> list[dict]:
    data = await search.search_by_type(
        keyword=keyword,
        search_type=SearchObjectType.VIDEO,
        order_type=ORDER_MAP[order],
        page=page,
    )
    out = []
    for it in (data or {}).get("result", []) or []:
        if it.get("type") != "video":
            continue
        disp, total_sec = fmt_duration(it.get("duration", 0))
        pub_ts = it.get("pubdate") or 0
        out.append({
            "title": strip_em(it.get("title", "")),
            "bvid": it.get("bvid", ""),
            "author": it.get("author", ""),
            "duration": disp,
            "duration_sec": total_sec,
            "url": f"https://www.bilibili.com/video/{it.get('bvid','')}",
            "intro": strip_em(it.get("description", ""))[:200],
            "tname": it.get("typename", ""),
            "play": it.get("play", 0),
            "danmaku": it.get("video_review", 0),
            "pubdate": datetime.fromtimestamp(pub_ts).strftime("%Y-%m-%d") if pub_ts else "",
            "_pub_ts": pub_ts,
        })
    return out


def main() -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("keyword", help="搜索关键词")
    ap.add_argument("--order", default="totalrank", choices=list(ORDER_MAP),
                    help="排序方式，默认 totalrank(综合)")
    ap.add_argument("--page", type=int, default=1)
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--days", type=int, default=None, help="只要最近 N 天发布的")
    ap.add_argument("--min-min", type=int, default=None, help="最短时长(分钟)")
    ap.add_argument("--max-min", type=int, default=None, help="最长时长(分钟)")
    ap.add_argument("--json", action="store_true", help="（默认即 JSON，兼容用）")
    args = ap.parse_args()

    select_http_client()
    cred = load_credential()

    eprint(f"[..] 搜索「{args.keyword}」order={args.order} page={args.page}")
    try:
        results = sync(do_search(cred, args.keyword, args.order, args.page))
    except Exception as e:
        eprint(f"[错误] 搜索失败（{type(e).__name__}）: {e}")
        return 2

    raw_n = len(results)

    # 客户端过滤
    if args.days is not None:
        cutoff = (datetime.now() - timedelta(days=args.days)).timestamp()
        results = [r for r in results if r["_pub_ts"] >= cutoff]
    if args.min_min is not None:
        results = [r for r in results if r["duration_sec"] >= args.min_min * 60]
    if args.max_min is not None:
        results = [r for r in results if r["duration_sec"] <= args.max_min * 60]

    results = results[: args.limit]
    for r in results:
        r.pop("_pub_ts", None)

    eprint(f"[ok] 搜到 {raw_n} 条，过滤后输出 {len(results)} 条")
    if not results:
        eprint("[i] 无结果。可放宽 --days / --min-min / --max-min，或换关键词、翻页。")
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
