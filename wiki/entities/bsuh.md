---
type: entity
created: 2026-06-02
updated: 2026-06-02
sources:
  - "[[../summaries/20260507-BearBlog-AgentsNeedControlFlowNotMorePrompts]]"
tags: [人物, agent, llm, 工程实践, 一手源, 已验证]
aliases: [bsuh]
---

# bsuh

> 一句话定义：bsuh 是 Bear Blog 作者，在 2026-05-07 的短文 [[../summaries/20260507-BearBlog-AgentsNeedControlFlowNotMorePrompts|agents need control flow, not more prompts]] 中提出“可靠 Agent 需要确定性控制流，而不是更多 prompt”的工程观点。

## 基本信息

- **身份**：Bear Blog 作者 / Hacker News 讨论帖作者
- **代表观点**：复杂 Agent 系统要把控制流、状态转移、验证检查点写进 runtime，而不是继续堆 `MANDATORY` / `DO NOT SKIP` 之类 prompt 强调词 (来源: [[../summaries/20260507-BearBlog-AgentsNeedControlFlowNotMorePrompts]])
- **相关平台**：[[Bear Blog]] · [[Hacker News]]

## 在本知识库中的角色

bsuh 为本库的 Agent 工程线补上了一个简洁但关键的判断：

**凡是必须发生的步骤，都不应该只存在于 prompt 里。**

这与 [[../concepts/Hooks确定性执行|Hooks 确定性执行]]、[[../concepts/Agent工程化兜底|Agent 工程化兜底]]、[[../concepts/确定性控制流|确定性控制流]] 形成同一条脉络。

## 关键贡献

- 将“prompt 越写越长”的失败模式命名为 [[../concepts/Prompt天花板|Prompt 天花板]] (来源: [[../summaries/20260507-BearBlog-AgentsNeedControlFlowNotMorePrompts]])
- 明确提出“logic out of prose and into runtime” (来源: [[../summaries/20260507-BearBlog-AgentsNeedControlFlowNotMorePrompts]])
- 将 LLM 定位为系统组件，而不是系统本身 (来源: [[../summaries/20260507-BearBlog-AgentsNeedControlFlowNotMorePrompts]])

## 相关资料

- [[../summaries/20260507-BearBlog-AgentsNeedControlFlowNotMorePrompts]]
- [[../concepts/确定性控制流]]
- [[../concepts/Prompt天花板]]
