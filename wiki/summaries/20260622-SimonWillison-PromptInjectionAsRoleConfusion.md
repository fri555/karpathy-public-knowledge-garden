---
type: summary
created: 2026-06-24
updated: 2026-06-24
sources:
  - "[[20260622-SimonWillison-PromptInjectionAsRoleConfusion]]"
source_tier: 一手源
tags: [ai, llm, agent, 安全, prompt注入, 方法论]
---

# Prompt Injection as Role Confusion — 提示注入即角色混淆

> Simon Willison 对 ICML 2026 论文的解读。核心发现：LLM 判断"谁在说话"时，文本风格权重远超角色标签。

## 核心论点

**角色标签不可靠**。模型在区分 `<system>` / `<assistant>` 等特权标签与 `<user>` 等用户输入时，更看重文本的**写作风格**而非实际的 XML 标签。这从根本上动摇了当前基于角色标签的提示注入防御体系。

## 关键事实

- **风格优先级实验**：将用户输入改写为系统风格后，模型会将用户文本误判为系统指令，攻击成功率可达 61%
- **去风格化（Destyling）防御**：用略微不同的措辞改写相同内容后，攻击成功率从 61% 暴跌至 10%——这种对人类几乎不可见的变化，对 LLM 产生了巨大影响
- **根本问题**：模型缺乏真正的"角色感知（role perception）"能力，它不是在判断"谁在说话"，而是在模式匹配"这种文本通常属于哪个角色"
- **论文出处**：Charles Ye, Jasmine Cui, Dylan Hadfield-Menell @ MIT, ICML 2026, arXiv:2603.12277
- **Willison 评价**："I wish every paper would come with a blog-style writeup"

## 引用原文

> "To a human reader, these two versions say the same thing. But to the LLM, the difference is enormous: destyling causes average attack success in our dataset to plunge from 61% to 10%. A change nearly invisible to humans completely changes the LLM's role perception."

> "Unless LLMs achieve genuine role perception, we think injection defense will remain a perpetual whack-a-mole game."

## 来源

- Simon Willison 博文：https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/
- 论文官网：https://role-confusion.github.io/
- HN 讨论：https://news.ycombinator.com/item?id=48631888

## 提取实体

- [[Charles Ye]] — MIT 研究者，论文第一作者
- [[Jasmine Cui]] — MIT 研究者
- [[Dylan Hadfield-Menell]] — MIT 研究者

## 提取概念

- [[concepts/角色混淆攻击|角色混淆攻击（Role Confusion）]] — 新建
- [[concepts/去风格化防御|去风格化防御（Destyling）]] — 新建
- 关联：[[concepts/工具调用幻觉|工具调用幻觉]] — LLM 缺陷家族的新成员
- 关联：[[concepts/提示注入|提示注入]] — 需更新加入此攻击向量
