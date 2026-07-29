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

# initial_prompt 被模型截断到 n_ctx // 2 - 1 tokens（whisper n_text_ctx=448 → **223**），
# 而且是从**尾部**保留。实测裸塞一整段 shownotes（1811 tokens，超 8 倍）会把模型
# 搞崩：输出退化成“路路路路…”且专名命中 0/7。所以热词必须限长。
# 留余量：标点引导句约 30 tokens，热词预算取 120，不把 223 吃满。
PROMPT_TOKEN_LIMIT = 223
HOTWORD_TOKEN_BUDGET = 120


def _fmt_hotwords(hotwords: list[str] | None) -> str:
    """热词 → 引导语。**必须把词放进真正的句式位置，不能堆成列表。**

    initial_prompt 是“上文续写”通道：模型模仿“前一段话长什么样”，而不是查词表。
    四种写法的实测结果（同一段音频，看人名“携隐”能否纠对）：

        携隐Melody、纵横四海、斯坦福商学院。                    → ✗
        本段话里提到了携隐Melody，纵横四海，…。                 → ✗
        大家好，欢迎来到纵横四海。今天要聊的是携隐Melody、…。  → ✗（人名在列表里）
        大家好，欢迎来到纵横四海，**我是**携隐Melody。           → ✓ **纠对**

    结论：词必须出现在它在真实语音里会出现的**同类句式位置**上（人名跟在
    “我是…”后面、节目名跟在“欢迎来到…”后面），才能真正影响解码。
    所以上层传 hotwords 时需区分类型：用 dict 形式传（见 hotwords 参数说明）。
    """
    return _fmt_hotwords_typed({"topics": list(hotwords or [])})


def _fmt_hotwords_typed(groups: dict) -> str:
    """按类型把热词编进对应句式。

    groups 可含：
      channel : 节目/频道名  → “欢迎来到X”
      speakers: 人名（主播/UP主/嘉宾）→ “我是X” / “今天的嘉宾是X”
      topics  : 其他专名（书名/机构/术语）→ “今天要聊的是X”
    """
    def clean(lst):
        out, seen = [], set()
        for w in lst or []:
            w = (w or "").strip()
            if w and w not in seen:
                seen.add(w)
                out.append(w)
        return out

    channel = clean(groups.get("channel"))
    speakers = clean(groups.get("speakers"))
    topics = clean(groups.get("topics"))

    sents: list[str] = []
    budget = HOTWORD_TOKEN_BUDGET

    def add(sent: str) -> None:
        nonlocal budget
        cost = _rough_tokens(sent)
        if cost <= budget:
            sents.append(sent)
            budget -= cost

    # 人名和节目名合成一句开场白（实测最有效的形态）
    if channel and speakers:
        add(f"大家好，欢迎来到{channel[0]}，我是{speakers[0]}。")
        speakers = speakers[1:]
    elif channel:
        add(f"大家好，欢迎来到{channel[0]}。")
    elif speakers:
        add(f"大家好，我是{speakers[0]}。")
        speakers = speakers[1:]

    # 剩下的人名当嘉宾介绍（同样是“人名位置”）
    if speakers:
        add("今天的嘉宾是" + "和".join(speakers[:3]) + "。")

    # 其他专名：逐个加到预算用完
    if topics:
        kept = []
        for w in topics:
            trial = "今天要聊的是" + "、".join(kept + [w]) + "。"
            if _rough_tokens(trial) > budget:
                break
            kept.append(w)
        if kept:
            add("今天要聊的是" + "、".join(kept) + "。")

    return "".join(sents)


def _rough_tokens(text: str) -> int:
    """粗估 token 数（不依赖 tokenizer，避免为了数个数去加载模型）。

    中文约 1 字 1 token，拉丁/数字约 4 字符 1 token。宁可高估。
    """
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
    other = len(text) - cjk
    return cjk + other // 3 + 1


def _build_prompt(
    language: str | None,
    initial_prompt: str | None,
    hotwords: list[str] | dict | None,
) -> str | None:
    """组装最终 prompt：热词引导句 + 标点引导句，并卡总预算。

    initial_prompt 为显式传入时完全尊重调用方（传 "" 即禁用）。
    hotwords 可以是 list（全当 topics）或 dict（区分 channel/speakers/topics，效果更好）。
    """
    if initial_prompt is not None:
        return initial_prompt or None

    is_zh = bool(language and language.lower().startswith("zh"))
    parts = []
    if isinstance(hotwords, dict):
        hot = _fmt_hotwords_typed(hotwords)
    else:
        hot = _fmt_hotwords(hotwords)
    if hot:
        parts.append(hot)
    if is_zh:
        parts.append(ZH_PUNCT_PROMPT)
    if not parts:
        return None

    prompt = "".join(parts)
    # 守住硬上限：若超出则优先牺牲热词（标点引导是可读性的命根子，不能丢）
    if _rough_tokens(prompt) > PROMPT_TOKEN_LIMIT:
        prompt = ZH_PUNCT_PROMPT if is_zh else ""
    return prompt or None


def _default_prompt(language: str | None) -> str | None:
    """向后兼容的薄封装（旧调用方可能在用）。"""
    return _build_prompt(language, None, None)


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
    hotwords: list[str] | None = None,
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
    prompt = _build_prompt(language, initial_prompt, hotwords)
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
        "hotwords": len(hotwords or []),
    }
    return text, meta


def _transcribe_faster(
    audio: Path,
    model: str | None,
    language: str | None,
    initial_prompt: str | None = None,
    timestamps: bool = True,
    hotwords: list[str] | None = None,
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

    prompt = _build_prompt(language, initial_prompt, hotwords)
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
        "hotwords": len(hotwords or []),
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
    hotwords: list[str] | None = None,
) -> TextResult:
    """音频/视频 → 文字。视频先抽音轨（临时文件用完必清）。

    language="zh" 时默认注入标点引导 prompt（见 ZH_PUNCT_PROMPT）；
    hotwords 会被包成自然句式一并注入（见 _fmt_hotwords）。
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
                audio_path, model, language, initial_prompt, timestamps, hotwords
            )
        else:
            text, meta = _transcribe_faster(
                audio_path, model, language, initial_prompt, timestamps, hotwords
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
