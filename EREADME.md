# 公开知识花园复习卡片项目说明

## 项目定位

本项目是 Karpathy 式知识库的公网学习入口，用前后端分离架构把本地 Markdown 知识库发布为公开知识花园，并提供复习卡片模式。

第一版重点：

- 浏览公开 wiki 页面。
- 从 wiki 页面进入复习卡片。
- 首页进入今日复习包。
- 每日 ingest 后刷新卡片数据。
- 公开来源元数据和原链接，不公开第三方 `raw/` 全文快照。

## 目录结构

```text
.
├── backend/    # 后端服务，FastAPI
├── frontend/   # 前端应用，Vue 3 + TypeScript
├── docs/       # 开发文档、需求文档、设计文档
├── raw/        # 原始资料私有证据层
├── wiki/       # Markdown 知识库源头
└── EREADME.md  # 项目工程说明
```

## 技术栈

### 后端

- Python
- FastAPI

### 前端

- Vue 3
- TypeScript
- Tailwind CSS
- Lucide icon
- shadcn/ui 标准组件与样式
- inspira-ui 动效组件，按需使用

## UX 原则

产品交互严格遵循尼尔森十大交互原则：

1. 系统状态可见。
2. 系统与现实世界匹配。
3. 用户控制与自由。
4. 一致性和标准。
5. 防错。
6. 识别优于回忆。
7. 灵活高效。
8. 美学与极简设计。
9. 帮助用户识别、诊断并恢复错误。
10. 帮助与文档。

## 开发约束

- 后续开发基于 `backend/`、`frontend/`、`docs/` 三个工程目录展开。
- 本地 Markdown wiki 仍然是知识源头。
- `raw/` 默认不作为公网全文内容发布。
- 第一版不做登录、数据库、个人进度和真正的间隔重复。

## 本地开发命令

### 后端

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

后端接口：

- `GET /api/health`
- `GET /api/cards/today`

### 前端

```bash
cd frontend
npm install
npm run dev
```

Vite 开发服务会把 `/api` 代理到 `http://127.0.0.1:8000`。

### 生成静态卡片 JSON

```bash
PYTHONPATH=backend python3 -m app.export_cards
```

当前导出位置：

- `frontend/public/cards/today.json`
- `frontend/public/pages/index.json`

## GitHub Pages 公网部署

第一版公网访问使用 GitHub Pages 静态部署，不依赖 FastAPI 后端在线运行。

部署文件：

- `.github/workflows/deploy-pages.yml`
- `docs/deployment/github-pages.md`

部署流程：

1. GitHub Actions 生成静态知识数据。
2. 构建 `frontend/`。
3. 发布 `frontend/dist` 到 GitHub Pages。

如果本项目仍放在更大的私人笔记仓库子目录中，建议先把本目录作为独立 GitHub 仓库发布，避免把整个笔记仓库公开。

本地推送前检查：

```bash
bash scripts/predeploy-check.sh
```
