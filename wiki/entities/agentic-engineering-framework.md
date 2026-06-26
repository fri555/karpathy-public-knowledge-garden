---
type: entity
created: 2026-06-03
updated: 2026-06-03
sources:
  - "[[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]]"
tags: [工具, agent, llm, skill, 工程实践, 方法论, 已验证]
aliases: [davidYichengWei/agentic-engineering-framework]
---

# agentic-engineering-framework

> 一句话定义：[[davidycwei]] 提出的基于 Skill 的模块化 [[../concepts/Agentic Engineering|Agentic Engineering]] 框架，用 Markdown + YAML 将 SDLC 工作流、最佳实践、项目规范和错误复盘组织成 Agent 可按需加载的工程上下文。

## 基本信息

- **类型**：Agentic Engineering 方法论框架 / Skill 集合
- **载体**：Markdown + YAML 元数据 + 可选参考资源
- **作者**：[[davidycwei]]
- **兼容目标**：Claude Code、Cursor、CodeBuddy、Codex CLI 等主流 Coding Agent（来源: [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]])

## 核心结构

- **Workflow Skills**：需求澄清 → 系统设计 → 测试生成 → 代码生成 → 代码评审
- **Best Practices**：架构设计、编码实践、性能优化、分布式系统等可复用知识
- **Standards**：项目私有编码规范、模块约束、测试规范
- **Troubleshooting**：排查场景下独立触发
- **Self-Refinement**：监听协作错误，把经验回写到 Best Practices / Standards / Rules

## 关键设计

- **Agent-Agnostic**：纯文本结构，不依赖特定 Agent 平台 API (来源: [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]])
- **按需加载**：三层渐进式披露，L1 元数据 → L2 指令 → L3 参考资源，避免把所有规范一次性塞进上下文 (来源: [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]])
- **风险分级**：简单任务轻流程，复杂任务必须先进入 [[../concepts/Spec-First工作流|Spec-First 工作流]] (来源: [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]])
- **知识可演进**：Skills 与代码同仓库、同 MR 流程，团队经验通过版本化管理持续生长 (来源: [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]])

## 与本库的关系

这个框架与本库的 [[../concepts/LLM Wiki|LLM Wiki]] 有同构关系：

- LLM Wiki 把资料编译成可持续更新的知识层。
- agentic-engineering-framework 把工程经验编译成可执行的 Skill 层。

两者共同目标都是：让 Agent 不依赖一次性上下文，而是通过可维护的知识结构持续变强。

## 争议 / 局限

- 复杂流程有 token 和执行成本，必须靠风险分级避免过度流程化。
- 框架效果依赖团队是否愿意持续维护 Standards / Best Practices，否则容易退化为文档摆设。
- 本次只读取了知乎原文和其引用的一手资料，GitHub README 待补。

## 相关资料

- [[../summaries/20260306-知乎-从第一性原理思考AgenticEngineering]]
- [[../concepts/Agentic Engineering|Agentic Engineering]]
- [[../concepts/Spec-First工作流|Spec-First 工作流]]
- [[../concepts/Error-Driven Context Refinement|Error-Driven Context Refinement]]

## 待深入

- [ ] 抓取 `github.com/davidYichengWei/agentic-engineering-framework` README。
- [ ] 对比本库 `.agents/skills/` 的 Skill 结构，评估哪些可借鉴。
