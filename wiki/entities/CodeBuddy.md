---
type: entity
created: 2026-06-03
updated: 2026-06-03
sources:
  - "[[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]]"
tags: [工具, agent, llm, coding, 已验证]
aliases: []
---

# CodeBuddy

> 一句话定义：CodeBuddy 是本文案例中使用的 AI Coding Agent，用于在 [[TDSQL]] HBase 兼容层 conditional mutation 功能开发中执行需求澄清、方案设计、测试生成和代码编写工作流。

## 基本信息

- **类型**：AI Coding Agent
- **出现语境**：[[davidycwei]] 的 [[agentic-engineering-framework]] 真实项目案例
- **关联概念**：[[../concepts/Agentic Engineering|Agentic Engineering]] · [[../concepts/Spec-First工作流|Spec-First 工作流]]

## 关键事实

- 在 TDSQL HBase conditional mutation 案例中，CodeBuddy 按框架定义的 Workflow 执行：需求澄清、方案设计、测试生成、代码编写 (来源: [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]])
- 需求澄清阶段，Agent 先通过代码搜索理解现状，再向工程师确认判断，避免基于错误前提继续推进 (来源: [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]])
- 编码阶段，Agent 会按文件类型自动加载通用编码实践、公司 C++ 规范、项目编码约束、分布式系统最佳实践 (来源: [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]])

## 在本库中的角色

CodeBuddy 暂时不是主线产品节点，而是 [[../concepts/Agentic Engineering|Agentic Engineering]] 案例中的执行载体。它证明方法论不局限于 Claude Code / Codex，也可以迁移到其他 Coding Agent。

## 相关资料

- [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]]
- [[agentic-engineering-framework]]

## 待深入

- [ ] 了解 CodeBuddy 产品形态与 Claude Code / Codex 的差异。
