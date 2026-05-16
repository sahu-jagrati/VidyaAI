"""
Daily question selection:
  - 5 questions per day
  - Mix: 2 easy, 2 medium, 1 hard
  - At least 1 question from each subject where possible
  - Excludes questions the user already attempted today
"""

from sqlalchemy.orm import Session
from sqlalchemy import func, and_
from datetime import datetime, timezone, timedelta
from typing import List

from app.models.question_model import Question
from app.models.attempt_model   import Attempt


IST = timezone(timedelta(hours=5, minutes=30))

DIFFICULTY_MIX = {"easy": 2, "medium": 2, "hard": 1}


def get_daily_questions(user_id: int, db: Session) -> List[Question]:
    # Find questions already attempted by this user today (IST)
    today_start_utc = datetime.now(IST).replace(hour=0, minute=0, second=0, microsecond=0).astimezone(timezone.utc)

    attempted_today = (
        db.query(Attempt.question_id)
        .filter(
            Attempt.user_id    == user_id,
            Attempt.attempted_at >= today_start_utc,
        )
        .subquery()
    )

    selected: List[Question] = []

    for difficulty, count in DIFFICULTY_MIX.items():
        questions = (
            db.query(Question)
            .filter(
                Question.difficulty == difficulty,
                Question.phase      == "main",
                ~Question.id.in_(attempted_today),
            )
            .order_by(func.random())
            .limit(count)
            .all()
        )
        selected.extend(questions)

    # Fallback: if we don't have 5 questions (e.g. user exhausted easy ones), fill with any
    if len(selected) < 5:
        existing_ids = [q.id for q in selected]
        fillers = (
            db.query(Question)
            .filter(
                Question.phase == "main",
                ~Question.id.in_(attempted_today),
                ~Question.id.in_(existing_ids),
            )
            .order_by(func.random())
            .limit(5 - len(selected))
            .all()
        )
        selected.extend(fillers)

    return selected
