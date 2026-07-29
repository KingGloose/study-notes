#!/usr/bin/env python3
"""把文档转成 Markdown 存入 raw/，供后续 AI 解析沉淀。

支持三种输入：
  1. 单个文件   PDF / Word / PPT / Excel / txt / md
  2. 文件夹     批量处理（--batch，支持断点续传：已存在的输出会跳过）
  3. 网页 URL   抓正文转 Markdown（普通技术博客；公众号请用 kg-wechat）

薄上层：转换全部委托底层库 media_to_text，本脚本只负责
「命名 + 写 raw + 加溯源头部 + 批量调度」这些业务约定。

用法:
  python ingest_doc.py <文件路径>                     # 单文件
  python ingest_doc.py <文件夹> --batch               # 批量
  python ingest_doc.py <文件夹> --batch --ext pdf,md  # 限定类型
  python ingest_doc.py <http(s)://...>                # 网页
  python ingest_doc.py <输入> --stdout                # 只预览不落盘
"""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

from media_to_text import to_text, MediaToTextError

# 库根：优先 KG_VAULT 环境变量 / ~/.config/kg-wiki/config.json，
# 否则从 cwd 或本文件位置向上找（含 AGENTS.md + wiki/ 的目录）
from media_to_text import find_vault
REPO_ROOT = find_vault(__file__)
RAW_DIR = REPO_ROOT / "raw"

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

# 批量默认处理的扩展名
BATCH_EXTS = ("pdf", "docx", "doc", "pptx", "ppt", "xlsx", "xls", "csv", "txt", "md")


def eprint(*a, **k):
    print(*a, file=sys.stderr, **k)


def sanitize(name: str) -> str:
    name = re.sub(r"[\\/:*?\"<>|\n\r\t]", "_", name).strip()
    return name[:60] or "document"


def is_url(s: str) -> bool:
    try:
        u = urlparse(s)
        return u.scheme in ("http", "https") and bool(u.netloc)
    except ValueError:
        return False


# ---------- 网页 ----------

def fetch_webpage(url: str) -> tuple[str, str]:
    """抓网页正文，返回 (markdown, 标题)。用 curl_cffi + readability 思路：
    优先 <article>/<main>，退而用正文密度最大的容器。"""
    try:
        from curl_cffi import requests as cffi
        from bs4 import BeautifulSoup
        from markdownify import markdownify as md
    except ImportError as e:
        sys.exit(f"[错误] 网页抓取需要 base+wechat 依赖: {e}")

    if "mp.weixin.qq.com" in url:
        eprint("[!] 这是微信公众号链接，建议改用 kg-wechat（有专门的图片防盗链处理）")

    try:
        # allow_redirects：curl_cffi 默认不跟随重定向，很多博客有 /page → /page/ 的跳转
        r = cffi.get(url, headers={"User-Agent": UA}, impersonate="chrome",
                     timeout=30, allow_redirects=True)
        r.raise_for_status()
    except Exception as e:
        sys.exit(f"[错误] 请求网页失败（{type(e).__name__}）: {e}")

    soup = BeautifulSoup(r.text, "lxml")

    # 处理 meta refresh / JS 跳转页（不是 HTTP 3xx，allow_redirects 接不到）
    meta_rf = soup.find("meta", attrs={"http-equiv": re.compile("refresh", re.I)})
    if meta_rf and meta_rf.get("content"):
        m = re.search(r"url=([^;\s]+)", meta_rf["content"], re.I)
        if m:
            nxt = m.group(1).strip("'\"")
            if nxt.startswith("/"):
                u = urlparse(url)
                nxt = f"{u.scheme}://{u.netloc}{nxt}"
            if nxt != url:
                eprint(f"[..] 跟随 meta 跳转 → {nxt}")
                return fetch_webpage(nxt)

    title = ""
    if soup.title is not None:
        title = (soup.title.get_text() or "").strip()
    og = soup.find("meta", property="og:title")
    if og and og.get("content"):
        title = og["content"].strip()

    # 去噪
    for tag in soup(["script", "style", "nav", "header", "footer", "aside", "form", "noscript"]):
        tag.decompose()

    # 选正文容器：article > main > 文字最多的 div
    node = soup.find("article") or soup.find("main")
    if node is None:
        best, best_len = None, 0
        for d in soup.find_all(["div", "section"]):
            n = len(d.get_text(strip=True))
            if n > best_len:
                best, best_len = d, n
        node = best or soup.body or soup
    body = md(str(node), heading_style="ATX", strip=["script", "style"]).strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body, title


