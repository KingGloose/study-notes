# 1 基本介绍


# 2 基本使用



# 4 Claude Agent
## 4.1 基本使用

下面就是实现的一个最基础的 Claude Code SDK 内容，主要是询问文件夹有哪些文件：

```javascript
import { query } from "@anthropic-ai/claude-agent-sdk";

const toolAgent = query({
  prompt: "What files are in this directory?",
  options: {
    cwd: process.cwd(),
    allowedTools: ["Bash", "Glob"],
    env: {
      // 如果不传入 process.env 会导致找不到 node_modules 的 .node 文件，报错 Is options.pathToClaudeCodeExecutable set
      ...process.env,
      ANTHROPIC_API_KEY: "sk-47a377628eef44b6814811f166237ed1",
      ANTHROPIC_BASE_URL: "https://dashscope.aliyuncs.com/apps/anthropic",
      API_TIMEOUT_MS: "600000",
      CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC: "1",
    },
    model: 'glm-5'
  },
});

for await (const message of toolAgent) {
  console.log(message);
  if ("result" in message) console.log(message.result);
}

```

下面就是针对这里的 message 中的内容

```bash
{
  "type": "system",
  "subtype": "init",
  "cwd": "/Users/zhangjiahui04/测试代码/claude-code-sdk",
  "session_id": "656e6cf4-55d0-4c13-8227-37a5bf17ed57",
  "tools": [
    "Task",
    "TaskOutput",
    "Bash",
    "Glob",
    "Grep",
    "ExitPlanMode",
    "Read",
    "Edit",
    "Write",
    "NotebookEdit",
    "WebFetch",
    "TodoWrite",
    "WebSearch",
    "TaskStop",
    "AskUserQuestion",
    "Skill",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitWorktree",
    "CronCreate",
    "CronDelete",
    "CronList"
  ],
  "mcp_servers": [],
  "model": "glm-5",
  "permissionMode": "default",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "loop",
    "claude-api",
    "compact",
    "context",
    "cost",
    "heapdump",
    "init",
    "pr-comments",
    "release-notes",
    "review",
    "security-review",
    "insights"
  ],
  "apiKeySource": "ANTHROPIC_API_KEY",
  "claude_code_version": "2.1.80",
  "output_style": "default",
  "agents": [
    "general-purpose",
    "statusline-setup",
    "Explore",
    "Plan"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "loop",
    "claude-api"
  ],
  "plugins": [],
  "uuid": "f0f6b35b-c668-42f7-8cf7-bd9d362ea109",
  "fast_mode_state": "off"
}
-------
{
  "type": "assistant",
  "message": {
    "model": "glm-5",
    "id": "msg_57c9da7e-ae8e-4bd9-b850-4b5f63692c46",
    "role": "assistant",
    "type": "message",
    "content": [
      {
        "type": "thinking",
        "signature": "",
        "thinking": "The user is asking what files are in the current directory. I should use the Bash tool with `ls` to list the files in the current working directory."
      }
    ],
    "usage": {
      "input_tokens": 16884,
      "output_tokens": 0
    },
    "context_management": null
  },
  "parent_tool_use_id": null,
  "session_id": "656e6cf4-55d0-4c13-8227-37a5bf17ed57",
  "uuid": "c7cc4dae-c789-4c39-8d43-8ee7edc745e0"
}
-------
{
  "type": "assistant",
  "message": {
    "model": "glm-5",
    "id": "msg_57c9da7e-ae8e-4bd9-b850-4b5f63692c46",
    "role": "assistant",
    "type": "message",
    "content": [
      {
        "name": "Bash",
        "input": {
          "command": "ls -la",
          "description": "List files in current directory"
        },
        "id": "toolu_tool-fa7b16dc28944fdf81c7d0194c007d64",
        "type": "tool_use"
      }
    ],
    "usage": {
      "input_tokens": 16884,
      "output_tokens": 0
    },
    "context_management": null
  },
  "parent_tool_use_id": null,
  "session_id": "656e6cf4-55d0-4c13-8227-37a5bf17ed57",
  "uuid": "2f8f7d31-8e9e-4308-885b-c2aaad08abb5"
}
-------
{
  "type": "user",
  "message": {
    "role": "user",
    "content": [
      {
        "tool_use_id": "toolu_tool-fa7b16dc28944fdf81c7d0194c007d64",
        "type": "tool_result",
        "content": "total 80\ndrwxr-xr-x   8 zzzz  admin    256  3月 21 23:49 .\ndrwxr-xr-x  16 zzzz  admin    512  3月 20 16:14 ..\n-rw-r--r--@  1 zzzz  admin   1052  3月 21 23:49 index.ts\n-rw-r--r--@  1 zzzz  admin   2679  3月 21 23:49 messages.log\ndrwxr-xr-x@ 26 zzzz  admin    832  3月 20 17:42 node_modules\n-rw-r--r--@  1 zzzz  admin    525  3月 20 17:24 package.json\n-rw-r--r--@  1 zzzz  admin  21144  3月 20 17:24 pnpm-lock.yaml\n-rw-r--r--@  1 zzzz  admin    715  3月 20 17:22 README.md",
        "is_error": false
      }
    ]
  },
  "parent_tool_use_id": null,
  "session_id": "656e6cf4-55d0-4c13-8227-37a5bf17ed57",
  "uuid": "7576d2c3-7c75-4e8f-a00e-b16d3eef2c32",
  "timestamp": "2026-03-21T15:49:47.782Z",
  "tool_use_result": {
    "stdout": "total 80\ndrwxr-xr-x   8 zzzz  admin    256  3月 21 23:49 .\ndrwxr-xr-x  16 zzzz  admin    512  3月 20 16:14 ..\n-rw-r--r--@  1 zzzz  admin   1052  3月 21 23:49 index.ts\n-rw-r--r--@  1 zzzz  admin   2679  3月 21 23:49 messages.log\ndrwxr-xr-x@ 26 zzzz  admin    832  3月 20 17:42 node_modules\n-rw-r--r--@  1 zzzz  admin    525  3月 20 17:24 package.json\n-rw-r--r--@  1 zzzz  admin  21144  3月 20 17:24 pnpm-lock.yaml\n-rw-r--r--@  1 zzzz  admin    715  3月 20 17:22 README.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
-------
{
  "type": "assistant",
  "message": {
    "model": "glm-5",
    "id": "msg_911bcc57-dc92-43da-80f3-02195d509d85",
    "role": "assistant",
    "type": "message",
    "content": [
      {
        "type": "thinking",
        "signature": "",
        "thinking": "The user wants to know what files are in the current directory. The ls output shows the contents. Let me summarize this for the user."
      }
    ],
    "usage": {
      "input_tokens": 16884,
      "output_tokens": 0
    },
    "context_management": null
  },
  "parent_tool_use_id": null,
  "session_id": "656e6cf4-55d0-4c13-8227-37a5bf17ed57",
  "uuid": "b276cd4d-0d66-4b8d-a961-5691414d7d76"
}
-------
{
  "type": "assistant",
  "message": {
    "model": "glm-5",
    "id": "msg_911bcc57-dc92-43da-80f3-02195d509d85",
    "role": "assistant",
    "type": "message",
    "content": [
      {
        "type": "text",
        "text": "The current directory contains:\n\n| Name | Type | Description |\n|------|------|-------------|\n| `index.ts` | File | TypeScript source file (1KB) |\n| `messages.log` | File | Log file (2.6KB) |\n| `node_modules/` | Directory | npm dependencies |\n| `package.json` | File | npm package config |\n| `pnpm-lock.yaml` | File | pnpm lock file |\n| `README.md` | File | Documentation file |"
      }
    ],
    "usage": {
      "input_tokens": 16884,
      "output_tokens": 0
    },
    "context_management": null
  },
  "parent_tool_use_id": null,
  "session_id": "656e6cf4-55d0-4c13-8227-37a5bf17ed57",
  "uuid": "4a858f5f-d373-47fb-8584-2930ae1afd38"
}
-------
{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "duration_ms": 8515,
  "duration_api_ms": 8071,
  "num_turns": 2,
  "result": "The current directory contains:\n\n| Name | Type | Description |\n|------|------|-------------|\n| `index.ts` | File | TypeScript source file (1KB) |\n| `messages.log` | File | Log file (2.6KB) |\n| `node_modules/` | Directory | npm dependencies |\n| `package.json` | File | npm package config |\n| `pnpm-lock.yaml` | File | pnpm lock file |\n| `README.md` | File | Documentation file |",
  "stop_reason": "end_turn",
  "session_id": "656e6cf4-55d0-4c13-8227-37a5bf17ed57",
  "total_cost_usd": 0.0198234,
  "usage": {
    "input_tokens": 2593,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 30748,
    "output_tokens": 188,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [],
    "speed": "standard"
  },
  "modelUsage": {
    "glm-5": {
      "inputTokens": 2593,
      "outputTokens": 188,
      "cacheReadInputTokens": 30748,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0198234,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "fast_mode_state": "off",
  "uuid": "a7fcbf83-c4da-47ca-8a36-fb75423997fb"
}
"The current directory contains:\n\n| Name | Type | Description |\n|------|------|-------------|\n| `index.ts` | File | TypeScript source file (1KB) |\n| `messages.log` | File | Log file (2.6KB) |\n| `node_modules/` | Directory | npm dependencies |\n| `package.json` | File | npm package config |\n| `pnpm-lock.yaml` | File | pnpm lock file |\n| `README.md` | File | Documentation file |"
-------

```


