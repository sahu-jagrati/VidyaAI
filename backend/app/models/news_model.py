from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime, timezone
from app.database.connection import Base


class NewsArticle(Base):
    __tablename__ = "news_articles"

    id           = Column(Integer, primary_key=True, index=True)
    title        = Column(String(500), nullable=False)
    title_hi     = Column(Text, nullable=True)
    summary      = Column(Text, nullable=True)
    summary_hi   = Column(Text, nullable=True)
    source       = Column(String(150), nullable=False, default="")
    url          = Column(String(1000), nullable=True, unique=True)
    category     = Column(String(60), default="General", index=True)
    lang         = Column(String(5), nullable=False, server_default="en", default="en")
    published_at = Column(DateTime(timezone=True), nullable=True, index=True)
    created_at   = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
