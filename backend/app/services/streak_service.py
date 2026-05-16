"""
Streak rules:
  - Streak increments when user submits at least 1 correct answer on a new calendar day (IST).
  - If user missed yesterday → streak resets to 1 (today counts as day 1).
  - Same-day activity → streak unchanged (already counted).
"""

from datetime import datetime, timezone, timedelta
from sqlalchemy.orm import Session
from app.models.user_model import User


IST = timezone(timedelta(hours=5, minutes=30))


def _today_ist() -> datetime:
    return datetime.now(IST).date()


def update_streak(user: User) -> None:
    """
    Called after a correct answer is recorded.
    Mutates `user` in place — caller must commit the session.
    """
    today = _today_ist()

    if user.last_activity is None:
        # First ever activity
        user.current_streak = 1
    else:
        last = user.last_activity.astimezone(IST).date()
        delta = (today - last).days

        if delta == 0:
            pass                              # Already played today — streak unchanged
        elif delta == 1:
            user.current_streak += 1          # Consecutive day — extend streak
        else:
            user.current_streak = 1           # Missed day(s) — reset to 1

    # Always update highest streak
    if user.current_streak > user.highest_streak:
        user.highest_streak = user.current_streak

    user.last_activity = datetime.now(timezone.utc)
