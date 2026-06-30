from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime, timezone
from app.database.connection import Base


class PushSubscription(Base):
    __tablename__ = "push_subscriptions"

    id            = Column(Integer, primary_key=True, index=True)
    user_id       = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    endpoint      = Column(String(1000), nullable=False, unique=True)
    p256dh        = Column(String(500), nullable=False)
    auth          = Column(String(200), nullable=False)
    reminder_time = Column(String(5), nullable=True)   # "HH:MM" in IST
    created_at    = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
