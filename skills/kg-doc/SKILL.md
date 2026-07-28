---
name: kg-doc
description: 把本地文档（PDF / Word / PPT / Excel / txt / md）、整个文件夹（批量）或普通网页 URL 解析成 Markdown 存入 raw/，再由 AI 解析并按 LLM Wiki 契约沉淀进知识库。当主人给出本地文档路径、文件夹、技术博客链接，说「把这个 PDF 存进知识库」「解析这份文档」「这个文件夹里的 PDF 都处理一下」「这篇博客存一下」时使用。转换委托底层库 kg-media-to-text（PDF 走 Docling 含 OCR、Office 走 MarkItDown）。不负责网页/公众号（走 kg-wechat）、B站视频（走 kg-bilibili）、播客（走 kg-xiaoyuzhou）。
---

# kg-doc · 本地文档消化

把主人手上的文档转成干净 Markdown，AI 解析后按 `AGENTS.md` 沉淀进 `wiki/`。

## 何时用

- 「把这个 PDF 存进知识库 `/path/xx.pdf`」
- 「这个文件夹里的文档都处理一下」→ 批量（`--batch`，带断点续传）
- 「这篇技术博客存一下 <链接>」→ 网页抓取（公众号请用 kg-wechat）
- 「解析这份文档」「这个 Word/PPT/Excel 转一下」
- 需要先看看文档讲什么再决定要不要沉淀

## 环境

见 `../README.md`。本 skill 需要：`base` + `doc` + 底层库 editable 安装。

```bash
cd 学习笔记/skills && source .venv/bin/activate && cd kg-doc
```

## 用法

```bash
# 单文件 → 存入 raw/（返回输出路径）
python scripts/ingest_doc.py /path/to/文件.pdf

# 只预览不落盘（判断价值时用）
python scripts/ingest_doc.py /path/to/文件.pdf --stdout

# 批量处理文件夹（递归，已处理过的自动跳过 = 断点续传）
python scripts/ingest_doc.py /path/to/文件夹 --batch
python scripts/ingest_doc.py /path/to/文件夹 --batch --ext pdf,docx   # 限定类型
python scripts/ingest_doc.py /path/to/文件夹 --batch --force          # 强制重跑

# 网页（普通技术博客；自动跟随 HTTP 与 meta 跳转）
python scripts/ingest_doc.py "https://blog.example.com/post"

# 自定义输出位置/标题（单文件、URL 有效）
python scripts/ingest_doc.py /path/to/x.docx --out ../../raw/自定义.md --title "我的标题"
```

参数：`--batch` 批量 | `--ext` 限定扩展名 | `--force` 覆盖已有 | `--stdout` 预览 | `--out` 输出路径 | `--title` 标题

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
- **批量前先单跑一个抽查质量**，别一次跑几十个才发现提取有问题。批量支持断点续传，中断后重跑会跳过已完成的。
- **网页提取是启发式的**（优先 `<article>`/`<main>`，否则取文字最多的容器），可能含残留导航或漏段，产物头部已标注提醒。JS 渲染的页面可能抓不到正文。
- 公众号链接虽然也能抓，但**建议用 kg-wechat**（有图片防盗链处理和公众号专属元信息），脚本会给出提示。

## 已验证

- 单文件：11 页 jsPDF 图片型中文 PDF → Docling+RapidOCR，8226 字符，标题/表格/链接正确还原（二次约 30 秒）；md/csv/xlsx 均通过。
- 批量：3 个文件（md/md/csv）全部成功，正确跳过非目标类型（.log）；重跑时 3 个全部跳过（断点续传生效）；`--ext csv --force` 正确只处理 1 个。
- 网页：Rust 官方博客 8843 字符，标题/代码块/链接完整；`.html → /` 的 meta refresh 跳转能自动跟随。
