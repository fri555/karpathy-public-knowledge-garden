---
type: entity
created: 2026-06-01
updated: 2026-06-01
sources:
  - "[[../summaries/20260601-掘金-LangGraph+RAG长文档生成4个工程踩坑.md]]"
tags: [项目, 开源, 长文档生成, LangGraph, RAG]
aliases: [OpenSpec 开源项目]
---

# OpenSpec（AI 长文档生成平台）

## 概述

OpenSpec 是一个基于 LangGraph 多智能体架构的 AI 长文档生成平台，由张居邪团队开发并开源。项目旨在解决建筑设计领域 50 页专业文档的自动生成问题，核心挑战包括：必须引用行业标准、每个章节都有合规要求、长上下文窗口管理。

- **项目地址**：https://github.com/zhuzhaoyun/OpenSpec
- **开源协议**：（原文未明确标注）
- **发布时间**：2026 年 2 月

## 核心论点

> _"做 AI 长文档生成这大半年，最大的感受是：核心难点不在模型能力，而在工程架构。选什么模型、用什么框架，这些决策一两天就能定下来。但 Token 怎么省、检索质量怎么稳定、Prompt 怎么高效迭代、流式输出怎么做到丝滑——这些工程问题，每一个都需要反复试错和打磨。没有银弹，都是一个个方案堆出来的。"_

## 整体架构：Nginx 分流，双引擎并行

```
用户 → Vue3 前端 → Nginx
                        ├─ /api/* ──→ Spring Boot（业务处理：文档/用户/项目管理，PostgreSQL）
                        └─ /agent/* ──→ FastAPI AI 引擎
                                         ├── LangGraph（工作流编排）
                                         ├── RAGFlow（知识库检索）
                                         ├── DashScope/Qwen（LLM）
                                         └── Langfuse（可观测性）
```

**架构决策理由**：SSE 流式输出经过 Java 后端转发后延迟明显增大，Spring Boot 处理长连接不是强项。Nginx 分流让 AI 生成流直接推到前端，延迟最低，业务逻辑和 AI 逻辑完全解耦。

**部署方式**：4 个 Docker 容器（Web/Nginx + Backend + Agent + PostgreSQL），`docker-compose up` 一键启动。

## 为什么选 LangGraph（vs CrewAI/AutoGen）

| 核心特性 | 选型理由 |
|----------|----------|
| **确定性边和护栏** | 专业文档生成不能"随机发挥"，每一步需要可控、可追踪、可回溯。LangGraph 有状态图（Stateful Graph）天然支持 |
| **持久化检查点** | 50 页文档按章节生成，每章完成后状态写入 PostgreSQL 作为 checkpoint。中途出错可从断点恢复 |
| **原生流式支持** | `astream_events` 提供 token 级别流式输出，配合 SSE 推送到前端 |

## 多智能体工作流：写、查、审分离

**单 Agent 问题**：会"自说自话"——生成内容通顺，但可能引用不存在的标准条款，遗漏合规要求。

**三角色分工**：

```
Router（意图路由）
  ├── 文档生成链路：
  │   Researcher（知识库检索 + 上下文收集）
  │       ↓
  │   Generator（章节内容生成）
  │       ↓
  │   Auditor（质量审核）→ 不合格 → 回到 Researcher 重新检索
  │                     → 合格 → 输出最终内容
  │
  └── General Agent（通用对话）
```

**三角色职责清晰**：
- **Researcher**：只负责从知识库检索相关标准和案例，不做内容生成
- **Generator**：基于 Researcher 提供的上下文生成章节内容
- **Auditor**：审核生成内容是否符合要求，不合格则打回重来

**防止无限循环烧 Token 的护栏**：

```python
MAX_RESEARCH_LOOPS = 3       # Researcher 最多循环 3 次
MAX_AUDIT_LOOPS = 2          # Auditor 最多审核 2 次
MAX_AUDITOR_TOOL_CALLS = 5   # Auditor 单次工具调用上限
```

> _"实测下来，大部分章节 1-2 轮就能通过审核。"_

## 四个工程踩坑与解决方案

### 踩坑 1：上下文窗口管理——动态 Token 预算

**问题**：生成 50 页文档，如果把所有已生成章节都塞进上下文，很容易超出模型最大输入长度。

