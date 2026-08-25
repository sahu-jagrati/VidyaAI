from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database.connection import Base


class Question(Base):
    __tablename__ = "questions"

    id              = Column(Integer, primary_key=True, index=True)
    exam            = Column(String(50),  nullable=True,  index=True)
    subject         = Column(String(50),  nullable=False, index=True)
    topic           = Column(String(100), nullable=True,  index=True)
    question_number = Column(Integer,     nullable=True)

    question_en     = Column(Text, nullable=False)
    question_hi     = Column(Text, nullable=True)

    option_a        = Column(Text, nullable=False)
    option_b        = Column(Text, nullable=False)
    option_c        = Column(Text, nullable=False)
    option_d        = Column(Text, nullable=False)

    image_url       = Column(Text,         nullable=True)   # diagram / figure image

    correct_answer  = Column(String(1),   nullable=True)   # NULL until solved
    difficulty      = Column(String(10),  nullable=True)   # NULL until graded
    source_pdf      = Column(String(500), nullable=True)

    created_at      = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    attempts = relationship("Attempt", back_populates="question")
