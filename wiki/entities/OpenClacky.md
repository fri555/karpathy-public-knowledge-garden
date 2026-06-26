---
type: entity
created: 2026-05-29
updated: 2026-05-29
sources:
  - "[[20260514-RubyChina-OpenClacky-Harness工程7个关键决策]]"
tags: [工具, ai, agent, llm, ruby, 开源, harness, 已验证]
aliases: [RubyAgent, clacky-ai/openclacky]
---

# OpenClacky

> 一句话定义：OpenClacky 是一个 Ruby 编写的开源通用 AI Agent，主张用 [[../concepts/Harness工程|Harness 工程]] 把 Agent 成本压低到接近 [[Claude Code]]，核心抓手是 [[../concepts/Prompt Cache局部性|Prompt Cache 局部性]] 和 [[../concepts/工具集稳定性|工具集稳定性]]。

## 基本信息

- **类型**：开源通用 Agent / CLI + WebUI
- **主要语言**：Ruby
- **仓库**：clacky-ai/openclacky（MIT 开源，来源: [[20260514-RubyChina-OpenClacky-Harness工程7个关键决策]]）
- **同类对照**：[[Claude Code]] · [[OpenClaw]] · [[Hermes]]
- **关联概念**：[[../concepts/Harness工程|Harness 工程]] · [[../concepts/Prompt Cache局部性|Prompt Cache 局部性]] · [[../concepts/工具集稳定性|工具集稳定性]] · [[../concepts/上下文膨胀与压缩|上下文膨胀与压缩]]

## 关键事实

- OpenClacky 定位为全功能 Agent：WebUI + 命令行、长期记忆、Skill 技能库、定时任务、IM 接入、浏览器自动化、子 Agent、运行时切模型、Skill 自进化与动态加载 (来源: [[20260514-RubyChina-OpenClacky-Harness工程7个关键决策]])
- 作者披露 3 项任务横评：OpenClacky 成本 $5.10、51 请求、90.6% cache 命中率；Claude Code $5.49、70 请求、95.2% 命中率（截至 2026-05-14，来源: [[20260514-RubyChina-OpenClacky-Harness工程7个关键决策]])
- 项目经历三代架构：第一代 RAG/知识库失败，第二代多 Agent 工作流失败，第三代 Ruby 重写并围绕 cache 局部性 + 工具集稳定性组织 (来源: [[20260514-RubyChina-OpenClacky-Harness工程7个关键决策]])
- 核心设计包括：双 cache marker、冻结 system prompt、`invoke_skill`、16 个稳定工具、Insert-then-Compress、脚本式工具自进化、接管已有浏览器 (来源: [[20260514-RubyChina-OpenClacky-Harness工程7个关键决策]])

## 在本知识库中的角色

OpenClacky 给本库补上了一个关键拼图：**Agent 产品的成本工程**。

此前本库已有：
- [[Claude Code]] / [[Codex]]：顶级 CLI Agent 产品侧
- [[../concepts/Skills 2.0模块化|Skills 2.0 模块化]]：能力模块化侧
- [[../concepts/Agent工程化兜底|Agent 工程化兜底]]：安全与可靠性侧
- [[../concepts/上下文膨胀与压缩|上下文膨胀与压缩]]：长期运行维护侧

OpenClacky 的独特贡献是：把这些能力放到 **prompt cache 与工具 schema 的成本几何** 中重新解释——功能越多，越要克制地保持前缀和工具集稳定。

## 争议 / 局限

- 作者“不要做多 Agent 编排”的观点非常激进，适合提醒 cache 成本，但不能一刀切否定长期岗位型 Agent 分工。
- 横评数据来自项目方自测，需后续用 GitHub benchmark 或第三方复测补强。
- Ruby 技术栈安装体验好，但生态与主流 Python/TypeScript Agent 社区存在差异。

## 相关资料

- [[20260514-RubyChina-OpenClacky-Harness工程7个关键决策]]
- [[Claude Code]]
- [[../concepts/Harness工程|Harness 工程]]
- [[../concepts/Prompt Cache局部性|Prompt Cache 局部性]]

## 待深入

- [ ] 抓取 GitHub README / benchmark 数据作为辅助源
- [ ] 对比 OpenClacky 与 OpenClaw / Hermes 的架构差异
- [ ] 研究 OpenClacky 的 `invoke_skill` 是否可迁移到本库 skill 设计
