---
type: entity
created: 2026-05-29
updated: 2026-05-29
sources:
  - "[[20260514-RubyChina-OpenClacky-Harness工程7个关键决策]]"
tags: [工具, ai, agent, llm, 对照, 待深入]
aliases: []
---

# Hermes

> 一句话定义：Hermes 是 OpenClacky 文章中被拿来横向评测的 Agent 对照对象之一；在本库中暂作为 [[OpenClacky]] 的成本/请求数/cache 命中率参照实体。

## 基本信息

- **类型**：Agent 工具（需后续一手源确认）
- **关联实体**：[[OpenClacky]] · [[Claude Code]] · [[OpenClaw]]
- **关联概念**：[[../concepts/Harness工程|Harness 工程]] · [[../concepts/Prompt Cache局部性|Prompt Cache 局部性]]

## 关键事实

- 在 OpenClacky 作者横评中，Hermes 任务总成本 $30.14、请求数 218、Cache 命中率 60.3%（截至 2026-05-14，来源: [[20260514-RubyChina-OpenClacky-Harness工程7个关键决策]]）
- OpenClacky 作者将 Hermes 的高成本归因于请求数高与 cache 命中率低 (来源: [[20260514-RubyChina-OpenClacky-Harness工程7个关键决策]])

## 在本知识库中的角色

当前仅作为 OpenClacky 横评中的成本反例实体。它提醒：Agent “功能多”不等于“工程好”，请求数与 cache 命中率会直接决定真实使用成本。

## 待深入

- [ ] 抓取 Hermes 一手源，确认它是否与长期记忆 Agent / Hermes 框架相关
- [ ] 与 [[OpenClacky]] / [[OpenClaw]] 做同类 Agent 架构对比