## 4.2 流式输出

在 Claude Agent SDK 里，**流式输入**指的是：你的程序不是一次性把一个字符串 prompt 扔给 Agent 就结束，而是把“后续用户消息”作为一个异步可迭代流，持续喂给同一个正在运行的 Agent 会话。官方把它定义为默认且推荐的模式，适合“持久的、交互式的会话”；它允许 Agent 作为长期运行进程接收用户输入、处理中断、显示权限请求并处理会话管理。

官方文档里的 `generateMessages()` 只是一个**示例函数名**；更准确地说，它是你自己写的 `async function*`，用于不断 `yield` 出 `SDKUserMessage`。它不是 SDK 里一个必须叫这个名字的内置 API。这个判断来自两点：一是 `query()` 的 `prompt` 类型是 `string | AsyncIterable<SDKUserMessage>`，二是文档示例自己写了一个 `async function* generateMessages()` 再把它传给 `query()`。

### 4.2.1 这种模式能带来什么

官方列出的核心能力包括：直接在消息里附加图片、顺序发送多条消息并支持中断、在会话期间完整访问工具和自定义 MCP、支持 hooks、实时看到响应流，以及自然地跨多轮保持上下文。换句话说，它更像一个“活着的 Agent 会话”，而不只是一次普通的 LLM 请求。


