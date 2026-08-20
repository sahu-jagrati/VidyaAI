"""
fix_cause_effect_question_text.py
===================================
Removes the embedded "(e) If both..." option text from the question_en and
question_hi fields of Cause and Effect Q1 and Q2.

The option E is already injected by the frontend via CE_OPTION_E constant, so
it must NOT also appear inside the question body.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Cause and Effect"

# The suffix that was incorrectly embedded in the question body
_SUFFIX_EN = (
    "\n\n(e) If both the statements (A) & (B) are effects of a common cause. / "
    "यदि दोनों कथन (A) और (B) किसी सामान्य कारण के परिणाम हैं।"
)
_SUFFIX_HI = _SUFFIX_EN   # same text was appended to both fields


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    fixed = 0
    try:
        questions = (
            db.query(Question)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        )

        for q in questions:
            changed = False

            if q.question_en and q.question_en.endswith(_SUFFIX_EN):
                q.question_en = q.question_en[: -len(_SUFFIX_EN)]
                changed = True

            if q.question_hi and q.question_hi.endswith(_SUFFIX_HI):
                q.question_hi = q.question_hi[: -len(_SUFFIX_HI)]
                changed = True

            if changed:
                print(f"  FIXED Q{q.question_number}")
                fixed += 1
            else:
                print(f"  OK    Q{q.question_number} (no embedded suffix found)")

        db.commit()
        print(f"\nDone -- fixed: {fixed}")

    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
