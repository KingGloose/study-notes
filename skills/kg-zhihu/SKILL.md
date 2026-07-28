---
name: kg-zhihu
description: 知乎内容摄入：读取专栏文章、回答、问题页多回答，转成 Markdown 存入 raw/，再按 LLM Wiki 契约沉淀。当主人给出知乎链接（zhuanlan.zhihu.com/p/... 或 zhihu.com/question/...）、说「解析这篇知乎」「这个回答存一下」「这个问题下的回答帮我看看」时使用。知乎有 JS 挑战（zse-ck），纯 HTTP 抓取会 403，故浏览器操作委派底层 kg-browser（走主人已登录的真实 Chrome）。不负责公众号（走 kg-wechat）、B站（kg-bilibili）、播客（kg-xiaoyuzhou）、本地文档（kg-doc）。
---

# kg-zhihu · 知乎内容消化

把知乎上的好文章/回答转成可读 Markdown，AI 解析后按 `AGENTS.md` 沉淀进 `wiki/`。

## 何时用

- 「解析这篇知乎 <链接>」
- 「这个回答值得存吗」
- 「这个问题下的高赞回答帮我梳理一下」
- 「之前在知乎看过一篇讲 X 的，帮我找出来沉淀」→ 先用历史查找定位（见第 1.5 步）

## 前提：为什么必须走浏览器

知乎上了 **`zse-ck` JS 挑战**——纯 HTTP 请求返回 403 + 一段必须由浏览器执行的 JS。
实测：curl_cffi 各种指纹（chrome/safari/移动端）、完整请求头、甚至带完整登录 cookie
（含 `z_c0`），**全部 403**。所以没有"轻量脚本"路线，必须真浏览器。

**能力委派 `kg-browser`**（读 那个 skill 拿命令细节），本 skill 只管知乎业务逻辑与沉淀。

## 环境

- 底层：见 `../kg-browser/SKILL.md`（需 `chrome-devtools` CLI + Chrome 开 remote debugging）
- 转 Markdown：`markdownify`（`requirements/wechat.txt` 里已有）

## 工作流

### 第 1 步：连接浏览器（每次会话首次）

```bash
cd 学习笔记/skills/kg-browser && bash scripts/connect-chrome.sh
```

连接脚本成功前不要跑任何页面命令（否则会操作到没有登录态的隔离浏览器）。

### 第 1.5 步：主人只记得内容、没有链接时

先从本地 Chrome 历史/书签找：

```bash
cd ../kg-browser && python3 scripts/find-history.py --keywords 知乎 <主题词> --articles-only
```

AI 应主动扩展同义词提高命中（如主人说"讲知识库那篇"→ `知识库 wiki 笔记 knowledge`）。
拿到候选让主人确认是哪篇，别自己挑。详见 `../kg-browser/references/history-search.md`。

### 第 2 步：打开目标页

主人可能已经在浏览器里打开了 —— 先 `chrome-devtools list_pages` 看一眼，别急着导航覆盖。
没打开则 `chrome-devtools new_page "<知乎链接>"`。

### 第 3 步：按页面类型取正文

**选择器与坑见 `../kg-browser/references/site-selectors.md` 的知乎小节。**
关键差异（不要用一套写法套所有页面）：

| 页面类型 | 要点 |
|----------|------|
| 专栏文章 `zhuanlan.zhihu.com/p/x` | 最简单，`.Post-RichTextContainer` 直接取 |
| 单条回答 `.../question/q/answer/a` | 注意**默认折叠**，先展开 |
| 问题页 `.../question/q` | **无限滚动 + 多回答**，先和主人确认要看几条，滚动加载后逐条取 |

**处理折叠**（回答页常见）：
```bash
chrome-devtools evaluate_script "() => {document.querySelectorAll('.ContentItem-expandButton').forEach(b => b.click()); return document.querySelectorAll('.ContentItem-expandButton').length}"
```

**取正文 HTML**（保留结构，别取 innerText）：
```bash
chrome-devtools evaluate_script "() => document.querySelector('<选择器>').outerHTML" --filePath /tmp/zhihu.html
```

**知乎特有的两个处理**：
- **公式**：LaTeX 在 `<img>` 的 `alt`/`data-formula` 属性里。要保公式得先把这些属性
  转成 `$...$` 文本，否则 Markdown 里只剩图片链接。
- **图片**：优先 `data-original`（原图）而非 `src`（缩略图）。

### 第 4 步：转 Markdown + 判断价值

转换后**先和主人讨论**：这篇讲了什么、值不值得沉淀。别默认全都要存。

### 第 5 步：沉淀（走 AGENTS.md）

- 存 `raw/zhihu-<日期>-<短标题>.md`，头部记**作者/原文链接/摄入日期/页面类型**做溯源。
- 按契约判断：纯通用知识 → 只进 `index.md` 唤醒；有个人判断/项目上下文/独特理解 →
  写 `wiki/` 领域页 + 双链。
- 追加 `log.md` 一条。

## 知乎内容的特殊判断

知乎信息质量方差大，沉淀时比其他来源更需要审慎：

- **高赞 ≠ 正确**。热门回答可能是故事讲得好。技术类内容注意核对，必要时联网验证。
- **注意时效**。知乎老回答很多（技术栈可能已过时），沉淀时记下原答的时间。
- **区分"作者的经验"和"作者的转述"**。前者有价值（一手踩坑），后者不如去读原始文档。
- 按 `AGENTS.md`：**明确区分「原文说的」和「AI 补充的」**，别混在一起。

## 边界

- **不绕登录**：付费内容（盐选/live）、仅关注可见的内容取不到属正常，不要尝试绕过。
- **只读不写**：不在主人账号上点赞、评论、关注。
- **不批量爬**：一次处理主人指定的内容。批量抓取知乎违反 ToS 且有账号风险。
- **ToS 提示**：用登录态读取内容严格说违反知乎服务协议。只读自己可见内容、不批量、
  不商用，实际风险低，但主人应知晓这点。
- 跨平台限制见 `../kg-browser/references/troubleshooting.md`（WSL 需额外配置，
  配不通有手动降级方案）。
