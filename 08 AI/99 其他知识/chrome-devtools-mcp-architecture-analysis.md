# Chrome DevTools MCP 架构深度解析：通信机制与连接排查

## 问题背景

在使用 `chrome-devtools start --browserUrl http://127.0.0.1:53563` 启动后,执行 `chrome-devtools new_page "www.baidu.com"` 时遇到连接失败:

```
Failed to fetch browser webSocket URL from http://127.0.0.1:53563/json/version: HTTP Not Found
```

这引发了对整个架构的深入探究:
1. CLI 和 daemon 是如何通信的?
2. MCP Server 扮演什么角色?
3. 什么东西在和浏览器连接?
4. 为什么会出现连接失败?

## 核心架构图

### 完整通信链路

```text
[你敲命令]
    |
    v
[chrome-devtools CLI]
    |
    | Unix Socket
    | /tmp/chrome-devtools-mcp-{sessionId}.sock
    v
[daemon 后台进程]
    |
    | stdio (标准输入输出)
    | JSON-RPC 风格的 MCP 消息
    v
[chrome-devtools-mcp 子进程]
    |
    | HTTP GET /json/version   (仅用于发现 WebSocket 地址)
    | WebSocket                (真正控制浏览器的长连接)
    v
[Chrome 浏览器]
```

### 四个角色的职责

#### A. CLI: `chrome-devtools`

- 解析用户敲的命令和参数
- 通过 Unix Socket 把请求发给 daemon
- 把 daemon 返回的结果打印给用户
- **不操作浏览器，不保持状态，执行完就退出**

#### B. daemon（后台常驻进程）

- 在本机开一个 Unix Socket，等 CLI 来连
- 管理一个 `chrome-devtools-mcp` 子进程（通过 stdio 通信）
- 把 CLI 的请求转发给 MCP Server 子进程
- 把子进程的结果回传给 CLI
- **角色是"调度器 / 转发器"，不直接操作浏览器**

#### C. MCP Server: `chrome-devtools-mcp`（核心执行者）

- 注册所有 MCP tools（new_page、click、take_snapshot 等）
- 真正处理工具调用
- 管理浏览器连接和页面上下文
- **浏览器连接状态保存在这个进程里**

#### D. Chrome 浏览器

- 被控制对象
- 必须以 `--remote-debugging-port` 启动，暴露 Chrome DevTools Protocol (CDP) 端点

## `start` 命令的完整执行链路

### 阶段一：CLI 解析参数

```text
chrome-devtools start --browserUrl http://127.0.0.1:53563
```

`start` 函数做了以下事情：

1. 将 `--browserUrl http://127.0.0.1:53563` 与默认参数合并
2. 默认追加 `--viaCli` 和 `--experimentalStructuredContent`
3. CLI 模式下 `headless` 默认为 `true`，`isolated` 模式会创建临时 `user-data-dir`
4. 调用 `startDaemon(combinedArgs)` 启动后台进程

### 阶段二：启动 daemon 进程

`startDaemon()` 的逻辑（源码位于 `src/daemon/client.ts`）：

1. 检查是否已有 daemon 在运行（通过 PID 文件判断）
2. 如果有，先 `stopDaemon()` 再重启
3. 通过 `child_process` 以 **detached 模式** spawn 一个子进程
4. 等待 PID 文件写入成功（10 秒超时），确认 daemon 已启动
5. daemon 启动后，**CLI 进程退出，daemon 留在后台**

### 阶段三：daemon 初始化

daemon 进程启动后（源码位于 `src/daemon/daemon.ts`）：

1. 将自己的 PID 写入文件（用于后续 status/stop 命令定位进程）
2. 创建 **Unix Socket Server**（路径按 sessionId 隔离，如 `/tmp/chrome-devtools-mcp-501.sock`）
3. 通过 **stdio transport** 启动 `chrome-devtools-mcp` 子进程（MCP Server）
4. `--browserUrl http://127.0.0.1:53563` 作为参数传给 MCP Server

**关键：此时并不会立即连接浏览器。MCP Server 只是记住了 browserUrl，等待第一次工具调用时才懒加载连接。**

### 阶段四：工具调用时才连接浏览器

当执行 `chrome-devtools new_page "www.baidu.com"` 时：

```text
┌──────────────────────────────────────────────────────────────────┐
│ 第一步：CLI → daemon                                             │
│                                                                  │
│ CLI 通过 Unix Socket 发送请求：                                    │
│ {                                                                │
│   "type": "invoke_tool",                                         │
│   "tool": "new_page",                                            │
│   "args": { "url": "www.baidu.com" }                             │
│ }                                                                │
├──────────────────────────────────────────────────────────────────┤
│ 第二步：daemon → MCP Server                                      │
│                                                                  │
│ daemon 通过 stdio 将请求转发给 chrome-devtools-mcp 子进程          │
│ 走的是 MCP 消息协议 / JSON-RPC 风格消息                            │
├──────────────────────────────────────────────────────────────────┤
│ 第三步：MCP Server → 浏览器                                       │
│                                                                  │
│ MCP Server 的 getContext() 被触发，检查浏览器是否已连接：            │
│                                                                  │
│ 3a. HTTP 发现阶段（一次性）：                                      │
│     GET http://127.0.0.1:53563/json/version                      │
│     → 期望返回 { "webSocketDebuggerUrl": "ws://..." }             │
│     → 实际返回 404 → 报错！                                       │
│                                                                  │
│ 3b. WebSocket 连接阶段（如果 3a 成功）：                            │
│     通过 Puppeteer 建立 WebSocket 长连接                           │
│     后续所有操作都走这个 WebSocket/CDP 通道                         │
└──────────────────────────────────────────────────────────────────┘
```

