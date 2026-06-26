---
type: summary
created: 2026-05-28
updated: 2026-05-28
source_file: "[[../raw/20260528-Shareuhack-CLAUDE四层架构实战|raw/20260528-Shareuhack-CLAUDE四层架构实战]]"
source_url: https://www.shareuhack.com/zh-TW/posts/claude-code-claudemd-skills-setup-guide-2026
source_author: Shareuhack（AI fleet 主理人）
source_date: 2026 年（具体月份未标）
source_tier: 二手源-内容型
tags: [claude, agent, llm, 方法论, 案例, 架构, prompt工程, 工作流, 已验证]
---

# 20260528 · Shareuhack · CLAUDE.md + Skills + Hooks + Memory 四层架构实战

> 一句话摘要：自运营 6-Agent fleet 的 Shareuhack 团队基于第一手生产经验，把 Claude Code 的混乱配置拆成 **CLAUDE.md（宪法）/ Skills（SOP）/ Hooks（强制法）/ Memory（学习记录）** 四层分工矩阵——核心洞察是"AI 是概率性的，所以建议靠 Hooks 升级为法律"。

## 核心论点

1. **CLAUDE.md 是行为宪法，不是 README**。每个 session 全量载入、优先级高于对话指令——把它当 README 写是根本性误解
2. **四层各有不该放的东西**（这才是关键）：
   - CLAUDE.md 不放步骤型指令（用 Skills）
   - Skills 不放永久规则（放 CLAUDE.md）
   - Hooks 不放灵活判断（那是 AI 的事）
   - Memory 不放不变规则（放 CLAUDE.md）
3. **Hooks 是把"建议"变"法律"的唯一机制**。CLAUDE.md 写"每次都要跑测试"，Claude 在压力情境下常会跳过——**这不是 bug，是 LLM 概率本质**。Stop Hook 强制跑测试遵守率 100%
4. **Skills 2.0 是 folder-based 模块**：`.claude/skills/{name}/SKILL.md` + `scripts/` + `references/`，on-demand 载入。Shareuhack 自己有 20+ Skills，**全塞 CLAUDE.md 会超过 5000 行无法运作**
5. **三套记忆系统不能混用**：CLAUDE.md（人写的规则）/ Auto Memory（Claude 写的笔记）/ Session Memory（系统写的状态）——**混用是 Agent 不稳定的最常见原因**
6. **`.claude/rules/` 路径作用域**：让 CLAUDE.md 从静态文件进化成动态规则引擎，前端文件只载入 frontend.md 规则
7. **架构哲学差异**：Claude Code = 规则+强制+模块；Gemini CLI = Plan Mode 谨慎型；System Prompt = 灵活无保障
8. **Top 5 常见错误**：CLAUDE.md 过长（>300 行该拆 rules）/ Skills 未迁移 2.0 / Hooks 写错位置 / Auto Memory 与 CLAUDE.md 混用 / 忘记建 CLAUDE.local.md

## 关键事实 / 数据

- Shareuhack 自家 fleet：Sage、Mia、Luna、Rex 等 **6 个 agents**(截至 2026-05)，从选题到发布全流程无人值守
- 20+ Skills，5000 行经验阈值
- 社区生态：awesome-claude-code **28,500+ 资源**(截至 2026-05)；awesome-claude-code-toolkit 含 **135 agents / 35 Skills / 42 commands / 176+ plugins / 20 hooks**(截至 2026-05)
- antigravity-awesome-skills **1,400+ 跨 agent Skills**(截至 2026-05)，支持 Claude Code/Codex/Gemini CLI/Cursor

## 原文金句

> "CLAUDE.md 不是给 Claude 看的 README，是行为宪法（Constitution）——每个 session 强制全量载入。"

> "AI 天生是概率性的。即使你在 CLAUDE.md 写明'每次修改程式碼後必須跑 lint'，Claude 在某些情境下仍可能跳過——這不是 bug，而是語言模型的本質。"

> "CLAUDE.md 裡寫'每次都要跑測試'，遵守率不穩定。設定 Stop Hook 強制跑測試，遵守率是 100%——這就是'建議'和'法律'的差距。"

> "最常見的問題不是'不知道有這些功能'，而是'把所有東西塞進 CLAUDE.md'。"

## 抽取的实体

- [[../entities/CLAUDE.md|CLAUDE.md]] — 关联，本文给它补全了"4 层架构中的定位"维度
- [[../entities/Claude Code|Claude Code]] — 关联，本文是其完整设定指南
- [[../entities/Shareuhack|Shareuhack]] — 新建（自运营 6-Agent fleet 的内容团队）

## 抽取的概念

- [[../concepts/CLAUDE.md四层架构|CLAUDE.md 四层架构]] — 新建 ⭐ 核心
- [[../concepts/Hooks确定性执行|Hooks 确定性执行]] — 新建 ⭐ "建议 vs 法律"
- [[../concepts/Skills 2.0模块化|Skills 2.0 模块化]] — 新建
- [[../concepts/三套记忆系统|三套记忆系统]] — 新建
- [[../concepts/路径作用域规则|路径作用域规则]] — 新建
- [[../concepts/原则化指令|原则化指令]] — 关联（同源）

## 与已有知识的关系

- **重要补全**：[[../entities/CLAUDE.md|CLAUDE.md]] 实体页之前讲的是 forrestchang 的"4 条原则"，本文补全了 **CLAUDE.md 在整个配置体系中的层级地位**——它是 4 层之一，不是全部
- **印证 + 升级**：[[../concepts/原则化指令|原则化指令]] 之前只讲"少量原则"，本文升级到"**规则放哪一层** 才是更深的工程问题"
- **强连接**：[[../concepts/Goal-Driven Execution|Goal-Driven Execution]] 中"定义成功标准 + 循环验证"——Hooks 就是把"验证"从 LLM 自觉变成系统强制的工程化兑现
- **跨流派印证**：[[summaries/20260528-36氪-Saboo30天6Agent复盘|Saboo 30 天复盘]] 中"记忆 vs 技能文件拆开" = Shareuhack 的 "CLAUDE.md vs Skills 拆开" + "Auto Memory vs CLAUDE.md 拆开"——**两个独立团队基于实战收敛到了同一套二分法**

## 我的批注 / 思考

- **本知识库的镜像应用**：先生的 AGENT.md（本库协议）= CLAUDE.md，skills/ 目录 = Skills，但**缺 Hooks 这一层**——是否需要把"ingest 后必须更新 index 和 log"这种"建议"用 git hook 或 CI 升级为"法律"？
- **盲点警报**：本文未提"什么时候 CLAUDE.md 反而应该长"——所有建议都倾向于"精简"，但有些项目就是需要密集的禁止事项。需要追问
- **作者偏见**：Shareuhack 自家在卖 awesome-claude-code-toolkit 的内容服务，所以推 Skills 生态可能略夸大。但四层架构本身的工程逻辑独立成立
- **跨域种子**：Hooks "建议 vs 法律"的二分法可以借给**任何需要确定性的人机系统**——电商 SOP、内部审批流程也适用

## 待深入

- [ ] 抓 Anthropic 官方 Claude Code Hooks 文档对齐
- [ ] 评估本库要不要加 ingest 后 git pre-commit hook 强制更新 index/log
- [ ] 与 Saboo 复盘合写综述"两条独立路径都收敛到了拆分"
