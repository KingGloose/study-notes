#!/usr/bin/env python3
"""学习笔记库健康检查：找出知识网的断点与账目不一致。

用法:
  python lint_vault.py              # 全部检查，人类可读报告
  python lint_vault.py --json       # 结构化输出
  python lint_vault.py --only orphan,deadlink   # 只跑指定检查

检查项:
  deadlink   死链：[[xxx]] 指向不存在的页/文件
  orphan     孤儿页：没有任何其他 wiki 页链接到它（知识网断点）
  rawlink    raw 原文未被任何 wiki 页引用（存了但没用上）
  indexsync  wiki 有页但 index.md 没提到对应领域/关键词
  logsync    wiki 页没在 log.md 里留下痕迹（无摄入记录）
  empty      内容过短的页（可能是没写完的坑）

退出码：0 = 无问题；1 = 有发现（供 CI/脚本判断）
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
WIKI = VAULT / "wiki"
RAW = VAULT / "raw"
INDEX = VAULT / "index.md"
LOG = VAULT / "log.md"

LINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
MIN_CHARS = 400  # 低于此字符数视为“可能没写完”


def eprint(*a, **k):
    print(*a, file=sys.stderr, **k)


def wiki_pages() -> list[Path]:
    return sorted(WIKI.rglob("*.md")) if WIKI.is_dir() else []


def page_key(p: Path) -> str:
    """页的规范标识：领域/页名（不含 .md）。"""
    return str(p.relative_to(WIKI).with_suffix(""))


def resolve_link(target: str, from_page: Path) -> Path | None:
    """把双链目标解析成实际文件路径。支持三种写法：
    1. 纯页名          [[同源策略与 CORS]]        → 在 wiki 下按文件名找
    2. 相对路径        [[../网络/同源策略与 CORS]] → 相对 from_page 所在目录
    3. 指向 raw 等     [[../../raw/xxx.md]]
    找不到返回 None。
    """
    t = target.strip()
    base = from_page.parent

    cands: list[Path] = []
    if "/" in t:
        # 相对路径写法
        cands.append((base / t))
        cands.append((base / t).with_suffix(".md"))
        cands.append(VAULT / t)
        cands.append((VAULT / t).with_suffix(".md"))
    else:
        # 纯页名：全 wiki 搜同名文件
        for p in wiki_pages():
            if p.stem == t:
                return p
        cands.append((base / t).with_suffix(".md"))

    for c in cands:
        try:
            if c.exists() and c.is_file():
                return c.resolve()
        except OSError:
            continue
    return None


def collect_links() -> tuple[dict[str, list[tuple[str, str]]], list[dict]]:
    """扫所有 wiki 页的双链。

    返回 (被链接映射, 死链列表)
      被链接映射: {被指向页的 page_key: [(来源页, 原始链接文本)]}
    """
    inbound: dict[str, list[tuple[str, str]]] = {}
    dead: list[dict] = []
    for p in wiki_pages():
        try:
            text = p.read_text(encoding="utf-8")
        except OSError as e:
            dead.append({"page": page_key(p), "link": "(读取失败)", "reason": str(e)})
            continue
        for m in LINK_RE.finditer(text):
            target = m.group(1)
            resolved = resolve_link(target, p)
            if resolved is None:
                dead.append({"page": page_key(p), "link": target})
            else:
                try:
                    if WIKI in resolved.parents:
                        k = page_key(resolved)
                        inbound.setdefault(k, []).append((page_key(p), target))
                except Exception:
                    pass
    return inbound, dead


def check_orphan(inbound) -> list[dict]:
    out = []
    for p in wiki_pages():
        k = page_key(p)
        if not inbound.get(k):
            out.append({"page": k})
    return out


def check_rawlink() -> list[dict]:
    """raw 文件是否被任何 wiki 页引用（双链或纯文本提到文件名）。"""
    if not RAW.is_dir():
        return []
    all_wiki_text = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore") for p in wiki_pages()
    )
    log_text = LOG.read_text(encoding="utf-8", errors="ignore") if LOG.is_file() else ""
    out = []
    for f in sorted(RAW.glob("*.md")):
        name = f.stem
        if name in all_wiki_text or f.name in all_wiki_text:
            continue
        out.append({"raw": f.name, "in_log": name in log_text or f.name in log_text})
    return out


def _mentioned(stem: str, haystack: str, haystack_low: str) -> bool:
    """判断页名是否在某文本里被“提到过”。

    三级匹配，从严到宽：
    1. 页名全称
    2. 按分隔符拆词（对含空白/标点的页名有效）
    3. 中文子串滑窗（中文页名往往无空白，如「泛域名与相关概念辨析」，
       index 里只写「泛域名」，故取长度>=3 的连续子串去碰）
    """
    if stem in haystack:
        return True

    tokens = [t for t in re.split(r"[\s\u3000/\-—·:：、（）()\[\]]+", stem) if len(t) >= 2]
    if any(t.lower() in haystack_low for t in tokens):
        return True

    # 中文子串滑窗：只对纯中文段做，避免英文短词误匹配
    for seg in re.findall(r"[\u4e00-\u9fff]{3,}", stem):
        for size in range(len(seg), 2, -1):
            for i in range(len(seg) - size + 1):
                if seg[i:i + size] in haystack:
                    return True
    return False


def check_indexsync() -> list[dict]:
    """wiki 页是否在 index.md 里有唤醒条目。

    index 的写法是“关键词”而非页名全称（页名「QuillJs 换行与 embed 光标问题」，
    index 里只写「QuillJs」），所以用宽松的 _mentioned 判定，宁可漏报不要误报。
    """
    if not INDEX.is_file():
        return [{"issue": "index.md 不存在"}]
    idx = INDEX.read_text(encoding="utf-8", errors="ignore")
    idx_low = idx.lower()
    out = []

    domains = {p.relative_to(WIKI).parts[0] for p in wiki_pages()
               if len(p.relative_to(WIKI).parts) > 1}
    for d in sorted(domains):
        if f"wiki/{d}" not in idx and d not in idx:
            out.append({"domain": d, "issue": "index.md 未提及该领域"})

    for p in wiki_pages():
        if not _mentioned(p.stem, idx, idx_low):
            out.append({"page": page_key(p), "issue": "index.md 里找不到相关关键词"})
    return out


def check_logsync() -> list[dict]:
    if not LOG.is_file():
        return [{"issue": "log.md 不存在"}]
    log = LOG.read_text(encoding="utf-8", errors="ignore")
    log_low = log.lower()
    return [{"page": page_key(p)} for p in wiki_pages()
            if not _mentioned(p.stem, log, log_low)]


def check_empty() -> list[dict]:
    out = []
    for p in wiki_pages():
        try:
            n = len(p.read_text(encoding="utf-8", errors="ignore").strip())
        except OSError:
            continue
        if n < MIN_CHARS:
            out.append({"page": page_key(p), "chars": n})
    return out


CHECKS = ("deadlink", "orphan", "rawlink", "indexsync", "logsync", "empty")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="结构化输出")
    ap.add_argument("--only", default=None,
                    help=f"只跑指定检查，逗号分隔。可选: {','.join(CHECKS)}")
    args = ap.parse_args()

    if not WIKI.is_dir():
        eprint(f"[错误] 找不到 wiki 目录: {WIKI}")
        return 2

    todo = CHECKS
    if args.only:
        todo = tuple(x.strip() for x in args.only.split(",") if x.strip() in CHECKS)
        if not todo:
            eprint(f"[错误] --only 无有效检查项。可选: {','.join(CHECKS)}")
            return 2

    inbound, dead = collect_links()
    result: dict[str, list] = {}
    if "deadlink" in todo:
        result["deadlink"] = dead
    if "orphan" in todo:
        result["orphan"] = check_orphan(inbound)
    if "rawlink" in todo:
        result["rawlink"] = check_rawlink()
    if "indexsync" in todo:
        result["indexsync"] = check_indexsync()
    if "logsync" in todo:
        result["logsync"] = check_logsync()
    if "empty" in todo:
        result["empty"] = check_empty()

    total = sum(len(v) for v in result.values())

    if args.json:
        print(json.dumps({
            "vault": str(VAULT),
            "wiki_pages": len(wiki_pages()),
            "total_findings": total,
            "findings": result,
        }, ensure_ascii=False, indent=2))
        return 1 if total else 0

    # 人类可读报告
    print(f"# 库健康检查 · {VAULT.name}")
    print(f"\nwiki 页数: {len(wiki_pages())}  |  发现问题: {total}\n")

    titles = {
        "deadlink": ("死链（指向不存在的页/文件）", "修：改正链接目标，或补上缺失的页"),
        "orphan": ("孤儿页（没有其他页链接到它）", "修：从相关页建双链，让它接入知识网"),
        "rawlink": ("raw 原文未被 wiki 引用", "修：若有价值则蒸馏成 wiki 页；否则确认它只是留档"),
        "indexsync": ("index.md 唤醒条目缺失", "修：在 index 对应领域补关键词（唤醒是 index 的职责）"),
        "logsync": ("log.md 无摄入记录", "修：补一条 log，或确认是早期页无需追记"),
        "empty": (f"内容过短（<{MIN_CHARS} 字符，可能没写完）", "修：补完或删除占位页"),
    }

    for k in todo:
        items = result.get(k, [])
        title, hint = titles[k]
        mark = "✅" if not items else "⚠️"
        print(f"## {mark} {title} — {len(items)}")
        if items:
            print(f"   建议：{hint}")
            for it in items[:30]:
                if k == "deadlink":
                    print(f"   · {it['page']}  →  [[{it['link']}]]")
                elif k == "rawlink":
                    tag = "（log 里有记录）" if it.get("in_log") else "（log 里也没记）"
                    print(f"   · {it['raw']} {tag}")
                elif k == "empty":
                    print(f"   · {it['page']}  ({it['chars']} 字符)")
                else:
                    print(f"   · {it.get('page') or it.get('domain') or it}"
                          + (f"  — {it['issue']}" if it.get("issue") else ""))
            if len(items) > 30:
                print(f"   … 另有 {len(items) - 30} 条")
        print()

    if total == 0:
        print("库很健康，没发现问题。")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
