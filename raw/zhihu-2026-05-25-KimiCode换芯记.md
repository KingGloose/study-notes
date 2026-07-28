# Kimi Code 换芯记：从 Python 到 TypeScript，一次被低估的终端 Agent 架构革命

- 来源: 知乎专栏
- 原文链接: https://zhuanlan.zhihu.com/p/2042390678047641743
- 发布: 编辑于 2026-05-25 23:55・四川
- 摄入日期: 2026-07-28
- 提取方式: kg-browser（真实 Chrome，登录态）+ markdownify

---

Kimi 最近把 Agent 从 Python 转成了 Typescipt 和 [pi-tui](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=pi-tui&zhida_source=entity) 的 kimi-code 新的 Agent，这个蛮有意思的，为什么 Kimi 要这么做。是跟着 Claude code 的步伐吗？

让我们看一下 Kimi-code 的结构变化

| 维度 | 旧版 kimi-cli | 新版 kimi-code |
| --- | --- | --- |
| 语言 | Python 3.12+ | TypeScript |
| 运行时 | [CPython](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=CPython&zhida_source=entity) | Node.js ≥ 24.15.0 |
| 包管理 | uv / pip | pnpm 10.33.0 |
| CLI 框架 | Typer | Commander |
| TUI 渲染 | Rich + prompt-toolkit | pi-tui |
| 配置校验 | Pydantic + tomlkit | Zod + smol-toml |
| Lint | — | oxlint |
| 构建 | PyInstaller | Node.js [SEA](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=SEA&zhida_source=entity) + postject |

这种迁移不是"把 Python 文件后缀改成 .ts"那么简单。它涉及核心抽象层（LLM 交互、OS 执行环境）的跨语言重写、终端 UI 框架的完全替换、以及构建产物的形态变革（从虚拟环境到[单二进制文件](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E5%8D%95%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%96%87%E4%BB%B6&zhida_source=entity)）

新版 Kimi Code 打出的第一个卖点是：**"Install with one command: no Node.js setup, PATH gymnastics, or global module conflicts."**（一行命令安装，无需 Node.js、无需折腾 PATH、无全局模块冲突。）

为什么 kimi 要强调这个

老版 `kimi-cli` 基于 Python，虽然用 `uv` 或 `pipx` 安装体验已经不错，但本质上它仍然是一个**解释型语言的包**。用户机器上必须有兼容的 Python 版本，依赖要解析，虚拟环境要隔离，不同平台的 wheels 要匹配。对于想覆盖"所有开发者"的终端工具来说，这始终是一个摩擦力点

同样，基于 python 的 vllm/sglang 也一直面临版本依赖和适配的“地狱”

Kimi 新版的做法：把 Node.js 和业务代码焊在一起

`kimi-code` 的构建流程藏在 `apps/kimi-code/scripts/native/` 里，分为五步：

1. **tsdown 打包**：用基于 Rolldown 的 tsdown 把整个应用 Tree-shake 并打包成一个 JS Bundle；
2. **SEA Blob 生成**：生成 Node.js 原生 SEA [配置文件](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6&zhida_source=entity)，声明入口和要内嵌的静态资源；
3. **postject 注入**：用 `postject` 工具把 JS Bundle 和资源注入到 Node.js [可执行文件](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%96%87%E4%BB%B6&zhida_source=entity)中；
4. **代码签名**：macOS 下用 `codesign` 签名，release 流程支持正式的 Apple 签名；
5. **验证**：确保注入后的二进制能正常启动且签名有效。

**结果是：一个 `kimi` 文件，内部包含了完整的 Node.js 运行时 + 业务代码 + 静态资源。** 用户下载后，chmod +x 就能跑，和 Go/Rust 编译出的单二进制体验完全一致。

SEA 是什么？

Node.js SEA 就是 Node.js 官方提供的一种能力，能把一个 Node.js 项目（包括代码、资源）打包成一个单独的可执行文件，用户不需要安装 Node.js 就能直接运行

SEA 也是达到这种单一二进制文件编译的关键能力

很多人听到"TypeScript 单二进制"会第一反应想到 Bun 的 `bun build --compile`。但 Kimi Code 没有选 Bun，而是选用了 **Node.js 官方 SEA + postject** 的组合。原因可能是：

* **稳定性与可控性**：Node.js SEA 是官方能力，与特定 Node.js 版本绑定，长期维护更可控；
* **生态兼容**：不需要用户/CI 额外安装 Bun，降低了构建链的复杂度；
* **签名与合规**：macOS 的 notarization 和 codesign 流程对官方 Node.js 二进制更友好。

这可能是因为 Bun 最近被 Anthropic 收购了，处在剧烈的重构中（从 zig 到 Rust）

还有一个很大的特点，kimi-code 用了 pi-tui，这个是什么？ **`@earendil-works/pi-tui`**，这是一个相对独立的 TUI 框架。Kimi Code 的 README 里专门致谢了 pi-tui 的作者。

