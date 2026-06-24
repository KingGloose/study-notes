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

## 七、Shell 脚本启动 MCP：exec 的关键作用

### 7.1 你的配置

```json
{
  "command": "bash",
  "args": ["/Users/zzzz/.claude/scripts/chrome-mcp-launcher.sh"]
}
```

Claude Code 做的事情等价于 `bash /Users/zzzz/.claude/scripts/chrome-mcp-launcher.sh`。此时系统会创建一组管道，Claude Code 持有子进程的 stdin 和 stdout，而这个子进程确实是 `bash`。

### 7.2 exec 做了什么

脚本核心：

```bash
exec npx -y chrome-devtools-mcp@latest --wsEndpoint "$WS_ENDPOINT"
```

`exec` 是 shell 内置命令，语义是：**用后面的程序替换当前 shell 进程本身。** 不是"启动一个子进程"，而是"把自己变成那个程序"。

替换后：PID 不变、stdin/stdout/stderr 管道不变、但进程内容完全换成了新程序、原来的 bash 代码不再存在。

### 7.3 进程生命周期

```
阶段 1：Claude Code spawn bash
  Claude Code ====stdin管道====> bash (PID 2001)
  Claude Code <===stdout管道==== bash (PID 2001)

阶段 2：bash 执行脚本（读端口、拼地址）
  bash 内部执行准备逻辑，Claude Code 还没发任何 MCP 消息

阶段 3：exec 替换进程
  exec 前：Claude Code ===stdio=== bash (PID 2001)
  exec 后：Claude Code ===stdio=== chrome-devtools-mcp (PID 2001)

  关键点：
  ✓ PID 没变，还是 2001
  ✓ stdin/stdout 管道没变
  ✓ 但进程内容完全换成了 chrome-devtools-mcp
  ✗ bash 已经不存在了

阶段 4：MCP 协议通信开始
  Claude Code 往 stdin 写 {"method":"tools/list"}
  chrome-devtools-mcp 从 stdout 回 {"result":{"tools":[...]}}

阶段 5：实际工具调用（两层通信）
  Claude Code --stdin--> chrome-devtools-mcp --WebSocket--> Chrome
  Claude Code <-stdout-- chrome-devtools-mcp <-WebSocket--- Chrome
```

### 7.4 完整进程生命周期时间线

```
时间 ──────────────────────────────────────────────────────────>

Claude Code  ████████████████████████████████████████████████████
                │
                │ spawn
                ▼
bash         ███████░░░
             │读端口│
             │拼地址│
             │ exec │
                    │
                    ▼ exec 替换（同一个 PID）
MCP server          ░████████████████████████████████████████████
                     │                    │
                     │ connect ws         │ 持续通信
                     ▼                    ▼
Chrome               ████████████████████████████████████████████

图例：
  ███ = 进程存活
  ░░░ = 进程即将被替换
  │   = 事件触发
```

## 八、为什么必须用 exec

### 8.1 如果不用 exec，进程结构变成什么

```bash
#!/bin/bash
PORT=$(head -1 "$DEVTOOLS_FILE")
# 注意：没有 exec
npx -y chrome-devtools-mcp@latest --wsEndpoint "ws://127.0.0.1:${PORT}"
```

进程结构变成：

```
Claude Code (PID 1000)
    └── bash launcher.sh (PID 2001)        ← bash 还活着
            └── npx chrome-devtools-mcp (PID 3002)   ← 新的子进程
```

Claude Code 持有的 stdio 管道，连的还是 bash (PID 2001)，不是真正的 MCP server。

### 8.2 问题 1：stdout 污染（最致命）

Claude Code 和 MCP server 之间的 stdout 是 JSON-RPC 协议通道，每一行都应该是合法的 JSON 消息。

但如果 bash 还活着，以下情况都可能往 stdout 写入非 JSON 内容：

- `npx` 启动时打印 `npm warn deprecated ...`
- bash 本身的错误提示
- shell 的 trap handler 输出

一旦 Claude Code 从 stdout 读到一行不是 JSON 的文本（如 `npm warn deprecated inflight@1.0.6`），JSON-RPC 解析器直接报错，MCP 通信就断了。

