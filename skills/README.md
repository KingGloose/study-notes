# skills · 环境准备（唯一维护点）

所有 skill **共用一个 Python 虚拟环境** `skills/.venv`，依赖按功能/平台分文件按需安装。
各 skill 的 SKILL.md 不再重复写环境步骤，统一看这里。

---

## 1. 架构：底层库 + 上层业务 skill

```
底层（能力层，供上层调用）
  kg-media-to-text/        任意素材 → 文字，按类型分流：
                           PDF→Docling / Office→MarkItDown / 音视频→Whisper(平台自适应)
  kg-browser/              真实 Chrome 读取：带登录态/过 JS 挑战的页面
                           （给 AI 灵活的 CLI 工具 + 站点知识，不写死脚本）

上层（各自独立触发，按 AGENTS.md 沉淀）
  kg-bilibili/             B站：稍后再看 / 收藏 / 字幕 / 无字幕时 ASR 兜底
  kg-wechat/               微信公众号文章
  kg-xiaoyuzhou/           小宇宙播客：shownotes + 可选本地转写
  kg-doc/                  本地文档 / 文件夹批量 / 普通网页 URL
  kg-youtube/              YouTube：字幕优先（覆盖率高）+ ASR 兜底
  kg-zhihu/                知乎：专栏/回答/问题页（依赖 kg-browser）

捕获与学习
  kg-capture/              ★ 跨项目知识捕获（在别的项目里干活时的收获回填进库）
  kg-learn/                ★ 学习模式（陌生领域渐进切入 + 可选学习计划）

使用与维护（不摄入）
  kg-ask/                  ★ 库内检索问答（区分"记过的"vs"AI补充的"）
  kg-review/               知识回顾（先回想再看答案，检验个人判断是否还认同）
  kg-lint/                 体检：孤儿页 / 死链 / raw未沉淀 / index未唤醒
```

> **知识库的价值在被查、被唤醒,不在被写。** `kg-ask` 是查的入口,`kg-review` 是唤醒的入口。

> 目录名与 skill 名一致，均为 `kg-` 前缀（kg = KingGloose，区分自有 skill）。
> `kg-media-to-text` 标了 `disable-model-invocation`，只被代码 import，不会被模型唤起。

上层 skill 通过 `from media_to_text import to_text` 调用底层库。

---

## 2. 首次准备 / 迁移到新机器

### 2.0 一键安装（推荐）

```bash
cd 学习笔记/skills
bash install.sh
```

自动完成：平台探测（macOS / WSL2）→ 检查 uv & ffmpeg → 建 Python 3.12 venv →
按平台装对应依赖（Mac 装 mlx-whisper / Linux 装 faster-whisper）→ 装底层库 →
软链注册到全局 → 5 项自检（--minimal 下 4 项）。**幂等，可重复运行**。

```bash
bash install.sh --minimal   # 只装基础，跳过 Docling(1GB) 和 Whisper 模型(1.5GB)
bash install.sh --no-link   # 不注册到全局
bash install.sh --help
```

装完还需两步：
1. `source .venv/bin/activate`
2. `python kg-bilibili/scripts/login.py`（B 站扫码登录，仅用 B 站功能时需要）

> 纯 Windows（非 WSL）不支持本脚本，请按下方 2.1~2.4 手动安装。

---

### 手动安装（了解细节 / 脚本不适用时）

