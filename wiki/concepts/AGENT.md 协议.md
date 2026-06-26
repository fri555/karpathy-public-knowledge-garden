---
type: concept
created: 2026-05-24
updated: 2026-05-24
sources:
  - "[[20260407-知乎-Karpathy开源Agent知识库]]"
tags: [架构, 协议, llm, agent]
aliases: [AGENT.md, agent 协议]
---

# AGENT.md 协议

> 一句话定义：[[三层架构]] 中的第三层——给 LLM Agent 读的配置文件，规定 Wiki 怎么组织、用什么约定、各种操作遵循什么流程。

## 核心要义

让人类和 LLM 能持续协作的"宪法"。任何 Agent 接手前必须先读，确保跨会话、跨模型行为一致。

## 关键设计原则

- **共同迭代**：人与 Agent 都可提议修改，但要走流程（log 留痕 → 人批准 → 修改）
- **覆盖所有关键流程**：[[Ingest 录入]]、[[Query 查询]]、[[Maintain 维护]] 都要写明
- **强约束 + 留弹性**：命名规范严格，分类体系开放
- **可审计**：每次操作都写入 log.md，便于追溯

## 本知识库的 AGENT.md 结构

参见 [[../../AGENT|AGENT.md]]，共 5 节：
1. 核心理念
2. [[三层架构]]
3. 工作流（三个操作）
4. 命名与格式规范
5. 关键约束
6. 迭代本协议的流程

## 与相关概念的关系

- 是 [[LLM Wiki]] 方法论的可执行化
- 是 [[三层架构]] 的协议层
- 类似软件工程中的 README + CONTRIBUTING + STYLE 三合一

## 典型应用 / 案例

- 本知识库的 [[../../AGENT|AGENT.md]]
- B 站 BV1p4DeB8ECi 视频提到的 up 主版 AGENT.md（待找）

## 相关资料

- [[20260407-知乎-Karpathy开源Agent知识库]]
- [[20260413-知乎-Qwen Code+Obsidian搭建Karpathy知识库]]

## 待深入

- [ ] 对比社区已公开的几版 AGENT.md，提炼最佳实践
- [ ] 何时该把 AGENT.md 拆成多文件（按操作分？按领域分？）