### 4.2.2 真实使用场景

**场景 1：聊天式 Agent / REPL / Copilot 工作台**  
最典型的用法，就是前端聊天面板、开发者工作台、Slack/IM 机器人这类持续交互产品。Agent 先收到一条任务，开始分析；几秒后用户又补一句限制条件，或者继续追问。官方把这种模式归类为“长时间运行会话”，并给了高频聊天机器人这类例子；而流式输入模式本身也支持队列消息和上下文持久性。

**场景 2：外部事件持续推送给 Agent**  
`generateMessages()` 很适合把外部事件流接进 Agent，比如新的日志片段、Webhook 回调、Jenkins 结果、扫描报告、监控告警、Slack 新消息。因为它本质上就是一个异步消息队列入口，而官方明确写了流式输入支持“顺序处理多条消息”和“长期运行进程”。

**场景 3：Human-in-the-loop 审批或补充信息**  
当 Agent 执行到一半，需要用户确认、补上下文、或在中途中断后继续，这个模式就很自然。官方说明里直接提到流式输入支持处理中断、显示权限请求和 hooks，所以这类“人机协作”的流程很适合用 `generateMessages()` 来继续往同一会话里塞新消息。

**场景 4：多模态补充资料**  
官方示例里就是先发文本，再等待一段时间后继续发一条带图片的消息，用来让 Agent 继续看架构图。这说明 `generateMessages()` 很适合“先做第一轮分析，后续再补截图、设计稿、流程图、错误界面”等场景。

**场景 5：间歇性交互但希望同一轮工作自然延续**  
如果你的产品不是一直在线聊天，而是“用户偶尔回来补一句”，那流式输入和会话恢复可以组合使用。官方在托管文档里把这类形态称为“混合会话”：用户启动工作，容器关闭后还能继续，适合个人项目经理、深度研究、客户支持代理这类跨多次交互的系统。


### 4.2.3 Agent 执行完，继续上次的会话

Claude Agent SDK 会在新查询启动时自动创建会话，并在第一条 system init 消息里返回 session_id。所以最标准的做法是：第一次运行时拿到 session_id 并存起来；下次要接着聊时，把这个 ID 通过 options.resume 传回去。SDK 会自动加载之前的对话历史和上下文，让 Claude 从上次中断的位置继续。

