---
type: concept
created: 2026-06-01
updated: 2026-06-25
sources:
  - "[[../summaries/20260506-SimonWillison-Vibe coding and agentic engineering]]"
  - "[[../summaries/20260622-SimonWillison-Porting-Moebius-model-to-browser]]"
tags: [方法论, agent, llm, coding, simon-willison, 一手源, 已验证]
aliases: [Agentic Engineering]
---

# Agentic Engineering

> 一句话定义：Simon Willison 定义的术语——**专业软件工程师用 AI 工具提升自己工作的方式**，关注质量、安全、可维护性、性能，不是用 AI 降低标准。

## 核心要义

与 [[Vibe Coding]] 严格区分：
- Vibe Coding：不审代码、不懂工程、不关心质量
- Agentic Engineering：用 AI 把自己能做的事做得**更好更快**，而不是用 AI 做更差的事

Willison 的核心信念："I want to build higher quality stuff faster. I want everything I am building to be better in every way than it was before."

**目标不是更便宜的烂软件，而是更好的软件**。

2026 年 5 月的反思：Willison 承认自己开始不审代码了——Agentic Engineering 和 Vibe Coding 在实践中正在融合，这让他不安。

## 关键要素

- **专业基础**：依赖工程师 25 年经验等已有能力 (来源: [[../summaries/20260506-SimonWillison-Vibe coding and agentic engineering]])
- **质量上限提升**：AI 是放大器，让能做的事做得更好 (同上)
- **覆盖范围扩展**：可以处理之前不敢碰的复杂度 (同上)
- **责任不减**：仍然对产出的安全、性能、可维护性负责 (同上)

## 与相关概念的关系

- 与 [[Vibe Coding]]：本概念的对立面（边界在模糊）
- 与 [[Simplicity First]] / [[Surgical Changes]] / [[Think Before Coding]] / [[Goal-Driven Execution]]：CLAUDE.md 4 原则是 Agentic Engineering 的具体实践指南
- 与 [[规范偏差正常化]]：长期 Agentic Engineering 实践者会逐渐松懈，触发该风险
- 与 [[Agent工程化兜底]]：工程化兜底是 Agentic Engineering 的工程纪律

## 典型应用 / 案例

- Willison 自述：用 Agent 处理过去不敢碰的复杂任务 (来源: [[../summaries/20260506-SimonWillison-Vibe coding and agentic engineering]])
- [[../entities/forrestchang|forrestchang]] 的 CLAUDE.md 4 原则 = Agentic Engineering 范式化 (来源: [[../summaries/20260526-GitHub-andrej-karpathy-skills原仓库]])
- 本库 AGENT.md = Agentic Engineering 在知识管理领域的应用 (来源: 自我观察)
- **Moebius 浏览器移植**（2026-06-22）：Simon Willison 展示了 Agentic Engineering 的"并行项目"模式——主项目在 Codex Desktop 处理 Datasette，同时 Claude Code 做 Moebius 移植 (来源: [[../summaries/20260622-SimonWillison-Porting-Moebius-model-to-browser]])。关键实践：\n  - "先研究再执行"流水线：Claude.ai 做可行性研究 → research.md → Claude Code 执行\n  - 信息准备：提前克隆所有相关 repo（源码、权重、依赖库）降低 Agent 失败率\n  - Sub-agent 分担子问题：混淆 JS 分析用子 agent 隔离，避免消耗主 context\n  - 事后补学：让 Claude.ai 读最终 repo 反向教学原理

## 争议 / 局限

- 与 Vibe Coding 边界模糊——专业工程师也会松懈
- "Higher quality faster" 的双重承诺难以同时兑现，多数实践是"差不多 quality faster"

## 相关资料

- [[../summaries/20260506-SimonWillison-Vibe coding and agentic engineering]]
- Willison 的 "agentic-engineering-patterns" 指南系列：simonwillison.net/guides/agentic-engineering-patterns/

## 待深入

- [ ] Willison 完整的 agentic-engineering-patterns 系列梳理
- [ ] Agentic Engineering 在非编程领域（写作、运营）的迁移
