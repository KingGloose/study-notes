"""media-to-text · 底层核心库

任意素材 → 文字。平台无关、按类型分流，供上层业务 skill（bilibili / 公众号 /
小宇宙 / 文档）随时调用。

用法：
    from media_to_text import to_text
    result = to_text("/path/to/file.pdf")
    print(result.text)
"""
from .router import to_text
from .detect import detect_kind
from .vault import find_vault, looks_like_vault, save_config, VaultNotFoundError
from .hotwords import extract_hotwords
from .types import (
    SourceKind,
    TextResult,
    MediaToTextError,
    UnsupportedSourceError,
    MissingDependencyError,
)

__all__ = [
    "to_text",
    "detect_kind",
    "find_vault",
    "looks_like_vault",
    "save_config",
    "VaultNotFoundError",
    "extract_hotwords",
    "SourceKind",
    "TextResult",
    "MediaToTextError",
    "UnsupportedSourceError",
    "MissingDependencyError",
]

__version__ = "0.1.0"
