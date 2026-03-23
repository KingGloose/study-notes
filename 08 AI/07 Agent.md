# 1 基本介绍


# 2 基本使用



# 4 Claude Agent

[(2) X 上的 Tw93：“你不知道的 Claude Code：架构、治理与工程实践” / X](https://x.com/HiTw93/status/2032091246588518683)

## 4.1 基本介绍

### 4.1.1 基本介绍

Claude Code 本质是拆成六层来看：只强化其中一层，系统就会失衡，CLAUDE.md 写太长，上下文先污染自己了；工具堆太多了，选择就搞不清楚了；subagents 开得到处都是，状态就漂移了；验证这步跳过了，出了问题根本不知道是哪里挂的。

![](assets/07%20Agent/file-20260323231911855.jpg)

![](assets/07%20Agent/file-20260323232100912.jpg)

Claude Code 的核心不是"回答"，而是一个反复循环的代理过程：

![](assets/07%20Agent/file-20260323231952803.jpg)

![](assets/07%20Agent/file-20260323232009011.jpg)

对着这几个面看，很多问题就好排查了。结果不稳定，查上下文加载顺序，不是模型的事；自动化失控，看控制层有没有设计，不是 agent 太主动；长会话质量下降，中间产物把上下文污染了，换个新会话比反复调 prompt 有用得多。

![](assets/07%20Agent/file-20260323232032615.jpg)



### 4.1.2 上下文工程

#### 4.1.2.1 基本介绍

![](assets/07%20Agent/file-20260323232419749.jpg)

Claude Code 的 200K 上下文并非全部可用：

```*
200K 总上下文
├── 固定开销 (~15-20K)
│   ├── 系统指令: ~2K
│   ├── 所有启用的 Skill 描述符: ~1-5K
│   ├── MCP Server 工具定义: ~10-20K  ← 最大隐形杀手
│   └── LSP 状态: ~2-5K
│
├── 半固定 (~5-10K)
│   ├── CLAUDE.md: ~2-5K
│   └── Memory: ~1-2K
│
└── 动态可用 (~160-180K)
    ├── 对话历史
    ├── 文件内容
    └── 工具调用结果
```

一个典型 MCP Server（如 GitHub）包含 20-30 个工具定义，每个约 200 tokens，合计 4,000-6,000 tokens。接 5 个 Server，光这部分固定开销就到了 25,000 tokens（12.5%）。我第一次算出这个数字的时候，真没想到有这么多，在要读大量代码的场景，这 12.5% 真的很关键。

![](assets/07%20Agent/file-20260323232444497.jpg)

推荐的上下文分层，说白了，偶尔用的东西就不要每次都加载进来

```*
始终常驻    → CLAUDE.md：项目契约 / 构建命令 / 禁止事项
按路径加载  → rules：语言 / 目录 / 文件类型特定规则
按需加载    → Skills：工作流 / 领域知识
隔离加载    → Subagents：大量探索 / 并行研究
不进上下文  → Hooks：确定性脚本 / 审计 / 阻断
```


#### 4.1.2.2 CLAUDE.md

- 保持 CLAUDE.md 短、硬、可执行，优先写命令、约束、架构边界。Anthropic 官方自己的 CLAUDE.md 大约只有 2.5K tokens，可以参考
- 把大型参考文档拆到 Skills 的 supporting files，不要塞进 SKILL.md 正文
- 使用 .claude/rules/ 做路径/语言规则，不让根 CLAUDE.md 承担所有差异
- 长会话主动用 /context 观察消耗，不要等系统自动压缩后再补救
- 任务切换优先 /clear，同一任务进入新阶段用 /compact
- 把 Compact Instructions 写进 CLAUDE.md，压缩后必须保留什么由你控制，不由算法猜



那么如何写比较合适呢？

**应该放什么**
- 怎么 build、怎么 test、怎么跑（最核心）
- 关键目录结构与模块边界
- 代码风格和命名约束
- 那些不明显的环境坑
- 绝对不能干的事（NEVER 列表）
- 压缩时必须保留的信息（Compact Instructions）

**不该放什么**
- 大段背景介绍
- 完整 API 文档
- 空泛原则，如"写高质量代码"
- Claude 通过读仓库即可推断的显然信息
- 大量背景资料和低频任务知识（这些放到 Skills）


```markdown
# Project Contract

## Build And Test

- Install: `pnpm install`
- Dev: `pnpm dev`
- Test: `pnpm test`
- Typecheck: `pnpm typecheck`
- Lint: `pnpm lint`

## Architecture Boundaries

- HTTP handlers live in `src/http/handlers/`
- Domain logic lives in `src/domain/`
- Do not put persistence logic in handlers
- Shared types live in `src/contracts/`

## Coding Conventions

- Prefer pure functions in domain layer
- Do not introduce new global state without explicit justification
- Reuse existing error types from `src/errors/`

## Safety Rails

## NEVER

- Modify `.env`, lockfiles, or CI secrets without explicit approval
- Remove feature flags without searching all call sites
- Commit without running tests

## ALWAYS

- Show diff before committing
- Update CHANGELOG for user-facing changes

## Verification

- Backend changes: `make test` + `make lint`
- API changes: update contract tests under `tests/contracts/`
- UI changes: capture before/after screenshots

## Compact Instructions

Preserve:

1. Architecture decisions (NEVER summarize)
2. Modified files and key changes
3. Current verification status (pass/fail commands)
4. Open risks, TODOs, rollback notes
```

我最喜欢的一个技巧：每次纠正 Claude 的错误后，让它自己更新 CLAUDE.md：

> "Update your CLAUDE.md so you don't make that mistake again."

Claude 在给自己补这类规则时其实还挺好用，用久了确实越来越少犯同样的错。不过也要定期 review，时间一长总会有些条目慢慢过时，当初有用的限制现在未必还适合



#### 4.1.2.3 Tool Output

前面算的是 MCP 工具定义的固定开销，但动态部分同样有个坑容易被忽视：Tool Output。cargo test 一次完整输出动辄几千行，git log、find、grep 在稍大的仓库里也能轻松塞满屏幕。这些输出 Claude 并不需要全看，但只要它出现在上下文里，就是实实在在的 token 消耗，同样会挤掉对话历史和文件内容的空间。

后来看到 [RTK（Rust Token Killer）](https://www.rtk-ai.app/)

这个思路觉得挺对的，它做的事很简单：在命令输出到 Claude 之前自动过滤，只留决策需要的核心信息。比如 cargo test：

```text
# Claude 看到的原始输出
running 262 tests
test auth::test_login ... ok
...（几千行）

# 走 RTK 之后
✓ cargo test: 262 passed (1 suite, 0.08s)
```

Claude 真正需要知道的就是「过了还是挂了，挂在哪里」，其他都是噪声。它通过 Hook 透明重写命令，对 Claude Code 来说完全无感。

#### 4.1.2.4 压缩机制的陷阱

默认压缩算法按"可重新读取"判断，早期的 Tool Output 和文件内容会被优先删掉，顺带把架构决策和约束理由也一起扔了。两小时后再改，可能根本不记得两小时前定了什么，莫名其妙的 Bug 就是这么来的。

![](assets/07%20Agent/file-20260323233501993.jpg)

解决方案就是在 CLAUDE.md 里写明：

```markdown
## Compact Instructions

When compressing, preserve in priority order:

1. Architecture decisions (NEVER summarize)
2. Modified files and their key changes
3. Current verification status (pass/fail)
4. Open TODOs and rollback notes
5. Tool outputs (can delete, keep pass/fail only)
```

除了写 Compact Instructions，还有一种更主动的方案：在开新会话前，先让 Claude 写一份 HANDOFF.md，把当前进度、尝试过什么、哪些走通了、哪些是死路、下一步该做什么写清楚。下一个 Claude 实例只读这个文件就能接着做，不依赖压缩算法的摘要质量：

在 HANDOFF.md 里写清楚现在的进展。解释你试了什么、什么有效、什么没用，让下一个拿到新鲜上下文的 agent 只看这个文件就能继续完成任务。

写完后快速扫一眼，有缺漏直接让它补，然后开新会话，把 HANDOFF.md 的路径发过去就行。



### 4.1.3 完整工程布局

全局约束（CLAUDE.md）、路径约束（rules）、工作流（skills）和架构细节各归各位，Claude Code 跑起来会稳很多。假如你同时维护多个项目，可以把稳定的个人基线放在 ~/.claude/，各项目的差异放在项目级 .claude/，通过同步脚本分发，不同项目之间就不会互相污染了。

```plaintext
Project/
├── CLAUDE.md
├── .claude/
│   ├── rules/
│   │   ├── core.md
│   │   ├── config.md
│   │   └── release.md
│   ├── skills/
│   │   ├── runtime-diagnosis/     # 统一收集日志、状态和依赖
│   │   ├── config-migration/      # 配置迁移回滚防污
│   │   ├── release-check/         # 发布前校验、smoke test
│   │   └── incident-triage/       # 线上故障分诊
│   ├── agents/
│   │   ├── reviewer.md
│   │   └── explorer.md
│   └── settings.json
└── docs/
    └── ai/
        ├── architecture.md
        └── release-runbook.md
```

最好不要做如下的事情

![](assets/07%20Agent/file-20260323235433672.jpg)







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

在 100 次编辑的会话中，每次节省 30-60 秒，累积节省 1-2 小时，还挺可观的。注意限制输出长度（| head -30），避免 Hook 输出反而污染上下文。如果不想在每条命令后面手动加截断，可以看看第 3 节提到的 RTK，它把这件事系统化了。

Hooks + Skills + CLAUDE.md 三层叠加
- CLAUDE.md：声明"提交前必须通过测试和 lint"
- Skill：告诉 Claude 在什么顺序下运行测试、如何看失败、如何修复
- Hook：对关键路径执行硬性校验，必要时阻断

用下来感觉，三样少任何一层都会有漏洞。只写 CLAUDE.md 规则，Claude 经常当没看见；只靠 Hooks，细节判断又做不了，放在一起才比较稳。

![](assets/07%20Agent/file-20260323234705501.jpg)

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

### 4.8.1 基本介绍

https://platform.claude.com/docs/zh-CN/agent-sdk/hosting ｜ https://platform.claude.com/docs/zh-CN/agent-sdk/secure-deployment

`hosting` 和 `secure-deployment` 这两章，本质上都在讲 **Claude Agent SDK 上线时该怎么部署**，只是关注点不同。`hosting` 讨论的是 **Agent 应该跑在什么环境里、以什么会话模式托管**；`secure-deployment` 讨论的是 **既然 Agent 能执行命令、读写文件、访问外部服务，那么怎样把风险控制在可接受范围内**。官方也明确说明，Claude Agent SDK 不同于传统的无状态 LLM API，它会维护对话状态，并在持久化环境中执行命令；而安全部署章节则专门承接“基本沙箱之外的安全加固”，包括网络控制、凭证管理和隔离选项。

对前端工程师来说，这两章最重要的提醒是：**Agent 不是一个普通的“问一句答一句”的接口**。官方在托管文档里直接把它描述成“长时间运行的进程”，会在持久化 shell 环境中执行命令、在工作目录中管理文件操作，并利用之前交互的上下文继续处理工具执行。也正因为它能“持续工作”，所以安全问题不能只看模型回答对不对，还要看它**能接触什么、能调用什么、能把数据发到哪里**。


### 4.8.2 基本使用

**1、先理解托管前提：它应该跑在什么环境里**

官方建议，在生产环境中，SDK 应该运行在**基于容器的沙箱环境**中，因为这种环境可以提供进程隔离、资源限制、网络控制和临时文件系统。对于 TypeScript SDK，基础依赖是 Node.js 18+；另外 Claude Code CLI 也需要 Node.js，并需要安装 `@anthropic-ai/claude-code`。官方还给出了一个推荐起点：每个实例约 1GiB 内存、5GiB 磁盘和 1 个 CPU，并且至少要能出站访问 `api.anthropic.com`。

这意味着，前端工程师如果只是本地试验，可以先在本机跑起来；但只要准备进入生产环境，就不应该把 Agent 直接丢到主业务机里裸跑。因为文档给出的默认方向就是“沙箱容器 + 资源限制 + 网络控制”，这不是锦上添花，而是官方建议的基础运行方式。

---


**2、部署模式怎么选：4 种托管模式**

官方在 `hosting` 里给了 4 种典型模式。

第一种是 **临时会话**。它的做法是：**每个用户任务启动一个新容器，任务完成后销毁**。官方明确说这最适合一次性任务，例如 bug 调查与修复、发票处理、翻译任务、图像或视频处理。

第二种是 **长时间运行会话**。它会维护持久化容器实例，通常会在容器内按需运行多个 Claude Agent 进程。官方说它最适合那些**无需用户持续输入、可以主动采取行动、持续提供内容、或者处理大量消息流**的代理，比如邮件代理、网站构建器、高频聊天机器人。

第三种是 **混合会话**。它使用临时容器，但可以通过数据库中的历史记录或 SDK 的会话恢复能力，把之前状态重新填充进来。官方把它定位给“用户间歇性交互、容器关闭后还能继续”的场景，比如个人项目经理、深度研究、客户支持代理。

第四种是 **单容器模式**。它是在一个全局容器中运行多个 Claude Agent SDK 进程，适合需要紧密协作的代理。但官方也直接提醒，这可能是最不常用的模式，因为必须防止代理之间相互覆盖。

如果把这 4 种模式翻译成更好落地的选型建议，那么通常可以这么理解：  
**一次性任务选临时会话，间歇式持续任务选混合会话，持续消息流或自治代理才考虑长时间运行会话，单容器模式是更少见的特殊方案。** 这个结论是根据官方对各模式的用途定义总结出来的。

---

**3、安全部署时到底要做什么**

`secure-deployment` 先解释了为什么安全会变成核心问题：Agent 可能因为**提示注入**或模型错误而采取非预期操作。文档举了一个很直观的风险：如果代理处理了一个恶意文件，而文件里嵌入了“把客户数据发到外部服务器”的指令，那么如果没有额外网络控制，它就可能真的尝试这样做。官方的态度很明确：哪怕模型本身已经很强，**纵深防御仍然是好实践**。

围绕这个目标，文档给了三个核心安全原则。

第一是 **安全边界**。官方定义为：把不同信任级别的组件隔开，把敏感资源放在 Agent 所在边界之外。最典型的例子就是：不要把 API Key 直接给 Agent，而是在边界外放一个代理服务器，由代理服务器在转发请求时注入凭证。这样 Agent 可以发请求，但永远看不到凭证本身。文档还特别指出，这对多租户部署和处理不可信内容尤其有用。

第二是 **最小权限**。官方给的操作建议非常直接：文件系统只挂载所需目录，优先只读；网络通过代理限制到特定端点；凭证通过代理注入而不是直接暴露；系统能力上，容器里应删除 Linux capabilities。

第三是 **纵深防御**。文档推荐把容器隔离、网络限制、文件系统控制、以及在代理服务器处做请求验证叠加起来使用，并明确说：正确的组合取决于你的威胁模型和运营需求。也就是说，安全不是“只配一个 Docker 就完事”，而是多层控制组合。

---

**4、隔离方案怎么选：轻量到重型的路线**

官方把隔离技术按“隔离强度、性能开销、复杂性”做了分类：沙箱运行时、Docker 容器、gVisor、虚拟机（如 Firecracker、QEMU）都可以作为 Agent 的运行边界，但它们在安全强度、性能和运维复杂度之间各有权衡。

如果你不想一开始就上重容器，文档给了一个轻量选项：`sandbox-runtime`。官方说它可以在**不使用容器**的情况下，在操作系统层面限制文件系统和网络访问；并且指出对于很多单开发者和 CI/CD 用例，它能在最小设置下显著提高安全门槛。

如果进入更正式的生产阶段，文档给了一个安全加固容器的例子，包括 `--cap-drop ALL`、`--security-opt no-new-privileges`、`--read-only`、`--network none`、资源限制、只读挂载代码目录等。这说明容器并不是“有就行”，而是要通过文件系统、网络、权限、资源限制一起收紧。

在更高安全需求下，文档进一步介绍了 gVisor 和虚拟机路线。官方对 gVisor 的解释是：普通容器共享主机内核，而 gVisor 通过在用户空间拦截系统调用，缩小恶意代码接触真实内核的攻击面。

### 4.8.3 系统原语

#### 4.8.3.1 基本介绍

操作系统原语就是**内核直接提供的底层能力**，比如进程、文件权限、网络、挂载、系统调用、资源限制。沙箱不是魔法，本质上就是用这些原语把程序的能力**圈起来**。

你可以把它想成前端里的浏览器原生能力：DOM API、Event Loop、`postMessage`、`fetch`、`localStorage`

这些都是“浏览器原语”。  你写 React、Vue、状态管理库，其实也是在这些原语上搭更高一层的抽象。

操作系统也一样：Docker 不是凭空发明隔离、sandbox-runtime 也不是凭空发明限制、它们是在 **OS 原语** 之上做封装

#### 4.8.3.2 沙盒化

因为操作系统本来就控制着程序，所以只要把这些权限收紧，就能形成沙箱。
- 能看到哪些文件
- 能访问哪些网络
- 能调用哪些系统能力
- 能占用多少 CPU / 内存

那么为什么能隔离呢？

**1. namespace：隔离视角**  
让进程看到的是一套“自己的世界”。  
比如只能看到自己的进程、自己的网络、自己的挂载点。

**2. cgroups：限制资源**  
控制一个进程最多能用多少 CPU、内存、磁盘、进程数。  
作用是防止程序失控，把机器拖死。

**3. seccomp：过滤系统调用**  
限制程序能调用哪些内核接口。  
本质上是给程序的“底层 API”加白名单，防止高危操作。

**4. capabilities：拆分 root 权限**  
把 root 的大权限拆成很多小权限。  
这样程序就算权限较高，也只拿到必须那一小部分，而不是全能。

一句话总结：**namespace 负责隔离，cgroups 负责限流，seccomp 负责拦底层能力，capabilities 负责收权限。**  它们组合起来，就能把程序放进一个受限的小环境里，这就是沙箱。



## 4.9 系统提示词

用户修改、添加 Claude 默认提示词：
https://platform.claude.com/docs/zh-CN/agent-sdk/modifying-system-prompts





## 4.10 MCP / Skills

Tools：https://platform.claude.com/docs/zh-CN/agent-sdk/mcp ｜ https://platform.claude.com/docs/zh-CN/agent-sdk/custom-tools

Skills：https://platform.claude.com/docs/zh-CN/agent-sdk/skills


## 4.10.1 工具设计思路

我后面越用越觉得，给 Claude 的工具和给人写的 API 不是一回事。给人用的 API 往往会追求功能齐全，但给 agent 用，重点不是功能堆得多完整，而是让它更容易用对。

![](assets/07%20Agent/file-20260323234414306.jpg)

几个实用设计原则
- 名称前缀按系统或资源分层：github_pr_* 、jira_issue_*
- 对大响应支持 response_format: concise / detailed
- 错误响应要教模型如何修正，不要只抛 opaque error code
- 能合并成高层任务工具时，不要暴露过多底层碎片工具，避免 list_all_* 让模型自行筛选


## 4.11 SubAgent

https://platform.claude.com/docs/zh-CN/agent-sdk/subagents

## 4.12 Plan 模式

https://platform.claude.com/docs/zh-CN/agent-sdk/todo-tracking


## 4.13 提示词缓存

这块我之前在很多教程里都没怎么看到有人展开讲，但它其实很影响 Claude Code 的成本结构和很多设计取舍。

工程界有句话 "Cache Rules Everything Around Me"，对 agent 同样如此，Claude Code 的整个架构都是围绕 Prompt 缓存构建的，高命中率不光省钱，速率限制也会松很多，Anthropic 甚至会对命中率跑告警，太低直接宣布 SEV。

![](assets/07%20Agent/file-20260323234844632.jpg)

Prompt 缓存是按前缀匹配工作的，从请求开头到每个 cache_control 断点之前的内容都会被缓存。所以这里的顺序很重要：

```markdown
Claude Code 的 Prompt 顺序：
1. System Prompt → 静态，锁定
2. Tool Definitions → 静态，锁定
3. Chat History → 动态，在后面
4. 当前用户输入 → 最后
```

破坏缓存的常见陷阱
- 在静态系统 Prompt 中放入带时间戳的内容（让它每次都变）
- 非确定性地打乱工具定义顺序
- 会话中途增删工具

那像当前时间这种动态信息怎么办？别去动系统 Prompt，放到下一条消息里传进去就行。Claude Code 自己也是这么做的，用户消息里加 < system-reminder > 标签，系统 Prompt 不动，缓存也就不会被打坏。

Prompt 缓存是模型唯一的。假如你已经和 Opus 对话了 100K tokens，想问个简单问题，切换到 Haiku 实际上比继续用 Opus 更贵，因为要为 Haiku 重建整个缓存。确实需要切换的话，用 Subagent 交接：Opus 准备一条"交接消息"给另一个模型，说明需要完成的任务就行。

![](assets/07%20Agent/file-20260323235023689.jpg)

上图是 Compaction（上下文压缩）的执行流程：左边是上下文快满时的状态，中间是 Claude Code 开一个 fork 调用，把完整对话历史喂给模型，加一句"Summarize this conversation"，这一步命中缓存所以只需 1/10 的价格，右边是压缩完之后，原来几十轮对话被替换成一段 ~20k tokens 的摘要，System + Tools 还在，再挂上之前用到的文件引用，腾出空间继续新的轮次。

直觉上 Plan Mode 应该切换成只读工具集，但这会破坏缓存。实际实现是：EnterPlanMode 是模型可以自己调用的工具，检测到复杂问题时自主进入 plan mode，工具集不变，缓存不受影响。

defer_loading：工具的延迟加载：Claude Code 有数十个 MCP 工具，每次请求全量包含会很贵，但中途移除会破坏缓存。解决方案是发送轻量级 stub，只有工具名，标记 defer_loading: true。模型通过 ToolSearch 工具"发现"它们，完整的工具 schema 只在模型选择后才加载，这样缓存前缀保持稳定。





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


