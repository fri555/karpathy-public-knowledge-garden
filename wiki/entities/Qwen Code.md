---
type: entity
created: 2026-05-24
updated: 2026-05-24
sources:
  - "[[20260413-知乎-Qwen Code+Obsidian搭建Karpathy知识库]]"
tags: [工具, ai, agent, llm, 阿里, 国产]
aliases: []
---

# Qwen Code

> 一句话定义：阿里通义千问推出的 CLI 编码 Agent，是国内用户搭建 [[LLM Wiki]] 时 [[Claude Code]] / [[Codex]] 的国产替代。

## 基本信息

- **类型**：CLI Agent / 编码助手
- **厂商**：阿里 / 通义千问
- **官网**：https://qwen.ai/qwencode
- **关联实体**：[[Claude Code]] · [[Codex]] · [[obsidian-agent-client]]
- **关联概念**：[[LLM Wiki]] · [[AGENT.md 协议]]

## 关键事实

- 安装方式：以管理员身份打开命令行，输入官网提供的安装指令 (来源: [[20260413-知乎-Qwen Code+Obsidian搭建Karpathy知识库]])
- 安装时会自动带上 [[Node.js]] 运行环境
- 可作为 [[obsidian-agent-client]] 的后端 agent，把 Agent 嵌进 Obsidian 侧边栏
- 对国内网络更友好——这是 [[菠萝吹雪]] 用它替换 Claude Code 的核心动机

## 在本知识库中的角色

本知识库选择"方案 A"未启用 Qwen Code。但如果先生未来想升级到"方案 B"（在 Obsidian 内常驻 agent），Qwen Code 是首选后端。

## 相关资料

- [[20260413-知乎-Qwen Code+Obsidian搭建Karpathy知识库]]

## 待深入

- [ ] Qwen Code 与 Claude Code 在执行 [[Ingest 录入]] / [[Maintain 维护]] 任务时的能力差异
