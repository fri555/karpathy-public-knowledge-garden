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
