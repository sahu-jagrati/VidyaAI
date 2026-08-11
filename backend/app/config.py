import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL: str = os.getenv("DATABASE_URL", "")
SECRET_KEY: str   = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
ALGORITHM: str    = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))
GOOGLE_CLIENT_ID: str   = os.getenv("GOOGLE_CLIENT_ID", "")
VAPID_PRIVATE_KEY: str  = os.getenv("VAPID_PRIVATE_KEY", "")
VAPID_PUBLIC_KEY: str   = os.getenv("VAPID_PUBLIC_KEY", "")
VAPID_EMAIL: str        = os.getenv("VAPID_EMAIL", "support@vidyaai.in")

# ── RAZORPAY (commented out) ──────────────────────────────────────────────────
# RAZORPAY_KEY_ID: str        = os.getenv("RAZORPAY_KEY_ID", "")
# RAZORPAY_KEY_SECRET: str    = os.getenv("RAZORPAY_KEY_SECRET", "")
# RAZORPAY_WEBHOOK_SECRET: str = os.getenv("RAZORPAY_WEBHOOK_SECRET", "")
# RAZORPAY_MONTHLY_PLAN_ID: str = os.getenv("RAZORPAY_MONTHLY_PLAN_ID", "")
# RAZORPAY_YEARLY_PLAN_ID: str  = os.getenv("RAZORPAY_YEARLY_PLAN_ID", "")
# ─────────────────────────────────────────────────────────────────────────────

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set in .env file")
