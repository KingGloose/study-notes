#!/usr/bin/env python3
"""把文档（PDF/Word/PPT/Excel/txt/md）转成 Markdown 存入 raw/，供后续 AI 解析沉淀。

薄上层：转换全部委托底层库 media_to_text，本脚本只负责
「命名 + 写 raw + 加溯源头部」这些业务约定。

用法:
  python ingest_doc.py <文件路径> [--out <输出md>] [--stdout] [--title <标题>]

默认输出到 学习笔记/raw/doc-<日期>-<文件名>.md
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

from media_to_text import to_text, MediaToTextError

# 仓库根：本脚本在 skills/kg-doc/scripts/ 下，向上三级
REPO_ROOT = Path(__file__).resolve().parents[3]
RAW_DIR = REPO_ROOT / "raw"


def eprint(*a, **k):
    print(*a, file=sys.stderr, **k)


def sanitize(name: str) -> str:
    name = re.sub(r"[\\/:*?\"<>|\n\r\t]", "_", name).strip()
    return name[:60] or "document"


def build_header(src: Path, result, title: str | None) -> str:
    lines = [
        f"# {title or src.stem}",
        "",
        f"- 来源文件: `{src.name}`",
        f"- 原始路径: `{src}`",
        f"- 素材类型: {result.kind.value}",
        f"- 解析后端: {result.backend}",
    ]
    pages = result.metadata.get("pages")
    if pages:
        lines.append(f"- 页数: {pages}")
    lines.append(f"- 摄入日期: {datetime.now().strftime('%Y-%m-%d')}")
    if result.warnings:
        lines.append("")
        for w in result.warnings:
            lines.append(f"> [!] {w}")
    lines += ["", "---", ""]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="文档路径")
    ap.add_argument("--out", default=None, help="输出 md 路径；默认写入 raw/")
    ap.add_argument("--stdout", action="store_true", help="只打到 stdout，不写文件（预览用）")
    ap.add_argument("--title", default=None, help="自定义标题")
    args = ap.parse_args()

    src = Path(args.path).expanduser()
    if not src.exists():
        eprint(f"[错误] 文件不存在: {src}")
        return 1

    eprint(f"[..] 解析 {src.name}（首次跑可能需下载模型，请耐心等）")
    try:
        result = to_text(src)
    except MediaToTextError as e:
        eprint(f"[错误] {e}")
        return 2
    except OSError as e:
        # 权限/IO 类错误，不让裸 traceback 冒给用户
        eprint(f"[错误] 读取文件失败: {e}")
        return 2

    eprint(f"[ok] {result.kind.value} via {result.backend}，{len(result.text)} 字符")
    for w in result.warnings:
        eprint(f"[warn] {w}")

    if result.is_empty:
        eprint("[错误] 未提取到任何文字，终止（不写空文件）。")
        return 3

    content = build_header(src, result, args.title) + result.text.rstrip() + "\n"

    if args.stdout:
        sys.stdout.write(content)
        return 0

    if args.out:
        out = Path(args.out).expanduser()
    else:
        date = datetime.now().strftime("%Y-%m-%d")
        out = RAW_DIR / f"doc-{date}-{sanitize(src.stem)}.md"

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    eprint(f"[ok] 已写入 {out}")
    print(out)  # stdout 输出路径，便于上层脚本/AI 取用
    return 0


if __name__ == "__main__":
    sys.exit(main())
