---
type: summary
created: 2026-06-08
updated: 2026-06-08
source_file: "[[../../raw/20260608-知乎-SkillFactory面向Harness设计的技能工厂]]"
source_url: https://zhuanlan.zhihu.com/p/2043031358063236428
source_author: 未标明（知乎专栏）
source_date: 2026-06-02
source_tier: 二手源
tags: [ai, agent, skill, harness-engineering, 方法论, 二手源, 已验证]
aliases: [Skill Factory, 技能工厂]
---

# 20260608 · 知乎 · SkillFactory 面向 Harness 设计的技能工厂

> 一句话摘要：这篇实践复盘把 Skill 生产从“人工写/对话生成”推进到“失败优先、评测驱动、多路并发、回归验证”的工程流水线，并用 [[Trace2Skill]] 一手论文解释下一步：从 agent 轨迹里蒸馏可迁移技能。

## 核心论点

1. **Skill 的真实起点不是“想写一个技能”，而是失败诊断**：先用裸模型执行目标任务、再召回相似 skill 测试；只有当基线失败或复用不满足时，才说明存在真正的能力缺口。
2. **Skill 生产应该 TDD 化**：先沉淀测试问题和评价维度，再生成 skill，再做回归验证；否则只是把 prompt 随机性包装成“技能”。
3. **多路并发 creator 是对抗 LLM 随机性的工程策略**：同时调用不同模型 / Prompt / skill-creator 路径，相当于一次性探索多个候选实现，用 First-Time Pass Rate 换用户等待时间。
4. **Trace → Skill 是规模化方向**：从执行日志中提取成功经验和失败教训，把隐性轨迹压缩成可复用的 SKILL.md / references，而不是长期堆 raw memory。
5. **SkillFactory 的目标不是多造 Skill，而是沉淀可验证、可迁移、可复用的团队能力资产**。

## 关键事实 / 数据

- 原文提出两个生成前评估模块：裸模型评估、skill 匹配分析，用来判断“是否真的需要新 skill”（来源: [[20260608-知乎-SkillFactory面向Harness设计的技能工厂]]）。
- 原文把质量评价拆成格式规范、复用创新、功能可用性、运行稳定性、文档规范等维度（来源: [[20260608-知乎-SkillFactory面向Harness设计的技能工厂]]）。
- [[Trace2Skill]] arXiv v5 于 2026-06-04 修订；论文称 Qwen3.5-35B 轨迹演化出的 skills 可让 Qwen3.5-122B agent 在 WikiTableQuestions 上最高提升 57.65 个百分点（截至 2026-06-08，来源: [[20260608-知乎-SkillFactory面向Harness设计的技能工厂]]）。
- Qwen 官方 Trace2Skill 仓库给出的 pipeline 是：trajectory generation → parallel multi-agent patch proposal → conflict-free patch consolidation（来源: [[20260608-知乎-SkillFactory面向Harness设计的技能工厂]]）。
- Anthropic 官方 skills 仓库把 Skills 定义为包含 instructions、scripts、resources 的文件夹，Claude 会动态加载这些文件夹来提升特定任务表现（来源: [[20260608-知乎-SkillFactory面向Harness设计的技能工厂]]）。

## 原文金句

> 如果不能解决或者不匹配这些失败点和不确定行为，本质上就是 Skill 需要解决的真实能力缺口。

> 通过并行调用 3 种不同策略（或不同模型/不同 Prompt 模板）的 Creator，相当于一次性买了三张不同号码的彩票。

> Trace2Skill 的本质是将智能体的“隐性经验”（大量具体的执行轨迹）转化为“显性知识”（结构化的技能文档）。

## 抽取的实体

- [[../entities/SkillFactory|SkillFactory]]
- [[../entities/Trace2Skill|Trace2Skill]]
- [[../entities/Qwen Code|Qwen Code]]
- [[../entities/Anthropic|Anthropic]]
- [[../entities/OpenClaw|OpenClaw]]
- [[../entities/Claude Code|Claude Code]]

## 抽取的概念

- [[../concepts/Skill工厂|Skill 工厂]]
- [[../concepts/轨迹蒸馏为技能|轨迹蒸馏为技能]]
- [[../concepts/评测驱动Skill生成|评测驱动 Skill 生成]]
- [[../concepts/多路并发竞优|多路并发竞优]]
- [[../concepts/Skills 2.0模块化|Skills 2.0 模块化]]
- [[../concepts/Harness工程|Harness 工程]]
- [[../concepts/验证瓶颈|验证瓶颈]]

## 与已有知识的关系

- **补全**：为 [[../concepts/Skills 2.0模块化|Skills 2.0 模块化]] 补上“生产侧”问题：Skill 不只要会被按需加载，还要能被测试、评分、回归和发布。
- **印证**：与 [[../concepts/验证瓶颈|验证瓶颈]] 同向——AI 让生成 skill 变便宜后，瓶颈变成如何验证 skill 真有效、不过拟合、可复用。
- **延伸**：把 [[../concepts/反馈闭环写入文件|反馈闭环写入文件]] 推进为轨迹级闭环：不是只记录用户纠错，而是系统性分析 agent 成功/失败轨迹。
- **连接**：和 [[../entities/Agent Skills for Context Engineering|Agent Skills for Context Engineering]] 形成互补：后者是高质量 skill 库样本，本文关注 skill 如何规模化生产。

## 我的批注 / 思考

- Surprise：这篇文章有价值的不是“又一个 skill 生成器”，而是把 Skill 当成类似软件交付件：需求诊断、测试集、并行候选、质量门禁、回归、发布。这比“让 Agent 自己写一个 SKILL.md”成熟一截。
- 对个人 Agent 系统的启发：Hana 的经验库 / skill 修改可以引入“失败先行”——每个新 skill 先写它要修掉哪些失败样本，而不是先写漂亮描述。
- 风险：如果测试问题只复用用户输入，容易过拟合单点需求；Trace2Skill 强调 broad trajectories 和 conflict-free consolidation，正好补这个洞。

## 待深入

- [ ] 录入 [[Trace2Skill]] 论文细节，特别是 success/error analyst 与 patch consolidation prompt。
- [ ] 对比 [[SkillRL]]：一个偏离线技能蒸馏，一个偏 RL 中 skill bank 与策略共同演化。
- [ ] 抽样查看 Anthropic 官方 xlsx skill 与 Trace2Skill released skills 的差异。
