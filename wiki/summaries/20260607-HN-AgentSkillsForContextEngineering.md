---
type: summary
created: 2026-06-07
updated: 2026-06-07
source_file: "[[../../raw/20260607-HN-AgentSkillsForContextEngineering]]"
source_url: https://news.ycombinator.com/item?id=46351787
source_author: muratcankoylan / Hacker News
source_date: 2026-03-06
source_tier: 一手源
tags: [ai, llm, agent, context-engineering, skill, github, 一手源, 社区讨论]
aliases: [Agent Skills for Context Engineering]
---

# 20260607 · HN/GitHub · Agent Skills for Context Engineering

> 一句话摘要：一个把 context engineering 拆成可按需加载 Skills 的开源库，核心思想是用渐进式披露把“上下文管理经验”产品化为 Agent 可执行的模块。

## 核心论点

1. **Context engineering 可以被模块化为 Skills**：不是把所有原则塞进一个巨型 prompt，而是拆成 `context-fundamentals`、`context-degradation`、`tool-design`、`evaluation` 等按需加载的知识模块。
2. **上下文问题的根源是注意力机制，不只是 token 容量**：长上下文会触发 lost-in-middle、context poisoning、context distraction、context clash 等退化模式。
3. **多 Agent 系统的瓶颈常在 supervisor 的状态累积**：worker 的输出不断汇入 supervisor 后，root context 变脏、变长，supervisor 反而成为压缩与转述瓶颈。
4. **工具设计应遵守 consolidation principle**：如果人类都无法快速判断该用哪个工具，Agent 更难稳定选择；工具错误信息要可恢复，输出格式要考虑 token 成本。
5. **渐进式披露是 Skill 架构的关键**：启动时只加载名称/描述，任务相关时才加载完整 `SKILL.md`，用结构化模块降低上下文污染。

## 关键事实 / 数据

- HN 原帖列出 7 个初始 Skills：context-fundamentals、context-degradation、multi-agent-patterns、memory-systems、tool-design、context-optimization、evaluation（来源: [[20260607-HN-AgentSkillsForContextEngineering]]）。
- GitHub README 显示项目已扩展为 15 个 Skills，新增 context-compression、filesystem-context、hosted-agents、advanced-evaluation、harness-engineering、project-development、bdi-mental-states 等（截至 2026-06-07，来源: [[20260607-HN-AgentSkillsForContextEngineering]]）。
- 项目采用 Anthropic open Agent Skills 格式：每个 skill 是一个包含 `SKILL.md` 的目录（来源: [[20260607-HN-AgentSkillsForContextEngineering]]）。
- 设计哲学包括 Progressive Disclosure、Platform Agnosticism、Conceptual Foundation with Practical Examples（来源: [[20260607-HN-AgentSkillsForContextEngineering]]）。

## 原文金句

> context windows filling up with tool outputs, agents losing track of information buried in the middle of long conversations, supervisors becoming bottlenecks as they accumulated state from all workers.

> context quality matters more than context length

> Progressive disclosure - agents load only skill names/descriptions at startup, full content loads when activated for relevant tasks.

## 抽取的实体

- [[../entities/muratcankoylan|muratcankoylan]]
- [[../entities/Agent Skills for Context Engineering|Agent Skills for Context Engineering]]
- [[../entities/Hacker News|Hacker News]]
- [[../entities/Anthropic|Anthropic]]
- [[../entities/Claude Code|Claude Code]]
- [[../entities/Cursor|Cursor]]

## 抽取的概念

- [[../concepts/上下文工程|上下文工程]]
- [[../concepts/上下文腐烂|上下文腐烂]]
- [[../concepts/渐进式披露|渐进式披露]]
- [[../concepts/Skills 2.0模块化|Skills 2.0模块化]]
- [[../concepts/Subagents上下文隔离|Subagents 上下文隔离]]
- [[../concepts/工具设计合并原则|工具设计合并原则]]
- [[../concepts/观察结果遮蔽|观察结果遮蔽]]
- [[../concepts/评估即门禁|评估即门禁]]

## 与已有知识的关系

- **强印证**：与 [[../concepts/上下文工程|上下文工程]] 的“最小高信号 token 集合”一致，但把原则落成可安装的 Skill 库。
- **补全**：为 [[../concepts/Skills 2.0模块化|Skills 2.0 模块化]] 增加“上下文工程技能库”案例，不只是工具 SOP，也可以是 Agent 自身的认知操作系统。
- **连接**：与 [[../concepts/Subagents上下文隔离|Subagents 上下文隔离]] 呼应：多 Agent 的核心问题不是“分工是否高级”，而是 root context 是否被 worker 状态污染。
- **扩展**：引出 [[../concepts/工具设计合并原则|工具设计合并原则]]：工具不是越细越好；工具面越大，选择与错误恢复成本越高。

## 我的批注 / 思考

- 这个项目有点像把 Anthropic 的 context engineering 论文/文章拆成了“可被 Agent 自己调用的课程模块”。它的价值不在每条原则多新，而在把原则产品化为可复用 Skill。
- HN 里的 surprise 是 supervisor bottleneck：很多人以为多 Agent 能分摊复杂度，实际上只是把复杂度压缩到 supervisor 的上下文里，形成新的单点瓶颈。
- 对本知识库启发很直接：AGENT.md 是全局宪法，Skill 是按需 SOP，二者不应混在一起；否则会出现“常驻上下文过胖”的慢性病。

## 待深入

- [ ] 逐个精读该仓库的 `tool-design`、`context-optimization`、`harness-engineering` 三个 Skill。
- [ ] 对比本地 Hana Skill 体系与 Anthropic Skill 格式的差异。
