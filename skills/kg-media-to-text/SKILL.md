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
to_text(path, language="zh")              # 语言提示（仅音视频）
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
