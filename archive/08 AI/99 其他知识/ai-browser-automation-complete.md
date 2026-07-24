# AI + 浏览器自动化技术调研与实践（完整版）

## 一、产品调研汇总

### 1.1 AI 直接操作浏览器类

**browser-use** — 开源 AI 浏览器代理框架，让 LLM 驱动浏览器完成任务。社区热度高，上手快，但工程化和稳定性一般。

**Stagehand** — Browserbase 推出的 AI 浏览器自动化 SDK，结合 Playwright，用自然语言操作页面。偏工程化，本质建立在 Playwright 生态之上。

**Chrome DevTools MCP（推荐）** — Chrome DevTools 团队官方 MCP 服务器，基于 Puppeteer 和 CDP 构建。能力覆盖：浏览器自动化、调试分析、性能审计、设备模拟。优势在于闭环调试：启动浏览器 → 发现问题 → 分析根因 → 验证修复。

**Krometrail** — 基于 CDP 的浏览器录制与运行时分析工具，能检测 React/Vue/Svelte 框架问题（无限重渲染、闭包陷阱等），可导出 Playwright 测试骨架。

**Playwright** — Microsoft 的跨浏览器自动化测试框架，工程化最好，适合 E2E 测试落地。在 AI 体系里是最适合承接 AI 生成结果的执行层。

**Puppeteer** — Chrome/Chromium 自动化框架，生态成熟，适合抓取和轻量自动化，跨浏览器能力弱于 Playwright。

**Lightpanda** — 轻量级无头浏览器，资源消耗低，适合 AI Agent 信息获取场景，但不支持完整 CSS 渲染。

### 1.2 能力分层

1. **Agent 操作层**：Operator、Computer Use、browser-use、Stagehand、Chrome DevTools MCP
2. **浏览器基础设施层**：Browserbase、Steel、Browserless
3. **录制与诊断层**：Krometrail、Replay.io、LogRocket、FullStory、Sentry Replay
4. **测试执行层**：Playwright、Puppeteer、Cypress、Selenium

## 二、CDP 核心技术解析

### 2.1 CDP 是什么

CDP 全称是 **Chrome DevTools Protocol**。它本质上是 Chrome 暴露出来的一套"远程控制协议"，让外部程序可以像 DevTools 一样去操作和观察浏览器。

可以把它理解成：

- Chrome 是被控端
- 外部程序通过 **WebSocket** 连上 Chrome
- 然后发送一条条 JSON 指令
- Chrome 执行后返回结果，或者持续推送事件

核心能力包括：

- 打开某个页面
- 获取 DOM 树
- 执行一段 JavaScript
- 监听网络请求
- 获取控制台日志
- 采集性能 trace
- 截图、导出 PDF
- 模拟手机、弱网、地理位置

**CDP 不是一个库，也不是一个工具，而是一套协议**。Puppeteer、Playwright、Chrome DevTools MCP，底层很多能力都建立在它之上。

### 2.2 CDP 怎么工作

典型流程：

1. 启动 Chrome，并打开远程调试端口
2. 外部程序通过 WebSocket 连上这个端口
3. 调用不同的 domain/method

```bash
# 启动 Chrome 并开启 CDP
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-cdp-profile
```

常见 domain：

- **Page**：页面导航、生命周期
- **Runtime**：执行 JavaScript
- **DOM**：DOM 查询和修改
- **Network**：请求/响应监听、拦截
- **Emulation**：设备模拟
- **Log / Console**：日志
- **Tracing / Performance**：性能采样

### 2.3 CDP 怎么用

#### 方式 1：直接连协议

最小示例：

```js
const WebSocket = require("ws");

const ws = new WebSocket("ws://127.0.0.1:9222/devtools/page/<target-id>");

ws.on("open", () => {
  ws.send(JSON.stringify({
    id: 1,
    method: "Page.enable"
  }));

  ws.send(JSON.stringify({
    id: 2,
    method: "Page.navigate",
    params: { url: "https://example.com" }
  }));
});

ws.on("message", data => {
  const msg = JSON.parse(data.toString());
  console.log(msg);
});
```

这是最原始的 CDP 用法：**自己发协议包**。

