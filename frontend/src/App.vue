<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, reactive, ref } from "vue";
import {
  ArrowLeft,
  ArrowRight,
  Brain,
  Check,
  Eye,
  HelpCircle,
  RotateCcw,
  Shuffle,
  Sparkles,
  X,
} from "lucide-vue-next";
import { fetchTodayCards } from "./api/cards";
import { demoCards } from "./data/demoCards";
import type { ReviewCard } from "./types";

type Feedback = "known" | "unclear" | "unknown";

const currentIndex = ref(0);
const isAnswerVisible = ref(false);
const cards = ref<ReviewCard[]>(demoCards);
const isLoading = ref(false);
const loadError = ref<string | null>(null);
const feedbackByCard = reactive<Record<string, Feedback>>({});

const currentCard = computed(() => cards.value[currentIndex.value] ?? demoCards[0]);
const progressPercent = computed(() => ((currentIndex.value + 1) / cards.value.length) * 100);
const currentFeedback = computed(() => feedbackByCard[currentCard.value.id]);
const answeredCount = computed(() => Object.keys(feedbackByCard).length);

const cardTypeLabel = computed(() => {
  const labels: Record<string, string> = {
    definition: "定义",
    connection: "连接",
  };
  return labels[currentCard.value.type] ?? currentCard.value.type;
});

onMounted(async () => {
  window.addEventListener("keydown", handleKeydown);
  isLoading.value = true;
  try {
    const remoteCards = await fetchTodayCards();
    cards.value = remoteCards.length > 0 ? remoteCards : demoCards;
    loadError.value = null;
  } catch (error) {
    loadError.value = error instanceof Error ? error.message : "已使用本地示例卡片";
    cards.value = demoCards;
  } finally {
    isLoading.value = false;
  }
});

onBeforeUnmount(() => {
  window.removeEventListener("keydown", handleKeydown);
});

function revealAnswer() {
  isAnswerVisible.value = true;
}

function nextCard() {
  goToRandomCard();
}

function previousCard() {
  currentIndex.value = (currentIndex.value - 1 + cards.value.length) % cards.value.length;
  isAnswerVisible.value = false;
}

function goToRandomCard() {
  if (cards.value.length < 2) return;
  let nextIndex = Math.floor(Math.random() * cards.value.length);
  if (nextIndex === currentIndex.value) {
    nextIndex = (nextIndex + 1) % cards.value.length;
  }
  currentIndex.value = nextIndex;
  isAnswerVisible.value = false;
}

function shuffleCard() {
  goToRandomCard();
}

function mark(feedback: Feedback) {
  feedbackByCard[currentCard.value.id] = feedback;
  window.setTimeout(nextCard, 180);
}

function resetSession() {
  Object.keys(feedbackByCard).forEach((id) => delete feedbackByCard[id]);
  currentIndex.value = 0;
  isAnswerVisible.value = false;
}

function handleKeydown(event: KeyboardEvent) {
  if (event.key === "ArrowRight") nextCard();
  if (event.key === "ArrowLeft") previousCard();
  if (event.key === " ") {
    event.preventDefault();
    isAnswerVisible.value ? nextCard() : revealAnswer();
  }
}
</script>

<template>
  <main class="relative min-h-screen overflow-hidden bg-[#f5f7f4] text-zinc-950">
    <div class="ambient ambient-one"></div>
    <div class="ambient ambient-two"></div>
    <div class="ambient ambient-three"></div>

    <section class="relative mx-auto flex min-h-screen w-full max-w-3xl flex-col px-4 py-4 sm:px-6 sm:py-6">
      <header class="flex items-center justify-between gap-3">
        <div class="glass-pill min-w-0">
          <Sparkles class="h-4 w-4 shrink-0 text-emerald-700" />
          <span class="truncate">今日卡片</span>
        </div>
        <div class="glass-pill shrink-0">
          <Brain class="h-4 w-4 text-zinc-700" />
          <span>{{ currentIndex + 1 }} / {{ cards.length }}</span>
        </div>
      </header>

      <div class="mt-3 h-1 overflow-hidden rounded-full bg-white/45">
        <div class="h-full rounded-full bg-zinc-950 transition-all duration-300" :style="{ width: `${progressPercent}%` }"></div>
      </div>

      <div class="flex flex-1 items-center py-5 sm:py-8">
        <article class="card-shell w-full">
          <div class="flex items-center justify-between gap-3">
            <span class="glass-tag">{{ cardTypeLabel }}</span>
            <button class="icon-button" type="button" aria-label="随机一张" @click="shuffleCard">
              <Shuffle class="h-4 w-4" />
            </button>
          </div>

          <button class="question-area" type="button" @click="isAnswerVisible ? nextCard() : revealAnswer()">
            <span v-if="isLoading" class="status-copy">正在同步卡片</span>
            <span v-else-if="loadError" class="status-copy">{{ loadError }}</span>
            <span v-else>{{ currentCard.question }}</span>
          </button>

          <section v-if="isAnswerVisible" class="answer-surface">
            <p>{{ currentCard.answer }}</p>
            <p v-if="currentCard.explanation" class="answer-note">{{ currentCard.explanation }}</p>
          </section>

          <button v-else class="reveal-button" type="button" @click="revealAnswer">
            <Eye class="h-4 w-4" />
            看答案
          </button>

          <div class="concept-row">
            <span v-for="concept in currentCard.concepts.slice(0, 3)" :key="concept" class="concept-chip">
              {{ concept }}
            </span>
          </div>

          <div class="source-line">{{ currentCard.sourcePage }}</div>
        </article>
      </div>

      <footer class="glass-dock">
        <button class="dock-button" type="button" aria-label="上一张" @click="previousCard">
          <ArrowLeft class="h-5 w-5" />
        </button>
        <button
          class="feedback-button"
          :class="{ active: currentFeedback === 'unknown' }"
          type="button"
          @click="mark('unknown')"
        >
          <X class="h-4 w-4" />
          还不会
        </button>
        <button
          class="feedback-button"
          :class="{ active: currentFeedback === 'unclear' }"
          type="button"
          @click="mark('unclear')"
        >
          <HelpCircle class="h-4 w-4" />
          模糊
        </button>
        <button
          class="feedback-button primary"
          :class="{ active: currentFeedback === 'known' }"
          type="button"
          @click="mark('known')"
        >
          <Check class="h-4 w-4" />
          记住了
        </button>
        <button class="dock-button" type="button" aria-label="下一张" @click="nextCard">
          <ArrowRight class="h-5 w-5" />
        </button>
      </footer>

      <div class="session-line">
        <span>{{ answeredCount }} 已反馈</span>
        <button type="button" @click="resetSession">
          <RotateCcw class="h-3.5 w-3.5" />
          重来
        </button>
      </div>
    </section>
  </main>
</template>
