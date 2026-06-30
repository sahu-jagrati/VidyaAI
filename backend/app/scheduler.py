import threading
from datetime import datetime, timezone
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger

from app.database.connection import SessionLocal
from app.models.news_model import NewsArticle
from app.services.news_service import fetch_and_store_news, translate_missing
from app.services.question_translation_service import translate_missing_questions
from app.services.push_service import send_reminders

NEWS_STALE_HOURS = 12   # fetch on startup if last article is older than this

_scheduler = BackgroundScheduler(timezone="Asia/Kolkata")


def _news_job():
    db = SessionLocal()
    try:
        fetch_and_store_news(db)
        translate_missing(db)
        translate_missing_questions(db)
    except Exception as exc:
        print(f"[scheduler] news job error: {exc}")
    finally:
        db.close()


def _translate_job():
    db = SessionLocal()
    try:
        translate_missing(db)
        translate_missing_questions(db)
    except Exception as exc:
        print(f"[scheduler] translate job error: {exc}")
    finally:
        db.close()


def _reminder_job():
    db = SessionLocal()
    try:
        send_reminders(db)
    except Exception as exc:
        print(f"[scheduler] reminder job error: {exc}")
    finally:
        db.close()


def start():
    if _scheduler.running:
        return

    # Fetch news every day at 06:00 and 18:00 IST
    _scheduler.add_job(_news_job, CronTrigger(hour="6,18", minute=0), id="news_fetch", replace_existing=True)
    # Check reminders every minute
    _scheduler.add_job(_reminder_job, IntervalTrigger(minutes=1), id="reminders", replace_existing=True)
    _scheduler.start()

    # Fetch on startup if DB is empty or last article is older than NEWS_STALE_HOURS
    db = SessionLocal()
    try:
        latest = db.query(NewsArticle).order_by(NewsArticle.created_at.desc()).first()
        if latest is None:
            needs_fetch = True
            reason = "DB empty"
        else:
            age_hours = (datetime.now(timezone.utc) - latest.created_at).total_seconds() / 3600
            needs_fetch = age_hours >= NEWS_STALE_HOURS
            reason = f"last article is {age_hours:.1f}h old"
    finally:
        db.close()

    if needs_fetch:
        print(f"[scheduler] {reason} — running news fetch in background...")
        threading.Thread(target=_news_job, daemon=True).start()
    else:
        print(f"[scheduler] News is fresh ({reason}) — back-filling translations...")
        threading.Thread(target=_translate_job, daemon=True).start()


def stop():
    if _scheduler.running:
        _scheduler.shutdown(wait=False)
