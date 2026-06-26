---
type: summary
created: 2026-06-01
updated: 2026-06-01
source_file: "[[../raw/20260506-SimonWillison-Vibe coding and agentic engineering]]"
source_url: https://simonwillison.net/2026/may/6/vibe-coding-and-agentic-engineering/
source_author: Simon Willison
source_date: 2026-05-06
source_tier: 一手源
tags: [agent, llm, ai, vibe-coding, agentic-engineering, 方法论, 一手源, 人物, 已验证]
---

# 20260506 · Simon Willison · Vibe coding and agentic engineering are getting closer than I'd like

> 一句话摘要：Simon Willison 反思 [[../concepts/Vibe Coding|Vibe Coding]] 和 [[../concepts/Agentic Engineering|Agentic Engineering]] 的边界正在模糊——他自己也开始不审查 Agent 写的代码，触发 [[../concepts/规范偏差正常化|规范偏差正常化]] 风险；同时提出"用过"比"测过"更可信的软件评估新标准。

## 核心论点

1. **Vibe coding 和 Agentic engineering 的边界正在消失**：前者是"不审代码、只看结果"，后者是"专业工程师用 AI 提升质量"。但随着 Agent 越来越可靠，专业工程师也开始不审代码——两者在实践中融合了。
2. **"其他团队"类比**：Willison 把 Agent 产出比作大型组织里其他团队的代码——你不会逐行审查，而是看文档、用接口、出问题时才深入。问题是：团队有声誉和问责，Agent 没有。
3. **规范偏差正常化（Normalization of Deviance）**：每次 Agent 在无人监督下写出正确代码，就增加了一次"信任侥幸"——未来某次在错误时刻信任它就会被烧伤。
4. **软件评估的新挑战**：AI 能在半小时内生成 100 commits + 精美 README + 全覆盖测试的仓库——与传统"用心写的项目"外观无差别。新标准：**有没有人真正用过**比有没有好测试更重要。
5. **瓶颈已经转移**：200 行/天 → 2000 行/天，整个软件开发生命周期都围绕"写代码很慢"设计——现在不只是下游（测试/部署）跟不上，上游（设计/决策）也需要重新思考。
6. **Jenny Wen（Anthropic 设计负责人）洞察**：设计流程的核心假设是"设计错了 = 工程师白花 3 个月"，如果实现成本大幅降低，设计流程也可以更冒险。

## 关键事实 / 数据

- Willison 25 年软件工程经验（来源: 原文自述）
- Matthew Yglesias 观点："我不想 vibecode——我想让专业软件公司用 AI 辅助做出更好更便宜的软件"（来源: 原文引用推文）
- Jenny Wen 在 Anthropic 的设计实践（来源: 原文引用讲座）
- 企业版"用过才算数"：不想用 CRM 除非至少 2 家大型企业已成功使用 6 个月（来源: 原文）

## 原文金句

> "Weirdly though, those things have started to blur for me already, which is quite upsetting."

> "Claude Code does not have a professional reputation! It cannot take accountability for what it has done. But it has been proving itself anyway."

> "I want to build higher quality stuff faster. I want everything I am building to be better in every way than it was before."

> "What I value more than the quality of the tests and documentation is that I want somebody to have used the thing."

> "Producing software is a ferociously difficult thing to do."

## 抽取的实体

- [[../entities/Andrej Karpathy|Andrej Karpathy]] — 关联：Willison 是 Karpathy 思想的长期追踪者
- [[../entities/Anthropic|Anthropic]] — 关联：Jenny Wen 是 Anthropic 设计负责人

## 抽取的概念

- [[../concepts/Vibe Coding|Vibe Coding]] — 新建：不看代码只看结果的 AI 编程方式
- [[../concepts/Agentic Engineering|Agentic Engineering]] — 新建：专业工程师用 AI 提升质量
- [[../concepts/规范偏差正常化|规范偏差正常化]] — 新建：反复侥幸导致风险感知退化

## 与已有知识的关系

- **强呼应**：[[../concepts/LLM 编程三宗罪|LLM 编程三宗罪]] 的"不审代码就提交"是 Vibe Coding 的负面案例
- **强呼应**：[[../concepts/Simplicity First|Simplicity First]] 和 [[../concepts/Surgical Changes|Surgical Changes]] 是 Agentic Engineering 的正面实践
- **延伸**：[[../concepts/Agent工程化兜底|Agent 工程化兜底]] 的"确定性手段弥补概率性"是 Normalization of Deviance 的工程解药
- **张力**：Willison 说"不审代码"，[[../concepts/Goal-Driven Execution|Goal-Driven Execution]] 说"定义成功标准循环验证"——前者是实践中正在发生的妥协，后者是理想防线
- **新视角**：[[../concepts/上下文工程|上下文工程]] 讲 Agent 的 context 怎么管，本文讲 Agent 的产出怎么评估——是 Agent 生命周期的两端

## 我的批注 / 思考

- Willison 的自我坦诚很有价值：他不是在鼓吹"不审代码好"，而是在承认"我已经在这样做了，这让我不安"——这是真实的一手反思，不是立场输出。
- Normalization of Deviance 原本来自航天（挑战者号灾难），用在 AI 编程上极精准——每一次 Agent 写对了都是一次"侥幸"，但侥幸累积不等于安全。
- "用过比测过更可信"对先生的 AI 运营场景有启发：公司内部 AI 工具/流程的可靠性，最终靠真实使用场景验证，不靠测试覆盖。
- Surprise：Willison 把 Agent 产出类比为"其他团队的代码"——这个类比的力量在于它同时说明了为什么可以不审（接口约定）和为什么有风险（没有声誉机制）。

## 待深入

- [ ] 追溯 Jenny Wen "Dont Trust the Process" 讲座的完整内容
- [ ] 写综述：Vibe Coding / Agentic Engineering / LLM 编程三宗罪 三者关系图
- [ ] Normalization of Deviance 在 AI Agent 场景下的具体缓解策略
