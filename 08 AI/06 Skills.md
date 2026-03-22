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

