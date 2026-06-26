---
type: concept
created: 2026-05-24
updated: 2026-05-24
sources:
  - "[[20260407-知乎-Karpathy开源Agent知识库]]"
tags: [方法论, ai, llm, 知识管理]
aliases: [Retrieval-Augmented Generation, 检索增强生成]
---

# RAG

> 一句话定义：Retrieval-Augmented Generation——把文档分块索引，提问时检索相关片段拼进 prompt 让 LLM 生成回答的主流方案。

## 核心要义

主流 LLM 知识管理范式：
1. 文档上传 → 切块 → 向量化 → 索引
2. 用户提问 → 检索 Top-K 相关片段 → 拼进 prompt
3. LLM 基于检索片段生成答案

[[NotebookLM]]、ChatGPT 的文件上传、大部分企业知识库都是这个套路。

## 关键要素

- 向量检索（embedding + 向量数据库）
- 文档分块（chunking）
- 上下文拼接（context stuffing）
- 生成回答（answer generation）

## 与 [[LLM Wiki]] 的对立

| 维度 | RAG | LLM Wiki |
|---|---|---|
| 编译时机 | 查询时检索拼接 | 录入时编译沉淀 |
| 持久产物 | 无（答完即忘） | Markdown Wiki（复利增长） |
| 跨文档综合 | 每次重做 | 已预先建好 |
| 矛盾处理 | 不感知 | 录入时标注 |
| 维护成本 | 低 | 高（但 LLM 承担） |
| 适用规模 | 大语料、低频追问 | 中等语料、高频深耕 |

[[Andrej Karpathy]] 对 RAG 的核心批判：**每次提问 LLM 都得从原始文档里重新找、重新拼，问完了答案就没了**。

## 典型应用 / 案例

- [[NotebookLM]]
- ChatGPT 的文件上传
- 各类企业内部知识库

## 争议 / 局限（按 Karpathy 视角）

- 答案不持久——同一问题反复推导
- 跨多文档综合的复杂问题低效
- 没有"知识增长"的概念——堆得越多越乱

## 相关资料

- [[20260407-知乎-Karpathy开源Agent知识库]]

## 待深入

- [ ] RAG 与 LLM Wiki 是否可融合（用 RAG 检索 Wiki 页）
