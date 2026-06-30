from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, Integer
from typing import Dict
from datetime import datetime, timezone, timedelta

from app.database.connection import get_db
from app.models.user_model   import User
from app.models.attempt_model import Attempt
from app.models.question_model import Question
from app.schemas.user_schema  import UserResponse
from app.utils.helpers        import get_current_user

IST = timezone(timedelta(hours=5, minutes=30))

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    """Get the currently logged-in user's profile."""
    return current_user


@router.get("/stats")
def get_stats(
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    """Breakdown of accuracy and attempts by subject."""
    rows = (
        db.query(
            Question.subject,
            func.count(Attempt.id).label("total"),
            func.sum(Attempt.is_correct.cast(Integer)).label("correct"),
        )
        .join(Question, Attempt.question_id == Question.id)
        .filter(Attempt.user_id == current_user.id)
        .group_by(Question.subject)
        .all()
    )

    subject_stats: Dict = {}
    for row in rows:
        total   = row.total   or 0
        correct = row.correct or 0
        subject_stats[row.subject] = {
            "solved":   total,
            "correct":  correct,
            "accuracy": round((correct / total * 100), 1) if total else 0,
        }

    return {
        "user_id":        current_user.id,
        "xp":             current_user.xp,
        "current_streak": current_user.current_streak,
        "highest_streak": current_user.highest_streak,
        "total_questions":current_user.total_questions,
        "accuracy":       current_user.accuracy,
        "subject_stats":  subject_stats,
    }


@router.get("/activity")
def get_activity(
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    """Return active dates (last 90 days) and whether today's challenge is done."""
    ninety_days_ago = datetime.now(timezone.utc) - timedelta(days=90)

    # Convert UTC → IST before taking the date so calendar days match the user's local date
    ist_date = func.date(func.timezone('Asia/Kolkata', Attempt.attempted_at))

    rows = (
        db.query(ist_date.label("day"))
        .filter(
            Attempt.user_id      == current_user.id,
            Attempt.attempted_at >= ninety_days_ago,
        )
        .distinct()
        .all()
    )
    active_dates = [str(row.day) for row in rows]

    count_rows = (
        db.query(
            ist_date.label("day"),
            func.count(Attempt.id).label("cnt"),
        )
        .filter(
            Attempt.user_id      == current_user.id,
            Attempt.attempted_at >= ninety_days_ago,
        )
        .group_by(ist_date)
        .all()
    )
    submission_counts = {str(row.day): row.cnt for row in count_rows}

    today_start_utc = (
        datetime.now(IST)
        .replace(hour=0, minute=0, second=0, microsecond=0)
        .astimezone(timezone.utc)
    )
    today_done = (
        db.query(Attempt)
        .filter(
            Attempt.user_id      == current_user.id,
            Attempt.attempted_at >= today_start_utc,
        )
        .first()
    ) is not None

    return {
        "active_dates":      active_dates,
        "today_done":        today_done,
        "current_streak":    current_user.current_streak,
        "highest_streak":    current_user.highest_streak,
        "submission_counts": submission_counts,
    }
