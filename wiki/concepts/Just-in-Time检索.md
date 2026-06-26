---
type: concept
created: 2026-06-01
updated: 2026-06-01
sources:
  - "[[../summaries/20260929-Anthropic-Effective context engineering for AI agents]]"
tags: [方法论, agent, llm, context, anthropic, 一手源, 已验证]
aliases: [JIT Retrieval, Just-in-Time Context, 按需检索]
---

# Just-in-Time 检索

> 一句话定义：Agent 不预先加载所有可能相关的数据，而是维护轻量标识符（文件路径、查询、链接），在运行时按需动态加载数据到 context——类比人类用文件系统/书签而非记忆全部内容。

## 核心要义

[[../entities/Anthropic|Anthropic]] 在 [[上下文工程]] 中提出的核心检索范式，作为传统 RAG 的进化方向。

传统 RAG：embedding 预计算 → 向量检索 → 重排 → 注入 context（推理前全量准备）
Just-in-Time：Agent 维护指针 → 运行时用工具按需读取 → 只加载必要的部分

Claude Code 是此模式的典范：用 glob/grep 搜索文件系统 + Bash 命令分析大数据，而不是把整个代码库预加载。

## 关键要素

- **轻量标识符**：文件路径、存储查询、URL 等，只占极少 token (来源: [[../summaries/20260929-Anthropic-Effective context engineering for AI agents]])
- **工具驱动**：Agent 用工具（如文件读取、SQL 查询、HTTP 请求）获取实际数据 (同上)
- **元数据信号**：文件名、目录结构、时间戳本身就是信息 (同上)
- **渐进发现**：见 [[渐进式披露]] (同上)
- **Hybrid 策略**：CLAUDE.md 前置（预计算）+ glob/grep just-in-time = 混合模式 (同上)

## 与相关概念的关系

- 与 [[上下文工程]]：本概念是 context engineering 的检索策略
- 与 [[上下文腐烂]]：按需检索避免无关 token 进入 context，减缓腐烂
- 与 [[RAG]]：JIT 是 RAG 的进化方向，不是完全替代——hybrid 可能更好
- 与 [[渐进式披露]]：JIT 是检索机制，渐进披露是用户体验
- 与 [[Prompt Cache局部性]]：JIT 不改前缀，对 cache 友好

## 典型应用 / 案例

- [[../entities/Claude Code|Claude Code]]：CLAUDE.md 前置 + glob/grep just-in-time (来源: [[../summaries/20260929-Anthropic-Effective context engineering for AI agents]])
- [[../entities/OpenClacky|OpenClacky]] 的 `invoke_skill`：Skill 按需载入，不占主工具列表 (来源: [[../summaries/20260514-RubyChina-OpenClacky-Harness工程7个关键决策]])
- 本知识库：[[三层架构]] 的 raw/ 只读 + wiki/ 按需读取 = JIT 模式 (来源: 自我观察)

## 争议 / 局限

- 运行时探索比预计算慢
- Agent 可能"用错工具"浪费 context
- 纯 JIT 在非动态内容场景（法律/金融）可能不够

## 相关资料

- [[../summaries/20260929-Anthropic-Effective context engineering for AI agents]]

## 待深入

- [ ] Claude Code auto-compact 的 95% 阈值实现细节
- [ ] 本库是否可以更 JIT——哪些 wiki 页可以不在启动时加载
