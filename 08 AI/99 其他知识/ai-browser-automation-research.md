# AI + 浏览器自动化技术调研报告

## 一、AI + 浏览器产品调研汇总

这一部分关注的是：当前 AI + 浏览器方向上，具体有哪些产品、分别解决什么问题、适合什么场景。

### 1.1 AI 直接操作浏览器类

这类产品的核心是：让 AI 像人一样理解页面、点击按钮、填写表单、完成流程。

**1) browser-use**

- 定位：开源的 AI 浏览器代理框架
- 能力：让 LLM 驱动浏览器完成任务
- 特点：社区热度高，上手快，适合实验
- 适用场景：快速验证 AI 浏览器代理思路
- 局限：工程化、稳定性、可控性相对一般

**2) Stagehand**

- 定位：Browserbase 推出的 AI 浏览器自动化 SDK
- 能力：结合 Playwright，用自然语言和结构化方式操作页面
- 特点：偏工程化，适合接入研发流程
- 适用场景：AI 辅助自动化测试、网页任务执行
- 局限：本质上还是建立在 Playwright 生态之上

**3) Chrome DevTools MCP（推荐）**

- 定位：Chrome DevTools 团队官方推出的 MCP 服务器，专为 AI 编码助手设计
- 能力：
  - 浏览器自动化：页面导航、元素点击、表单填写、截图
  - 调试分析：网络请求监控、控制台日志、JavaScript 执行
  - 性能审计：Lighthouse 审计、Core Web Vitals 追踪、内存快照
  - 设备模拟：移动端视口、弱网环境、地理位置
- 特点：官方维护、基于 Puppeteer 和 CDP、AI 原生设计
- 适用场景：
  - AI 辅助开发调试
  - 自动化功能测试
  - 性能分析与优化
  - Lighthouse 审计
- 优势：闭环调试能力（启动浏览器 → 发现问题 → 分析根因 → 验证修复）

**4) Krometrail**

- 定位：基于 CDP 的浏览器录制与运行时分析工具
- 能力：录制用户行为、检测 React/Vue/Svelte 框架问题、导出 Playwright 测试骨架
- 适用场景：复现前端 bug、检测闭包陷阱、无限重渲染等框架问题
- 局限：依赖 Chrome CDP、无法直接 attach 用户默认浏览器、更适合开发/测试环境

**5) Playwright**

- 定位：现代浏览器自动化测试框架
- 能力：跨浏览器测试、录制、回放、断言、网络拦截
- 特点：工程化最好，适合测试落地
- 适用场景：E2E 测试、回归测试、自动化表单/流程测试
- 在 AI 体系里的角色：最适合承接 AI 生成结果的执行层

**6) Puppeteer**

- 定位：Chrome/Chromium 自动化框架
- 特点：生态成熟，但跨浏览器能力弱于 Playwright
- 适用场景：抓取、脚本化页面操作、轻量自动化

**7) Lightpanda**

- 定位：轻量级无头浏览器，偏 AI Agent 场景
- 能力：以更轻的方式提供浏览器能力
- 特点：资源消耗低，适合 Agent 运行环境
- 适用场景：AI Agent 网页访问、轻量任务执行
- 局限：生态不如 Playwright 成熟、对复杂前端页面兼容性需要验证

### 1.2 结论

如果把"AI + 浏览器"按能力层拆开，可以大致分成四层：

1. **Agent 操作层**：Operator、Computer Use、browser-use、Stagehand、Chrome DevTools MCP
2. **浏览器基础设施层**：Browserbase、Steel、Browserless
3. **录制与诊断层**：Krometrail、Replay.io、LogRocket、FullStory、Sentry Replay
4. **测试执行层**：Playwright、Puppeteer、Cypress、Selenium

结合这次实践，比较明确的判断是：

- 要做 AI 驱动的浏览器操作和调试，Chrome DevTools MCP 是当前最佳选择（官方支持、能力完整）
- 要做前端自动化测试落地，Playwright 仍然最实用
- 要做浏览器运行时框架问题排查，Krometrail 有一定价值
- 要做线上用户行为回放，应该看 LogRocket / FullStory / Sentry Replay，而不是 Krometrail

### 1.3 Chrome DevTools Protocol (CDP) 核心技术

定义：Chrome 提供的远程调试协议，允许外部工具控制浏览器。

核心能力：

