# 📜 操作日志

> 倒序排列：最新在最上面。

- `2026-06-25 10:45 | ingest | 先生纠偏：不是只做 MVP AI Agent，而是系统学习功能完备、好用的 AI Agent 工作台；将《从0搭建小龙虾工作台》作为自产规划资料正式 ingest | 新增 1 raw + 1 summary + 3 concept（AI Agent 工作台 / Agent 工作台能力分层 / Agent 工作台产品化）+ 1 synthesis（功能完备 AI Agent 工作台学习路线）+ index/log 更新；核心收获：MVP 只是训练场，完整工作台要补齐体验、任务、Agent 编排、工具、上下文、数据、治理、可观测与评测 | 影响 7 个文件`

- `2026-06-25 09:15 | ingest | 每日 AI 内容 ingest（非新闻）· 收录 Simon Willison 博文 1 篇：用 Claude Code 将 Moebius 图像 inpainting 模型移植到浏览器（06-22）| 新增 1 raw + 1 summary + 更新 2 concept（Vibe Coding / Agentic Engineering 增补 Moebius 案例）+ index/log 更新；核心收获：(1) Agent 端到端交付可部署产品已可行——PyTorch→ONNX→WebGPU→HuggingFace 发布→GitHub Pages 全链路 Agent 独立完成 (2) "先研究再执行"的 Agent 流水线模式——Claude.ai 可行性研究 → research.md → Claude Code 执行 (3) 信息准备降低 Agent 失败率——提前克隆源码/权重/依赖库 (4) Sub-agent 分担子问题避免污染主 context | 影响 5 个文件；扫描源：Simon Willison/知乎/掘金/HN/Shareuhack；弃用：Context Engineering Guide 2026（Shareuhack 综合二手料→下次单独处理）/产品评测/新闻/泛综述 | 保留 Agentic Engineering 一手实践`

- `2026-06-24 09:15 | ingest | 每日 AI 内容 ingest（非新闻）· 收录 Simon Willison 博文 2 篇：Claude Fable 极限自主性（06-11）+ Prompt Injection 角色混淆（06-22，ICML 2026 论文解读）| 新增 2 raw + 2 summary + 4 entity（Charles Ye/Jasmine Cui/Dylan Hadfield-Menell/Claude Fable 5）+ 4 concept（角色混淆攻击/去风格化防御/Agent 自主工具链构建/Coding Agent 安全沙箱）+ index/log 更新；核心收获：(1) LLM 按风格判断角色而非标签，去风格化降攻击率 61%→10% (2) 前沿 Agent 可现场发明完整工具链，沙箱从可选变必须 | 影响 14 个文件；扫描源：Simon Willison/HN/知乎/掘金；弃用：新闻/纯产品发布/泛综述，保留一手体验 + 安全研究`


> 格式：`YYYY-MM-DD HH:MM | <类型> | <摘要> | <影响>`
> 类型：`ingest` / `query` / `maintain` / `proposal` / `agent-update` / `human-edit` / `init` / `scan`

---

