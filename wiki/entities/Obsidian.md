---
type: entity
created: 2026-05-24
updated: 2026-06-01
sources:
  - "[[20260407-知乎-Karpathy开源Agent知识库]]"
  - "[[20260413-知乎-Qwen Code+Obsidian搭建Karpathy知识库]]"
tags: [工具, 知识管理, 软件]
aliases: [obsidian]
---

# Obsidian

> 一句话定义：基于本地 Markdown 文件的笔记软件，以双向链接和图谱视图见长，是 [[LLM Wiki]] 方法论的默认载体。

## 基本信息

- **类型**：软件 / 工具
- **领域**：个人知识管理
- **官网**：https://obsidian.md/
- **数据模型**：本地 Markdown 文件 + 文件夹
- **关联实体**：[[obsidian-agent-client]] · [[BRAT]]
- **关联概念**：[[LLM Wiki]] · [[三层架构]]

## 关键事实

- 所有数据是本地 Markdown 文件，本质上就是一个文件夹 (来源: [[20260407-知乎-Karpathy开源Agent知识库]])
- 整个 vault 可视作 Git 仓库，天然支持版本历史、分支、协作
- 图谱视图（Graph View）是看 Wiki 整体形态的最佳方式：什么连着什么、哪些是枢纽、哪些是孤岛一目了然
- 插件生态丰富，支持 Dataview（元数据查询）、Templates（模板）等
- 是 Karpathy 推荐的 LLM Wiki 默认前端

## Karpathy 工作流中的位置

在 [[三层架构]] 中，Obsidian 是人类"读"的窗口：
- LLM 在后台编辑 Markdown 文件
- 人在 Obsidian 里跟着 `[[双向链]]` 浏览、看图谱、读更新

## 在本知识库中的角色

先生的工作 vault 路径：`/Users/richelleshi/Documents/💼/【N】笔记`
本知识库位于其下的 `【K】Karpathy知识库/` 子目录，与其他工作笔记（【A】~【M】）严格隔离。

## 多端同步

Obsidian 本地优先的特性带来两个工程问题：数据安全和多端同步。七种主流方案（按推荐度）(来源: [[20260601-知乎-阿浩的笔记-Obsidian七种同步方案对比]])：

| 方案 | 适用场景 |
|---|---|
| 坚果云插件 | 国内轻度用户，免费 5G |
| Syncthing（P2P） | 技术用户全平台，iOS 需 Mobius Sync |
| Git + 坚果云双库 | 重度写作者：主库 Git 版本控制 + 移动端坚果云轻量同步 |
| 官方 Sync | 不差钱用户，$8/月 |
| Remotely Save | 小白用户，支持 S3/WebDAV |
| iCloud / OneDrive | 苹果/Win 全家桶用户 |
| Self-hosted LiveSync | 有服务器/NAS 用户 |

> 核心方法论：**分库策略**——主库（版本控制，深度写作）+ 移动库（轻量同步，灵感记录）分离。

## 相关资料

- [[20260407-知乎-Karpathy开源Agent知识库]]
- [[20260413-知乎-Qwen Code+Obsidian搭建Karpathy知识库]]

## 待深入

- [ ] Dataview 插件能否用于本知识库的健康度自动统计
- [ ] Graph View 在本知识库 50+ 页时的视觉效果