用了 `exec` 就没有这个问题，因为 bash 已经不存在了，stdout 完全由 `chrome-devtools-mcp` 控制。

### 8.3 问题 2：退出码被掩盖

假设 `chrome-devtools-mcp` 启动失败，退出码是 1。

- **有 exec**：Claude Code 直接拿到退出码 1，知道 MCP server 启动失败。
- **没有 exec**：bash 等 npx 退出后自己再退出。bash 的退出码默认是最后一条命令的退出码，通常能传递。但如果脚本后面还有别的逻辑或 trap，退出码就可能被覆盖。Claude Code 看到的是 bash 的退出行为，不是 MCP server 的，错误诊断变得模糊。

### 8.4 问题 3：信号传递不直接

当 Claude Code 要关闭 MCP server 时，它会给子进程发 `SIGTERM`。

- **有 exec**：`SIGTERM` 直接发到 `chrome-devtools-mcp`，MCP server 收到后清理资源、断开 Chrome 连接、退出。
- **没有 exec**：`SIGTERM` 发到 bash (PID 2001)。bash 默认行为是收到 SIGTERM 后退出，但不一定会转发 SIGTERM 给它的子进程 npx。npx 可能变成孤儿进程，继续在后台运行，占着 Chrome 的调试端口不放。

### 8.5 问题 4：僵尸进程风险

- **有 exec**：只有一个进程，不存在父子关系，不会有僵尸进程。
- **没有 exec**：如果 bash 因为某种原因先退出了（比如收到信号），而 npx 还在运行，npx 变成孤儿进程。或者反过来，npx 退出了但 bash 没有 wait，npx 变成僵尸进程。

### 8.6 对比总结

| 维度 | 有 exec | 没有 exec |
|------|---------|-----------|
| 进程数 | 1 个（MCP server） | 2 个（bash + MCP server） |
| Claude Code 连接对象 | 直接是 MCP server | 是 bash，间接到 MCP server |
| stdout 干净度 | 完全由 MCP server 控制 | bash/npx 都可能写入杂音 |
| 退出码 | MCP server 的真实退出码 | 可能被 bash 掩盖 |
| SIGTERM 传递 | 直达 MCP server | 先到 bash，不一定转发 |
| 孤儿/僵尸风险 | 无 | 有 |
| 资源占用 | 少一个 bash 进程 | 多一个 bash 进程常驻 |

### 8.7 结论

`exec` 的作用是让 launcher 脚本在完成准备工作后彻底消失，把 stdio 管道干净地交给真正的 MCP server。

不用 `exec` 不是"绝对不能跑"，而是多了一层 bash 壳，会在 stdout 污染、信号传递、退出码、进程生命周期上引入不确定性。对于 MCP 这种依赖"干净 stdio 通道"的协议来说，这些不确定性随时可能变成 bug。

所以在 MCP launcher 脚本里，`exec` 不是可选的优化，而是**工程上的必要写法**。

## 九、最本质的理解

### 9.1 MCP 和 shell 的本质区别

- **MCP = Claude Code 直接把外部能力纳入自己的工具系统**
- **shell = Claude Code 借助命令行间接使用外部能力**

区别不是"能不能控制浏览器"，而是：这个能力是以"Claude 原生工具"的身份存在，还是以"外部命令"的身份存在。

### 9.2 stdio 通信的本质

stdio 通信的意思不是"在终端里手工输入输出"，而是：Claude Code 启动一个 MCP 子进程后，通过操作系统提供的标准输入/标准输出管道，持续交换 JSON-RPC 消息。

### 9.3 chrome-devtools 场景的两层通信

```
Claude Code <-> MCP server    用 stdio（本地进程管道）
MCP server <-> Chrome          用 WebSocket（CDP 协议）
```

Claude Code 不直接连 Chrome。MCP server 是中间的"翻译桥"。

### 9.4 shell launcher 的定位

shell 脚本在这里不是协议服务本身，只是一个 bootstrap / launcher。它做的事只是：读端口文件、拼 wsEndpoint、然后把自己 `exec` 替换成真正的 MCP server。stdio 这一层是 Claude Code 和子进程天然就有的，shell 脚本只是帮你完成了"动态参数准备"。
