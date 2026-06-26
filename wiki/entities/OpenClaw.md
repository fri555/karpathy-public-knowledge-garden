---
type: entity
created: 2026-05-29
updated: 2026-05-29
sources:
  - "[[20260514-RubyChina-OpenClacky-Harness工程7个关键决策]]"
tags: [工具, ai, agent, llm, 开源, 对照, 待深入]
aliases: []
---

# OpenClaw

> 一句话定义：OpenClaw 是 OpenClacky 文章中被拿来横向评测的开源 Agent 对照对象之一；在本库中暂作为 [[OpenClacky]] 的成本/架构参照实体。

## 基本信息

- **类型**：开源 Agent / 个人 AI 助手类工具（需后续一手源确认）
- **关联实体**：[[OpenClacky]] · [[Claude Code]] · [[Hermes]]
- **关联概念**：[[../concepts/Harness工程|Harness 工程]] · [[../concepts/Prompt Cache局部性|Prompt Cache 局部性]]

## 关键事实

- 在 OpenClacky 作者横评中，OpenClaw 任务总成本 $15.70、请求数 81、Cache 命中率 88.7%（截至 2026-05-14，来源: [[20260514-RubyChina-OpenClacky-Harness工程7个关键决策]]）
- OpenClacky 作者认为成本差距主要来自请求数和 cache 命中率，而不是模型智能本身 (来源: [[20260514-RubyChina-OpenClacky-Harness工程7个关键决策]])

## 在本知识库中的角色

当前仅作为 OpenClacky 横评中的对照实体，不独立展开。它的价值在于帮助本库从“某个 Agent 好不好用”转向“不同 Harness 工程如何影响成本结构”。

## 待深入

- [ ] 抓取 OpenClaw 一手源，确认项目定位、架构与维护状态
- [ ] 与 [[OpenClacky]] / [[Hermes]] 做同类 Agent 架构对比
