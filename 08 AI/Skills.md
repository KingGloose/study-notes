【Agent Skills到底是什么，一个动画彻底搞懂！】 https://www.bilibili.com/video/BV1EXksBGEa8/?share_source=copy_web&vd_source=8992a13080c32977bce93a5140823f3b

这个本质其实就是一个提示词加载工程技术的应用

![](assets/Skills/file-20260118225102062.jpg)

## AI Agent Skills 介绍与实战教程（2026 实用指南）

### 概览
- Agent Skills 是“可被 LLM 主动调用的能力模块”，包含名称、描述、输入/输出模式、执行器与权限边界。
- 它把“提示词工程 + 工具函数 + 数据检索/动作执行”工程化，使智能体具备可组合、可复用、可治理的业务能力。
- 社区主流生态包括：OpenAI 工具调用（Function/Tool Calls、Assistants）、LangChain Tools、LlamaIndex Tools、Autogen、CrewAI、Vercel AI Router 等。

### 为什么需要 Skills
- 降低耦合：把复杂任务拆分为独立能力模块，便于复用与测试。
- 可靠执行：通过结构化参数与权限控制，减少幻觉、越权和副作用风险。
- 可观测与迭代：对每个技能建立指标、日志与版本，持续优化。

### 核心概念
- 输入/输出 Schema：使用 JSON Schema/Pydantic 定义参数与返回结构，利于验证与约束。
- 工具/动作执行：LLM 通过 tool/function 调用选择合适技能并传入参数；技能在受控环境内执行。
- 上下文与检索（RAG）：技能可内置检索步骤，把外部知识注入对话上下文。
- 安全与权限：最小权限、域名白名单、资源限额（时长/并发/成本）。
- 版本与可观测性：以语义化版本管理技能，收集调用成功率、时延、成本等指标。

### 典型工作流
- 用户意图 → LLM 规划 → 选择/路由技能 → 参数填充 → 执行 → 返回结果 → 继续/停止。
- 单体技能可直接返回结果；组合技能通过路由器或多轮调用完成复杂任务。

---

## 快速上手：从一个可用技能开始

### 选型与生态（择一即可）
- OpenAI 工具调用（Function/Tool Calls）：最通用，直接由模型触发工具。
- OpenAI Assistants：内置文件/检索等能力，适合多资源场景。
- LangChain Tools：Python/JS 生态成熟，StructuredTool/Pydantic 定义很方便。
- LlamaIndex Tools：与文档/索引深度集成，适于知识库场景。
- Autogen/CrewAI：多智能体编排，适合复杂协作任务。

### 我们要做的示例技能
- 名称：web_summarize_with_citation
- 能力：抓取网页并生成中文要点摘要，返回参考链接列表。
- 输入：`url`（必填）、`question`（选填）、`max_tokens`（选填）
- 输出：`{ summary: string, citations: string[] }`

### Python（LangChain）实现示例

```python
from typing import Optional, List
from pydantic import BaseModel, Field
import requests
from bs4 import BeautifulSoup
from langchain.tools import StructuredTool
from langchain_openai import ChatOpenAI

class SummarizeInput(BaseModel):
    url: str = Field(..., description="要摘要的网页 URL")
    question: Optional[str] = Field(None, description="关注的问题或主题")
    max_tokens: int = Field(512, ge=128, le=4096, description="摘要最大 token")

def fetch_page(url: str) -> tuple[str, List[str]]:
    resp = requests.get(url, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    text = " ".join([p.get_text(" ", strip=True) for p in soup.find_all(["p","li"])])
    links = [a.get("href") for a in soup.find_all("a") if a.get("href")]
    return text[:100_000], links[:50]

def summarize_with_citation(url: str, question: Optional[str], max_tokens: int) -> dict:
    content, links = fetch_page(url)
    llm = ChatOpenAI(model="gpt-4o-mini")
    prompt = f"请用要点式中文总结以下网页内容，保留关键数字与结论。关注：{question or '总体'}。\n\n正文：{content[:4000]}"
    res = llm.invoke(prompt)
    return {"summary": res.content, "citations": links}

summarize_tool = StructuredTool.from_function(
    name="web_summarize_with_citation",
    description="抓取网页并生成中文要点摘要，返回引用链接",
    func=summarize_with_citation,
    args_schema=SummarizeInput,
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
from langchain.agents import AgentExecutor, create_tool_calling_agent
tools = [summarize_tool]
prompt = "阅读 https://example.com 的内容，提取关键结论并列出出处。"
agent = create_tool_calling_agent(llm, tools)
executor = AgentExecutor(agent=agent, tools=tools)
print(executor.invoke({"input": prompt}))
```

### Node.js（OpenAI Function/Tool Calls）实现示例

