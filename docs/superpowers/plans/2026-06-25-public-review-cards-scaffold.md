# Public Review Cards Scaffold Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first runnable frontend/backend scaffold for the public knowledge garden review-card app.

**Architecture:** Use a frontend/backend split. `backend/` exposes a FastAPI API with health and demo review-card endpoints. `frontend/` is a Vue 3 + TypeScript + Tailwind-style app that consumes the API shape through local typed fixtures for the first scaffold.

**Tech Stack:** Python, FastAPI, pytest, Vue 3, TypeScript, Tailwind CSS conventions, Lucide icon dependency, shadcn/ui style tokens.

---

## File Structure

- Rename: `backed/` -> `backend/`
- Rename: `fronted/` -> `frontend/`
- Modify: `EREADME.md`
- Modify: `docs/requirements/2026-06-25-公开知识花园复习卡片需求文档.md`
- Create: `backend/README.md`
- Create: `backend/requirements.txt`
- Create: `backend/app/__init__.py`
- Create: `backend/app/main.py`
- Create: `backend/app/schemas.py`
- Create: `backend/tests/test_main.py`
- Create: `frontend/README.md`
- Create: `frontend/package.json`
- Create: `frontend/index.html`
- Create: `frontend/src/main.ts`
- Create: `frontend/src/App.vue`
- Create: `frontend/src/types.ts`
- Create: `frontend/src/data/demoCards.ts`
- Create: `frontend/src/style.css`
- Create: `frontend/tsconfig.json`
- Create: `frontend/vite.config.ts`

## Task 1: Standardize Project Directory Names

**Files:**
- Rename: `backed/` -> `backend/`
- Rename: `fronted/` -> `frontend/`
- Modify: `EREADME.md`
- Modify: `docs/requirements/2026-06-25-公开知识花园复习卡片需求文档.md`

- [ ] **Step 1: Rename directories**

Run:

```bash
mv backed backend
mv fronted frontend
```

Expected: `backend/.gitkeep` and `frontend/.gitkeep` exist.

- [ ] **Step 2: Update documentation names**

Replace all `backed` references with `backend`, and all `fronted` references with `frontend` in:

```text
EREADME.md
docs/requirements/2026-06-25-公开知识花园复习卡片需求文档.md
```

- [ ] **Step 3: Verify names**

Run:

```bash
find backend frontend -maxdepth 1 -type f -print | sort
rg -n "backed|fronted" EREADME.md docs/requirements/2026-06-25-公开知识花园复习卡片需求文档.md
```

Expected: `find` shows `.gitkeep` files; `rg` returns no matches.

## Task 2: Scaffold FastAPI Backend

**Files:**
- Create: `backend/README.md`
- Create: `backend/requirements.txt`
- Create: `backend/app/__init__.py`
- Create: `backend/app/main.py`
- Create: `backend/app/schemas.py`
- Create: `backend/tests/test_main.py`

- [ ] **Step 1: Create backend dependencies**

Create `backend/requirements.txt`:

```text
fastapi>=0.115.0
uvicorn[standard]>=0.30.0
pydantic>=2.7.0
pytest>=8.2.0
httpx>=0.27.0
```

- [ ] **Step 2: Create response schemas**

Create `backend/app/schemas.py`:

```python
from typing import Literal

from pydantic import BaseModel


CardType = Literal["definition", "counterintuitive", "comparison", "application", "connection"]
Difficulty = Literal["easy", "medium", "hard"]


class ReviewCard(BaseModel):
    id: str
    type: CardType
    question: str
    answer: str
    explanation: str
    source_page: str
    source_url: str | None = None
    concepts: list[str] = []
    difficulty: Difficulty = "medium"
    created: str


class HealthResponse(BaseModel):
    status: str
    service: str


class CardsResponse(BaseModel):
    cards: list[ReviewCard]
```

- [ ] **Step 3: Create FastAPI app**

Create `backend/app/main.py`:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import CardsResponse, HealthResponse, ReviewCard

