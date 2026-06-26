---
type: entity
created: 2026-05-26
updated: 2026-05-28
sources:
  - "[[20260526-知乎-CLAUDE.md神文件让ClaudeCode听话]]"
  - "[[20260526-GitHub-andrej-karpathy-skills原仓库]]"
  - "[[20260528-Shareuhack-CLAUDE四层架构实战]]"
tags: [工具, 案例, prompt工程, 方法论, llm, agent, claude, cursor, 已验证]
aliases: [CLAUDE.md 神文件, Claude Code 指令文件, andrej-karpathy-skills]
---

# CLAUDE.md

> 一句话定义:[[forrestchang]] 编写的、放在代码仓库根目录的 **2.3KB markdown 指令文件**,用 **4 条核心原则**系统性矫正 [[Claude Code]] / [[Cursor]] 等 AI 编程助手的行为偏差。GitHub **15.5 万 star**(截至 2026-05-26),登顶全球热榜。

## 基本信息

- **类型**:Prompt 工程产物 / Agent 指令文件 / Claude Code 插件
- **作者**:[[forrestchang]](Jiayuan Zhang)
- **大小**:**2,357 字节**(2.3 KB)
- **格式**:Markdown
- **位置**:代码仓库根目录(Claude Code / Cursor 启动时自动加载)
- **仓库**:https://github.com/multica-ai/andrej-karpathy-skills(原 forrestchang/andrej-karpathy-skills)
- **现归属**:[[Multica|multica-ai]] 组织
- **创建**:2026-01-27
- **License**:MIT
- **关联实体**:[[forrestchang]] · [[Multica]] · [[Claude Code]] · [[Cursor]] · [[Andrej Karpathy]] · [[GitHub]]
- **关联概念**:[[LLM 编程三宗罪]] · [[Think Before Coding]] · [[Simplicity First]] · [[Surgical Changes]] · [[Goal-Driven Execution]] · [[原则化指令]]

## 4 条核心原则(基于 GitHub 一手源,完整版)

> 开篇 tradeoff 声明:**These guidelines bias toward caution over speed. For trivial tasks, use judgment.**

| # | 原则 | 一句话 | 对应 Karpathy 观察 |
|---|---|---|---|
| 1 | **[[Think Before Coding]]** | Don't assume. Don't hide confusion. Surface tradeoffs. | 默默做错误假设 + 不管理困惑 |
| 2 | **[[Simplicity First]]** | Minimum code that solves the problem. Nothing speculative. | 把简单问题复杂化 |
| 3 | **[[Surgical Changes]]** | Touch only what you must. Clean up only your own mess. | 改动/删除无关代码 |
| 4 | **[[Goal-Driven Execution]]** | Define success criteria. Loop until verified. | "给它成功标准,看着它完成" |

> **重要修正**:前 3 条对应 Karpathy 提的"3 个 LLM 缺陷",**第 4 条对应另一个不同的观察——LLM 的优势**(循环执行至目标达成)。所以并不是"三宗罪 → 四原则凑数",而是 **3 防错 + 1 激发优势** 的完整组合。

## 设计哲学

- **极简**:仅 2.3KB,4 条原则
- **抓本质**:每条原则有副标题 + 3-5 条子条款 + 1 个检验标准
- **承认 tradeoff**:开篇就声明"偏向 caution 而非 speed",琐碎任务自己判断
- **可工程化交付**:不只是 markdown,还有 Claude Code 插件清单(`.claude-plugin/`)、Cursor 规则(`.cursor/`)、14.8KB 案例库(EXAMPLES.md)

## 关键事实

- GitHub star:**155,338**(截至 2026-05-26),fork **15,932** (来源: [[20260526-GitHub-andrej-karpathy-skills原仓库]])
- 知乎二手文章引用的"10.2 万 star"已过时,实际增长到 15.5 万
- 作用机制:Claude Code 启动时自动读取仓库根目录的 CLAUDE.md,作为系统级指令注入
- 安装方式三种:Claude Code 插件市场 / curl 直接拉取 / Cursor 自动加载 `.cursor/rules/`

## 在本知识库中的角色

- 是 [[LLM Wiki]] 哲学在"Agent 行为规训"维度的典型实践
- 与本知识库 [[../../AGENT|AGENT.md]] 协议同源同构——都是"用少量原则代替详细规则"
- **第 4 条 Goal-Driven Execution 可反向启发本协议**:把 ingest/maintain 流程从"步骤式"改成"目标 + 验证循环"

## ⭐ 2026-05-28 重要补全：CLAUDE.md 在四层架构中的定位

来自 [[Shareuhack]] 6-Agent fleet 实战 (来源: [[20260528-Shareuhack-CLAUDE四层架构实战]])：

**CLAUDE.md 不是 README，是行为宪法**——但它**只是 Claude Code 完整配置的 4 层之一**：

| 层 | 职责 | 不该放什么 |
|---|---|---|
| **CLAUDE.md** | 行为规则、禁止事项、架构 | 步骤型指令（用 Skills）|
| Skills | 可执行 SOP | 永久规则（放 CLAUDE.md）|
| Hooks | 强制执行 | 灵活判断（那是 AI 的事）|
| Memory | 跨 session 状态 | 不变规则（放 CLAUDE.md）|

之前本页只讲 forrestchang 的"4 条原则"，本次补全了 CLAUDE.md **在整个 Claude Code 配置体系中的层级定位**。详见 [[../concepts/CLAUDE.md四层架构|CLAUDE.md 四层架构]]。

**三层优先级**：global(`~/.claude/`) → project(`{proj}/`) → local(`CLAUDE.local.md`)
**路径作用域**：`.claude/rules/frontend.md` 只在处理前端文件时载入（[[../concepts/路径作用域规则|路径作用域规则]]）
**长度阈值**：> 300 行该拆 .claude/rules/；超过 5000 行无法正常运作

## 相关资料

- [[20260526-GitHub-andrej-karpathy-skills原仓库]] —— 一手源(权威)
- [[20260526-知乎-CLAUDE.md神文件让ClaudeCode听话]] —— 二手解读(已被一手源补全)
- [[20260528-Shareuhack-CLAUDE四层架构实战]] —— CLAUDE.md 在四层架构中的定位

## 待深入

- [ ] 单独 ingest EXAMPLES.md(14.8KB 案例库)
- [ ] 抓 Karpathy 原始推文 ID 2015883857489522876 的英文原文
- [ ] 把 CLAUDE.md 抄一份放进先生的开发工作流?
- [ ] 写"CLAUDE.md vs 本知识库 AGENT.md"设计哲学对比综述
