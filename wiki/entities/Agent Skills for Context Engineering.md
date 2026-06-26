---
type: entity
created: 2026-06-07
updated: 2026-06-07
sources:
  - "[[../summaries/20260607-HN-AgentSkillsForContextEngineering]]"
tags: [项目, github, ai, agent, context-engineering, skill, 一手源]
aliases: [Agent-Skills-for-Context-Engineering, context-engineering skills]
---

# Agent Skills for Context Engineering

> 一句话定义：Agent Skills for Context Engineering 是一个开源 Skill 集合，把 context engineering、multi-agent architecture、tool design、evaluation、harness engineering 等原则封装成可按需加载的 Agent Skills。

## 基本信息

- **类型**：GitHub 开源项目 / Agent Skill 库
- **作者**：[[muratcankoylan]]
- **仓库**：muratcankoylan/Agent-Skills-for-Context-Engineering
- **关联平台**：[[Claude Code]] · [[Cursor]]
- **关联概念**：[[../concepts/上下文工程|上下文工程]] · [[../concepts/Skills 2.0模块化|Skills 2.0 模块化]] · [[../concepts/渐进式披露|渐进式披露]] · [[../concepts/工具设计合并原则|工具设计合并原则]]

## 关键事实

- 项目使用 Anthropic open Agent Skills 格式，每个 skill 是包含 `SKILL.md` 的目录 (来源: [[../summaries/20260607-HN-AgentSkillsForContextEngineering]])。
- 初始 HN 帖列出 7 个 skills：context-fundamentals、context-degradation、multi-agent-patterns、memory-systems、tool-design、context-optimization、evaluation (来源: [[../summaries/20260607-HN-AgentSkillsForContextEngineering]])。
- GitHub README 截至 2026-06-07 显示项目已扩展到 15 个 skills，并增加 context-compression、filesystem-context、hosted-agents、harness-engineering 等模块 (来源: [[../summaries/20260607-HN-AgentSkillsForContextEngineering]])。
- 设计哲学强调 Progressive Disclosure：启动时只加载 skill 名称和描述，任务相关时才加载全文 (来源: [[../summaries/20260607-HN-AgentSkillsForContextEngineering]])。

## 在本知识库中的角色

该项目是 [[../concepts/Skills 2.0模块化|Skills 2.0 模块化]] 的典型样本：Skill 不只是“某项任务的操作手册”，也可以是 Agent 的认知/工程操作系统。它与本地 Hana Skills 的关系值得持续观察。

## 相关资料

- [[../summaries/20260607-HN-AgentSkillsForContextEngineering]]
- [[muratcankoylan]]

## 待深入

- [ ] 抽样审计该仓库 Skills 的安全性与实用性。
- [ ] 研究是否有适合迁移到 Hana 的模块。
