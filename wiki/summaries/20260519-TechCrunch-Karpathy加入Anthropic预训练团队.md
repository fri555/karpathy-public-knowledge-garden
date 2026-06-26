---
type: summary
created: 2026-05-27
updated: 2026-05-27
source_file: "[[../../raw/20260519-TechCrunch-Karpathy加入Anthropic预训练团队]]"
source_url: https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/
source_author: Rebecca Bellan & Lorenzo Franceschi-Bicchierai
source_date: 2026-05-19
source_tier: 一手源
tags: [ai, llm, anthropic, karpathy, 人物动态, 一手源, 公司]
---

# 20260519 · TechCrunch · Karpathy 加入 Anthropic 预训练团队

> 一句话摘要：[[entities/Andrej Karpathy|Karpathy]] 2026-05-19 在 X 官宣加入 [[entities/Anthropic|Anthropic]] 预训练团队（团队 lead 是 Nick Joseph），将组建一个新小组，使命是**用 Claude 加速 Claude 自身的预训练研究**——这是他 2026-03 开源 [[entities/autoresearch|autoresearch]] (83k★) 同一思路的工业级延伸。

## 核心论点

1. **个人级回归一线**：Karpathy 离开 Tesla（2022）→ 短暂回 OpenAI 一年（2022-2023）→ 2024 创办教育创业 [[entities/Eureka Labs|Eureka Labs]] → 2026-05-19 加入 Anthropic 做 R&D；自述教育不会放弃但暂缓
2. **岗位的核心使命**：不是普通预训练研究员，而是组建一个新团队，**用 Claude 自己来加速训练下一代 Claude 的研究**（"using Claude to accelerate pre-training research"）
3. **战略级信号**：Anthropic 押注 "AI-assisted research" 而非纯算力堆叠——这是和 OpenAI / Google 拉开差距的杠杆点（来源原文："AI-assisted research, rather than pure compute, is how it stays competitive"）
4. **思路有迹可循**：早在 2026-03 Karpathy 个人就发布了 [[entities/autoresearch|autoresearch]]（630 行 Python、单 GPU、5 分钟一轮、夜里 100 实验），证明 [[concepts/递归自我改进|"AI 训练 AI"]] 是可工程化的范式；Anthropic 这次是把它放大到产业级
5. **附带消息**：同日 Anthropic frontier red team 也招到老兵 Chris Rohlf（Meta 6 年 / 前 Yahoo Paranoids）

## 关键事实 / 数据

- **官宣时间**：2026-05-19（Karpathy X 推 + TechCrunch 同日报道）
- **直属 lead**：Nick Joseph（Anthropic 预训练团队负责人）
- **任务范围**：组建新团队，用 Claude 加速预训练研究
- **Karpathy 个人 X 推 ID**：https://x.com/karpathy/status/2056753169888334312
- **[[entities/autoresearch|autoresearch]] GitHub star**：**83,345**(截至 2026-05-27)，MIT 协议
- **autoresearch 创建时间**：2026-03-06，最后 push 2026-03-26
- **autoresearch 设计核心**：5 分钟固定时间预算 / 12 实验/小时 / 单文件（train.py）只让 agent 改 / `program.md` 是"超轻量 skill"
- **Anthropic 估值**：约 8000 亿美元，传闻最早 2026 年底 IPO（TechNextWeb 5/19 同步报道）

## 原文金句

> "I've joined Anthropic. I think the next few years at the frontier of LLMs will be especially formative. I am very excited to join the team here and get back to R&D. I remain deeply passionate about education and plan to resume my work on it in time."
> —— Andrej Karpathy, X, 2026-05-19

> "Karpathy is one of the few researchers who can bridge the gap between LLM theory and large-scale training practice. Tapping him to build such a team is a clear sign from Anthropic that it believes AI-assisted research, rather than pure compute, is how it stays competitive with OpenAI and Google."
> —— TechCrunch 编辑解读

> "One day, frontier AI research used to be done by meat computers in between eating, sleeping, having other fun, and synchronizing once in a while using sound wave interconnect in the ritual of 'group meeting'. That era is long gone."
> —— Karpathy, autoresearch README 开篇（2026-03）

> "program.md is essentially a super lightweight 'skill'."
> —— Karpathy, autoresearch README（对应 [[entities/CLAUDE.md|CLAUDE.md]] 和 [[../../wiki/concepts/原则化指令|原则化指令]] 的同源叙事）

## 抽取的实体

