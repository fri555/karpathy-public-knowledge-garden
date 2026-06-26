---
type: concept
created: 2026-06-24
updated: 2026-06-24
sources:
  - "[[20260611-SimonWillison-ClaudeFableRelentlesslyProactive]]"
tags: [ai, agent, llm, 安全, 方法论, claude]
---

# Agent 自主工具链构建

> Agent 不仅调用预定义工具，还能在现场**发明新的工具组合**来完成目标——包括编写测试页面、枚举系统窗口、自建 CORS 服务器、注入 JS 到 Web Component 等。

## 案例：Claude Fable 5 的 CSS Bug 调试

> 来源：[[20260611-SimonWillison-ClaudeFableRelentlesslyProactive]]

Simon Willison 给 Claude Fable 5 一张截图 + 一句话指令，要求找出水平滚动条的原因。Fable **未被指示**使用浏览器自动化，但它自主建构了以下工具链：

### 自建工具链清单

| 步骤 | 工具 | 性质 |
|------|------|------|
| 1. 启动 dev server | 已有能力 | 常规 |
| 2. Playwright 多浏览器测试 | 已有工具 | 常规 |
| 3. 启用 Chrome 滚动条 | `defaults write` | 自主发现 |
| 4. 枚举窗口获取 ID | pyobjc-framework-Quartz Python 脚本 | **现场发明** |
| 5. 截图 | `screencapture -l <id>` | 自主组合 |
| 6. 编写 HTML 测试页 | 生成代码 | 自主创建 |
| 7. 注入 JS 到模板触发快捷键 | 修改源码 | **跨越边界** |
| 8. 自建 CORS 服务器 | Python http.server 20 行 | **现场发明** |
| 9. 穿透 Shadow DOM | JS 代码 | 自主探索 |
| 10. 获取测量数据并回传 | 自建服务器 + fetch | **完整管线** |

## 含义

1. **"预定义工具"假设已过时**：前沿 Agent 会把任何可执行的系统能力当作潜在工具
2. **工具边界是幻觉**：Agent 运行在完整 OS 环境中，`bash` 就是万能工具
3. **审计不可能穷举**：无法预测 Agent 会发明什么新工具组合
4. **安全沙箱是唯一防线**：见 [[concepts/Coding Agent 安全沙箱|Coding Agent 安全沙箱]]

## 对比

- **传统 Agent**：调用预注册的 tool schema → 工具能力 = schema 总和
- **前沿 Agent**：bash/shell 是元工具 → 工具能力 = OS 能力总和

## 关联

- [[concepts/Coding Agent 安全沙箱|Coding Agent 安全沙箱]] — 自主工具链的必然推论
- [[concepts/工具调用|工具调用]] — 从预定义到自发明
- [[concepts/Agent 工程化兜底|Agent 工程化兜底]] — 如何兜住自主工具的边界
- [[entities/Claude Fable 5|Claude Fable 5]] — 案例模型