- 页面导航和 DOM 操作
- 网络请求拦截和修改
- JavaScript 执行
- 性能分析和追踪
- 截图和 PDF 生成

使用方式：

```bash
# 启动 Chrome 并开启 CDP
chrome --remote-debugging-port=9222
```

关键限制（实测验证）：

| 限制 | 说明 |
|------|------|
| 必须指定 `--user-data-dir` | Chrome 安全策略要求远程调试必须使用非默认 profile |
| 无法 attach 到默认浏览器 | 用户日常使用的 Chrome 无法被外部工具控制 |
| 登录态丢失 | 使用独立 profile 后，Cookie、书签、插件全部丢失 |

### 1.4 登录态问题的解决方案

在实际业务测试中，登录态是最大的障碍。以下是各方案对比：

| 方案 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| 复制 Chrome Profile | 保留登录态 | 一次性快照，不同步 | 短期测试 |
| Playwright storageState | 可复用，CI 友好 | 需首次手动登录 | 自动化测试 |
| 独立 Profile + 手动登录 | 持久化登录态 | 首次需手动操作 | 开发调试 |
| Cookie 注入 | 灵活 | 需要获取 Cookie | 脚本化测试 |

## 二、Chrome DevTools MCP 深度实践

### 2.1 工具简介

Chrome DevTools MCP 是 Google Chrome DevTools 团队官方推出的 Model Context Protocol (MCP) 服务器。它基于 Puppeteer 和 CDP 构建，让 AI 编码助手能够直接控制和检查真实的 Chrome 浏览器。

工作原理：

```
AI Agent (Claude/LLM)
    ↓ MCP Protocol
Chrome DevTools MCP Server (桥接层)
    ↓ Chrome DevTools Protocol (CDP)
Chrome/Chromium Browser
```

### 2.2 安装与配置

项目配置（`.mcp.json`）：

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "/path/to/scripts/chrome-devtools-mcp.sh",
      "args": [
        "--no-usage-statistics",
        "--no-performance-crux"
      ]
    }
  }
}
```

启动脚本（`scripts/chrome-devtools-mcp.sh`）：

```bash
#!/usr/bin/env bash
set -euo pipefail
NODE_BIN="/Users/zzzz/.nvm/versions/node/v22.18.0/bin"
export PATH="$NODE_BIN:$PATH"
exec npx -y chrome-devtools-mcp@latest "$@"
```

### 2.3 核心工具列表

**页面管理：**

| 工具 | 功能 | 使用场景 |
|------|------|----------|
| `new_page` | 打开新标签页 | 启动浏览器会话 |
| `navigate_page` | 导航（URL/前进/后退/刷新） | 访问目标页面 |
| `list_pages` | 列出所有标签页 | 管理多个页面 |
| `select_page` | 切换标签页 | 多页面操作 |
| `close_page` | 关闭标签页 | 清理资源 |
| `resize_page` | 调整窗口大小 | 响应式测试 |

**页面交互：**

| 工具 | 功能 | 使用场景 |
|------|------|----------|
| `take_snapshot` | 获取页面 a11y tree 快照 | AI 理解页面结构（优先于截图） |
| `click` | 点击元素 | 按钮、链接 |
| `fill` | 填写输入框/选择下拉 | 表单字段 |
| `fill_form` | 批量填写多个表单字段 | 多字段表单提交 |
| `hover` | 鼠标悬停 | 触发悬停效果 |
| `press_key` | 键盘操作（含组合键） | 快捷键、Enter、Tab |
| `type_text` | 连续输入文本 | 聚焦后输入 |
| `drag` | 拖拽元素到目标 | 拖放交互 |
| `upload_file` | 上传文件 | 文件选择器 |
| `handle_dialog` | 处理 alert/confirm/prompt | 浏览器对话框 |
| `wait_for` | 等待页面出现特定文本 | 异步内容加载 |

**调试与监控：**

| 工具 | 功能 | 使用场景 |
|------|------|----------|
| `take_screenshot` | 页面/元素截图 | 视觉验证 |
| `list_network_requests` | 查看网络请求列表 | 接口调试 |
| `get_network_request` | 获取请求/响应详情 | 分析接口数据 |
| `list_console_messages` | 查看控制台日志 | 错误排查 |
| `get_console_message` | 获取日志详情 | 深入分析 |
| `evaluate_script` | 在页面执行 JavaScript | 状态检查、数据提取 |

**性能与审计：**

| 工具 | 功能 | 使用场景 |
|------|------|----------|
| `lighthouse_audit` | 运行 Lighthouse 审计 | 性能/SEO/可访问性/最佳实践 |
| `performance_start_trace` | 开始性能追踪 | Core Web Vitals (LCP/INP/CLS) |
| `performance_stop_trace` | 停止追踪并分析 | 获取性能洞察 |
| `performance_analyze_insight` | 分析特定性能洞察 | 深入定位瓶颈 |
| `take_memory_snapshot` | 堆快照 | 内存泄漏分析 |
| `emulate` | 模拟设备/网络/位置 | 移动端测试、弱网测试 |

### 2.4 使用模式

**模式 1：AI 自动启动浏览器**

AI 直接通过 `new_page` 工具打开页面，无需手动启动 Chrome。这是最简单的使用方式。

**模式 2：手动启动 Chrome + MCP 连接**

```bash
# 启动 Chrome（带登录态）
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/.chrome-profiles/logged-in" \
  "https://example.com" &