app = FastAPI(
    title="公开知识花园复习卡片 API",
    description="Karpathy 式知识库的复习卡片后端服务",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


DEMO_CARDS = [
    ReviewCard(
        id="concept-llm-wiki-definition-001",
        type="definition",
        question="什么是 LLM Wiki？",
        answer="LLM Wiki 是由 Agent 持续维护和编译的知识网络。",
        explanation="重点不是存文档，而是让每份资料和每次提问都沉淀为可链接、可复用、可继续生长的知识。",
        source_page="wiki/concepts/LLM Wiki.md",
        source_url=None,
        concepts=["LLM Wiki", "知识复利", "Ingest 录入"],
        difficulty="medium",
        created="2026-06-25",
    )
]


@app.get("/api/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="public-review-cards")


@app.get("/api/cards/today", response_model=CardsResponse)
def today_cards() -> CardsResponse:
    return CardsResponse(cards=DEMO_CARDS)
```

- [ ] **Step 4: Create package marker**

Create `backend/app/__init__.py`:

```python
"""FastAPI backend for the public knowledge garden review-card app."""
```

- [ ] **Step 5: Create backend tests**

Create `backend/tests/test_main.py`:

```python
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "public-review-cards",
    }


def test_today_cards_endpoint() -> None:
    response = client.get("/api/cards/today")

    assert response.status_code == 200
    body = response.json()
    assert len(body["cards"]) == 1
    assert body["cards"][0]["question"] == "什么是 LLM Wiki？"
```

- [ ] **Step 6: Create backend README**

Create `backend/README.md`:

```markdown
# Backend

FastAPI backend for the public knowledge garden review-card app.

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Test

```bash
PYTHONPATH=. pytest
```
```

- [ ] **Step 7: Verify backend syntax**

Run:

```bash
python3 -m compileall backend/app backend/tests
```

Expected: compile succeeds.

## Task 3: Scaffold Vue 3 Frontend

**Files:**
- Create: `frontend/README.md`
- Create: `frontend/package.json`
- Create: `frontend/index.html`
- Create: `frontend/src/main.ts`
- Create: `frontend/src/App.vue`
- Create: `frontend/src/types.ts`
- Create: `frontend/src/data/demoCards.ts`
- Create: `frontend/src/style.css`
- Create: `frontend/tsconfig.json`
- Create: `frontend/vite.config.ts`

- [ ] **Step 1: Create package metadata**

Create `frontend/package.json`:

```json
{
  "name": "public-review-cards-frontend",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vue-tsc -b && vite build",
    "preview": "vite preview",
    "typecheck": "vue-tsc -b"
  },
  "dependencies": {
    "@vitejs/plugin-vue": "^5.2.0",
    "lucide-vue-next": "^0.468.0",
    "vite": "^5.4.0",
    "vue": "^3.5.0"
  },
  "devDependencies": {
    "typescript": "^5.6.0",
    "vue-tsc": "^2.1.0"
  }
}
```

- [ ] **Step 2: Create TypeScript config**

Create `frontend/tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "module": "ESNext",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "skipLibCheck": true,
    "moduleResolution": "Bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "strict": true,
    "jsx": "preserve",
    "types": []
  },
  "include": ["src/**/*.ts", "src/**/*.vue"]
}
```

- [ ] **Step 3: Create Vite config**

Create `frontend/vite.config.ts`:

```ts
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5173,
  },
});
```

- [ ] **Step 4: Create app entry**

Create `frontend/index.html`:

```html
<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>公开知识花园复习卡片</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.ts"></script>
  </body>
</html>
```

Create `frontend/src/main.ts`:

```ts
import { createApp } from "vue";
import App from "./App.vue";
import "./style.css";

createApp(App).mount("#app");
```

- [ ] **Step 5: Create frontend types and demo data**

Create `frontend/src/types.ts`:

```ts
export type CardType = "definition" | "counterintuitive" | "comparison" | "application" | "connection";

