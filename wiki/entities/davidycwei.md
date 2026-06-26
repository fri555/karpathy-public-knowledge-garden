---
type: entity
created: 2026-06-03
updated: 2026-06-03
sources:
  - "[[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]]"
tags: [人物, agent, llm, 工程实践, 方法论, 已验证]
aliases: [davidYichengWei, 鹅厂架构师 davidycwei]
---

# davidycwei

> 一句话定义：知乎文章《从第一性原理思考 Agentic Engineering》的作者，鹅厂架构师，提出基于 Skill 的模块化 [[../concepts/Agentic Engineering|Agentic Engineering]] 框架。

## 基本信息

- **身份**：鹅厂架构师（来源: [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]])
- **代表内容**：《从第一性原理思考 Agentic Engineering》
- **关联项目**：[[agentic-engineering-framework]]
- **关联概念**：[[../concepts/Agentic Engineering|Agentic Engineering]] · [[../concepts/Spec-First工作流|Spec-First 工作流]] · [[../concepts/Error-Driven Context Refinement|Error-Driven Context Refinement]]

## 关键贡献

- 将 [[../concepts/Agentic Engineering|Agentic Engineering]] 放回软件工程语境，强调 Engineering 的本质是“约束优化”而非单纯提速 (来源: [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]])
- 提出 AI 时代核心矛盾：生成成本下降，但 [[../concepts/验证瓶颈|验证瓶颈]] 没有同步下降 (来源: [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]])
- 将工程知识组织为可组合的 Agent Skills：Workflow / Best Practices / Standards / Troubleshooting / Self-Refinement (来源: [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]])
- 提供 TDSQL HBase conditional mutation 的真实项目案例，展示 Agent 参与需求澄清、方案设计、测试生成、代码编写四阶段 (来源: [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]])

## 与本库的关系

本库已有 [[../concepts/LLM Wiki|LLM Wiki]]、[[../concepts/Harness工程|Harness 工程]]、[[../concepts/Agent工程化兜底|Agent 工程化兜底]] 等概念。davidycwei 的贡献是把这些原则迁移到完整 SDLC：从“让 Agent 能工作”推进到“让 Agent 在生产级工程约束下可靠工作”。

## 相关资料

- [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]]
- [[agentic-engineering-framework]]

## 待深入

- [ ] 溯源 GitHub 账号和仓库 README，确认框架文件结构与最新状态。
