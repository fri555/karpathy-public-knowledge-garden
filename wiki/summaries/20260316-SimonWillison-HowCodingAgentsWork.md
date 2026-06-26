---
type: summary
created: 2026-06-05
updated: 2026-06-05
source_file: "[[../raw/20260316-SimonWillison-HowCodingAgentsWork|raw/20260316-SimonWillison-HowCodingAgentsWork]]"
source_url: https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/
source_author: Simon Willison
source_date: 2026-03-16
source_tier: 一手源
tags: [ai, agent, llm, coding, simon-willison, 一手源, 已验证]
---

# 20260316 · Simon Willison · How coding agents work

> 一句话摘要：Simon Willison 把 coding agent 拆到最小机械结构：LLM + system prompt + tools + harness loop；理解这个朴素循环，才能判断哪些问题该靠模型，哪些该靠工具和 harness。

## 核心论点

1. **Agent 不是魔法，是 harness 包住 LLM**：coding agent 是一层软件，把隐藏 prompt、工具函数和循环控制加到 LLM 外面。
2. **工具调用是 Agent 的定义性特征**：工具只是 harness 暴露给模型的函数；模型请求调用，harness 解析、执行、把结果塞回上下文。
3. **LLM 无状态，长对话靠 harness 重放历史**：因此 token 成本、上下文长度、cache 命中率都是 Agent 工程问题。
4. **简单 tool loop 很短，好的 tool loop 很难**：几十行代码能跑通原理，但真正可靠的 Agent 需要系统 prompt、工具设计、错误处理、验证和上下文管理。

## 关键事实 / 数据

- Simon Willison 明确定义：coding agent 是 “a harness for an LLM”。(来源: [[../raw/20260316-SimonWillison-HowCodingAgentsWork]])
- LLM 每次调用都是无状态的，聊天体验由调用方软件保存并重放历史实现。(同上)
- 许多 coding agent 通过不修改早期 conversation content 来提高 token cache 效率。(同上)
- OpenAI Codex 2026 年 3 月的 system prompt 可作为 coding agent 指令设计案例。(同上)

## 原文金句

> “A coding agent is a piece of software that acts as a harness for an LLM.”

> “A tool is a function that the agent harness makes available to the LLM.”

> “LLMs are stateless.”

> “A simple tool loop can be achieved with a few dozen lines of code... A good tool loop is a great deal more work.”

## 抽取的实体

- [[../entities/Simon Willison|Simon Willison]]
- [[../entities/Codex|Codex]]

## 抽取的概念

- [[../concepts/Tool Loop|Tool Loop]]
- [[../concepts/Harness工程|Harness 工程]]
- [[../concepts/Prompt Cache局部性|Prompt Cache 局部性]]
- [[../concepts/Agentic Engineering|Agentic Engineering]]

## 与已有知识的关系

- **底层补丁**：给 [[../concepts/Harness工程|Harness 工程]] 一个最小定义——不是抽象大词，而是“模型外负责提示、工具、状态、循环的软件层”。
- **印证**：[[../concepts/Prompt Cache局部性|Prompt Cache 局部性]] 的必要性来自 LLM 无状态 + 每轮重放上下文的成本结构。
- **连接**：与 [[../concepts/Agentic Engineering|Agentic Engineering]] 同属 Simon Willison 的方法论体系，前者讲价值观，本文讲机械结构。

## 我的批注 / 思考

- 这篇很基础，但适合做“概念地基”。很多人把 Agent 想玄了，Simon 的价值是把它还原成软件工程对象。
- Surprise：越是强模型时代，越需要理解这种朴素机械结构；否则所有问题都会被误诊成“模型不够聪明”。

## 待深入

- [ ] 补读同系列 Subagents、Using Git with coding agents、Red/green TDD 等章节。
