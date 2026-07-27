---
name: kg-bilibili
description: 读取用户 B 站「稍后再看」/收藏夹，抓取视频字幕（CC/AI），交由 AI 解析后按 LLM Wiki 契约沉淀进学习笔记库。当主人想「让 AI 消化我稍后再看的视频」「挑几个视频做成笔记」「解析某个 B 站视频」时使用。**领域不限**：技术、话术沟通、心理、商业财经、人文历史、健康、生活技艺等一切知识向内容都在范围内。无字幕视频可用 --asr 走本地转写（委派底层库 kg-media-to-text）。不负责公众号（走 kg-wechat）、播客（走 kg-xiaoyuzhou）、本地文档（走 kg-doc）。
---

# kg-bilibili · B 站视频消化 skill

把主人稍后再看/收藏里的视频，抓成文字，让 AI 解析，最终按 `AGENTS.md` 的 Ingest 流程沉淀进 `wiki/`。

## 何时用

- 「今天帮我挑几个视频消化」→ 形态 1(每日精选)
- 「解析这个视频 <链接>」→ 形态 2(指定视频)
- 「我稍后再看里有啥值得看的」→ 只列表 + 筛选

## 前置：环境准备

**环境已统一到 `skills/.venv`，安装步骤见 [`../README.md`](../README.md)。**
本 skill 需要：`base` + `bilibili`（无字幕视频要转写则额外 `asr-mac`/`asr-linux` + 底层库 + ffmpeg）。

```bash
cd 学习笔记/skills && source .venv/bin/activate && cd kg-bilibili
```

### 配置 cookie（跨平台通用，一次性）

个人数据(稍后再看/收藏)和字幕都需要 B 站登录态。有两种方式，任选其一：

**方式 A：扫码登录（推荐，最省事）**

```bash
python scripts/login.py
```

运行后会在 skill 目录生成 `qrcode.png`（同时终端也打印 ANSI 二维码）。用手机 B 站 APP 扫码确认，脚本自动把 cookie 写进 `.env`，成功后删掉二维码图片。终端 ANSI 二维码在部分环境无法扫描时，直接打开 `qrcode.png` 扫即可。

**方式 B：手动填 `.env`**

1. 浏览器登录 B 站 → F12 → Application → Cookies → `https://www.bilibili.com`
2. 复制 `SESSDATA`(必填)、`bili_jct`、`buvid3` 的值
3. 复制模板并填入：

```bash
cp .env.example .env    # Windows: copy .env.example .env
```

4. 编辑 `.env` 填三个值。

> `SESSDATA` 有效期约一个月，报鉴权错误时重新扫码（方式 A）或重填一次即可。
> 迁移新机器：`.env` 不进 git，需在新机器重新扫码/填一次（或手动拷过去）。

## 脚本用法

所有命令先 `source .venv/bin/activate`（Windows 用对应激活方式）。脚本 stdout 是纯 JSON/文本，进度打在 stderr。

```bash
# 扫码登录（首次/换机器/cookie 过期时）
python scripts/login.py

# 稍后再看列表
python scripts/list_videos.py toview

# 我的所有收藏夹（拿 media_id）
python scripts/list_videos.py favlist

# 某个收藏夹内容（media_id 来自上一步），可带页码
python scripts/list_videos.py fav <media_id> [页数]

# 抓某个视频的字幕（纯文本）
python scripts/get_transcript.py <bvid或视频URL>

# 抓字幕（结构化 JSON，含分P/分区/简介）
python scripts/get_transcript.py <bvid或视频URL> --json

# 无字幕视频：下音频本地 ASR 转写（需 asr 依赖 + ffmpeg，约 12 倍实时）
python scripts/get_transcript.py <bvid> --asr
python scripts/get_transcript.py <bvid> --asr --model large-v3
```

## 工作流

### 形态 2：指定视频（先跑通这个）