一个最小的 TypeScript 写法可以这样记：

```javascript
import { query } from "@anthropic-ai/claude-agent-sdk";

let sessionId: string | undefined;

// 第一次运行：拿到 session_id
for await (const message of query({
  prompt: "先帮我分析这个项目的登录流程",
})) {
  if (message.type === "system" && message.subtype === "init") {
    sessionId = message.session_id;
  }
}

// 之后继续上次会话
if (sessionId) {
  for await (const message of query({
    prompt: "继续刚才的分析，并补充风险点",
    options: {
      resume: sessionId,
    },
  })) {
    console.log(message);
  }
}
```

上面这套思路和官方“获取会话 ID”与“恢复会话”的示例是一致的。

如果你想的是“从同一个历史起点，试两个不同方案”，那就不是单纯继续，而是分叉会话：在 resume 的同时加上 forkSession: true。官方说明里说得很清楚：默认恢复会继续原始会话；开启 forkSession 后，会从恢复点创建一个新的会话 ID，适合探索不同方法、做实验而不污染原始会话历史。

另外，TypeScript Options 里还有一个 continue: boolean，官方描述是“继续最近的对话”。但如果你是在真实工程里做持久化恢复，我更建议优先用 session_id + resume，因为它更显式，也更适合你把会话 ID 存到数据库、Redis 或任务记录里。continue 适合更轻量的“接着最近一次聊”。




## 4.3 权限处理

### 4.3.1 基本介绍

https://platform.claude.com/docs/zh-CN/agent-sdk/permissions

![](assets/07%20Agent/file-20260322161539768.png)

### 4.3.2 用户审批操作

其本质就是询问用户是否允许去调用某一类工具，这个有对应的方法来控制，如果用户输入 “y” 这类的就可以去让 AI 执行：https://platform.claude.com/docs/zh-CN/agent-sdk/user-input


## 4.4 执行钩子

### 4.4.1 基本介绍

本质就是对应 AI 执行生命周期中的钩子函数：https://platform.claude.com/docs/zh-CN/agent-sdk/hooks

**Hooks = 给 Agent 执行过程加“拦截器 / 中间件”。**  
它的作用是在 Agent 运行到关键节点时插一段你自己的逻辑，用来做安全校验、日志审计、权限审批、输入输出改写、会话状态管理等。官方列的典型用途包括：阻止危险操作、记录每次工具调用、转换输入输出、要求人工审批，以及跟踪会话生命周期。

在 SDK 里，hook 由两部分组成：  一部分是**回调函数**，负责真正执行你的逻辑；另一部分是**hook 配置**，用来声明挂在哪个事件上，比如 `PreToolUse`，以及要匹配哪些工具。配置入口是在 `query()` 的 `options.hooks` 里。

工程上最常见的价值有 4 类：

**1. 安全控制**：比如禁止执行高危 Bash 命令、禁止修改 `.env`、限制访问某些目录。官方示例就是在 `PreToolUse` 里拦截 `Write` / `Edit`，阻止修改 `.env`。

**2. 日志与审计**：你可以把每次工具调用、结果、失败原因都打到日志系统里，方便排障、风控、合规审计。官方也把“记录和审计每个工具调用”列成了核心用途。

**3. 权限审批 / 人机协作**：比如 Agent 想写数据库、调内部 API、执行部署命令时，先走一层审批或自定义权限判断。官方明确提到可以要求人工审批敏感操作，也有专门的 `PermissionRequest` 事件。

**4. 生命周期管理**：比如会话开始时初始化 tracing，结束时清理临时文件，停止前保存状态，或者把状态通知发到 Slack / PagerDuty。官方把 `SessionStart`、`SessionEnd`、`Stop`、`Notification` 都列成了可用钩子。

### 4.4.2 生命周期介绍

![](assets/07%20Agent/file-20260322161539770.png)

#### 4.4.2.1 PreToolUse

这是最核心的一个。 它在**工具真正执行之前**触发，可以决定 allow / deny / ask，还能改写工具输入，典型场景是：
- 拦截危险命令
- 限制文件路径或目录
- 自动给某些工具补参数
- 对敏感操作强制走审批

文档里还提到它可以通过 `updatedInput` 修改工具输入，但要配合 `permissionDecision: 'allow'` 才会生效。

#### 4.4.2.2 PostToolUse

