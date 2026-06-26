---
type: concept
created: 2026-05-26
updated: 2026-05-26
sources:
  - "[[20260526-GitHub-andrej-karpathy-skills原仓库]]"
tags: [llm, agent, prompt工程, 原则, 已验证]
aliases: [精准修改, 最小手术]
---

# Surgical Changes

> 一句话定义:[[CLAUDE.md]] 神文件第 3 条原则——**只碰必须碰的,只清理自己造成的混乱**(Touch only what you must. Clean up only your own mess.)。

## 核心要义

针对 [[LLM 编程三宗罪]] 第 3 条:LLM 喜欢"顺手优化"无关代码——改注释、改格式、删它认为没用的代码,把简单的编辑搞成大范围 diff。

编辑现有代码时的规则 (来源: [[20260526-GitHub-andrej-karpathy-skills原仓库]]):
- 不要"改进"相邻代码、注释或格式
- 不要重构没坏的东西
- 匹配现有风格,**即使你更倾向于不同的写法**
- 如果注意到无关的死代码,提一下——**不要删除它**

产生孤儿代码时:
- 删除因你的改动而变得无用的导入/变量/函数
- 不要删除预先存在的死代码,除非被要求

**检验标准**:**Every changed line should trace directly to the user's request.**(每一行修改都应该能直接追溯到用户的请求)

## 关键要素

- **黄金法则**:每行 diff 都要能追溯到请求
- **风格匹配**:即使你更喜欢另一种写法,也要服从既有风格——这反 LLM 本能
- **死代码区分**:你造成的孤儿要清,既有的死代码不要碰

## 与相关概念的关系

- **解药对应**:专治 [[LLM 编程三宗罪]] 第 3 条
- **同源思想**:与 Git 提交规范"一次提交只做一件事"同源
- **属于**:[[原则化指令]] 范式
- **延伸到知识库**:本协议也可借鉴——ingest 单份资料时,不要顺手改无关页面

## 典型应用 / 案例

- [[CLAUDE.md]] 神文件第 3 条原则 (来源: [[20260526-GitHub-andrej-karpathy-skills原仓库]])
- Code Review 中识别"AI 越界改动"的检查项

## 争议 / 局限

- 严守"不动相邻代码"会错过真正该修的关联 bug
- 团队若希望 AI 顺手改进代码质量,此原则会拖慢演进
- 对"格式不规范的遗留代码库",硬性"匹配现有风格"反而固化烂代码

## 相关资料

- [[20260526-GitHub-andrej-karpathy-skills原仓库]]
- [[CLAUDE.md]]
- [[LLM 编程三宗罪]]

## 待深入

- [ ] 收集 AI "顺手优化"反而引入 bug 的具体案例
- [ ] 评估本知识库 ingest 流程是否需要类似"surgical"约束
