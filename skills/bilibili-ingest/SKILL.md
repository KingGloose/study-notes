---
name: bilibili-ingest
description: 读取用户 B 站「稍后再看」/收藏夹，抓取视频字幕（CC/AI），交由 AI 解析后按 LLM Wiki 契约沉淀进学习笔记库。当主人想「让 AI 消化我稍后再看的视频」「挑几个视频做成笔记」「解析某个 B 站视频」时使用。侧重编程/技术类科普内容。不负责无字幕视频的语音转写（Whisper 兜底后续再加）。
---

# bilibili-ingest · B 站视频消化 skill

把主人稍后再看/收藏里的视频，抓成文字，让 AI 解析，最终按 `AGENTS.md` 的 Ingest 流程沉淀进 `wiki/`。

## 何时用

- 「今天帮我挑几个视频消化」→ 形态 1(每日精选)
- 「解析这个视频 <链接>」→ 形态 2(指定视频)
- 「我稍后再看里有啥值得看的」→ 只列表 + 筛选

## 前置：环境准备（首次 / 迁移到新机器时）

脚本依赖一个本地 venv，**代码随库走，环境各机器本地重建**。`.venv/` 和 `.env` 都已被 git 忽略。

### macOS

```bash
cd 学习笔记/skills/bilibili-ingest
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Windows / WSL

WSL(推荐，和 Mac 命令一致)：

```bash
cd 学习笔记/skills/bilibili-ingest
python3 -m venv .venv          # 建议 WSL 里用 Python 3.10+
source .venv/bin/activate
pip install -r requirements.txt
```

纯 Windows(PowerShell)：

```powershell
cd 学习笔记\skills\bilibili-ingest
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

> 版本要求：Python **3.9+**（Mac 自带 3.9.6 刚好可用；新机器建议 3.10+ 更稳）。
> 核心依赖：`bilibili-api-python`(接口封装) + `curl_cffi`(HTTP client，绕风控) + `python-dotenv`。
> 注意：`bilibili-api-python` 的 HTTP client 是可插拔的，裸装不带 client，脚本已在 `_common.select_http_client()` 里注册并选中 `curl_cffi`，无需手动配置。

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
```

## 工作流

### 形态 2：指定视频（先跑通这个）

1. 主人给链接/BV 号。
2. `get_transcript.py <url>` 抓字幕。
   - 有字幕 → 把纯文本存进 `raw/`（文件名如 `raw/bili-<bvid>-<标题>.md`，开头记链接/UP主/抓取日期做溯源）。
   - `has_subtitle=false` → 明确告诉主人「这个视频没字幕」，暂不硬处理（Whisper 兜底后续再加）。
3. 读 `raw/` 里的转写，向主人做 AI 解析：讲清楚讲了什么、关键结论、和主人已有知识的关联。
4. 按 `AGENTS.md` 判断沉淀方式：
   - 纯通用知识 → 只在 `index.md` 补唤醒关键词。
   - 有个人判断/项目上下文/踩坑/独特理解 → 写 `wiki/` 对应领域页，主动建双链 `[[...]]`。
5. 追加 `log.md` 一条。

### 形态 1：每日精选 5 个

1. `list_videos.py toview` 拉稍后再看（收藏用 `favlist` + `fav`）。
2. **筛选口径**（主人已定）：
   - 优先级最高：**编程/技术相关**（看标题、UP主、`tname` 分区，如「科技」「计算机技术」「编程」等）。
   - 次之：其他知识/科普类。
   - 基本排除：娱乐、游戏实况、Vlog 等非知识向。
   - **不卡时长**，「合适、值得消化」为准。
3. 选出候选（约 5 个）给主人过目，附标题/UP主/时长/一句话理由，让主人拍板选几个。
4. 对选中的逐个走「形态 2」的第 2~5 步。

## 边界与坑

- 无字幕视频：当前不处理，标记出来。Whisper 兜底是明确的后续项，不要偷偷本地转写。
- 鉴权失败/风控：多半是 `SESSDATA` 过期，让主人重填 `.env`。
- 批量拉取别太猛，B 站有频率限制。
- 处理图片/长文时遵守 `AGENTS.md`：优先文字和代码，少截图；通用知识只进 index 不写详细页。
