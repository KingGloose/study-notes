"""文档处理 handler：PDF → Docling，Office → MarkItDown，txt/md → 直接读。

选型理由：
- Docling(IBM, MIT)：版面感知，表格/公式/多栏保真最好，本地推理。
- MarkItDown(微软, MIT)：Office 系(docx/pptx/xlsx)转 md 更顺。
- txt/md：本来就是文字，零依赖直接读。
"""
from __future__ import annotations

from pathlib import Path

from ..types import (
    SourceKind,
    TextResult,
    MissingDependencyError,
    MediaToTextError,
)

_DOC_HINT = "缺少文档依赖，请安装：uv pip install -r requirements/doc.txt"


def handle_plain(path: Path, kind: SourceKind) -> TextResult:
    """txt / md 直接读，不做任何转换。"""
    for enc in ("utf-8", "gbk", "latin-1"):
        try:
            text = path.read_text(encoding=enc)
            return TextResult(
                text=text,
                kind=kind,
                backend="builtin",
                metadata={"encoding": enc, "filename": path.name},
            )
        except UnicodeDecodeError:
            continue
    # 不是依赖问题，是文件本身编码问题，用基类异常
    raise MediaToTextError(f"无法解码文本文件（已尝试 utf-8/gbk/latin-1）: {path}")


def handle_pdf(path: Path) -> TextResult:
    """PDF → Markdown，用 Docling。"""
    try:
        from docling.document_converter import DocumentConverter
    except ImportError as e:
        raise MissingDependencyError(f"{_DOC_HINT}（docling 未安装）") from e

    converter = DocumentConverter()
    try:
        result = converter.convert(str(path))
        doc = result.document
        text = doc.export_to_markdown()
    except Exception as e:
        # 包成库的统一异常，否则上层 except MediaToTextError 捕不到，
        # 用户会看到裸 traceback（常见于加密/损坏的 PDF）。
        raise MediaToTextError(
            f"Docling 解析 PDF 失败（{type(e).__name__}）: {e}\n"
            f"常见原因：文件加密、已损坏、或不是有效 PDF。"
        ) from e

    warnings: list[str] = []
    meta = {"filename": path.name}
    try:
        meta["pages"] = len(doc.pages) if getattr(doc, "pages", None) else None
    except Exception:
        pass

    if not text.strip():
        warnings.append(
            "未提取到文字。可能是扫描件/图片型 PDF，需要 OCR（Docling 可开启 OCR 选项）。"
        )

    return TextResult(
        text=text,
        kind=SourceKind.PDF,
        backend="docling",
        metadata=meta,
        warnings=warnings,
    )


def handle_office(path: Path, kind: SourceKind) -> TextResult:
    """docx / pptx / xlsx / csv → Markdown，用 MarkItDown。"""
    try:
        from markitdown import MarkItDown
    except ImportError as e:
        raise MissingDependencyError(f"{_DOC_HINT}（markitdown 未安装）") from e

    md = MarkItDown()
    try:
        res = md.convert(str(path))
    except Exception as e:
        raise MediaToTextError(
            f"MarkItDown 解析失败（{type(e).__name__}）: {e}\n"
            f"常见原因：文件加密、格式损坏、或是旧版二进制格式（.doc/.xls 可试先另存为 docx/xlsx）。"
        ) from e
    text = getattr(res, "text_content", "") or ""

    warnings: list[str] = []
    if not text.strip():
        warnings.append("未提取到文字，文件可能为空或格式异常。")

    return TextResult(
        text=text,
        kind=kind,
        backend="markitdown",
        metadata={"filename": path.name, "title": getattr(res, "title", None)},
        warnings=warnings,
    )