# MCP Server 自动 attach 到已有的 Chrome 实例
```

**模式 3：带代理启动（Whistle 抓包）**

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/.chrome-profiles/dev" \
  --proxy-server="http://127.0.0.1:8899" \
  "https://example.com" &
```

### 2.5 典型场景示例

**场景 1：自动化功能测试**

> 用户：帮我测试资产入库页面，选择业务方为"行政"后，检查"行政性质"字段是否显示

AI 执行流程：

1. `new_page` → 打开目标页面
2. `take_snapshot` → 获取页面结构，找到表单元素
3. `fill` → 选择业务方下拉框为"行政"
4. `take_snapshot` → 检查"行政性质"字段是否出现
5. `take_screenshot` → 截图记录结果

**场景 2：性能分析**

> 用户：分析首页加载性能，找出 LCP 瓶颈

AI 执行流程：

1. `navigate_page` → 打开首页
2. `performance_start_trace` → 开始追踪
3. `navigate_page` (reload) → 刷新页面
4. `performance_stop_trace` → 获取追踪数据
5. `performance_analyze_insight` → 分析 LCP 瓶颈
6. 输出优化建议

**场景 3：接口调试**

> 用户：查看登录接口为什么返回 401

AI 执行流程：

1. `new_page` → 打开登录页
2. `fill_form` → 填写用户名密码
3. `click` → 点击登录
4. `list_network_requests` → 过滤 fetch/xhr 请求
5. `get_network_request` → 查看 401 响应的详细内容
6. `list_console_messages` → 检查控制台报错
7. 分析根因并提供修复建议

**场景 4：Lighthouse 审计**

> 用户：对详情页做一次完整的 Lighthouse 审计

AI 执行流程：

1. `navigate_page` → 打开详情页
2. `lighthouse_audit` → 运行审计（performance 除外，用 trace 更准确）
3. 分析可访问性、SEO、最佳实践得分
4. 逐条给出优化建议和代码示例

## 三、Playwright 与 Lightpanda 调研

### 3.1 Playwright 概述

Playwright 是 Microsoft 开发的浏览器自动化框架，支持 Chromium、Firefox、WebKit。

核心能力：

- 跨浏览器测试
- 自动等待机制
- 网络拦截
- 截图和视频录制
- Codegen 录制工具

### 3.2 Playwright 安装问题（国内环境）

在国内网络环境下，Playwright 浏览器下载是主要障碍：

问题：

- 官方 CDN（cdn.playwright.dev）被网络拦截
- 国内镜像（npmmirror）可能缺少最新版本

尝试过的方案：

```bash
# 方案 1：官方源（超时）
npx playwright install chromium
# Error: connect ETIMEDOUT

# 方案 2：npmmirror 镜像（404）
PLAYWRIGHT_DOWNLOAD_HOST=https://npmmirror.com/mirrors/playwright/ npx playwright install chromium
# Error: 404 NoSuchKey

# 方案 3：cdn.npmmirror.com（404）
PLAYWRIGHT_DOWNLOAD_HOST=https://cdn.npmmirror.com/binaries/playwright npx playwright install chromium
# Error: 404 NoSuchKey
```

最终解决方案：使用系统已安装的 Chrome（`--channel=chrome`）：

```bash
# 跳过下载，使用系统 Chrome
npx playwright codegen --browser=chromium --channel=chrome "https://example.com"
```

### 3.3 Playwright Codegen