export interface ReviewCard {
  id: string;
  type: CardType;
  question: string;
  answer: string;
  explanation: string;
  sourcePage: string;
  sourceUrl?: string;
  concepts: string[];
  difficulty: "easy" | "medium" | "hard";
  created: string;
}
```

Create `frontend/src/data/demoCards.ts`:

```ts
import type { ReviewCard } from "../types";

export const demoCards: ReviewCard[] = [
  {
    id: "concept-llm-wiki-definition-001",
    type: "definition",
    question: "什么是 LLM Wiki？",
    answer: "LLM Wiki 是由 Agent 持续维护和编译的知识网络。",
    explanation: "重点不是存文档，而是让每份资料和每次提问都沉淀为可链接、可复用、可继续生长的知识。",
    sourcePage: "wiki/concepts/LLM Wiki.md",
    concepts: ["LLM Wiki", "知识复利", "Ingest 录入"],
    difficulty: "medium",
    created: "2026-06-25",
  },
];
```

- [ ] **Step 6: Create first mobile-first UI**

Create `frontend/src/App.vue`:

```vue
<script setup lang="ts">
import { computed, ref } from "vue";
import { BookOpen, Brain, ChevronRight, Link, Sparkles } from "lucide-vue-next";
import { demoCards } from "./data/demoCards";

const currentIndex = ref(0);
const isAnswerVisible = ref(false);

const currentCard = computed(() => demoCards[currentIndex.value]);

function revealAnswer() {
  isAnswerVisible.value = true;
}

function nextCard() {
  currentIndex.value = (currentIndex.value + 1) % demoCards.length;
  isAnswerVisible.value = false;
}
</script>

<template>
  <main class="min-h-screen bg-stone-50 text-zinc-950">
    <section class="mx-auto flex min-h-screen w-full max-w-5xl flex-col px-5 py-6 sm:px-8 lg:px-10">
      <header class="flex items-center justify-between gap-4">
        <div class="flex items-center gap-3">
          <div class="flex h-10 w-10 items-center justify-center rounded-xl border border-zinc-200 bg-white shadow-sm">
            <Brain class="h-5 w-5 text-emerald-700" />
          </div>
          <div>
            <p class="text-xs font-medium uppercase tracking-wide text-zinc-500">Personal Cognitive OS</p>
            <h1 class="text-lg font-semibold text-zinc-950">公开知识花园</h1>
          </div>
        </div>
        <button class="inline-flex h-10 items-center gap-2 rounded-lg border border-zinc-200 bg-white px-3 text-sm font-medium text-zinc-800 shadow-sm">
          <BookOpen class="h-4 w-4" />
          知识库
        </button>
      </header>

      <div class="grid flex-1 gap-5 py-8 lg:grid-cols-[0.9fr_1.1fr] lg:items-center">
        <section>
          <div class="mb-4 inline-flex items-center gap-2 rounded-full border border-emerald-200 bg-emerald-50 px-3 py-1 text-sm text-emerald-800">
            <Sparkles class="h-4 w-4" />
            今日复习包
          </div>
          <h2 class="max-w-xl text-4xl font-semibold leading-tight text-zinc-950 sm:text-5xl">
            把死知识变成每天能想起来的问题。
          </h2>
          <p class="mt-4 max-w-lg text-base leading-7 text-zinc-600">
            从 Markdown 知识库生成复习卡片。先回忆，再展开答案，再回到来源页面继续深读。
          </p>
          <div class="mt-6 grid gap-3 sm:grid-cols-3">
            <div class="rounded-xl border border-zinc-200 bg-white p-4 shadow-sm">
              <p class="text-2xl font-semibold">5</p>
              <p class="mt-1 text-sm text-zinc-500">卡片类型</p>
            </div>
            <div class="rounded-xl border border-zinc-200 bg-white p-4 shadow-sm">
              <p class="text-2xl font-semibold">0</p>
              <p class="mt-1 text-sm text-zinc-500">登录要求</p>
            </div>
            <div class="rounded-xl border border-zinc-200 bg-white p-4 shadow-sm">
              <p class="text-2xl font-semibold">∞</p>
              <p class="mt-1 text-sm text-zinc-500">开放主题</p>
            </div>
          </div>
        </section>

        <section class="rounded-2xl border border-zinc-200 bg-white p-5 shadow-sm">
          <div class="mb-4 flex items-center justify-between gap-4">
            <div>
              <p class="text-sm font-medium text-zinc-500">定义卡</p>
              <h3 class="mt-1 text-xl font-semibold text-zinc-950">{{ currentCard.question }}</h3>
            </div>
            <span class="rounded-full bg-zinc-100 px-3 py-1 text-xs font-medium text-zinc-600">
              {{ currentIndex + 1 }} / {{ demoCards.length }}
            </span>
          </div>

          <button
            v-if="!isAnswerVisible"
            class="flex min-h-44 w-full items-center justify-center rounded-xl border border-dashed border-zinc-300 bg-zinc-50 p-6 text-center text-sm font-medium text-zinc-600 transition hover:border-emerald-300 hover:bg-emerald-50 hover:text-emerald-800"
            type="button"
            @click="revealAnswer"
          >
            点击展开答案
          </button>

          <div v-else class="rounded-xl border border-emerald-200 bg-emerald-50 p-5">
            <p class="text-base font-semibold text-emerald-950">{{ currentCard.answer }}</p>
            <p class="mt-3 text-sm leading-6 text-emerald-900">{{ currentCard.explanation }}</p>
          </div>

          <div class="mt-5 flex flex-wrap gap-2">
            <span
              v-for="concept in currentCard.concepts"
              :key="concept"
              class="rounded-full bg-zinc-100 px-3 py-1 text-xs font-medium text-zinc-600"
            >
              {{ concept }}
            </span>
          </div>

          <div class="mt-6 flex items-center justify-between gap-3 border-t border-zinc-100 pt-4">
            <a class="inline-flex items-center gap-2 text-sm font-medium text-zinc-600" href="#">
              <Link class="h-4 w-4" />
              {{ currentCard.sourcePage }}
            </a>
            <button
              class="inline-flex h-10 items-center gap-2 rounded-lg bg-zinc-950 px-4 text-sm font-medium text-white"
              type="button"
              @click="nextCard"
            >
              下一张
              <ChevronRight class="h-4 w-4" />
            </button>
          </div>
        </section>
      </div>
    </section>
  </main>
