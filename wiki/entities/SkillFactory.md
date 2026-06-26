---
type: entity
created: 2026-06-08
updated: 2026-06-08
sources:
  - "[[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]]"
tags: [项目, ai, agent, skill, harness-engineering, 二手源]
aliases: [技能工厂, Skill Factory]
---

# SkillFactory

> 一句话定义：SkillFactory 是知乎实践文章中的一个面向 [[../concepts/Harness工程|Harness 工程]] 的技能生产系统，把 Skill 创建流程改造成基线诊断、测试驱动、多路生成、质量评分、回归优化的流水线。

## 基本信息

- **类型**：项目 / 原型系统
- **领域**：AI Agent / Skill 生产 / Harness 工程
- **关联实体**：[[Trace2Skill]] · [[Anthropic]] · [[OpenClaw]] · [[Claude Code]]
- **关联概念**：[[../concepts/Skill工厂|Skill 工厂]] · [[../concepts/评测驱动Skill生成|评测驱动 Skill 生成]] · [[../concepts/多路并发竞优|多路并发竞优]]

## 关键事实

- 系统先做裸模型评估与 skill 匹配分析，用失败点判断是否需要生成新 skill (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。
- 生成阶段并行调用多种 creator 策略，以提升首次生成成功率 (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。
- 回归阶段按格式规范、复用创新、功能可用性、运行稳定性、文档规范等维度评分 (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。
- 迭代方向包括基于 trace 的 skill 机会挖掘，以及参考 [[Trace2Skill]] / SkillRL 从轨迹中蒸馏技能 (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。

## 在本知识库中的角色

SkillFactory 是 [[../concepts/Skills 2.0模块化|Skills 2.0 模块化]] 的“生产系统”样本：它不讨论单个 skill 如何写得漂亮，而讨论 skill 如何批量、可测、可回归地变成团队资产。

## 相关资料

- [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]]
- [[Trace2Skill]]

## 待深入

- [ ] 原项目是否有可访问 demo / 代码仓库。
- [ ] 验证其评价维度是否能迁移到 Hana 本地 skills。