用 [uv](https://docs.astral.sh/uv/) 管理（比 pip 快一个数量级，且全局缓存去重）。

### 2.1 建统一环境

```bash
cd 学习笔记/skills
uv python install 3.12        # 若本机没有 3.12
uv venv --python 3.12         # 创建 skills/.venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
```

### 2.2 装依赖（按需组合）

```bash
uv pip install -r requirements/base.txt     # 必装：公共 HTTP/解析
uv pip install -e ./kg-media-to-text           # 必装：底层库（editable，改代码立即生效）

# 按要用的功能补装
uv pip install -r requirements/doc.txt       # 文档处理（docling + markitdown，约 1GB 含模型）
uv pip install -r requirements/bilibili.txt  # B站
uv pip install -r requirements/wechat.txt    # 公众号

# ASR（音视频转写）按平台二选一
uv pip install -r requirements/asr-mac.txt    # macOS Apple Silicon（mlx-whisper，Metal 加速）
uv pip install -r requirements/asr-linux.txt  # Linux/WSL2（faster-whisper，CUDA 加速）
```

### 2.3 系统级依赖（不能 pip 装）

| 依赖 | 用途 | macOS | WSL2/Ubuntu |
|------|------|-------|-------------|
| ffmpeg | 视频抽音轨、音频转码 | `brew install ffmpeg` | `sudo apt install ffmpeg` |

### 2.4 注册到全局（让任何目录都能用这些 skill）

pi 默认只扫描 `~/.agents/skills/`、`~/.pi/agent/skills/` 等固定位置。
把本目录软链进去，**任何工作目录下都能唤起 kg-* skill**：

```bash
# macOS / WSL2
ln -s /path/to/学习笔记/skills ~/.agents/skills/kg
```

```powershell
# 纯 Windows（管理员 PowerShell）
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.agents\skills\kg" `
         -Target "C:\path\to\学习笔记\skills"
```

一条软链覆盖全部——pi 会**递归发现**所有含 `SKILL.md` 的子目录，
所以**以后新增 skill 自动生效，不用再补软链**。

验证：

```bash
cd /tmp && pi --print "列出名字以 kg- 开头的 skill"
```

> 已知开销：软链后 pi 启动约慢 2 秒（递归扫描 `skills/.venv`），可接受。
> `kg-media-to-text` 不会出现在列表里是正常的——它标了
> `disable-model-invocation: true`，作为底层库只被代码 import，不该被模型唤起。

---

## 3. 平台差异说明（重要）

**ASR 后端必须按平台选，这是硬约束：**

- **faster-whisper 不支持 Apple MPS**，在 Mac 上只能 CPU 干跑，很慢。
- 所以 macOS 用 **mlx-whisper**（Apple MLX + Metal GPU）；Linux/WSL2 用 **faster-whisper**（CUDA）。
- 底层库 `handlers/audio.py` 会**自动检测平台选后端**，上层代码无需关心。

其余部分（文档处理、HTTP 抓取）两平台完全一致。

---

## 4. 各 skill 需要的依赖

| skill（目录） | 需要的 requirements |
|-------|---------------------|
| kg-media-to-text（文档能力） | base + doc |
| kg-media-to-text（转写能力） | base + asr-mac 或 asr-linux（+ ffmpeg） |
| kg-bilibili | base + bilibili（无字幕视频要 `--asr` 还需 asr-* + ffmpeg） |
| kg-wechat | base + wechat |
| kg-xiaoyuzhou | base（仅 shownotes）；`--transcribe` 还需 asr-* + ffmpeg |
| kg-doc | base + doc（网页抓取还需 wechat 里的 markdownify） |
| kg-youtube | base + asr-*（为其中的 yt-dlp）；ASR 兜底还需 ffmpeg |
| kg-lint | 无额外依赖（纯标准库） |
| kg-ask | 无额外依赖（纯标准库） |
| kg-review | 无额外依赖（纯标准库） |
| kg-capture | 无额外依赖（复用 kg-ask 查重、kg-lint 体检） |
| kg-learn | 无额外依赖（纯标准库） |
| kg-browser | 无 Python 依赖；需 `npm i -g chrome-devtools-mcp@latest` + Chrome 开 remote debugging |
| kg-zhihu | base + wechat(markdownify)；浏览器能力依赖 kg-browser |

---

## 5. 注意事项

- `.venv/`、`.env` 已被 `skills/.gitignore` 忽略，**不进版本库**。代码随库迁移，环境各机器本地重建。
- 各 skill 的 `.env`（如 B 站 SESSDATA）是本机凭证，迁移需重新配置。
- 首次跑文档处理时 Docling 会下载版面/OCR 模型（几百 MB），首次跑转写时下载 Whisper 模型（约 1.5GB），之后走本地缓存。模型存在 `~/.cache/huggingface`，**在仓库外**，不影响 git。
- 实测性能（M4 Mac，模型已缓存后）：
  - 11 页中文扫描型 PDF：约 30 秒（首次含下模型约 5 分钟）
  - 7 秒中文音频转写：约 4.4 秒，结果准确（首次含下模型约 11 分钟）
