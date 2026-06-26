---
type: concept
created: 2026-05-28
updated: 2026-05-28
sources:
  - "[[20260528-Shareuhack-CLAUDE四层架构实战]]"
tags: [方法论, claude, agent, llm, 工程哲学, 已验证]
aliases: [Suggestion vs Law, 建议 vs 法律, Claude Code Hooks]
---

# Hooks 确定性执行

> 一句话定义：**Hooks 是把"建议"变成"法律"的唯一机制**——CLAUDE.md 写"每次都要跑测试"，Claude 在压力情境下常会跳过；Stop Hook 强制跑测试遵守率 100%。**这就是"建议"和"法律"的差距**。

## 核心要义

[[Shareuhack]] 提出的工程哲学，是四层架构中**最被低估**的一层。

核心论证链：
1. **AI 是概率性的**——LLM 在多步骤任务中会"自行判断"哪些步骤"必要"
2. **这不是 bug，是本质**——再精确的 prompt 也只能改变概率分布，无法保证 100%
3. **唯一的解药是把判断权从 LLM 拿回来**——交给确定性的 shell 执行（git hook 同理）
4. **所以 Hooks 是"建议 → 法律"的桥**

## 关键要素

- **Hook 事件类型**：PreToolUse / PostToolUse / Notification / Stop / SubagentStart / SubagentStop（来源: [[20260528-Shareuhack-CLAUDE四层架构实战]]）
- **PreToolUse**：可以 block 工具呼叫（如阻挡 `rm -rf` / `DROP TABLE`）（来源: [[20260528-Shareuhack-CLAUDE四层架构实战]]）
- **PostToolUse**：可以注入验证结果（如 Write 后自动跑 eslint）（来源: [[20260528-Shareuhack-CLAUDE四层架构实战]]）
- **Stop**：结束前强制跑测试（来源: [[20260528-Shareuhack-CLAUDE四层架构实战]]）
- **设定位置**：`.claude/settings.json` 的 `hooks` 字段，不是 CLAUDE.md（常见错误）

## 与相关概念的关系

- 与 [[Goal-Driven Execution]]：GDE 是"循环验证"，Hooks 是把验证从 LLM 自觉变成系统强制
- 与 [[原则化指令]]：原则给"该做什么"的方向，Hooks 兜底"必须做什么"
- 与 [[Agent工程化兜底]]：沙河 rain 的"三层防幻觉" = 把 LLM 不确定性用工程手段兜住，与 Hooks 同源
- **跨域种子**：任何需要确定性的人机系统都适用——电商 SOP、审批流程也是同样的"建议 vs 法律"

## 典型应用 / 案例

- Shareuhack fleet 强制所有 file write 后跑格式检查 (来源: [[20260528-Shareuhack-CLAUDE四层架构实战]])
- 阻挡危险 shell 命令 (rm -rf / force push / DROP TABLE) (来源: [[20260528-Shareuhack-CLAUDE四层架构实战]])
- 本知识库可借鉴：用 git pre-commit hook 强制 ingest 后更新 index/log——这正是当前"建议级"约定的潜在升级 (来源: 自我观察)

## 争议 / 局限

- Hooks 写错会让 Agent 完全卡死，需要良好测试
- 不适合需要灵活判断的场景——"什么时候格式化什么时候不格式化"还是要 LLM 决定

## 相关资料

- [[20260528-Shareuhack-CLAUDE四层架构实战]]
- [[20260528-掘金-MCP协议落地三条铁律]]（Agent 工程化兜底同源）

## 待深入

- [ ] 本库引入 Hooks 层的最小可行实验
