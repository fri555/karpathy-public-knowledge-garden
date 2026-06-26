---
type: entity
created: 2026-06-01
updated: 2026-06-01
sources:
  - "[[../summaries/20260601-知乎-Harness不是目的知识才是护城河-AITeam知识沉淀实践.md]]"
  - "[[../summaries/20260601-掘金-LangGraph+RAG长文档生成4个工程踩坑.md]]"
tags: [工具, 可观测性, Prompt管理, 成本分析]
aliases: []
---

# Langfuse（LLM 可观测性平台）

## 概述

Langfuse 是一个 LLM 应用的可观测性和管理平台，核心功能包括：Prompt 版本管理、调用链路追踪、成本分析。它是 2026 年 AI 应用工程化落地的重要工具之一。

## 核心功能

### 1. Prompt 版本管理

**问题背景**：Prompt 调优是高频操作，一天改十几次很正常。如果 Prompt 硬编码在代码里，每次调整都要改代码、重新构建 Docker 镜像、重新部署，迭代效率极低。

**Langfuse 解决方案**：

```python
class PromptManager:
    """Langfuse Prompt 管理器（单例模式）"""

    def get_prompt(self, prompt_name, label=None):
        target_label = label or self.default_label  # 默认 "latest"
        return self.langfuse.get_prompt(prompt_name, label=target_label)

# 运行时动态加载，支持变量编译
prompt = prompt_manager.get_prompt("construction_agent_system")
full_prompt = prompt.compile(
    context=context,
    question=question,
    template=template
)
```

**三大好处**：
1. **即时生效**：改完 Prompt 在 Langfuse 后台保存，线上立即生效，不用重新部署
2. **版本回滚**：每个版本自动保存历史，出了问题随时回滚
3. **链路追踪**：每次 LLM 调用关联到具体的 Prompt 版本，排查问题可精确定位

### 2. 调用链路追踪

- 每次 LLM 调用自动记录输入输出
- 关联到具体的 Prompt 版本
- 支持按用户、按项目、按时间段筛选
- 可视化展示调用链和耗时

### 3. 成本分析

- 自动记录每次调用的 input/output token 数
- 按项目、按章节、按时间段统计成本
- 支持多模型定价配置
- 识别成本热点（哪类任务 token 消耗最大）

### 4. Token 成本追踪

在长文档生成场景中，Langfuse 与动态 Token 预算机制配合使用：

> _"每次 LLM 调用都记录 input/output token 数和对应成本，方便按项目、按章节分析费用。"_

## 典型使用场景

### 场景 1：多 Agent 系统的 Prompt 管理

在 Researcher/Generator/Auditor 三角色分离的系统中，每个角色有独立的 Prompt，通过 Langfuse 统一管理和版本控制。

### 场景 2：A/B 测试 Prompt 效果

不同 label 的 Prompt 可以同时在线，通过 Langfuse 追踪不同版本的输出质量和 token 消耗，选择最优版本。

### 场景 3：问题回溯定位

用户反馈某段生成内容有问题时，可以通过 Langfuse 回溯到具体的 Prompt 版本、输入参数、模型版本，快速定位根因。

## 技术架构

Langfuse 通常以以下三种方式部署：

1. **SaaS 版本**：langfuse.com，开箱即用，适合中小团队
2. **自托管版本**：Docker 一键部署，适合企业内网
3. **开源核心**：核心代码开源，可二次开发

## 与其他工具的对比

| 工具 | 核心定位 | Prompt 管理 | 成本追踪 | 开源 |
|------|----------|-------------|----------|------|
| **Langfuse** | 全链路可观测性 | ✅ 版本管理 + 运行时加载 | ✅ 详细统计 | ✅ |
| **LangSmith** | LangChain 生态工具 | ✅ | ✅ | ❌ |
| **Helicone** | OpenAI 专用代理 | ❌ | ✅ | ✅ |

## 在本知识库中的出现场景

Langfuse 在两篇实践文章中被提及：

1. **OpenSpec 长文档生成项目**——用 Langfuse 做 Prompt 版本管理和成本追踪
2. **AI Team 知识沉淀实践**——作为可观测性工具提及

## 关联概念

- [[Prompt 版本化管理]] —— 基于 Langfuse 的 Prompt 管理最佳实践
- [[动态 Token 预算]] —— 与 Langfuse 成本追踪配合使用
- [[上下文预算控制]] —— 整体的上下文管理理念
- [[Harness Engineering]] —— LLM 应用工程化的整体范畴

---

*Langfuse 是 2026 年 AI 应用从"能用"到"能上线"的必备工程化工具之一。*
