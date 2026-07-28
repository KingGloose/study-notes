---
name: kg-youtube
description: YouTube 视频摄入：优先白拿官方/自动字幕（零算力成本），无字幕才本地 ASR 转写，含元信息与简介，存入 raw/ 后由 AI 解析并按 LLM Wiki 契约沉淀。当主人给出 YouTube 链接或视频 ID、说「解析这个视频」「这个演讲讲了什么」「把这个 YouTube 存进知识库」时使用。转写委派底层库 kg-media-to-text。不负责 B站（走 kg-bilibili）、播客（走 kg-xiaoyuzhou）、公众号（走 kg-wechat）、本地文档（走 kg-doc）。
---

# kg-youtube · YouTube 视频消化

把 YouTube 上的技术演讲/教程转成可读文字，AI 解析后按 `AGENTS.md` 沉淀进 `wiki/`。

## 何时用

- 「解析这个视频 <YouTube 链接>」
- 「这个演讲讲了什么」
- 「把这个 YouTube 存进知识库」

## 为什么 YouTube 比 B站更划算

**字幕覆盖率高得多**：YouTube 有官方人工字幕 + 157 种自动字幕（含自动翻译），
绝大多数视频都能走 **L0 白拿**（直接搬运平台已生成的文字，零本地算力）。
B站很多视频没有 CC/AI 字幕，得走 ASR。

## 环境

见 `../README.md`。本 skill 需要：
- 字幕路径（多数情况）：`asr-mac.txt` 或 `asr-linux.txt` —— **只为其中的 yt-dlp**
- ASR 兜底：额外需要 ffmpeg

```bash
cd 学习笔记/skills && source .venv/bin/activate && cd kg-youtube
```

## 用法

```bash
# 默认：按语言优先级找字幕，找不到才本地转写
python scripts/ingest_video.py "https://www.youtube.com/watch?v=xxxx"
python scripts/ingest_video.py xxxxxxxxxxx          # 直接给 11 位视频 ID 也行

# 指定字幕语言优先级（默认 zh-Hans,zh-CN,zh,en,en-orig）
python scripts/ingest_video.py "<链接>" --lang en
python scripts/ingest_video.py "<链接>" --lang zh-Hans,en

# 跳过字幕，强制本地 ASR（字幕质量差时用）
python scripts/ingest_video.py "<链接>" --asr

# 预览不落盘 / 自定义输出
python scripts/ingest_video.py "<链接>" --stdout
python scripts/ingest_video.py "<链接>" --out ../../raw/自定义.md
```

## 工作流（遵守 AGENTS.md）

1. 主人给链接 → 跑脚本。脚本会先报告有哪些字幕语言可用。
2. 拿到文本后**先和主人讨论**：这个视频讲了什么、值不值得沉淀。
   - 产物落 `raw/yt-<视频ID>-<标题>.md`，头部含频道/时长/上传日期/播放量/**文本来源**（字幕 or ASR）做溯源。
3. 按 `AGENTS.md` 判断沉淀方式：
   - 纯通用知识 → 只在 `index.md` 补唤醒关键词。
   - 有个人判断/项目上下文/独特理解 → 写 `wiki/` 领域页 + 双链 `[[...]]`。
4. 追加 `log.md` 一条。

## 边界与坑

- **429 限流**：一次请求多个字幕语言容易被 YouTube 限流。脚本因此**逐个语言尝试、拿到就停**，
  遇到 429 会跳过该语言继续下一个（实测有效）。别改成一次请求多语言。
- **自动字幕 ≠ 人工字幕**：脚本每种语言先试人工（`--write-subs`）再试自动（`--write-auto-subs`），
  产物头部标注了实际来源（如 `字幕 en(自动)`）。自动字幕无标点、可能有识别错误，解析时注意。
- **自动翻译字幕质量差**：`xx-en`（从英文自动翻译）这类语言标记的字幕是机翻，
  宁可用原文 `en` 让 AI 直接读英文，别用机翻中文。
- **VTT 清理**：YouTube 自动字幕带内联时间标签 `<00:00:19><c>` 和滚动重复行，脚本已清理。
- **yt-dlp 警告 JS runtime**：会提示缺 deno 等 JS 运行时导致"部分格式缺失"。
  抓字幕和音频不受影响，可忽略。
- **私有/受限视频**：需登录或地区限制的会失败，脚本给出明确提示（本 skill 不处理登录态）。
- **ASR 不区分说话人**：多人对谈的转写是连续文本，解析时不确定谁在说就说不确定。

## 已验证

- 人工字幕路径：`dQw4w9WgXcQ` → 2066 字符，元信息完整（频道/时长/播放量/上传日期）。
- 自动字幕路径：`BKorP55Aqvg` → 5904 字符。
- 429 限流处理：请求 zh-Hans 触发 429 后正确跳过、降级到 en 人工字幕成功。
- VTT 清理：无内联时间标签、无 `<c>` 标签、无滚动重复行残留。
- 边界：无效视频 ID 给明确报错；纯 11 位 ID 输入能自动补全 URL；无临时文件泄漏。
