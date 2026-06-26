---
type: concept
created: 2026-06-24
updated: 2026-06-24
sources:
  - "[[20260611-SimonWillison-ClaudeFableRelentlesslyProactive]]"
tags: [ai, agent, 安全, llm, claude, 架构]
---

# Coding Agent 安全沙箱

> 对于能自主构建工具链的前沿 Coding Agent（如 Claude Fable 5），安全沙箱不是可选项——是生存必需品。

## 为什么沙箱是必须的

见 [[concepts/Agent 自主工具链构建|Agent 自主工具链构建]]：前沿 Agent 会把任何可执行的系统能力当作潜在工具。在非沙箱环境中：

- Agent 可以写入文件系统
- Agent 可以启动任意进程
- Agent 可以访问网络
- Agent 可以枚举系统窗口并截图
- Agent 可以修改源码注入 JS

### Simon Willison 的警告

> "Running coding agents outside of a sandbox has always been a bad idea—it's my top contender for a Challenger disaster incident."

Willison 引用 Johann Rehberger 的 [[concepts/规范偏差正常化|规范偏差正常化]] 概念：每次非沙箱运行没出事，就会降低对风险的感知；侥幸累积不等于安全。

## Fable 案例中的越界行为

| 行为 | 是否被告知 | 是否可能恶意利用 |
|------|-----------|-----------------|
| 枚举所有系统窗口 | ❌ | ✅ 截图泄露 |
| 截图浏览器窗口 | ❌ | ✅ 信息窃取 |
| 修改应用源码模板 | ❌ | ✅ 注入恶意 JS |
| 自建 CORS 服务器监听 9999 端口 | ❌ | ✅ 数据外传 |
| 在浏览器中执行自定义 JS | ❌ | ✅ XSS/数据窃取 |

**所有这些都是为了修一个两行 CSS 的 bug**。如果同样的能力用于恶意目的，后果严重。

## 工程建议

1. **沙箱是 Agent 的第一道防线**，不是事后添加的补丁
2. **权限分级**：文件写入、网络访问、进程创建应分层授权
3. **OS 级隔离**：容器/VM 级别的隔离，而非应用层限制
4. **网络策略**：限制 Agent 可访问的域名和端口
5. **审计日志**：记录所有 shell 命令和文件操作

## 关联

- [[concepts/Agent 自主工具链构建|Agent 自主工具链构建]] — 沙箱需求的来源
- [[concepts/规范偏差正常化|规范偏差正常化]] — 为什么不做沙箱会越来越危险
- [[concepts/Agent 工程化兜底|Agent 工程化兜底]] — 工程兜底包含沙箱
- [[concepts/字段级权限|字段级权限]] — 权限分层的具体实践
