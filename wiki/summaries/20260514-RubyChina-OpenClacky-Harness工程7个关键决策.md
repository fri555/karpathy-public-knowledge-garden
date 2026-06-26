---
type: summary
created: 2026-05-29
updated: 2026-05-29
source_file: "[[../raw/20260514-RubyChina-OpenClacky-Harness工程7个关键决策|raw/20260514-RubyChina-OpenClacky-Harness工程7个关键决策]]"
source_url: https://ruby-china.org/topics/44571
source_author: lyfi2003（Ruby China；OpenClacky 作者/团队成员）
source_date: 2026-05-14
source_tier: 一手源-作者复盘
tags: [agent, llm, harness, 工程实践, prompt-cache, ruby, 开源, 已验证]
---

# 20260514 · Ruby China · OpenClacky Harness 工程 7 个关键决策

> 一句话摘要：OpenClacky 团队两年三代 Agent 架构复盘：真正拉开 Agent 成本与稳定性差距的不是模型，而是 [[../concepts/Harness工程|Harness 工程]]——尤其是 [[../concepts/Prompt Cache局部性|Prompt Cache 局部性]] 和 [[../concepts/工具集稳定性|工具集稳定性]]。

## 核心论点

1. **Agent 的主要矛盾从“效果”转向“成本”**：同样任务中，不同 Agent 的成本差异直接来自请求数和 cache 命中率，而非单纯模型能力。
2. **功能完整性和高 cache 命中率天然冲突**：切模型、装 Skill、知道日期、读 PDF、压缩上下文都会改变 prompt 前缀或 tool schema，导致 cache 失效。
3. **两代失败收敛出第三代原则**：RAG/知识库分片增加不可靠部件，多 Agent 工作流造成 cache 灾难；第三代改围绕 cache 局部性和工具集稳定性组织。
4. **Harness 是模型外的一切工程纪律**：冻结 system prompt、双 cache marker、稳定工具集、Insert-then-Compress、脚本式自进化工具、可见浏览器，都是把成本和可靠性从概率模型手里拿回工程层。
5. **把工程预算花在不会随模型进步过时的地方**：cache 命中率、工具稳定性、安装体验、压缩策略，会比追 benchmark 或堆多 Agent 编排更抗时间。

## 关键事实 / 数据

- 3 项任务实测，OpenClacky 总成本 **$5.10**、请求数 **51**、Cache 命中率 **90.6%**；Claude Code **$5.49 / 70 / 95.2%**；OpenClaw **$15.70 / 81 / 88.7%**；Hermes **$30.14 / 218 / 60.3%**（截至 2026-05-14，来源为作者 OpenRouter CSV 核算）。
- OpenClacky 是全功能 Agent：WebUI + 命令行、长期记忆、Skill 技能库、定时任务、IM 接入、浏览器自动化、子 Agent、运行时切模型、Skill 自进化与动态加载。
- OpenClacky 第三代用 Ruby 从零重写 4 个月，围绕“cache 局部性”和“工具集稳定性”组织。
- 压缩策略对比：一次 50K token 会话压缩，独立 call 约 50,000 cold token，Insert-then-Compress 约 500 cold token。
- 作者给出的压缩甜区为 20–30 万 token，压缩后压到 1 万 token 以内；用户停止输入 90 秒后开始检查是否触发空闲压缩。

## 原文金句

> “这些功能里很多跟高 cache 命中率是结构性冲突的。”

> “多 Agent 在结构上就是 cache 灾难。”

> “把工程预算花在 harness 上，不要花在编排上。”

> “cache 是按前缀匹配的——前缀里改一个字节，从那里往后全部失效。”

> “把工程预算花在 harness 上，把智能预算留给模型。”

## 抽取的实体

- [[../entities/OpenClacky|OpenClacky]] — 新建：Ruby 开源 Agent，本文的实践主体
- [[../entities/Claude Code|Claude Code]] — 对照基准：闭源顶级 Harness，cache 命中率对照
- [[../entities/OpenClaw|OpenClaw]] — 评测对照对象之一
- [[../entities/Hermes|Hermes]] — 评测对照对象之一

## 抽取的概念

- [[../concepts/Harness工程|Harness 工程]] — 新建：模型之外的一切 Agent 工程
- [[../concepts/Prompt Cache局部性|Prompt Cache 局部性]] — 新建：高命中率的底层几何
- [[../concepts/工具集稳定性|工具集稳定性]] — 新建：通过少量稳定工具 + Skill 外包能力避免 schema 膨胀
- [[../concepts/上下文膨胀与压缩|上下文膨胀与压缩]] — 更新：补充 Insert-then-Compress 和空闲压缩策略
- [[../concepts/RAG|RAG]] — 更新：补充 Agent 场景下“RAG/知识库分片”的失败教训

## 与已有知识的关系

- **强印证**：[[../concepts/Agent工程化兜底|Agent 工程化兜底]] 说“Agent 再智能也是软件系统”，OpenClacky 则给出 cache / tool schema / 压缩 / 浏览器可见性的具体工程做法。
- **延伸**：[[../concepts/上下文膨胀与压缩|上下文膨胀与压缩]] 原有 Saboo 案例关注“定期维护”，本文提供更底层的“压缩也要命中 cache”的成本策略。
- **修正/细化**：[[../concepts/RAG|RAG]] 原本主要从知识管理范式批判 RAG，本文从 Agent 运行时角度指出：RAG 还会增加实时更新成本、延迟和新的失败部件。
- **呼应**：[[../concepts/Skills 2.0模块化|Skills 2.0 模块化]] 的 on-demand 载入，与 OpenClacky 用 `invoke_skill` 保持主工具列表稳定同源，都是“能力扩展不污染主上下文”。
- **张力**：本文强烈反对多 Agent 工作流编排，但本库已有 [[../concepts/Agent团队三阶段曲线|Agent 团队三阶段曲线]] / [[../entities/Mac Mini Agent Fleet|Mac Mini Agent Fleet]] 的多 Agent 实践；后续可做“多 Agent 何时是 cache 灾难，何时是组织分工”的专题对照。

## 我的批注 / 思考

- 这篇是今天巡检里最符合“内容而非新闻”的材料：作者不是转述发布，而是把两代失败、第三代取舍、具体工程策略全摊开，三年后仍有价值。
- 对先生的 AI 运营场景也有启发：很多 AI 项目不是“模型不够聪明”，而是工作流、数据接入、权限、成本、缓存、压缩、工具稳定性没设计好。**模型是发动机，Harness 是底盘和刹车。**
- “不要做多 Agent 编排”的表述很激进，不能直接当铁律；它更准确的适用范围是：在同一个长任务、同一个上下文连续执行场景下，多 Agent 交接会破坏 cache 局部性。但对于长期岗位分工、权限隔离、多视角审查，多 Agent 仍可能成立。
- Surprise：OpenClacky 不是靠“更多工具”赢，而是靠**拒绝增加第 17 个工具**来赢。克制本身就是工程能力。

## 待深入

- [ ] 抓取 OpenClacky GitHub README / benchmark 作为一手仓库辅助源
- [ ] 写综述：Saboo / Shareuhack / 沙河 rain / OpenClacky 四种 Agent 工程化流派对照
- [ ] 专题研究：多 Agent 作为“工作流编排”与“长期岗位分工”的边界
