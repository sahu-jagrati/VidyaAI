"""
seed_reasoning_cube_cuboid_sheet4.py
=====================================
Seeds Cuboid cutting questions Q33-Q37 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Cube & Cuboid
Run     : python seed_reasoning_cube_cuboid_sheet4.py

Answer key verification:
  Q33:  (2×10×12) ÷ 2cm -> 1×5×6 slab
        (i)  3-face = 2(5-2)+2(6-2) = 6+8 = 14                                  -> D
        (ii) 2-face = (5-2)(6-2) = 3×4 = 12                                      -> A
  Q34:  (2×6×10) ÷ 2cm  -> 1×3×5 slab
        (i)  total = 1×3×5 = 15                                                   -> B
        (ii) 4-face = 4 corners                                                   -> A
  Q35:  (2×6×10) ÷ 2cm  -> 1×3×5 slab (same setup as Q34)
        (i)  3-face = 2(3-2)+2(5-2) = 2+6 = 8                                   -> C
        (ii) 2-face = (3-2)(5-2) = 1×3 = 3                                       -> D
  Q36:  (3×12×15) ÷ 3cm -> 1×4×5 slab
        (i)  total = 1×4×5 = 20                                                   -> D
        (ii) 4-face = 4 corners                                                   -> B
  Q37:  (3×12×15) ÷ 3cm -> 1×4×5 slab (same setup as Q36)
        (i)  3-face = 2(4-2)+2(5-2) = 4+6 = 10                                  -> A
        (ii) 2-face = (4-2)(5-2) = 2×3 = 6                                       -> C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Cube_Cuboid_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"

_D33 = "One (2×10×12) cm. colored cuboid is cut into smaller cubes of 2cm side. "
_D33_HI = (
    "एक (2×10×12) सेमी. के रंगे हुए घनाभ को 2 सेमी. के छोटे-छोटे घनों में "
    "काटा जाता है। "
)

_D34 = "One (2×6×10) cm. colored cuboid is cut into smaller cubes of 2cm side. "
_D34_HI = (
    "एक (2×6×10) सेमी. के रंगे हुए घनाभ को 2 सेमी. के छोटे-छोटे घनों में "
    "काटा जाता है। "
)

_D36 = "One (3×12×15) cm. colored cuboid is cut into smaller cubes of 3cm side. "
_D36_HI = (
    "एक (3×12×15) सेमी. के रंगे हुए घनाभ को 3 सेमी. के छोटे-छोटे घनों में "
    "काटा जाता है। "
)

QUESTIONS = [
    # ── Q33 (i) ──────────────────────────────────────────────────────────────
    {
        "question_number": 33,
        "difficulty": "medium",
        "question_en": _D33 + "How many cubes have 3 surfaces painted?",
        "question_hi": _D33_HI + "3 सतह रंगे घनों की संख्या बताइए?",
        "option_a": "12",
        "option_b": "20",
        "option_c": "10",
        "option_d": "14",
        "correct_answer": "D",
    },
    # ── Q33 (ii) ─────────────────────────────────────────────────────────────
    {
        "question_number": 33,
        "difficulty": "medium",
        "question_en": _D33 + "How many cubes have 2 surfaces painted?",
        "question_hi": _D33_HI + "2 सतह रंगे घनों की संख्या बताइए?",
        "option_a": "12",
        "option_b": "14",
        "option_c": "16",
        "option_d": "10",
        "correct_answer": "A",
    },
    # ── Q34 (i) ──────────────────────────────────────────────────────────────
    {
        "question_number": 34,
        "difficulty": "easy",
        "question_en": _D34 + "What is the number of total cubes made?",
        "question_hi": _D34_HI + "कुल कितने छोटे-छोटे घन बनेंगे?",
        "option_a": "20",
        "option_b": "15",
        "option_c": "18",
        "option_d": "16",
        "correct_answer": "B",
    },
    # ── Q34 (ii) ─────────────────────────────────────────────────────────────
    {
        "question_number": 34,
        "difficulty": "hard",
        "question_en": _D34 + "How many cubes have 4 surfaces painted?",
        "question_hi": _D34_HI + "4 सतह रंगे घनों की संख्या बताइए?",
        "option_a": "4",
        "option_b": "8",
        "option_c": "10",
        "option_d": "6",
        "correct_answer": "A",
    },
    # ── Q35 (i) ──────────────────────────────────────────────────────────────
    {
        "question_number": 35,
        "difficulty": "medium",
        "question_en": _D34 + "How many cubes have 3 surfaces painted?",
        "question_hi": _D34_HI + "3 सतह रंगे घनों की संख्या बताइए?",
        "option_a": "4",
        "option_b": "10",
        "option_c": "8",
        "option_d": "6",
        "correct_answer": "C",
    },
    # ── Q35 (ii) ─────────────────────────────────────────────────────────────
    {
        "question_number": 35,
        "difficulty": "medium",
        "question_en": _D34 + "How many cubes have 2 surfaces painted?",
        "question_hi": _D34_HI + "2 सतह रंगे घनों की संख्या बताइए?",
        "option_a": "4",
        "option_b": "1",
        "option_c": "2",
        "option_d": "3",
        "correct_answer": "D",
    },
    # ── Q36 (i) ──────────────────────────────────────────────────────────────
    {
        "question_number": 36,
        "difficulty": "easy",
        "question_en": _D36 + "What is the number of total cubes made?",
        "question_hi": _D36_HI + "कुल कितने छोटे-छोटे घन बनेंगे?",
        "option_a": "28",
        "option_b": "26",
        "option_c": "30",
        "option_d": "20",
        "correct_answer": "D",
    },
    # ── Q36 (ii) ─────────────────────────────────────────────────────────────
    {
        "question_number": 36,
        "difficulty": "hard",
        "question_en": _D36 + "How many cubes have 4 surfaces painted?",
        "question_hi": _D36_HI + "4 सतह रंगे घनों की संख्या बताइए?",
        "option_a": "10",
        "option_b": "4",
        "option_c": "8",
        "option_d": "6",
        "correct_answer": "B",
    },
    # ── Q37 (i) ──────────────────────────────────────────────────────────────
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": _D36 + "How many cubes have 3 surfaces painted?",
        "question_hi": _D36_HI + "3 सतह रंगे घनों की संख्या बताइए?",
        "option_a": "10",
        "option_b": "20",
        "option_c": "16",
        "option_d": "12",
        "correct_answer": "A",
    },
    # ── Q37 (ii) ─────────────────────────────────────────────────────────────
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": _D36 + "How many cubes have 2 surfaces painted?",
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
            if d["question_en"][:80] in existing_short:
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
