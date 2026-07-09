from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.utils.helpers import get_current_user
from app.models.user_model import User
from app.schemas.subscription import (
    CreateSubscriptionRequest,
    CreateSubscriptionResponse,
    VerifySubscriptionRequest,
    SubscriptionStatusResponse,
    CancelSubscriptionRequest,
    ChangePlanRequest,
)
from app.services import subscription_service, razorpay_service
from app import config

router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])


@router.post("/create", response_model=CreateSubscriptionResponse)
def create_subscription(
    body: CreateSubscriptionRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    sub = subscription_service.create_subscription(db, user, body.plan_type)
    return CreateSubscriptionResponse(
        subscription_id=sub.id,
        razorpay_subscription_id=sub.razorpay_subscription_id,
        razorpay_key_id=config.RAZORPAY_KEY_ID,
        plan_type=sub.plan_type,
        status=sub.status,
    )


@router.post("/verify")
def verify_subscription(
    body: VerifySubscriptionRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    sub = subscription_service.verify_and_activate(
        db,
        user,
        body.razorpay_payment_id,
        body.razorpay_subscription_id,
        body.razorpay_signature,
    )
    return {"message": "Subscription activated successfully", "status": sub.status}


@router.get("/me", response_model=SubscriptionStatusResponse)
def get_my_subscription(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    sub = subscription_service.get_active_subscription(db, user.id)
    if not sub:
        raise HTTPException(status_code=404, detail="No active subscription found")
    return sub


@router.post("/cancel")
def cancel_subscription(
    body: CancelSubscriptionRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    sub = subscription_service.cancel_subscription(db, user, body.cancel_at_period_end)
    msg = (
        "Subscription will be cancelled at end of current billing period."
        if body.cancel_at_period_end
        else "Subscription cancelled immediately."
    )
    return {"message": msg, "status": sub.status}


@router.post("/change-plan")
def change_plan(
    body: ChangePlanRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    if body.new_plan_type not in ("monthly", "yearly"):
        raise HTTPException(status_code=400, detail="new_plan_type must be 'monthly' or 'yearly'")

    # Cancel existing then create new
    existing = subscription_service.get_active_subscription(db, user.id)
    if existing:
        subscription_service.cancel_subscription(db, user, cancel_at_period_end=False)

    sub = subscription_service.create_subscription(db, user, body.new_plan_type)
    return CreateSubscriptionResponse(
        subscription_id=sub.id,
        razorpay_subscription_id=sub.razorpay_subscription_id,
        razorpay_key_id=config.RAZORPAY_KEY_ID,
        plan_type=sub.plan_type,
        status=sub.status,
    )