- `2026-06-08 09:15 | ingest | 每日 AI 内容 ingest（非新闻）· 收录知乎 SkillFactory 实践，溯源 Trace2Skill arXiv/GitHub 与 Anthropic Skills | 新增 1 raw + 1 summary + 2 entities（SkillFactory/Trace2Skill）+ 4 concepts（Skill工厂/评测驱动Skill生成/轨迹蒸馏为技能/多路并发竞优），更新 Skills 2.0 模块化与 index；核心收获：Skill 生产从“写 Markdown”转为失败诊断、测试驱动、多路竞优、轨迹蒸馏 | 影响 10 个文件；扫描源：知乎/掘金/Simon Willison/HN/Karpathy/arXiv；弃用：新闻/纯产品发布/泛综述，保留作者实践复盘 + 一手论文溯源`
- `2026-05-28 09:30 | ingest | 每日 AI 巡检（知识图谱定时任务）· 合格资料 3 份，全部 ingest | 【主菜 1】Anthropic 收购 Stainless（SDK/MCP 工具链）→ 战略布局 Agent 连接能力，6 个新建实体（Stainless/MCP/Thrive Holdings/Crete/Symphony/Simon Willison）+ 11 个新建概念（Agent 连接性/从模型到 Agent/Agent 自改进/生产轨迹驱动开发/领域专家+AI协同/Harness Engineering/PMF/Agent商业化/Token经济/2025年11月拐点/SDK生成）【主菜 2】OpenAI 自改进税务 Agent → Codex 生产级自改进循环里程碑，准确率 25%→97% 【主菜 3】Simon Willison PMF 分析 → 编码 Agent 带来真正产品市场契合，企业按 token 付费，Anthropic 即将首次盈利 | 影响 33 个文件：3 raw + 3 summaries + 6 新建 entities + 11 新建 concepts + index/log 全面更新 | 扫描源：Anthropic News / OpenAI News / Simon Willison Blog / Hacker News / arXiv
- `2026-05-28 06:30 | ingest | 每日 AI 巡检（定时任务 studio_job_4）· 合格资料 3 份，全部 ingest | 【主菜 1】OpenAI 税务 AI 自改进循环（Codex 首个大型生产级案例）→ 实体 [[Chris Olah|Chris Olah]] 新建 + [[Codex]] 更新 + [[递归自我改进]] 概念大幅扩展 【主菜 2】Simon Willison PMF 分析 → 行业商业化拐点信号 【主菜 3】Chris Olah 梵蒂冈演讲 → #种子节点 跨域伦理视角 | 影响 9 个文件：3 raw + 3 summaries + 1 新建 entity + 2 存量 entity/concept 更新 + index/log 更新 | 扫描源：Anthropic News / OpenAI Engineering Blog / Simon Willison Blog
- `2026-05-27 23:30 | maintain | 首次全库审计（先生授权 Jarvis 执行）· 产出 [[../syntheses/20260527-审计报告|首次审计报告]] | 扫描全部 60 页的引用图谱，决策：(1) index Tag 一览从装饰性列表改为活跃 tag + 长尾池二分 (2) 健康度表新增「累计对外产出物」输出 KPI (3) 验证无孤儿 entity（最低 2 引用），撤销马斯克镜片「要刪实体」的判断 (4) 验证无断链，反链密度合格 (5) 识别 5 项需先生决策项留在审计报告 | 影响 3 个文件：syntheses 新增审计报告 + index.md 修订 + 本 log`
- `2026-05-27 23:25 | query | 「用马斯克视角看知识库 + 建议提升」（先生调用）· Jarvis 输出 4 个马斯克问题拆解 + 3 个具体建议，诊断本库「结构健康 + 输出回路缺失」，先生确认输出由外部任务承担，本库仅需优化结构 | 未新增 wiki 页，仅产出决策输入 → 触发后续 maintain`
- `2026-05-27 12:10 | ingest | 录入知乎《卡尔的AI沃茨 · 淘金小镇 Skill 榜单情报项目》（应用篇/Goal 模式工程验证）| 影响 11 个文件：1 raw + 1 summary + 6 新建 entity（卡尔/淘金小镇/ClawHub/Codex/Convex/LearnPrompt）+ 3 新建 concept（Skill 榜单情报化/复刻用户视角拿数据/Goal 模式自动化爬虫）+ 1 存量 concept 大幅扩展（Goal-Driven Execution 加入工程验证案例）+ index/log`
- `2026-05-26 11:00 | ingest | 每日 AI 巡检（手动测试）· 录入 Karpathy 加入 Anthropic 预训练团队（2026-05-19 事件，一手源）| 影响 9 个文件：1 raw + 1 summary + 3 新建（entity Nicholas Joseph / entity Eureka Labs / concept 递归自我改进）+ 2 存量 entity 修订（Karpathy · Anthropic · 含 05-20→05-19 日期修正）+ 1 综述（剧情闭环）+ index/log`
- `2026-05-26 11:00 | scan | 今日 AI 巡检（手动测试）· 扫描 Anthropic/OpenAI/DeepMind/Karpathy X/arXiv | 找到 5 条候选，ingest 1 主菜，其余下方列表`
- `2026-05-26 11:00 | agent-update | 修正一次红线违规：误在知识库顶级建了 syntheses/ 目录，已移到 wiki/syntheses/ 并删除空目录 | 修复 1 个目录结构错误`
- `2026-05-26 14:30 | agent-update | AGENT.md 升级 · 并入 6 项原则 | 修订 AGENT.md 1 个文件`
- `2026-05-26 14:25 | proposal | 先生批准「二手必溯一手」＋「反信息茧房（跨域种子节点）」为正式卍议 | 启动 AGENT.md 升级`
- `2026-05-26 14:00 | ingest | 录入知乎《Claude「永久大脑」真的来了》— Anthropic 三件套 (Memory Files / Dreams / Conway) | 影响 12 个文件：1 raw + 1 summary + 4 新建 entity(Anthropic/Memory Files/Dreams/Conway) + 1 新建 concept(REM 睡眠式记忆整合) + 3 存量页修订(LLM Wiki/Maintain/Claude Code) + 1 综述(理念vs产品化) + index/log`
- `2026-05-26 11:50 | ingest | 录入 GitHub 一手源 multica-ai/andrej-karpathy-skills(CLAUDE.md 原仓库) | 影响 13 个文件：1 raw + 1 summary + 2 新建 entity(Multica/Cursor) + 3 新建 concept(Simplicity First/Surgical Changes/Goal-Driven Execution) + 4 存量页大幅修订(CLAUDE.md/forrestchang/三宗罪/TBC) + 1 综述 + index/log`
- `2026-05-26 11:30 | ingest | 录入知乎《CLAUDE.md 神文件让 Claude Code 听话》(应用篇,二手源,截断) | 影响 8 个文件：1 raw + 1 summary + 2 新建 entity + 3 新建 concept + Karpathy/Claude Code 两个存量实体追加 + index/log`
- `2026-05-26 11:50 | proposal | 基于本次"二手 vs 一手"教训,建议 AGENT.md 增加:§ 2.1 二手源识别+一手源溯源 / § 3 数字事实必标(截至 YYYY-MM-DD) / § 2.3 框架化叙述盲点检查 | 待先生批准`
- `2026-05-24 09:50 | ingest | 录入两篇知乎文章(理念篇 + 实操篇) | 影响 16 个文件：2 raw + 2 summary + 6 entity + 7 concept + 1 synthesis + index 更新`
- `2026-05-24 09:30 | init | 知识库初始化 | 由 Hana 按 Karpathy 方法论搭建三层结构`

