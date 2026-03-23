【Agent Skills蓝皮书：从概念、局限到使用、制作，一次讲清】 https://www.bilibili.com/video/BV1t467BFEPb/?share_source=copy_web&vd_source=8992a13080c32977bce93a5140823f3b

https://platform.claude.com/docs/zh-CN/agents-and-tools/agent-skills/overview

[(2) X 上的 阿西_出海（2.0版）：“Claude Skills 喂饭级教程，99%的人不会用Skill” / X](https://x.com/imaxichuhai/status/2032397341701906735)


# 1 介绍 

**prompt**：大家应该都比较熟悉了，就是提示词。不论系统提示词还是用户提示词，它们通常都是静态的文本，会一次性加载到上下文。

**Skills**：全称是Agent Skills，以文件夹形式组织而成，包括一个SKILL.md文件和可选资源（如脚本或模板），Agent可以动态发现并按需分阶段加载这些文件内容到上下文。其中的SKILL.md文件在形态上很像prompt。

大家可能都发现它们的不同了：
- **prompt** 是 静态的文本，而 **Skills** 是包含 prompt 在内的文件夹；
- **prompt** 是 一次性加载到上下文的，而 **Skills** 是动态按需分阶段加载到上下文的。


本质其实就是一个提示词加载工程技术的应用
- **Agent Skills** 是“可被 LLM 主动调用的能力模块”，包含名称、描述、输入/输出模式、执行器与权限边界。
- 它把“提示词工程 + 工具函数 + 数据检索/动作执行”工程化，使智能体具备可组合、可复用、可治理的业务能力。
- 社区主流生态包括：OpenAI 工具调用（Function/Tool Calls、Assistants）、LangChain Tools、LlamaIndex Tools、Autogen、CrewAI、Vercel AI Router 等。

典型工作流
- 用户意图 → LLM 规划 → 选择/路由技能 → 参数填充 → 执行 → 返回结果 → 继续/停止。
- 单体技能可直接返回结果；组合技能通过路由器或多轮调用完成复杂任务。

【Agent Skills到底是什么，一个动画彻底搞懂！】 https://www.bilibili.com/video/BV1EXksBGEa8/?share_source=copy_web&vd_source=8992a13080c32977bce93a5140823f3b

![](assets/06%20Skills/file-20260322143345026.jpg)


# 2 基本使用

https://platform.claude.com/docs/zh-CN/agents-and-tools/agent-skills/overview

其中SKILL.md文件是每个 Skill 必须具备的文件，相当于 Skill 的大脑。它由两部分组成：**YAML Frontmatter metadata（元数据层）** 和 **Markdown instructions（指令层）**。

![](assets/06%20Skills/file-20260322165304529.png)


## 2.1 YAML Frontmatter

元数据层，这是 Skill 能被Agent“发现”的关键。通常包含name和description两个字段：
- **name**：就是Skills的名称。只能使用小写字母、数字和连字符。和文件夹名称匹配。
- **description**：描述这个Skill的功能以及触发时机（比如，“在处理PDF文件或用户提及PDF时使用”）。这样Agent就知道该在什么时候激活这个 Skill。具体怎么写好description，有一定的原则和技巧，我们会在第二节详细介绍。

它们就像是Skill的“名片”，让Agent一眼就能知道什么时候该用哪个Skill。

Agent在启动时就会加载Skills的元数据层。比如你安装了10个Skills，Agent在启动时就会加载这10个Skills对应的元数据层。由于每个Skills的元数据层很简短（50-100 tokens），所以占用的上下文空间很小，这也是Skills对比MCP更省token的重要原因之一。

![](assets/06%20Skills/file-20260322165412342.png)


## 2.2 Markdown instructions

指令层，主要包含具体的执行逻辑。这部分内容只有在 Skill 被激活后才会被加载到上下文。它通常包含：
- **触发条件确认**：再次明确技能的适用边界。
- **分步程序（SOP）**：确定性的操作步骤（例如，“第一步：读取文件；第二步：提取类名……”）。这也是SKill被大家视为标准工作手册的原因。
- **Few-Shot Examples（少样本示例）**：通过具体的输入输出对，向模型展示预期的行为模式，这是提高技能执行可靠性的关键手段。

对比元数据层，指令层包含的上下文会更长，一般在 5000 tokens 以内，具体视任务指令长度而定。


## 2.3 Bundled Resources

最简单的Skill，就是只包括SKILL.md文件的。比如我之前分享过的frontend-design skill，就是这种单SKILL.md文件,这种Skill在形态上就很像prompt，也是大家误解的最主要原因。

![](assets/06%20Skills/file-20260322165648466.png)


实际上，更复杂的Skill的目录，是包括脚本、模板等资源文件的。

![](assets/06%20Skills/file-20260322165739213.png)

比如：ui-ux-pro-max-skill，这个在定位、能力都和frontend-design非常相似的Skill，在SKILL.md文件外，还包括CSV设计数据库和Python搜索脚本，Agent在生成 UI 时会自动查询数据库，提供匹配的推荐。

当 Agent 读取到 SKILL.md 的指令层引用了这两个文件时，就会通过 bash 读取 ui-resoning.csv（references文件）和运行 search.py（script文件）。但不同的是，bash 读取 ui-resoning.csv时，csv 的完整内容会加载到上下文窗口；而运行search.py时，bash 只是运行脚本呢并仅接收输出（脚本代码本身不会进入上下文，这也是 Skills 省 token 的另一个重要原因）。

![](assets/06%20Skills/file-20260322170013919.png)

![](assets/06%20Skills/file-20260322170025154.png)

这里补充一个小的知识点：Bash 就是一个**命令行的“翻译官”+“脚本小助手”**：你在终端里敲的命令，它负责告诉电脑去执行，还能把一堆命令写进文件里，让电脑自动帮你干活。

![](assets/06%20Skills/file-20260322204528416.png)

Skills 这种分层加载的设计架构，在 Agent 应用领域中，被称为“渐进式披露”。

Agent 启动时仅加载所有 Skills 的**名称与描述（元数据层）**，当识别到相关任务时，再按需动态加载相应 Skill 的**详细指令（指令层）、参考资料和脚本（资源层）**，从而以最小的上下文消耗扩展Agent能力。

它特别像我们平时看一本书，会先看目录（对应元数据层），然后根据目录翻到对应的章节（指令层），如果这个章节有引用，我们就可以根据引用跳转其它书籍或资源（对应资源层）。


## 2.4 安装 Skills

### Claude Code官方Skills库

Claude Code官方的Skills库有两个（严格来说有三个，其中一个没维护了），是他们不同时间段发布的，两者存在一些重叠的Skills：

早期的：https://github.com/anthropics/skills

最新的：https://github.com/anthropics/claude-plugins-official（我们前面介绍的Frontend-design skill和ralph-loop skill都在这个仓库）

### awesome-claude-skills

GitHub上awesome系列的仓库基本不会太差，这里收录了四个stars数较高的awesome-claude-skills仓库：

https://github.com/ComposioHQ/awesome-claude-skills

https://github.com/travisvn/awesome-claude-skills

https://github.com/BehiSecc/awesome-claude-skills

https://github.com/VoltAgent/awesome-claude-skills

### skillsmp

这个Skills网站收录了目前GitHub社区超8W+的开源Skills，应该是目前收录Skills数量最多的网站。

支持 AI 语义搜索和关键字筛选，也支持按分类浏览、按热度排序。

🔗：https://skillsmp.com

### Skill.sh

前面分享过Vercel官方的三个很实用的Skill项目：React-Best-Practices、Agent Browser以及 add-skill。

这回他们把这些项目整合起来，做了个网站：https://skills.sh/

这个网站提供的核心服务有两个：

第一，通过add skill这个库，实现在不同AI编程工具中快速安装各种Skill；

第二，提供Skills安装排行榜，分总榜和24h榜，大家可以从24h榜快速了解最近都有哪些热门Skills。之前分享的一些热门Skills，比如Vercel官方的、Anthropic官方的、@宝玉老师的、SEO相关的，基本都在榜上。

### claude-scientific-skills

这个Skills资源库比较垂直，是专门科学研究的，目前包括 138 个科学Skills，涵盖生物学、化学、医学、物理学和工程等多个领域。

🔗：https://github.com/K-Dense-AI/claude-scientific-skills

![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=ODkwZmZhYmY1ODY1MjJhNWU4ZDI2MDBlMWI0N2ZhYmRfY1JYeUJ2dmtRODQ5anFDODBBV1dzM0Fpc2NSWVZkcDRfVG9rZW46QW8yZ2JTMUlZb3hwNHR4MWN0SmNodFprbmVoXzE3NzQxODU5ODc6MTc3NDE4OTU4N19WNA)

### @宝玉 Skills

个人开发者的Skills仓库，我个人学习比较多的就是@宝玉 老师的。

@宝玉 老师本身是Prompt、AI编程、Skills的深度实践者，这个开源仓库基本是把他日常工作流（比如文章智能插图、封面图片生成、漫画创作、公众号发布、X发布等）都公开出来了。**大家可以从他的Skills中学习Skils工作流拆解：**

🔗：https://github.com/JimLiu/baoyu-skills/tree/main/skills

![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=MWFkM2NkNTdhMTYwY2U5NzUwZWQyZTA2OWQzMTBhNjVfSUREek1DWGt5bGhvYklMRTVjblhpUXRPZkhVNzFPMnBfVG9rZW46VDVzSWI3bXZvbzVRaUF4UTFnamNyd080bktnXzE3NzQxODU5ODc6MTc3NDE4OTU4N19WNA)

### awesome-moltbot-skills

这是由社区驱动整理的 Skills 库，专门用来武装 moltbot（原clawbot）的

GitHub🔗：https://github.com/VoltAgent/awesome-moltbot-skills

在线版🔗：https://clawdhub.com/skills


## 2.5 使用方式

>自动加载

Skills是被设计为按需自动加载的。以 frontend-design skills 为例，当我们的提示词涉及前端 UI，AI 就会进行意图判断并自动加载相关的 Skills。这是理想的情况。

![](assets/06%20Skills/file-20260322205350280.png)

为什么说这是理想的情况？因为如果你之前频繁使用过 Skills，那么你会遇到这样的情况：**Agent 有时候压根不管你配置的 Skills，直接按照自己的理解开始干活，** 这不是个例，很多开发者都遇到过。

怎么解决这种问题呢？两种方案。一种是通过 Hook 强制调用 Skills。另一种就是用户自己手动加载Skills。

![](assets/06%20Skills/file-20260322205458501.png)

怎么解决这种问题呢？两种方案。一种是通过 Hook 强制调用 Skills。另一种就是用户自己手动加载Skills。

![](assets/06%20Skills/file-20260322205709135.png)

Skills+Hooks的组合方案不是我想出来的，最早由国外大神 Scott Spence 提出。他之前也碰到同样的问题，于是搭了个测试框架，跑了 200 多次测试，找出了两套方案，把激活成功率从最初的 20% 提升到了 80-84%。

https://scottspence.com/posts/how-to-make-claude-code-skills-activate-reliably

![](assets/06%20Skills/file-20260322205725310.png)

整个流程具体是这样的：
1. 在你的项目中创建 `.claude/hooks/skill-forced-eval-hook.sh` （或者在 `~/.claude/hooks/` 下全局创建
2. 将这段强制执行脚本复制到`skill-forced-eval-hook.sh`里
```Plain
Step 1 - EVALUATE: For each skill, state YES/NO with reason
Step 2 - ACTIVATE: Use Skill() tool NOW
Step 3 - IMPLEMENT: Only after activation

CRITICAL: The evaluation is WORTHLESS unless you ACTIVATE the skills.
```
3. 让这段脚本可执行： `chmod +x skill-forced-eval-hook.sh`
4. 添加到 `.claude/settings.json`
```JSON
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
            {
              "type": "command",
              "command": ".claude/hooks/skill-forced-eval-hook.sh"
            }
          ]
        }
     ]
  }
}
```


>手动加载

我们可以在提示词中注明要调用 skill 的名称，这种方法在大部分工具都通用，比如：

```Plain
用frontend-design skills,生成一个简洁的博客网站,单HTML文件
```

在Claude Code和Cursor中，我们还可以通过 / {skill-name} 的快捷命令指定Skills；

![](assets/06%20Skills/file-20260322205908693.png)

在Codex中，则可以通过 $ {skill-name} 的快捷命令指定Skills；

![](assets/06%20Skills/file-20260322205939817.jpg)

# 3 各平台支持

| 工具                   | Skills文档🔗                                                                                 | 全局（用户级）路径                                     | 项目级路径                              |
| -------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------- | ---------------------------------- |
| Claude          Code | [https://code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)           | ~/.claude/skills/                             | .claude/skills/                    |
| Codex                | [https://developers.openai.com/codex/skills/](https://developers.openai.com/codex/skills/) | ~/.codex/skills/                              | .codex/skills/                     |
| Gemini CLI           | [https://geminicli.com/docs/cli/skills/](https://geminicli.com/docs/cli/skills/)           | ~/.gemini/skills/                             | .gemini/skills/                    |
| Opencode             | [https://opencode.ai/docs/skills/](https://opencode.ai/docs/skills/)                       | ~/.config/opencode/skill/ 或 ~/.claude/skills/ | .opencode/skill/ 或 .claude/skills/ |
| Cursor               | [https://cursor.com/cn/docs/context/skills](https://cursor.com/cn/docs/context/skills)     | ~/.cursor/skills/ 或 ~/.claude/skills/         | .cursor/skills/ 或 .claude/skills/  |



# 4 制作 Skills

## 4.1 基本介绍

这里整理的最佳实践，大部分来自[Anthropic官方：Skills制作最佳实践](https://my.feishu.cn/docx/PW2MdTU1pon4stxI8ILcqaimnBf?from=from_copylink)，更详细的内容可以移步原文档查看。

>核心原则

- **简洁是关键**：只添加 AI 原本不了解的上下文。
- **设定适当的自由度**：根据任务的脆弱性和可变性调整具体程度。

>Skills结构

- **SKILL.md-name**：尽量采用动名词形式，比如`processing-pdfs`、`writing-documentation`，避免名称含糊不清，如`helper` 、`documents` ；
- **SKILL.md-descriptions**：要包括Skills的功能和触发条件/使用时机。这样Agent才知道什么时候选择这个Skill
- **SKILL.md-渐进式披露原则**：将 SKILL.md 正文控制在 500 行以内。接近这个限制时，将内容拆分为单独的文件
- **Skills-资源层**：资源层应保持在 SKILL.md 的一级目录 。所有资源层文件都应直接链接到 SKILL.md，以确保Agent在需要时能够读取完整的文件。
- **Skills-资源层**：对于超过 100 行的资源层文件，请在顶部添加目录。这样即使在预览部分读取结果时，Claude 也能看到所有可用信息。  

>工作流和反馈循环

- 将复杂的操作分解成清晰的、循序渐进的步骤。对于特别复杂的流程，提供一份清单，Agent 可以将其复制到回复中，并在执行过程中逐项勾选。
- 实施反馈回路。使用“运行验证器 → 修复错误 → 重复”这种反馈循环模式，能显著提高输出质量。

>双Agent开发Skills

核心思路就是，使用Agent A来创建Skills，然后在Agent B中测试这个Skills。将你在Agent B观察到的一些问题反馈给Agent A进行迭代优化。

>有效的Skills清单

在分享Skills之前，验证：

 **核心质量**
- Description具体并包含关键术语    
- Description包括Skills的功能和使用时机
- SKILL.md 正文在 500 行以下
- 更多详情放在单独的文件中（如果需要）
- 没有时效性信息（或在"旧模式"部分中）
- 整个Skills中术语一致
- 示例要具体，不要抽象
- 文件引用是一层深度    
- 适当使用渐进式披露
- 工作流有清晰的步骤

**代码和脚本**
- 脚本是用来解决问题的，而不是推卸给 Claude
- 错误处理机制清晰明确且有帮助
- 没有"神秘常量"（所有值都合理化）
- 说明文档中列出了所需的软件包，并已确认可用
- 脚本有清晰的文档
- 不使用 Windows 风格的路径（全部为正斜杠）
- 关键操作的验证/验证步骤
- 包含针对质量关键任务的反馈回路

**测试**
- 至少创建了三份评估报告
- 使用 Haiku、Sonnet 和 Opus 进行了测试
- 使用真实使用场景进行了测试
- 团队反馈意见已纳入考虑（如适用）

## 4.2 什么任务值得做成Skills？

Anthropic在官方博客中有回答过这个问题。

官方博客：[Skills explained: How Skills compares to prompts, Projects, MCP, and subagents | Claude](https://claude.com/blog/skills-explained)

> 当你需要 Claude 持续高效地执行特定任务时，请选择Skills。Skills非常适合以下情况：
> - 组织工作流程 ：品牌指南、合规流程、文档模板
> - 专业领域： Excel 公式、PDF 处理、数据分析
> - 个人偏好： 笔记系统、编码模式、研究方法

为了更细致地回答这个问题，我抓取了 skills.sh 安装排行榜 Top 100 的Skill，基于SKILL.md内容，对它们的任务类型分布进行了分析。

![](assets/06%20Skills/file-20260322210719292.jpg)

然后我发现目前大家安装比较多的Skills的类型分布是这样的（注：左侧是Skills类型，右侧是对应的Skills数量）：
1. 增长/营销（SEO/CRO/投放/定价/增长策略）：23
2. 软件工程：前端/全栈 UI 与最佳实践：19
3. 内容生产（图文/幻灯片/图片/媒体处理/社媒分发）：17
4. 工程方法论（计划/执行/协作/评审/调试等流程）：13
5. 文档与办公（PDF/DOCX/PPTX/XLSX/文档协作）：8
6. Agent 工程（MCP/工具链/浏览器自动化等元技能）：5
7. 软件工程：移动开发（Expo/RN/iOS/Android）：4
8. 软件工程：DevOps/发布/CI/CD/依赖维护：4
9. 软件工程：后端/API/数据与数据库：4
10. 沟通与管理（会议/汇报/内部沟通）：2
11. 软件工程：测试/质量保障/验证（偏测试方法）：1

它们大致可以分为三类任务（这三类任务彼此可以重叠）：
- **“高频处理+有可复用流程”的任务**：这类任务目标明确，执行步骤固定，可通过标准化流程或脚本反复、高效地完成。例如，代码审查、自动化测试、CI/CD构建、SEO审计等。
- **“强模板化产出”的任务**：这类任务产出物的格式和风格有固定要求，核心在于将内容高效地适配到预设的模板中。例如社媒配图、PPT制作、品牌设计、报告/周报等。
- **“多模块/多流程组合”的任务**：这类任务本身比较复杂，需要串联或并联多个独立模块或子流程来完成。例如社媒文章的发布（收集资料+选题分析+学习文风+正文写作+配图智能插入）等。

这三类任务，也可以作为三条标准，来判断任务是否值得做成Skills。当然，更简单的判断标准是：**这是一次性任务，还是需要反复做的任务？**

如果只是一次性任务，没必要做成 Skill——Skill 的核心价值在于复用。如果是需要反复做的任务，建议按这个流程走：
1. **手动跑通，沉淀标准：** 先手动执行几次，厘清固定步骤，识别潜在卡点，并明确高质量输出的标准。
2. **示范教学，封装 Skill：** 新建会话，在支持 Skills 的 Agent 中完整演示一遍任务。确认无误后，指示 Agent 将刚才的操作链封装为 Skill，以便复用。
3. **循环使用，持续迭代：** 后续直接调用 Skill 执行任务。每次完成后校验输出，针对不满意之处指令 Agent 调整并更新 Skill。

**简单来说，Skill 的本质是“可复用的最佳实践”。先跑通流程，再固化为Skill，最后在实战中不断打磨。

## 4.3 Skill 三种典型类型

### 类型一：检查清单型（质量门禁）

发布前跑一遍，确保不漏项：

```yaml
---
name: release-check
description: Use before cutting a release to verify build, version, and smoke test.
---

## Pre-flight (All must pass)
- [ ] `cargo build --release` passes
- [ ] `cargo clippy -- -D warnings` clean
- [ ] Version bumped in Cargo.toml
- [ ] CHANGELOG updated
- [ ] `kaku doctor` passes on clean env

## Output
Pass / Fail per item. Any Fail must be fixed before release.
```


### 类型二：工作流型（标准化操作）

配置迁移高风险，显式调用 + 内置回滚步骤：

```yaml
---
name: config-migration
description: Migrate config schema. Run only when explicitly requested.
disable-model-invocation: true
---

## Steps
1. Backup: `cp ~/.config/kaku/config.toml ~/.config/kaku/config.toml.bak`
2. Dry run: `kaku config migrate --dry-run`
3. Apply: remove `--dry-run` after confirming output
4. Verify: `kaku doctor` all pass

## Rollback
`cp ~/.config/kaku/config.toml.bak ~/.config/kaku/config.toml`
```


### 类型三：领域专家型（封装决策框架）

运行时出问题时让 Claude 按固定路径收集证据，不要瞎猜：

```yaml
---
name: runtime-diagnosis
description: Use when kaku crashes, hangs, or behaves unexpectedly at runtime.
---

## Evidence Collection
1. Run `kaku doctor` and capture full output
2. Last 50 lines of `~/.local/share/kaku/logs/`
3. Plugin state: `kaku --list-plugins`

## Decision Matrix
| Symptom | First Check |
|---|---|
| Crash on startup | doctor output → Lua syntax error |
| Rendering glitch | GPU backend / terminal capability |
| Config not applied | Config path + schema version |

## Output Format
Root cause / Blast radius / Fix steps / Verification command
```

描述符写短点，每个 Skill 都在偷你的上下文空间，每个启用的 Skill，描述符常驻上下文，优化前后差距很大：

```yaml
# 低效（~45 tokens）
description: |
  This skill helps you review code changes in Rust projects.
  It checks for common issues like unsafe code, error handling...
  Use this when you want to ensure code quality before merging.

# 高效（~9 tokens）
description: Use for PR reviews with focus on correctness.
```

还有一个很重要的 disable-auto-invoke 使用策略：
- 高频（>1 次/会话）→ 保持 auto-invoke，优化描述符
- 低频（<1 次/会话）→ disable-auto-invoke，手动触发，描述符完全脱离上下文
- 极低频（<1 次/月）→ 移除 Skill，改为 AGENTS.md 中的文档

### Skills 反模式

- 描述过短：description: help with backend（任何后端工作都能触发，哈哈）
- 正文过长：几百行工作手册全塞进 SKILL.md 正文
- 一个 Skill 覆盖 review、deploy、debug、docs、incident 五件事
- 有副作用的 Skill 允许模型自动调用





# 5 技术对比

## 5.1 对比 workflow

说到Workflow，大家第一反应应该就是扣子、Dify、n8n这类工作流编排工具。用户只需要通过拖拽节点和连线，就能搭建好一个自动化流程。

![](assets/06%20Skills/file-20260322210926842.jpg)

Skills 其实也能做类似的事情，这段时间就有用户尝试将自己之前的扣子工作流、n8n工作流转成Skills。

既然都能编排工作流，那它俩的差别在哪里？

核心区别在于三个地方。

注：这里列举的三个不同，主要是指扣子Skills之外的Agent Skills。因为在我看来，目前的扣子Skills和Claude Skills走的是两条不一样的路。这个话题后面有机会再单独展开 ~

### 区别一：确定性不同

Workflow具有高度确定性——用户输入指令后，一定是按照节点顺序推进的，节点 A 执行完一定是节点 B，不会突然跳到节点 C 或节点 D。

但这种确定性的反面是不够灵活，当你的流程固定后，遇到输入条件的变化，整个工作流可能就没法运行了。

在 Workflow 里，如果我一开始就将输入条件固定为图标关键词的输入，它确实可以根据关键词帮我搜索符合条件的SVG图标并转为Chrome插件所需的四种PNG尺寸；但如果我已经有了SVG图标，那我就没法用这个工作流了。而Skills按需自动加载的机制可以解决这种问题。

### 区别二：模块化程度不同

假设我要实现将英文博客翻译为中文，并实现中英文混合排版优化。

如果我之前分别做了「英文博客翻译」和「中英文混合排版优化」两个 Workflow，要实现上面的任务目标，我就需要重新编排一个全新的Workflow，或者在原有的 Workflow 中任选一个进行重新编排。

但如果我之前做的是「英文博客翻译」和「中英文混合排版优化」两个Skill，情况就完全不同了。同样是实现上面的任务目标，我就只需要在Claude Code（或其他IDE/CLI）用自然语言进行编排：

```Markdown
先调用「英文博客翻译」Skill翻译文章，翻译完成后保存为translate.md，然后启动「中英文混合排版优化」Skill进行排版优化
```

### 区别三：分发难度不同

Workflow 基本是锁定平台的。比如你在n8n上搭建了一个很厉害的 Workflow，你是没法分享给平时在用扣子和Dify的朋友的。

但Skills可以。不论你是在Claude Code中创建的Skills还是在扣子中创建的Skills，它们都是标准的带SKILL.md文件和可选资源层的文件夹形态，遵循的也是Agent Skills的结构和渐进式披露原则，都可以快速安装到任何一个支持Skills的工具中使用。

用户可以在单个 Skill 里实现自动化流程，也可以用自然语言将多个 Skill 串联起来运行。

  **那什么时候用Workflow，什么时候用Skills呢？**

更适合Workflow的场景：
- **追求极致的稳定、可控、可追溯、可审计**，典型如金融、医疗、法律这类行业。

更合适Skills的场景：
- 输入条件多变、需要智能判断的任务；
- 工作流需要跨平台分享复用。


## 5.2 对比 MCP

MCP 和 Skills 两者很容易被混淆，甚至有激进的观点认为 Skills 可以取代 MCP。

> 注：这里说的 MCP 都是指 MCP Server。

两者之所以容易被混淆，是因为它们都是为了增强 Agent 能力而设计的协议或标准，并且Skills的概念出来后，部分 MCP 开始推出 Skills，典型如 Context7 MCP 推出了 Context7 Skills。乍一看以为是一回事，其实两者在在设计理念、实现方式、应用场景和功能焦点上存在显著差异。

还是先从概念出发。

**MCP**：即模型上下文协议，是为了标准化 AI 模型与外部系统（如数据源、工具）的连接方式而诞生的。它的核心是引入一个中间层接口，减少自定义集成的工作量。MCP 解决了传统 API 连接的“m × n”问题（m 个 AI 应用与 n 个外部工具需连接 m × n 次），转为只需 m + n 次连接。通过 MCP，AI 可以安全、双向地访问实时数据，而无需为每个模型或工具编写独特的代码。

![](assets/06%20Skills/file-20260322211102640.jpg)![](assets/06%20Skills/file-20260322211127586.jpg)

但 MCP 有个很严重的问题，就是非常占上下文空间。因为每个 MCP 连接到 AI 时，就会把所有 tools 的定义（名称、描述、参数、示例）一次性塞进上下文。一个 tool 的定义大概几百个 tokens，一个 MCP 通常有 10-20 个工具。当你连接的 MCP 数量一多，整个上下文空间就会被挤掉。

**Agent Skills** 的推出，采用渐进式披露的信息加载方式（具体可以看>>>[Agent Skills概念拆解](https://my.feishu.cn/wiki/S8Fjwvl5yiazqNkwWlQcvhKBnZb)），一定程度上解决了 MCP 非常占用上下文空间的问题。

但要注意，Skills 只是解决此前 MCP 很占上下文空间这个问题，而不是解决了 MCP 原本要解决的问题。因为两者一开始要解决的问题就不是一回事。

### 核心区别：解决的问题不同

MCP 解决的是Agent“数据访问”的痛点（如从外部源拉取信息），**它的核心是连接**；

Skills 解决 Agent“任务执行”的痛点（如教Agent新技能），**它的核心是提供流程知识（SOP）**。

如果你要让 Agent 连接外部数据，用 MCP；如果你要向 Agent 解释怎么处理这些数据，用Skills。


## 5.3 对比 SubAgent

SubAgent 和 Skills 就比较好区分了，它俩都可以用来处理特定工作流程。区别在于“**谁在做决策**”以及“**上下文如何管理**”。

### 区别一：谁在做决策

SubAgent，就是子Agent（是相对主Agent来说，主Agent下管理着多个子Agent），它有独立的上下文窗口、自定义系统提示和特定工具权限，是为了特定工作流程专门构建的。比如 Cursor 的 Plan Mode 和 Debug Mode 就是两个SubAgent，分别用来做任务规划和代码调试。

**SubAgent 相当于“大脑的分身”**，接收主Agent的目标后，负责局部决策。

而 Skills 是被动的脚本和指令， 相当于是“手”，负责任务执行；每个 SubAgent 在执行任务时，可以调用自己专属的 Skills 来完成具体操作（当然，Skills 也可以直接交给主Agent调用，区别会在下面具体介绍）。

### 区别二：上下文如何管理

如果把 Skills 加载到主Agent，那就是正常的按需分层加载。但这种方法通常会增加主对话的上下文负担，因为主Agent需要加载 Skills 的使用说明和 Skills 返回的所有上下文（注：在简单的任务中一般问题不大）。

但如果你是处理复杂任务，那么更建议采用 SubAgent + Skills 的组合方式。由于每个 SubAgent 都有独立的上下文窗口。这意味着它可以在后台用处理海量繁琐信息，而只给主Agent返回一个精简的结果，从而保护主对话的上下文空间不被撑爆。

  

总结来说：

如果你的任务是**线性的、步骤明确的**（例如：抓取网页 -> 翻译 -> 保存为 PDF），或者多个Agent需要相同的专业知识，或者你希望主Agent对每一个细节都有更好的掌控。**优先选择 Skills。**

如果你的任务是**探索性的、极其复杂的**（例如：深入研究一个技术主题、大规模代码重构），或者单次任务涉及的数据量超过了主模型的上下文限制。**优先选择 Sub-Agents。**


# 6 局限与应对

Skills确实强大，但也存在一些局限。如果不加以应对，这些问题反而可能会导致效率低下、安全风险或维护成本上升。

## 局限一：使用门槛高

看完前面的介绍，大家可能也感受到了，如果要正常使用Skills，还是有点门槛的。
- **第一道门槛**：工具门槛。除了扣子，其它能运行Skills的工具都是IDE或CLI，安装门槛高。有些还得解决网络问题。
- **第二道门槛**：配置环境门槛。即使你解决了工具门槛，也把Skills下载安装好了，但迎接你的可能是各种依赖和配置环境缺失带来的运行报错。比如你去用最近很火的Remotion Skills，大概率就会遇到这个问题。
- **第三道门槛**：管理和维护门槛。在Claude Code中，如果你不通过插件市场安装Skill的话，Skill本身是没法跟随仓库更新的，那么你使用的Skill就一直是老版本。其它IDE或CLI甚至没有插件市场这东西。当你安装了多个Skills，后续的管理和更新维护就会成为一个很大的问题。

应对策略
- 如果你的任务并不需要在本地处理，也不需要使用Claude、Gemini、GPT、Kimi、GLM这类更强大的模型（Skills的执行效果很依赖模型），那么可以在扣子中使用Skills；
- 如果你要在IDE或CLI工具中使用Skills，但又不太熟悉其中的操作细节（比如安装和配置环境等问题），基本可以向AI提问解决；
- 至于Skills更新这个问题，优先选择Claude Code插件市场这种安装方法（适合按需更新）。而其它第三方Skills自动更新工具，暂时不建议使用，因为这涉及接下来要介绍的局限二：安全漏洞。

## 局限二：安全漏洞

Skills 的开放性允许从各种来源获取和集成，但这也引入了潜在的安全风险。大家应该还记得Skills的结构，它的资源层通常包含脚本文件，这意味着如果在 Claude Code 中安装了恶意 Skills，它可能在本地引入漏洞、滥用权限（如通过网络请求窃取敏感信息），或执行非预期操作（如数据泄露或有害命令）。

应对策略：

**一、只用可信来源**

可信来源大致可以分为这么几类：
- 你自己/你的公司/团队内部写的 Skills
- Anthropic/Vercel/Obsidian等知名官方发布的 Skills
- 知名开发者在 GitHub 开源的。需要满足三个条件：
    - GitHub Stars > 500，说明多人在用；
    - 有其他开发者 Review 过（看 Issues 和 PR）
    - 作者有其他知名项目（不是新账号）

**二、审查代码**

下载 Skill 后，**不要直接使用**，先审查（也可以将下面的内容发给AI，让它帮你阅读）
1. 打开 SKILL.md 和脚本（如有）文件，逐行阅读
2. 搜索这些危险关键词：
```Plain
curl
wget
bash
sh
eval
exec
system
subprocess
silently
background
hidden
```
3. 检查是否访问敏感路径：
```Plain
~/.ssh
~/.aws
~/.config
/etc/passwd
/etc/shadow
.env
credentials
```
4. 检查网络请求：
    1. 所有 HTTP/HTTPS 请求的目标
    2. 是否有向未知域名发送数据
    3. 是否有 Base64 编码的数据（可能是混淆）
5. 检查依赖安装：
    1. 是否使用 `--global` 或 `-g`
    2. 版本号是否合理
    3. 是否从官方源安装

初次使用建议在沙盒环境中测试 Skill。也可以用一个叫做 Skill-Vetter 的 skills，它就是将以上的策略制作成了 Skill：

[https://clawhub.ai/spclaudehome/skill-vetter](https://clawhub.ai/spclaudehome/skill-vetter)

https://github.com/openclaw/skills/blob/main/skills/spclaudehome/skill-vetter/SKILL.md

**三、版本控制**

将 Skills 加入 Git 管理。这样你就知道什么时候添加了什么 Skill（方便追溯和对比），如果 Skill 出问题，也可以快速回滚快速恢复。

```Plain
# 进入 Claude Code 的 Skills 目录
cd ~/.claude/skills/  # 或者你的 Skills 目录

# 初始化 Git 仓库
git init

# 添加所有现有 Skills
git add .
git commit -m "Initial Skills snapshot"

# 以后每次添加新 Skill：
git add new-skill/
git commit -m "Add: new-skill for log analysis"
```


## 局限三：低观测性

不同于Workflow在过程中每一步都可以观测结果，大部分Skills在执行复杂任务时往往缺乏透明度，导致调试困难。

应对策略：在[Anthropic官方：Skills制作最佳实践](https://my.feishu.cn/wiki/T4HLwkCa2i5qIjkTWNLco7uDnkD)中有这么一个制作技巧：**创建可验证的中间输出**。



# 7 Claude Code Skills 原理

【抓包ClaudeCode窥探Skill的实现原理】 https://www.bilibili.com/video/BV1yRPWzqEhL/?share_source=copy_web&vd_source=8992a13080c32977bce93a5140823f3b

【抓包ClaudeCode窥探Skill的渐进式加载的过程】 https://www.bilibili.com/video/BV1cywWztEur/?share_source=copy_web&vd_source=8992a13080c32977bce93a5140823f3b

1、其本质就还是提示词工程，因为大模型本质就是 llm，所以工具都是以提示词的形式来披露执行的。这个就是 Skill Tools

![](assets/06%20Skills/file-20260322213428258.png)

这个 Skills 里面对应执行的具体内容

![](assets/06%20Skills/file-20260322213528172.png)
![](assets/06%20Skills/file-20260322213546581.png)



2、那么具体的执行路径是什么样的呢？这里的 messages 是通信的消息，tools 是对应可以去调用的工具，之前 Claude Code 发送的 tools 里面就包含了 Skills，现在是放到了 messages 中了

![](assets/06%20Skills/file-20260322214803690.png)

在第一轮还没对话的时候，就发送了一个请求 skills 被包含在了 messages 中

![](assets/06%20Skills/file-20260322214951540.png)

如果你发送了 “你好～”，其中回复的内容中 content 就是最终的内容，thinking 就是思考的内容，tool_calls 就是对应的工具调用，他想去调用 Agent 下面的 subagent 中的 greeting-responder agent

![](assets/06%20Skills/file-20260322215136791.png)

此时本机的 agent 执行，发现没有这个 greeting-responder agent，就会返回一个结果

![](assets/06%20Skills/file-20260322215338148.png)

这个就是 AI 对应 的思考和回复了

![](assets/06%20Skills/file-20260322215429445.png)


3、对话结束之后又发送了一次请求，用于预测用户下次可能会询问什么

![](assets/06%20Skills/file-20260322215526569.png)

AI 给出了预测的结果，用户可能只是打个招呼，没有最终的结果

![](assets/06%20Skills/file-20260322215618852.png)

这是 claude code 的一个预测的功能

![](assets/06%20Skills/file-20260322215704483.png)


4、如果你输入 “创建一个空的 word 文档”，下吗就是 AI 的回复，tool_calls 里面就包含了 Bash、Skill 的 tool_calls 的调用，并且针对 Skill 里面的 input.skill 有对应的 docx Skill 的调用

![](assets/06%20Skills/file-20260322215917662.png)

这个就是对应的 tool_calls 的具体调用，这里的 tool_use_id 就和之前的工具调用的 id 是一致的；其中最下面的 text 就最终的 docx skill 中的所有内容

![](assets/06%20Skills/file-20260322220133696.png)

调用完之后，这个就是后续的结果

![](assets/06%20Skills/file-20260322220411301.png)




https://github.com/yusifeng/formax

Claude Code 最早那版，Skill 是直接放在 Skill tool 的 desc 里的。那时候暴露出来的 Tool 也很多，比如 AskUserQuestion、Bash、Edit、EnterPlanMode、ExitPlanMode、Glob、Grep、KillShell、NotebookEdit、Read、Search、WebSearch、Write。 

后面有一次更新，cc 基本改成只保留一个 Tool，也就是 ToolSearch。也是从这个阶段开始，Skill 相关的提示词被放进了 system-reminder(以下简称sr)，格式大概是： 

<sr>The following skills are available for use with the Skill tool ${getSkillsText()}</sr> 

这么改（原因个人猜测），一方面是因为新版只剩一个 Tool 了，所以 Skill 这部分内容不能再像以前那样放在独立的 Skill desc 里，只能放到 sr 里。另一方面是因为之前 Skill 是放在 tools 里的，而 tools 本身是会变的，Anthropic 那边缓存命中又是先从 tools 开始算，所以只要 tools 一变，后面的缓存就容易一起失效。现在把 Skill 挪到 sr，至少可以减少 tools 这一层变化对缓存命中的影响。 

再补充一点，Claude Code 以前的 /commander 和 Skill 其实是分开的，但本质上做的是同一件事。所以在新版提示词里会有这种描述： 

/<skill-name>（比如 /commit）是用户调用用户可调用技能的简写，执行时会展开成完整提示，再通过 Skill 工具执行。 也就是说，到了新版里，/commander 和 Skill 实际上已经并到一起了，表面上看是 slash command，底层本质上还是 skill 那一套。

我还可以在分享一个 CladueCode 是如何去增加 memory 功能的，本质其实非常简单，就是在提示词中加入了这一句： You have a persistent auto memory directory at \`${autoMemoryDir}\`. Its contents persist across conversations. 然后还有一些注意事项相关的； 

然后在代码层面需要将这个目录去增加为一个白名单，因为 Claudecode 是有一个 preflight 机制（就是访问非pwd路径下的文件需要弹出一个是否允许），这个 memory 是跟工作目录相当定的，所以你可以自己去改 ~/.claude/projects/{一个以-开头的特定的文件夹名}/memory/MEMORY.md 这个文件内容，来调整需要记忆的内容




