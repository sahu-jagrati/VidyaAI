"""
seed_reasoning_cube_cuboid_sheet3.py
=====================================
Seeds Cuboid cutting questions from Gagan Pratap Reasoning PDFs - Sheet 3.
Subject : Reasoning
Topic   : Cube & Cuboid
Run     : python seed_reasoning_cube_cuboid_sheet3.py

Answer key verification:
  Q25:  (10×12×14) ÷ 2cm  -> 5×6×7 = 210                                        -> A
  Q26:  (15×18×21) ÷ 3cm  -> interior = 3×4×5 = 60                               -> C
  Q27i: (8×10×12) ÷ 2cm   -> 4×5×6 = 120 total                                   -> A
  Q27ii:(8×10×12) ÷ 2cm   -> 3 faces = 8 corners                                  -> C
  Q28i: (8×10×12) ÷ 2cm   -> 2 faces = 4(2)+4(3)+4(4) = 36                       -> B
  Q28ii:(8×10×12) ÷ 2cm   -> 1 face  = 2(2)(3)+2(3)(4)+2(2)(4) = 52             -> D
  Q28iii:(8×10×12)÷ 2cm   -> 0 faces = 2×3×4 = 24                                -> A
  Q29i: (3×12×15) ÷ 3cm   -> 1×4×5 = 20 total                                    -> C
  Q29ii:(3×12×15) ÷ 3cm   -> 4 faces = 4 corners of thin slab                    -> C
  Q30i: (3×12×15) ÷ 3cm   -> 2 faces = (4-2)(5-2) = 6 (interior slab cubes)      -> C
  Q30ii:(3×12×15) ÷ 3cm   -> 3 faces = 2(5-2)+2(4-2) = 10                        -> A
  Q31i: (3×12×15) ÷ 3cm   -> 1 face  = 0 (all cubes have ≥2 in 1-thick slab)     -> C
  Q31ii:(3×12×15) ÷ 3cm   -> 0 faces = 0                                          -> A
  Q32i: (2×10×12) ÷ 2cm   -> 1×5×6 = 30 total                                    -> B
  Q32ii:(2×10×12) ÷ 2cm   -> 4 faces = 4 corners of thin slab                    -> A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Cube_Cuboid_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"

_D27 = (
    "One (8×10×12) cm. colored cuboid is cut into smaller cubes of 2cm side. "
)
_D27_HI = (
    "एक (8×10×12) सेमी. के रंगे हुए घनाभ को 2 सेमी. के छोटे-छोटे घनों में "
    "काटा जाता है। "
)

_D29 = (
    "One (3×12×15) cm. colored cuboid is cut into smaller cubes of 3cm side. "
)
_D29_HI = (
    "एक (3×12×15) सेमी. के रंगे हुए घनाभ को 3 सेमी. के छोटे-छोटे घनों में "
    "काटा जाता है। "
)

_D32 = (
    "One (2×10×12) cm. colored cuboid is cut into smaller cubes of 2cm side. "
)
_D32_HI = (
    "एक (2×10×12) सेमी. के रंगे हुए घनाभ को 2 सेमी. के छोटे-छोटे घनों में "
    "काटा जाता है। "
)

QUESTIONS = [
    # ── Q25 ──────────────────────────────────────────────────────────────────
    {
        "question_number": 25,
        "difficulty": "easy",
        "question_en": (
            "One (10×12×14) cm. cuboid is painted red on all its surfaces. Now it "
            "is cut into smaller cubes of 2cm side, then what is the total number "
            "of cubes made?"
        ),
        "question_hi": (
            "एक (10×12×14) सेमी. घनाभ को लाल रंग से रंगा गया है। इसे 2 सेमी. के "
            "बराबर आकार के छोटे घनों में काटा जाता है तब बनने वाले कुल घनों की "
            "संख्या क्या होगी?"
        ),
        "option_a": "210",
        "option_b": "216",
        "option_c": "208",
        "option_d": "200",
        "correct_answer": "A",
    },
    # ── Q26 ──────────────────────────────────────────────────────────────────
    {
        "question_number": 26,
        "difficulty": "medium",
        "question_en": (
            "One (15×18×21) cm. cuboid is painted red on all its surfaces. Now it "
            "is cut into smaller cubes of 3cm side, then how many cubes are there "
            "which have no surface painted?"
        ),
        "question_hi": (
            "एक (15×18×21) सेमी. के रंगे हुए घनाभ को 3 सेमी. के बराबर आकार के "
            "छोटे घनों में काटा जाता है। ऐसे कितने घन होंगे जिनकी कोई भी सतह "
            "रंगी न हो?"
        ),
        "option_a": "120",
        "option_b": "210",
        "option_c": "60",
        "option_d": "30",
        "correct_answer": "C",
    },
    # ── Q27 (i) ──────────────────────────────────────────────────────────────
    {
        "question_number": 27,
        "difficulty": "easy",
        "question_en": (
            _D27 +
            "What is the number of total cubes made?"
        ),
        "question_hi": (
            _D27_HI +
            "बनने वाले कुल छोटे-छोटे घन की संख्या बताइए?"
        ),
        "option_a": "120",
        "option_b": "100",
        "option_c": "110",
        "option_d": "140",
        "correct_answer": "A",
    },
    # ── Q27 (ii) ─────────────────────────────────────────────────────────────
    {
        "question_number": 27,
        "difficulty": "easy",
        "question_en": (
            _D27 +
            "How many cubes have 3 surfaces painted?"
        ),
        "question_hi": (
            _D27_HI +
            "3 सतह रंगे घनों की संख्या बताइए?"
        ),
        "option_a": "6",
        "option_b": "10",
        "option_c": "8",
        "option_d": "5",
        "correct_answer": "C",
    },
    # ── Q28 (i) ──────────────────────────────────────────────────────────────
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": (
            _D27 +
            "How many cubes have 2 surfaces painted?"
        ),
        "question_hi": (
            _D27_HI +
            "2 सतह रंगे घनों की संख्या बताइए?"
        ),
        "option_a": "20",
        "option_b": "36",
        "option_c": "40",
        "option_d": "50",
        "correct_answer": "B",
    },
    # ── Q28 (ii) ─────────────────────────────────────────────────────────────
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": (
            _D27 +
            "How many cubes have 1 surface painted?"
        ),
        "question_hi": (
            _D27_HI +
            "1 सतह रंगे घनों की संख्या बताइए?"
        ),
        "option_a": "24",
        "option_b": "48",
        "option_c": "50",
        "option_d": "52",
        "correct_answer": "D",
    },
    # ── Q28 (iii) ────────────────────────────────────────────────────────────
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": (
            _D27 +
            "What is the number of colorless cubes?"
        ),
        "question_hi": (
            _D27_HI +
            "रंगहीन घनों की संख्या बताइए?"
        ),
        "option_a": "24",
        "option_b": "20",
        "option_c": "30",
        "option_d": "18",
        "correct_answer": "A",
    },
    # ── Q29 (i) ──────────────────────────────────────────────────────────────
    {
        "question_number": 29,
        "difficulty": "easy",
        "question_en": (
            _D29 +
            "What is the number of total cubes made?"
        ),
        "question_hi": (
            _D29_HI +
            "कुल कितने छोटे-छोटे घन बनेंगे?"
        ),
        "option_a": "40",
        "option_b": "30",
        "option_c": "20",
        "option_d": "32",
        "correct_answer": "C",
    },
    # ── Q29 (ii) ─────────────────────────────────────────────────────────────
    {
        "question_number": 29,
        "difficulty": "hard",
        "question_en": (
            _D29 +
            "How many cubes have 4 surfaces painted?"
        ),
        "question_hi": (
            _D29_HI +
            "कुल कितने छोटे-छोटे घन बनेंगे, जिनकी केवल 4 सतह रंगी हुई हैं?"
        ),
        "option_a": "10",
        "option_b": "8",
        "option_c": "4",
        "option_d": "6",
        "correct_answer": "C",
    },
    # ── Q30 (i) ──────────────────────────────────────────────────────────────
    {
        "question_number": 30,
        "difficulty": "medium",
        "question_en": (
            _D29 +
            "How many cubes have 2 surfaces painted?"
        ),
        "question_hi": (
            _D29_HI +
            "2 सतह रंगे घनों की संख्या बताइए?"
        ),
        "option_a": "20",
        "option_b": "4",
        "option_c": "6",
        "option_d": "18",
        "correct_answer": "C",
    },
    # ── Q30 (ii) ─────────────────────────────────────────────────────────────
    {
        "question_number": 30,
        "difficulty": "medium",
        "question_en": (
            _D29 +
            "How many cubes have 3 surfaces painted?"
        ),
        "question_hi": (
            _D29_HI +
            "3 सतह रंगे घनों की संख्या बताइए?"
        ),
        "option_a": "10",
        "option_b": "12",
        "option_c": "18",
        "option_d": "14",
        "correct_answer": "A",
    },
    # ── Q31 (i) ──────────────────────────────────────────────────────────────
    {
        "question_number": 31,
        "difficulty": "medium",
        "question_en": (
            _D29 +
            "How many cubes have 1 surface painted?"
        ),
        "question_hi": (
            _D29_HI +
            "1 सतह रंगे घनों की संख्या बताइए?"
        ),
        "option_a": "4",
        "option_b": "6",
        "option_c": "0",
        "option_d": "10",
        "correct_answer": "C",
    },
    # ── Q31 (ii) ─────────────────────────────────────────────────────────────
    {
        "question_number": 31,
        "difficulty": "medium",
        "question_en": (
            _D29 +
            "What is the number of colorless cubes?"
        ),
        "question_hi": (
            _D29_HI +
            "0 सतह रंगे घनों की संख्या बताइए?"
        ),
        "option_a": "0",
        "option_b": "2",
        "option_c": "4",
        "option_d": "6",
        "correct_answer": "A",
    },
    # ── Q32 (i) ──────────────────────────────────────────────────────────────
    {
        "question_number": 32,
        "difficulty": "easy",
        "question_en": (
            _D32 +
            "What is the number of total cubes made?"
        ),
        "question_hi": (
            _D32_HI +
            "कुल कितने छोटे-छोटे घन बनेंगे?"
        ),
        "option_a": "16",
        "option_b": "30",
        "option_c": "18",
        "option_d": "20",
        "correct_answer": "B",
    },
    # ── Q32 (ii) ─────────────────────────────────────────────────────────────
    {
        "question_number": 32,
        "difficulty": "hard",
        "question_en": (
            _D32 +
            "How many cubes have 4 surfaces painted?"
        ),
        "question_hi": (
            _D32_HI +
            "4 सतह रंगे घनों की संख्या बताइए?"
        ),
        "option_a": "4",
        "option_b": "8",
        "option_c": "10",
        "option_d": "2",
        "correct_answer": "A",
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
