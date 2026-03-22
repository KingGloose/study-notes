# 1 基本使用

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


# 2 流式输出

在 Claude Agent SDK 里，**流式输入**指的是：你的程序不是一次性把一个字符串 prompt 扔给 Agent 就结束，而是把“后续用户消息”作为一个异步可迭代流，持续喂给同一个正在运行的 Agent 会话。官方把它定义为默认且推荐的模式，适合“持久的、交互式的会话”；它允许 Agent 作为长期运行进程接收用户输入、处理中断、显示权限请求并处理会话管理。

官方文档里的 `generateMessages()` 只是一个**示例函数名**；更准确地说，它是你自己写的 `async function*`，用于不断 `yield` 出 `SDKUserMessage`。它不是 SDK 里一个必须叫这个名字的内置 API。这个判断来自两点：一是 `query()` 的 `prompt` 类型是 `string | AsyncIterable<SDKUserMessage>`，二是文档示例自己写了一个 `async function* generateMessages()` 再把它传给 `query()`。

## 2.1 这种模式能带来什么

官方列出的核心能力包括：直接在消息里附加图片、顺序发送多条消息并支持中断、在会话期间完整访问工具和自定义 MCP、支持 hooks、实时看到响应流，以及自然地跨多轮保持上下文。换句话说，它更像一个“活着的 Agent 会话”，而不只是一次普通的 LLM 请求。


## 2.2 真实使用场景

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


## 2.3 Agent 执行完，继续上次的会话

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



# 3 权限处理

https://platform.claude.com/docs/zh-CN/agent-sdk/permissions









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