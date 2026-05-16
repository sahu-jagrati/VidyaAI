from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from datetime import datetime, timezone, timedelta
from typing import List

from app.database.connection import get_db
from app.models.user_model   import User
from app.models.attempt_model import Attempt
from app.utils.helpers        import get_current_user

router = APIRouter(prefix="/leaderboard", tags=["Leaderboard"])


def _rank_data(user: User, rank: int, is_current: bool = False) -> dict:
    return {
        "rank":          rank,
        "user_id":       user.id,
        "name":          user.name,
        "xp":            user.xp,
        "current_streak":user.current_streak,
        "accuracy":      user.accuracy,
        "is_current_user": is_current,
    }


@router.get("")
def get_leaderboard(
    filter:       str     = Query("weekly", enum=["daily", "weekly", "monthly", "all"]),
    limit:        int     = Query(50, le=100),
    current_user: User    = Depends(get_current_user),
    db:           Session = Depends(get_db),
):
    """
    Returns top users ranked by XP.
    filter = all     → total XP
    filter = daily   → XP earned today (IST)
    filter = weekly  → XP earned this week
    filter = monthly → XP earned this month
    """
    IST = timezone(timedelta(hours=5, minutes=30))
    now_ist = datetime.now(IST)

    if filter == "all":
        # Sort by total XP
        top_users = (
            db.query(User)
            .order_by(desc(User.xp))
            .limit(limit)
            .all()
        )
        entries = [_rank_data(u, i + 1, u.id == current_user.id) for i, u in enumerate(top_users)]

    else:
        # Calculate period start
        if filter == "daily":
            period_start = now_ist.replace(hour=0, minute=0, second=0, microsecond=0)
        elif filter == "weekly":
            period_start = now_ist - timedelta(days=now_ist.weekday())
            period_start = period_start.replace(hour=0, minute=0, second=0, microsecond=0)
        else:  # monthly
            period_start = now_ist.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        period_start_utc = period_start.astimezone(timezone.utc)

        # Sum XP earned in the period from attempts table
        xp_in_period = (
            db.query(
                Attempt.user_id,
                func.sum(Attempt.xp_earned).label("period_xp"),
            )
            .filter(Attempt.attempted_at >= period_start_utc)
            .group_by(Attempt.user_id)
            .order_by(desc("period_xp"))
            .limit(limit)
            .subquery()
        )

        rows = (
            db.query(User, xp_in_period.c.period_xp)
            .join(xp_in_period, User.id == xp_in_period.c.user_id)
            .order_by(desc(xp_in_period.c.period_xp))
            .all()
        )

        entries = []
        for i, (user, period_xp) in enumerate(rows):
            entry = _rank_data(user, i + 1, user.id == current_user.id)
            entry["xp"] = period_xp or 0
            entries.append(entry)

    # Inject current user's rank if not in top list
    current_in_list = any(e["is_current_user"] for e in entries)
    if not current_in_list:
        all_xp = db.query(User.xp).order_by(desc(User.xp)).all()
        my_rank = next((i + 1 for i, (xp,) in enumerate(all_xp) if xp <= current_user.xp), len(all_xp))
        entries.append({**_rank_data(current_user, my_rank, True), "is_outside_top": True})

    return {"filter": filter, "entries": entries}
