---
type: entity
created: 2026-05-26
updated: 2026-05-26
sources:
  - "[[20260526-GitHub-andrej-karpathy-skills原仓库]]"
tags: [软件, 工具, ai, agent, ide, 已验证]
aliases: [cursor.sh]
---

# Cursor

> 一句话定义:基于 VSCode 的 AI 编程 IDE,通过 `.cursor/rules/*.mdc` 加载项目级 prompt 规则——也是 [[CLAUDE.md|andrej-karpathy-skills]] 仓库的目标工具之一。

## 基本信息

- **类型**:AI 编程 IDE
- **关联实体**:[[Claude Code]](同类竞品)· [[CLAUDE.md]]
- **关联概念**:[[原则化指令]]

## 关键事实

- 通过 `.cursor/rules/*.mdc` 文件加载项目级 prompt 规则 (来源: [[20260526-GitHub-andrej-karpathy-skills原仓库]])
- [[CLAUDE.md|andrej-karpathy-skills]] 仓库自带 `.cursor/rules/karpathy-guidelines.mdc`,Cursor 打开项目时自动生效
- 详细适配说明在仓库的 [CURSOR.md](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CURSOR.md)(1.9KB)

## 在本知识库中的角色

- 作为 [[CLAUDE.md]] 神文件适用对象之一被提及
- 与 [[Claude Code]] 并列,印证"AI 编程 IDE 都需要项目级行为规训"的趋势

## 相关资料

- [[20260526-GitHub-andrej-karpathy-skills原仓库]]

## 待深入

- [ ] Cursor `.mdc` 规则文件格式 vs Claude Code CLAUDE.md 的对比
- [ ] 先生是否在用 Cursor?是否考虑接入这套 karpathy-guidelines?
