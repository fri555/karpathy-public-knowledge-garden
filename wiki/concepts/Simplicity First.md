---
type: concept
created: 2026-05-26
updated: 2026-05-26
sources:
  - "[[20260526-GitHub-andrej-karpathy-skills原仓库]]"
tags: [llm, agent, prompt工程, 原则, 已验证]
aliases: [简洁优先, KISS for LLM]
---

# Simplicity First

> 一句话定义:[[CLAUDE.md]] 神文件第 2 条原则——**用最少的代码解决问题,不要过度推测**(Minimum code that solves the problem. Nothing speculative.)。

## 核心要义

针对 [[LLM 编程三宗罪]] 第 2 条:LLM 喜欢把简单问题复杂化,堆砌抽象、添加未要求的"灵活性"。

具体反模式 (来源: [[20260526-GitHub-andrej-karpathy-skills原仓库]]):
- 添加要求之外的功能
- 为一次性代码创建抽象
- 添加未要求的"灵活性"或"可配置性"
- 为不可能发生的场景做错误处理
- **如果 200 行代码可以写成 50 行,重写它**

**检验标准**:"资深工程师会觉得这过于复杂吗?"如果是,简化。

## 关键要素

- **量化阈值**:"200 行 vs 50 行"——给出可观察的反直觉指标
- **反向投票**:用"资深工程师视角"做内省 prompt,而非靠 LLM 自评

## 与相关概念的关系

- **解药对应**:专治 [[LLM 编程三宗罪]] 第 2 条
- **同源思想**:与软件工程 KISS / YAGNI 原则同源,只是把目标对象换成 LLM
- **属于**:[[原则化指令]] 范式
- **潜在张力**:与本知识库"宁可多链不要少链"(AGENT.md § 3.3)存在表面冲突——但前者是"代码生成场景",后者是"知识连接场景",目标不同

## 典型应用 / 案例

- [[CLAUDE.md]] 神文件第 2 条原则 (来源: [[20260526-GitHub-andrej-karpathy-skills原仓库]])
- 适用于所有让 LLM 写代码的场景:Claude Code / Cursor / Copilot

## 争议 / 局限

- "简单"是相对概念,在大型项目中"提前抽象"反而避免后期重构成本
- 某些领域(如金融、医疗)需要"防御性编程",过度强调简洁可能漏掉边缘情况
- 对初级开发者可能误导:他们看不出"50 行 vs 200 行"哪个更好

## 相关资料

- [[20260526-GitHub-andrej-karpathy-skills原仓库]]
- [[CLAUDE.md]]
- [[LLM 编程三宗罪]]

## 待深入

- [ ] 收集"过度复杂代码 vs 简化后"的具体 diff 案例,加深直觉
