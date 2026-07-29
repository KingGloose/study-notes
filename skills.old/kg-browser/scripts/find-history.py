#!/usr/bin/env python3
"""Find Chrome site candidates from local bookmarks and history."""

from __future__ import annotations

import argparse
import json
import shutil
import sqlite3
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


CHROME_EPOCH = datetime(1601, 1, 1, tzinfo=timezone.utc)
DEFAULT_CHROME_HOME = (
    Path.home() / "Library" / "Application Support" / "Google" / "Chrome"
)


def chrome_time_to_iso(value: int | None) -> str | None:
    if not value:
        return None
    return (CHROME_EPOCH + timedelta(microseconds=int(value))).isoformat()


def profile_dirs(chrome_home: Path) -> list[Path]:
    candidates: list[Path] = []

    default_profile = chrome_home / "Default"
    if default_profile.is_dir():
        candidates.append(default_profile)

    if chrome_home.is_dir():
        candidates.extend(
            path
            for path in sorted(chrome_home.glob("Profile *"))
            if path.is_dir()
        )

    return candidates


def normalize_text(value: str | None) -> str:
    """标准化文本：转小写并移除空格，便于模糊匹配。"""
    return (value or "").casefold().replace(" ", "")


def expand_keywords(keyword: str) -> list[str]:
    """扩展关键词，支持分词。

    例如：
    - "OA 系统" -> ["oa系统", "oa", "系统"]
    - "综合平台" -> ["综合平台", "综合", "平台"]
    - "转转办公" -> ["转转办公", "转转", "办公"]

    设计原则：
    - 只做通用的分词处理，不做同义词映射
    - 用户可以通过输入更精确的关键词来找到目标站点
    - 保持工具简单、可预测
    """
    normalized = normalize_text(keyword)
    keywords = [normalized]

    # 按空格分词
    original_parts = keyword.strip().split()
    if len(original_parts) > 1:
        # 添加每个分词的标准化版本
        keywords.extend([normalize_text(part) for part in original_parts])

    # 去重并保持顺序
    seen = set()
    result = []
    for kw in keywords:
        if kw and kw not in seen:
            seen.add(kw)
            result.append(kw)

    return result


def matches_keyword(keyword: str, title: str | None, url: str | None) -> bool:
    """检查标题或 URL 是否匹配关键词（支持多关键词 OR 匹配）。"""
    keywords = expand_keywords(keyword)
    title_norm = normalize_text(title)
    url_norm = normalize_text(url)

    return any(
        kw in title_norm or kw in url_norm
        for kw in keywords
    )


def calculate_match_score(keyword: str, title: str | None, url: str | None) -> float:
    """计算匹配分数，用于排序。

    评分规则：
    - 完整关键词匹配 > 分词匹配
    - 标题匹配 > URL 匹配
    - 分词越靠前权重越高
    """
    keywords = expand_keywords(keyword)
    title_norm = normalize_text(title)
    url_norm = normalize_text(url)
    original_keyword = normalize_text(keyword)

    score = 0.0

    # 完整关键词匹配（最高权重）
    if original_keyword in title_norm:
        score += 10.0
    if original_keyword in url_norm:
        score += 5.0

    # 分词匹配（中等权重）
    for i, kw in enumerate(keywords):
        if kw == original_keyword:
            continue
        weight = 3.0 / (i + 1)  # 越靠前权重越高
        if kw in title_norm:
            score += weight
        if kw in url_norm:
            score += weight * 0.5

    return score


