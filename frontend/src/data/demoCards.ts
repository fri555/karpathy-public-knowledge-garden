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
