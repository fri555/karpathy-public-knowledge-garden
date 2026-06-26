---
type: entity
created: 2026-05-27
updated: 2026-05-27
sources:
  - "[[20260527-知乎-卡尔-淘金小镇Skill榜单情报项目]]"
tags: [软件, 平台, ai, agent, skill, 市场, 待深入]
aliases: [Claw Hub, clawhub.ai]
---

# ClawHub

> 一句话定义:[[Claude Code]] 生态的 Skill 市场,允许开发者上传/下载/排行 Agent Skill,被 [[淘金小镇]] 作为榜单情报源每日抓取。

## 基本信息

- **类型**:Skill 市场 / 平台
- **域名**:clawhub.ai
- **核心 URL**:`clawhub.ai/skills?sort=downloads`
- **后端**:基于 [[Convex]] 云数据库 + 后端函数
- **关键 API**:`skills:listPublicPageV4`(分页 25/页,`nextCursor` 翻页)
- **关联实体**:[[Claude Code]] · [[淘金小镇]]
- **关联概念**:[[Skill 榜单情报化]]

## 关键事实

- 是 [[淘金小镇]] 的唯一数据源 (来源: [[20260527-知乎-卡尔-淘金小镇Skill榜单情报项目]])
- 没有官方公开 API,但前端是直连 Convex 后端的——可被复刻
- 提供"非可疑"过滤(`nonSuspiciousOnly=true`)——平台已经在做内容审核
- 上面有多种 Skill 类型:UI 设计、HTML PPT、Polymarket 预测市场、Agent 上下文管理、Self-Improving Agent、Proactive Agent 等

## 在本知识库中的角色

- 是当前(2026-05)最重要的**第三方 Skill 市场之一**
- 与 [[Multica]] 平台并列为"Skill 生态承载者"——但 Multica 还小,ClawHub 已成熟
- 是先生潜在的工具栈来源,也是 AI 工具趋势观察窗口

## 待深入

- [ ] 是否提供官方 API/文档?是否需要登录?
- [ ] Skill 提交流程、审核机制
- [ ] 头部 Skill 是哪些?
- [ ] 是否值得收录到先生的"AI 工具栈情报源"
