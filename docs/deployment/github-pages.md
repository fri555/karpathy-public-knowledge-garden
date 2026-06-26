# GitHub Pages 部署说明

## 部署方式

第一版公网访问使用 GitHub Pages 静态部署：

1. GitHub Actions checkout 仓库。
2. 运行 `PYTHONPATH=backend python -m app.export_cards`。
3. 从本地 `wiki/` 生成：
   - `frontend/public/cards/today.json`
   - `frontend/public/pages/index.json`
4. 进入 `frontend/` 安装依赖并构建。
5. 发布 `frontend/dist` 到 GitHub Pages。

## 关键边界

- GitHub Pages 只托管静态前端和静态 JSON。
- FastAPI 后端不运行在 GitHub Pages 上。
- 前端会优先请求 `/api`；如果 API 不可用，会自动回退到静态 JSON。
- `raw/` 全文不会作为公网内容发布。

## 使用步骤

如果本目录作为独立 GitHub 仓库根目录：

1. 运行预部署检查：

   ```bash
   bash scripts/predeploy-check.sh
   ```

2. 将项目推送到 GitHub。
3. 在 GitHub 仓库 Settings -> Pages 中选择 GitHub Actions。
4. 推送到 `main` 后，`.github/workflows/deploy-pages.yml` 会自动部署。

如果使用 GitHub CLI 创建公开仓库，可在本目录执行：

```bash
git init
git add .
git commit -m "Initial public knowledge garden"
gh repo create <repo-name> --public --source=. --remote=origin --push
```

创建后，在 GitHub 仓库 Settings -> Pages 中确认 Source 为 GitHub Actions。

如果当前项目仍作为更大笔记仓库的子目录：

1. GitHub Actions 文件必须位于实际仓库根目录的 `.github/workflows/`。
2. 需要把 workflow 中的路径改成子目录路径。
3. 更推荐把本项目单独作为一个 GitHub 仓库发布，避免公开整个私人笔记仓库。

## 本地静态数据生成

```bash
PYTHONPATH=backend python3 -m app.export_cards
```

## 本地前端构建

```bash
cd frontend
npm install
npm run build
```

## 注意

当前本地目录位于更大的“笔记”git 仓库之下，且当前没有配置 GitHub remote。为了避免公开整个私人笔记仓库，推荐把 `【K】Karpathy知识库` 作为独立 GitHub 仓库发布。