Playwright 提供了 codegen 命令用于录制用户操作并生成测试代码：

```bash
# 基础录制
npx playwright codegen "https://example.com"

# 带代理录制
npx playwright codegen --proxy-server=http://127.0.0.1:8899 "https://example.com"

# 保存认证状态（解决登录问题）
npx playwright codegen --save-storage=auth.json "https://example.com"
```

### 3.4 Lightpanda

Lightpanda 是一个轻量级的无头浏览器，专为 AI Agent 和自动化场景设计。

定位：

- 比 Puppeteer/Playwright 更轻量
- 专注于 AI Agent 的浏览器交互需求
- 不需要完整的浏览器渲染引擎

适用场景：

- AI Agent 需要浏览网页获取信息
- 不需要完整的 CSS 渲染和视觉验证
- 需要快速、低资源消耗的浏览器环境

局限性：

- 不支持完整的 CSS 渲染
- 不适合视觉回归测试
- 生态不如 Playwright 成熟

结论：对于前端功能测试场景，Playwright 仍是更好的选择；Lightpanda 更适合 AI Agent 的信息获取场景。

## 四、Krometrail 简介

### 4.1 工具简介

Krometrail 是基于 Chrome DevTools Protocol (CDP) 的浏览器录制和分析工具，核心能力：

- 录制浏览器操作（事件流、网络请求、控制台输出）
- 自动检测框架级别问题（React/Vue/Svelte）
- 导出 Playwright 测试脚本

### 4.2 安装与配置

```bash
# 安装
npm install -g krometrail
```

配置 MCP Server（集成到 Claude Code）：

```json
// ~/.claude/settings.json
{
  "mcpServers": {
    "krometrail": {
      "command": "krometrail",
      "args": ["--mcp"]
    }
  }
}
```

### 4.3 框架问题检测能力

Krometrail 的独特价值在于自动检测框架级问题：

| 问题类型 | 严重级别 | 检测方式 |
|----------|----------|----------|
| `infinite_rerender` | high | 组件短时间内渲染次数异常 |
| `stale_closure` | medium | Hook 依赖数组未变但状态已改变 |
| `observer_overflow` | medium | Observer 组件触发过多 |

## 五、实战案例：资产入库功能测试

### 5.1 需求背景

在资产入库页面，当业务方选择"行政"时，需要显示"行政性质"下拉框（选项：外部、内部）。

### 5.2 测试流程（使用 Chrome DevTools MCP）

1. AI 通过 `new_page` 打开资产入库页面
2. AI 通过 `take_snapshot` 获取表单结构
3. AI 通过 `fill` 选择业务方为"行政"
4. AI 通过 `take_snapshot` 验证"行政性质"字段是否出现
5. 发现问题：选择"行政"后，"行政性质"字段没有出现

### 5.3 根因分析

查看代码发现：

```tsx
// InBound/index.tsx 第 78 行
const isExecutive = businessId === "行政";  // ❌ Bug!
```

而 BusinessSelect 组件的 store 定义：

```ts
// store/business.ts 第 37 行
value: Number(item.businessId)  // businessId 是数字类型
```

根因：businessId 是数字（如 1, 2, 3），而代码中用字符串 "行政" 比较，条件永远为 false。

### 5.4 修复方案

```tsx
// 修复前
const isExecutive = businessId === "行政";

// 修复后
const businessName = getBusinessName(businessId);
const isExecutive = businessName === "行政";
```

### 5.5 经验总结

- Chrome DevTools MCP 让 AI 可以直接操作浏览器、验证功能、发现问题
- AI 可以同时分析页面结构和源码，快速定位问题根因
- 整个调试闭环无需人工干预：操作页面 → 发现异常 → 分析代码 → 提供修复

## 六、总结与建议

### 6.1 工具选型建议

| 场景 | 推荐工具 | 原因 |
|------|----------|------|
| AI 辅助开发/调试 | Chrome DevTools MCP | 官方支持、完整能力、AI 原生、闭环调试 |
| 功能自动化测试 | Playwright | 成熟稳定，CI 友好 |
| 运行时框架问题诊断 | Krometrail | 框架问题检测（React/Vue/Svelte） |
| 录制生成测试 | Krometrail → Playwright | 录制后导出测试骨架 |
| AI Agent 浏览网页 | Lightpanda | 轻量，低资源消耗 |
| 视觉回归测试 | Percy / Chromatic | 专业视觉对比 |
