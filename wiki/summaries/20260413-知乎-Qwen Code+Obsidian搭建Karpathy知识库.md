---
type: summary
created: 2026-05-24
updated: 2026-05-24
source_file: "[[20260413-知乎-Qwen Code+Obsidian搭建Karpathy知识库]]"
source_url: https://zhuanlan.zhihu.com/p/2026602422873637335
source_author: 菠萝吹雪
source_date: 2026-04-13
tags: [ai, llm, agent, 工具, 教程, 知识管理]
---

# 20260413-知乎-Qwen Code+Obsidian搭建Karpathy知识库

> 一句话摘要：[[菠萝吹雪]] 在 Windows 下用 [[Qwen Code]] + [[Obsidian]] + [[obsidian-agent-client]] 三件套，复刻了 [[Andrej Karpathy]] 的 [[LLM Wiki]] 工作流。

## 核心论点

1. **三步走的最小可行方案**：装 Qwen Code → 装 Obsidian + obsidian-agent-client 插件 → 把 Karpathy 方法论文档喂给 agent 让它自动建结构
2. **国产化替代**：原 Gist 用 [[Claude Code]] / [[Codex]]，本方案换成 [[Qwen Code]]——对国内网络更友好
3. **BRAT 路径**：第三方 Obsidian 插件（如 obsidian-agent-client）推荐用 [[BRAT]] 安装，比手动下文件可靠
4. **Agent 自建结构**：不需要人手动设计目录，直接把 Karpathy 方法论文档丢给 agent，它会自己生成知识库结构和 AGENT.md

## 关键事实 / 数据

- 教程在 Windows 系统下完成
- obsidian-agent-client 的 GitHub URL：`https://github.com/RAIT-09/obsidian-agent-client.git`
- 插件在 Obsidian 左侧侧边栏显示为 🤖 小机器人图标
- Qwen Code 安装时会自动带上 [[Node.js]]，无需单独装
- B 站有配套视频教程 BV1p4DeB8ECi，提供了 skill 和 AGENT.md 模板

## 原文金句

> 个人推荐用 BRAT 插件安装，比较省事，下载文件安装可能存在一些问题（例如连不上 qwen）。

> 把 Karpathy 方法论原文文档贴出来供小伙伴直接使用，直接复制到 Obsidian 中，告诉 agent 根据此文档建立文件结构。

## 抽取的实体

- [[菠萝吹雪]]
- [[Qwen Code]]
- [[Obsidian]]
- [[obsidian-agent-client]]
- [[BRAT]]
- [[Andrej Karpathy]]
- [[Node.js]]

## 抽取的概念

- [[LLM Wiki]]
- [[AGENT.md 协议]]

## 与已有知识的关系

- **实操对位**：本文是 [[20260407-知乎-Karpathy开源Agent知识库]] 的实操配套——前者讲理念，本文讲怎么落地
- **差异 / 取舍**：
  - 工具栈差异：原 Gist 用 Claude Code，本教程用 Qwen Code（国内可达性优先）
  - 入口差异：原 Gist 通过 CLI 调 Agent，本教程把 Agent 嵌进 Obsidian 侧边栏
  - 平台差异：本教程在 Windows，原 Gist 平台无关
- **本知识库的方案选择**：先生最终选了"方案 A"——不装任何插件，由 [[Hana]]（Claude）直接扮演 agent。即本文方案的更轻量版

## 我的批注 / 思考

- **教程信息密度偏低**：作者强调"参考 B 站 up 主提供的教程"，关键的 skill 和 AGENT.md 模板没在本文给出
- **值得追问**：B 站 up 主那份 AGENT.md 长什么样？和我刚写的版本有何差异，可以互相借鉴
- **风险点**：obsidian-agent-client 是第三方插件（RAIT-09 仓库），需关注维护活跃度
- **关键空白**：教程没提"录入第一份资料后效果如何"——只到了"搭好环境"，没到"跑起来"

## 待深入

- [ ] 找到 B 站 BV1p4DeB8ECi 视频，看 up 主版本的 AGENT.md
- [ ] 调研 obsidian-agent-client 当前活跃度和已知问题
- [ ] 如果先生未来想从"方案 A"升级到"方案 B"，本文是直接的操作清单