它在**工具执行成功之后**触发，最适合做：
- 审计日志
- 结果归档
- 对工具输出做二次加工
- 把文件改动、接口返回等同步到外部系统

因为这个事件能拿到 `tool_name`、`tool_input` 和 `tool_response`。

#### 4.4.2.3 PostToolUseFailure（TypeScript）

它在**工具执行失败后**触发，而且是 **TypeScript SDK 专有**。  适合用来：
- 统一记录错误
- 区分是否是中断导致失败
- 做失败告警
- 自动降级或补偿处理

文档里说明它可以拿到 `error` 和 `is_interrupt`。

#### 4.4.2.4 UserPromptSubmit

它在**用户提示词提交时**触发。  典型用途是：
- 给 prompt 自动注入额外上下文
- 做 prompt 预处理
- 补充业务规则、身份信息、环境信息
- 做输入规范化

官方可用钩子表里就举了“向提示中注入额外上下文”这个例子。

#### 4.4.2.5 PermissionRequest（TypeScript）

它在**即将显示权限对话框时**触发，也是 **TypeScript SDK 专有**。 ，适合：
- 自定义权限处理
- 根据工具类型自动批准或拒绝
- 把权限建议同步到你的权限系统
- 减少重复弹窗

文档里还提到它能拿到 `permission_suggestions`。

#### 4.4.2.6 Stop

它在**Agent 执行停止时**触发。  适合：
- 退出前保存会话状态
- 清理资源
- 记录停止原因附近的业务状态
- 做收尾通知

官方表格里给的示例就是“退出前保存会话状态”。

#### 4.4.2.7 SessionStart / SessionEnd（TypeScript）

这两个是**会话级生命周期钩子**，并且 **只在 TypeScript SDK 可用**。  最常见的用途是：
- 会话开始时初始化日志、追踪、指标
- 根据启动来源做不同处理，比如 `startup`、`resume`
- 会话结束时清理临时目录、连接、缓存
- 做会话级监控和统计

文档里说明 `SessionStart` 可拿到 `source`，比如 `startup`、`resume`、`clear`、`compact`。同时官方也明确说 `SessionStart`、`SessionEnd`、`Notification` 仅 TypeScript 可用。

#### 4.4.2.8 Notification（TypeScript）

它处理的是**Agent 的状态消息**。  适合：
- 把状态更新同步到 Slack / PagerDuty
- 前端展示“正在等待权限 / 已认证成功 / 需要补充信息”
- 做用户提醒

文档里给了 `message`、`notification_type`、`title` 这些字段，`notification_type` 例子包括 `permission_prompt`、`idle_prompt`、`auth_success`、`elicitation_dialog`。

#### 4.4.2.9 SubagentStart / SubagentStop

这是子代理相关的钩子，其中 `SubagentStart` 是 **TypeScript 专有**，`SubagentStop` 两边可用。  适合：
- 跟踪并行子任务
- 统计子代理耗时和数量
- 聚合多个子代理的结果
- 调试多 Agent 工作流

文档里提到可以拿到 `agent_id`、`agent_type`、`agent_transcript_path`。

#### 4.4.2.10 PreCompact

它在**对话压缩前**触发，适合：
- 在压缩前归档完整上下文
- 自定义摘要前处理
- 给 compact 增加额外指令

文档表格给的例子就是“摘要前归档完整记录”，并且这个事件有 `trigger` 和 `custom_instructions`。


## 4.5 会话管理

本质其实就是就是针对 session_id 的处理：https://platform.claude.com/docs/zh-CN/agent-sdk/sessions


## 4.6 文件检查点

文件的修改设置一个检查点：https://platform.claude.com/docs/zh-CN/agent-sdk/file-checkpointing


## 4.7 结构化输出

https://platform.claude.com/docs/zh-CN/agent-sdk/structured-outputs

