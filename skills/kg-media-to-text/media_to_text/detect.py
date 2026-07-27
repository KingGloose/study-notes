"""素材类型探测：扩展名优先，辅以文件头(magic bytes)兜底。"""
from __future__ import annotations

from pathlib import Path

from .types import SourceKind

# 扩展名 → 类型
_EXT_MAP: dict[str, SourceKind] = {
    ".pdf": SourceKind.PDF,
    ".doc": SourceKind.WORD,
    ".docx": SourceKind.WORD,
    ".ppt": SourceKind.PPT,
    ".pptx": SourceKind.PPT,
    ".xls": SourceKind.EXCEL,
    ".xlsx": SourceKind.EXCEL,
    ".csv": SourceKind.EXCEL,
    ".txt": SourceKind.PLAIN,
    ".md": SourceKind.PLAIN,
    ".markdown": SourceKind.PLAIN,
    # 音频
    ".mp3": SourceKind.AUDIO,
    ".m4a": SourceKind.AUDIO,
    ".wav": SourceKind.AUDIO,
    ".flac": SourceKind.AUDIO,
    ".ogg": SourceKind.AUDIO,
    ".aac": SourceKind.AUDIO,
    ".wma": SourceKind.AUDIO,
    # 视频
    ".mp4": SourceKind.VIDEO,
    ".mkv": SourceKind.VIDEO,
    ".mov": SourceKind.VIDEO,
    ".avi": SourceKind.VIDEO,
    ".flv": SourceKind.VIDEO,
    ".webm": SourceKind.VIDEO,
    # 图片
    ".png": SourceKind.IMAGE,
    ".jpg": SourceKind.IMAGE,
    ".jpeg": SourceKind.IMAGE,
    ".gif": SourceKind.IMAGE,
    ".bmp": SourceKind.IMAGE,
    ".webp": SourceKind.IMAGE,
    ".tiff": SourceKind.IMAGE,
}

# 文件头签名 → 类型（扩展名缺失/错误时兜底）
_MAGIC: list[tuple[bytes, SourceKind]] = [
    (b"%PDF", SourceKind.PDF),
    (b"\x89PNG", SourceKind.IMAGE),
    (b"\xff\xd8\xff", SourceKind.IMAGE),  # jpeg
    (b"GIF8", SourceKind.IMAGE),
    (b"ID3", SourceKind.AUDIO),           # mp3
    (b"OggS", SourceKind.AUDIO),
    (b"fLaC", SourceKind.AUDIO),
]


def detect_kind(path: str | Path) -> SourceKind:
    """判断素材类型。扩展名优先，未知时读文件头兜底。"""
    p = Path(path)
    ext = p.suffix.lower()
    if ext in _EXT_MAP:
        return _EXT_MAP[ext]

    # 扩展名不认识 → 嗅探文件头
    try:
        with open(p, "rb") as f:
            head = f.read(16)
    except OSError:
        return SourceKind.UNKNOWN

    for sig, kind in _MAGIC:
        if head.startswith(sig):
            return kind

    # zip 容器（docx/xlsx/pptx 都是 zip）无法只靠头区分，交给扩展名；此处兜底未知
    return SourceKind.UNKNOWN
