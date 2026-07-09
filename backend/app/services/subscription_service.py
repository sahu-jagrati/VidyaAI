from datetime import datetime, timezone, timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.subscription_model import Subscription
from app.models.user_model import User
from app.services import razorpay_service


def get_active_subscription(db: Session, user_id: int) -> Subscription | None:
    return (
        db.query(Subscription)
        .filter(
            Subscription.user_id == user_id,
            Subscription.status.in_(["created", "authenticated", "active"]),
        )
        .order_by(Subscription.created_at.desc())
        .first()
    )


def create_subscription(db: Session, user: User, plan_type: str) -> Subscription:
    if plan_type not in ("monthly", "yearly"):
        raise HTTPException(status_code=400, detail="plan_type must be 'monthly' or 'yearly'")

    # Cancel any existing active subscription first
    existing = get_active_subscription(db, user.id)
    if existing:
        raise HTTPException(
            status_code=400,
            detail="You already have an active subscription. Cancel it first or use change-plan.",
        )

    rz_sub = razorpay_service.create_subscription(plan_type)

    now = datetime.now(timezone.utc)
    trial_end = now + timedelta(days=7)

    sub = Subscription(
        user_id=user.id,
        razorpay_subscription_id=rz_sub["id"],
        razorpay_plan_id=rz_sub["plan_id"],
        plan_type=plan_type,
        billing_cycle=plan_type,
        status=rz_sub.get("status", "created"),
        trial_start_date=now,
        trial_end_date=trial_end,
    )
    db.add(sub)
    db.commit()
    db.refresh(sub)
    return sub


def verify_and_activate(
    db: Session,
    user: User,
    razorpay_payment_id: str,
    razorpay_subscription_id: str,
    razorpay_signature: str,
) -> Subscription:
    valid = razorpay_service.verify_payment_signature(
        razorpay_payment_id, razorpay_subscription_id, razorpay_signature
    )
    if not valid:
        raise HTTPException(status_code=400, detail="Invalid payment signature")

    sub = (
        db.query(Subscription)
        .filter(Subscription.razorpay_subscription_id == razorpay_subscription_id)
        .first()
    )
    if not sub or sub.user_id != user.id:
        raise HTTPException(status_code=404, detail="Subscription not found")

    sub.status = "authenticated"
    sub.last_payment_id = razorpay_payment_id
    sub.last_payment_status = "authorized"

    user.is_premium = True
    db.commit()
    db.refresh(sub)
    return sub


def cancel_subscription(db: Session, user: User, cancel_at_period_end: bool = True) -> Subscription:
    sub = get_active_subscription(db, user.id)
    if not sub:
        raise HTTPException(status_code=404, detail="No active subscription found")

    razorpay_service.cancel_subscription(
        sub.razorpay_subscription_id, cancel_at_cycle_end=cancel_at_period_end
    )

    sub.cancel_at_period_end = cancel_at_period_end
    if not cancel_at_period_end:
        sub.status = "cancelled"
        sub.cancelled_at = datetime.now(timezone.utc)
        user.is_premium = False

    db.commit()
    db.refresh(sub)
    return sub


def handle_webhook_event(db: Session, event: dict) -> None:
    event_type = event.get("event", "")
    payload = event.get("payload", {})

    sub_entity = payload.get("subscription", {}).get("entity", {})
    payment_entity = payload.get("payment", {}).get("entity", {})

    rz_sub_id = sub_entity.get("id") or payment_entity.get("subscription_id")
    if not rz_sub_id:
        return

    sub = (
        db.query(Subscription)
        .filter(Subscription.razorpay_subscription_id == rz_sub_id)
        .first()
    )
    if not sub:
        return

    user = db.query(User).filter(User.id == sub.user_id).first()

    if event_type == "subscription.activated":
        sub.status = "active"
        sub.autopay_enabled = True
        if user:
            user.is_premium = True

    elif event_type == "subscription.charged":
        sub.status = "active"
        sub.last_payment_id = payment_entity.get("id")
        sub.last_payment_status = "captured"
        if user:
            user.is_premium = True
        # Update billing dates from Razorpay entity
        cs = sub_entity.get("current_start")
        ce = sub_entity.get("current_end")
        if cs:
            sub.current_period_start = datetime.fromtimestamp(cs, tz=timezone.utc)
        if ce:
            sub.current_period_end = datetime.fromtimestamp(ce, tz=timezone.utc)
        charge_at = sub_entity.get("charge_at")
        if charge_at:
            sub.next_billing_date = datetime.fromtimestamp(charge_at, tz=timezone.utc)

    elif event_type == "subscription.halted":
        sub.status = "halted"
        sub.last_payment_status = "failed"
        if user:
            user.is_premium = False

    elif event_type in ("subscription.cancelled", "subscription.completed"):
        sub.status = event_type.split(".")[1]
        sub.cancelled_at = datetime.now(timezone.utc)
        if user:
            user.is_premium = False

    elif event_type == "subscription.pending":
        sub.status = "pending"

    elif event_type == "payment.failed":
        sub.last_payment_status = "failed"

    sub.updated_at = datetime.now(timezone.utc)
    db.commit()
