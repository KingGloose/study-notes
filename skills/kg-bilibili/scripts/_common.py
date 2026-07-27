"""公共工具：加载 cookie、构造 Credential。跨平台（Mac/WSL/Windows）通用。"""
import os
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = SKILL_DIR / ".env"


def select_http_client():
    """注册并选中 curl_cffi 作为 HTTP client。

    bilibili-api-python 的 HTTP client 是可插拔的，裸装不带任何 client，
    必须显式选一个才能发请求。curl_cffi 是官方推荐（可模拟浏览器指纹绕风控）。
    每个用到网络的脚本在 load_credential 前调用一次即可。
    """
    from bilibili_api import select_client
    select_client("curl_cffi")


def load_credential():
    """从 skill 目录下的 .env 读取 cookie，返回 bilibili_api.Credential。

    .env 需包含 SESSDATA（必填）、BILI_JCT、BUVID3。
    """
    from dotenv import dotenv_values
    from bilibili_api import Credential

    if not ENV_PATH.exists():
        sys.exit(
            f"[错误] 未找到 {ENV_PATH}\n"
            f"请复制 .env.example 为 .env 并填入浏览器里的 B 站 cookie（SESSDATA 等）。"
        )

    cfg = dotenv_values(ENV_PATH)
    sessdata = (cfg.get("SESSDATA") or "").strip()
    if not sessdata:
        sys.exit("[错误] .env 里 SESSDATA 为空。请从浏览器 F12 → Application → Cookies → bilibili.com 复制。")

    return Credential(
        sessdata=sessdata,
        bili_jct=(cfg.get("BILI_JCT") or "").strip() or None,
        buvid3=(cfg.get("BUVID3") or "").strip() or None,
    )


def eprint(*args, **kwargs):
    """打到 stderr，避免污染 stdout 的 JSON 输出。"""
    print(*args, file=sys.stderr, **kwargs)