1. 主人给链接/BV 号。
2. `get_transcript.py <url>` 抓字幕。
   - 有字幕 → 把纯文本存进 `raw/`（文件名如 `raw/bili-<bvid>-<标题>.md`，开头记链接/UP主/抓取日期做溯源）。
   - 无字幕 → 告知主人；征得同意后加 `--asr` 下音频本地转写（L1，委派底层库 kg-media-to-text，自动按平台选 mlx/faster）。
3. 读 `raw/` 里的转写，向主人做 AI 解析：讲清楚讲了什么、关键结论、和主人已有知识的关联。
4. 按 `AGENTS.md` 判断沉淀方式：
   - 纯通用知识 → 只在 `index.md` 补唤醒关键词。
   - 有个人判断/项目上下文/踩坑/独特理解 → 写 `wiki/` 对应领域页，主动建双链 `[[...]]`。
5. 追加 `log.md` 一条。

### 形态 1：每日精选 5 个

1. `list_videos.py toview` 拉稍后再看（收藏用 `favlist` + `fav`）。
2. **筛选口径**（主人已定）：
   - **领域不限，只按「是否知识向」筛，不按「是不是技术」筛。** 主人的知识库涵盖技术、话术与沟通、心理、商业财经、人文历史、健康、生活技艺等多个领域，技术只是其中一块。
   - 判据是**看完能不能带走一个可复用的认知/方法/判断**，而不是题材属于哪个分区。
     - 要：技术解析、话术拆解、心理机制、商业分析、历史脉络、科普、方法论、技艺教程。
     - 不要：纯娱乐消费向（游戏实况、Vlog、音乐/影视纯欣赏、猫狗日常、吃播）——看完只有情绪没有认知。
   - **别被 `tname` 分区骗了**：B站分区很粗，「人文历史」下可能是话术解析，「日常」下可能是硬核技术连载，「野生技能协会」常放原理讲解。**以标题+简介的实际内容为准。**
   - **不卡时长**，「合适、值得消化」为准。
   - 给候选时**主动跨领域搭配**（例如 3 技术 + 2 非技术），不要一次全给同一个领域，否则主人只能在技术里挑。
3. 选出候选（约 5 个）给主人过目，附标题/UP主/时长/一句话理由，让主人拍板选几个。
4. 对选中的逐个走「形态 2」的第 2~5 步。

## 边界与坑

- **无字幕视频**：默认只标注，不自作主张转写；需显式 `--asr`（消耗本地算力）。转写结果标注"可能有识别误差"。
- **ASR 不区分说话人**：多人对谈是连续文本，不知道谁在说。解析时不确定就说不确定。
- **yt-dlp 抓 B 站高清格式不稳**（社区已知问题），但本 skill 只用它 `-x` 抽音轨，不受影响。
- 鉴权失败/风控：多半是 `SESSDATA` 过期，让主人重填 `.env`。
- 批量拉取别太猛，B 站有频率限制。
- 处理图片/长文时遵守 `AGENTS.md`：优先文字和代码，少截图；通用知识只进 index 不写详细页。
- **不要因为内容「不是技术」就降级处理**：非技术领域同样按 Ingest 流程判断，同样可以进 `wiki/`。判断标准永远是「抽掉主人的个人上下文后 AI 还能不能完整答出」，不是题材。
- 非技术内容的沉淀重点不同：技术类核对的是 API/版本是否过时，**话术/心理/商业类核对的是术语归属、案例出处、适用边界和代价**（这类内容最容易漏掉「什么时候不该用、用了有什么副作用」）。

## 已验证

- 稍后再看列表：604 条，字段完整。
- 有字幕视频（L0 白拿）：抓到 27060 字 AI 字幕（`ai-zh`）。
- 无字幕视频 + `--asr`（L1）：3 分钟视频共 25 秒完成（yt-dlp 抽音 1.9MB + mlx-whisper 转写 1350 字），技术术语（线程池/内存溢出/GC Root）识别准确。
