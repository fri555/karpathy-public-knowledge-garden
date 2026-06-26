---
type: entity
created: 2026-05-27
updated: 2026-05-28
sources:
  - "[[20260407-知乎-Karpathy开源Agent知识库]]"
  - "[[20260527-知乎-卡尔-淘金小镇Skill榜单情报项目]]"
tags: [工具, ai, agent, llm, openai, cli]
aliases: [OpenAI Codex]
---

# Codex

> 一句话定义：OpenAI 的 CLI 编码 Agent，与 [[Claude Code]] 同类竞品，[[Andrej Karpathy]] 自己日常使用的两大 Agent 之一；**`/goal` 无限循环模式**是其旗舰特性，已被 [[卡尔的AI沃茨]] 的 [[淘金小镇]] 项目工程验证。

## 基本信息

- **类型**：CLI Agent / 编码助手
- **厂商**：OpenAI
- **关联实体**：[[Claude Code]]（同类竞品）· [[Qwen Code]]（同类竞品）· [[淘金小镇]]（用 Codex 开发）
- **关联概念**：[[Goal-Driven Execution]] · [[Goal 模式自动化爬虫]] · [[LLM Wiki]]

## 关键事实

- Karpathy 自己日常使用的 Agent 之一（与 Claude Code 并列）(来源: [[20260407-知乎-Karpathy开源Agent知识库]])
- **`/goal` 无限循环模式**是其旗舰特性——给定成功标准，Agent 自主循环验证直到达成
- 是 [[Goal-Driven Execution]]（[[CLAUDE.md]] 第 4 条原则）的产品化实现

## `/goal` 模式工程实证

卡尔的 [[淘金小镇]] 项目实战记录 (来源: [[20260527-知乎-卡尔-淘金小镇Skill榜单情报项目]])：

| 旧方案 | Codex `/goal` 模式 |
|---|---|
| 浏览器自动化 + prompt-heavy 提示词 | `/goal` 循环 30 次，目标："找出依赖最少的方案" |
| 一周三天失败 | 第 5 小时发现 [[Convex]] API，问题解决 |
| 升 GPT 5.5 high 还是高失败率 | 稳定拿到 ClawHub Top100 |

> "就算我写了足够复杂足够详细的提示语,一周还是有三天是失败的……让新版 Codex 上无限循环模式(/goal),目标就是找出依赖最少的方案,**这样比我在提示语里面上十几个限制都好用**。" — 卡尔

## 在本知识库中的角色

- [[Goal-Driven Execution]] 原则的**产品化落地证据**
- 与 [[Claude Code]] 形成"OpenAI vs Anthropic CLI Agent"对照轴

## 相关资料

- [[20260407-知乎-Karpathy开源Agent知识库]]
- [[20260527-知乎-卡尔-淘金小镇Skill榜单情报项目]] ⭐

## 待深入

- [ ] Codex `/goal` 的具体语法和限制
- [ ] Codex vs Claude Code 在长任务上的稳定性对比
- [ ] Codex 在国内的访问方案（VPN？API 代理？）