从架构上看，pi-tui 的引入解决了几个关键问题：

**第一，渲染模型的区分。** [传统终端](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E4%BC%A0%E7%BB%9F%E7%BB%88%E7%AB%AF&zhida_source=entity) UI 要么是"全屏应用"（如 Vim），要么是"[流式输出](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E6%B5%81%E5%BC%8F%E8%BE%93%E5%87%BA&zhida_source=entity)"（如 `ls -la`）。但 AI Agent 的界面是**两者的混合**：既有流式滚动的对话历史，又有需要固定位置的底部输入区、状态栏、浮动审批弹窗。pi-tui 提供了更灵活的 panel 和 layer系统，让 Agent 的复杂布局不再需要用胶水代码拼凑。

**第二，事件驱动的内部协议。** `apps/kimi-code/src/tui/` 里有一个 `reverse-rpc/` 目录，说明 TUI 层与 Agent 核心层是通过类 RPC 的消息协议通信的，而不是直接函数调用。这意味着：

* TUI 可以独立于 Agent 核心进行测试；
* 未来如果要支持 GUI 或 Web 版本，可以复用同一套 Agent 核心，只替换前端；
* 流式输出的[背压](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E8%83%8C%E5%8E%8B&zhida_source=entity)（backpressure）控制更精细。

**第三，为什么是 pi-tui 而不是 Ink？** Ink 是 React 生态里很火的 TUI 框架，但 Kimi Code 没有用它。可能的考量包括：

* Ink 依赖 React 的 reconciler，对于需要极致性能的长会话流式渲染，React 的 diff 开销是负担；
* pi-tui 可能提供了更底层的终端控制原语，方便做自定义的 diff 高亮、视频帧渲染等 Agent 特有的需求；
* 减少 React 依赖可以显著减小 bundle 体积，这对 SEA 单二进制至关重要。

或者这么说，pi-tui 是针对 agent 设计的，未来的优化和适配会更适合 agent。在 AI 技术栈选择上，“喜新厌旧”也是一个合理的选择

如果你只看语言变化，可能会以为 kimi 把以前的代码全扔了。但打开 `packages/` 目录，会发现两个熟悉的名字：**kosong** 和 **kaos**。

老版 Python 的 `kosong` 是一个内部 PyPI 包，描述为"The LLM abstraction layer for modern AI agent applications"，统一了 OpenAI、Anthropic、Google GenAI、Vertex AI、Moonshot API 的调用。

新版的 `@moonshot-ai/kosong` 保留了完全相同的定位，但变成了 TypeScript 包。它依赖：

* `openai`（官方 Node SDK）
* `@anthropic-ai/sdk`
* `@google/genai`
* `zod` + `zod-to-json-schema`（用于工具参数的模式定义与 JSON Schema 转换）

**这不仅仅是翻译，而是利用 TypeScript 的[类型系统](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E7%B1%BB%E5%9E%8B%E7%B3%BB%E7%BB%9F&zhida_source=entity)进行了一次重构。** Zod 的 schema 可以直接推导 TypeScript 类型，工具定义、LLM 响应、消息结构的[类型安全](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E7%B1%BB%E5%9E%8B%E5%AE%89%E5%85%A8&zhida_source=entity)比 Python 的 Pydantic 更紧密地绑定在编译期

我觉得这是个好东西，可以抽象出来作为 Agent 的一个基础开源组件

老版的 `kaos/pykaos` 提供了"本地/远程 SSH 文件和命令执行"的统一抽象。

新版的 `@moonshot-ai/kaos` 直接依赖 `ssh2`，提供了：

* 本地文件系统操作
* 通过 SSH2 的远程执行环境
* 统一的接口让 Agent 不需要关心代码运行在本地还是远程服务器上

ssh 怎么实现本地还是远程服务器的统一呢？

实际上，kaos 做了一个抽象。因为 Agent 需要对文件做这些操作：

运行 shell 命令:exec()

文件操作：readText()、writeText()、stat()、glob()

kaos 设计一个 POSIX-like 的操作系统抽象：

```
exec(...args: string[])           // → SSH exec channel
readText(path: string)            // → SFTP read
writeText(path: string, data)     // → SFTP write
stat(path: string)                // → SFTP stat
iterdir(path: string)             // → SFTP readdir
```

这些操作在 SSH 协议里都有原子级对应，不需要额外封装或模拟。比如： • exec("git", "status") 直接映射到 SSH exec channel • readText("/etc/nginx/nginx.conf") 直接映射到 SFTP open → read → close

通过这种抽象和封装，kaos 就能让 kimi 能操作"任何机器"——你的笔记本、[云服务器](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8&zhida_source=entity)、CI runner、[边缘节点](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E8%BE%B9%E7%BC%98%E8%8A%82%E7%82%B9&zhida_source=entity)

SSH 协议是最通用的协议，POSIX 文件操作是最通用的文件操作，所以 kaos 的适用性就会很广

kaos 也是一个很好的抽象，可以拿出来做 agent 通用库来使用

