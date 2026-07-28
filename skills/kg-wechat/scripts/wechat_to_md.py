#!/usr/bin/env python3
"""抓取微信公众号单篇文章，转成 Markdown，图片下载到本地（解决防盗链）。

用法:
  python wechat_to_md.py <公众号文章URL> [--out <输出md路径>] [--assets <图片目录>] [--no-images]

说明:
  - 单篇公开文章（mp.weixin.qq.com/s/...）无需登录/cookie。
  - 图片由 mmbiz.qpic.cn 提供，有 Referer 防盗链，必须下载到本地，
    否则笔记里图片会裂。默认下载到 --assets 指定目录（相对 md 引用）。
  - 默认输出到 stdout（纯 Markdown）；给 --out 则写文件。

退出码: 0 成功；非 0 失败（stderr 有原因）。
"""
import argparse
import hashlib
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

from curl_cffi import requests as cffi
from bs4 import BeautifulSoup
from markdownify import markdownify as md

WX_HEADERS_REFERER = {"Referer": "https://mp.weixin.qq.com/"}
UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) "
      "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")


def eprint(*a, **k):
    print(*a, file=sys.stderr, **k)


def sniff_image_ext(data: bytes, fallback: str = "png") -> str:
    """按文件头（magic number）判真实图片格式。

    公众号部分图的 URL 带 wx_fmt=other，拿不到扩展名；若直接存成 .other，
    Obsidian 和浏览器都识别不了（实测遇到过：实际是 WebP）。
    """
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return "png"
    if data[:3] == b"\xff\xd8\xff":
        return "jpeg"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return "gif"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    if data[:2] == b"BM":
        return "bmp"
    if data[:5] == b"<?xml" or data[:4] == b"<svg":
        return "svg"
    return fallback


def fetch_html(url: str) -> str:
    try:
        r = cffi.get(url, headers={"User-Agent": UA}, impersonate="safari_ios", timeout=30)
        r.raise_for_status()
    except Exception as e:
        sys.exit(f"[错误] 请求文章失败（{type(e).__name__}）: {e}\n"
                 f"       检查网络与链接有效性；文章可能已删除或需要登录。")
    html = r.text
    if any(x in html for x in ("环境异常", "访问过于频繁", "去验证")):
        sys.exit("[错误] 触发微信风控（环境异常/频繁）。稍后再试或换网络。")
    return html


def extract_meta(soup: BeautifulSoup, html: str) -> dict:
    def og(prop):
        tag = soup.find("meta", property=prop)
        return tag["content"].strip() if tag and tag.get("content") else ""

    def jsvar(name):
        m = re.search(rf'var {name} = "([^"]*)"', html)
        return m.group(1).strip() if m else ""

    ct = jsvar("ct")
    date = ""
    if ct.isdigit():
        date = datetime.fromtimestamp(int(ct)).strftime("%Y-%m-%d")

    # 真实公众号名在 nickname = htmlDecode("...") 里（og:site_name 是通用值）
    m_nick = re.search(r'nickname\s*=\s*htmlDecode\("([^"]*)"', html)
    account = m_nick.group(1).strip() if m_nick else (og("og:site_name") or "")

    # soup.title 存在但 .string 可能为 None（错误页/嵌套标签），故用 get_text 兜底
    fallback_title = ""
    if soup.title is not None:
        fallback_title = (soup.title.get_text() or "").strip()

    return {
        "title": og("og:title") or fallback_title,
        "author": jsvar("author"),
        "account": account,
        "date": date,
    }


def sanitize(name: str) -> str:
    name = re.sub(r"[\\/:*?\"<>|\n\r\t]", "_", name).strip()
    return name[:80] or "wechat-article"


