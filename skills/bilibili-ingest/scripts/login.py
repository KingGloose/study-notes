#!/usr/bin/env python3
"""二维码登录 B 站，把 cookie 写进 skill 目录的 .env。

用法:
  python login.py

流程: 终端打印二维码 → 手机 B 站 APP 扫码确认 → 自动轮询 → 成功后写 .env。
跨平台通用（Mac/WSL/Windows 终端都能显示二维码）。
"""
import asyncio
import sys
import time
from pathlib import Path

from bilibili_api import login_v2, sync
from _common import select_http_client, SKILL_DIR, ENV_PATH, eprint


def write_env(cred):
    cookies = cred.get_cookies()  # dict: SESSDATA / bili_jct / buvid3 / DedeUserID ...
    sessdata = cookies.get("SESSDATA", "")
    bili_jct = cookies.get("bili_jct", "")
    buvid3 = cookies.get("buvid3", "")
    dedeuserid = cookies.get("DedeUserID", "")

    lines = [
        "# 由 login.py 扫码登录自动生成。SESSDATA 有效期约一个月，过期重新扫码即可。",
        f"SESSDATA={sessdata}",
        f"BILI_JCT={bili_jct}",
        f"BUVID3={buvid3}",
        f"DEDEUSERID={dedeuserid}",
        "",
    ]
    ENV_PATH.write_text("\n".join(lines), encoding="utf-8")
    return sessdata


async def run():
    select_http_client()
    qr = login_v2.QrCodeLogin(platform=login_v2.QrCodeLoginChannel.WEB)
    await qr.generate_qrcode()

    # 存二维码图片（终端 ANSI 色块在很多环境无法扫描，图片更通用）
    qr_path = SKILL_DIR / "qrcode.png"
    pic = qr.get_qrcode_picture()
    pic.to_file(str(qr_path))
    eprint(f"[qr] 二维码图片已保存: {qr_path}")
    print(qr.get_qrcode_terminal())
    eprint("[..] 请用手机 B 站 APP 扫描二维码并确认登录（限时约 3 分钟）")

    while not qr.has_done():
        state = await qr.check_state()
        if state == login_v2.QrCodeLoginEvents.TIMEOUT:
            eprint("[x] 二维码已过期，请重新运行 login.py")
            sys.exit(1)
        elif state == login_v2.QrCodeLoginEvents.SCAN:
            pass  # 还没扫
        elif state == login_v2.QrCodeLoginEvents.CONF:
            eprint("[..] 已扫描，请在手机上点击确认")
        await asyncio.sleep(2)

    cred = qr.get_credential()
    sessdata = write_env(cred)
    # 登录成功后删掉二维码图片
    try:
        (SKILL_DIR / "qrcode.png").unlink(missing_ok=True)
    except Exception:
        pass
    if sessdata:
        eprint(f"[ok] 登录成功，cookie 已写入 {ENV_PATH}")
    else:
        eprint("[x] 登录疑似失败：未拿到 SESSDATA")
        sys.exit(1)


if __name__ == "__main__":
    sync(run())
