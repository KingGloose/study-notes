"""音视频转写 handler：本地 ASR，按平台自动选后端。

平台适配（这是本模块存在的核心理由）：
- macOS + Apple Silicon → mlx-whisper（走 MLX/Metal GPU 加速）
- Linux / WSL2          → faster-whisper（CTranslate2，有 NVIDIA GPU 走 CUDA，否则 CPU）
  说明：faster-whisper 不支持 Apple MPS，Mac 上只能 CPU 干跑，故 Mac 专用 mlx。

视频文件会先用 ffmpeg 抽音轨再转写。
"""
from __future__ import annotations

import platform
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from ..types import SourceKind, TextResult, MissingDependencyError, MediaToTextError

DEFAULT_MODEL_MAC = "mlx-community/whisper-large-v3-turbo"
DEFAULT_MODEL_LINUX = "large-v3"

# Whisper 作为自回归模型会随机陷入「无标点模式」，中文尤其严重（实测 2 分钟中文
# 播客片段标点数为 0，整段几万字连成一串，人类不可读）。社区通用解法是用
# initial_prompt 给一段「带标点的正常中文」，把模型推回「有标点模式」。
#
# 踩坑（实测）：prompt 里不要写冒号、不要写「例如」「请保留标点」这类元指令，
# 也不要塞示范句 —— 模型会把它们当成上文内容续写，输出里会混进「Ｂ」这种
# 全角垃圾字符。只给一段平实的陈述句效果最好。
ZH_PUNCT_PROMPT = (
    "这是一段普通话内容。说话人在正常讲述，句子之间有标点，语气自然。"
)


def _default_prompt(language: str | None) -> str | None:
    """中文默认注入标点引导 prompt；其他语言不干预。"""
    if language and language.lower().startswith("zh"):
        return ZH_PUNCT_PROMPT
    return None


def _normalize_zh_punct(text: str) -> str:
    """中文行里的半角标点转全角。

    Whisper 中文输出的逗号/问号常是半角（如“可是呢,时间一长”），混在中文里难看。
    只在标点紧邻中文字符时才转，避免误伤英文句子与小数（如 3.5、large-v3, turbo）。
    """
    CJK = r"\u4e00-\u9fff\u3000-\u303f"
    for half, full in ((",", "，"), ("?", "？"), ("!", "！"), (";", "；")):
        h = re.escape(half)
        text = re.sub(rf"(?<=[{CJK}]){h}", full, text)      # 中文在前
        text = re.sub(rf"{h}(?=[{CJK}])", full, text)        # 中文在后（中英混排）
    # 句末半角句点：仅当前一字是中文且后面不是数字时
    text = re.sub(rf"(?<=[{CJK}])\.(?!\d)", "。", text)
    return text


def _segments_to_text(segments, with_timestamps: bool = True) -> str:
    """把 segment 列表拼成可读文本。

    不要直接用 whisper 返回的 res["text"] —— 那是所有 segment 的裸拼接，
    没有换行，几万字会变成一堵墙。按 segment 分行才是人类可读的形态。
    """
    lines = []
    for seg in segments:
        txt = (seg["text"] if isinstance(seg, dict) else seg.text).strip()
        if not txt:
            continue
        txt = _normalize_zh_punct(txt)
        if with_timestamps:
            start = seg["start"] if isinstance(seg, dict) else seg.start
            m, s = divmod(int(start), 60)
            h, m = divmod(m, 60)
            stamp = f"[{h:02d}:{m:02d}:{s:02d}]" if h else f"[{m:02d}:{s:02d}]"
            lines.append(f"{stamp} {txt}")
        else:
            lines.append(txt)
    return "\n".join(lines)


def _is_apple_silicon() -> bool:
    return platform.system() == "Darwin" and platform.machine() in ("arm64", "aarch64")


def pick_backend() -> str:
    """返回本机应使用的 ASR 后端名。"""
    return "mlx-whisper" if _is_apple_silicon() else "faster-whisper"