#### 方式 2：通过封装库使用

大多数场景不会手写 CDP 包，而是通过 Puppeteer、Playwright、chrome-remote-interface、Chrome DevTools MCP 等工具。这些工具把 CDP 包装成更易用的 API。

### 2.4 CDP 解决了什么问题

#### 2.4.1 解决"浏览器可编程控制"问题

以前浏览器主要是人手动点。CDP 让浏览器能被程序精确控制。

应用场景：自动化测试、自动化登录、批量截图、页面抓取、表单自动填写。

#### 2.4.2 解决"浏览器内部可观测性"问题

普通 HTTP 抓取工具只能拿 HTML，拿不到浏览器运行时信息。CDP 可以拿到：

- 哪些请求发出去了
- 返回了什么状态码
- 页面执行了什么 JS
- 控制台报了什么错
- 哪个资源拖慢了页面
- LCP/CLS/INP 等性能指标

这对排查前端问题非常关键。

#### 2.4.3 解决"真实浏览器环境复现"问题

前端很多问题不是"接口错了"，而是：渲染时序问题、登录态问题、异步请求竞态、DOM 状态和数据状态不一致、某个按钮点不到、某个字段在某些交互路径下才出现。

CDP 可以在**真实浏览器上下文**里复现和定位这些问题。

### 2.5 CDP 典型案例：排查"登录后接口为什么 401"

问题现象：用户点击登录按钮，页面跳转失败，某个接口返回 401。仅看代码不容易判断是 Cookie 丢了、Header 不对，还是重定向有问题。

用 CDP 怎么做：

1. 启动 Chrome 并连接 CDP
2. 开启 `Network.enable`
3. 操作页面触发登录
4. 监听 `Network.requestWillBeSent`、`Network.responseReceived`、`Network.loadingFinished`
5. 检查：请求 URL、请求头、Cookie、响应状态码、响应 body、是否发生 302 跳转

示例：

```js
ws.send(JSON.stringify({ id: 1, method: "Network.enable" }));

ws.on("message", data => {
  const msg = JSON.parse(data);

  if (msg.method === "Network.requestWillBeSent") {
    console.log("请求", msg.params.request.url);
  }

  if (msg.method === "Network.responseReceived") {
    console.log("响应", msg.params.response.url, msg.params.response.status);
  }
});
```

CDP 解决的是：**不仅能"点登录"，还能看到登录过程中浏览器内部到底发生了什么**。从"黑盒操作"变成"白盒调试"。

### 2.6 CDP 的局限

#### 2.6.1 太底层

直接使用时，你要自己管理：WebSocket 连接、target/page、命令 ID、事件订阅、页面生命周期、异步时序。所以直接写 CDP 开发成本不低。

#### 2.6.2 和 Chromium 绑定很深

CDP 的核心生态围绕 Chrome/Chromium，虽然别的工具会做兼容层，但它天然不是"跨浏览器抽象"的最佳入口。

#### 2.6.3 登录态管理复杂

如果你用独立 profile 做远程调试，就会遇到：

- 默认浏览器不能直接 attach
- 登录态不共享
- 需要 profile 持久化或 Cookie 注入

### 2.7 登录态问题的解决方案

| 方案 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| 复制 Chrome Profile | 保留登录态 | 一次性快照，不同步 | 短期测试 |
| Playwright storageState | 可复用，CI 友好 | 需首次手动登录 | 自动化测试 |
| 独立 Profile + 手动登录 | 持久化登录态 | 首次需手动操作 | 开发调试 |
| Cookie 注入 | 灵活 | 需要获取 Cookie | 脚本化测试 |

## 三、Puppeteer 调研

### 3.1 Puppeteer 是什么

Puppeteer 是 Google 官方维护的一个 **Node.js 浏览器自动化库**。它给 Chrome/Chromium 提供了一层高层 API，让你不用直接手写 CDP 包。

可以把它理解成：

- CDP 是"浏览器协议"
- Puppeteer 是"协议的高级封装"

例如：直接写 CDP 要自己发 `Page.navigate`，用 Puppeteer 只要写 `page.goto(url)`。

关系图：

