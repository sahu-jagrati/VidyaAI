"""
cleanup_cube_cuboid_keep_52_53_54.py
=====================================
Deletes ALL Cube & Cuboid questions EXCEPT question_numbers 52, 53, 54
(the three Piyush Varshney questions added in sheet8).

Run from backend/ directory:
    python cleanup_cube_cuboid_keep_52_53_54.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"
KEEP    = {52, 53, 54}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    deleted = kept = 0
    try:
        rows = (
            db.query(Question)
            .filter(Question.subject == SUBJECT, Question.topic == TOPIC)
            .all()
        )
        print(f"Total rows found in '{TOPIC}': {len(rows)}")

        for row in rows:
            if row.question_number in KEEP:
                print(f"  KEEP   Q{row.question_number}")
                kept += 1
            else:
                print(f"  DELETE Q{row.question_number}")
                db.delete(row)
                deleted += 1

        db.commit()
        print(f"\nDone — deleted: {deleted}, kept: {kept}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
