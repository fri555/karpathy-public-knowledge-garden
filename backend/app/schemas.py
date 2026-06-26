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


class PublicPageSummary(BaseModel):
    title: str
    kind: str
    path: str
    tags: list[str] = []
    links: list[str] = []


class PublicPageDetail(PublicPageSummary):
    body: str


class PagesResponse(BaseModel):
    pages: list[PublicPageSummary]
