"""定位知识库根目录（vault root）。

本模块让 skills 可以住在**任何位置**——库内、独立仓库、全局安装——
都能正确找到用户的知识库。这是 skills 独立开源的前提。

解析优先级（前面命中就不再往下找）：
  1. 环境变量 KG_VAULT
  2. 配置文件 ~/.config/kg-wiki/config.json 里的 "vault"
  3. 从当前工作目录向上找（适合在库里执行命令时）
  4. 从本文件位置向上找（适合 skills 住在库内的传统布局）

"是知识库"的判据：目录下同时有 AGENTS.md 和 wiki/（index.md 可选，新库可能还没建）。
"""
from __future__ import annotations

import json
import os
from pathlib import Path

CONFIG_PATH = Path.home() / ".config" / "kg-wiki" / "config.json"
_MARKERS_REQUIRED = ("AGENTS.md",)
_MARKERS_DIR = ("wiki",)


class VaultNotFoundError(RuntimeError):
    """找不到知识库时抛出，消息里带可操作的指引。"""


def looks_like_vault(p: Path) -> bool:
    """判断某目录是否是知识库根。"""
    try:
        if not p.is_dir():
            return False
        if not all((p / m).is_file() for m in _MARKERS_REQUIRED):
            return False
        return all((p / d).is_dir() for d in _MARKERS_DIR)
    except OSError:
        return False


def _from_env() -> Path | None:
    v = os.environ.get("KG_VAULT")
    if not v:
        return None
    p = Path(v).expanduser().resolve()
    if looks_like_vault(p):
        return p
    raise VaultNotFoundError(
        f"环境变量 KG_VAULT 指向 {p}，但那里不像知识库"
        f"（需要 AGENTS.md 和 wiki/ 目录）。"
    )


def _from_config() -> Path | None:
    if not CONFIG_PATH.is_file():
        return None
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    v = data.get("vault")
    if not v:
        return None
    p = Path(v).expanduser().resolve()
    if looks_like_vault(p):
        return p
    raise VaultNotFoundError(
        f"配置文件 {CONFIG_PATH} 里的 vault 指向 {p}，但那里不像知识库。"
    )


def _walk_up(start: Path, limit: int = 8) -> Path | None:
    cur = start.resolve()
    for _ in range(limit):
        if looks_like_vault(cur):
            return cur
        if cur.parent == cur:
            break
        cur = cur.parent
    return None


def find_vault(hint: str | Path | None = None) -> Path:
    """返回知识库根目录。找不到时抛 VaultNotFoundError（带指引）。

    Args:
        hint: 可选的起点路径（通常是调用方的 __file__），用于向上查找。
    """
    p = _from_env()
    if p:
        return p
    p = _from_config()
    if p:
        return p

    # 从当前工作目录往上找
    p = _walk_up(Path.cwd())
    if p:
        return p

    # 从调用方文件位置往上找（skills 住在库内时有效）
    if hint:
        p = _walk_up(Path(hint).parent)
        if p:
            return p

    raise VaultNotFoundError(
        "找不到知识库。请用以下任一方式指定：\n"
        "  1. 环境变量：  export KG_VAULT=/path/to/your-vault\n"
        f"  2. 配置文件：  {CONFIG_PATH}\n"
        '                 内容 {"vault": "/path/to/your-vault"}\n'
        "  3. 在知识库目录内执行命令\n"
        "\n知识库需要包含 AGENTS.md 和 wiki/ 目录。"
    )


def save_config(vault: str | Path) -> Path:
    """把库路径写进配置文件，返回配置文件路径。"""
    p = Path(vault).expanduser().resolve()
    if not looks_like_vault(p):
        raise VaultNotFoundError(f"{p} 不像知识库（需要 AGENTS.md 和 wiki/）。")
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    data = {}
    if CONFIG_PATH.is_file():
        try:
            data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            data = {}
    data["vault"] = str(p)
    CONFIG_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                           encoding="utf-8")
    return CONFIG_PATH
