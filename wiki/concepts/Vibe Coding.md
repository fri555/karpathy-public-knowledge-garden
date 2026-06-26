---
type: concept
created: 2026-06-01
updated: 2026-06-25
sources:
  - "[[../summaries/20260506-SimonWillison-Vibe coding and agentic engineering]]"
  - "[[../summaries/20260622-SimonWillison-Porting-Moebius-model-to-browser]]"
tags: [方法论, agent, llm, coding, 一手源, 已验证]
aliases: [Vibe Coding, 氛围编程]
---

# Vibe Coding

> 一句话定义：[[../entities/Andrej Karpathy|Karpathy]] 2025 年 3 月提出的术语——用 AI 写代码时**完全不看代码**，只看运行结果；不工作就告诉模型不工作，碰运气让它修。

## 核心要义

Simon Willison 把 Vibe Coding 与 [[Agentic Engineering]] 严格区分：
- Vibe Coding：不审代码，可能不懂编程，要的是结果
- Agentic Engineering：专业工程师用 AI 工具，关心质量、安全、维护性

**Vibe Coding 不是错——而是有适用场景**：个人小工具，出 bug 只伤自己时完全没问题。但给别人用的软件用 vibe coding 就是不负责任——别人会被你的 bug 伤到。

2026 年 5 月 Willison 的反思：**这个边界正在模糊**——Agent 太可靠了，他自己也开始不审代码，触发 [[规范偏差正常化]] 风险。

## 关键要素

- **不审代码**：核心特征 (来源: [[../summaries/20260506-SimonWillison-Vibe coding and agentic engineering]])
- **结果导向**：能跑就行 (同上)
- **试错驱动**：不工作就让 AI 改，碰运气 (同上)
- **适用边界**：个人工具/原型 OK，生产/给别人用 NOT OK (同上)

## 与相关概念的关系

- 与 [[Agentic Engineering]]：本概念的对立面（也是正在模糊的对立面）
- 与 [[LLM 编程三宗罪]]：Vibe Coding 不防范三宗罪
- 与 [[规范偏差正常化]]：长期 Vibe Coding 的风险
- 与 [[Goal-Driven Execution]]：GDE 的循环验证可以作为 Vibe Coding 的轻量级兜底

## 典型应用 / 案例

- Willison 自述：他用 Claude Code 写 JSON API 端点时已不审代码 (来源: [[../summaries/20260506-SimonWillison-Vibe coding and agentic engineering]])
- 反例：Matthew Yglesias 说"我不想 vibecode——我想让专业软件公司用 AI 做更好的产品卖给我" (同上)
- **Moebius 浏览器移植**（2026-06-22）：Simon Willison 用 Claude Code 将 PyTorch 图像 inpainting 模型完整移植到浏览器 WebGPU，全程未看一行代码 (来源: [[../summaries/20260622-SimonWillison-Porting-Moebius-model-to-browser]])。特征：\n  - 作者完全不懂 ONNX/WebGPU，依赖 Claude Opus 4.8 完成全部技术工作\n  - 1.24GB ONNX 权重 + WebGPU 推理 + CacheStorage 缓存 全部由 Agent 构建\n  - 事后用 Claude.ai 反向教学补学原理——"学什么是可能的"比学具体代码更重要\n  - 这既是 Vibe Coding 的典型案例，也体现了 Agent 端到端交付可部署产品的能力边界

## 争议 / 局限

- 没有问责机制：Agent 不像团队有职业声誉
- "用过 2 周"比"测过"更可信——但 Vibe Coding 的产物很难积累使用历史

## 相关资料

- [[../summaries/20260506-SimonWillison-Vibe coding and agentic engineering]]
- Karpathy 原推文（2025-03，待补充链接）

## 待深入

- [ ] Karpathy 原推文中的 Vibe Coding 完整定义
- [ ] Vibe Coding 在企业内部工具/Demo 场景的边界
