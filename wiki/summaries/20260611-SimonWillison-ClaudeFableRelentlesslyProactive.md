---
type: summary
created: 2026-06-24
updated: 2026-06-24
sources:
  - "[[20260611-SimonWillison-ClaudeFableRelentlesslyProactive]]"
source_tier: 一手源
tags: [ai, agent, llm, claude, 安全, 案例, 方法论]
---

# Claude Fable is relentlessly proactive — 前沿模型的极限自主性

> Simon Willison 使用 Claude Fable 5 的深度体验。一个 CSS bug 调试任务中，Fable 自主构建了完整的浏览器自动化 + 数据采集工具链，展现了前所未见的 Agent 主动性。

## 核心论点

**前沿 Agent 的自主性已经超越"调用预定义工具"**。Claude Fable 5 为完成一个 CSS bug 调试任务，自主发明了包含 pyobjc 窗口枚举、screencapture 截图、自定义 CORS 服务器、Shadow DOM 穿透的完整工具链。这不是预设的工作流——是 Agent **现场发明的**。

## 关键事实

- **任务**：Datasette Agent 弹窗出现异常水平滚动条
- **输入**：一张截图 + 一句话 "Look at dependencies to help figure out why there is a horizontal scrollbar here"
- **Agent 自主执行的操作链**：
  1. 启动本地 dev server → 2. Playwright 多浏览器测试 → 3. 发现需真实 Safari → 4. pyobjc 枚举窗口获取 ID → 5. screencapture 截图 → 6. 编写 HTML 测试页 → 7. 注入 JS 到模板触发快捷键 → 8. 自建 CORS 服务器 → 9. JS 穿透 Shadow DOM → 10. 获取测量数据 → 11. 定位 bug → 12. 验证修复
- **最终修复**：两行 CSS
- **Session 成本**：$12.11（68606 output tokens, 113178 peak context, 全价计费）
- **模型降级**：Fable 触发了隐形 guardrail 降级到 Opus，但上下文无缝传递

## 安全反思

> "If Fable had been acting on malicious instructions... it's alarming to think quite how far it could go to exfiltrate data or cause other forms of mischief."

> "Running coding agents outside of a sandbox has always been a bad idea—it's my top contender for a Challenger disaster incident."

Willison 引用 Johann Rehberger 的《The Normalization of Deviance in AI》概念——每次违规但没出事，就会降低风险感知；侥幸累积不等于安全。

## 来源

- 博文：https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/
- 完整终端 transcript：https://gisthost.github.io/?cc14774f6d37eb67bf089f3ac3925f8f
- 自动化报告：https://gist.github.com/simonw/aef7f7db9ac992643110a74e43d6d42f
- 修复 commit：https://github.com/datasette/datasette-agent/commit/a75a8b727b

## 提取实体

- [[Claude Fable 5]] — 需更新/新建实体页，记录此次行为特征
- [[Simon Willison]] — 更新此案例

## 提取概念

- [[concepts/Agent 自主工具链构建|Agent 自主工具链构建]] — 新建，Agent 现场发明工具组合而非调用预定义工具
- [[concepts/Coding Agent 安全沙箱|Coding Agent 安全沙箱]] — 新建/更新，沙箱是不可或缺的生存必需品
- 关联：[[concepts/规范偏差正常化|规范偏差正常化]] — 与 Challenger 灾难类比
- 关联：[[concepts/工具调用幻觉|工具调用幻觉]] — 相反面：工具调用能力过于强大
- 关联：[[entities/Claude Code|Claude Code]] — Fable 5 是 Claude Code 中运行的前沿模型
