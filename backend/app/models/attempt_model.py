from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database.connection import Base


class Attempt(Base):
    __tablename__ = "attempts"

    id              = Column(Integer, primary_key=True, index=True)
    user_id         = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    question_id     = Column(Integer, ForeignKey("questions.id"), nullable=False, index=True)

    selected_answer = Column(String(1), nullable=True)   # A|B|C|D or None if timed out
    is_correct      = Column(Boolean, nullable=False, default=False)
    xp_earned       = Column(Integer, nullable=False, default=0)
    time_taken      = Column(Integer, nullable=False, default=0)   # seconds

    attempted_at    = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), index=True)

    # Relationships
    user     = relationship("User",     back_populates="attempts")
    question = relationship("Question", back_populates="attempts")
