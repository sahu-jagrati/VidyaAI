"""
Run once to create all tables in the database.
Usage:  python -m app.database.init_db
"""
from app.database.connection import Base, engine

# Import models so SQLAlchemy registers them before creating tables
from app.models import user_model, question_model, attempt_model  # noqa: F401


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ All tables created successfully.")


if __name__ == "__main__":
    create_tables()
