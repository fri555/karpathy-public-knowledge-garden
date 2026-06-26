---
type: entity
created: 2026-06-08
updated: 2026-06-08
sources:
  - "[[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]]"
tags: [项目, 论文, ai, agent, skill, qwen, 一手源]
aliases: [Distill Trajectory-Local Lessons into Transferable Agent Skills]
---

# Trace2Skill

> 一句话定义：Trace2Skill 是 Qwen Large Model Application Team 提出的 agent skill 自动演化框架，把大量执行轨迹中的局部经验并行分析、合并成统一且无冲突的可迁移 skill directory。

## 基本信息

- **类型**：论文 / 开源项目
- **组织**：Qwen Large Model Application Team, Alibaba
- **论文**：arXiv:2603.25158，v5 于 2026-06-04 修订（截至 2026-06-08）
- **仓库**：Qwen-Applications/Trace2Skill
- **关联概念**：[[../concepts/轨迹蒸馏为技能|轨迹蒸馏为技能]] · [[../concepts/评测驱动Skill生成|评测驱动 Skill 生成]] · [[../concepts/Skills 2.0模块化|Skills 2.0 模块化]]

## 关键事实

- Pipeline：trajectory generation → parallel multi-agent patch proposal → conflict-free patch consolidation (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。
- 支持两种模式：从已有人工 skill 继续深化，以及从弱 LLM 草稿创建新 skill (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。
- 实验覆盖 office workflow、math reasoning、vision QA 等领域 (来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。
- 论文摘要称 evolved skills 能跨模型规模、模型家族和 OOD 场景迁移；Qwen3.5-35B 轨迹演化出的 skills 可使 Qwen3.5-122B agent 在 WikiTableQuestions 上最高提升 57.65 个百分点（截至 2026-06-08）(来源: [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]])。

## 在本知识库中的角色

Trace2Skill 为 [[../concepts/反馈闭环写入文件|反馈闭环写入文件]] 提供了研究级证据：agent 经验不必长期以 raw trajectory / retrieval memory 形态存在，可以被压缩成声明式、可迁移、按需加载的 [[../concepts/Skills 2.0模块化|Skill]]。

## 相关资料

- [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]]
- arXiv:2603.25158
- Qwen-Applications/Trace2Skill

## 待深入

- [ ] 精读论文方法章节，拆出 success analyst / error analyst / consolidation 三类 prompt。
- [ ] 查看 released spreadsheet skills 与 Anthropic xlsx skill 的差异。