---

- `2026-06-05 09:30 | maintain | 补登 6/4~6/5 cron 产出 — 4 篇新内容（Simon Willison ×3 + OpenAI Harness Engineering + Latent Space Token Town）全部补入 index | 96→100 页

- `2026-06-03 09:30 | maintain | 补全积压 ingest 登记 — 6/1~6/3 三次定时任务 + 两次手动测试共 10 篇文章的未完成 ingest 全部补入 index+log | 影响：18 summaries+18 raw+42 entities+42 concepts+5 syntheses = 63→95 页。文章来源覆盖 掘金/知乎/BearBlog/SimonWillison/Anthropic(技术文)/RubyChina/36氪/Shareuhack。概念方向：Agentic Engineering/Vibe Coding/上下文工程/验证瓶颈 等方法论类 | 影响 1 个文件（index.md）

- `2026-06-01 08:45 | ingest | 先生指定 digest 知乎文章《Obsidian 七种主流多端同步方式对比与实践》— 工具篇 / #种子节点 / 本地优先 vs 多端同步工程实践 | 作者 [[阿浩的笔记]] 创建，[[Obsidian]] 补充多端同步方案，新增 1 raw + 1 summary + 1 entity + index/log 更新 | 影响 5 个文件

- `2026-05-28 09:35 | rollback | 先生判定昨日 ingest 三条均为「新闻」非「内容」，全部回滚 | 删除 31 个文件：6 raw + 6 summary + 7 entity（Chris Olah/Stainless/MCP/Thrive/Crete/Symphony/Simon Willison）+ 12 concept（递归自我改进/从模型到 Agent/Agent 连接性/SDK 生成/Agent 自改进/生产轨迹驱动开发/领域专家+AI 协同/Harness Engineering/产品市场契合 PMF/Agent 商业化/Token 经济/2025 年 11 月拐点）。Codex 实体保留并重建为干净版（去除税务 AI 内容污染，回归 5/27 卡尔淘金小镇起源）。index.md 同步清理失效登记。教训：「新闻 vs 内容」是新的硬过滤标准——新闻=事件发生了什么，内容=人对事件的思考与方法论沉淀，只收后者 | 影响 ~35 文件（31 删 + Codex 重写 + index 修订 + log 本条）

