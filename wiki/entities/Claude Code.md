---
type: entity
created: 2026-05-24
updated: 2026-05-28
sources:
  - "[[20260407-知乎-Karpathy开源Agent知识库]]"
  - "[[20260526-知乎-CLAUDE.md神文件让ClaudeCode听话]]"
  - "[[20260525-知乎-Claude永久大脑真的来了]]"
  - "[[20260528-Shareuhack-CLAUDE四层架构实战]]"
tags: [工具, ai, agent, llm, anthropic, claude]
aliases: []
---

# Claude Code

> 一句话定义：[[Anthropic]] 推出的 CLI 编码 Agent，是 [[Andrej Karpathy]] 本人在 [[LLM Wiki]] 工作流中使用的主力工具之一。

## 基本信息

- **类型**：CLI Agent / 编码助手
- **厂商**：[[Anthropic]]
- **关联实体**：[[Codex]]（同类）· [[Qwen Code]]（国产替代）
- **关联概念**：[[LLM Wiki]] · [[Ingest 录入]] · [[Maintain 维护]]

## 关键事实

- Karpathy 自己日常使用的 Agent 之一 (来源: [[20260407-知乎-Karpathy开源Agent知识库]])
- 社区已有人为 Claude Code 做了 LLM Wiki 的 skill，一行命令即可装上、直接 ingest 来源
- 可一次性修改 15 个文件而不出错——契合 LLM Wiki 高频跨页编辑的需求
- 在代码仓库根目录放一个 [[CLAUDE.md]] 文件可以系统性矫正其行为偏差,是 Claude Code 用户的官方推荐 prompt 注入方式 (来源: [[20260526-知乎-CLAUDE.md神文件让ClaudeCode听话]])
- 用过 Claude Code 的开发者普遍能识别出 [[LLM 编程三宗罪]] 中的三个典型毛病——这正是 [[CLAUDE.md]] 神文件能爆红的群众基础
- **[[Dreams]] 首发载体**：Anthropic 的「Auto Dream」功能已在 Claude Code 上线，触发条件为 ≥5 次对话 OR >24h，也可手动 `/dream` (来源: [[20260525-知乎-Claude永久大脑真的来了]])
- 2026-03 底 Anthropic 意外泄露的 **51.2 万行 Claude Code 源码** 首次揭开了 [[Conway]] 的面纱

## 在本知识库中的角色

本知识库选择"方案 A"——由 [[Hana]]（基于 Claude 的助手）直接扮演 Agent 角色，未走 Claude Code CLI 路径，但底层模型同源。

## ⭐ 2026-05-28 补全：完整配置 = 四层架构

来自 [[Shareuhack]] 6-Agent fleet 实战（来源: [[20260528-Shareuhack-CLAUDE四层架构实战]]）：

Claude Code 的完整配置体系不是 [[CLAUDE.md]] 一个文件，而是 **[[CLAUDE.md四层架构|四层架构]]**：

1. **[[CLAUDE.md]]** — 行为宪法（session 全量载入）
2. **[[Skills 2.0模块化|Skills]]** — 可执行 SOP（on-demand 载入）
3. **[[Hooks确定性执行|Hooks]]** — 强制执行法（确定性 shell 兜底）
4. **[[三套记忆系统|Memory]]** — 学习记录（CLAUDE.md / Auto Memory / Session Memory 三层）

**关键洞察**：Hooks 是把"建议"变成"法律"的唯一机制——CLAUDE.md 写"每次跑测试"遵守率不稳定，Stop Hook 强制 100% 执行。

## 相关资料

- [[20260407-知乎-Karpathy开源Agent知识库]]
- [[20260413-知乎-Qwen Code+Obsidian搭建Karpathy知识库]] — 提供了 Qwen Code 的替代路径
- [[20260526-知乎-CLAUDE.md神文件让ClaudeCode听话]] — 介绍如何用 [[CLAUDE.md]] 规训其行为
- [[20260525-知乎-Claude永久大脑真的来了]] — Auto Dream / 源码泄露 / Conway 揭面纱

## 待深入

- [ ] 那个 Claude Code 的 LLM Wiki skill 具体在哪？叫什么？
- [ ] [[forrestchang]] 的 CLAUDE.md 完整 4 条原则是什么(目前只读到前 2 条) — ⚠️ 注意：另一个会话已 ingest 一手源补全，见 [[entities/CLAUDE.md]]
- [ ] Auto Dream 在 Claude Code 中的完整文档