```javascript
import OpenAI from "openai";
import fetch from "node-fetch";
import cheerio from "cheerio";

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const tools = [
  {
    type: "function",
    function: {
      name: "web_summarize_with_citation",
      description: "抓取网页并生成中文要点摘要，返回引用链接",
      parameters: {
        type: "object",
        properties: {
          url: { type: "string", description: "网页 URL" },
          question: { type: "string", description: "关注的问题", nullable: true },
          max_tokens: { type: "integer", description: "摘要长度", default: 512 }
        },
        required: ["url"]
      }
    }
  }
];

async function web_summarize_with_citation({ url, question, max_tokens }) {
  const resp = await fetch(url, { timeout: 20000 });
  const html = await resp.text();
  const $ = cheerio.load(html);
  const text = $("p,li").toArray().map(el => $(el).text().trim()).join(" ");
  const links = $("a").toArray().map(el => $(el).attr("href")).filter(Boolean).slice(0, 50);
  const sys = "你是中文研究助理，请用要点式总结输入文本，保留关键数字与结论。";
  const res = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      { role: "system", content: sys },
      { role: "user", content: `关注：${question || "总体"}。正文：${text.slice(0, 8000)}` }
    ],
    max_tokens
  });
  return { summary: res.choices[0].message.content, citations: links };
}

const toolImpl = { web_summarize_with_citation };

async function run() {
  const messages = [{ role: "user", content: "阅读 https://example.com 并总结，列出处" }];
  while (true) {
    const response = await client.chat.completions.create({ model: "gpt-4o-mini", messages, tools });
    const msg = response.choices[0].message;
    if (msg.tool_calls?.length) {
      for (const call of msg.tool_calls) {
        const name = call.function.name;
        const args = JSON.parse(call.function.arguments || "{}");
        const result = await toolImpl[name](args);
        messages.push({ role: "tool", tool_call_id: call.id, content: JSON.stringify(result) });
      }
      continue;
    } else {
      console.log(msg.content);
      break;
    }
  }
}

run().catch(console.error);
```

### 本地测试建议
- 使用固定 URL 与期望关键词进行对比，确保摘要包含关键数字与结论。
- 记录时延、调用成本与失败率，快速定位网络超时、解析异常等问题。
- 对异常场景（无正文、需要登录、重定向频繁）设置防护与降级策略。

---

## 进阶用法与工程实践

### 与检索（RAG）结合
- 在技能内部调用向量库/索引，先检索相关段落，再让 LLM 摘要或回答，减少幻觉。
- 返回时包含 `citations`（来源 URL/段落 ID），提升可追溯性。

### 技能路由与多步计划
- 构建“技能选择器”，按意图/上下文/信心分数路由不同技能。
- 使用多轮计划（Plan-and-Execute/ReAct）把复杂任务拆解为多个技能调用。

### 记忆与状态管理
- 把会话中的“实体/约束/偏好”写入短期/长期记忆，作为技能参数或上下文注入。
- 定义清晰的持久化策略（例如数据库/文件/向量库），避免隐形耦合。

### 并发与长任务
- 对长任务（爬取/生成/分析）采用异步队列与进度回调；设置超时与重试策略。
- 对并发技能调用使用限流与隔离，避免资源争用。

### 安全与治理
- 最小权限原则：只开放必要的网络/文件/系统操作；敏感操作必须二次确认。
- 参数验证：严格的 Schema 校验，拒绝异常输入（例如超长、非法 URL）。
- 输出约束：要求结构化 JSON 与明确字段，减少 LLM 漫游式输出。
- 审计与可观测：记录调用链、参数、结果摘要与代价，支持回溯与优化。

### 部署与版本管理
- 以微服务形式部署技能（HTTP/GRPC），对外暴露稳定接口与版本号。
- 使用语义化版本（MAJOR.MINOR.PATCH），维护变更日志与兼容性说明。
- 采集指标（成功率、P95 延迟、成本/token），建立告警与容量规划。

### 常见坑与最佳实践
- 技能描述过于模糊 → LLM 选择失败：提高描述的明确性与边界。
- 参数映射错误 → 执行异常：统一输入 Schema，加入校验与错误提示。
- 文本截断 → 信息丢失：在抓取环节做清洗与抽取，分段摘要并合并。
- 幻觉与过度总结：引入检索证据与引用；设置事实核验与反问策略。
- 不可重复执行：保证技能幂等性，避免副作用（写文件/发请求）重复发生。

---

## 小结与下一步
- 你已经理解了 Agent Skills 的工程化方法，并完成一个“网页摘要+引用”的示例技能设计与实现。
- 可依次扩展更多技能（数据查询、文件操作、可视化、自动化流程），并通过路由/计划实现复杂任务。