</template>
```

- [ ] **Step 7: Create CSS**

Create `frontend/src/style.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  font-family:
    Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: #09090b;
  background: #fafaf9;
}

body {
  margin: 0;
}

button,
a {
  -webkit-tap-highlight-color: transparent;
}
```

- [ ] **Step 8: Create frontend README**

Create `frontend/README.md`:

```markdown
# Frontend

Vue 3 + TypeScript frontend for the public knowledge garden review-card app.

## Run

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```
```

- [ ] **Step 9: Verify scaffold files**

Run:

```bash
find frontend/src -maxdepth 3 -type f -print | sort
```

Expected: `App.vue`, `main.ts`, `style.css`, `types.ts`, and `data/demoCards.ts` exist.

## Task 4: Final Lightweight Verification

**Files:**
- Inspect: `backend/`
- Inspect: `frontend/`
- Inspect: `EREADME.md`
- Inspect: `docs/requirements/2026-06-25-公开知识花园复习卡片需求文档.md`

- [ ] **Step 1: Verify docs use standard directory names**

Run:

```bash
rg -n "backed|fronted" EREADME.md docs/requirements/2026-06-25-公开知识花园复习卡片需求文档.md
```

Expected: no matches.

- [ ] **Step 2: Verify backend Python syntax**

Run:

```bash
python3 -m compileall backend/app backend/tests
```

Expected: compile succeeds.

- [ ] **Step 3: Verify top-level structure**

Run:

```bash
find backend frontend docs -maxdepth 2 -type f -print | sort
```

Expected: backend, frontend, and docs files are listed.

- [ ] **Step 4: Report dependency limitation**

Because network access may be restricted, do not run `pip install` or `npm install` unless explicitly approved. Report that full backend tests and frontend builds require installing dependencies.
