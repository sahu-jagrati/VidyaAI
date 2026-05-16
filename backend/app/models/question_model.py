from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database.connection import Base


class Question(Base):
    __tablename__ = "questions"

    id             = Column(Integer, primary_key=True, index=True)
    subject        = Column(String(50), nullable=False, index=True)   # e.g. "Quantitative Aptitude"
    subject_code   = Column(String(20), nullable=False, index=True)   # e.g. "quant"
    topic          = Column(String(100), nullable=True)               # e.g. "Percentage"
    difficulty     = Column(String(10), nullable=False, index=True)   # easy | medium | hard
    phase          = Column(String(10), nullable=False, default="main")  # main | advanced

    question_text  = Column(String(1000), nullable=False)
    option_a       = Column(String(300), nullable=False)
    option_b       = Column(String(300), nullable=False)
    option_c       = Column(String(300), nullable=False)
    option_d       = Column(String(300), nullable=False)
    correct_answer = Column(String(1), nullable=False)   # A | B | C | D
    explanation    = Column(String(1000), nullable=False)

    created_at     = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relationships
    attempts = relationship("Attempt", back_populates="question")
