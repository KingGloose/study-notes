"""音视频转写 handler：本地 ASR，按平台自动选后端。

平台适配（这是本模块存在的核心理由）：
- macOS + Apple Silicon → mlx-whisper（走 MLX/Metal GPU 加速）
- Linux / WSL2          → faster-whisper（CTranslate2，有 NVIDIA GPU 走 CUDA，否则 CPU）
  说明：faster-whisper 不支持 Apple MPS，Mac 上只能 CPU 干跑，故 Mac 专用 mlx。

视频文件会先用 ffmpeg 抽音轨再转写。
"""
from __future__ import annotations

import platform
import shutil
import subprocess
import tempfile
from pathlib import Path

from ..types import SourceKind, TextResult, MissingDependencyError, MediaToTextError

DEFAULT_MODEL_MAC = "mlx-community/whisper-large-v3-turbo"
DEFAULT_MODEL_LINUX = "large-v3"


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


def _transcribe_mlx(audio: Path, model: str | None, language: str | None) -> tuple[str, dict]:
    try:
        import mlx_whisper
    except ImportError as e:
        raise MissingDependencyError(
            "缺少 mlx-whisper，请安装：uv pip install -r requirements/asr-mac.txt"
        ) from e

    kwargs = {"path_or_hf_repo": model or DEFAULT_MODEL_MAC}
    if language:
        kwargs["language"] = language
    res = mlx_whisper.transcribe(str(audio), **kwargs)
    return res.get("text", ""), {"language": res.get("language"), "model": kwargs["path_or_hf_repo"]}


def _transcribe_faster(audio: Path, model: str | None, language: str | None) -> tuple[str, dict]:
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

    segments, info = m.transcribe(str(audio), language=language)
    text = "\n".join(seg.text.strip() for seg in segments)
    meta = {"language": info.language, "model": name, "device": device}
    if gpu_error:
        meta["gpu_fallback_reason"] = gpu_error
    return text, meta


def handle_audio_video(
    path: Path,
    kind: SourceKind,
    model: str | None = None,
    language: str | None = None,
) -> TextResult:
    """音频/视频 → 文字。视频先抽音轨（临时文件用完必清）。"""
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
            text, meta = _transcribe_mlx(audio_path, model, language)
        else:
            text, meta = _transcribe_faster(audio_path, model, language)
    finally:
        # 无论转写成败都清理抽出的临时音轨，避免 /tmp 堆积
        if tmp_to_clean is not None:
            shutil.rmtree(tmp_to_clean, ignore_errors=True)

    meta["filename"] = path.name
    if not text.strip():
        warnings.append("转写结果为空，音频可能无人声或格式异常。")

    return TextResult(
        text=text.strip(),
        kind=kind,
        backend=backend,
        metadata=meta,
        warnings=warnings,
    )
