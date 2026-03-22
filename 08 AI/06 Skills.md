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

安装的方式就很多了，其本质就是将 skills 放入对应 ide 的路径下面，或者可以去平台看一下：https://skillsmp.com/zh/search


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

# 4 Skills 推荐

https://my.feishu.cn/wiki/KCEfwUxHFihEXIk76k0cFimNnng


# 5 制作 Skills