`packages/agent-core/src/` 是整个产品最值钱的部分。它的目录结构揭示了 Kimi Code 对"Agent 应该长什么样"的理解：

```
agent-core/src/
├── loop/              # Agent 主循环
│   ├── run-turn.ts    # 单轮执行
│   ├── turn-step.ts   # 单步执行
│   ├── tool-call.ts   # 工具调用
│   ├── tool-scheduler.ts  # 工具调度
│   ├── retry.ts       # 重试逻辑
│   ├── llm.ts         # LLM 流式调用
│   └── events.ts      # 内部事件系统
├── agent/             # Agent 运行时
├── session/           # 会话管理
├── tools/             # 工具实现
│   ├── file/          # 文件操作
│   ├── shell/         # Shell 执行
│   ├── web/           # 网页搜索/抓取
│   ├── background/    # 后台任务
│   ├── agent/         # 子 Agent 调用
│   ├── plan/          # Plan 模式
│   ├── ask-user/      # 用户提问
│   └── skill/         # 技能系统
├── mcp/               # MCP 客户端
├── skill/             # 技能发现与加载
├── rpc/               # Wire / ACP 协议
├── config/            # 配置系统
└── logging/           # 结构化日志
```

这个结构与老版 Python 的 `kimi_cli/soul/` + `kimi_cli/tools/` 几乎一一对应，但 TS 版的模块化更清晰：**loop、tools、session、rpc 是完全独立的子系统**，通过事件和接口交互，而不是像 Python 版那样有较多的[隐式耦合](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E9%9A%90%E5%BC%8F%E8%80%A6%E5%90%88&zhida_source=entity)

另外，还有一些边还，例如 tsup 更换为 tsdown；ESLint 换成 oxlint；npm run build 改为SEA标准的build 过程。这些都是工程上加固

尽管语言和技术栈全换了，但 Kimi Code 的"架构 DNA"被完整地保留了下来。

例如 Wire 协议，解决跨语言的调用。具体工具对比如下：

| 工具 | Python 版位置 | TS 版位置 |
| --- | --- | --- |
| ReadFile / WriteFile / StrReplaceFile | tools/file/ | tools/file/ |
| Glob / Grep | tools/file/ | tools/file/ |
| Shell | tools/shell/ | tools/shell/ |
| SearchWeb / FetchURL | tools/web/ | tools/web/ |
| Agent（子 Agent） | subagents/ | tools/agent/ |
| TaskList / TaskOutput / TaskStop | tools/background/ | tools/background/ |
| EnterPlanMode / ExitPlanMode | tools/plan/ | tools/plan/ |
| AskUserQuestion | tools/ask\_user/ | tools/ask-user/ |
| SetTodoList | tools/todo/ | （可能在 tools/ 内） |

这种对齐不是巧合，而是说明团队对"Agent 需要哪些能力"有清晰的共识，重写只是换实现语言，不换产品定义

从这个改变来看，我已经切换了，还没有深度使用。等过一周，可能会有更多的对比出来

但是从这个转换，如此大动干戈啊，为什么要这样做呢，我理解可能有几个原因：

1、简化分发。 通过 Node.js SEA，一个 TypeScript 项目做出了 Go 级别的单二进制分发体验。这打破了"TypeScript/Node.js 不适合做 CLI 工具"的偏见——关键不在于语言，而在于构建工程。

2、TUI 框架的独立趋势 选 pi-tui 而不是 Ink，说明当 Agent 会话的复杂度超过一定阈值后，通用的 React/组件化模型会成为负担，领域专用的 TUI 框架会更有优势。

3、Agent 内核的语言无关性。

kosong、kaos、Wire 协议、工具集、子 Agent 模型——这些核心抽象从 Python 平移到 TypeScript 后依然成立，说明**AI Agent 的[架构模式](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E6%9E%B6%E6%9E%84%E6%A8%A1%E5%BC%8F&zhida_source=entity)正在收敛**。语言只是实现层，Agent 的"操作系统化"（文件、Shell、网络、[子进程](https://zhida.zhihu.com/search?content_id=275562826&content_type=Article&match_order=1&q=%E5%AD%90%E8%BF%9B%E7%A8%8B&zhida_source=entity)、MCP、技能）才是本质。

对于普通用户来说，这次重写可能只意味着启动快了一点、安装简单了一点。但对于观察终端 Agent 演进的开发者来说，Kimi Code 的这次"换芯"，是一张关于未来 AI Native 终端软件该如何构建的 Kimi 的看法

Kimi Code 是开源的，而且如果体验下来的工程能力很好。那的确可以按照这个成功实践来构建自己的 Agent。同时 kosong、kaos 、Wire 都是很好的组件，可以拿来复用。最近好几个新的 Agent ，例如 CommanCode、Flue、都是用 TS 构建的。而 Python 由于性能、类型安全、依赖和 TUI 的不足，可能难以支撑终端 Agent 向“真正好用的生产力工具”演进
