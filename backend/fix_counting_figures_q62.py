"""
fix_counting_figures_q62.py
============================
Corrects Q62 (Counting Figures): correct_answer was stored as D (85)
but should be B (75).

Correct answer: B (75)
Reasoning: 4×4 base grid (30 squares) + 4 embedded inner sub-structures
each contributing additional squares → total = 75.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Counting Figures"


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    try:
        q62 = (
            db.query(Question)
            .filter(
                Question.subject         == SUBJECT,
                Question.topic           == TOPIC,
                Question.question_number == 62,
            )
            .first()
        )
        if q62 is None:
            print("ERROR: Q62 not found in DB")
            return

        print(f"  BEFORE  Q62 → correct_answer={q62.correct_answer}")
        q62.correct_answer = "B"   # 75 squares
        db.commit()
        print(f"  AFTER   Q62 → correct_answer={q62.correct_answer}")
        print("\nDone — Q62 corrected to B (75).")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
