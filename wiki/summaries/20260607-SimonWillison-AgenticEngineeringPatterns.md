---
type: summary
created: 2026-06-07
updated: 2026-06-07
source_file: "[[../../raw/20260607-SimonWillison-AgenticEngineeringPatterns]]"
source_url: https://simonwillison.net/guides/agentic-engineering-patterns/
source_author: Simon Willison
source_date: 2026-02-23
source_tier: 一手源
tags: [ai, llm, agent, coding, agentic-engineering, 测试, 一手源, 方法论]
aliases: [Agentic Engineering Patterns]
---

# 20260607 · Simon Willison · Agentic Engineering Patterns

> 一句话摘要：Simon Willison 把 coding agent 实践整理成一套持续更新的工程模式：代码生成变便宜了，但好代码仍贵，核心瓶颈转向问题定义、上下文管理、测试验证与责任承担。

## 核心论点

1. **Agentic engineering = 用能写且能执行代码的 Agent 做软件工程**：Agent 的最小定义是“tools in a loop to achieve a goal”，coding agent 的关键差异是能执行代码并迭代验证。
2. **写代码便宜，不等于好代码便宜**：Agent 降低的是初始生成成本；能工作、可验证、简单、可维护、安全、可观测的好代码依旧需要工程判断。
3. **测试从“可选纪律”变成 Agent 工作流的默认入口**：`First run the tests` 与 `Use red/green TDD` 是短 prompt 背后的工程纪律，用测试把模型输出从“看起来对”拉回“可证明对”。
4. **理解 harness 才能理解 Agent 产品差异**：coding agent 本质是 LLM 外的一层 harness：system prompt、工具定义、状态重放、token cache、工具执行循环共同决定效果与成本。
5. **Subagents 的主要价值是隔离上下文，而不是模拟人类组织结构**：子 Agent 可用于探索、测试、审查和调试，核心收益是保留 root context、隔离 token-heavy 操作。

## 关键事实 / 数据

- Willison 将 LLM Agent 定义为：**Agents run tools in a loop to achieve a goal**（来源: [[20260607-SimonWillison-AgenticEngineeringPatterns]]）。
- coding agent 例子包括 [[../entities/Claude Code|Claude Code]]、[[../entities/Codex|OpenAI Codex]]、Gemini CLI（来源: [[20260607-SimonWillison-AgenticEngineeringPatterns]]）。
- LLM 是无状态的；多轮对话靠 harness 每轮重放历史维持，因此上下文越长，输入 token 成本越高（来源: [[20260607-SimonWillison-AgenticEngineeringPatterns]]）。
- Token caching 依赖稳定前缀；coding agents 会尽量避免修改早期 conversation content，以复用 cache（来源: [[20260607-SimonWillison-AgenticEngineeringPatterns]]）。
- Willison 把 `First run the tests` 视为四个词压缩出的工程纪律：让 Agent 发现测试入口、感知项目复杂度、进入测试心态（来源: [[20260607-SimonWillison-AgenticEngineeringPatterns]]）。

## 原文金句

> Agents run tools in a loop to achieve a goal.

> Code execution is the defining capability that makes agentic engineering possible.

> Delivering new code has dropped in price to almost free... but delivering good code remains significantly more expensive than that.

> Automated tests are no longer optional when working with coding agents.

## 抽取的实体

- [[../entities/Simon Willison|Simon Willison]]
- [[../entities/Claude Code|Claude Code]]
- [[../entities/Codex|Codex]]
- [[../entities/Gemini CLI|Gemini CLI]]
- [[../entities/Andrej Karpathy|Andrej Karpathy]]

## 抽取的概念

- [[../concepts/Agentic Engineering|Agentic Engineering]]
- [[../concepts/Vibe Coding|Vibe Coding]]
- [[../concepts/Agent工具循环|Agent 工具循环]]
- [[../concepts/Harness工程|Harness 工程]]
- [[../concepts/Prompt Cache局部性|Prompt Cache 局部性]]
- [[../concepts/Subagents上下文隔离|Subagents 上下文隔离]]
- [[../concepts/Red-Green TDD|Red-Green TDD]]
- [[../concepts/First Run The Tests|First Run The Tests]]
- [[../concepts/验证瓶颈|验证瓶颈]]

## 与已有知识的关系

- **补全**：为 [[../concepts/Agentic Engineering|Agentic Engineering]] 补上 Willison 的 2026 guide 版本定义：不仅是“专业工程师用 AI”，而是围绕 coding agent 能执行代码这一能力形成的工作模式。
- **印证**：与 [[../concepts/验证瓶颈|验证瓶颈]] 强呼应——生成成本下降后，真正稀缺的是确认代码“对且好”。
- **印证**：与 [[../entities/OpenClacky|OpenClacky]] 的 cache/工具稳定性实践互相补强：Willison 解释底层 mechanics，OpenClacky 展示产品工程取舍。
- **边界修正**：对 [[../concepts/Vibe Coding|Vibe Coding]] 的定义保持 Karpathy 原义：不看代码、不审查；不要把“用 AI 写代码”全部泛化成 vibe coding。
- **扩展**：为本库新增测试纪律分支：[[../concepts/Red-Green TDD|Red-Green TDD]] 与 [[../concepts/First Run The Tests|First Run The Tests]]。

## 我的批注 / 思考

- 这份资料的 surprise 在于：它不是新工具介绍，而是在给 Agent 时代重新校准“工程直觉”。以前“不值得花一天做”的事情，现在可以交给异步 agent 试十分钟；但以前“必须亲自负责正确性”的事情，一点都没有变便宜。
- `First run the tests` 很适合沉淀为个人 Agent SOP：每次接手代码库先让 Agent 发现验证方式，而不是先改代码。
- Subagents 与 OpenClacky 的“不要多 Agent 编排”并不矛盾：前者是上下文隔离工具，后者反对的是为了模仿人类分工而引入昂贵的多 Agent 工作流。

## 待深入

- [ ] 继续录入 Willison guide 中 `Agentic manual testing`、`Linear walkthroughs` 两章，补全“测试与理解代码”分支。
- [ ] 对比 Willison 的 Subagents 观点与 Anthropic 多 Agent research 的差异。
