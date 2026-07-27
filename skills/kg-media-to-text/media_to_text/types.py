"""统一数据契约：所有 handler 都返回 TextResult。"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class SourceKind(str, Enum):
    """素材类型。"""

    PDF = "pdf"
    WORD = "word"
    PPT = "ppt"
    EXCEL = "excel"
    PLAIN = "plain"          # txt / md，直接读
    AUDIO = "audio"
    VIDEO = "video"
    IMAGE = "image"
    UNKNOWN = "unknown"


@dataclass
class TextResult:
    """统一输出。上层业务 skill 只依赖这个结构，不关心内部用了哪个库。

    text     : 提取出的纯文字或 Markdown
    kind     : 素材类型
    backend  : 实际使用的后端（docling / markitdown / mlx-whisper / ...），便于排查
    metadata : 附加信息（页数、时长、语言、标题等，按素材类型不同）
    warnings : 非致命问题（如"未提取到文字，可能是扫描件"）
    """

    text: str
    kind: SourceKind
    backend: str
    metadata: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)

    @property
    def is_empty(self) -> bool:
        return not self.text.strip()

    def __repr__(self) -> str:  # 避免 print 时刷屏
        return (
            f"TextResult(kind={self.kind.value}, backend={self.backend}, "
            f"chars={len(self.text)}, warnings={len(self.warnings)})"
        )


class MediaToTextError(Exception):
    """底层库统一异常基类。"""


class UnsupportedSourceError(MediaToTextError):
    """不支持的素材类型。"""


class MissingDependencyError(MediaToTextError):
    """缺少可选依赖（提示用户装哪个 requirements 文件）。"""
