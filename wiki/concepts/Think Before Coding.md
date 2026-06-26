---
type: concept
created: 2026-05-26
updated: 2026-05-26
sources:
  - "[[20260526-知乎-CLAUDE.md神文件让ClaudeCode听话]]"
  - "[[20260526-GitHub-andrej-karpathy-skills原仓库]]"
tags: [llm, agent, prompt工程, 原则, 方法论, 已验证]
aliases: [TBC, 思考再编码, 编码前思考]
---

# Think Before Coding

> 一句话定义:[[CLAUDE.md]] 神文件第 1 条核心原则——**不要假设,不要隐藏困惑,呈现权衡**(Don't assume. Don't hide confusion. Surface tradeoffs.)。

## 核心要义

针对 [[LLM 编程三宗罪]] 第 1 条:LLM 不确定时不问,自己猜,bug 就埋进去了。要求 LLM 在动手写代码前,主动暴露自己的假设、要求人类确认,而不是"先假设,后实现"。

## 具体子条款(来自 GitHub 一手源)

实施前 (来源: [[20260526-GitHub-andrej-karpathy-skills原仓库]]):
- **明确说明假设**(State your assumptions explicitly)。如果不确定,询问
- **多种解释要呈现**(If multiple interpretations exist, present them)——不要默默选择
- **更简单方案要说出来**(If a simpler approach exists, say so)。必要时反对用户的方案
- **不清楚就停下**(If something is unclear, stop)。指出困惑,要求澄清

原文金句:
> "LLM 应该主动说『这里我假设了 X,你确认吗』,而不是假设完直接实现"

## 关键要素

- **暴露假设**:让推理过程可见
- **拒绝静默选择**:歧义不能私下决断
- **可以反对用户**:更简单的方案要敢提
- **困惑必须命名**:不是"我有点不确定",而是"X 这个地方不确定"——具体到点

## 与相关概念的关系

- **解药对应**:专门治疗 [[LLM 编程三宗罪]] 第 1 条"默默做错误假设"
- **同源哲学**:与本知识库 [[../../AGENT|AGENT.md]] § 4.4 红线"**不确定时停下来问人类**"完全同源——这是两份独立诞生的协议在同一原则上的共鸣
- **属于**:[[原则化指令]] 范式下的一条具体原则
- **延伸**:可推广到 ingest / query / maintain 任何 Agent 任务,不只是写代码

## 典型应用 / 案例

- [[CLAUDE.md]] 神文件第 1 条原则(GitHub 15.5 万 star,登顶热榜) (来源: [[20260526-GitHub-andrej-karpathy-skills原仓库]])
- 本知识库 Agent 的工作准则:发现资料含糊时主动询问,不脑补
- [[Hana]] / [[Claude Code]] / [[Codex]] / [[Cursor]] 等 CLI Agent / IDE 的通用质量护栏

## 争议 / 局限

- 实际操作中"问与不问的尺度"难以拿捏:问得太频繁会拖慢节奏,问得太少又会埋 bug
- 对"自主性高"的 Agent 任务(如自动巡检、批量数据处理),"必须问"会破坏自动化体验,需要分级
- 有时 LLM 的"假设"反而比人类初始描述更准——硬性要求"先问"可能错失生产力
- 与 [[Goal-Driven Execution]] 存在表面张力:一个要"先问",一个要"循环干"。实际是分场景——目标清晰用 Goal-Driven,假设不清用 TBC

## 相关资料

- [[20260526-GitHub-andrej-karpathy-skills原仓库]]
- [[CLAUDE.md]]
- [[LLM 编程三宗罪]]

## 待深入

- [ ] 对比 Anthropic 官方 prompt 工程指南里的"clarify before act"建议
- [ ] 本知识库 ingest 流程里如何具体落地 TBC——什么算"足够不确定要打断人类"
