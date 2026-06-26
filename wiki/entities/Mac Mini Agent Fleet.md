---
type: entity
created: 2026-05-28
updated: 2026-05-28
sources:
  - "[[20260528-36氪-Saboo30天6Agent复盘]]"
tags: [案例, agent, 项目, llm, 已验证]
aliases: [Saboo 6-Agent fleet, 龙虾团队, Saboo Agent 团队]
---

# Mac Mini Agent Fleet

> 一句话定义：[[Shubham Saboo]] 在一台 Mac Mini 上跑的 6 个 Agent 自治系统，托管他的副业内容创作全流程——是 2026 年最广为流传的"一个人 + 一台机器 + 一支 AI 团队"实战案例。

## 基本信息

- **类型**：实战案例 / Agent 项目
- **主理人**：[[Shubham Saboo]]
- **硬件**：单台 Mac Mini
- **Agent 数**：6 个（已知名字 3 个：Kelly / Dwight / Monica）
- **持续时间**：30 天首期复盘，至今仍在运行
- **关联实体**：[[Shubham Saboo]] · [[Claude Code]]（架构同源）
- **关联概念**：[[纠错式Prompt工程]] · [[Agent团队三阶段曲线]] · [[反馈闭环写入文件]]

## 6 个 Agent 的角色（已知）

| Agent | 角色 | 关键事件 |
|---|---|---|
| **Kelly** | 运营 Agent，负责 X 账号 | 上下文从 161K 压缩到 40K，第 20 天可直接发推 |
| **Dwight** | 研究 Agent，扫行业线索 | 第 1 天 47 条 / 40 噪音 → 第 25 天 7 条全可读 |
| **Monica** | 首席运营 Agent / SRE | 监控任务心跳，>26h 未运行自动重启 |
| 其他 3 个 | 未公开 | — |

## 关键事实

- 全流程 24h 自动运转(截至 2026-02) (来源: [[20260528-36氪-Saboo30天6Agent复盘]])
- 第 4 天差点被关掉（混乱期典型症状） (来源: [[20260528-36氪-Saboo30天6Agent复盘]])
- 第 4 周开始进入"复利期"，反馈在文件中沉淀后 Agent 自动跑通 (来源: [[20260528-36氪-Saboo30天6Agent复盘]])

## 核心架构（推断 + 文章描述）

- **SOUL.md**：Agent 行为设定文件（类似 CLAUDE.md）
- **记忆文件**（BAD/GOOD）：用户偏好的样本积累
- **技能文件**：操作 SOP / 任务说明书
- **反馈闭环**：先反馈 → Agent 更新文件 → 下轮重新加载

## 在本知识库中的角色

- 实证了 Karpathy "模型 + harness" 哲学：模型不变，**harness 在 30 天里把 Agent 从废柴养成员工**
- 与 [[淘金小镇]]（卡尔）、[[CLAUDE.md]]（forrestchang）并列为本库 **Agent 工程化三大实战参照**
- 跨域启发：可借鉴到先生的电商 AI 运营场景

## 相关资料

- [[20260528-36氪-Saboo30天6Agent复盘]]

## 待深入

- [ ] 另外 3 个 Agent 的角色与具体工作流
- [ ] SOUL.md 的字段结构与示例
- [ ] 6 个 Agent 之间的协作图（文件协作机制）
