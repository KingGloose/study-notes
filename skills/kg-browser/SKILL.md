---
name: kg-browser
description: 底层能力：通过 chrome-devtools CLI 操作「用户可见的真实 Chrome」，读取需要登录态或有反爬/JS 挑战的网页内容（知乎、内网文档、语雀、Notion、掘金等），也可用于翻页滚动加载、展开折叠内容、多标签批量读取。当上层摄入 skill（如 kg-zhihu）需要浏览器，或主人说「读一下我浏览器里打开的这个页面」「这个站要登录才能看」「纯抓取被 403 了」时使用。不做前端调试（CSS/性能/内存那些去用 fe-chrome-devtools）。
---

# kg-browser · 真实浏览器读取能力

**定位**：底层能力层（和 `kg-media-to-text` 同级），供上层摄入 skill 调用，也可直接用。
它解决一件事：**让 AI 读到"只有你登录的浏览器才能看到"的内容**。

## 为什么用真实 Chrome 而不是无头浏览器

| | 真实 Chrome（本 skill） | Playwright/无头 |
|---|---|---|
| 登录态 | **天然有**（就是你的浏览器） | 要导 cookie / 配 profile |
| JS 挑战（知乎 `zse-ck` 等） | **天然通过**（真浏览器在跑） | 要额外应对 |
| 反爬对抗 | **不存在**——就是你在正常浏览 | 需持续跟进 |
| 安装 | 只需一个 CLI | +300MB Chromium |

**边界原则**：只读你自己已经能看到的页面。不注入 cookie、不伪造凭证、不绕权限。
遇到登录页/403，让主人在可见 Chrome 里自己登录，而不是想办法绕过。

## 前置（一次性）

1. 装 CLI：`npm i -g chrome-devtools-mcp@latest`
2. Chrome 开启 remote debugging：
   - 访问 `chrome://inspect/#remote-debugging`
   - 勾选 **Allow remote debugging for this browser instance**
   - **彻底退出 Chrome（⌘Q）**，重新打开
3. 每次会话首个浏览器命令**必须**先连接：

```bash
bash scripts/connect-chrome.sh
```

> **连接脚本成功前，不要执行任何 `chrome-devtools` 页面命令**，否则 CLI 会隐式启动一个
> 干净的隔离浏览器——那里面没有主人的登录态，等于白干。
> 反复连不上时：让主人彻底退出 Chrome 重开（`DevToolsActivePort` 里的 WS UUID 会失效）。

## 核心命令（按需组合，不要被固定套路限制）

```bash
chrome-devtools list_pages                      # 看当前打开了哪些标签页
chrome-devtools select_page <idx>                # 切到某个标签页
chrome-devtools new_page "<url>"                 # 新标签打开
chrome-devtools navigate_page "<url>"            # 当前标签导航

chrome-devtools take_snapshot                    # 页面结构快照（拿 uid 用于交互）
chrome-devtools evaluate_script "() => ..."      # ★ 主力：在页面里执行任意 JS
chrome-devtools evaluate_script "() => ..." --filePath /tmp/out.json   # 大输出写文件

chrome-devtools click "<uid>"                    # 点击（如"展开阅读全文"）
chrome-devtools take_screenshot --filePath /tmp/p.png   # 截图（图表类内容兜底）
```

需要某命令的完整参数时**先跑 `chrome-devtools <command> --help`**，不要照搬可能过时的文档。

## 读正文的思路（不是固定脚本）

**核心工具是 `evaluate_script`——想提取什么、怎么提取，由 AI 按页面实际情况决定。**
下面是思路和常用片段，按需改写，别当成唯一写法。

### 1. 先看页面状态

```bash
chrome-devtools evaluate_script "() => ({url: location.href, title: document.title, len: document.body.innerText.length})"
```

正文长度异常小 → 可能没加载完、需要登录、或内容在折叠区。

### 2. 探选择器（不确定用哪个容器时）

```bash
chrome-devtools evaluate_script "() => [...document.querySelectorAll('article,main,[role=main],.content')].map(e => ({sel: e.tagName + '.' + e.className.slice(0,40), len: e.innerText.trim().length})).sort((a,b) => b.len - a.len).slice(0,6)"
```

拿到候选后挑文字量合理的那个。常见站点选择器见 `references/site-selectors.md`。

### 3. 取正文

```bash
chrome-devtools evaluate_script "() => document.querySelector('<选择器>').outerHTML" --filePath /tmp/body.html
```

取 `outerHTML` 而非 `innerText`——保留结构（标题层级/代码块/表格/公式）交给
Markdown 转换，比纯文本信息量大。转换用 `markdownify`（`kg-wechat` 的依赖）：

```bash
python3 -c "
from markdownify import markdownify as md
import re, pathlib
h = pathlib.Path('/tmp/body.html').read_text()
print(re.sub(r'\n{3,}', '\n\n', md(h, heading_style='ATX', strip=['script','style'])))
"
```

### 4. 需要交互才能看全的内容

- **懒加载/无限滚动**：`evaluate_script "() => window.scrollTo(0, document.body.scrollHeight)"` 后等一会再取
- **折叠/"阅读全文"**：`take_snapshot` 找到按钮 uid → `click` → 重新 `take_snapshot`
- **分页**：逐页 `navigate_page` + 提取，或点下一页
- 页面变化后**必须重新 `take_snapshot`**，旧 uid 会失效

### 5. 元信息

```bash
chrome-devtools evaluate_script "() => {const m = p => (document.querySelector('meta[property=\"'+p+'\"],meta[name=\"'+p+'\"]')||{}).content || ''; return {title: m('og:title') || document.title, site: m('og:site_name'), author: m('author'), published: m('article:published_time')}}"
```

## 上层 skill 怎么用它

上层（如 `kg-zhihu`）**不该重复实现浏览器控制**，而是：
1. 引导主人在 Chrome 打开目标页（或用 `navigate_page`）
2. 用本 skill 的 `evaluate_script` 取正文 HTML
3. 转 Markdown → 存 `raw/` → 走 `AGENTS.md` 的沉淀流程

站点专属的选择器和坑记在 `references/site-selectors.md`，不要硬编码进脚本。

## 专题

| 场景 | 读取 |
|------|------|
| 各站点正文选择器、已知坑 | `references/site-selectors.md` |
| 连接失败、CLI 问题排查 | `references/troubleshooting.md` |

## 边界与注意

- **不做前端调试**：CSS 布局、LCP、内存泄漏、组件树那些用 `fe-chrome-devtools`（那才是它的主场）。
- **不注入 cookie、不绕登录**：遇到登录墙让主人自己登录。
- **只读不写**：不要在主人的浏览器里提交表单、点赞、发评论——除非主人明确要求。
- **大输出写文件**：正文 HTML、snapshot 用 `--filePath`，别直接刷进上下文。
- **跨平台限制**：本 skill 依赖能访问到用户 Chrome 的 remote debugging。
  macOS 可用；**WSL2 访问 Windows 侧 Chrome 需要额外配置**（Windows 上的 Chrome 要以
  `--remote-debugging-port=9222` 启动，WSL 里连 `$(hostname).local:9222` 或 Windows 主机 IP）。
  配不通时的降级方案：主人手动复制正文，或用浏览器扩展导出 md 后走 `kg-doc`。
- 每次会话开头必须先跑 `connect-chrome.sh`，否则可能操作到隔离浏览器。
