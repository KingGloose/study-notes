# Claude Code MCP 调用机制深度解析：Shell 调用 vs 直接 MCP 调用

## 一、核心结论

在 Claude Code 中，"通过 shell/CLI 调用工具"与"直接调用 MCP 工具"的本质区别，不在于"能不能干活"，而在于：

- Claude Code 是否把它当成一个"原生工具"
- 模型是否提前知道这个工具的能力边界
- 返回结果是不是结构化数据
- 调用过程是不是进入 tool_use 通道
- 这套能力是不是会常驻在上下文里

一句话概括：

> **MCP 是"模型知道自己在调用什么工具"**
> **shell 是"模型只是执行一条命令并读回文本输出"**

## 二、Claude Code 里直接调用 MCP 是怎么回事

### 2.1 Claude Code 会先启动 MCP server

比如配置里有：

```json
"mcpServers": {
  "context7": {
    "command": "npx",
    "args": ["-y", "@upstash/context7-mcp"],
    "type": "stdio"
  }
}
```

Claude Code 会：

1. 启动这个进程
2. 用 `stdin/stdout` 和它通信
3. 读取这个 MCP server 提供的 tools/schema
4. 把这些工具注册成 Claude 可调用的工具

于是模型就能直接看到类似：

- `mcp__chrome-devtools__navigate_page`
- `mcp__chrome-devtools__take_snapshot`
- `mcp__context7__query-docs`

这些不是"命令"，而是**结构化工具**。

### 2.2 模型提前知道工具长什么样

每个 MCP tool 会带上：

- tool name
- 参数结构
- 每个参数的类型
- 是否必填
- 返回什么风格的数据

所以模型不是"瞎试"，而是知道：

- `navigate_page` 要传 `url`
- `take_snapshot` 不需要 url，只对当前 page 生效
- `list_network_requests` 返回的是请求列表

这和 shell 最大的不同是：MCP 工具的"接口定义"在调用前就暴露给模型了。模型是在"按 API 调工具"。

### 2.3 调用结果也是结构化的

比如 `mcp__chrome-devtools__list_pages` 返回的是明确的 page 列表。模型拿到后，能直接继续下一步推理：有几个 page、当前选中了哪个、下一步要 select 哪个 page。这是"机器可理解"的数据流。

## 三、shell 调用是什么回事

如果走 shell，比如：

```bash
chrome-devtools list_pages
```

Claude Code 看到的不是"工具调用"，而是：

- 我执行了一条 Bash 命令
- Bash 返回了一段 stdout/stderr 文本

模型只能把它当普通文本来读。也就是说：

- shell 不会提前告诉模型"这个命令支持哪些参数"
- 也不会告诉模型"返回值一定是某种结构"
- 模型只能依赖命令帮助、经验、输出格式去猜

所以 shell 更像：**把一个黑盒程序跑起来，然后把打印结果拿回来读。**

## 四、两者的关键区别

### 4.1 工具是否对模型"可见"

**MCP**：对模型可见。模型从一开始就知道有哪些工具、每个工具叫什么、参数怎么传、返回值大致是什么。

**shell**：对模型不可见。模型只知道有 Bash 可用，可以执行某个命令，但这个命令的内部能力并没有注册进工具系统。

### 4.2 是否占用"工具上下文"

**MCP**：会占。因为 MCP tool 会进入 Claude Code 的工具调用体系，工具定义和 tool result 都是模型工作流的一部分。如果把某个能力配置成 MCP，那么它的 tool schema 会进入模型环境，这会带来上下文成本。

**shell**：不会以 MCP tool 的形式占上下文。shell 只表现为一次 Bash 调用和一段 stdout/stderr 输出。不会把一整套 chrome-devtools 的所有命令 schema 都挂进模型工具列表里。所以 shell 更省"工具面"的上下文成本。

### 4.3 返回结果是否结构化

**MCP**：结构化，非常适合链式调用。比如：

- `list_pages` → 得到 pageId
- `select_page(pageId=3)` → 切换标签页
- `take_snapshot()` → 获取结构化快照
- `click(uid="1_47")` → 点某个元素

模型很容易连续推理。

**shell**：通常是文本。模型要继续下一步，通常得自己解析文本。这会带来解析不稳定、CLI 输出格式改了就麻烦、更难做稳健链式自动化等问题。

### 4.4 权限模型不同

**MCP**：权限粒度更细。可以细到允许 `mcp__chrome-devtools__take_snapshot`、不允许 `mcp__chrome-devtools__upload_file`。这是"按工具授权"。

**shell**：权限通常是命令级、模式级。例如允许 `Bash(chrome-devtools *)`。这属于"按命令授权"，粒度粗很多。

### 4.5 状态管理不同

**MCP**：如果 MCP server 自己维护状态，那么 Claude 调的是"有状态工具"。例如 browser/page/session 的状态可以保留在 MCP server 一侧。

**shell**：每次 Bash 调用本身是无状态的。但如果 shell 调到的是一个 CLI + daemon 架构（比如 `chrome-devtools` CLI），那么状态其实保留在 daemon 那边，而不是 Bash 本身。所以更准确地说：Bash 调用自己无状态，但 Bash 可以连接一个有状态后台。

### 4.6 对比总结表