def _extract_audio(video_path: Path) -> Path:
    """用 ffmpeg 从视频抽出 16k 单声道 wav（ASR 友好格式）。

    返回的临时文件由调用方负责清理（见 handle_audio_video 的 finally）。
    """
    if not shutil.which("ffmpeg"):
        raise MissingDependencyError(
            "处理视频需要 ffmpeg。macOS: brew install ffmpeg；WSL/Ubuntu: sudo apt install ffmpeg"
        )
    tmpdir = Path(tempfile.mkdtemp(prefix="m2t-"))
    tmp = tmpdir / "audio.wav"
    proc = subprocess.run(
        ["ffmpeg", "-y", "-i", str(video_path), "-vn",
         "-ac", "1", "-ar", "16000", "-f", "wav", str(tmp)],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        shutil.rmtree(tmpdir, ignore_errors=True)
        # 把 ffmpeg 的真实错误带出来，否则用户只能看到无信息的 CalledProcessError
        tail = (proc.stderr or "").strip().splitlines()[-5:]
        raise MediaToTextError(
            "ffmpeg 抽取音轨失败：\n" + "\n".join(tail)
        )
    return tmp


def _transcribe_mlx(
    audio: Path,
    model: str | None,
    language: str | None,
    initial_prompt: str | None = None,
    timestamps: bool = True,
) -> tuple[str, dict]:
    try:
        import mlx_whisper
    except ImportError as e:
        raise MissingDependencyError(
            "缺少 mlx-whisper，请安装：uv pip install -r requirements/asr-mac.txt"
        ) from e

    kwargs = {"path_or_hf_repo": model or DEFAULT_MODEL_MAC}
    if language:
        kwargs["language"] = language
    prompt = initial_prompt if initial_prompt is not None else _default_prompt(language)
    if prompt:
        kwargs["initial_prompt"] = prompt
    res = mlx_whisper.transcribe(str(audio), **kwargs)

    segments = res.get("segments") or []
    # 有 segment 就按 segment 分行；万一后端没给 segments，退回裸 text 不至于丢内容
    text = _segments_to_text(segments, timestamps) if segments else res.get("text", "")
    meta = {
        "language": res.get("language"),
        "model": kwargs["path_or_hf_repo"],
        "segments": len(segments),
        "punct_prompt": bool(prompt),
    }
    return text, meta


def _transcribe_faster(
    audio: Path,
    model: str | None,
    language: str | None,
    initial_prompt: str | None = None,
    timestamps: bool = True,
) -> tuple[str, dict]:
    try:
        from faster_whisper import WhisperModel
    except ImportError as e:
        raise MissingDependencyError(
            "缺少 faster-whisper，请安装：uv pip install -r requirements/asr-linux.txt"
        ) from e

    name = model or DEFAULT_MODEL_LINUX
    # 优先 GPU(float16)，失败降级 CPU(int8)。降级原因会写进 metadata，
    # 不静默吞掉——否则用户不知道为何突然变慢。
    gpu_error = None
    try:
        m = WhisperModel(name, device="cuda", compute_type="float16")
        device = "cuda"
    except Exception as e:
        gpu_error = f"{type(e).__name__}: {e}"[:200]
        m = WhisperModel(name, device="cpu", compute_type="int8")
        device = "cpu"

    prompt = initial_prompt if initial_prompt is not None else _default_prompt(language)
    segments, info = m.transcribe(
        str(audio), language=language, initial_prompt=prompt
    )
    seg_list = list(segments)  # 生成器，先落地才能同时算数量和文本
    text = _segments_to_text(seg_list, timestamps)
    meta = {
        "language": info.language,
        "model": name,
        "device": device,
        "segments": len(seg_list),
        "punct_prompt": bool(prompt),
    }
    if gpu_error:
        meta["gpu_fallback_reason"] = gpu_error
    return text, meta


def handle_audio_video(
    path: Path,
    kind: SourceKind,
    model: str | None = None,
    language: str | None = None,
    initial_prompt: str | None = None,
    timestamps: bool = True,
) -> TextResult:
    """音频/视频 → 文字。视频先抽音轨（临时文件用完必清）。

    language="zh" 时默认注入标点引导 prompt（见 ZH_PUNCT_PROMPT）；
    输出按 segment 分行并带时间戳，timestamps=False 可只分行不带戳。
    """
    audio_path = path
    tmp_to_clean: Path | None = None
    warnings: list[str] = []
    if kind == SourceKind.VIDEO:
        audio_path = _extract_audio(path)
        tmp_to_clean = audio_path.parent
        warnings.append("视频已抽取音轨后转写（画面内容未处理）。")

    try:
        backend = pick_backend()
        if backend == "mlx-whisper":
            text, meta = _transcribe_mlx(
                audio_path, model, language, initial_prompt, timestamps
            )
        else:
            text, meta = _transcribe_faster(
                audio_path, model, language, initial_prompt, timestamps
            )
    finally:
        # 无论转写成败都清理抽出的临时音轨，避免 /tmp 堆积
        if tmp_to_clean is not None:
            shutil.rmtree(tmp_to_clean, ignore_errors=True)

    meta["filename"] = path.name
    if not text.strip():
        warnings.append("转写结果为空，音频可能无人声或格式异常。")
    # 中文没走 prompt 引导时大概率无标点，明确告警而不是让人事后困惑
    if not meta.get("punct_prompt") and (meta.get("language") or "").startswith("zh"):
        warnings.append("未注入标点引导 prompt，中文结果可能缺少标点。")

    return TextResult(
        text=text.strip(),
        kind=kind,
        backend=backend,
        metadata=meta,
        warnings=warnings,
    )
