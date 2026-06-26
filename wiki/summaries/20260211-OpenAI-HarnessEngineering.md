---
type: summary
created: 2026-06-05
updated: 2026-06-05
source_file: "[[../raw/20260211-OpenAI-HarnessEngineering|raw/20260211-OpenAI-HarnessEngineering]]"
source_url: https://openai.com/index/harness-engineering/
source_author: Ryan Lopopolo / OpenAI
source_date: 2026-02-11
source_tier: 一手源
tags: [ai, agent, coding, 工程实践, harness, 一手源, 已验证]
---

# 20260211 · OpenAI · Harness Engineering

> 一句话摘要：OpenAI 的 Harness 团队用 5 个月、约 1500 个 PR、约 100 万行 Codex 生成代码构建内部产品，核心教训是：人类的工作从“写代码”迁移到“设计环境、指定意图、构建反馈循环”。

## 核心论点

1. **Agent 失败时不要让它 try harder，要补环境能力**：每次失败都应追问“缺什么工具、约束、文档或可观测性，如何让它对 Agent 可读且可执行”。
2. **AGENTS.md 是目录，不是百科全书**：短入口 + 结构化 docs/ 才能让 Agent 逐层发现 context，避免巨型指令文件腐烂和挤占任务上下文。
3. **Agent 可读性是设计目标**：UI、日志、指标、trace、设计文档、执行计划、质量评分都要变成 Agent 能访问和查询的系统。
4. **架构与品味要机械执行**：自定义 linter、结构测试、命名/文件大小/可靠性约束，把“团队品味”编码成 Agent 每次运行都会遇到的反馈。
5. **熵管理必须自动化**：当生成吞吐超过人类审查带宽，靠每周人工清理 AI slop 会崩，必须用后台 cleanup agents 做持续垃圾回收。

## 关键事实 / 数据

- OpenAI Harness 团队约 **5 个月**构建内部 beta 产品，宣称 **0 行人工手写代码**，所有应用逻辑、测试、CI、文档、可观测性和内部工具都由 Codex 写成。(来源: [[../raw/20260211-OpenAI-HarnessEngineering]])
- 项目规模约 **100 万行代码**、约 **1500 个 PR**，小团队从 3 人扩到 7 人，平均约 **3.5 PR/工程师/天**（截至 2026-02-11）。(同上)
- 初期进展慢不是因为 Codex 不会，而是环境欠规格化：缺工具、抽象和内部结构。(同上)
- 应用被做成每个 git worktree 可启动，Codex 可用 Chrome DevTools、DOM snapshot、截图、LogQL / PromQL / TraceQL 验证 UI 和可观测性。(同上)
- 人工 Friday cleanup 曾占一周 **20%**，后来被“golden principles + recurring cleanup agents”替代。(同上)

## 原文金句

> “Humans steer. Agents execute.”

> “Early progress was slower than we expected, not because Codex was incapable, but because the environment was underspecified.”

> “Give Codex a map, not a 1,000-page instruction manual.”

> “From the agent’s point of view, anything it can’t access in-context while running effectively doesn’t exist.”

> “Human taste is captured once, then enforced continuously on every line of code.”

## 抽取的实体

- [[../entities/OpenAI|OpenAI]]
- [[../entities/Codex|Codex]]
- [[../entities/Ryan Lopopolo|Ryan Lopopolo]]

## 抽取的概念

- [[../concepts/Harness工程|Harness 工程]]
- [[../concepts/Agent可读性|Agent可读性]]
- [[../concepts/AGENTS.md作为目录|AGENTS.md作为目录]]
- [[../concepts/Agent垃圾回收|Agent垃圾回收]]
- [[../concepts/验证瓶颈|验证瓶颈]]
- [[../concepts/渐进式披露|渐进式披露]]

## 与已有知识的关系

- **强印证**：[[../concepts/验证瓶颈|验证瓶颈]] 在 OpenAI 案例中表现为“human QA capacity”成为瓶颈，于是把 UI、日志、指标做成 Agent 可读。
- **延伸**：把 [[../concepts/反馈闭环写入文件|反馈闭环写入文件]] 从“记忆规则”升级到“整个 repo 是 Agent 的系统记录”。
- **补全**：本库已有 OpenClacky 的 [[../concepts/Harness工程|Harness 工程]] 成本视角；OpenAI 提供了组织与 SDLC 视角。
- **呼应**：[[../concepts/渐进式披露|渐进式披露]] 不只是 context 技巧，而是 AGENTS.md + docs/ + plans + quality score 的知识系统设计。

## 我的批注 / 思考

- 这篇应作为本库 Harness 轴的核心一手源。它把“Agent 工程化”从 prompt 技巧拉到了组织操作系统。
- Surprise：OpenAI 最激进的地方不是“让 Agent 写代码”，而是把**人手写代码定义成 harness 失败信号**。这很极端，不一定可迁移，但足够启发。
- 对个人系统的启发：当 Agent 失败，不要只改一句提示词；更高杠杆的问题是——我能不能增加一个可读文件、校验脚本、模板或可观测信号，让下一次不再靠提醒？

## 待深入

- [ ] 对照 [[../summaries/20260514-RubyChina-OpenClacky-Harness工程7个关键决策]] 写“成本型 Harness vs 可读性型 Harness”。
- [ ] 补抓 OpenAI cookbook 的 Codex execution plans，一并完善 spec / plan 相关概念。
