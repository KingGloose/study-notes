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
