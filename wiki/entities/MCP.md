---
type: entity
created: 2026-05-28
updated: 2026-05-28
sources:
  - "[[20260528-掘金-MCP协议落地三条铁律]]"
tags: [协议, agent, llm, anthropic, 标准, 工具调用, 已验证]
aliases: [Model Context Protocol, MCP 协议]
---

# MCP

> 一句话定义：Model Context Protocol，[[Anthropic]] 在 2024-2025 年间开源的 **Agent 与外部工具/数据源通信的标准协议**，被视为 Agent 时代的"TCP/IP"。

## 基本信息

- **类型**：开放协议
- **提出方**：[[Anthropic]]
- **同类对手**：A2A（Google）/ ACP（IBM）
- **标准化推动者**：Linux 基金会下的"智能体式 AI 基金会"(截至 2026)
- **关联实体**：[[Anthropic]] · [[Claude Code]] · [[A2A]]
- **关联概念**：[[字段级权限]] · [[Agent Gateway协议翻译层]] · [[工具调用幻觉]] · [[30-70定律]]

## 核心抽象

- **MCP Server**：暴露工具/数据源给 Agent 调用
- **tools/list**：声明可用工具及参数
- **权限令牌**：会话级最小权限
- 在 2026 实战中已成为最广泛采用的 Agent-Tool 通信协议(截至 2026-05) (来源: [[20260528-掘金-MCP协议落地三条铁律]])

## 关键事实

- 不到一年从 Anthropic 开源到 Google/IBM 跟进推出竞品(截至 2026-05) (来源: [[20260528-掘金-MCP协议落地三条铁律]])
- 实战发现"搭完就完"的误区——权限粒度不够细会让模型调用不该调用的工具 (来源: [[20260528-掘金-MCP协议落地三条铁律]])
- 沙河 rain 提出权限应下沉到字段级，且检查应前置到 planning 阶段 (来源: [[20260528-掘金-MCP协议落地三条铁律]])

## 在本知识库中的角色

- 首次进入本库的"基础设施层"概念——之前都是 Agent 应用层（CLAUDE.md / Skills）
- 与 [[Claude Code]] / [[Anthropic]] 形成主线延伸
- 30/70 定律的载体：Agent 的智能 30%，连接 70% 都靠 MCP 及周边

## 相关资料

- [[20260528-掘金-MCP协议落地三条铁律]]

## 待深入

- [ ] 抓 Anthropic MCP 官方 spec 一手源
- [ ] 单独 ingest "MCP 安全实践"主题
- [ ] 调研先生公司是否需要建 MCP Server
