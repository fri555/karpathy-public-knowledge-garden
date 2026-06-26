---
type: entity
created: 2026-05-26
updated: 2026-05-26
sources:
  - "[[20260519-TechCrunch-Karpathy加入Anthropic预训练团队]]"
tags: [软件, ai, llm, agent, 开源, github, 一手源, 复利, 种子]
aliases: [karpathy/autoresearch]
---

# autoresearch

> 一句话定义：[[Andrej Karpathy]] 2026-03 个人开源的 AI-assisted research 极简框架（630 行 Python / 单 GPU / 5 分钟一轮 / 夜间自动跑 100 实验），是他 2026-05 加入 [[Anthropic]] 做 [[递归自我改进]] 团队的**技术伏笔与可行性证明**。

## 基本信息

- **类型**：开源软件 / 个人项目
- **作者**：[[Andrej Karpathy]]
- **首次提交**：2026-03-06
- **最后 push**：2026-03-26
- **协议**：MIT
- **GitHub star**：**83,345**（截至 2026-05-27）
- **关联实体**：[[Andrej Karpathy]]（作者）· [[Anthropic]]（招他放大此思路的雇主）· [[Claude Code]]（被用作 agent 执行）

## 设计要点

- **5 分钟固定时间预算 / 12 实验每小时**：把"研究"压缩进可重复的固定时间盒
- **单文件 `train.py`**：agent 只允许改动这一个文件
- **`program.md`**：Karpathy 自称"超轻量 skill"——对应 [[CLAUDE.md]] / [[Simplicity First]] 的同源叙事
- **夜间批量跑**：人睡觉时 agent 跑 100 个变种实验，早上看 metric 选优胜

## 在本知识库中的角色

- 是 [[Goal-Driven Execution]] 原则的**纯粹工程化演示**（给 agent 一个 metric: val_bpb + 一个时间预算 + 循环到达成）
- 是 [[递归自我改进]] 概念在**个人尺度**上的存在性证明
- 与 [[Dreams]] 的"REM 式后台整合" 在 ergonomic 上同源——都是"夜里跑、白天看结果"
- 与 [[原则化指令]] 同脉络——`program.md` 是"超轻量 skill"
- 解释了 Anthropic 为什么招 Karpathy 做这件事——他不是"被分配课题"，而是"被放大已有作品"

## 原文金句

> One day, frontier AI research used to be done by meat computers in between eating, sleeping, having other fun, and synchronizing once in a while using sound wave interconnect in the ritual of 'group meeting'. That era is long gone.
> —— Karpathy, autoresearch README 开篇

> program.md is essentially a super lightweight 'skill'.
> —— Karpathy, autoresearch README

## 待深入

- [ ] README 中引用的两条推文（ID 2029701092347630069 / 2031135152349524125）原文
- [ ] 是否有人复现 / fork 出衍生项目？
- [ ] Anthropic 是否会公开把 autoresearch 思路扩展为产品/论文
- [ ] 与 [[Conway]]（永不下线 Agent 平台）的运行时是否兼容/将合并

## 相关资料

- [[20260519-TechCrunch-Karpathy加入Anthropic预训练团队]] ⭐ 一手源（首次将 autoresearch 与 Anthropic 招聘关联起来）
