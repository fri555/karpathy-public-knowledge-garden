---
type: summary
created: 2026-06-02
updated: 2026-06-02
source_file: "[[../raw/20260507-BearBlog-AgentsNeedControlFlowNotMorePrompts|raw/20260507-BearBlog-AgentsNeedControlFlowNotMorePrompts]]"
source_url: https://bsuh.bearblog.dev/agents-need-control-flow/
source_author: bsuh
source_date: 2026-05-07
source_tier: 一手源-作者观点
tags: [agent, llm, harness, 工程实践, 控制流, 确定性, 已验证]
aliases: [Agents need control flow not more prompts]
---

# 20260507 · Bear Blog · Agents need control flow, not more prompts

> 一句话摘要：bsuh 提出一个很硬的 Agent 工程判断：复杂任务里的可靠性不能继续靠 `MANDATORY` / `DO NOT SKIP` 这类 prompt 咒语堆叠，而要把控制流、状态转移、验证检查点搬进确定性软件层；LLM 应该是组件，不是系统本身。

## 核心论点

1. **出现 MANDATORY / DO NOT SKIP 就说明 prompt 到顶了**：这些词本质是在用散文模拟程序控制流，但 LLM 会把它们当成概率性建议，而不是可执行语义。
2. **Prompt chain 缺少软件组合性**：代码可以靠函数、模块、库递归组合，并暴露可预测行为；prompt chain 弱规范、非确定、难验证，复杂度上来后可靠性会塌。
3. **可靠 Agent 需要确定性脚手架**：显式状态转移、validation checkpoint、runtime 控制流要写进软件，而不是藏在越来越长的 prompt 里。
4. **LLM 是组件，不是系统**：LLM 适合做不确定性判断/生成/翻译，但系统的边界、顺序、校验、失败处理应该由确定性 runtime 接管。
5. **没有程序化验证，只剩三条烂路**：babysitter（人工盯全程）、auditor（事后穷尽验证）、prayer（vibe 接受结果）。

## 关键事实 / 辅助语境

- 原文发布于 2026-05-07，Hacker News 讨论获 **590 points**(截至 2026-06-02)，说明该判断触发了开发者社区的广泛共鸣。
- HN 高赞评论直接补强核心观点："the breakthrough in ai coding was not that AI intelligence increased as much as that a lot of the core process execution moved out of the LLM prompt and into the harness."（来源: HN thread，见 raw 辅助摘录）
- 另一条实践评论把 Agent 降格为“自然语言 → 通过 input validator 的 commands/args”的翻译层：这正是“把运行时逻辑移出 LLM”的具体形态。

## 原文金句

> “If you’ve ever resorted to MANDATORY or DO NOT SKIP, you’ve hit the ceiling of prompting.”

> “Imagine a programming language where statements are suggestions and functions return ‘Success’ while hallucinating.”

> “Reliability requires moving logic out of prose and into runtime.”

> “We need deterministic scaffolds: explicit state transitions and validation checkpoints that treat the LLM as a component, not the system.”

## 抽取的实体

- [[../entities/Bear Blog|Bear Blog]] — 文章发布平台
- [[../entities/Hacker News|Hacker News]] — 辅助讨论源，提供工程社区语境
- [[../entities/bsuh|bsuh]] — 作者，提出“Agent 需要控制流而非更多 prompt”的观点

## 抽取的概念

- [[../concepts/确定性控制流|确定性控制流]] — 新建：用软件 runtime 承担状态转移、分支、循环、检查点
- [[../concepts/Prompt天花板|Prompt 天花板]] — 新建：当 prompt 开始堆 `MANDATORY` / `DO NOT SKIP` 时，说明问题已经越过语言指令可稳定约束的范围
- [[../concepts/Agent工程化兜底|Agent 工程化兜底]] — 更新：补充“逻辑出 prose，进 runtime”的表述
- [[../concepts/Hooks确定性执行|Hooks 确定性执行]] — 更新：bsuh 文章与 Shareuhack 的“建议 vs 法律”同源
- [[../concepts/Agentic Engineering|Agentic Engineering]] — 更新：补充控制流/验证检查点是专业工程师与 vibe coding 的关键分水岭

## 与已有知识的关系

- **强呼应**：[[../concepts/Hooks确定性执行|Hooks 确定性执行]] 说“建议变法律”，本文说“logic out of prose and into runtime”，两者是同一个判断的不同表达。
- **连接 OpenClacky**：[[20260514-RubyChina-OpenClacky-Harness工程7个关键决策]] 讲 cache、工具集、压缩；本文从控制流角度解释为什么 Harness 不只是省钱，而是可靠性的必要条件。
- **补足 Agentic Engineering**：[[../concepts/Agentic Engineering|Agentic Engineering]] 不只是“用 AI 写代码”，还要知道哪些部分必须留给确定性软件。
- **反向修正 prompt 崇拜**：[[../concepts/原则化指令|原则化指令]] 仍然有用，但它负责方向和偏好；凡是必须 100% 发生的步骤，不能只靠原则化 prompt。

## 我的批注 / 思考

- 这篇短，但密度很高。它把很多 Agent 失败的根因压成一句话：**你不能用建议级语言模拟法律级控制流**。
- 对知识库自身也有提醒：AGENT.md 的规则目前仍主要是 prompt/协议层，index/log 更新靠 Agent 自觉。若未来出错频率上升，应考虑用脚本或 pre-commit 检查“摘要页创建后 index/log 是否同步”。
- Surprise：这篇不是“反 Agent”，而是“把 Agent 放回软件系统里”。最成熟的 Agent 形态可能不是一个更长 prompt 的模型，而是一个确定性程序中嵌入若干 LLM 判断点。

## 待深入

- [ ] 专题对照：OpenClacky / Shareuhack / bsuh / Stripe Minions 的“确定性外壳 + LLM 内核”路线
- [ ] 研究 Salesforce AgentScript、LangGraph、BAML 在“控制流外置”上的差异
- [ ] 本知识库最小 hook：检查新增 summary 是否已进入 index，log 是否追加