```javascript
import { query } from '@anthropic-ai/claude-agent-sdk'

// 定义您想要返回的数据形状
const schema = {
  type: 'object',
  properties: {
    company_name: { type: 'string' },
    founded_year: { type: 'number' },
    headquarters: { type: 'string' }
  },
  required: ['company_name']
}

for await (const message of query({
  prompt: 'Research Anthropic and provide key company information',
  options: {
    outputFormat: {
      type: 'json_schema',
      schema: schema
    }
  }
})) {
  // 结果消息包含带有经过验证数据的 structured_output
  if (message.type === 'result' && message.structured_output) {
    console.log(message.structured_output)
    // { company_name: "Anthropic", founded_year: 2021, headquarters: "San Francisco, CA" }
  }
}

======== 使用 zod 来约束 =========

import { z } from 'zod'
import { query } from '@anthropic-ai/claude-agent-sdk'

// 使用 Zod 定义 schema
const FeaturePlan = z.object({
  feature_name: z.string(),
  summary: z.string(),
  steps: z.array(z.object({
    step_number: z.number(),
    description: z.string(),
    estimated_complexity: z.enum(['low', 'medium', 'high'])
  })),
  risks: z.array(z.string())
})

type FeaturePlan = z.infer<typeof FeaturePlan>

// 转换为 JSON Schema
const schema = z.toJSONSchema(FeaturePlan)

// 在查询中使用
for await (const message of query({
  prompt: 'Plan how to add dark mode support to a React app. Break it into implementation steps.',
  options: {
    outputFormat: {
      type: 'json_schema',
      schema: schema
    }
  }
})) {
  if (message.type === 'result' && message.structured_output) {
    // 验证并获取完全类型化的结果
    const parsed = FeaturePlan.safeParse(message.structured_output)
    if (parsed.success) {
      const plan: FeaturePlan = parsed.data
      console.log(`Feature: ${plan.feature_name}`)
      console.log(`Summary: ${plan.summary}`)
      plan.steps.forEach(step => {
        console.log(`${step.step_number}. [${step.estimated_complexity}] ${step.description}`)
      })
    }
  }
}
```


## 4.8 部署指南

部署沙箱：https://platform.claude.com/docs/zh-CN/agent-sdk/hosting

部署AI：https://platform.claude.com/docs/zh-CN/agent-sdk/secure-deployment












# 99 其他

## 99.1 Anthropic / OpenAI 协议区别

