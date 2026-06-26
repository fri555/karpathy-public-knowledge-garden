---
type: entity
created: 2026-05-27
updated: 2026-05-27
sources:
  - "[[20260527-知乎-卡尔-淘金小镇Skill榜单情报项目]]"
tags: [软件, 平台, 后端, 数据库, 待深入]
aliases: [convex.dev]
---

# Convex

> 一句话定义:云端数据库 + 后端函数平台——前端打开页面后通过 query path 取数据,被很多网站(如 [[ClawHub]])用作 BaaS 后端,可被复刻调用。

## 基本信息

- **类型**:BaaS / 云数据库 + 后端函数平台
- **数据访问方式**:前端通过 `query path` 调后端函数(如 `skills:listPublicPageV4`)
- **关联实体**:[[ClawHub]](使用 Convex)
- **关联概念**:[[复刻用户视角拿数据]]

## 关键事实

- 在 [[淘金小镇]] 的开发故事里被识别为"金矿入口"——前端打开网页时直连 Convex 后端,稍加抓包就能复刻 (来源: [[20260527-知乎-卡尔-淘金小镇Skill榜单情报项目]])
- 典型分页模式:`numItems` 控制每页条数,`nextCursor` 翻页书签
- 支持过滤参数:如 `sort` / `dir` / 业务字段(`nonSuspiciousOnly`)

## 在本知识库中的角色

- 是"现代网站为什么容易被抓"的代表答案——前端直调后端 → 接口暴露 → 可被复刻
- 教育意义:遇到反爬时**先看是不是 Convex/GraphQL/REST 接口**,优于 DOM 抓取

## 待深入

- [ ] Convex 是不是所有网站都用?如何识别?
- [ ] 是否有现成工具列出"用 Convex 的热门网站"
