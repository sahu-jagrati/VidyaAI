"""
add_option_image_url_column.py
==============================
Adds the `option_image_url` column to the questions table (if it doesn't
already exist), then sets it for Cube-and-Dice questions that have an
options-panel image uploaded to Supabase Storage.

Run from backend/ directory:
    python add_option_image_url_column.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from sqlalchemy import text
from app.database.connection import SessionLocal, engine
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Cube and Dice"
BASE    = (
    "https://mlzcmlopkddsdwcmiujq.supabase.co"
    "/storage/v1/object/public/question_image_Cube_and_Dice"
)

# Questions that have a separate options-panel image (cube_dice_ans_N.png)
ANS_IMAGE_QUESTIONS = [2, 3, 8, 11, 12, 13, 24, 25]


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    # ── Step 1: add column if missing ────────────────────────────────────────
    with engine.connect() as conn:
        # Check if column already exists
        result = conn.execute(text(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_name='questions' AND column_name='option_image_url'"
        ))
        if result.fetchone():
            print("Column `option_image_url` already exists — skipping ALTER.")
        else:
            conn.execute(text(
                "ALTER TABLE questions ADD COLUMN option_image_url TEXT"
            ))
            conn.commit()
            print("Column `option_image_url` added to questions table ✅")

    # ── Step 2: set option_image_url for the 8 Cube-and-Dice questions ───────
    db = SessionLocal()
    updated = not_found = already_set = 0
    try:
        for qnum in ANS_IMAGE_QUESTIONS:
            url = f"{BASE}/cube_dice_ans_{qnum}.png"
            row = (
                db.query(Question)
                .filter(
                    Question.subject         == SUBJECT,
                    Question.topic           == TOPIC,
                    Question.question_number == qnum,
                )
                .first()
            )
            if row is None:
                print(f"  NOT FOUND  Q{qnum}")
                not_found += 1
                continue
            if row.option_image_url == url:
                print(f"  SKIP (already set)  Q{qnum}")
                already_set += 1
                continue
            row.option_image_url = url
            updated += 1
            print(f"  UPDATED  Q{qnum}  →  cube_dice_ans_{qnum}.png")

        db.commit()
        print(
            f"\nDone — updated: {updated}, "
            f"already set: {already_set}, "
            f"not found: {not_found}"
        )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
