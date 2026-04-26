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

### 2.1 什么是 Chrome DevTools Protocol

CDP 是 Chrome 提供的远程调试协议，允许外部工具通过 WebSocket 控制浏览器。核心能力：页面导航和 DOM 操作、网络请求拦截和修改、JavaScript 执行、性能分析和追踪、截图和 PDF 生成。

```bash
# 启动 Chrome 并开启 CDP
chrome --remote-debugging-port=9222
```

### 2.2 关键限制（实测验证）

| 限制 | 说明 |
|------|------|
| 必须指定 `--user-data-dir` | Chrome 安全策略要求远程调试必须使用非默认 profile |
| 无法 attach 到默认浏览器 | 用户日常使用的 Chrome 无法被外部工具控制 |
| 登录态丢失 | 使用独立 profile 后，Cookie、书签、插件全部丢失 |

### 2.3 登录态问题的解决方案

| 方案 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| 复制 Chrome Profile | 保留登录态 | 一次性快照，不同步 | 短期测试 |
| Playwright storageState | 可复用，CI 友好 | 需首次手动登录 | 自动化测试 |
| 独立 Profile + 手动登录 | 持久化登录态 | 首次需手动操作 | 开发调试 |
| Cookie 注入 | 灵活 | 需要获取 Cookie | 脚本化测试 |

## 三、Puppeteer 调研

### 3.1 定位与特点

Puppeteer 是 Google 官方维护的 Node.js 库，提供对 Chrome/Chromium 的高级 API 控制。它是 Chrome DevTools MCP 的底层依赖。

- 直接基于 CDP 协议，与 Chrome 绑定最紧密
- 默认自带 Chromium，开箱即用
- API 设计偏底层，灵活但需要更多手动管理
- 仅支持 Chromium 内核浏览器

### 3.2 Puppeteer vs Playwright

| 维度 | Puppeteer | Playwright |
|------|-----------|------------|
| 维护方 | Google | Microsoft |
| 浏览器支持 | 仅 Chromium | Chromium + Firefox + WebKit |
| 自动等待 | 需手动处理 | 内置自动等待 |
| 网络拦截 | 支持 | 支持，API 更友好 |
| 移动端模拟 | 支持 | 支持 |
| 录制工具 | 无内置 | codegen 录制 |
| 生态成熟度 | 更早，社区大 | 后发，功能更全 |

### 3.3 Puppeteer 在 Chrome DevTools MCP 中的角色

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
