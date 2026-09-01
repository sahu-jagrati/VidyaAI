"""
cleanup_dice_topic.py
=====================
Removes all questions from topic 'Dice' EXCEPT question_numbers 1, 2, 3, 4.
Run from backend/ directory:
    python cleanup_dice_topic.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Dice"
KEEP    = {1, 2, 3, 4}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    try:
        all_rows = (
            db.query(Question)
            .filter(Question.subject == SUBJECT, Question.topic == TOPIC)
            .order_by(Question.question_number)
            .all()
        )
        print(f"Total '{TOPIC}' questions in DB: {len(all_rows)}")

        to_delete = [r for r in all_rows if r.question_number not in KEEP]
        to_keep   = [r for r in all_rows if r.question_number in KEEP]

        print(f"Keeping  : {sorted(r.question_number for r in to_keep)}")
        print(f"Deleting : {sorted(r.question_number for r in to_delete)} ({len(to_delete)} rows)")

        for r in to_delete:
            db.delete(r)

        db.commit()
        print(f"\nDone — deleted {len(to_delete)} questions, kept {len(to_keep)}.")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
