import json
from datetime import datetime, date
from zoneinfo import ZoneInfo
from sqlalchemy.orm import Session
from pywebpush import webpush, WebPushException

from app.models.push_model import PushSubscription
from app.models.attempt_model import Attempt
from app.config import VAPID_PRIVATE_KEY, VAPID_EMAIL

IST = ZoneInfo("Asia/Kolkata")


def _send_push(sub: PushSubscription, title: str, body: str, url: str = "/daily-challenge") -> bool:
    if not VAPID_PRIVATE_KEY:
        print("[push] VAPID_PRIVATE_KEY not configured — skipping push")
        return False
    try:
        webpush(
            subscription_info={
                "endpoint": sub.endpoint,
                "keys": {"p256dh": sub.p256dh, "auth": sub.auth},
            },
            data=json.dumps({"title": title, "body": body, "url": url}),
            vapid_private_key=VAPID_PRIVATE_KEY,
            vapid_claims={"sub": f"mailto:{VAPID_EMAIL}"},
        )
        return True
    except WebPushException as exc:
        print(f"[push] WebPushException for endpoint {sub.endpoint[:40]}…: {exc}")
        if exc.response and exc.response.status_code == 410:
            return None  # subscription expired — caller should delete it
        return False
    except Exception as exc:
        print(f"[push] Unexpected error: {exc}")
        return False


def send_reminders(db: Session) -> None:
    now_ist = datetime.now(IST)
    current_hhmm = now_ist.strftime("%H:%M")
    today_ist = now_ist.date()

    subs = (
        db.query(PushSubscription)
        .filter(PushSubscription.reminder_time == current_hhmm)
        .all()
    )
    if not subs:
        return

    for sub in subs:
        # Check if user already attempted anything today (IST)
        today_start_utc = datetime(
            today_ist.year, today_ist.month, today_ist.day, tzinfo=IST
        ).astimezone(tz=None).replace(tzinfo=None)

        practiced = (
            db.query(Attempt)
            .filter(
                Attempt.user_id == sub.user_id,
                Attempt.attempted_at >= datetime(
                    today_ist.year, today_ist.month, today_ist.day,
                    tzinfo=IST,
                ),
            )
            .first()
        )
        if practiced:
            continue

        result = _send_push(
            sub,
            title="⚡ Time to Practice!",
            body="It's your scheduled practice time. Keep your streak alive! 🔥",
        )
        if result is None:  # expired subscription
            db.delete(sub)

    db.commit()
