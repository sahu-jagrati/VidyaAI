from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CreateSubscriptionRequest(BaseModel):
    plan_type: str  # 'monthly' | 'yearly'


class CreateSubscriptionResponse(BaseModel):
    subscription_id: int
    razorpay_subscription_id: str
    razorpay_key_id: str
    plan_type: str
    status: str


class VerifySubscriptionRequest(BaseModel):
    razorpay_payment_id: str
    razorpay_subscription_id: str
    razorpay_signature: str


class SubscriptionStatusResponse(BaseModel):
    id: int
    plan_type: str
    status: str
    trial_start_date: Optional[datetime]
    trial_end_date: Optional[datetime]
    next_billing_date: Optional[datetime]
    current_period_start: Optional[datetime]
    current_period_end: Optional[datetime]
    autopay_enabled: bool
    cancel_at_period_end: bool
    cancelled_at: Optional[datetime]
    razorpay_subscription_id: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class CancelSubscriptionRequest(BaseModel):
    cancel_at_period_end: bool = True  # False = immediate cancel


class ChangePlanRequest(BaseModel):
    new_plan_type: str  # 'monthly' | 'yearly'
