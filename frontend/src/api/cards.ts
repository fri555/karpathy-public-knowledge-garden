import type { ReviewCard } from "../types";

interface ApiReviewCard {
  id: string;
  type: ReviewCard["type"];
  question: string;
  answer: string;
  explanation: string;
  source_page: string;
  source_url?: string | null;
  concepts: string[];
  difficulty: ReviewCard["difficulty"];
  created: string;
}

interface CardsResponse {
  cards: ApiReviewCard[];
}

export async function fetchTodayCards(): Promise<ReviewCard[]> {
  const response = await fetchWithStaticFallback("/api/cards/today", `${import.meta.env.BASE_URL}cards/today.json`);

  if (!response.ok) {
    throw new Error(`获取今日复习包失败：${response.status}`);
  }

  const body = (await response.json()) as CardsResponse;
  return body.cards.map((card) => ({
    id: card.id,
    type: card.type,
    question: card.question,
    answer: card.answer,
    explanation: card.explanation,
    sourcePage: card.source_page,
    sourceUrl: card.source_url ?? undefined,
    concepts: card.concepts,
    difficulty: card.difficulty,
    created: card.created,
  }));
}

async function fetchWithStaticFallback(apiPath: string, staticPath: string): Promise<Response> {
  try {
    const apiResponse = await fetch(apiPath);

    if (apiResponse.ok) {
      return apiResponse;
    }
  } catch {
    // Static deployments do not have the FastAPI backend available.
  }

  return fetch(staticPath);
}
