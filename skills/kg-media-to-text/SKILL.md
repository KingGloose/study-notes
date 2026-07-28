---
name: kg-media-to-text
description: 底层核心库（非用户直接调用）：把任意素材转成文字。按类型分流——PDF 走 Docling、Office 走 MarkItDown、音视频走本地 Whisper（macOS 用 mlx-whisper / Linux 用 faster-whisper 自动选）、txt/md 直接读。供上层业务 skill（kg-bilibili / kg-wechat / kg-xiaoyuzhou / kg-doc）在代码中 import 调用，不面向用户唤起。
disable-model-invocation: true
---

# kg-media-to-text · 素材 → 文字 底层库

**定位**：这是被上层业务 skill **代码调用**的共享库，不是给用户唤起的技能。
它只回答一个问题：给我任意素材，还你文字。**平台无关、不懂业务、不做沉淀**。

沉淀逻辑（按 AGENTS.md 进 raw/wiki/index/log）属于上层业务 skill 的职责，本库不涉及。

## 环境

见 `../README.md`（统一环境）。本库需要：
- 文档能力：`requirements/doc.txt`
- 转写能力：`requirements/asr-mac.txt`（Mac）或 `asr-linux.txt`（WSL），视频还需 ffmpeg

## API

对外只有一个入口：

```python
from media_to_text import to_text

r = to_text("/path/to/任意文件")

r.text          # 提取的纯文字 / Markdown
r.kind          # SourceKind.PDF / AUDIO / ...
r.backend       # 实际用的后端：docling / markitdown / mlx-whisper / faster-whisper / builtin
r.metadata      # 页数、时长、语言、模型等（按类型不同）
r.warnings      # 非致命提示（如"疑似扫描件未提取到文字"）
r.is_empty      # 是否没提取到内容
```

可选参数：

```python
to_text(path, kind=SourceKind.PDF)        # 强制类型（跳过自动探测）
to_text(path, model="large-v3")           # 指定 ASR 模型（仅音视频）
to_text(path, language="zh")              # 语言提示（仅音视频）——**中文必传**
to_text(path, timestamps=False)           # 不要时间戳（仍按语义分行）
to_text(path, initial_prompt="...")       # 自定义 ASR 引导词（"" 可禁用内置的）
```

### 中文转写必读：为何必须传 `language="zh"`

Whisper 是自回归模型，会随机陷入**「无标点模式」**，中文尤其严重。实测同一段 2 分钟
中文播客：

| 调用方式 | segment 数 | 标点数 | 可读性 |
|---|---|---|---|
| 不传 language | 4（30s 大块） | **0** | 几万字连成一堵墙，人类不可读 |
| 传 `language="zh"`（现默认） | 9（语义段） | **64** | 带标点 + 分行 + 时间戳 |

本库已在 `language` 以 `zh` 开头时自动注入内置的标点引导 prompt；**不传 language 就不会注入**
（此时会在 `warnings` 里明确告警）。

**initial_prompt 踩坑（实测）**：prompt 里不要写冒号、不要写“例如”“请保留标点”这类
**元指令**，也不要塞示范句——模型会把它们当成上文内容续写，输出里会混进「Ｂ」
这种全角垃圾字符（本库第一版就踩了这个坑）。只给平实的陈述句。

### 输出形态

音视频转写**永远按 segment 分行**，不会返回无换行的一整块（不要用 whisper 原始的
`res["text"]`，那是裸拼接）。中文行内的半角标点会归一化为全角（`,`→`，`），
但不会误伤英文句子和小数（`large-v3, turbo`、`98.5%` 保持原样）。

```
[00:00] 就是也合得来啊。可是呢，时间一长就会觉得说，约出来就是吃吃喝喝闲聊八卦。
[00:23] 这就是为什么有时候你觉得朋友间的谈话也很有意思啊，话题也很多元啊。
```

## 支持矩阵

| 素材 | 后端 | 说明 |
|------|------|------|
| PDF | Docling | 版面感知，表格/公式保真；扫描件自动 OCR（RapidOCR） |
| docx/pptx/xlsx/csv | MarkItDown | Office 系转 Markdown |
| txt/md | 内置 | 直接读，自动试 utf-8/gbk/latin-1 |
| 音频(mp3/m4a/wav/flac...) | mlx-whisper(Mac) / faster-whisper(Linux) | 平台自动选 |
| 视频(mp4/mkv/mov...) | 同上 + ffmpeg | 先抽音轨再转写，**画面内容不处理** |
| 图片 | ✗ 未实现 | OCR 属规划中的 L2 能力，会抛 UnsupportedSourceError |

## 内部结构

```
media_to_text/
├── __init__.py          只导出 to_text / detect_kind / 类型
├── detect.py            类型探测（扩展名优先 + magic bytes 兜底）
├── router.py            分流调度（唯一入口逻辑）
├── types.py             TextResult 契约 + 异常
└── handlers/
    ├── document.py      Docling / MarkItDown / 纯文本
    └── audio.py         ASR，含平台检测(pick_backend)与 ffmpeg 抽音轨
```

## 设计原则

1. **薄调度层**：核心转换全部委托给社区最成熟的库，本库只做探测、分流、统一接口。
2. **平台差异内聚在 handler**：`audio.py` 内部判断 Mac/Linux 选后端，上层与其他 handler 无感。
3. **依赖可选**：缺依赖时抛 `MissingDependencyError` 并提示装哪个 requirements 文件，不强迫一次装全套。
4. **统一契约**：任何素材都返回 `TextResult`，上层处理方式一致。

## 已验证

- **PDF**（jsPDF 生成的图片型中文 PDF，11 页）→ Docling + RapidOCR，8226 字符，标题层级/表格/链接正确还原。M4 上首次约 5 分钟（含下模型），二次约 30 秒（约 2.7 秒/页）。
- **音频**（7 秒中文）→ mlx-whisper + large-v3-turbo，转写**完全准确**。首次约 11 分钟（下模型 1.5GB），二次 **4.4 秒**。
- **视频**（含同音轨）→ 自动 ffmpeg 抽音轨后转写，结果一致，正确返回“画面未处理” warning。
- **平台检测**：M4 Mac 正确返回 `mlx-whisper`，MLX 设备为 GPU(Metal)。
- **类型探测 / 纯文本直读 / 图片未实现报错**：均通过。

> 模型缓存在 `~/.cache/huggingface`（仓库外，不影响 git），首次下载后复用。

## 边界

- 不做沉淀（那是上层 skill 的事）
- 不做图片 OCR（L2，未实现）
- 视频只处理音轨，不理解画面
