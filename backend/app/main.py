from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.database.connection import Base, engine
from app.models import user_model, question_model, attempt_model  # noqa: F401
from app.models import news_model, push_model                      # noqa: F401
from app.models import subscription_model                          # noqa: F401
from app.routes import auth, questions, users, leaderboard
from app.routes import news, notifications
from app.routes import subscription, webhooks
from app import scheduler


def _run_migrations():
    Base.metadata.create_all(bind=engine)
    with engine.connect() as conn:
        conn.execute(text("ALTER TABLE news_articles ADD COLUMN IF NOT EXISTS lang VARCHAR(5) NOT NULL DEFAULT 'en'"))
        conn.execute(text("ALTER TABLE news_articles ADD COLUMN IF NOT EXISTS title_hi TEXT"))
        conn.execute(text("ALTER TABLE news_articles ADD COLUMN IF NOT EXISTS summary_hi TEXT"))
        conn.execute(text("ALTER TABLE questions ADD COLUMN IF NOT EXISTS question_text_hi TEXT"))
        conn.execute(text("ALTER TABLE questions ADD COLUMN IF NOT EXISTS option_a_hi TEXT"))
        conn.execute(text("ALTER TABLE questions ADD COLUMN IF NOT EXISTS option_b_hi TEXT"))
        conn.execute(text("ALTER TABLE questions ADD COLUMN IF NOT EXISTS option_c_hi TEXT"))
        conn.execute(text("ALTER TABLE questions ADD COLUMN IF NOT EXISTS option_d_hi TEXT"))
        conn.execute(text("ALTER TABLE questions ADD COLUMN IF NOT EXISTS explanation_hi TEXT"))
        # Subscription / premium columns on users
        conn.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS is_premium BOOLEAN NOT NULL DEFAULT FALSE"))
        conn.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS subscription_id INTEGER"))
        conn.commit()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("====== VidyaAi backend starting (Hindi support enabled) ======")
    _run_migrations()
    scheduler.start()
    yield
    scheduler.stop()


app = FastAPI(
    title="VidyaAi API",
    description="Backend for VidyaAi — gamified SSC CGL exam preparation",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(questions.router)
app.include_router(users.router)
app.include_router(leaderboard.router)
app.include_router(news.router)
app.include_router(notifications.router)
app.include_router(subscription.router)
app.include_router(webhooks.router)


@app.get("/", tags=["Health"])
def health():
    return {"status": "ok", "message": "VidyaAi Backend is running 🚀"}