```
你的代码
   ↓
Puppeteer API
   ↓
CDP (Chrome DevTools Protocol)
   ↓
Chrome/Chromium
```

### 3.2 Puppeteer 解决了什么问题

#### 3.2.1 把底层协议封装成易用 API

CDP 虽然强，但太底层。Puppeteer 帮你封装成 `browser`、`page`、`elementHandle`、`locator`、`response`、`request` 这些更贴近开发者直觉的对象模型。

#### 3.2.2 解决自动化脚本编写难的问题

打开页面、等待元素出现、输入用户名密码、点击按钮、截图、抓取数据 — Puppeteer 都有现成 API，不用自己管协议细节。

#### 3.2.3 解决真实浏览器场景的测试和抓取问题

很多任务需要"真实浏览器"：页面依赖 JS 渲染、需要登录、需要执行点击/滚动/上传文件、需要监听请求、需要截图验证。这类问题单靠 `axios` 或 `fetch` 做不了，Puppeteer 就是专门解决这类问题的。

### 3.3 Puppeteer 怎么用

#### 安装

```bash
npm install puppeteer        # 自带 Chromium
npm install puppeteer-core   # 不下载 Chromium，手动指定浏览器路径
```

#### 最小示例

```ts
import puppeteer from "puppeteer";

const browser = await puppeteer.launch();
const page = await browser.newPage();

await page.goto("https://example.com");
await page.screenshot({ path: "example.png" });

await browser.close();
```

#### 常见操作

```ts
// 导航页面
await page.goto("https://example.com", { waitUntil: "networkidle2" });

// 输入文本
await page.type("#username", "alice");
await page.type("#password", "123456");

// 点击按钮
await page.click("#login-btn");

// 等待元素出现
await page.waitForSelector(".result");

// 执行页面内 JavaScript
const title = await page.evaluate(() => document.title);

// 截图元素
const el = await page.waitForSelector(".card");
await el.screenshot({ path: "card.png" });
```

#### 监听和拦截网络请求

```ts
// 监听
page.on("request", req => {
  console.log("请求:", req.method(), req.url());
});
page.on("response", res => {
  console.log("响应:", res.status(), res.url());
});

// 拦截
await page.setRequestInterception(true);
page.on("request", request => {
  const type = request.resourceType();
  if (type === "image" || type === "stylesheet") {
    request.abort();
  } else {
    request.continue();
  }
});
```

### 3.4 Puppeteer 典型案例：自动化登录并抓取用户首页信息

需求：打开后台系统登录页 → 输入账号密码 → 登录成功后进入首页 → 抓取欢迎文案 → 保存截图。

```ts
import puppeteer from "puppeteer";

const browser = await puppeteer.launch({ headless: false });
const page = await browser.newPage();

await page.goto("https://example.com/login");

await page.type("#username", "alice");
await page.type("#password", "123456");
await page.click("#submit");

await page.waitForSelector(".welcome-text");

const welcomeText = await page.$eval(".welcome-text", el => el.textContent);
console.log("欢迎文案:", welcomeText);

await page.screenshot({ path: "home.png", fullPage: true });

await browser.close();
```

Puppeteer 在这里解决的是：需要真实浏览器执行登录流程、页面依赖 JS 渲染、登录后要等异步内容出现、还要截图留证据。如果不用 Puppeteer，你需要手动点页面，或直接写很底层的 CDP。

### 3.5 Puppeteer vs Playwright

| 维度 | Puppeteer | Playwright |
|------|-----------|------------|
| 维护方 | Google | Microsoft |
| 浏览器支持 | 仅 Chromium | Chromium + Firefox + WebKit |
| 自动等待 | 需手动处理 | 内置自动等待 |
| 网络拦截 | 支持 | 支持，API 更友好 |
| 移动端模拟 | 支持 | 支持 |
| 录制工具 | 无内置 | codegen 录制 |
| 生态成熟度 | 更早，社区大 | 后发，功能更全 |

Puppeteer 适合：浏览器自动化、页面抓取、截图/PDF 生成、后台系统自动操作、登录态脚本、前端调试辅助。

不那么适合：强跨浏览器 E2E 测试、团队级大型测试工程体系（这类场景 Playwright 更合适）。

