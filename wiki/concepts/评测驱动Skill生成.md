---
type: concept
created: 2026-06-08
updated: 2026-06-08
sources:
  - "[[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]]"
tags: [方法论, ai, agent, skill, 测试, 已验证]
aliases: [Skill TDD, 测试驱动技能生成]
---

# 评测驱动 Skill 生成

> 一句话定义：评测驱动 Skill 生成是在写 Skill 前先定义基线、测试问题和评分维度，用验证闭环决定是否生成、保留、优化或发布 Skill。

## 核心要义

它把 Skill 开发从“写一段说明让 Agent 试试”改造成类似 TDD / CI 的闭环：先知道没有 skill 时会怎样，再知道已有 skill 是否够用，最后让新 skill 对准明确失败样本改进。这样可以防止为了“显得工程化”而制造无用 skill，也能防止 skill 与已有能力重复。

## 关键要素

- **without-skill 基线**：先让裸模型执行目标任务，确认失败模式 (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。
- **with-existing-skill 对照**：召回相似 skill 执行测试，判断是否可复用 (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。
- **测试问题复用**：把用户原始测试问题作为初始评测集，而不是只写抽象描述 (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。
- **多维评分**：格式规范、复用创新、功能可用性、运行稳定性、文档规范共同决定质量 (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。

## 与相关概念的关系

- 与 [[验证瓶颈]]：直接回应 Skill 生成后的验证成本。
- 与 [[First Run The Tests]]：同样强调先找验证入口，再改动系统。
- 与 [[Goal-Driven Execution]]：成功标准清楚，Agent 才能循环改进。
- 与 [[Skill工厂]]：是 Skill 工厂的核心流程。

## 典型应用 / 案例

- [[../entities/SkillFactory|SkillFactory]] 先做裸模型评估和 skill 匹配分析，再进入多路生成与回归优化 (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。

## 争议 / 局限

- 测试集太小会诱导 skill 只“背答案”。
- 许多非执行型 skill（如审美、写作、策略分析）难以自动评测，需要人工 rubrics。

## 相关资料

- [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]]

## 待深入

- [ ] 设计适合写作/运营类 skill 的人工评测 rubric。
