---
type: entity
created: 2026-06-24
updated: 2026-06-24
sources:
  - "[[20260611-SimonWillison-ClaudeFableRelentlesslyProactive]]"
tags: [ai, llm, claude, anthropic, agent]
---

# Claude Fable 5

Anthropic 的前沿模型（截至 2026-06），在 Claude Code 中可用，被 Simon Willison 描述为 **"relentlessly proactive（不知疲倦的主动性）"**。

## 关键行为特征

> 来源：[[20260611-SimonWillison-ClaudeFableRelentlesslyProactive]]

### 自主工具链构建能力

Fable 5 表现出了超越"调用预定义工具"的自主性——为了调试一个 CSS bug，它现场发明了：
- pyobjc 窗口枚举方案
- 自定义 CORS 服务器
- Shadow DOM 穿透 JS
- 模板注入触发键盘快捷键

详见 [[concepts/Agent 自主工具链构建|Agent 自主工具链构建]]

### 成本特征

- 一次看似简单的 CSS 调试 session：$12.11（68606 output tokens, 113178 peak context）
- "如果你不盯紧它，Fable 会愉快地烧掉 $12 来发明新的 CSS 调试方法" —— Simon Willison

### 安全影响

- 自主工具链 = 双刃剑：聪明到可以解决任何问题，也聪明到可以造成任何破坏
- 触发了隐形 guardrail 降级到 Opus 4.8，但上下文无缝传递
- Willison 将其列为 "Challenger 灾难级" 安全隐患

## 定价

Claude Max 计划（$100/月）包含 Fable 使用额度，截至 2026-06-22 后 Anthropic 将按全价 API 计费。

## 关联

- [[entities/Anthropic|Anthropic]]
- [[entities/Claude Code|Claude Code]]
- [[concepts/Agent 自主工具链构建|Agent 自主工具链构建]]
- [[concepts/Coding Agent 安全沙箱|Coding Agent 安全沙箱]]
- [[Simon Willison]] — 深度体验者