## 今日巡检候选清单（2026-05-26 11:00）

扫描覆盖源：Anthropic news / OpenAI news / Google DeepMind blog / Karpathy X / arXiv / Reuters AI / TechCrunch AI

**主菜（1 条，已 ingest）**：
- **Karpathy 加入 Anthropic 预训练团队**（2026-05-19, 一手源 X+发言人邮件）—— 本知识库两大主角人事级闭环，重中主题

**候选（4 条，记入清单等先生拍板）**：

1. **OpenAI Deployment Company 创立 + 收购 Tomoro**（2026-05-11, 一手源 https://openai.com/index/openai-launches-the-deployment-company/）
   - 估值：$4B 初始投入，带 150 个 FDE。主解决“企业部署”深水区。距本知识库主线（LLM Wiki / Karpathy / Anthropic）略远，但与先生本职位（AI 运营）隐含相关——“企业怎么落地 AI”是您可能关心的。
   - 建议：下次如遇“企业 AI 落地/FDE 模式/商业化”主题再集中 ingest。
2. **GPT-5.5 发布**（2026-04-23，已过一个多月）—— 不是“今日”动态，且本知识库不以模型发布为重点。弃。
3. **Google I/O 2026 / Gemini Omni · Gemini 3.5 · AlphaEvolve**（2026-05-20 前后）—— 一手源充足（deepmind.google/blog · blog.google），但需要专项 Google 生态 ingest（一口气装不下）。本周暂弃，建议先生未来主动调度一次专项。
4. **Sam Altman: AI 不会带来“jobs apocalypse”**（Reuters, 2026-05-26）—— 是访谈表态，不到“组建独立节点”门槛。弃。

**弃用原因归纳**：
- 年代不对口（1 条）
- 与主线弱关联但量大（1 条）
- 表态类、不够独立成页（1 条）
- 与本职位弱相关但不是主线（1 条，已入候选等拍板）

---

## 历史 ingest 详情(2026-05-26 11:50)— GitHub 一手源补全

**输入**：
- [[../raw/20260526-GitHub-andrej-karpathy-skills原仓库|raw/20260526-GitHub-...]] —— ⭐ 一手源,4 条原则齐全

**新建文件**(7 个)：
- summaries × 1：20260526-GitHub-andrej-karpathy-skills原仓库
- entities × 2：Multica / Cursor
- concepts × 3：Simplicity First / Surgical Changes / Goal-Driven Execution
- syntheses × 1：20260526-二手源vs一手源-CLAUDE.md的两次ingest教训

**大幅修订文件**(4 个)：
- entities/CLAUDE.md.md — 从"1.5 条原则"补全到 4 条 + tradeoff 声明 + 工程交付细节,star 数刷新 10.2 万 → **15.5 万**
- entities/forrestchang.md — 补全本名 Jiayuan Zhang / X @jiayuan_jy / Multica 创办人身份
- concepts/LLM 编程三宗罪.md — **重大修正**：实际是"4 个观察"(3 缺陷 + 1 优势),保留原名 + 加修正说明
- concepts/Think Before Coding.md — 补全 4 条具体子条款 + 原文金句

**更新元文件**(2 个)：
- index.md(登记 6 个新页 + 健康度 16→**31** + 新标签)
- log.md(本条)

