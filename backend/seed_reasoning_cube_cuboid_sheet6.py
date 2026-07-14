"""
seed_reasoning_cube_cuboid_sheet6.py
=====================================
Seeds questions Q44-Q51 (colored cuboid, multi-face painting).
Subject : Reasoning
Topic   : Cube & Cuboid
Run     : python seed_reasoning_cube_cuboid_sheet6.py

Setup A: (6×8×10) cm cuboid cut into 2cm cubes → 3×4×5
  Red   = (6×8) cm faces  (perpendicular to 10cm axis, a=3, b=4 face)
  Blue  = (8×10) cm faces (perpendicular to 6cm axis,  b=4, c=5 face)
  Yellow= (6×10) cm faces (perpendicular to 8cm axis,  a=3, c=5 face)

Answer key verification:
  Q44: 3 diff colors = 8 corners                                                  -> A
  Q45: 2 faces red+blue   = 4 edges × (b-2)=2 = 8                                -> B
  Q46: 2 faces blue+yellow= 4 edges × (c-2)=3 = 12                               -> A
  Q47: 1 face red         = (a-2)(b-2)×2 = 1×2×2 = 4                             -> D
  Q48: 1 face yellow      = (a-2)(c-2)×2 = 1×3×2 = 6                             -> B

Setup B: (8×10×12) cm cuboid cut into 2cm cubes → 4×5×6
  Red   = (8×10)  cm faces
  Blue  = (10×12) cm faces
  Yellow= (8×12)  cm faces

  Q49: corner cubes          = 8                                                   -> C
  Q50: inner central cubes   = (a-2)(b-2)(c-2) = 2×3×4 = 24                      -> B
  Q51: total cubes           = 4×5×6 = 120                                        -> D

NOTE: All question_en strings are written question-first so the unique
      sub-question word ("3 different", "red and blue", etc.) falls within
      the 80-char dedup window. Do NOT use the raw book-description as prefix.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Cube_Cuboid_Sheet6"
SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"

# ── Shared setup text (appended after the unique opening) ─────────────────────
_CTX_A = (
    " There is one (6×8×10) cm. cuboid. Its (6×8) cm surfaces are painted red, "
    "(8×10) cm surfaces are painted blue and (6×10) cm surfaces are painted yellow. "
    "Now this cuboid is cut into smaller cubes of 2 cm."
)
_CTX_A_HI = (
    " एक (6×8×10) सेमी. के घनाभ की (6×8) सेमी. वाली सतहों को लाल रंग से, "
    "(8×10) सेमी. वाली सतहों को नीले रंग से और (6×10) सेमी. वाली सतहों को "
    "पीले रंग से रंगा जाता है। अब इस घनाभ को 2 सेमी. के छोटे-छोटे घनों में काटा जाता है।"
)

_CTX_B = (
    " There is one (8×10×12) cm. cuboid. Its (8×10) cm surfaces are painted red, "
    "(10×12) cm surfaces are painted blue and (8×12) cm surfaces are painted yellow. "
    "Now this cuboid is cut into smaller cubes of 2 cm side."
)
_CTX_B_HI = (
    " एक (8×10×12) सेमी. का घनाभ है। इसकी (8×10) सेमी. वाली सतह को लाल रंग से, "
    "(10×12) सेमी. वाली सतह को नीले रंग से और (8×12) सेमी. वाली सतह को "
    "पीले रंग से रंगा जाता है। अब इस घनाभ को 2 सेमी. के छोटे-छोटे घनों में काटा जाता है।"
)

QUESTIONS = [
    # ── Q44 ──────────────────────────────────────────────────────────────────
    {
        "question_number": 44,
        "difficulty": "easy",
        "question_en": (
            "How many cubes have 3 different colors in a (6×8×10) cm. colored "
            "cuboid cut into 2cm cubes?" + _CTX_A
        ),
        "question_hi": (
            "ऐसे कितने घन होंगे जो 3 अलग-अलग रंगों से रंगे हों?" + _CTX_A_HI
        ),
        "option_a": "8",
        "option_b": "10",
        "option_c": "6",
        "option_d": "12",
        "correct_answer": "A",
    },
    # ── Q45 ──────────────────────────────────────────────────────────────────
    {
        "question_number": 45,
        "difficulty": "medium",
        "question_en": (
            "How many cubes have 2 surfaces in red and blue in a (6×8×10) cm. "
            "colored cuboid cut into 2cm cubes?" + _CTX_A
        ),
        "question_hi": (
            "ऐसे कितने घन होंगे जिनकी 2 सतह लाल और नीले रंग से रंगी हों?" + _CTX_A_HI
        ),
        "option_a": "10",
        "option_b": "8",
        "option_c": "20",
        "option_d": "15",
        "correct_answer": "B",
    },
    # ── Q46 ──────────────────────────────────────────────────────────────────
    {
        "question_number": 46,
        "difficulty": "medium",
        "question_en": (
            "How many cubes have 2 surfaces in blue and yellow in a (6×8×10) cm. "
            "colored cuboid cut into 2cm cubes?" + _CTX_A
        ),
        "question_hi": (
            "ऐसे कितने घन होंगे जिनकी 2 सतह नीले और पीले रंग से रंगी हों?" + _CTX_A_HI
        ),
        "option_a": "12",
        "option_b": "10",
        "option_c": "14",
        "option_d": "20",
        "correct_answer": "A",
    },
    # ── Q47 ──────────────────────────────────────────────────────────────────
    {
        "question_number": 47,
        "difficulty": "medium",
        "question_en": (
            "How many cubes have 1 surface painted red in a (6×8×10) cm. "
            "colored cuboid cut into 2cm cubes?" + _CTX_A
        ),
        "question_hi": (
            "ऐसे कितने घन होंगे जिनकी 1 सतह लाल रंग से रंगी हो?" + _CTX_A_HI
        ),
        "option_a": "6",
        "option_b": "1",
        "option_c": "2",
        "option_d": "4",
        "correct_answer": "D",
    },
    # ── Q48 ──────────────────────────────────────────────────────────────────
    {
        "question_number": 48,
        "difficulty": "medium",
        "question_en": (
            "How many cubes have 1 surface painted yellow in a (6×8×10) cm. "
            "colored cuboid cut into 2cm cubes?" + _CTX_A
        ),
        "question_hi": (
            "ऐसे कितने घन होंगे जिनकी 1 सतह पीले रंग से रंगी हो?" + _CTX_A_HI
        ),
        "option_a": "8",
        "option_b": "6",
        "option_c": "4",
        "option_d": "10",
        "correct_answer": "B",
    },
    # ── Q49 ──────────────────────────────────────────────────────────────────
    {
        "question_number": 49,
        "difficulty": "easy",
        "question_en": (
            "How many corner cubes are there in a (8×10×12) cm. colored cuboid "
            "cut into 2cm cubes?" + _CTX_B
        ),
        "question_hi": (
            "शीर्ष घनों की संख्या बताइए?" + _CTX_B_HI
        ),
        "option_a": "10",
        "option_b": "6",
        "option_c": "8",
        "option_d": "0",
        "correct_answer": "C",
    },
    # ── Q50 ──────────────────────────────────────────────────────────────────
    {
        "question_number": 50,
        "difficulty": "medium",
        "question_en": (
            "How many inner central colorless cubes are there in a (8×10×12) cm. "
            "colored cuboid cut into 2cm cubes?" + _CTX_B
        ),
        "question_hi": (
            "अन्तः केंद्रीय घनों की संख्या बताइए?" + _CTX_B_HI
        ),
        "option_a": "10",
        "option_b": "24",
        "option_c": "30",
        "option_d": "20",
        "correct_answer": "B",
    },
    # ── Q51 ──────────────────────────────────────────────────────────────────
    {
        "question_number": 51,
        "difficulty": "easy",
        "question_en": (
            "What is the total number of cubes made from a (8×10×12) cm. "
            "colored cuboid cut into 2cm cubes?" + _CTX_B
        ),
        "question_hi": (
            "कुल कितने घन बनेंगे?" + _CTX_B_HI
        ),
        "option_a": "80",
        "option_b": "50",
        "option_c": "100",
        "option_d": "120",
        "correct_answer": "D",
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