**解决方案：动态 Token 预算**

每次 LLM 调用前先计算固定开销（问题 + 模板 + 项目信息 + Prompt + 响应预留），剩余空间才是可用的检索上下文窗口。

**三个关键策略**：
1. **ToolMessage 裁剪**：上下文最多保留 30 条 ToolMessage，超出的按时间顺序丢弃
2. **中文 Token 估算优化**：Qwen 模型对中文切分和 tiktoken 有差异，系数校准（中文字符 ×1.2，英文单词 ×1.3）
3. **Langfuse 成本追踪**：每次 LLM 调用都记录 input/output token 数和对应成本

**实测效果**：上下文长度压缩约 70%，长文档生成全程不会触发 Token 超限。

### 踩坑 2：RAG 检索质量——三层方案解决召回率不稳定

**问题**：直接用 RAG 检索行业标准，召回率忽高忽低。有时候明明知识库里有相关内容，就是检索不出来。

**三层解决方案**：

1. **知识库分类**：案例库和标准库分开存储、分开检索，避免不同类型的文档互相干扰
2. **相似度阈值 + 最小内容阈值**：相似度低于 0.55 的结果直接过滤；检索内容总量低于 1000 字符时触发二次检索
3. **个人模板知识库**：用户可以上传自己的文档模板，系统优先匹配用户模板的结构和风格

### 踩坑 3：Prompt 管理——从硬编码到 Langfuse 版本管理

**问题**：早期 Prompt 硬编码在 Python 代码里，每次调整都要改代码、重新构建 Docker 镜像、重新部署。

**解决方案：Langfuse 做 Prompt 的版本管理和运行时加载**

三大好处：
1. 改完 Prompt 在 Langfuse 后台保存，线上立即生效，不用重新部署
2. 每个版本自动保存历史，出了问题随时回滚
3. 完整的调用链路追踪——每次 LLM 调用关联到具体的 Prompt 版本

### 踩坑 4：流式输出——让用户看到生成过程

**问题**：长文档按章节生成，单个章节的生成时间从几秒到几十秒不等。没有实时反馈的话，用户体验很差。

**解决方案：SSE + LangGraph astream_events + 工作流进度事件**

- 用 SSE（Server-Sent Events）做流式推送
- 前端直连 FastAPI Agent 服务
- **关键体验优化**：除了 token 流，还推送工作流进度事件——用户能看到当前处于哪个阶段

> _"这个细节对用户体验的提升比想象中大。"_

## 技术栈全景

| 层级 | 技术选型 |
|------|----------|
| 前端 | Vue 3 + TypeScript + Vite + Element Plus |
| 业务后端 | Spring Boot 3 + Java 17 + MyBatis Plus |
| AI 引擎 | FastAPI + LangGraph + LangChain + DashScope (Qwen) |
| 知识库 | RAGFlow |
| 可观测性 | Langfuse（Prompt 管理 + 调用追踪 + 成本分析） |
| 存储 | PostgreSQL（业务数据 + LangGraph checkpoint） |
| 部署 | Docker Compose，4 个容器，Nginx 做路由分发 |

## 核心启示总结

**四个核心工程经验**：
1. **架构解耦**：AI 逻辑和业务逻辑分开走，Nginx 分流，SSE 流直接推送到前端
2. **多角色分离**：Researcher/Generator/Auditor 三角色分工，加护栏防烧 Token
3. **动态 Token 预算**：上下文窗口管理是长文档场景的必选项
4. **Prompt 版本化**：别硬编码 Prompt，用 Langfuse 这类工具做版本管理和运行时加载

## 关联内容

- [[LangGraph]] —— 工作流编排框架
- [[RAGFlow]] —— 知识库检索系统
- [[Langfuse]] —— 可观测性平台
- [[三角色分离工作流]] —— 本文提出的核心工作流模式
- [[动态 Token 预算]] —— 长文档上下文管理方法
- [[Prompt 版本化管理]] —— Prompt 工程化最佳实践
- [[双引擎架构]] —— Nginx 分流架构模式

---

*OpenSpec 是 2026 年 AI 长文档生成领域的代表性开源项目，其工程实践对同类项目有重要参考价值。*