def download_images(content_tag, assets_dir: Path, md_asset_prefix: str) -> int:
    """把正文里的 img 下载到 assets_dir，并把 src 改成本地相对路径。返回下载成功数。"""
    imgs = content_tag.find_all("img")
    n = 0
    for i, img in enumerate(imgs):
        src = img.get("data-src") or img.get("src") or ""
        if not src or src.startswith("data:"):
            continue
        try:
            r = cffi.get(src, headers={**WX_HEADERS_REFERER, "User-Agent": UA},
                         impersonate="safari_ios", timeout=30)
            r.raise_for_status()
        except Exception as e:
            eprint(f"[warn] 图片下载失败 {src[:60]}...: {e}")
            continue
        fmt = "png"
        m = re.search(r"wx_fmt=([a-z0-9]+)", src)
        if m:
            fmt = m.group(1)
        # 公众号部分图的 wx_fmt=other（或缺失），拿不到真实扩展名，
        # 存成 .other 会让 Obsidian / 浏览器认不出图。按文件头嗅探真实格式。
        if fmt not in ("png", "jpeg", "jpg", "gif", "webp", "bmp", "svg"):
            fmt = sniff_image_ext(r.content, fallback="png")
        h = hashlib.md5(src.encode()).hexdigest()[:10]
        fname = f"wx-{h}.{fmt}"
        assets_dir.mkdir(parents=True, exist_ok=True)
        (assets_dir / fname).write_bytes(r.content)
        img["src"] = f"{md_asset_prefix}/{fname}"
        # 清掉懒加载属性避免干扰 markdownify
        for attr in ("data-src", "data-croporisrc", "data-backh", "data-backw", "data-ratio", "data-type"):
            if img.has_attr(attr):
                del img[attr]
        n += 1
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--out", default=None, help="输出 md 文件路径；不给则打到 stdout")
    ap.add_argument("--assets", default=None, help="图片下载目录；默认 <out同级>/assets 或临时忽略")
    ap.add_argument("--asset-prefix", default="assets", help="md 里图片引用的相对前缀，默认 assets")
    ap.add_argument("--no-images", action="store_true", help="不下载图片（保留原链接，可能防盗链裂图）")
    args = ap.parse_args()

    if "mp.weixin.qq.com" not in args.url:
        eprint("[warn] URL 不是 mp.weixin.qq.com，仍尝试抓取")

    eprint(f"[..] 抓取 {args.url}")
    html = fetch_html(args.url)
    soup = BeautifulSoup(html, "lxml")
    meta = extract_meta(soup, html)

    content = soup.find(id="js_content")
    if content is None:
        sys.exit("[错误] 未找到正文容器 js_content，可能是非图文消息或页面结构变化。")

    # 处理图片
    img_count = 0
    if not args.no_images:
        if args.assets:
            assets_dir = Path(args.assets)
        elif args.out:
            assets_dir = Path(args.out).resolve().parent / args.asset_prefix
        else:
            assets_dir = Path.cwd() / args.asset_prefix
        img_count = download_images(content, assets_dir, args.asset_prefix)
        eprint(f"[ok] 图片下载 {img_count} 张 -> {assets_dir}")

    body_md = md(str(content), heading_style="ATX", strip=["script", "style"]).strip()
    body_md = re.sub(r"\n{3,}", "\n\n", body_md)
    # 清掉空标题（原文分隔符/装饰元素渲染成的 "# " 空行）
    body_md = re.sub(r"^#+\s*$", "", body_md, flags=re.MULTILINE)
    body_md = re.sub(r"\n{3,}", "\n\n", body_md).strip()

    front = [
        f"# {meta['title']}",
        "",
        f"- 作者: {meta['author']}",
        f"- 公众号: {meta['account']}",
        f"- 发布日期: {meta['date']}",
        f"- 原文: {args.url}",
        f"- 抓取日期: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "---",
        "",
    ]
    result = "\n".join(front) + body_md + "\n"

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(result, encoding="utf-8")
        eprint(f"[ok] 已写入 {args.out}（正文 {len(body_md)} 字，图片 {img_count} 张）")
    else:
        sys.stdout.write(result)
        eprint(f"[ok] 正文 {len(body_md)} 字，图片 {img_count} 张")


if __name__ == "__main__":
    main()