**关键发现**：
1. **数据时效失真**：知乎引用的"10.2 万 star"已过时,实际 **15.5 万**(涨 52%)
2. **核心洞察丢失**：知乎只提"三宗罪"(前 3 条),完全漏掉**第 4 条 [[../concepts/Goal-Driven Execution|Goal-Driven Execution]]**——这是 Karpathy"给它成功标准,看着它完成"的关键洞察,**性质完全不同**(前 3 防错,第 4 激发优势)
3. **溯源链断裂**：知乎未提 Karpathy 原始推文 ID(2015883857489522876)
4. **延伸视野缺失**：知乎未提 forrestchang 创办的 [[../entities/Multica|Multica]] 平台
5. **工程交付维度坍缩**：知乎只讲"一个 MD",一手源还有 Claude Code 插件 + Cursor 规则 + 14.8KB EXAMPLES 案例库

**沉淀为方法论**(写入 [[../syntheses/20260526-二手源vs一手源-CLAUDE.md的两次ingest教训|教训综述]])：
1. 优先一手源(看到二手解读先查能否追溯原始仓库/推文/论文)
2. 警惕框架化叙述(二手用某概念套新事物会过滤"框架外"信息)
3. 数字事实必标 `(截至 YYYY-MM-DD)`
4. ingest 完成后回头检查"有没有 surprise"
5. 新发现修正既有页,不新建并行页

**待先生决策**：
- 是否批准把上述 5 条教训写入 [[../../AGENT|AGENT.md]] § 2.1 / § 3 / § 2.3?
- 是否继续 ingest EXAMPLES.md(14.8KB 案例库)和 Karpathy 原始推文?
- 是否调研 Multica 平台并独立扩展实体页?

---

## 本次 ingest 详情(2026-05-26 11:30)— 知乎二手版

**输入**：
- [[../raw/20260526-知乎-CLAUDE.md神文件让ClaudeCode听话|raw/20260526-知乎-...]] ⚠️ 正文被知乎截断,仅得到前 2 条原则

**新建文件**(6 个)：
- summaries × 1：20260526-知乎-CLAUDE.md神文件让ClaudeCode听话
- entities × 2：forrestchang / CLAUDE.md
- concepts × 3：LLM 编程三宗罪 / Think Before Coding / 原则化指令

**更新文件**(4 个)：
- entities/Andrej Karpathy.md(追加三宗罪洞察 + 新来源)
- entities/Claude Code.md(追加 CLAUDE.md 案例 + 新来源)
- index.md
- log.md

**关键观察**：
- 三篇文章完美闭环：**理念篇 → 实操篇 → 应用篇**
- 哲学同源响应:CLAUDE.md(4 条原则)与本知识库 AGENT.md 同构
- 截断问题:知乎未登录只能读正文前半 → 触发了下一次"一手源补全"

---

## 本次 ingest 详情(2026-05-24 09:50)

**输入**：
- [[../raw/20260407-知乎-Karpathy开源Agent知识库|raw/20260407-...]]
- [[../raw/20260413-知乎-Qwen Code+Obsidian搭建Karpathy知识库|raw/20260413-...]]

**新建文件**(14 个)：
- summaries × 2：理念篇 + 实操篇
- entities × 6：Andrej Karpathy / Obsidian / Claude Code / Qwen Code / obsidian-agent-client / BRAT
- concepts × 7：LLM Wiki / RAG / 三层架构 / Ingest 录入 / Query 查询 / Maintain 维护 / AGENT.md 协议 / 知识复利
- syntheses × 1：理念 vs 实操对比综述

**更新文件**(2 个)：
- index.md(登记所有新页 + 健康度)
- log.md(本条)

**关键观察**：
- 两篇文章互补性强,一篇理念一篇实操
- 关键差异:Agent 后端选择(Claude Code vs Qwen Code),先生最终选了方案 A(不走任何 CLI)
- 标矛盾点 0 个——两篇没有实质冲突
- 未来追查线索：B 站 BV1p4DeB8ECi 视频里的 up 主版 AGENT.md / Karpathy 原始 Gist 链接
- `2026-06-16 test`
