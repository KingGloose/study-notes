---
name: kg-doc
description: 把本地文档（PDF / Word / PPT / Excel / txt / md）解析成 Markdown 存入 raw/，再由 AI 解析并按 LLM Wiki 契约沉淀进知识库。当主人给出本地文档路径、说「把这个 PDF 存进知识库」「解析这份文档」「这个 Word 转一下」时使用。转换委托底层库 kg-media-to-text（PDF 走 Docling 含 OCR、Office 走 MarkItDown）。不负责网页/公众号（走 kg-wechat）、B站视频（走 kg-bilibili）、播客（走 kg-xiaoyuzhou）。
---

# kg-doc · 本地文档消化

把主人手上的文档转成干净 Markdown，AI 解析后按 `AGENTS.md` 沉淀进 `wiki/`。

## 何时用

- 「把这个 PDF 存进知识库 `/path/xx.pdf`」
- 「解析这份文档」「这个 Word/PPT/Excel 转一下」
- 需要先看看文档讲什么再决定要不要沉淀

## 环境

见 `../README.md`。本 skill 需要：`base` + `doc` + 底层库 editable 安装。

```bash
cd 学习笔记/skills && source .venv/bin/activate && cd kg-doc
```

## 用法

```bash
# 转换并存入 raw/（默认，返回输出路径）
python scripts/ingest_doc.py /path/to/文件.pdf

# 只预览不落盘（判断价值时用）
python scripts/ingest_doc.py /path/to/文件.pdf --stdout

# 自定义输出位置/标题
python scripts/ingest_doc.py /path/to/x.docx --out ../../raw/自定义.md --title "我的标题"
```

支持：`.pdf` `.doc/.docx` `.ppt/.pptx` `.xls/.xlsx/.csv` `.txt` `.md`
（底层自动分流：PDF→Docling，Office→MarkItDown，纯文本→直读）

## 工作流（遵守 AGENTS.md）

1. 主人给文档路径。
2. **先预览判断价值**：`--stdout` 看内容，和主人讨论这文档值不值得沉淀、重点在哪。
3. 决定沉淀 → 不带 `--stdout` 正式跑，产物落 `raw/doc-<日期>-<名>.md`（头部自带来源路径/类型/后端/页数/摄入日期做溯源）。
4. 读 raw 内容做 AI 解析，按 `AGENTS.md` 判断：
   - 纯通用知识 → 只在 `index.md` 补唤醒关键词。
   - 有个人判断/项目上下文/踩坑/独特理解 → 写 `wiki/` 对应领域页，主动建双链 `[[...]]`。
   - 明确区分「文档里写的」和「AI 补充的」。
5. 追加 `log.md` 一条。

## 注意事项

- **敏感文档**（简历、合同、内部材料、含个人信息的）：解析可以做，但沉淀进 wiki 前先问主人；不要把个人隐私信息摘录到对话或笔记里。
- **扫描件/图片型 PDF**：Docling 会自动 OCR（RapidOCR），中文可用。若结果为空脚本会报错而非写空文件。
- **首次运行慢**：Docling 要下版面/OCR 模型（几百 MB），之后走缓存。11 页 PDF 二次约 30 秒。
- **图片**：文档里的插图当前不提取（图片 OCR 属未实现的 L2 能力）。需要图时手动截图存 `assets/`。
- 大文档（几十页以上）建议先 `--stdout | head` 抽查质量再全量落盘。
