from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from app.database.connection import get_db
from app.models.news_model import NewsArticle

router = APIRouter(prefix="/news", tags=["News"])

MIN_PER_CATEGORY = 10


class NewsOut(BaseModel):
    id:           int
    title:        str
    summary:      Optional[str]
    source:       str
    url:          Optional[str]
    category:     str
    published_at: Optional[datetime]
    created_at:   datetime

    model_config = {"from_attributes": True}


def _apply_lang(articles: list[NewsArticle], lang: str) -> list[dict]:
    out = []
    for a in articles:
        d = {
            "id":           a.id,
            "title":        (a.title_hi or a.title) if lang == "hi" else a.title,
            "summary":      (a.summary_hi or a.summary) if lang == "hi" else a.summary,
            "source":       a.source,
            "url":          a.url,
            "category":     a.category,
            "published_at": a.published_at,
            "created_at":   a.created_at,
        }
        out.append(d)
    return out


@router.get("", response_model=list[NewsOut])
def get_news(
    category: Optional[str] = Query(None),
    lang:     str            = Query("en"),
    limit:    int            = Query(40, le=100),
    db:       Session        = Depends(get_db),
):
    base_q = db.query(NewsArticle).order_by(
        NewsArticle.published_at.desc().nullslast(),
        NewsArticle.created_at.desc(),
    )

    if not category or category.lower() == "all":
        articles = base_q.limit(limit).all()
    else:
        articles = (
            base_q
            .filter(NewsArticle.category == category)
            .limit(max(limit, MIN_PER_CATEGORY))
            .all()
        )

    return _apply_lang(articles, lang)
