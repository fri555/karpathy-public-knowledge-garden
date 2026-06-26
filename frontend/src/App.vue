<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { BookOpen, Brain, ChevronRight, Link, Sparkles } from "lucide-vue-next";
import { fetchTodayCards } from "./api/cards";
import { fetchPublicPages, type PublicPageSummary } from "./api/pages";
import { demoCards } from "./data/demoCards";
import type { ReviewCard } from "./types";

const currentIndex = ref(0);
const isAnswerVisible = ref(false);
const cards = ref<ReviewCard[]>(demoCards);
const pages = ref<PublicPageSummary[]>([]);
const isLoading = ref(false);
const loadError = ref<string | null>(null);

const currentCard = computed(() => cards.value[currentIndex.value] ?? demoCards[0]);

onMounted(async () => {
  isLoading.value = true;
  try {
    const [remoteCards, remotePages] = await Promise.all([fetchTodayCards(), fetchPublicPages()]);
    cards.value = remoteCards.length > 0 ? remoteCards : demoCards;
    pages.value = remotePages.slice(0, 5);
    loadError.value = null;
  } catch (error) {
    loadError.value = error instanceof Error ? error.message : "后端暂不可用，已使用本地示例卡片。";
    cards.value = demoCards;
  } finally {
    isLoading.value = false;
  }
});

function revealAnswer() {
  isAnswerVisible.value = true;
}

function nextCard() {
  currentIndex.value = (currentIndex.value + 1) % cards.value.length;
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
          <div class="mt-6 rounded-xl border border-zinc-200 bg-white p-4 shadow-sm">
            <div class="mb-3 flex items-center justify-between gap-3">
              <p class="text-sm font-semibold text-zinc-900">最近知识页</p>
              <span class="text-xs text-zinc-500">{{ pages.length }} 个入口</span>
            </div>
            <div class="space-y-2">
              <a
                v-for="page in pages"
                :key="page.path"
                class="flex items-center justify-between gap-3 rounded-lg px-2 py-2 text-sm text-zinc-700 hover:bg-zinc-50"
                href="#"
              >
                <span class="truncate">{{ page.title }}</span>
                <span class="shrink-0 rounded-full bg-zinc-100 px-2 py-0.5 text-xs text-zinc-500">
                  {{ page.kind }}
                </span>
              </a>
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
              {{ currentIndex + 1 }} / {{ cards.length }}
            </span>
          </div>

          <div
            v-if="isLoading || loadError"
            class="mb-4 rounded-lg border border-zinc-200 bg-zinc-50 px-3 py-2 text-sm text-zinc-600"
          >
            {{ isLoading ? "正在加载今日复习包..." : loadError }}
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
