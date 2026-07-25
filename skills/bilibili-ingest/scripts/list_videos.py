#!/usr/bin/env python3
"""拉取稍后再看 / 收藏夹的视频列表，输出 JSON 到 stdout。

用法:
  python list_videos.py toview                 # 稍后再看
  python list_videos.py favlist                # 列出所有收藏夹（拿 media_id）
  python list_videos.py fav <media_id> [页数]  # 某个收藏夹的内容，默认第 1 页

输出: JSON 数组，每项含 title / bvid / author / duration / url / intro（收藏夹有）。
供上层 AI 读取后做筛选，不做业务判断。
"""
import asyncio
import json
import sys

from bilibili_api import user, favorite_list, sync
from _common import load_credential, select_http_client, eprint


def _fmt_duration(sec):
    try:
        sec = int(sec)
    except (TypeError, ValueError):
        return ""
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


async def list_toview(cred):
    data = await user.get_toview_list(credential=cred)
    out = []
    for it in data.get("list", []):
        out.append({
            "title": it.get("title", ""),
            "bvid": it.get("bvid", ""),
            "author": it.get("owner", {}).get("name", ""),
            "duration": _fmt_duration(it.get("duration")),
            "url": f"https://www.bilibili.com/video/{it.get('bvid','')}",
            "intro": (it.get("desc") or "").strip()[:200],
            "tname": it.get("tname", ""),  # 分区名，用于筛选编程/科普类
        })
    return out


async def list_favlists(cred):
    """列出当前用户的所有收藏夹，返回 [{id, title, media_count}]。"""
    me = await user.get_self_info(credential=cred)
    uid = me["mid"]
    data = await favorite_list.get_video_favorite_list(uid=uid, credential=cred)
    out = []
    for fl in (data or {}).get("list", []):
        out.append({
            "media_id": fl.get("id"),
            "title": fl.get("title", ""),
            "media_count": fl.get("media_count", 0),
        })
    return out


async def list_fav_content(cred, media_id, page):
    data = await favorite_list.get_video_favorite_list_content(
        media_id=int(media_id), page=int(page), credential=cred
    )
    out = []
    for it in (data or {}).get("medias", []) or []:
        out.append({
            "title": it.get("title", ""),
            "bvid": it.get("bvid", ""),
            "author": it.get("upper", {}).get("name", ""),
            "duration": _fmt_duration(it.get("duration")),
            "url": f"https://www.bilibili.com/video/{it.get('bvid','')}",
            "intro": (it.get("intro") or "").strip()[:200],
        })
    return out


def main():
    if len(sys.argv) < 2:
        eprint(__doc__)
        sys.exit(1)

    select_http_client()
    cred = load_credential()
    mode = sys.argv[1]

    if mode == "toview":
        result = sync(list_toview(cred))
    elif mode == "favlist":
        result = sync(list_favlists(cred))
    elif mode == "fav":
        if len(sys.argv) < 3:
            sys.exit("用法: python list_videos.py fav <media_id> [页数]")
        page = sys.argv[3] if len(sys.argv) > 3 else 1
        result = sync(list_fav_content(cred, sys.argv[2], page))
    else:
        sys.exit(f"未知模式: {mode}（可选 toview / favlist / fav）")

    eprint(f"[ok] {mode} 共 {len(result)} 条")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
