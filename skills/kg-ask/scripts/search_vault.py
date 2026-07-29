#!/usr/bin/env python3
"""库内检索：给关键词/问题，找出最相关的页面与片段。

为什么不用裸 grep：archive 有 975MB(6790 张图),grep 全库要 9 秒。
本脚本只索引 md 文本(全库仅 3.7MB),构建一次后查询在毫秒级。

用法:
  python search_vault.py "泛域名 证书"              # 检索(自动建/用索引)
  python search_vault.py "Agent 架构" --scope wiki   # 只搜 wiki(不含 archive 旧笔记)
  python search_vault.py "xxx" --context 3           # 每个命中显示前后 3 行
  python search_vault.py "xxx" --json                # 结构化输出
  python search_vault.py --rebuild                   # 强制重建索引
  python search_vault.py --stats                     # 看库的构成

分区语义(对应 AGENTS.md 的三层):
  wiki    AI 沉淀的知识(最高优先,含个人判断)
  index   唤醒索引(知道知识点存在)
  raw     原始资料留档
  archive 旧世界封存(整体归档,权重最低但不可忽略)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

# ---------- 库根解析（内联，保持本脚本零依赖） ----------
def _looks_like_vault(p: Path) -> bool:
    try:
        return p.is_dir() and (p / "AGENTS.md").is_file() and (p / "wiki").is_dir()
    except OSError:
        return False


def _walk_up(start: Path, limit: int = 8) -> Path | None:
    cur = start.resolve()
    for _ in range(limit):
        if _looks_like_vault(cur):
            return cur
        if cur.parent == cur:
            break
        cur = cur.parent
    return None


def find_vault() -> Path:
    """定位知识库根。优先级：KG_VAULT 环境变量 → 配置文件 → cwd 向上 → 本文件向上。"""
    import os
    v = os.environ.get("KG_VAULT")
    if v:
        p = Path(v).expanduser().resolve()
        if _looks_like_vault(p):
            return p
        sys.exit(f"[错误] KG_VAULT 指向 {p}，但那里不像知识库（需 AGENTS.md + wiki/）")

    cfg = Path.home() / ".config" / "kg-wiki" / "config.json"
    if cfg.is_file():
        try:
            v = json.loads(cfg.read_text(encoding="utf-8")).get("vault")
            if v:
                p = Path(v).expanduser().resolve()
                if _looks_like_vault(p):
                    return p
        except (json.JSONDecodeError, OSError):
            pass

    for start in (Path.cwd(), Path(__file__).parent):
        p = _walk_up(start)
        if p:
            return p

    sys.exit(
        "[错误] 找不到知识库。请用以下任一方式指定：\n"
        "  1. export KG_VAULT=/path/to/your-vault\n"
        f"  2. 写入 {cfg}：{{\"vault\": \"/path/to/your-vault\"}}\n"
        "  3. 在知识库目录内执行\n"
        "知识库需包含 AGENTS.md 和 wiki/ 目录。"
    )



VAULT = find_vault()
INDEX_FILE = VAULT / "skills" / "kg-ask" / ".vault-index.json"

# 分区权重：wiki 是蒸馏过的知识，优先级最高；archive 是旧世界，兜底用
SCOPE_WEIGHT = {"wiki": 3.0, "index": 2.0, "raw": 1.2, "archive": 0.8}
SCOPES = ("wiki", "index", "raw", "archive")


def eprint(*a, **k):
    print(*a, file=sys.stderr, **k)


def scope_of(rel: str) -> str:
    head = rel.split("/", 1)[0]
    if head in ("wiki", "raw", "archive"):
        return head
    if rel in ("index.md", "log.md", "AGENTS.md", "README.md"):
        return "index"
    return "raw"


def iter_md() -> list[Path]:
    out: list[Path] = []
    for sub in ("wiki", "raw", "archive"):
        d = VAULT / sub
        if d.is_dir():
            out.extend(d.rglob("*.md"))
    for f in ("index.md", "log.md", "AGENTS.md"):
        p = VAULT / f
        if p.is_file():
            out.append(p)
    return out


def build_index() -> dict:
    eprint("[..] 构建索引（只扫 md 文本，跳过图片）")
    t0 = time.time()
    docs = []
    for p in iter_md():
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        rel = str(p.relative_to(VAULT))
        docs.append({
            "path": rel,
            "scope": scope_of(rel),
            "title": p.stem,
            "text": text,
            "mtime": p.stat().st_mtime,
        })
    idx = {"built_at": time.time(), "vault": str(VAULT), "docs": docs}
    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
    INDEX_FILE.write_text(json.dumps(idx, ensure_ascii=False), encoding="utf-8")
    eprint(f"[ok] 索引 {len(docs)} 个文件，耗时 {time.time()-t0:.1f}s → {INDEX_FILE.name}")
    return idx


def load_index(rebuild: bool = False) -> dict:
    if rebuild or not INDEX_FILE.is_file():
        return build_index()
    try:
        idx = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return build_index()
    # 有文件比索引新就重建（简单策略，够用）
    newest = max((p.stat().st_mtime for p in iter_md()), default=0)
    if newest > idx.get("built_at", 0):
        eprint("[i] 检测到文件变更，重建索引")
        return build_index()
    return idx


def tokenize_query(q: str) -> list[str]:
    """拆查询词。中文按 2-4 字滑窗补充，提高中文召回。"""
    parts = [t for t in re.split(r"[\s\u3000,，、;；]+", q.strip()) if t]
    toks = set(parts)
    for p in parts:
        # 纯中文长词额外拆子串（"泛域名证书" → "泛域名","域名证书"...）
        if re.fullmatch(r"[\u4e00-\u9fff]{4,}", p):
            for size in (3, 2):
                for i in range(len(p) - size + 1):
                    toks.add(p[i:i + size])
    return [t for t in toks if len(t) >= 2]


def score_doc(doc: dict, toks: list[str]) -> tuple[float, dict[str, int]]:
    text_low = doc["text"].lower()
    title_low = doc["title"].lower()
    hits: dict[str, int] = {}
    score = 0.0
    for t in toks:
        tl = t.lower()
        n = text_low.count(tl)
        if n:
            hits[t] = n
            # 命中次数取对数式衰减，避免长文档霸榜
            score += 1.0 + min(n, 20) * 0.15
        if tl in title_low:
            score += 4.0  # 标题命中权重高
    if not hits:
        return 0.0, {}
    # 覆盖率加成：命中的查询词种类越多越相关
    score *= 1 + 0.5 * (len(hits) / max(len(toks), 1))
    score *= SCOPE_WEIGHT.get(doc["scope"], 1.0)
    return score, hits


def extract_snippets(text: str, toks: list[str], context: int, limit: int = 3) -> list[str]:
    lines = text.splitlines()
    low = [l.lower() for l in lines]
    picked: list[str] = []
    used: set[int] = set()
    for i, l in enumerate(low):
        if any(t.lower() in l for t in toks):
            if any(abs(i - u) <= context for u in used):
                continue
            s, e = max(0, i - context), min(len(lines), i + context + 1)
            seg = "\n".join(lines[s:e]).strip()
            if seg:
                picked.append(seg)
                used.add(i)
            if len(picked) >= limit:
                break
    return picked


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?", default=None)
    ap.add_argument("--scope", default=None,
                    help=f"限定分区，逗号分隔。可选: {','.join(SCOPES)}（默认全部）")
    ap.add_argument("--limit", type=int, default=8, help="返回文档数（默认 8）")
    ap.add_argument("--context", type=int, default=1, help="片段上下文行数（默认 1）")
    ap.add_argument("--snippets", type=int, default=3, help="每个文档最多几个片段")
    ap.add_argument("--min-score", type=float, default=8.0,
                    help="相关度门槛，低于此值视为不相关（默认 8.0）")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--rebuild", action="store_true", help="强制重建索引")
    ap.add_argument("--stats", action="store_true", help="显示库构成统计")
    args = ap.parse_args()

    idx = load_index(rebuild=args.rebuild)

    if args.stats:
        by: dict[str, int] = {}
        chars: dict[str, int] = {}
        for d in idx["docs"]:
            by[d["scope"]] = by.get(d["scope"], 0) + 1
            chars[d["scope"]] = chars.get(d["scope"], 0) + len(d["text"])
        print("# 库构成\n")
        for s in SCOPES:
            if s in by:
                print(f"  {s:8} {by[s]:>4} 个文件  {chars[s]/1024:>8.0f} KB  (权重 {SCOPE_WEIGHT[s]})")
        print(f"\n  合计     {len(idx['docs']):>4} 个文件")
        return 0

    if not args.query:
        eprint("[错误] 需要查询词。用法见 --help")
        return 2

    allow = set(x.strip() for x in args.scope.split(",")) if args.scope else set(SCOPES)
    toks = tokenize_query(args.query)
    if not toks:
        eprint("[错误] 查询词太短（需至少 2 字符）")
        return 2

    ranked = []
    for d in idx["docs"]:
        if d["scope"] not in allow:
            continue
        sc, hits = score_doc(d, toks)
        if sc > 0:
            ranked.append((sc, d, hits))
    ranked.sort(key=lambda x: -x[0])

    # 相关度门槛：过滤掉只因中文拆词碰巧命中零星片段的噪声
    weak = [r for r in ranked if r[0] < args.min_score]
    ranked = [r for r in ranked if r[0] >= args.min_score][: args.limit]

    if args.json:
        print(json.dumps({
            "query": args.query,
            "tokens": toks,
            "results": [{
                "path": d["path"], "scope": d["scope"], "title": d["title"],
                "score": round(sc, 2), "hits": hits,
                "snippets": extract_snippets(d["text"], toks, args.context, args.snippets),
            } for sc, d, hits in ranked],
        }, ensure_ascii=False, indent=2))
        return 0

    if not ranked:
        print(f"库里没找到「{args.query}」的相关沉淀。")
        if weak:
            print(f"\n（有 {len(weak)} 个文件弱命中，相关度均 < {args.min_score}，"
                  f"多半是中文拆词碰巧撞上，不算真相关。"
                  f"想看的话加 --min-score 0）")
        print("\n→ 这意味着这个知识点**还没沉淀过**。对 AI 的提示："
              "回答时要明确说明「库里没有记录，以下是我的通用知识」，不要冒充库里的内容。")
        return 0

    print(f"# 检索「{args.query}」\n")
    print(f"查询词: {', '.join(sorted(toks)[:8])}{'…' if len(toks) > 8 else ''}")
    print(f"命中 {len(ranked)} 个文件（按相关度排序，wiki 权重最高）\n")
    for sc, d, hits in ranked:
        tag = {"wiki": "★ 沉淀", "index": "◇ 索引", "raw": "· 原文", "archive": "▫ 旧笔记"}[d["scope"]]
        print(f"## {tag} {d['path']}")
        print(f"   相关度 {sc:.1f} | 命中: {', '.join(f'{k}×{v}' for k, v in list(hits.items())[:5])}")
        for seg in extract_snippets(d["text"], toks, args.context, args.snippets):
            first = seg.splitlines()[0][:150]
            print(f"   ┆ {first}")
            for more in seg.splitlines()[1:3]:
                print(f"   ┆ {more[:150]}")
            print("   ┆")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
