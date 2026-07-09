# Subscription model — tracks each user's Razorpay subscription lifecycle.
# One user → one active subscription at a time (previous ones remain for history).
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.database.connection import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id                       = Column(Integer, primary_key=True, index=True)

    # Link to user
    user_id                  = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    # Razorpay identifiers
    razorpay_subscription_id = Column(String(100), unique=True, index=True, nullable=True)
    razorpay_plan_id         = Column(String(100), nullable=True)

    # Plan details
    plan_type                = Column(String(20), nullable=False)   # 'monthly' | 'yearly'
    billing_cycle            = Column(String(20), nullable=False)   # 'monthly' | 'yearly'

    # Status from Razorpay: created → authenticated → active → halted / cancelled / completed
    status                   = Column(String(30), default="created", nullable=False)

    # Trial window (7 days from mandate creation)
    trial_start_date         = Column(DateTime(timezone=True), nullable=True)
    trial_end_date           = Column(DateTime(timezone=True), nullable=True)

    # Billing dates (populated by webhook events)
    next_billing_date        = Column(DateTime(timezone=True), nullable=True)
    current_period_start     = Column(DateTime(timezone=True), nullable=True)
    current_period_end       = Column(DateTime(timezone=True), nullable=True)

    # AutoPay / payment details
    autopay_enabled          = Column(Boolean, default=False)
    payment_method           = Column(String(50), nullable=True)   # 'upi' | 'card' | 'netbanking'

    # Cancellation
    cancel_at_period_end     = Column(Boolean, default=False)
    cancelled_at             = Column(DateTime(timezone=True), nullable=True)

    # Last payment info (updated by webhook)
    last_payment_id          = Column(String(100), nullable=True)
    last_payment_status      = Column(String(30), nullable=True)

    # Timestamps
    created_at               = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at               = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc),
                                      onupdate=lambda: datetime.now(timezone.utc))

    # Relationship back to user
    user = relationship("User", back_populates="subscriptions")
