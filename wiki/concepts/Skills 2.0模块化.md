---
type: concept
created: 2026-05-28
updated: 2026-06-08
sources:
  - "[[20260528-Shareuhack-CLAUDE四层架构实战]]"
  - "[[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂]]"
tags: [方法论, claude, agent, llm, 架构, skill, 已验证]
aliases: [Skills 2.0, folder-based Skills, .claude/skills/]
---

# Skills 2.0 模块化

> 一句话定义：Claude Code 2026 年的 Skills 升级——从旧版 `.claude/commands/*.md` 单文件，升级到 `.claude/skills/{name}/SKILL.md + scripts/ + references/` 文件夹结构，**支持 on-demand 载入和可执行脚本**。

## 核心要义

[[Shareuhack]] 总结的 Skills 系统升级要点：

| | 旧版 | Skills 2.0 |
|---|---|---|
| 结构 | `.claude/commands/deploy.md` | `.claude/skills/deploy/` 文件夹 |
| 内容 | 单一 markdown | SKILL.md + scripts/ + references/ |
| 触发 | 手动 /command | YAML frontmatter 自动触发 |
| 载入 | 在 UI 自动完成 | On-demand 按需载入 |

核心好处：**references/ 的内容不占平时的 context，只在需要时载入**——这让一个 fleet 拥有 20+ Skills 而不爆炸。

## 关键要素

- **SKILL.md frontmatter**：定义 name 和 description，让 Claude 知道何时自主载入（来源: [[20260528-Shareuhack-CLAUDE四层架构实战]]）
- **scripts/**：可执行脚本，Skill 触发时自动可用（来源: [[20260528-Shareuhack-CLAUDE四层架构实战]]）
- **references/**：按需载入的参考文件（来源: [[20260528-Shareuhack-CLAUDE四层架构实战]]）
- **遗留兼容**：旧版 `.claude/commands/*.md` 仍可执行，但不再出现在新版 UI 自动完成清单（来源: [[20260528-Shareuhack-CLAUDE四层架构实战]]）

## 与相关概念的关系

- 与 [[CLAUDE.md四层架构]]：Skills 是四层中的"SOP 层"
- 与 [[原则化指令]]：CLAUDE.md 放原则，Skills 放工作流
- 与 [[Skill 榜单情报化]]：卡尔做的淘金小镇就是 Skill 的二级市场情报

## 典型应用 / 案例

- [[Shareuhack]] fleet 的 /scout /collect /synthesize /write /content-review /translate 等 20+ Skills (来源: [[20260528-Shareuhack-CLAUDE四层架构实战]])
- 本库 `.agents/skills/` 目录已采用类似结构（taojin-xiaozhen、wechat-publish 等） (来源: 自我观察)

## 生产侧补充：Skill 也需要工厂化

2026-06-08 补入的 [[../summaries/20260608-知乎-SkillFactory面向Harness设计的技能工厂|SkillFactory 实践]] 提醒：Skills 2.0 不只是运行时的按需加载机制，也会带来生产侧问题——谁来判断是否该新建 skill、如何避免重复造轮子、如何验证新 skill 真能提升任务表现。

因此，[[Skill工厂]] / [[评测驱动Skill生成]] / [[轨迹蒸馏为技能]] 构成了 Skills 2.0 的下一层：

- **运行层**：SKILL.md + scripts/ + references/ 让 Agent 能按需加载能力。
- **生产层**：基线诊断、测试集、多路并发、质量评分、回归验证让 Skill 可持续交付。
- **进化层**：[[../entities/Trace2Skill|Trace2Skill]] 从成功/失败轨迹中抽取可迁移 SOP，让 Skill 不再完全依赖人工手写。

## 争议 / 局限

- 文件夹结构虽然清晰但管理成本高于单文件
- 自动触发依赖 description 质量——写不好就触发不准
- Skill 生成变便宜后，重复、低质、不可验证的 skill 会迅速堆积；必须引入 [[评测驱动Skill生成]] 门禁

## 相关资料

- [[20260528-Shareuhack-CLAUDE四层架构实战]]

## 待深入

- [ ] Anthropic 官方 Skills 2.0 文档对齐
- [ ] 本库 .agents/skills/ 各 Skill 是否符合 2.0 最佳实践
