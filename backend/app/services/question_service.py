"""
Daily question selection:
  - 5 questions per day
  - Prefers difficulty mix: 2 easy, 2 medium, 1 hard
  - Falls back to any unattempted question when difficulty buckets are empty
    (new questions have difficulty = NULL until graded)
  - Excludes questions the user already attempted today
"""

from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timezone, timedelta
from typing import List

from app.models.question_model import Question
from app.models.attempt_model  import Attempt


IST = timezone(timedelta(hours=5, minutes=30))
DIFFICULTY_MIX = {"easy": 2, "medium": 2, "hard": 1}


def get_daily_questions(user_id: int, db: Session) -> List[Question]:
    today_start_utc = (
        datetime.now(IST)
        .replace(hour=0, minute=0, second=0, microsecond=0)
        .astimezone(timezone.utc)
    )

    attempted_today = (
        db.query(Attempt.question_id)
        .filter(
            Attempt.user_id      == user_id,
            Attempt.attempted_at >= today_start_utc,
        )
        .subquery()
    )

    selected: List[Question] = []

    # Try to fill difficulty buckets first
    for difficulty, count in DIFFICULTY_MIX.items():
        questions = (
            db.query(Question)
            .filter(
                Question.difficulty == difficulty,
                ~Question.id.in_(attempted_today),
            )
            .order_by(func.random())
            .limit(count)
            .all()
        )
        selected.extend(questions)

    # Fill remaining slots from any unattempted question (covers null-difficulty new questions)
    needed = 5 - len(selected)
    if needed > 0:
        existing_ids = [q.id for q in selected]
        filters = [~Question.id.in_(attempted_today)]
        if existing_ids:
            filters.append(~Question.id.in_(existing_ids))

        fillers = (
            db.query(Question)
            .filter(*filters)
            .order_by(func.random())
            .limit(needed)
            .all()
        )
        selected.extend(fillers)

    return selected
