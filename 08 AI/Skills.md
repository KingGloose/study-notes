# 1 介绍 

1、本质其实就是一个提示词加载工程技术的应用
- Agent Skills 是“可被 LLM 主动调用的能力模块”，包含名称、描述、输入/输出模式、执行器与权限边界。
- 它把“提示词工程 + 工具函数 + 数据检索/动作执行”工程化，使智能体具备可组合、可复用、可治理的业务能力。
- 社区主流生态包括：OpenAI 工具调用（Function/Tool Calls、Assistants）、LangChain Tools、LlamaIndex Tools、Autogen、CrewAI、Vercel AI Router 等。

2、典型工作流
- 用户意图 → LLM 规划 → 选择/路由技能 → 参数填充 → 执行 → 返回结果 → 继续/停止。
- 单体技能可直接返回结果；组合技能通过路由器或多轮调用完成复杂任务。

【Agent Skills到底是什么，一个动画彻底搞懂！】 https://www.bilibili.com/video/BV1EXksBGEa8/?share_source=copy_web&vd_source=8992a13080c32977bce93a5140823f3b

![](assets/Skills/file-20260118225102062.jpg)





