---
type: entity
created: 2026-06-03
updated: 2026-06-03
sources:
  - "[[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]]"
tags: [产品, 数据库, 工程实践, 案例, 已验证]
aliases: []
---

# TDSQL

> 一句话定义：TDSQL 是腾讯数据库产品；在 [[davidycwei]] 的 [[../concepts/Agentic Engineering|Agentic Engineering]] 文章中，它作为真实工程案例的项目背景出现。

## 基本信息

- **类型**：数据库产品
- **所属组织**：腾讯
- **本文案例**：HBase 兼容层支持 conditional mutation
- **关联实体**：[[CodeBuddy]] · [[agentic-engineering-framework]]

## 关键事实

- 文章案例要求在 TDSQL 的 HBase 兼容层中支持 conditional mutation 功能 (来源: [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]])
- 该功能开发被拆成需求澄清、方案设计、测试生成、代码编写四个阶段，用于展示 [[../concepts/Spec-First工作流|Spec-First 工作流]] 与多层验证 (来源: [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]])

## 在本库中的角色

TDSQL 不是本库主线实体，而是 Agentic Engineering 的生产级复杂系统案例：它说明复杂工程任务不能只靠 vibe coding，必须用 spec、边界条件、测试计划和项目规范约束 Agent。

## 相关资料

- [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]]
- [[CodeBuddy]]
