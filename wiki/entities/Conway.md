---
type: entity
created: 2026-05-26
updated: 2026-05-26
sources:
  - "[[20260525-知乎-Claude永久大脑真的来了]]"
tags: [产品, ai, agent, claude, anthropic, 平台, 待验证]
aliases: [Claude Conway, CNW]
---

# Conway

> 一句话定义：[[Anthropic]] 在研的**永不下线 Agent 平台**——独立运行环境、监听外部事件、操控浏览器，把 [[Memory Files]] + [[Dreams]] 拼成完整闭环。

## 基本信息

- **类型**：产品 / Agent 平台
- **厂商**：[[Anthropic]]
- **状态**：灰度测试中（已在 Claude 界面侧边栏出现独立入口）
- **代号**：CNW（Conway 缩写）
- **关联实体**：[[Memory Files]]（存储基座）· [[Dreams]]（维护基座）· [[Claude Code]]（可运行）· [[OpenClaw]]（对标）

## 核心定位

> Conway 不是一个更智能的聊天窗口，而是一个完全不同品类的产品。

颠覆当前所有 AI 助手的「被动式」范式：用户输入提示词 → AI 回复 → 对话结束。Conway 是**主动式 / 常驻式**。

## 三大功能区

| 区 | 中文 | 职责 |
|---|---|---|
| Search | 搜索 | 信息检索 |
| Chat | 对话 | 即时交互 |
| System | 系统 | 任务编排、外部事件、自动化 |

## 关键能力

- 常驻后台运行（24/7）
- 监听外部事件
- 主动触发任务
- 通过 Webhook 接收信号
- 操控浏览器
- 运行 [[Claude Code]]

## 历史时间线

- `2026-03 底` — Anthropic 意外泄露 51.2 万行 Claude Code 源码，首次揭开 Conway 面纱
- `2026-05 月初` — Code with Claude 大会披露相关能力
- `2026-05-25` — TestingCatalog 证实 Conway 存在，灰度入口在 Claude 侧边栏出现

## 与 OpenClaw 的对比（来源: [[20260525-知乎-Claude永久大脑真的来了]]）

| 维度 | OpenClaw | Conway |
|---|---|---|
| 出身 | 开源 | Anthropic 原生 |
| 运行 | 用户自部署 | Anthropic 托管云 |
| 扩展 | 自由安装 | 必须显式安装 |
| Webhook | 自由配置 | 可逐服务开关 |
| 浏览器 | 自由集成 | 走 Claude 权限模型 |
| 已知漏洞 | 头两个月 ≥9 个 CVE，4.2 万实例公网裸奔 | 跑在 Anthropic 托管基础设施 |
| 安全模型 | 弱（自部署的代价） | 强（托管的好处） |

## 三件套的逻辑

> 一个永不下线的 AI 智能体，最需要什么？没错，是记忆！

- [[Memory Files]] = 存储架构
- [[Dreams]] = 维护机制
- Conway = 运行时

三块拼图拼在一起 = Conway 完整基础设施。

## 在本知识库中的角色

- 是 [[LLM Wiki]] + [[Maintain 维护]] **配上"运行时"**之后的样子
- 给本知识库提示了一个未来方向：当本库长到一定规模，是否需要一个**后台进程**（cron / Hana 定时任务）来做主动 ingest 和 maintain，而不只是被动等"知识图谱"暗号

## 相关资料

- [[20260525-知乎-Claude永久大脑真的来了]] ⭐

## 待深入

- [ ] Conway 是否会开放 API
- [ ] System 区的具体能力清单
- [ ] 与 [[OpenClaw]] 的兼容性 / 迁移成本
- [ ] Webhook 协议是否标准化
