"""
fix_columns.py
==============
1. Drops the wrongly-named `option_image_url` column (if it exists).
2. Verifies `answer_image_url` is set correctly.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from sqlalchemy import text
from app.database.connection import engine

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    with engine.connect() as conn:
        # Drop the wrong column if present
        res = conn.execute(text(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_name='questions' AND column_name='option_image_url'"
        ))
        if res.fetchone():
            conn.execute(text("ALTER TABLE questions DROP COLUMN option_image_url"))
            conn.commit()
            print("Dropped extra `option_image_url` column ✅")
        else:
            print("`option_image_url` column not found — nothing to drop")

        # Verify answer_image_url
        res2 = conn.execute(text(
            "SELECT question_number, answer_image_url FROM questions "
            "WHERE topic='Cube and Dice' AND answer_image_url IS NOT NULL "
            "ORDER BY question_number"
        ))
        rows = res2.fetchall()
        print(f"\nQuestions with answer_image_url set: {len(rows)}")
        for r in rows:
            print(f"  Q{r[0]}: {r[1]}")

if __name__ == "__main__":
    main()