### 3.6 Puppeteer 在 Chrome DevTools MCP 中的角色

Chrome DevTools MCP 的架构：

```
AI Agent (Claude/LLM)
    ↓ MCP Protocol (JSON-RPC over stdio)
Chrome DevTools MCP Server
    ↓ Puppeteer API
    ↓ Chrome DevTools Protocol (CDP)
Chrome/Chromium Browser
```

MCP Server 内部使用 Puppeteer 作为浏览器控制层，将 MCP 工具调用翻译为 Puppeteer API 调用，再由 Puppeteer 通过 CDP 控制浏览器。

### 3.7 CDP 和 Puppeteer 的分工

一句话概括：

- **CDP** 解决的是"浏览器为什么能被程序控制"的问题
- **Puppeteer** 解决的是"开发者如何方便地去控制浏览器"的问题

再直白一点：CDP 是发动机接口，Puppeteer 是方向盘、油门和仪表盘。

## 四、Chrome DevTools MCP 深度实践

### 4.1 MCP 启动机制

#### 标准 MCP 启动方式

Claude Code 启动时读取 `~/.claude.json` 中的 `mcpServers` 配置，对每个 server 直接 `spawn(command, args)` 启动子进程，通过 stdin/stdout（stdio）与 MCP server 通信（JSON-RPC 协议）。

以 context7 为例，参数在 JSON 中写死，Claude Code 原样执行：

```json
"context7": {
  "command": "npx",
  "args": ["-y", "@upstash/context7-mcp"],
  "type": "stdio"
}
```

#### 自定义脚本启动（chrome-devtools 的做法）

chrome-devtools 的 MCP 配置：

```json
"chrome-devtools": {
  "command": "bash",
  "args": ["/Users/zzzz/.claude/scripts/chrome-mcp-launcher.sh"]
}
```

启动脚本 `chrome-mcp-launcher.sh` 的逻辑：

```bash
#!/bin/bash
DEVTOOLS_FILE="$HOME/Library/Application Support/Google/Chrome/DevToolsActivePort"

# 1. 读取 Chrome 的调试端口（每次启动都不同）
PORT=$(head -1 "$DEVTOOLS_FILE")
WS_PATH=$(tail -1 "$DEVTOOLS_FILE")
WS_ENDPOINT="ws://127.0.0.1:${PORT}${WS_PATH}"

# 2. exec 替换当前进程，启动 MCP server
exec npx -y chrome-devtools-mcp@latest --wsEndpoint "$WS_ENDPOINT"
```

完整链路：

```
Claude Code spawn
       ↓
  bash launcher.sh          ← 额外的一层 shim
       ↓
  读取 DevToolsActivePort   ← 动态获取端口
       ↓
  exec npx chrome-devtools-mcp --wsEndpoint ws://127.0.0.1:{PORT}{PATH}
       ↓
  MCP server 正常运行（stdio）
```

`exec` 替换当前 shell 进程后，Claude Code 的 stdio 管道直接连到 `chrome-devtools-mcp` 进程，和标准方式无异。

#### 为什么需要脚本？

标准 JSON 配置是静态的，无法表达「先读文件拿端口再拼参数」的动态逻辑：

| 配置 | 能否直接写 JSON | 原因 |
|------|----------------|------|
| context7 | 能 | 参数固定 |
| sentry | 能 | 只多了 env 变量 |
| chrome-devtools | 不能 | `--wsEndpoint` 端口号每次 Chrome 启动都不同 |

### 4.2 MCP 模式 vs CLI 模式

#### 通信协议差异

| 维度 | MCP 模式 | CLI 模式 |
|------|---------|---------|
| 配置方式 | settings.json 中显式配置 | 无需配置 |
| 通信协议 | stdio（标准输入输出） | Unix socket |
| Claude Code 可见性 | 工具定义加载到上下文 | Claude Code 不知道 daemon 存在 |
| 调用方式 | 直接调用 MCP 工具 | 通过 Bash 工具执行 CLI 命令 |
| 上下文开销 | ~15KB | 0 |

关键点：Claude Code 的 MCP 系统只识别通过 stdio 通信的 server。daemon 通过 Unix socket 监听，对 Claude Code 是"隐形"的。

