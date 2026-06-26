---
type: concept
created: 2026-05-24
updated: 2026-05-24
sources:
  - "[[20260407-知乎-Karpathy开源Agent知识库]]"
tags: [工作流, llm, agent]
aliases: [Query, 提问]
---

# Query 查询

> 一句话定义：[[LLM Wiki]] 三个核心操作之一——对着 Wiki 提问，Agent 综合相关页面回答，并把新洞察沉淀回 Wiki。

## 核心要义

不是简单的"问答"，而是**带着已有知识网络回答，再把回答中产生的新综合反哺给网络**。

> 这样你每次的探索和提问都在持续丰富知识库，知识在复利增长。

## 标准流程（按 [[../../AGENT|AGENT.md]]）

1. 先读 `wiki/index.md` 定位相关页
2. 读相关 Wiki 页（不是回去检索原文）
3. 综合回答，回答里**必须**带 `[[页面链接]]` 让人能跳过去
4. **沉淀回 Wiki**：新产生的对比/综述/洞察写进 `wiki/syntheses/` 或更新概念页
5. 追加 `wiki/log.md`

## 输出形式

可以是 Markdown 页面、对比表格、Marp 幻灯片、matplotlib 图表 (来源: [[20260407-知乎-Karpathy开源Agent知识库]])

## 关键约束

**问完即忘 = 系统失败。** 这是 [[LLM Wiki]] 与传统 LLM 问答最大的区别。

## 与相关概念的关系

- 消费 [[Ingest 录入]] 的产出
- 产物（综述、对比）反哺 Wiki，触发 [[Maintain 维护]] 的需求

## 相关资料

- [[20260407-知乎-Karpathy开源Agent知识库]]
- [[../../AGENT|AGENT.md]] § 2.2

## 待深入

- [ ] 多轮 query 的上下文管理
- [ ] query 触发自动 ingest 的边界（什么时候顺手把网页资料也 ingest 了）
