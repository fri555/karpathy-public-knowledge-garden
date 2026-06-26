---
type: concept
created: 2026-06-08
updated: 2026-06-08
sources:
  - "[[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]]"
tags: [方法论, ai, agent, skill, harness-engineering, 已验证]
aliases: [Skill Factory, 技能工厂]
---

# Skill 工厂

> 一句话定义：Skill 工厂是把 Skill 从“手写 Markdown / 对话生成”升级为可诊断、可评测、可回归、可发布的生产流水线。

## 核心要义

Skill 工厂解决的是 [[../concepts/Skills 2.0模块化|Skills 2.0]] 爆发后的生产质量问题：当生成一个 `SKILL.md` 变得很便宜，真正稀缺的是知道“该不该生成”“生成后是否有效”“是否重复造轮子”“能否稳定复用”。它把 Skill 当作软件交付件处理，而不是把 Skill 当作 prompt 文案。关键变化是从“先写 skill”转成“先定义失败样本和验证标准”。

## 关键要素

- **基线诊断**：裸模型评估 + 相似 skill 匹配，确认能力缺口真实存在 (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。
- **测试驱动**：复用/扩展用户测试问题，先有验证集再生成 skill (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。
- **并行候选**：多个 creator / 模型 / Prompt 路线并发生成候选，择优录用 (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。
- **质量门禁**：按格式、复用创新、可用性、稳定性、文档规范评分 (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。
- **轨迹蒸馏**：长期方向是从 agent 成功/失败轨迹中自动抽取可迁移经验 (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。

## 与相关概念的关系

- 与 [[Skills 2.0模块化]]：Skills 2.0 定义“Skill 如何被加载”，Skill 工厂定义“Skill 如何被生产和验证”。
- 与 [[评测驱动Skill生成]]：后者是 Skill 工厂的核心工作流。
- 与 [[轨迹蒸馏为技能]]：后者是 Skill 工厂规模化的经验来源。
- 与 [[验证瓶颈]]：Skill 工厂是对“生成便宜、验证昂贵”的工程回应。

## 典型应用 / 案例

- [[../entities/SkillFactory|SkillFactory]]：知乎实践文章中的原型系统 (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。
- [[../entities/Trace2Skill|Trace2Skill]]：研究级 pipeline，把执行轨迹合并成 skill directory (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。

## 争议 / 局限

- 初期搭建成本高，适合高频、可复用、可测试的任务，不适合一次性小需求。
- 如果测试集来自少量用户输入，容易把 skill 过拟合成“会答那几个样例”。

## 相关资料

- [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]]
- [[../entities/Trace2Skill|Trace2Skill]]

## 待深入

- [ ] 为 Hana 本地 skills 设计一个轻量版 Skill 工厂评分表。
