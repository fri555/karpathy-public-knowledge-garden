---
type: entity
created: 2026-06-01
updated: 2026-06-01
sources:
  - "[[../summaries/20260601-知乎-Harness不是目的知识才是护城河-AITeam知识沉淀实践.md]]"
tags: [团队, 知识管理, Harness]
aliases: [AITeam, AI工程交付团队]
---

# AI Team（AI 工程交付团队）

## 概述

AI Team 是本文所述的一个 AI 工程交付团队，专注于 Harness Engineering 和团队知识沉淀的实践。他们在落地过程中发现：**构建 Harness 工作流不是最终目的，私域和团队知识的沉淀才是真正的技术护城河**。

## 核心理念

> _"Skill、Agent、工具链会随模型迭代更新，但领域知识是永恒的。"_

## 核心成果

### 1. 五层知识存储架构

```
Layer 0-P：个人偏好 (~/.ai-team/) —— 纯本地，不共享
Layer 0-T：团队约定 (team-conventions/) —— 团队级，Git 共享
Layer 1：技术知识 (tech-wiki/) —— 团队级，跨项目
Layer 2：业务知识 (biz-wiki/{domain}/) —— 团队级，按领域
Layer 3：项目知识 (docs/knowledge/) —— 项目级，随项目走
```

**关键设计**：知识可以"向上提升"。Layer 3 的项目知识，如果被判定为跨项目通用，会自动提升到 Layer 1 或 Layer 2。

### 2. 五种知识类型（MECE 原则）

| 类型 | 定义 |
|------|------|
| **model** | 实体定义、数据结构、关系图 |
| **decision** | 技术选型、架构决策及理由 |
| **guideline** | 推荐做法/禁止做法 |
| **pitfall** | 已知风险、故障模式、排查步骤 |
| **process** | 业务流程、状态机、操作步骤 |

### 3. 三级成熟度 + 自动衰减机制

```
draft（新提取，单一来源）
  ↓ 在 1 个工作流中被成功引用
verified（单项目验证）
  ↓ 在 ≥2 个不同项目中被验证
proven（成熟/可信赖）
```

**自动衰减规则**：
- proven 条目 12 个月未被引用 → 降级为 verified
- verified 条目 6 个月未被引用 → 降级为 draft
- draft 条目持续未引用 + Lint 标记 → 归档，移出活跃索引

### 4. 三级渐进式索引（借鉴 Karpathy LLM Wiki）

| 层级 | 大小 | 作用 |
|------|------|------|
| **Layer A：全景目录** | ~50 行 | "知识库有什么？"——分类统计 + 按阶段推荐查阅路径 |
| **Layer B：分类清单** | ~100-300 行 | "这个分类有哪些条目？"——每条一行摘要 |
| **Layer C：完整条目** | ~50-200 行/条 | "这条知识说了什么？"——完整内容 + 背景 + 适用场景 |

**效率提升**：Agent 可以用 ~50 行的成本了解知识库全貌，用 ~300 行的成本定位到相关条目。对比"一次性推送 50 条完整知识"，上下文效率提升了一个数量级。

### 5. 独立 Git 仓库架构

团队知识库是一个独立的 Git 仓库，不寄生于任何业务项目：

```
team-knowledge.git
├── knowledge-catalog.md                  ← 全景目录（Agent 查询入口）
├── .knowledge-config.yaml                ← 团队配置（成员、冲突策略）
├── team-conventions/                     ← Layer 0-T: 团队约定
├── tech-wiki/                            ← Layer 1: 技术知识
├── biz-wiki/                             ← Layer 2: 业务知识
├── project-profiles/                     ← 项目画像
└── contributions/                        ← 贡献暂存区
    ├── pending/
    └── conflicts/
```

### 6. 贡献模式：贡献暂存 + 异步合并

借鉴区块链思想：
- **不可篡改的追加日志**：log.md 只追加不修改
- **贡献可溯源**：evidence.contributors[]（类似 Git blame）
- **共识机制**：maturity 多人验证提升（draft→verified: 1人; verified→proven: ≥2人+≥2项目）

## 16 阶段状态机与知识的三通道闭环

```
INIT 阶段（知识注入）→ 各阶段执行（知识消费）→ ARCHIVE 阶段（知识提取+提升判定）
```

每个阶段的 Agent 有独立的查询预算，聚焦不同类型的知识。

## 人机交互瓶颈突破：远程操控 + 跨设备接管

**核心架构启示**：
> _"好的 Harness 工程不仅要设计'Agent 怎么跑'，还要设计'人怎么随时参与'。"_

具体到架构层面：
- **状态持久化**：文件系统即状态机，不依赖内存或特定进程
- **断点恢复**：每个阶段的入口和出口都有明确的持久化产物
- **异步审批**：人工确认节点应设计为异步模式
- **通知触达**：关键节点通过企业微信等渠道主动推送

## Lint 机制（借鉴 Karpathy LLM Wiki）

知识库不能只进不出，定期 Lint 包括：索引不一致修复、孤儿条目降级、矛盾检测、过时检测、重复检测、成熟度自动衰减。

## 关联内容

- [[三层知识索引]] —— 本文提出的核心查询机制
- [[知识成熟度模型]] —— draft → verified → proven 三级体系
- [[知识分层架构]] —— 五层知识存储设计
- [[LLM Wiki]] —— Karpathy 提出的知识库范式，本文直接借鉴
- [[OpenClacky]] —— 另一篇 Harness Engineering 实践，可与本文互相印证
