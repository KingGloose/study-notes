#!/usr/bin/env python3
"""从「用户真实 Chrome」里提取网页正文 → Markdown。

面向「读内容做沉淀」，不是前端调试。核心价值：
  · 天然带用户登录态（知乎/内网文档等，无需配 cookie）
  · 天然通过站点 JS 挑战（如知乎 zse-ck）——真浏览器自己在跑
  · 只读用户自己已能看到的页面，不注入/伪造任何凭证

前置：
  1. npm i -g chrome-devtools-mcp@latest
  2. bash scripts/connect-chrome.sh   （连接用户 Chrome，一次性）

用法:
  python extract_page.py                        # 提取当前活动标签页
  python extract_page.py <URL>                  # 导航到 URL 后提取
  python extract_page.py <URL> --selector ".Post-RichText"   # 指定正文选择器
  python extract_page.py --list                 # 列出当前打开的标签页
  python extract_page.py <URL> --raw-html       # 输出原始 HTML（调试用）
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# 各站点的正文选择器（按域名匹配，命中则优先用）
SITE_SELECTORS: dict[str, list[str]] = {
    "zhihu.com": [
        ".Post-RichTextContainer",        # 专栏文章
        ".QuestionAnswer-content .RichContent-inner",  # 单条回答
        ".RichContent-inner",
        ".Post-RichText",
    ],
    "juejin.cn": ["#article-root", ".article-viewer"],
    "csdn.net": ["#content_views", ".blog-content-box"],
    "cnblogs.com": ["#cnblogs_post_body", "#post_detail"],
    "segmentfault.com": [".article__content", ".fmt"],
    "jianshu.com": ["article", ".show-content"],
    "notion.so": [".notion-page-content"],
    "yuque.com": [".ne-viewer-body", ".lake-content"],
}

# 通用兜底选择器（按优先级）
GENERIC_SELECTORS = ["article", "main", '[role="main"]', ".content", "#content"]


def eprint(*a, **k):
    print(*a, file=sys.stderr, **k)


def run_cdt(args: list[str], timeout: int = 90) -> str:
    """调用 chrome-devtools CLI，返回 stdout（已过滤噪声行）。"""
    try:
        proc = subprocess.run(
            ["chrome-devtools", *args],
            capture_output=True, text=True, timeout=timeout,
        )
    except FileNotFoundError:
        sys.exit("[错误] 未找到 chrome-devtools 命令。请先执行：npm i -g chrome-devtools-mcp@latest")
    except subprocess.TimeoutExpired:
        sys.exit(f"[错误] chrome-devtools {args[0]} 超时。"
                 f"请先跑 bash scripts/connect-chrome.sh 确认已连上用户 Chrome。")

    noise = ("Warning:", "trace-warnings", "exposes content of the browser",
             "Avoid sharing sensitive", "Performance tools may send",
             "Google collects usage statistics", "For more details, visit",
             "To disable, run with", "To opt-out, run with")
    out = "\n".join(l for l in proc.stdout.splitlines()
                    if l.strip() and not any(n in l for n in noise))
    if proc.returncode != 0 or "Failed to execute command" in out:
        eprint(out[-600:] or proc.stderr[-600:])
        sys.exit("[错误] chrome-devtools 执行失败。"
                 "多半是未连接用户 Chrome —— 请跑 bash scripts/connect-chrome.sh；"
                 "若反复失败，按提示在 chrome://inspect 开启 remote debugging 并彻底重启 Chrome。")
    return out


def list_pages() -> str:
    return run_cdt(["list_pages"])


def js_extract_snippet(selectors: list[str]) -> str:
    """生成在页面里执行的 JS：按选择器优先级取正文 HTML + 元信息。"""
    sel_json = json.dumps(selectors, ensure_ascii=False)
    return """() => {
  const sels = %s;
  const pick = () => {
    for (const s of sels) {
      const el = document.querySelector(s);
      if (el && el.innerText && el.innerText.trim().length > 200) return {el, sel: s};
    }
    // 兜底：取文字最多的容器
    let best = null, bestLen = 0;
    for (const el of document.querySelectorAll('article, main, div, section')) {
      const n = (el.innerText || '').trim().length;
      if (n > bestLen) { best = el; bestLen = n; }
    }
    return best ? {el: best, sel: '(auto:longest)'} : null;
  };
  const got = pick();
  const meta = (p) => {
    const m = document.querySelector(`meta[property="${p}"], meta[name="${p}"]`);
    return m ? m.content : '';
  };
  const h1 = document.querySelector('h1');
  return {
    url: location.href,
    title: meta('og:title') || (h1 && h1.innerText.trim()) || document.title,
    site: meta('og:site_name') || location.hostname,
    author: meta('author') || meta('article:author') || '',
    published: meta('article:published_time') || meta('datePublished') || '',
    usedSelector: got ? got.sel : null,
    html: got ? got.el.outerHTML : '',
    textLen: got ? got.el.innerText.trim().length : 0,
  };
}""" % sel_json


def selectors_for(url: str, override: str | None) -> list[str]:
    if override:
        return [override, *GENERIC_SELECTORS]
    for domain, sels in SITE_SELECTORS.items():
        if domain in url:
            return [*sels, *GENERIC_SELECTORS]
    return GENERIC_SELECTORS


def extract(url: str | None, selector: str | None) -> dict:
    if url:
        eprint(f"[..] 导航到 {url}")
        run_cdt(["navigate_page", url])

    # 先拿当前 URL 决定选择器
    tmp = Path(tempfile.mkdtemp(prefix="kgb-")) / "res.json"
    try:
        cur = run_cdt(["evaluate_script", "() => location.href"])
        cur_url = url or ""
        m = re.search(r"https?://[^\s\"'`]+", cur)
        if m:
            cur_url = m.group(0)

        sels = selectors_for(cur_url, selector)
        eprint(f"[..] 提取正文（选择器优先级: {', '.join(sels[:3])}…）")
        run_cdt(["evaluate_script", js_extract_snippet(sels), "--filePath", str(tmp)])

        raw = tmp.read_text(encoding="utf-8", errors="ignore")
        # CLI 可能包一层结构，找到第一个 JSON 对象
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            m2 = re.search(r"\{.*\}", raw, re.S)
            if not m2:
                sys.exit(f"[错误] 无法解析提取结果。原始输出前 300 字:\n{raw[:300]}")
            data = json.loads(m2.group(0))
        # 有的版本会把结果放在 result/value 字段里
        for key in ("result", "value", "data"):
            if isinstance(data, dict) and key in data and isinstance(data[key], dict):
                data = data[key]
        return data
    finally:
        try:
            tmp.unlink(missing_ok=True)
            tmp.parent.rmdir()
        except OSError:
            pass


def html_to_md(html: str) -> str:
    try:
        from markdownify import markdownify as md
    except ImportError:
        sys.exit("[错误] 缺少 markdownify：uv pip install -r requirements/wechat.txt")
    text = md(html, heading_style="ATX", strip=["script", "style"]).strip()
    return re.sub(r"\n{3,}", "\n\n", text)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url", nargs="?", default=None, help="要提取的 URL（省略=当前标签页）")
    ap.add_argument("--selector", default=None, help="自定义正文 CSS 选择器")
    ap.add_argument("--list", action="store_true", help="列出当前打开的标签页")
    ap.add_argument("--raw-html", action="store_true", help="输出原始 HTML 而非 Markdown")
    ap.add_argument("--json", action="store_true", help="输出结构化 JSON（含元信息）")
    args = ap.parse_args()

    if args.list:
        print(list_pages())
        return 0

    data = extract(args.url, args.selector)
    if not data.get("html"):
        eprint("[错误] 未提取到正文。可能是页面未加载完、需要登录，或选择器不匹配。")
        eprint("       建议：在 Chrome 里确认页面已正常显示，或用 --selector 指定容器。")
        return 3

    eprint(f"[ok] 命中选择器 {data.get('usedSelector')} | 正文 {data.get('textLen')} 字符")

    if args.raw_html:
        print(data["html"])
        return 0

    body = html_to_md(data["html"])
    if args.json:
        print(json.dumps({**{k: v for k, v in data.items() if k != "html"},
                          "markdown": body}, ensure_ascii=False, indent=2))
        return 0

    # 默认：带元信息头部的 Markdown
    head = [
        f"# {data.get('title') or '(无标题)'}",
        "",
        f"- 来源: {data.get('site') or ''}",
        f"- 原文链接: {data.get('url') or ''}",
    ]
    if data.get("author"):
        head.append(f"- 作者: {data['author']}")
    if data.get("published"):
        head.append(f"- 发布: {data['published'][:10]}")
    head += ["", "---", ""]
    print("\n".join(head) + body + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