- [[../entities/Andrej Karpathy|Andrej Karpathy]] —— 大幅修订（加入新东家 + autoresearch 作品 + 履历补全）
- [[../entities/Anthropic|Anthropic]] —— 修订（5/19 一手源补全，覆盖之前从二手猜出来的 5/20）
- [[../entities/autoresearch|autoresearch]] —— **新建**（Karpathy 个人开源项目 + 思路前身）
- [[../entities/Eureka Labs|Eureka Labs]] —— **新建**（Karpathy 2024 创办的教育创业，目前状态暧昧）
- [[../entities/Nick Joseph|Nick Joseph]] —— **新建轻量页**（Anthropic pre-training lead，Karpathy 直属上级）
- [[../entities/Claude Code|Claude Code]] —— 已存在，追加（autoresearch 显式提到"Claude/Codex"作为执行 agent）

## 抽取的概念

- [[../concepts/递归自我改进|递归自我改进 (Recursive Self-Improvement)]] —— **新建**（用 AI 训练 AI / 模型加速产出更好模型 / 与 [[../concepts/Goal-Driven Execution|Goal-Driven Execution]]、[[../entities/Dreams|Dreams]] 同根）
- [[../concepts/Goal-Driven Execution|Goal-Driven Execution]] —— 已存在，追加（autoresearch 是 Karpathy 本人对该原则最纯粹的产业级演示——给 agent 一个 metric (val_bpb)、一个时间预算，循环到达成）
- [[../concepts/原则化指令|原则化指令]] —— 已存在，追加（autoresearch 的 `program.md` 自称"超轻量 skill"，是 CLAUDE.md / SKILL.md 同一脉络）
- [[../concepts/LLM Wiki|LLM Wiki]] —— 已存在，无需大改但可追加交叉引用

## 与已有知识的关系

- **延伸**：补充了 [[../entities/Andrej Karpathy|Karpathy]] 实体页的 2026-05 履历变动 + autoresearch 这条 2026-03 起就铺好的隐藏伏笔
- **延伸**：[[../entities/Anthropic|Anthropic]] 的"用 AI 加速 AI 研发"路线第一次有了具体人选与方法论锚点
- **印证**：与 [[../concepts/Goal-Driven Execution|Goal-Driven Execution]]（"给它成功标准、循环验证直到达成"）完美互文——autoresearch 正是该原则的产业级演示
- **印证**：与 [[../entities/Dreams|Dreams]]（REM 式后台整合）共享"夜里跑、白天看结果"的 ergonomic 范式
- **修正**：把之前从二手"关联背景"猜的 5-20 修正为一手 5/19 推文 + 5/19 当周上工

## 我的批注 / 思考

1. **这条消息触及先生 Wiki 的最高密度节点**：Karpathy（核心人物）+ Anthropic（核心公司）+ 一个全新但前置可考据的工程（autoresearch）+ 与现有 [[../concepts/Goal-Driven Execution|Goal-Driven Execution]]、[[../entities/Dreams|Dreams]] 强共振——典型的"主菜"
2. **递归自我改进**这个概念之前 Wiki 没有独立成页，但 Karpathy + Anthropic 都在用同一思路，值得新建（同时挂 #种子 tag 留待未来 OpenAI / DeepMind 同主题动作扩展）
3. **Karpathy 的叙事一致性令人印象深刻**：autoresearch README 的"meat computers"开篇 + program.md 是"super lightweight skill"——和 [[../concepts/LLM Wiki|LLM Wiki]] Gist、[[../entities/CLAUDE.md|CLAUDE.md]] 4 原则同源；他的工作就是用最少的代码+最少的指令去激发最大的 agent 自主性
4. **Eureka Labs 现状是个伏笔**：从 2024-07 创办到 2026-05 加入 Anthropic 中间公开动作不多，先生可能感兴趣"教育创业实际上没做起来" vs "教育创业被暂停以追更大目标"——两种叙事差异挺大
5. **有 surprise**：原本以为只是个跳槽新闻，溯到 autoresearch 才发现这条线 2026-03 就埋好了——Anthropic 不是凭空决定让 Karpathy "用 Claude 训 Claude"，是他自己已经在 GPU 上跑了两个月并开源（83k 星）证明可行性。**符合 AGENT.md 5.1.bullet "检查 surprise"原则**

## 待深入

- [ ] 找到 Karpathy 在 autoresearch README 引用的两条推文（2029701092347630069 / 2031135152349524125）原文
- [ ] 关注 Nick Joseph 在 Anthropic 的公开发言（他作为 pre-training lead 直接收的 Karpathy）
- [ ] 关注 Eureka Labs 后续是否真的"暂停"或"被收归个人时间"
- [ ] 关注 Anthropic 是否会把 autoresearch 思路在官方博客或论文中扩展披露
- [ ] 横向对照 OpenAI / DeepMind / Meta 在"用 AI 加速 AI 研究"上的同期动作（DeepMind 5/19 同日发了 [[concepts/递归自我改进|Co-Scientist]] 论文，值得另发一条对照）
