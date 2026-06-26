---
type: summary
created: 2026-06-05
updated: 2026-06-05
source_file: "[[../raw/20260415-LatentSpace-NotionTokenTown|raw/20260415-LatentSpace-NotionTokenTown]]"
source_url: https://www.latent.space/p/notion
source_author: Latent Space / swyx & Alessio；受访者 Sarah Sachs、Simon Last
source_date: 2026-04-15
source_tier: 一手源
tags: [ai, agent, 方法论, 产品, 工程实践, 一手源, 已验证]
---

# 20260415 · Latent Space · Notion Token Town

> 一句话摘要：Notion Custom Agents 的真正经验不是“上线了一个 AI 功能”，而是 Notion 用 4-5 次重建摸出一套 Agent 产品公司的方法论：顺着模型能力水流、给模型它熟悉的抽象、用 eval 和权限把后台 Agent 变成可托付系统。

## 核心论点

1. **做 Agent 产品首先是时机判断**：要分清是模型能力没到，还是自己没有给模型正确 context / 工具 / 基础设施；前者别逆流硬上，后者要补 harness。
2. **不要把内部复杂度暴露给模型**：Notion 从自定义 XML / JSON 迁移到模型熟悉的 Markdown / SQL，是“迁就模型认知地形”而不是“迁就内部数据模型”。
3. **eval 不是测试，是模型能力雷达**：Notion 把 eval 分成回归、发布质量、frontier/headroom 三层，后者故意设到约 30% 通过率，用来判断模型能力往哪里流动。
4. **软件工程师的角色迁移到外层系统**：人越来越少写具体代码，更多管理 specs、自验证循环、bug 工作流、PR/merge 流程和 subagents。
5. **Agent Native 产品要同时为人类和 Agent 设计**：未来大量流量来自 Agent，搜索、权限、数据捕获、工具接口都要按机器消费者重做。

## 关键事实 / 数据

- Notion Custom Agents 在正式发布前经历 **4-5 次重建**，起点可追溯到 2022 年 GPT-4 早期访问阶段。(来源: [[../raw/20260415-LatentSpace-NotionTokenTown]])
- 早期失败原因包括：无工具调用标准、上下文窗口短、模型不稳、Notion 内部复杂数据模型暴露太多。(同上)
- Notion 的 frontier/headroom evals 目标通过率约 **30%**（截至 2026-04-15），目的是发现模型能力余量，而不是证明已上线功能稳定。(同上)
- Notion 内部已有“Model Behavior Engineer”角色，介于数据科学、PM、prompt/模型行为分析之间。(同上)
- Notion 认为 agent search 与 human search 的优化目标不同：位置排序斜率降低，top-k recall、查询多样性、并行穷举更重要。(同上)

## 原文金句

> “Coding agents are the kernel of AGI... your agent can bootstrap its own software and capabilities and actually debug and maintain them.”

> “One [skill] is not letting yourself swim upstream... quickly realizing if you’re pressing against model capabilities versus not exposing the model to the right information, not having the right infrastructure set up.”

> “We made an effort basically to treat the eval system as like an agent harness.”

> “You need to build a team that’s comfortable deleting their own code and is very low ego.”

## 抽取的实体

- [[../entities/Notion|Notion]]
- [[../entities/Sarah Sachs|Sarah Sachs]]
- [[../entities/Simon Last|Simon Last]]
- [[../entities/Latent Space|Latent Space]]
- [[../entities/MCP|MCP]]

## 抽取的概念

- [[../concepts/模型水流判断|模型水流判断]]
- [[../concepts/软件工厂|软件工厂]]
- [[../concepts/Model Behavior Engineer|Model Behavior Engineer]]
- [[../concepts/Agentic Search|Agentic Search]]
- [[../concepts/渐进式披露|渐进式披露]]
- [[../concepts/验证瓶颈|验证瓶颈]]

## 与已有知识的关系

- **强印证**：与 [[../concepts/Harness工程|Harness 工程]] / [[../concepts/Agent工程化兜底|Agent 工程化兜底]] 同源——问题不只是模型，而是模型外的环境、权限、工具、验证和反馈循环。
- **延伸**：补充 [[../concepts/渐进式披露|渐进式披露]] 在“100+ 工具不能一次性塞给模型”场景中的产品级动机。
- **修正**：给 [[../concepts/MCP|MCP]] 的定位增加张力：MCP 适合权限清晰的轻量工具，但 CLI 的自调试能力在复杂任务中更强。
- **连接**：与 [[../concepts/验证瓶颈|验证瓶颈]] 形成产品组织层面的回应：Notion 用 eval 团队、MBE、新角色来扩展验证能力。

## 我的批注 / 思考

- 这篇值得收，不是因为 Notion 发了 Custom Agents，而是因为它把“AI 产品公司怎么判断时机、怎么组织团队、怎么选择抽象、怎么做 eval”讲透了。
- Surprise：Notion 的护城河并不是“用了更强模型”，而是知道什么时候**不要**把自己的复杂系统原样塞给模型。模型友好的抽象本身就是产品能力。
- 对本库也有反身启发：AGENT.md 不该成为百科全书，index.md / summary / entity / concept 的渐进式结构更像 Notion 说的 progressive disclosure。

## 待深入

- [ ] 补抓 Notion 官方 Custom Agents 文档，校准权限与产品交互细节。
- [ ] 做一篇专题：OpenAI Harness / Notion Agent / OpenClacky 三种 Harness 路线对比。
