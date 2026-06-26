---
type: summary
created: 2026-06-25
updated: 2026-06-25
sources:
  - "[[20260625-Codex-从0搭建AI-Agent工作台规划]]"
source_tier: 一手源
tags: [ai, agent, 架构, 方法论, 自产, 待深入]
aliases: [小龙虾工作台规划, AI Agent 工作台规划]
---

# 20260625-Codex-从0搭建AI-Agent工作台规划

> 一句话摘要：这是一份面向“小龙虾工作台”的自产规划资料，把类似 WorkBuddy 的 AI 原生办公工作台拆成产品模块、技术栈、Agent 编排、工具系统、文件/知识库、数据库、安全、部署和学习路线；经先生纠偏后，本资料应作为“系统学习功能完备 AI Agent 工作台”的起点，而不是只做一个 MVP AI Agent。

## 信源识别

- **来源类型**：自产规划资料，由 Codex 在本地生成。
- **source_tier**：一手源。
- **注意**：文中提到 WorkBuddy/CodeBuddy 等外部产品，但本次没有把它们当作事实主源 ingest；后续若要研究竞品，应单独抓官方材料或一手演示资料。

## 核心论点

1. **AI Agent 工作台不是聊天机器人**：它的核心闭环是“自然语言目标 -> 计划 -> 工具调用 -> 结果沉淀 -> 上下文延续”，与单轮问答不同。
2. **MVP 只是学习入口，不是最终目标**：第一版可以从会话、文件、工具调用、任务记录做起，但真正好用的工作台必须补齐权限、可观测性、记忆、任务队列、RAG、集成、验证和成本控制。
3. **系统边界比模型选择更重要**：模型只是能力层之一，生产系统还需要前端工作台、后端 API、Agent 编排、工具注册、文件处理、数据库、对象存储、队列和部署运维。
4. **Agent 工程化要把不确定性关进确定性框架**：工具白名单、Schema 校验、敏感操作确认、日志审计、速率限制和失败重试，是从 demo 到可用产品的关键。
5. **学习路线应按闭环推进**：Web 基础 -> Next.js -> 数据库 -> AI API -> 文件处理 -> Agent/任务系统 -> RAG -> 办公工具集成。

## 关键事实 / 结构

### 产品能力

- 工作台首页：最近工作、快捷入口、任务状态。
- 会话页：用户与 AI 共同完成任务。
- 文件页：上传、解析、摘要、引用文件。
- 任务页：查看执行步骤、状态、错误、结果。
- 设置页：模型、API Key、工具权限。

### 工程能力

- 前端：React / Next.js / TypeScript / Tailwind CSS / shadcn/ui。
- 后端：Next.js Route Handler 或 Node.js 服务。
- 数据：PostgreSQL / Prisma / Redis / 对象存储 / pgvector。
- AI：LLM API、Streaming、Tool Calling、Agent Loop、RAG。
- 生产化：任务队列、权限、日志、审计、成本统计、限流。

### 数据模型

建议的核心表：

- users
- workspaces
- conversations
- messages
- tasks
- files
- tool_calls

其中 `tool_calls` 是 Agent 可追踪性的关键：没有工具调用记录，就无法回答“AI 刚才做了什么”。

## 提取出的实体

- [[../entities/CodeBuddy|CodeBuddy]]
- [[../entities/MCP|MCP]]
- [[../entities/Obsidian|Obsidian]]
- [[../entities/Codex|Codex]]

## 提取出的概念

- [[../concepts/AI Agent 工作台|AI Agent 工作台]]
- [[../concepts/Agent 工作台能力分层|Agent 工作台能力分层]]
- [[../concepts/Agent 工作台产品化|Agent 工作台产品化]]
- [[../concepts/Agentic Engineering|Agentic Engineering]]
- [[../concepts/RAG|RAG]]
- [[../concepts/上下文工程|上下文工程]]
- [[../concepts/Agent工程化兜底|Agent工程化兜底]]
- [[../concepts/验证瓶颈|验证瓶颈]]

## 与既有知识库的连接

- 与 [[../concepts/Agentic Engineering|Agentic Engineering]]：本资料把“专业工程师用 AI 提升交付质量”的思想从 coding 场景扩展到完整产品工作台搭建。
- 与 [[../concepts/上下文工程|上下文工程]]：工作台的长期会话、文件引用、任务状态、工具结果，本质上都是 context lifecycle 管理问题。
- 与 [[../concepts/RAG|RAG]]：RAG 是知识库问答能力的一部分，但不等于整个工作台；完整工作台还需要任务、工具、权限和产物。
- 与 [[../concepts/Agent工程化兜底|Agent工程化兜底]]：工具调用、敏感动作确认和日志审计是本资料里的重要产品化约束。
- 与 [[../concepts/验证瓶颈|验证瓶颈]]：功能越完整，生成越容易，验证越稀缺；因此需要任务状态、工具日志、测试和人工审批。

## 需要修正的理解

先生明确指出：当前目标不是“只要一个 MVP AI Agent”，而是“系统学习如何搭建一个功能完备、好用的 AI Agent 工作台”。因此：

- MVP 只能作为第一阶段训练场。
- 后续学习应围绕完整工作台能力图谱，而不是只围绕聊天和一个工具调用。
- 需要补充竞品研究、官方一手源、工程架构、UX、权限安全和生产化运营。

## 待深入

- [ ] 正式 ingest OpenAI Agents SDK 官方文档。
- [ ] 正式 ingest LangGraph 官方文档。
- [ ] 正式 ingest Vercel AI SDK 官方文档。
- [ ] 正式 ingest MCP 官方文档和安全实践。
- [ ] 单独研究 WorkBuddy / CodeBuddy / OpenClaw / OpenClacky 等产品形态差异。
