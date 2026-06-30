"""
Run once to create all tables in the database.
Usage:  python -m app.database.init_db
"""
from app.database.connection import Base, engine

from app.models import user_model, question_model, attempt_model   # noqa: F401
from app.models import news_model, push_model, processed_file_model # noqa: F401
from sqlalchemy import text


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("All tables created successfully.")

    # Migration: add lang column to news_articles if it doesn't exist
    try:
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE news_articles ADD COLUMN IF NOT EXISTS lang VARCHAR(5) NOT NULL DEFAULT 'en'"))
            conn.commit()
    except Exception:
        pass


if __name__ == "__main__":
    create_tables()
