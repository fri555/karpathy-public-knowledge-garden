---
type: concept
created: 2026-05-24
updated: 2026-05-26
sources:
  - "[[20260407-知乎-Karpathy开源Agent知识库]]"
  - "[[20260413-知乎-Qwen Code+Obsidian搭建Karpathy知识库]]"
  - "[[20260525-知乎-Claude永久大脑真的来了]]"
tags: [方法论, ai, llm, agent, 知识管理]
aliases: [Karpathy 知识库, Karpathy Wiki, LLM 知识库]
---

# LLM Wiki

> 一句话定义：[[Andrej Karpathy]] 提出的知识库范式——人类喂资料提问题，LLM 持续编译维护一个 Markdown 知识网络，知识"编译一次、持续保持最新"。

## 核心要义

颠覆"LLM = 检索式问答"的常规用法。把 LLM 当成**不知疲倦的知识工程师**，让它把散乱的原始资料编译成结构化的 Wiki，每次操作都让 Wiki 变得更丰富——这就是 [[知识复利]]。

关键区别：
- **传统 [[RAG]]**：每次提问从原文重新检索拼接，问完即忘
- **LLM Wiki**：编译一次，交叉引用预先建好，矛盾预先标注，综合分析持续累积

## 关键要素

- **[[三层架构]]**：原始资料层（只读）+ Wiki 层（LLM 写人读）+ [[AGENT.md 协议]]（共同迭代）
- **三个核心操作**：[[Ingest 录入]] · [[Query 查询]] · [[Maintain 维护]]
- **复利原则**：每加一份资料、每问一个问题，Wiki 都要更好——绝不允许"问完即忘"
- **数据格式**：纯 Markdown + 双向链 `[[...]]`，本质上是 Git 仓库

## 与相关概念的关系

- 与 [[RAG]] 的区别：RAG 是检索时拼接，LLM Wiki 是录入时编译——前者重查询轻维护，后者重维护轻查询
- 与 [[Zettelkasten]] / [[Roam Research]] 的联系：都是双向链知识网络。区别在于谁来维护——前者靠人，LLM Wiki 把维护工作完全交给 LLM
- 与 [[Memex]] 的呼应：Vannevar Bush 1945 年的设想终于在 LLM 时代找到了可行维护机制
- 与 [[NotebookLM]] 的对立：NotebookLM 是典型 RAG 范式，Karpathy 明确批判此类工具

## 典型应用 / 案例

- Karpathy 本人的研究知识库 (来源: [[20260407-知乎-Karpathy开源Agent知识库]])
- 本知识库本身就是一个实例 (见 [[../../AGENT|AGENT.md]])
- 社区已涌现多种工具实现：Go 写的 CLI（含 MCP Server）、[[Claude Code]] skill、专用 IDE
- ⭐ **[[Anthropic]] 的 [[Memory Files]]**（2026-05 灰度）——LLM Wiki 理念的**消费级产品化**，是迄今最有力的商业化背书。知乎评论 @袁医生要好好努力 直言「这不就是 kapathy 的 LLM wiki？」 (来源: [[20260525-知乎-Claude永久大脑真的来了]])

## 争议 / 局限

- 评论区有人指出：**专业知识"摘要即丢失关键信息"**——LLM Wiki 在高度专业的硬科学场景可能弱化原始材料的精度
- 中等规模（几百页）OK，更大规模能否仅靠索引文件支撑、未充分验证
- 矛盾点的最终裁决权问题——LLM 标矛盾，但谁拍板？

## 相关资料

- [[20260407-知乎-Karpathy开源Agent知识库]]
- [[20260413-知乎-Qwen Code+Obsidian搭建Karpathy知识库]]
- [[20260524-理念vs实操-两篇知乎对比综述]]
- [[20260525-知乎-Claude永久大脑真的来了]] ⭐ — Memory Files / Dreams / Conway 三件套
- [[20260526-Karpathy理念vsAnthropic产品化-LLM Wiki的消费级落地]] ⭐ — 本次新增综述

## 待深入

- [ ] Karpathy 原始 Gist 的完整内容
- [ ] 千页规模下的 context 管理策略
- [ ] 与 Zettelkasten 的方法论对比
- [ ] [[Memory Files]] 正式上线后，本知识库是否需要兼容 / 互通