def ingest_url(url: str, args) -> int:
    eprint(f"[..] 抓取网页 {url}")
    body, title = fetch_webpage(url)
    if not body.strip():
        eprint("[错误] 未提取到正文（可能是 JS 渲染页或反爬）。")
        return 3
    eprint(f"[ok] 正文 {len(body)} 字符 | 标题: {title or '(无)'}")

    head = [
        f"# {args.title or title or urlparse(url).netloc}",
        "",
        f"- 原文链接: {url}",
        f"- 素材类型: webpage",
        f"- 解析后端: bs4 + markdownify",
        f"- 摄入日期: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "> [!] 网页正文由启发式提取（article/main/最长容器），可能含残留导航或漏段，必要时核对原文。",
        "",
        "---",
        "",
    ]
    content = "\n".join(head) + body.rstrip() + "\n"

    if args.stdout:
        sys.stdout.write(content)
        return 0
    out = Path(args.out).expanduser() if args.out else (
        RAW_DIR / f"web-{datetime.now().strftime('%Y-%m-%d')}-{sanitize(title or urlparse(url).netloc)}.md"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    eprint(f"[ok] 已写入 {out}")
    print(out)
    return 0


# ---------- 本地文件 ----------

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


def out_path_for(src: Path) -> Path:
    return RAW_DIR / f"doc-{datetime.now().strftime('%Y-%m-%d')}-{sanitize(src.stem)}.md"


def ingest_one(src: Path, args, quiet: bool = False) -> tuple[int, Path | None]:
    """处理单个文件。返回 (退出码, 输出路径或 None)。"""
    if not quiet:
        eprint(f"[..] 解析 {src.name}（首次跑可能需下载模型，请耐心等）")
    try:
        result = to_text(src)
    except MediaToTextError as e:
        eprint(f"[错误] {src.name}: {e}")
        return 2, None
    except OSError as e:
        eprint(f"[错误] 读取文件失败 {src.name}: {e}")
        return 2, None

    if not quiet:
        eprint(f"[ok] {result.kind.value} via {result.backend}，{len(result.text)} 字符")
    for w in result.warnings:
        eprint(f"[warn] {src.name}: {w}")

    if result.is_empty:
        eprint(f"[错误] {src.name}: 未提取到任何文字，跳过（不写空文件）。")
        return 3, None

    content = build_header(src, result, args.title) + result.text.rstrip() + "\n"

    if args.stdout:
        sys.stdout.write(content)
        return 0, None

    out = Path(args.out).expanduser() if args.out else out_path_for(src)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    if not quiet:
        eprint(f"[ok] 已写入 {out}")
    return 0, out


def ingest_batch(folder: Path, args) -> int:
    exts = tuple(e.strip().lstrip(".").lower()
                 for e in (args.ext.split(",") if args.ext else BATCH_EXTS))
    files = sorted(p for p in folder.rglob("*")
                   if p.is_file() and p.suffix.lstrip(".").lower() in exts)
    if not files:
        eprint(f"[错误] {folder} 下没有匹配的文件（类型: {', '.join(exts)}）")
        return 1

    eprint(f"[..] 批量处理 {len(files)} 个文件（类型: {', '.join(exts)}）")
    ok, skipped, failed = [], [], []
    for i, f in enumerate(files, 1):
        dest = out_path_for(f)
        if dest.exists() and not args.force:
            eprint(f"[{i}/{len(files)}] 跳过（已存在，--force 可覆盖）: {f.name}")
            skipped.append(f.name)
            continue
        eprint(f"[{i}/{len(files)}] {f.name}")
        code, out = ingest_one(f, args, quiet=True)
        if code == 0 and out:
            ok.append(out)
            print(out)  # stdout 逐行输出成功路径
        else:
            failed.append(f.name)

    eprint(f"\n[汇总] 成功 {len(ok)} | 跳过 {len(skipped)} | 失败 {len(failed)}")
    if failed:
        eprint("[失败清单] " + ", ".join(failed[:10]) + (" …" if len(failed) > 10 else ""))
    return 0 if ok or skipped else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="文件路径 / 文件夹（配 --batch）/ 网页 URL")
    ap.add_argument("--batch", action="store_true", help="把 path 当文件夹批量处理")
    ap.add_argument("--ext", default=None,
                    help=f"批量时限定扩展名，逗号分隔。默认: {','.join(BATCH_EXTS)}")
    ap.add_argument("--force", action="store_true", help="批量时覆盖已存在的输出")
    ap.add_argument("--out", default=None, help="输出 md 路径（单文件/URL 有效）")
    ap.add_argument("--stdout", action="store_true", help="只打到 stdout，不写文件")
    ap.add_argument("--title", default=None, help="自定义标题")
    args = ap.parse_args()

    # URL
    if is_url(args.path):
        return ingest_url(args.path, args)

    src = Path(args.path).expanduser()
    if not src.exists():
        eprint(f"[错误] 路径不存在: {src}")
        return 1

    # 批量
    if args.batch or src.is_dir():
        if not src.is_dir():
            eprint(f"[错误] --batch 需要文件夹，但给的是文件: {src}")
            return 1
        if args.stdout:
            eprint("[错误] --batch 不支持 --stdout（会混在一起）")
            return 1
        if args.out:
            eprint("[错误] --batch 不支持 --out（输出名按各文件自动生成）")
            return 1
        return ingest_batch(src, args)

    # 单文件
    code, out = ingest_one(src, args)
    if code == 0 and out:
        print(out)
    return code


if __name__ == "__main__":
    sys.exit(main())
