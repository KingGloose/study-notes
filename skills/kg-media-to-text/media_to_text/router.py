"""分流调度：按素材类型路由到对应 handler。这是底层库的唯一入口逻辑。"""
from __future__ import annotations

from pathlib import Path

from .detect import detect_kind
from .types import SourceKind, TextResult, UnsupportedSourceError
from .handlers import document, audio


def to_text(
    source: str | Path,
    *,
    kind: SourceKind | None = None,
    model: str | None = None,
    language: str | None = None,
    initial_prompt: str | None = None,
    timestamps: bool = True,
    hotwords: list[str] | None = None,
) -> TextResult:
    """把任意素材转成文字。底层库对外的唯一 API。

    Args:
        source:   文件路径
        kind:     强制指定素材类型（可选，默认自动探测）
        model:    ASR 模型名（仅音视频有效，默认按平台选合适的）
        language: 语言提示，如 "zh"（仅音视频有效）。
                  **中文强烈建议传 "zh"**，否则不会注入标点引导 prompt。
        initial_prompt: 自定义 ASR 引导词（仅音视频）。不传时中文自动用内置的
                  标点引导 prompt。传空字符串 "" 可显式禁用。
                  注意：prompt 不要写元指令或示范句，会被模型当内容续写。
        timestamps: 输出是否带时间戳（仅音视频，默认 True）。无论真假都按
                  segment 分行，不会输出无换行的一堵墙。
        hotwords: 专名热词表（仅音视频），如 ["携隐Melody", "纵横四海"]。
                  库内会把它们**包成自然句**再注入（直接拼词表无效，见 SKILL.md），
                  并按 token 预算截断。**按重要度从前往后传**，尾部可能被舍弃。
                  切勿直接把整段 shownotes/简介传进来：实测会超 prompt 上限 8 倍
                  并把模型搞崩（输出退化成重复字）。

    Returns:
        TextResult(text, kind, backend, metadata, warnings)

    Raises:
        FileNotFoundError, UnsupportedSourceError, MissingDependencyError
    """
    path = Path(source).expanduser()
    if not path.exists():
        raise FileNotFoundError(f"文件不存在: {path}")
    if path.is_dir():
        raise UnsupportedSourceError(
            f"传入的是目录而非文件: {path}（本库一次只处理一个文件，批量请由上层循环调用）"
        )

    k = kind or detect_kind(path)

    if k == SourceKind.PDF:
        return document.handle_pdf(path)
    if k in (SourceKind.WORD, SourceKind.PPT, SourceKind.EXCEL):
        return document.handle_office(path, k)
    if k == SourceKind.PLAIN:
        return document.handle_plain(path, k)
    if k in (SourceKind.AUDIO, SourceKind.VIDEO):
        return audio.handle_audio_video(
            path, k,
            model=model,
            language=language,
            initial_prompt=initial_prompt,
            timestamps=timestamps,
            hotwords=hotwords,
        )
    if k == SourceKind.IMAGE:
        raise UnsupportedSourceError(
            "图片 OCR 暂未实现（规划中的 L2 能力）。当前支持：PDF/Office/txt/md/音频/视频。"
        )

    raise UnsupportedSourceError(f"无法识别的素材类型: {path.name}")
