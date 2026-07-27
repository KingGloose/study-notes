---
name: kg-xiaoyuzhou
description: 小宇宙播客单集摄入：解析元信息和 shownotes（含时间戳大纲，零成本白拿），可选下载音频用本地 ASR 转写逐字稿，存入 raw/ 后由 AI 解析并按 LLM Wiki 契约沉淀。当主人给出小宇宙链接（xiaoyuzhoufm.com/episode/...）、说「解析这集播客」「把这个播客存进知识库」「这期讲了什么」时使用。转写委托底层库 kg-media-to-text。不负责 B站视频（走 kg-bilibili）、公众号（走 kg-wechat）、本地文档（走 kg-doc）。
---

# kg-xiaoyuzhou · 小宇宙播客消化

把主人想听但没时间听的播客，转成可读文字，AI 解析后按 `AGENTS.md` 沉淀进 `wiki/`。

## 何时用

- 「解析这集播客 <小宇宙链接>」
- 「这期讲了什么，值得听吗」
- 「把这集存进知识库」

## 核心策略：先白拿 shownotes，按需才转写

播客动辄 1-2 小时，全量转写有成本。**分两档处理**：

| 档位 | 命令 | 耗时 | 拿到什么 |
|------|------|------|----------|
| **档1 · 白拿**（默认先做） | 不加参数 | 数秒 | 标题/播客/时长/发布日期 + **shownotes（多数含完整时间戳大纲和嘉宾信息）** |
| **档2 · 转写** | `--transcribe` | 约 音频时长/12 | 上述 + 本地 ASR 逐字稿 |

**很多时候档1 就够了**——shownotes 的时间戳大纲已能让你判断这期讲什么、值不值得深入。只在"这期真的重要、需要细节"时才上档2。

## 环境

见 `../README.md`。本 skill 需要：
- 档1：`base`
- 档2：额外 `asr-mac.txt`（Mac）或 `asr-linux.txt`（WSL）+ ffmpeg

```bash
cd 学习笔记/skills && source .venv/bin/activate && cd kg-xiaoyuzhou
```

## 用法

```bash
# 档1：元信息 + shownotes，存入 raw/（返回路径）
python scripts/ingest_episode.py "https://www.xiaoyuzhoufm.com/episode/xxxx"

# 预览不落盘（判断价值时用）
python scripts/ingest_episode.py "<链接>" --stdout

# 档2：连带下载音频 + 本地转写
python scripts/ingest_episode.py "<链接>" --transcribe

# 其他
--model <名>      指定 ASR 模型
--keep-audio      转写后保留音频（默认删）
--out <路径>      自定义输出位置
```

## 工作流（遵守 AGENTS.md）

1. 主人给链接 → 跑**档1**，拿 shownotes。
2. **和主人一起判断**：看标题/大纲/嘉宾，这期值不值得深入？
   - 不值得 → 到此为止，最多在 `index.md` 记个关键词。
   - 值得但大纲已够 → 直接基于 shownotes 讨论沉淀。
   - 值得且要细节 → 跑**档2**转写，产物落 `raw/xyz-<日期>-<标题>.md`。
3. 读 raw 做 AI 解析，按 `AGENTS.md` 判断沉淀方式：
   - 纯通用知识 → 只进 `index.md` 唤醒。
   - 有个人判断/项目上下文/独特理解 → 写 `wiki/` 领域页 + 双链 `[[...]]`。
   - **多人对谈要注意**：当前逐字稿**不区分说话人**，AI 解析时靠内容和称呼推断，不确定就说不确定，别编造"谁说的"。
4. 追加 `log.md` 一条。

## 边界与坑

- **不用登录**：单集公开页面直接解析 `__NEXT_DATA__`，无需 cookie，安全。
- **不碰官方逐字稿 API**：小宇宙有 `transcript` 字段但取用需鉴权（401），且社区警告**用登录 token 抓小宇宙可能触发封号**，故本 skill 一律走"本地 ASR"，不使用登录态。
- **不做批量**：只处理单集公开链接，不抓整个播客历史（风控风险）。
- **说话人分离未实现**：多人对谈的逐字稿是连续文本，不标注谁在说。如需精确区分需接 diarization（pyannote/FunASR），属后续增强项。
- **长音频耐心**：实测 M4 上约 12 倍实时（2 分钟音频约 10 秒）。2 小时的节目约需 11 分钟转写。
- 音频临时下载后默认删除，不占空间（`--keep-audio` 可保留）。

## 已验证

- 《#153. AI编程》（牛油果烤面包，2:10:59）：档1 拿到 1187 字 shownotes（含完整时间戳大纲、嘉宾名单）；音频 82MB 下载 24 秒；2 分钟片段转写 10.3 秒，中英混杂术语（code review / vibe coding）识别准确。