基础 Anthropic 风格接口在 SiliconFlow 上是可用的，但 **SiliconFlow 的“Claude Code / Claude Agent SDK 兼容层”没有把真实 Claude Code 请求形态完整跑通**；本地 SDK/CLI 确实会发送比最小 /v1/messages 更复杂的请求，但当前报错文本本身是上游返回的，不是我们本地代码凭空生成的。[Anthropic Messages API](https://docs.anthropic.com/en/api/messages-examples) [SiliconFlow Messages](https://docs.siliconflow.cn/cn/api-reference/chat-completions/messages) [SiliconFlow Claude Code](https://docs.siliconflow.cn/cn/usercases/use-siliconcloud-in-ClaudeCode)

**OpenAI 和 Anthropic API 的核心差异**  
OpenAI 目前对新项目主推的是 POST /v1/responses，请求主体核心字段是 model 和 input，响应主体是 object: "response"，正文落在 output 数组里；OpenAI 同时还保留 chat/completions，它更接近传统 messages -> choices 形态。[OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses/create) [OpenAI Text Generation](https://platform.openai.com/docs/guides/text?api-mode=responses)

Anthropic 的主接口是 POST /v1/messages，请求核心字段是 model、max_tokens 和 messages，并且官方文档要求带 x-api-key 与 anthropic-version 请求头；响应主体是 type: "message"，正文在 content 数组里，usage 也直接挂在顶层对象上。[Anthropic Messages API](https://docs.anthropic.com/en/api/messages-examples)

如果拿“最相近的旧接口”比较，OpenAI chat/completions 的返回是 choices[].message.content，而 Anthropic messages 的返回是 content[] block；这意味着两者不是“换个 base URL 就能完全互通”的关系，而是 **请求包体和响应包体的 envelope 都不同**。[OpenAI Chat Completions](https://platform.openai.com/docs/guides/text?api-mode=chat) [Anthropic Messages API](https://docs.anthropic.com/en/api/messages-examples)

**SiliconFlow 支持 Anthropic 风格请求时，结果是什么样**  
SiliconFlow 官方文档确实给出了 Anthropic 风格的 POST /v1/messages 页面，也给出了 Claude Code 的接入页面，文档里要求设置 ANTHROPIC_BASE_URL=https://api.siliconflow.cn/、ANTHROPIC_API_KEY 和 ANTHROPIC_MODEL。[SiliconFlow Messages](https://docs.siliconflow.cn/cn/api-reference/chat-completions/messages) [SiliconFlow Claude Code](https://docs.siliconflow.cn/cn/usercases/use-siliconcloud-in-ClaudeCode)

我本地实际用 Pro/zai-org/GLM-5 直打 https://api.siliconflow.cn/v1/messages，无论是用 Anthropic 风格的 x-api-key + anthropic-version，还是用 SiliconFlow 文档写法的 Authorization: Bearer ...，都返回了 **Anthropic 风格对象**：顶层有 type: "message"、role: "assistant"、model: "Pro/zai-org/GLM-5"、stop_reason: "end_turn"、usage，正文在 content 数组里，数组里既可能有 thinking block，也可能有 text block。这个结果说明 **SiliconFlow 的基础 /v1/messages 端点本身是通的**。[SiliconFlow Messages](https://docs.siliconflow.cn/cn/api-reference/chat-completions/messages)

**问题具体出在哪里**  
真实 claude CLI 2.1.80 在同样的 ANTHROPIC_BASE_URL=https://api.siliconflow.cn/、同样的 key、同样的 ANTHROPIC_MODEL=Pro/zai-org/GLM-5 下，返回的是 API Error: 400 {"type":"error","error":{"type":"invalid_request_error","message":"模型配置不存在: Pro/zai-org/GLM-5"}}；而这时我手写的最小 /v1/messages 请求是成功的。这个对照说明：**不是 GLM-5 模型本身在 SiliconFlow 上不可用，而是 Claude Code 发出的那种请求形态触发了另一个不兼容分支。** [SiliconFlow Messages](https://docs.siliconflow.cn/cn/api-reference/chat-completions/messages)

你项目里的 SDK 路径也给了同样方向的证据。run-agent.mjs (line 93) 不是在发一个最小消息请求，而是通过 @anthropic-ai/claude-agent-sdk 打开了 Read/Glob/Grep 工具、preset: claude_code 的系统提示和 json_schema 输出格式；这比最小 /v1/messages 明显更重。run-agent.mjs (line 93)

本地真实 Claude Code 的 bundle 里也能直接看到这一点：它走的是 client.beta.messages.create(...) / client.beta.messages.stream(...)，还会带 thinking、skipSystemPromptPrefix、tool_choice、以及部分 anthropic-beta / x-stainless-helper 头；这和我们手写的最小 /v1/messages 请求不是一回事。cli.js (line 314) cli.js (line 2828) cli.js (line 165)

**报错是不是 Claude Code SDK 本地造出来的**  
不是。Claude Code returned an error result: ... 这一层是 SDK 包装出来的前缀，位置在 sdk.mjs (line 19)。API Error: ... 这一层是 Claude Code CLI 的包装前缀，位置在 cli.js (line 165)。但里面那句中文，比如 模型配置不存在: Pro/zai-org/GLM-5 或 接口仅可用于Claude Code客户端，是上游接口返回的 message，不是本地代码写死的。sdk.mjs (line 19) cli.js (line 165)

**最终判断**  
如果问题表述成“SiliconFlow 支不支持 Anthropic 风格 API”，答案是 **支持基础 /v1/messages**，而且我本地已经实测成功。[SiliconFlow Messages](https://docs.siliconflow.cn/cn/api-reference/chat-completions/messages)

如果问题表述成“SiliconFlow 能不能无缝替代 Anthropic 后端来跑真实 Claude Code / Claude Agent SDK”，答案是 **当前不能视为可用**。原因不是本地 SDK 伪造错误，而是 **SiliconFlow 的 Claude Code 兼容层没有完整兼容 Claude Code/SDK 发出的 richer request shape**；真实 claude CLI 和 SDK 路径都失败，而最小 /v1/messages 成功，这个证据链已经足够把根因指向 **SiliconFlow 兼容层**，不是你本地 agent-code 包装逻辑。 [SiliconFlow Claude Code](https://docs.siliconflow.cn/cn/usercases/use-siliconcloud-in-ClaudeCode) run-agent.mjs (line 93) cli.js (line 314)

补一条边界信息：Anthropic 的 Agent SDK 官方文档明确写的是用 Anthropic API key，或者第三方云上的 Bedrock / Vertex AI / Azure OpenAI 这几类正式接入；文档并没有把“任意第三方自定义 Anthropic 兼容 base URL”列为官方支持面，所以把 SiliconFlow 直接塞到 Claude Agent SDK 后面，本身就不在 Anthropic 明确承诺的兼容范围内。[Anthropic Agent SDK Overview](https://platform.claude.com/docs/en/agent-sdk/overview)


