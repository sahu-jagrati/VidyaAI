import razorpay
import hmac
import hashlib
from datetime import datetime, timezone, timedelta
from app import config

_client: razorpay.Client | None = None


def _get_client() -> razorpay.Client:
    global _client
    if _client is None:
        _client = razorpay.Client(
            auth=(config.RAZORPAY_KEY_ID, config.RAZORPAY_KEY_SECRET)
        )
    return _client


def create_subscription(plan_type: str, customer_notify: int = 1) -> dict:
    plan_id = (
        config.RAZORPAY_MONTHLY_PLAN_ID
        if plan_type == "monthly"
        else config.RAZORPAY_YEARLY_PLAN_ID
    )
    # 7-day trial: delay first billing by 7 days via start_at
    start_at = int((datetime.now(timezone.utc) + timedelta(days=7)).timestamp())

    subscription = _get_client().subscription.create(
        {
            "plan_id": plan_id,
            "total_count": 120,
            "quantity": 1,
            "customer_notify": customer_notify,
            "start_at": start_at,
            "addons": [],
            "notes": {
                "plan_type": plan_type,
                "product": "VidyaAI Premium",
            },
        }
    )
    return subscription


def verify_payment_signature(
    razorpay_payment_id: str,
    razorpay_subscription_id: str,
    razorpay_signature: str,
) -> bool:
    message = f"{razorpay_payment_id}|{razorpay_subscription_id}"
    expected = hmac.new(
        config.RAZORPAY_KEY_SECRET.encode("utf-8"),
        message.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(expected, razorpay_signature)


def verify_webhook_signature(body: bytes, signature: str) -> bool:
    expected = hmac.new(
        config.RAZORPAY_WEBHOOK_SECRET.encode("utf-8"),
        body,
        hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(expected, signature)


def fetch_subscription(razorpay_subscription_id: str) -> dict:
    return _get_client().subscription.fetch(razorpay_subscription_id)


def cancel_subscription(razorpay_subscription_id: str, cancel_at_cycle_end: bool = True) -> dict:
    return _get_client().subscription.cancel(
        razorpay_subscription_id,
        {"cancel_at_cycle_end": 1 if cancel_at_cycle_end else 0},
    )