#### 架构对比

MCP 模式：

```
Claude Code ──stdio (MCP)──> chrome-devtools MCP Server ──CDP──> Chrome
```

CLI 模式：

```
Claude Code ──Bash──> CLI ──Unix socket──> daemon (MCP Server) ──CDP──> Chrome
```

#### daemon 架构的意义

没有 daemon，每次 CLI 命令都要启动浏览器、执行操作、关闭浏览器。有了 daemon：浏览器持续运行，Cookie/登录态/页面状态保留，多个命令无缝衔接。

### 4.3 核心工具列表

**页面管理**：`new_page`（新标签页）、`navigate_page`（导航/前进/后退/刷新）、`list_pages`（列出标签页）、`select_page`（切换）、`close_page`（关闭）、`resize_page`（调整大小）

**页面交互**：`take_snapshot`（a11y tree 快照，优先于截图）、`click`、`fill`、`fill_form`、`hover`、`press_key`、`type_text`、`drag`、`upload_file`、`handle_dialog`、`wait_for`

**调试监控**：`take_screenshot`、`list_network_requests`、`get_network_request`、`list_console_messages`、`get_console_message`、`evaluate_script`

**性能审计**：`lighthouse_audit`、`performance_start_trace`/`stop_trace`、`performance_analyze_insight`、`take_memory_snapshot`、`emulate`

### 4.4 登录态处理方案

分层策略：

1. **持久化 profile**：始终使用 `--userDataDir`，Cookie 保存到磁盘，daemon 重启后自动恢复
2. **自动注入 Cookie**：Cookie 过期时，通过 `zzcli cookie` 提取 + `evaluate_script` 注入
3. **302 重定向引导**：`zzcli` 失败时，从网络请求中获取 SSO 登录页 URL
4. **提醒手动登录**：以上都失败时的兜底

Cookie 注入限制：`document.cookie` 无法设置 HttpOnly Cookie。经验证转转 SSO Cookie 均为 `is_httponly=0`，可正常注入。

### 4.5 auto-login.py 脚本解析

脚本位于 chrome-devtools skill 的 `scripts/auto-login.py`，根据 URL host 判断走公司链路还是普通链路。

**普通网站**（2 步）：直接 `chrome-devtools start --headless false` → `navigate_page`

**公司网站**（6 步）：
1. `zzcli cookie <domain> --format json` 提取主域 + host Cookie
2. 无头启动：`chrome-devtools start --proxyServer http://127.0.0.1:8899 --userDataDir ~/.chrome-devtools-profile`
3. `navigate` 到 origin（让 Cookie 写入有正确的 document context）
4. `evaluate_script` 拼接 `document.cookie = ...` 注入（主域 Cookie 带 `domain=`，加 `Secure; SameSite=None`）
5. 用同一 `userDataDir` 重启为有界面浏览器（复用注入的 Cookie）
6. `navigate` 到目标 URL

关键设计：持久化 profile 复用 — 无头注入完 Cookie 后，有界面进程读同一个 `userDataDir` 继承登录态。

## 五、Playwright 实践

### 5.1 国内安装问题

官方 CDN 被拦截，npmmirror 镜像可能缺少最新版本。最终方案：使用系统已安装的 Chrome：

```bash
npx playwright codegen --browser=chromium --channel=chrome "https://example.com"
```

### 5.2 Codegen 录制

```bash
npx playwright codegen "https://example.com"                          # 基础录制
npx playwright codegen --proxy-server=http://127.0.0.1:8899 "..."     # 带代理
npx playwright codegen --save-storage=auth.json "..."                  # 保存认证状态
```

## 六、工具选型建议

| 场景 | 推荐工具 | 原因 |
|------|----------|------|
| AI 辅助开发/调试 | Chrome DevTools MCP | 官方支持、完整能力、AI 原生、闭环调试 |
| 功能自动化测试 | Playwright | 成熟稳定，CI 友好 |
| 运行时框架问题诊断 | Krometrail | 框架问题检测（React/Vue/Svelte） |
| AI Agent 浏览网页 | Lightpanda | 轻量，低资源消耗 |
| 视觉回归测试 | Percy / Chromatic | 专业视觉对比 |