def walk_bookmark_node(
    node: dict[str, Any],
    profile: str,
    keyword: str,
    path_parts: list[str],
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    node_type = node.get("type")
    name = node.get("name") or ""

    if node_type == "url":
        url = node.get("url") or ""
        if matches_keyword(keyword, name, url):
            results.append(
                {
                    "title": name,
                    "url": url,
                    "source": "bookmark",
                    "profile": profile,
                    "bookmark_path": " / ".join(path_parts),
                    "last_visit_time": None,
                    "match_score": calculate_match_score(keyword, name, url),
                }
            )
        return results

    children = node.get("children") or []
    next_path = path_parts + ([name] if name else [])
    for child in children:
        if isinstance(child, dict):
            results.extend(walk_bookmark_node(child, profile, keyword, next_path))

    return results


def read_bookmarks(profile_dir: Path, keyword: str) -> list[dict[str, Any]]:
    bookmarks_file = profile_dir / "Bookmarks"
    if not bookmarks_file.is_file():
        return []

    try:
        data = json.loads(bookmarks_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Warning: 无法读取书签 {bookmarks_file}: {error}", file=sys.stderr)
        return []

    roots = data.get("roots") or {}
    results: list[dict[str, Any]] = []
    for root_name, root in roots.items():
        if isinstance(root, dict):
            results.extend(
                walk_bookmark_node(root, profile_dir.name, keyword, [root_name])
            )
    return results


def copy_history_database(history_file: Path, temp_dir: Path) -> Path | None:
    target = temp_dir / f"{history_file.parent.name}-History"
    try:
        shutil.copy2(history_file, target)
    except OSError as error:
        print(f"Warning: 无法复制历史记录 {history_file}: {error}", file=sys.stderr)
        return None
    return target


def read_history(
    profile_dir: Path,
    keyword: str,
    per_profile_limit: int,
) -> list[dict[str, Any]]:
    history_file = profile_dir / "History"
    if not history_file.is_file():
        return []

    with tempfile.TemporaryDirectory(prefix="chrome-history-") as temp_name:
        temp_history = copy_history_database(history_file, Path(temp_name))
        if not temp_history:
            return []

        try:
            connection = sqlite3.connect(f"file:{temp_history}?mode=ro", uri=True)
        except sqlite3.Error as error:
            print(f"Warning: 无法打开历史记录 {history_file}: {error}", file=sys.stderr)
            return []

        with connection:
            # 扩展关键词以支持模糊匹配
            keywords = expand_keywords(keyword)
            # 构建 SQL 查询条件（OR 连接多个关键词）
            # 注意：使用 lower() 可以利用 SQLite 的 NOCASE collation
            conditions = []
            params = []
            for kw in keywords:
                # 使用简单的 LIKE 查询，避免在 SQL 中使用 replace()
                # 空格处理在 Python 层面的 matches_keyword 中完成
                conditions.append("(lower(title) LIKE ? OR lower(url) LIKE ?)")
                params.extend([f"%{kw}%", f"%{kw}%"])

            where_clause = " OR ".join(conditions)
            params.append(per_profile_limit)

            try:
                rows = connection.execute(
                    f"""
                    SELECT title, url, last_visit_time
                    FROM urls
                    WHERE {where_clause}
                    ORDER BY last_visit_time DESC
                    LIMIT ?
                    """,
                    params,
                ).fetchall()
            except sqlite3.Error as error:
                print(
                    f"Warning: 无法查询历史记录 {history_file}: {error}",
                    file=sys.stderr,
                )
                return []

    return [
        {
            "title": title or "",
            "url": url or "",
            "source": "history",
            "profile": profile_dir.name,
            "bookmark_path": None,
            "last_visit_time": chrome_time_to_iso(last_visit_time),
            "match_score": calculate_match_score(keyword, title, url),
        }
        for title, url, last_visit_time in rows
        if matches_keyword(keyword, title, url)
    ]


def dedupe_and_sort(candidates: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    """去重并排序候选结果。

    排序优先级：
    1. 匹配分数（越高越好）
    2. 来源类型（书签 > 历史记录）
    3. 访问时间（越近越好）
    """
    best_by_url: dict[str, dict[str, Any]] = {}

    for candidate in candidates:
        url = candidate.get("url")
        if not url:
            continue

        existing = best_by_url.get(url)
        if not existing:
            best_by_url[url] = candidate
            continue

        # 保留来源为书签的记录，或匹配分数更高的记录
        if existing["source"] == "history" and candidate["source"] == "bookmark":
            best_by_url[url] = candidate
        elif candidate.get("match_score", 0) > existing.get("match_score", 0):
            best_by_url[url] = candidate

    def sort_key(candidate: dict[str, Any]) -> tuple[float, int, str]:
        # 匹配分数（取负值，因为要降序）
        match_score = -(candidate.get("match_score") or 0.0)
        # 来源类型（书签优先）
        source_rank = 0 if candidate["source"] == "bookmark" else 1
        # 访问时间（越近越好，取反转字符串实现降序）
        last_visit_time = candidate.get("last_visit_time") or ""
        time_sort = "" if source_rank == 0 else _invert_string(last_visit_time)

        return (match_score, source_rank, time_sort)

    return sorted(best_by_url.values(), key=sort_key)[:limit]


def _invert_string(value: str) -> str:
    return "".join(chr(0x10FFFF - ord(char)) for char in value)


def find_candidates(
    chrome_home: Path, keywords: list[str], limit: int
) -> list[dict[str, Any]]:
    """查找候选 URL。

    Args:
        chrome_home: Chrome 用户数据根目录
        keywords: 关键词列表，支持多个关键词 OR 匹配
        limit: 最多返回的候选数量

    优化说明：
    - 对每个 profile 只读取一次书签和历史记录
    - 使用所有关键词进行匹配，避免重复查询
    """
    profiles = profile_dirs(chrome_home)
    per_profile_limit = max(limit * len(keywords) * 2, 50)  # 根据关键词数量调整限制
    candidates: list[dict[str, Any]] = []

    for profile in profiles:
        # 对每个 profile，使用所有关键词进行一次性查询
        for keyword in keywords:
            candidates.extend(read_bookmarks(profile, keyword))
            candidates.extend(read_history(profile, keyword, per_profile_limit))

    return dedupe_and_sort(candidates, limit)


# 噪声 URL 特征：搜索页、登录页、站点首页等（找"看过的文章"时无用）
_NOISE_PATTERNS = (
    "/search", "?q=", "&q=", "/signin", "/login", "/logout", "/auth",
    "google.com/search", "bing.com/search", "baidu.com/s?",
    "/tardis/", "/landing/",
)


def is_probably_article(url: str, title: str | None) -> bool:
    """粗判这个 URL 是否像一篇具体内容，而非搜索/登录/首页。

    宁可漏掉也不要误留噪声——AI 拿到候选后还会和主人确认。
    """
    u = (url or "").lower()
    if any(p in u for p in _NOISE_PATTERNS):
        return False
    # 站点首页（路径为空或只有 /）通常不是具体文章
    from urllib.parse import urlparse
    try:
        path = urlparse(u).path.rstrip("/")
    except ValueError:
        return False
    if not path:
        return False
    return True


def filter_candidates(
    candidates: list[dict[str, Any]], days: int | None, articles_only: bool
) -> list[dict[str, Any]]:
    out = candidates
    if articles_only:
        out = [c for c in out if is_probably_article(c.get("url", ""), c.get("title"))]
    if days is not None:
        from datetime import datetime, timedelta, timezone
        cutoff = datetime.now(timezone.utc) - timedelta(days=days)
        kept = []
        for c in out:
            t = c.get("last_visit_time")
            if not t:  # 书签没有访问时间，保留
                kept.append(c)
                continue
            try:
                if datetime.fromisoformat(t) >= cutoff:
                    kept.append(c)
            except (ValueError, TypeError):
                kept.append(c)
        out = kept
    return out


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="从本地 Chrome 历史记录和书签中按关键词查找候选 URL。"
    )
    parser.add_argument(
        "keyword",
        nargs="?",
        help="站点关键词，例如：OA 系统。如果使用 --keywords，此参数可省略。",
    )
    parser.add_argument(
        "--keywords",
        nargs="+",
        help="多个关键词（空格分隔），例如：--keywords OA 办公 审批。优先级高于单个 keyword 参数。",
    )
    parser.add_argument(
        "--chrome-home",
        default=str(DEFAULT_CHROME_HOME),
        help="Chrome 用户数据根目录，默认读取 macOS Google Chrome 路径。",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="最多输出候选数量，默认 10。",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=None,
        help="只要最近 N 天访问过的（找不久前看过的内容时用）。",
    )
    parser.add_argument(
        "--articles-only",
        action="store_true",
        help="过滤掉搜索页/登录页/首页等噪声，只留看起来像文章的 URL。",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="以缩进 JSON 输出。",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    # 优先使用 --keywords 参数，否则使用单个 keyword 参数
    if args.keywords:
        keywords = [kw.strip() for kw in args.keywords if kw.strip()]
    elif args.keyword:
        keywords = [args.keyword.strip()]
    else:
        print("Error: 必须提供 keyword 或 --keywords 参数", file=sys.stderr)
        return 2

    if not keywords:
        print("Error: keyword 不能为空", file=sys.stderr)
        return 2

    chrome_home = Path(args.chrome_home).expanduser()
    # 多拿一些再过滤，避免过滤后不够 limit 条
    raw_limit = max(args.limit, 1)
    if args.articles_only or args.days is not None:
        raw_limit = max(raw_limit * 4, 40)
    candidates = find_candidates(chrome_home, keywords, raw_limit)
    candidates = filter_candidates(candidates, args.days, args.articles_only)[: max(args.limit, 1)]
    payload = {
        "query": " ".join(keywords) if len(keywords) > 1 else keywords[0],
        "keywords": keywords,
        "chrome_home": str(chrome_home),
        "filters": {"days": args.days, "articles_only": args.articles_only},
        "candidates": candidates,
    }

    indent = 2 if args.pretty else None
    print(json.dumps(payload, ensure_ascii=False, indent=indent))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
