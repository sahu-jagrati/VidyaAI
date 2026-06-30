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

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set in .env file")
