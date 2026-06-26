---
type: summary
created: 2026-06-01
updated: 2026-06-01
source_file: "[[../raw/20260929-Anthropic-Effective context engineering for AI agents]]"
source_url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
source_author: Anthropic Engineering Team
source_date: 2026-05-29
source_tier: 一手源
tags: [agent, llm, context-engineering, prompt, anthropic, 方法论, 一手源, 已验证]
---

# 20260929 · Anthropic · Effective context engineering for AI agents

> 一句话摘要：Anthropic 官方系统阐述 [[../concepts/上下文工程|上下文工程]] 范式——从 [[../concepts/原则化指令|prompt engineering]] 进化到对 Agent 运行时全生命周期 context 的[[../concepts/注意力预算|注意力预算]]管理，核心原则是"找到最小高信号 token 集合最大化期望输出"。

## 核心论点

1. **Context engineering 是 prompt engineering 的自然进化**：prompt engineering 关注"怎么写指令"，context engineering 关注"在每一轮推理时，curate 什么信息进入有限的 context window"——包含 system prompt、tools、MCP、外部数据、消息历史等所有 token 来源。
2. **LLM 有有限的注意力预算**：基于 transformer 的 n² 注意力机制，context 越长注意力越分散；needle-in-a-haystack 研究揭示 [[../concepts/上下文腐烂|上下文腐烂]] 现象——token 越多，准确召回率越低。Context 必须被视为**有限且边际收益递减**的资源。
3. **System prompt 的"正确海拔"**：既不能硬编码脆弱的 if-else 逻辑（脆性高），也不能给过于笼统的指导（缺信号）。最佳位置是"足够具体以引导行为，又足够灵活以提供启发式"。
4. **工具设计的两个关键**：(a) 工具应返回 token 高效的信息、鼓励高效 Agent 行为；(b) 避免工具集膨胀——人类工程师无法明确判断用哪个工具时，Agent 也无法做到。
5. **Just-in-time 检索优于预计算 RAG**：Agent 维护轻量标识符（文件路径、查询、链接），运行时按需动态加载数据。[[../entities/Claude Code|Claude Code]] 就是此模式的典范：glob/grep 导航 + CLAUDE.md 前置 = 混合策略。
6. **长时域任务的三大技术**：[[../concepts/上下文膨胀与压缩|Compaction]]（压缩/摘要重启）、Structured note-taking（Agent 持久化笔记）、Sub-agent architectures（子 Agent 隔离 context）。

## 关键事实 / 数据

- Karpathy 在 X 上将 context engineering 称为"art and science"（来源: 原文引用 @karpathy 推文）
- Context rot 研究来自 Chroma Research 的 needle-in-a-haystack benchmarking（来源: 原文引用 research.trychroma.com）
- 人类工作记忆容量有限——LLM 的注意力稀缺是人类认知约束的架构镜像（来源: 原文引用 SAGE journals）
- Claude Code 的 hybrid 模型：CLAUDE.md 前置 + glob/grep just-in-time 导航（来源: 原文自述）
- Compaction 的技术要点：先最大化 recall（确保不丢关键信息），再迭代提高 precision（削减冗余）（来源: 原文）
- Sub-agent 返回蒸馏摘要通常 1,000–2,000 tokens，但探索可能消耗 tens of thousands（来源: 原文）

## 原文金句

> "Context engineering is the art and science of curating what will go into the limited context window from that constantly evolving universe of possible information."

> "Good context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome."

> "If a human engineer can't definitively say which tool should be used in a given situation, an AI agent can't be expected to do better."

> "This approach mirrors human cognition: we generally don't memorize entire corpuses of information, but rather introduce external organization and indexing systems."

> "Do the simplest thing that works will likely remain our best advice for teams building agents on top of Claude."

## 抽取的实体

- [[../entities/Anthropic|Anthropic]] — 更新：官方发布 Context Engineering 方法论
- [[../entities/Claude Code|Claude Code]] — 更新：hybrid context 策略（CLAUDE.md 前置 + just-in-time）

## 抽取的概念

- [[../concepts/上下文工程|上下文工程]] — 新建：prompt engineering 的自然进化，全生命周期 context 管理
- [[../concepts/注意力预算|注意力预算]] — 新建：有限且递减的 context 效用
- [[../concepts/上下文腐烂|上下文腐烂]] — 新建：context 增长导致召回率下降
- [[../concepts/Just-in-Time检索|Just-in-Time 检索]] — 新建：运行时按需动态加载
- [[../concepts/渐进式披露|渐进式披露]] — 新建：Agent 逐层发现相关 context
- [[../concepts/上下文膨胀与压缩|上下文膨胀与压缩]] — 更新：补充官方 Compaction 定义和技术要点
- [[../concepts/原则化指令|原则化指令]] — 更新：补充"正确海拔"概念
- [[../concepts/RAG|RAG]] — 更新：补充 vs Just-in-Time 检索的对比

## 与已有知识的关系

- **强印证**：[[../concepts/上下文膨胀与压缩|上下文膨胀与压缩]] 的 Saboo 两周压缩实践，是本文 Compaction 的非官方版本
- **强印证**：[[../entities/OpenClacky|OpenClacky]] 的 Insert-then-Compress = Compaction 的工程实现
- **延伸**：[[../concepts/Agent工程化兜底|Agent 工程化兜底]] 的"确定性手段弥补概率性"，本文的 context curation 是同一哲学的另一个维度
- **修正**：[[../concepts/RAG|RAG]] 概念页增加"预计算 vs Just-in-Time"视角
- **呼应**：[[../concepts/Skills 2.0模块化|Skills 2.0 模块化]] 的 on-demand 载入 = Just-in-Time 检索的 Skills 层实现
- **呼应**：[[../concepts/Prompt Cache局部性|Prompt Cache 局部性]] 的"前缀稳定"是本文"system prompt 冻结"的工程实现——Anthropic 说原理，OpenClacky 说做法

## 我的批注 / 思考

- 这篇是 2026 年 Agent 工程领域最权威的一手源之一。Anthropic 从 transformer 架构出发推导 context rot → 注意力预算 → 最小高信号集，逻辑链完整。
- Karpathy 引用 context engineering 定义是"art and science"——又一次 [[../entities/Andrej Karpathy|Karpathy]] 与 Anthropic 的理念共振。
- "Do the simplest thing that works" 与 [[../concepts/Simplicity First|Simplicity First]] 完全同源——Anthropic 和 CLAUDE.md 在方法论上高度一致。
- Surprise：Anthropic 官方推荐 hybrid 策略（CLAUDE.md 前置 + just-in-time 导航），而不是纯 just-in-time——这对本知识库的 AGENT.md 设计有直接参考价值。
- Sub-agent 返回 1-2K tokens 的蒸馏摘要 vs [[../entities/OpenClacky|OpenClacky]] 的 invoke_skill 返回一对"调用→结果"消息——两种 Sub-agent 隔离方案可以对照。

## 待深入

- [ ] 追溯 Karpathy 引用的原文推文（X ID 需确认）
- [ ] 对比 Anthropic Compaction vs OpenClacky Insert-then-Compress 的技术差异
- [ ] 研究 Claude Code 的 auto-compact 具体实现（95% 触发阈值）
