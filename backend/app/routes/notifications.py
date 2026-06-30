from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from pydantic import BaseModel

from app.database.connection import get_db
from app.models.push_model import PushSubscription
from app.utils.helpers import get_current_user
from app.config import VAPID_PUBLIC_KEY

router = APIRouter(prefix="/notifications", tags=["Notifications"])


class SubscribePayload(BaseModel):
    endpoint:      str
    p256dh:        str
    auth:          str
    reminder_time: Optional[str] = None   # "HH:MM"


class ReminderPayload(BaseModel):
    reminder_time: Optional[str]  # "HH:MM" or null to clear


@router.get("/vapid-key")
def vapid_key():
    return {"public_key": VAPID_PUBLIC_KEY}


@router.post("/subscribe")
def subscribe(
    payload:      SubscribePayload,
    db:           Session = Depends(get_db),
    current_user          = Depends(get_current_user),
):
    existing = db.query(PushSubscription).filter(
        PushSubscription.endpoint == payload.endpoint
    ).first()

    if existing:
        existing.p256dh        = payload.p256dh
        existing.auth          = payload.auth
        existing.reminder_time = payload.reminder_time
    else:
        sub = PushSubscription(
            user_id       = current_user.id,
            endpoint      = payload.endpoint,
            p256dh        = payload.p256dh,
            auth          = payload.auth,
            reminder_time = payload.reminder_time,
        )
        db.add(sub)

    db.commit()
    return {"status": "subscribed"}


@router.delete("/unsubscribe")
def unsubscribe(
    endpoint:     str,
    db:           Session = Depends(get_db),
    current_user          = Depends(get_current_user),
):
    sub = db.query(PushSubscription).filter(
        PushSubscription.endpoint == endpoint,
        PushSubscription.user_id  == current_user.id,
    ).first()
    if sub:
        db.delete(sub)
        db.commit()
    return {"status": "unsubscribed"}


@router.put("/reminder")
def set_reminder(
    payload:      ReminderPayload,
    db:           Session = Depends(get_db),
    current_user          = Depends(get_current_user),
):
    subs = db.query(PushSubscription).filter(
        PushSubscription.user_id == current_user.id
    ).all()
    if not subs:
        raise HTTPException(status_code=404, detail="No push subscription found. Enable notifications first.")
    for sub in subs:
        sub.reminder_time = payload.reminder_time
    db.commit()
    return {"status": "updated", "reminder_time": payload.reminder_time}


@router.get("/my-subscription")
def my_subscription(
    db:           Session = Depends(get_db),
    current_user          = Depends(get_current_user),
):
    sub = db.query(PushSubscription).filter(
        PushSubscription.user_id == current_user.id
    ).first()
    if not sub:
        return {"subscribed": False, "reminder_time": None}
    return {"subscribed": True, "reminder_time": sub.reminder_time}
