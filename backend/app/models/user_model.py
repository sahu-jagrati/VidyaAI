from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database.connection import Base


class User(Base):
    __tablename__ = "users"

    id               = Column(Integer, primary_key=True, index=True)
    name             = Column(String(100), nullable=False)
    email            = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password  = Column(String(255), nullable=False)

    # Gamification
    xp               = Column(Integer, default=0)
    current_streak   = Column(Integer, default=0)
    highest_streak   = Column(Integer, default=0)
    total_questions  = Column(Integer, default=0)
    correct_answers  = Column(Integer, default=0)

    # Timestamps
    created_at       = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    last_activity    = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    attempts = relationship("Attempt", back_populates="user")

    @property
    def accuracy(self) -> float:
        if self.total_questions == 0:
            return 0.0
        return round((self.correct_answers / self.total_questions) * 100, 1)
