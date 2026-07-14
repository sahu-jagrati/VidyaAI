"""
seed_reasoning_cube_cuboid_sheet5.py
=====================================
Seeds the 6 questions that were skipped in sheet4 due to the 80-char dedup
fingerprint collision — the sheet4 prefix was 72 chars, leaving only 8 chars
for the sub-question distinguisher ("3" vs "2" vs "4"), which fell past char 80.
This script uses a shorter 62-char prefix ("A (X×Y×Z) cm. ...") so all
fingerprints are unique.

Questions added:
  Q33(i,ii) : (2×10×12) cm, 2cm cuts -> 1×5×6 slab
  Q36(i,ii) : (3×12×15) cm, 3cm cuts -> 1×4×5 slab (total + 4-face)
  Q37(i,ii) : (3×12×15) cm, 3cm cuts -> 1×4×5 slab (3-face + 2-face)

Subject : Reasoning
Topic   : Cube & Cuboid
Run     : python seed_reasoning_cube_cuboid_sheet5.py

Answer key verification:
  Q33i:  1×5×6; 3-face = 2(5-2)+2(6-2)=14                                       -> D
  Q33ii: 1×5×6; 2-face = (5-2)(6-2)=12                                           -> A
  Q36i:  1×4×5; total  = 1×4×5=20                                                -> D
  Q36ii: 1×4×5; 4-face = 4 corners                                               -> B
  Q37i:  1×4×5; 3-face = 2(4-2)+2(5-2)=10                                        -> A
  Q37ii: 1×4×5; 2-face = (4-2)(5-2)=6                                            -> C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Cube_Cuboid_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"

# 62-char prefix keeps sub-question number within the 80-char dedup window
_D33 = "A (2×10×12) cm. colored cuboid is cut into 2cm smaller cubes. "
_D33_HI = (
    "एक (2×10×12) सेमी. के रंगे हुए घनाभ को 2 सेमी. के छोटे घनों में "
    "काटा जाता है। "
)

_D36 = "A (3×12×15) cm. colored cuboid is cut into 3cm smaller cubes. "
_D36_HI = (
    "एक (3×12×15) सेमी. के रंगे हुए घनाभ को 3 सेमी. के छोटे घनों में "
    "काटा जाता है। "
)

QUESTIONS = [
    # ── Q33 (i)  3-face ──────────────────────────────────────────────────────
    {
        "question_number": 33,
        "difficulty": "medium",
        "question_en": _D33 + "How many have 3 painted surfaces?",
        "question_hi": _D33_HI + "3 सतह रंगे घनों की संख्या बताइए?",
        "option_a": "12",
        "option_b": "20",
        "option_c": "10",
        "option_d": "14",
        "correct_answer": "D",
    },
    # ── Q33 (ii) 2-face ──────────────────────────────────────────────────────
    {
        "question_number": 33,
        "difficulty": "medium",
        "question_en": _D33 + "How many have 2 painted surfaces?",
        "question_hi": _D33_HI + "2 सतह रंगे घनों की संख्या बताइए?",
        "option_a": "12",
        "option_b": "14",
        "option_c": "16",
        "option_d": "10",
        "correct_answer": "A",
    },
    # ── Q36 (i)  total ───────────────────────────────────────────────────────
    {
        "question_number": 36,
        "difficulty": "easy",
        "question_en": _D36 + "What is the total number of smaller cubes?",
        "question_hi": _D36_HI + "कुल कितने छोटे-छोटे घन बनेंगे?",
        "option_a": "28",
        "option_b": "26",
        "option_c": "30",
        "option_d": "20",
        "correct_answer": "D",
    },
    # ── Q36 (ii) 4-face ──────────────────────────────────────────────────────
    {
        "question_number": 36,
        "difficulty": "hard",
        "question_en": _D36 + "How many have 4 painted surfaces?",
        "question_hi": _D36_HI + "4 सतह रंगे घनों की संख्या बताइए?",
        "option_a": "10",
        "option_b": "4",
        "option_c": "8",
        "option_d": "6",
        "correct_answer": "B",
    },
    # ── Q37 (i)  3-face ──────────────────────────────────────────────────────
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": _D36 + "How many have 3 painted surfaces?",
        "question_hi": _D36_HI + "3 सतह रंगे घनों की संख्या बताइए?",
        "option_a": "10",
        "option_b": "20",
        "option_c": "16",
        "option_d": "12",
        "correct_answer": "A",
    },
    # ── Q37 (ii) 2-face ──────────────────────────────────────────────────────
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": _D36 + "How many have 2 painted surfaces?",
        "question_hi": _D36_HI + "2 सतह रंगे घनों की संख्या बताइए?",
        "option_a": "12",
        "option_b": "8",
        "option_c": "6",
        "option_d": "10",
        "correct_answer": "C",
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        existing_short = {
            row[0][:80]
            for row in db.query(Question.question_en)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        for d in QUESTIONS:
            fp = d["question_en"][:80]
            if fp in existing_short:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue

            db.add(Question(
                subject    = SUBJECT,
                topic      = TOPIC,
                source_pdf = SOURCE,
                **d,
            ))
            inserted += 1

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
