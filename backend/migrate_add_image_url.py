"""
migrate_add_image_url.py
Adds image_url column to questions table (idempotent — skips if already exists).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import engine
from sqlalchemy import text

def main():
    with engine.connect() as conn:
        # Check if column already exists (PostgreSQL)
        result = conn.execute(text("""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = 'questions'
              AND column_name = 'image_url'
        """))
        if result.fetchone():
            print("Column 'image_url' already exists — skipping.")
        else:
            conn.execute(text(
                "ALTER TABLE questions ADD COLUMN image_url TEXT NULL"
            ))
            conn.commit()
            print("Column 'image_url' added to questions table.")

if __name__ == "__main__":
    main()
