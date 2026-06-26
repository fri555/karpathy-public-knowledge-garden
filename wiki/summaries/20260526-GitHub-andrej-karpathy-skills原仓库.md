---
type: summary
created: 2026-05-26
updated: 2026-05-26
source_file: "[[raw/20260526-GitHub-andrej-karpathy-skills原仓库]]"
source_url: https://github.com/multica-ai/andrej-karpathy-skills
source_author: forrestchang (Jiayuan Zhang)
source_date: 2026-01-27
tags: [ai, llm, agent, claude, cursor, prompt工程, 方法论, 一手源, 已验证]
---

# 20260526 · GitHub · andrej-karpathy-skills 原仓库

> 一句话摘要:这是 [[entities/CLAUDE.md|CLAUDE.md]] 神文件的**一手源 GitHub 仓库**,完整 4 条原则齐全,补全了 [[20260526-知乎-CLAUDE.md神文件让ClaudeCode听话|知乎二手文章]]被截断的内容,并揭示了重要修正:**不是"三宗罪 → 四原则"凑数,而是 Karpathy 4 个观察精准对应 4 个原则**。

## 核心论点(基于一手源)

1. **一对一映射**:[[forrestchang]] 总结的不是"三宗罪",而是 Karpathy 在推文中的 **4 个独立观察**——前 3 个讲"LLM 会犯什么错",第 4 个讲"LLM 的真正优势是循环执行"。
2. **正向 + 反向并存**:前 3 条原则在"防错",第 4 条 [[Goal-Driven Execution]] 在"激发优势"——这一点知乎文章完全没提,是被截断的关键信息。
3. **明确的 tradeoff 声明**:CLAUDE.md 开头就写"This guidelines bias toward caution over speed. For trivial tasks, use judgment.",承认不是万能,小事自己判断。
4. **可执行的工程化交付**:不仅是文档,还包含 Claude Code 插件清单(`.claude-plugin/`)、Cursor 规则(`.cursor/`)、案例库(EXAMPLES.md, 14.8KB)——是工程产品而非纯思想。

## 关键事实 / 数据(刷新自一手源)

- **GitHub Star**:**155,338**(知乎文章里的 10.2 万已过时,实际 **15.5 万**)
- **Fork**:15,932
- **CLAUDE.md 文件大小**:2,357 字节 ✓(知乎"2.3K"基本准确)
- **仓库创建**:2026-01-27
- **最近 push**:2026-04-20
- **作者**:[[forrestchang]](Jiayuan Zhang)· X: @jiayuan_jy
- **仓库现归属**:[[Multica|multica-ai]] 组织(forrestchang 创办的新项目)
- **Karpathy 原始推文 ID**:2015883857489522876

## 原文金句(英文原版)

> "Don't assume. Don't hide confusion. Surface tradeoffs." —— 第 1 条原则的副标题

> "If you write 200 lines and it could be 50, rewrite it." —— 第 2 条原则的具体指标

> "Every changed line should trace directly to the user's request." —— 第 3 条原则的检验标准

> "Strong success criteria let you loop independently. Weak criteria ('make it work') require constant clarification." —— 第 4 条原则的精髓

## Karpathy 4 个原始观察(来自 X 推文,经 README.zh.md 翻译)

1. "模型会代你做错误假设,然后不假思索地执行。它们不管理自身的困惑,不寻求澄清,不呈现矛盾,不展示权衡,在应该提出异议时也不反驳。"
2. "它们真的很喜欢把代码和 API 搞复杂,堆砌抽象概念,不清理死代码……"
3. "它们有时仍会改动或删除自己理解不足的代码和注释,即使这些内容与任务本身无关。"
4. "LLM 非常擅长循环执行直到达成特定目标……不要告诉它该做什么,**给它成功标准**,然后看着它完成。"

## 抽取的实体

- [[forrestchang]](已存在,本次追加 X 账号 + Multica 创办者身份)
- [[CLAUDE.md]](已存在,本次大幅补全 4 条完整原则)
- [[Andrej Karpathy]](已存在,本次追加原始推文链接)
- [[Multica]] —— forrestchang 的新开源平台(新建)
- [[Claude Code]](已存在,本次追加插件市场链接)
- [[Cursor]] —— 同样支持本仓库规则(新建)

## 抽取的概念

- [[Think Before Coding]](已存在,本次补全 4 条具体子条款)
- [[Simplicity First]] —— 第 2 条原则(新建)
- [[Surgical Changes]] —— 第 3 条原则(新建)
- [[Goal-Driven Execution]] —— 第 4 条原则,本次最大新发现(新建)
- [[原则化指令]](已存在,本次印证)

## 与已有知识的关系

- **重大修正 [[LLM 编程三宗罪]]**:严格说应叫"LLM 编程 **4 个观察**"——前 3 罪 + 1 优势。我之前页面命名失准,已在页面顶部加修正说明
- **补全 [[CLAUDE.md]]**:从"只知 1.5 条原则"到"4 条全齐 + 子条款 + tradeoff 声明"
- **延伸 [[forrestchang]]**:从"开发者"到"Multica 平台创办者"
- **形成新综述**:本次"二手源 vs 一手源"的对比本身就值得沉淀(见 syntheses/)

## 我的批注 / 思考

- **教训**:知乎二手解读不仅截断,还**漏掉了最重要的第 4 条原则(Goal-Driven)**——这恰恰是 Karpathy 强调"给它成功标准"的关键洞察。**永远优先一手源**。
- **数据感**:155K star / 15.9K fork 印证了"原则化指令"范式的市场需求——比绝大多数开源项目都火。
- **对本协议的启示**:第 4 条 Goal-Driven Execution 完全可以借鉴到本知识库——把 ingest/maintain 流程从"步骤式"改写成"目标式":
  - 现状:`步骤 1 → 步骤 2 → ...`
  - 可优化:`目标 = 影响 5-15 个页面 + 0 矛盾 + log 已写 → 循环验证`
- **看到 EXAMPLES.md(14.8KB)**:还有 14.8KB 案例库没读,值得后续单独 ingest

## 待深入

- [ ] 单独 ingest EXAMPLES.md(14.8KB 案例库),看 4 条原则的具体落地范例
- [ ] 抓 Karpathy 那条原始推文(ID 2015883857489522876)的英文原文
- [ ] 调研 Multica 平台,做独立实体页扩展
- [ ] 写一篇综述:"四原则 vs 本知识库 AGENT.md" 设计哲学对比
- [ ] 考虑是否把这 4 条原则纳入先生自己的开发工作流(在常用代码仓库根目录放 CLAUDE.md)
