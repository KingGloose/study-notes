---
name: kg-wechat
description: 抓取微信公众号单篇文章（mp.weixin.qq.com/s/...），转成干净 Markdown、图片下载到本地（解决防盗链），交由 AI 解析后按 LLM Wiki 契约沉淀进学习笔记库。当主人给出公众号文章链接、想「把这篇公众号文章存进知识库」「解析这篇文章」「转成 markdown」时使用。只处理单篇公开文章，不做批量/历史抓取（那需要登录凭证和无头浏览器，本 skill 不涉及）。
---

# kg-wechat · 公众号文章消化 skill

把主人读到的公众号文章，抓成带本地图片的干净 Markdown，让 AI 解析，最终按 `AGENTS.md` 的 Ingest 流程沉淀进 `wiki/`。

## 何时用

- 「把这篇公众号文章存进知识库 <链接>」
- 「解析这篇文章 <链接>」
- 「这篇公众号转成 markdown」

## 关键前提与边界

- **只处理单篇公开文章**：`https://mp.weixin.qq.com/s/xxx` 这种分享链接是公开的，**无需登录、无需 cookie**，直接抓即可。
- **不做批量/历史抓取**：抓某公众号全部历史文章需要登录凭证 + 无头浏览器 + 代理池，容易触发风控，本 skill 不涉及。
- **图片防盗链**：公众号图片由 `mmbiz.qpic.cn` 提供，检查 Referer，直接引用原链接会裂图。脚本默认带 Referer 下载到本地，从根上解决。

## 前置：环境准备

**环境已统一到 `skills/.venv`，安装步骤见 [`../README.md`](../README.md)。**
本 skill 需要：`base` + `wechat`。

```bash
cd 学习笔记/skills && source .venv/bin/activate && cd kg-wechat
```

## 脚本用法

```bash
source .venv/bin/activate    # Windows 用对应激活方式

# 抓文章 → md 存到指定路径，图片存到指定 assets 目录
python scripts/wechat_to_md.py "<公众号URL>" --out <输出.md> --assets <图片目录>

# 只看正文（打到 stdout，不下图，用于快速预览/AI 直接读）
python scripts/wechat_to_md.py "<公众号URL>" --no-images
```

参数：
- `--out`：输出 md 路径；不给则打到 stdout。
- `--assets`：图片下载目录；不给时默认 `<out同级>/assets`。
- `--asset-prefix`：md 里图片引用前缀，默认 `assets`。
- `--no-images`：不下载图片（保留原链接，会防盗链裂图，仅用于纯文字预览）。

脚本会在 md 开头写好 frontmatter：标题、作者、公众号名、发布日期、原文链接、抓取日期，方便溯源。

## 工作流（遵守 AGENTS.md）

1. 主人给公众号链接。
2. 先抓正文预览判断价值：`wechat_to_md.py <url> --no-images`，读正文和主人讨论。
3. 决定沉淀 → 正式抓取带图版本，**图片存进库的 `assets/`**：

   ```bash
   python scripts/wechat_to_md.py "<url>" \
     --out ../../raw/wx-<日期>-<短标题>.md \
     --assets ../../assets \
     --asset-prefix "../assets"
   ```

   > raw 里的 md 引用 `../assets/xxx`；若沉淀成 wiki 页，注意按 wiki 页所在层级调整图片相对路径，或统一用 Obsidian `![[assets/文件名]]` 语法（见 AGENTS.md 写作约定）。
4. 按 `AGENTS.md` 判断沉淀方式：
   - 纯通用知识 → 只在 `index.md` 补唤醒关键词。
   - 有个人判断/项目上下文/独特理解 → 写 `wiki/` 对应领域页，主动建双链 `[[...]]`。
   - **图片按 A/B/C 三档处理**：知识型图（架构图/流程图，有信息量）保留 + 补文字说明；装饰型图忽略。优先文字，别让知识困在图里。
5. 追加 `log.md` 一条。

## 边界与坑

- **风控**：单篇公开文章基本不触发；若脚本报「环境异常/频繁」，稍等或换网络。别用它做批量抓取。
- **非图文消息**：视频号动态、纯图片消息可能没有 `js_content` 正文容器，脚本会明确报错。
- **图片格式**：按 URL 里的 `wx_fmt` 存（png/jpeg/gif/webp）。gif 动图也会下载，注意体积。
- **付费/仅关注可见文章**：本 skill 不处理需要登录态的受限内容。