## 通信协议选型分析

### 为什么 CLI ↔ daemon 用 Unix Socket，而不是 stdio？

这是一个常见的架构疑问。如果 daemon ↔ MCP Server 用 stdio，为什么 CLI ↔ daemon 不也用 stdio？

核心原因：**CLI 不是常驻进程，每次命令执行完就退出。**

```bash
# 当前设计：可以这样用
chrome-devtools start --browserUrl ...  # CLI 退出，daemon 留在后台
chrome-devtools new_page "baidu.com"    # 新的 CLI 进程连接到已有 daemon
chrome-devtools take_screenshot         # 又一个新 CLI 进程
```

如果用 stdio：
- CLI 退出后 stdio 就断了，daemon 也得跟着退出
- 下一个 CLI 进程没法复用之前的会话
- 多个 CLI 进程也没法同时访问同一个后台服务

### 三层通信协议各自的适用场景

| 通信层 | 协议 | 原因 |
|--------|------|------|
| CLI ↔ daemon | Unix Socket | 多个短命客户端访问一个常驻服务 |
| daemon ↔ MCP Server | stdio | 父进程托管子进程，最简单高效 |
| MCP Server ↔ Chrome | WebSocket | CDP 协议要求持续的双向通信 |

### 为什么 daemon ↔ MCP Server 用 stdio？

MCP Server 是 daemon 的子进程，stdio 是父子进程间最简单高效的通信方式：
- 不需要额外的 socket 文件
- 子进程退出时 stdio 自动关闭，资源清理简单
- MCP 协议本身就支持 stdio transport

### 为什么 MCP Server ↔ Chrome 用 WebSocket 而不是 HTTP？

Chrome DevTools Protocol (CDP) 是一个双向协议：
- 客户端需要发送命令给浏览器
- 浏览器也需要主动推送事件给客户端（如页面加载完成、网络请求等）

HTTP 是请求-响应模式，无法实现浏览器主动推送。WebSocket 支持全双工通信，天然适合 CDP。

HTTP 只在连接建立前用了一次（`GET /json/version`），目的是发现 WebSocket 地址。

## 连接失败排查思路

### 排查流程

```text
chrome-devtools new_page 报错
    │
    ▼
检查错误信息
"Failed to fetch browser webSocket URL from http://127.0.0.1:53563/json/version"
    │
    ▼
curl http://127.0.0.1:53563/json/version
    │
    ├── 无响应 → 端口没有服务在监听
    ├── 404 → 有服务但不是 Chrome 调试端口
    └── 返回 JSON → 连接应该正常，检查其他原因
    │
    ▼
lsof -i :53563
    │
    ├── 无输出 → 端口未被占用，Chrome 没启动
    └── 有输出 → 检查是什么进程
        │
        ▼
    ps -p <PID> -ww -o args=
        │
        ├── 包含 --remote-debugging-port → Chrome 调试模式，检查端口是否匹配
        └── 不包含 → 不是调试模式的 Chrome，需要重新启动
```

### 本次排查结果

```bash
# 1. 检查端口占用
$ lsof -i :53563
COMMAND  PID  USER  FD  TYPE  DEVICE  NAME
Google   2366 zzzz  109u IPv4  ...    localhost:53563 (LISTEN)

# 2. 检查 Chrome 启动参数
$ ps -p 2366 -ww -o args=
/Applications/Google Chrome.app/Contents/MacOS/Google Chrome
# 没有 --remote-debugging-port 参数！

# 3. 验证 CDP 端点
$ curl -s http://127.0.0.1:53563/json/version
# 无输出（404）
```

**结论**：53563 端口虽然被 Chrome 占用，但它不是 remote debugging port。Chrome 内部有很多端口用于不同目的，只有通过 `--remote-debugging-port` 启动的端口才会暴露 CDP 协议的 `/json/version` 端点。

### 正确的启动方式

```bash
# 1. 启动带远程调试的 Chrome
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-debug-profile \
  --no-first-run \
  --no-default-browser-check

# 2. 验证 CDP 端点
$ curl -s http://127.0.0.1:9222/json/version
{
  "Browser": "Chrome/131.0.6778.109",
  "webSocketDebuggerUrl": "ws://127.0.0.1:9222/devtools/browser/..."
}

# 3. 启动 chrome-devtools daemon
chrome-devtools start --browserUrl http://127.0.0.1:9222

# 4. 正常使用
chrome-devtools new_page "https://www.baidu.com"
```

## 总结

chrome-devtools-mcp 采用三层架构（CLI → daemon → MCP Server），每层之间使用不同的通信协议，各有其设计考量：

- **CLI 是轻量的命令行入口**，执行完就退出
- **daemon 是常驻的转发器**，负责进程管理和多客户端调度
- **MCP Server 是核心执行者**，持有浏览器 WebSocket 长连接，真正控制浏览器
- **浏览器连接是懒加载的**，`start` 只是准备参数，第一次工具调用时才真正连接
- 连接浏览器时，先通过 HTTP 发现 WebSocket 地址，再建立 WebSocket 长连接
