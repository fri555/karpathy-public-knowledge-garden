---
type: entity
created: 2026-06-07
updated: 2026-06-07
sources:
  - "[[../summaries/20260607-SimonWillison-AgenticEngineeringPatterns]]"
tags: [人物, ai, llm, agent, coding, 一手源]
aliases: [simonw]
---

# Simon Willison

> 一句话定义：Simon Willison 是长期记录 LLM 与软件工程实践的技术作者/开发者，在本库中主要贡献 [[../concepts/Agentic Engineering|Agentic Engineering]]、[[../concepts/Vibe Coding|Vibe Coding]] 边界、coding agent 工作模式与 context engineering 术语传播。

## 基本信息

- **类型**：人物 / 技术作者 / 开源开发者
- **个人网站**：simonwillison.net
- **关联实体**：[[Claude Code]] · [[Codex]] · [[Gemini CLI]] · [[Hacker News]]
- **关联概念**：[[../concepts/Agentic Engineering|Agentic Engineering]] · [[../concepts/Agent工具循环|Agent 工具循环]] · [[../concepts/Harness工程|Harness 工程]] · [[../concepts/Red-Green TDD|Red-Green TDD]]

## 关键事实

- Willison 将 Agent 在 LLM 语境下定义为“tools in a loop to achieve a goal”，并强调 coding agent 的关键能力是写代码并执行代码 (来源: [[../summaries/20260607-SimonWillison-AgenticEngineeringPatterns]])。
- 他将 [[../concepts/Agentic Engineering|Agentic Engineering]] 定义为使用 coding agents 开发软件的实践，强调人类仍负责问题定义、权衡、验证与责任承担 (来源: [[../summaries/20260607-SimonWillison-AgenticEngineeringPatterns]])。
- 其 `Agentic Engineering Patterns` guide 是持续更新的 evergreen guide，而非一次性博文，章节包括测试、Subagents、理解代码、annotated prompts 等 (来源: [[../summaries/20260607-SimonWillison-AgenticEngineeringPatterns]])。
- 他明确区分 [[../concepts/Vibe Coding|Vibe Coding]] 与 Agentic Engineering：前者按 Karpathy 原义是“不看代码”的原型式生成，后者要求把结果提升到生产级标准 (来源: [[../summaries/20260607-SimonWillison-AgenticEngineeringPatterns]])。

## 在本知识库中的角色

Simon Willison 在本库中承担“实践命名者”的角色：他把分散的 coding agent 经验命名为可讨论、可复用的 patterns。与 [[Andrej Karpathy]] 偏理念/范式、[[Anthropic]] 偏产品/研究不同，Willison 的价值在于把日常工程动作压缩成短句 SOP，例如 `First run the tests`、`Use red/green TDD`。

## 相关资料

- [[../summaries/20260506-SimonWillison-Vibe coding and agentic engineering]]
- [[../summaries/20260316-SimonWillison-HowCodingAgentsWork]]
- [[../summaries/20260607-SimonWillison-AgenticEngineeringPatterns]]

## 待深入

- [ ] 继续跟踪 Agentic Engineering Patterns 后续新增章节。
- [ ] 梳理 Willison 与 Karpathy 在 vibe coding 定义上的差异与演变。