| 维度 | 直接 MCP 调用 | shell 调用 CLI |
|------|-------------|---------------|
| 工具对模型可见性 | 可见，schema 提前暴露 | 不可见，只是 Bash 命令 |
| 上下文开销 | 占用（~15KB tool schema） | 不占用 |
| 返回数据格式 | 结构化 JSON | 纯文本，需解析 |
| 权限粒度 | 按工具级别 | 按命令模式 |
| 状态管理 | MCP server 内部维护 | 依赖外部 daemon |
| 链式调用 | 天然支持 | 需要手动解析串联 |
| 适合场景 | 频繁多步交互 | 按需执行、前置编排 |

## 五、用 chrome-devtools 例子解释两种模式

这个例子最典型，因为它两种方式都存在。

### 5.1 方式 A：直接 MCP

Claude Code 配置里有：

```json
"chrome-devtools": {
  "command": "bash",
  "args": ["/Users/zzzz/.claude/scripts/chrome-mcp-launcher.sh"]
}
```

然后 Claude Code 启动这个 server，server 把工具暴露出来：

- `mcp__chrome-devtools__new_page`
- `mcp__chrome-devtools__navigate_page`
- `mcp__chrome-devtools__take_snapshot`

此时模型是在"原生调工具"。特点：工具清单可见、参数类型明确、返回结构化、更适合复杂多步交互。

### 5.2 方式 B：shell 调 CLI

比如脚本里调用：

```bash
chrome-devtools start --proxyServer http://127.0.0.1:8899 --userDataDir ~/.chrome-devtools-profile
chrome-devtools navigate_page --url "https://oa.zhuanspirit.com"
```

Claude Code 这里只是执行 Bash。特点：Claude 不知道 `chrome-devtools` CLI 的完整 schema、只能读命令输出、但不会把整套工具能力常驻到 MCP 工具上下文中、很适合"按需执行、少暴露 schema、少占上下文"。

### 5.3 方式 C：shell 启动 MCP server（你当前的做法）

你的 `chrome-mcp-launcher.sh` 更特殊：

- 外层是 shell 编排（读端口、拼参数）
- 内层是 MCP 接入（`exec` 成真正的 MCP server）

所以它介于两者之间：**用 shell 做启动前准备，最终交给 MCP server 接管通信**。

### 5.4 什么时候适合 MCP，什么时候适合 shell

**适合直接 MCP**：频繁多步调用、强结构化返回、AI 连续推理和自动编排、更细粒度权限控制、工具本身就是给模型长期用的。比如：浏览器调试、structured search、文档查询、Sentry issue 查询。

**适合 shell**：按需执行不想常驻 schema、前后要包很多脚本逻辑、工具本身更像"命令行程序"而不是"模型原生工具"、输出文本就够了、希望少占工具上下文。比如：启动本地服务、做一段预处理、跑构建、执行 CLI daemon、包一层登录注入逻辑。

## 六、stdin/stdout 通信机制详解

### 6.1 什么叫 stdin/stdout

任何命令行程序启动时，系统默认会给它三条标准通道：

- `stdin`：标准输入
- `stdout`：标准输出
- `stderr`：标准错误

你平时在终端里执行 `node app.js`：

- 你的键盘输入 → `stdin`
- 程序 `console.log()` 输出 → `stdout`
- 报错输出 → `stderr`

只是平时这三条通道接在终端窗口上，所以你不觉得它们是"通信通道"。

### 6.2 Claude Code 里怎么用它

当 Claude Code 看到 MCP 配置后，它会 spawn 一个子进程：

```js
spawn("npx", ["-y", "@upstash/context7-mcp"])
```

这时候 Claude Code 不是"看它在终端打印什么"，而是：

- 自己拿着这个子进程的 `stdin`
- 自己监听这个子进程的 `stdout`

于是就能直接通过管道交换消息。

### 6.3 通信消息长什么样

MCP 本质上是 **JSON-RPC 消息** 在来回传。

Claude Code 往 MCP server 的 `stdin` 写一段 JSON：

```json
{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}
```

MCP server 从自己的 `stdin` 里读到这条消息，解析后执行逻辑，然后往自己的 `stdout` 写回：

```json
{"jsonrpc":"2.0","id":1,"result":{"tools":[...]}}
```

Claude Code 一直监听 `stdout`，读到这条 JSON，就知道这是对 `id=1` 的响应，工具列表拿到了。

本质上就是：**通过本地进程管道，来回写 JSON 消息。**

### 6.4 为什么不需要端口

因为这里不是"网络通信"，而是**父进程和子进程之间的本地进程间通信**。Claude Code 启动 MCP server 时，操作系统已经帮它们连好了管道。所以不需要开 TCP 端口、起 HTTP 服务、做本地 socket 暴露、防止端口冲突。

### 6.5 和 HTTP / WebSocket 的区别

| 通信方式 | 特点 | 适合场景 |
|---------|------|---------|
| stdio | 本地进程间通信，简单、低开销、无端口 | Claude Code 启动 MCP server |
| HTTP | 请求-响应模型，要起服务、监听端口 | 跨进程、跨机器、标准服务接口 |
| WebSocket | 长连接双向实时通信 | 浏览器调试、实时事件流 |

stdio 更像"贴身管道"，WebSocket/HTTP 更像"网络协议"。

### 6.6 两层通信：不要混淆

在 chrome-devtools 场景里，通信分两层：

```text
Claude Code <-> chrome-devtools-mcp    协议：JSON-RPC over stdio
chrome-devtools-mcp <-> Chrome         协议：CDP over WebSocket
```

Claude Code **不直接连 Chrome**。它只管通过 stdin/stdout 给 MCP server 发请求；真正跟 Chrome 浏览器走 WebSocket/CDP 的，是 MCP server。

<!-- PLACEHOLDER_C -->
