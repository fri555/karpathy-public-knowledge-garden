---
type: entity
created: 2026-05-24
updated: 2026-05-24
sources:
  - "[[20260413-知乎-Qwen Code+Obsidian搭建Karpathy知识库]]"
tags: [工具, obsidian插件, agent]
aliases: []
---

# obsidian-agent-client

> 一句话定义：把外部 CLI Agent（[[Qwen Code]] / [[Claude Code]] 等）嵌入 [[Obsidian]] 侧边栏的第三方插件，是"方案 B"的核心粘合剂。

## 基本信息

- **类型**：Obsidian 第三方插件
- **仓库**：https://github.com/RAIT-09/obsidian-agent-client
- **作者**：RAIT-09（GitHub）
- **安装方式**：通过 [[BRAT]] 加载 beta 插件
- **UI 特征**：侧边栏显示为 🤖 小机器人图标
- **关联实体**：[[Qwen Code]] · [[Claude Code]] · [[BRAT]] · [[Obsidian]]

## 关键事实

- 通过 BRAT 安装：在 BRAT 中输入仓库 URL → 选 Latest version → Add plugin (来源: [[20260413-知乎-Qwen Code+Obsidian搭建Karpathy知识库]])
- 支持 "Add custom agent" 配置任意 CLI agent 作为后端
- 自动检测 [[Node.js]]，也可手动指定路径
- 作者反馈"下载文件安装可能有连不上 qwen 的问题"，故推荐 BRAT 路径

## 在本知识库中的角色

本知识库选择"方案 A"，未启用本插件。如果先生未来想升级到"方案 B"（Agent 常驻 Obsidian），这是关键依赖。

## 风险提示

- 第三方插件，需关注维护活跃度（RAIT-09 仓库）
- Beta 状态，需通过 BRAT 而非官方插件市场安装

## 相关资料

- [[20260413-知乎-Qwen Code+Obsidian搭建Karpathy知识库]]

## 待深入

- [ ] 该插件是否支持 Anthropic API 直连（绕过 CLI）
- [ ] 当前 Star 数 / 维护活跃度
