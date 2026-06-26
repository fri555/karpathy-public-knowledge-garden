---
type: concept
created: 2026-05-28
updated: 2026-05-28
sources:
  - "[[20260528-Shareuhack-CLAUDE四层架构实战]]"
tags: [方法论, claude, agent, llm, 架构, 已验证]
aliases: [Claude Code 四层架构, CLAUDE.md 四层分工]
---

# CLAUDE.md 四层架构

> 一句话定义：Claude Code 的完整配置体系不是 CLAUDE.md 一个文件，而是 **CLAUDE.md（行为宪法）/ Skills（可执行 SOP）/ Hooks（强制执行法）/ Memory（学习记录）** 四层分工——把所有东西塞进 CLAUDE.md 是最常见的错误。

## 核心要义

[[Shareuhack]] 基于自家 6-Agent fleet 实战提出的核心架构。理解关键不是"每一层能做什么"，而是"每一层**不该做什么**"：

| 层级 | 职责 | 载入时机 | **不该放的东西** |
|---|---|---|---|
| **CLAUDE.md** | 行为规则、禁止事项、专案架构 | 每 session 全量载入 | 步骤型操作指令（用 Skills） |
| **Skills** | 可执行的工作流模组 | On-demand（呼叫时才载入） | 永久性规则（放 CLAUDE.md） |
| **Hooks** | 确定性强制执行 | 工具呼叫前后自动触发 | 灵活判断逻辑（那是 AI 的事） |
| **Memory** | 跨 session 状态延续 | 自动累积、自动载入 | 不变的规则（放 CLAUDE.md） |

核心好处是 **context 效率**：CLAUDE.md 的规则永远在场，但 Skills 只在被呼叫时占用 context。塞 30 个工作流到 CLAUDE.md 会浪费大量 token。

## 关键要素

- **CLAUDE.md 三层优先级**：global(~/.claude/) → project({proj}/) → local(CLAUDE.local.md)（来源: [[20260528-Shareuhack-CLAUDE四层架构实战]]）
- **路径作用域**：`.claude/rules/frontend.md` 只在处理前端文件时载入（来源: [[20260528-Shareuhack-CLAUDE四层架构实战]]）
- **Skills 2.0 文件夹结构**：`SKILL.md + scripts/ + references/`（来源: [[20260528-Shareuhack-CLAUDE四层架构实战]]）
- **5000 行经验阈值**：Shareuhack 自家 20+ Skills 全塞 CLAUDE.md 会超过 5000 行无法运作（来源: [[20260528-Shareuhack-CLAUDE四层架构实战]]）

## 与相关概念的关系

- 与 [[原则化指令]]：原则化指令是哲学，四层架构是工程化实现
- 与 [[记忆文件vs技能文件]]：Saboo 的二分法是四层架构的子集
- 与 [[Hooks确定性执行]]：Hooks 是四层中"最被低估"的一层
- 与 [[三套记忆系统]]：Memory 这一层的内部进一步细分

## 典型应用 / 案例

- [[Shareuhack]] 自家 6-Agent fleet 全流程无人值守 (来源: [[20260528-Shareuhack-CLAUDE四层架构实战]])
- 本知识库 AGENT.md（CLAUDE.md 等价）+ .agents/skills/（Skills 等价）+ log.md（Memory 等价），**缺 Hooks 层**——是潜在升级方向 (来源: 自我观察)

## 争议 / 局限

- 没回答"什么时候 CLAUDE.md 反而该长"——对密集禁止事项的场景没指引
- 四层之间的优先级冲突处理细节文中未完全展开

## 相关资料

- [[20260528-Shareuhack-CLAUDE四层架构实战]]
- [[20260528-36氪-Saboo30天6Agent复盘]]（独立路径收敛同一二分法）

## 待深入

- [ ] 本库要不要建 Hooks 层（git pre-commit）？
- [ ] 与 Anthropic 官方 Claude Code 文档对齐
