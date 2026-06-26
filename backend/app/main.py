from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.content import GeneratedCard, PublicPage, collect_public_pages, get_today_cards, read_public_page
from app.schemas import CardsResponse, HealthResponse, PagesResponse, PublicPageDetail, PublicPageSummary, ReviewCard

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

PROJECT_ROOT = Path(__file__).resolve().parents[2]


@app.get("/api/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="public-review-cards")


@app.get("/api/cards/today", response_model=CardsResponse)
def today_cards() -> CardsResponse:
    return CardsResponse(cards=[_to_schema(card) for card in get_today_cards(PROJECT_ROOT)])


@app.get("/api/pages", response_model=PagesResponse)
def pages() -> PagesResponse:
    return PagesResponse(pages=[_to_page_summary(page) for page in collect_public_pages(PROJECT_ROOT)])


@app.get("/api/pages/content", response_model=PublicPageDetail)
def page_content(path: str) -> PublicPageDetail:
    return _to_page_detail(read_public_page(PROJECT_ROOT, path))


def _to_schema(card: GeneratedCard) -> ReviewCard:
    return ReviewCard(
        id=card.id,
        type=card.type,
        question=card.question,
        answer=card.answer,
        explanation=card.explanation,
        source_page=card.source_page,
        source_url=None,
        concepts=card.concepts,
        difficulty=card.difficulty,
        created=card.created,
    )


def _to_page_summary(page: PublicPage) -> PublicPageSummary:
    return PublicPageSummary(
        title=page.title,
        kind=page.kind,
        path=page.path,
        tags=page.tags,
        links=page.links,
    )


def _to_page_detail(page: PublicPage) -> PublicPageDetail:
    return PublicPageDetail(
        title=page.title,
        kind=page.kind,
        path=page.path,
        tags=page.tags,
        links=page.links,
        body=page.body,
    )
