"""
seed_reasoning_cube_cuboid_sheet8.py
=====================================
Seeds Reasoning → Cube & Cuboid  Q1–Q3 (Piyush Varshney source).

NOTE: question_numbers 1,2,3 are already in the DB (Gagan Pratap set).
      These Piyush Varshney questions are stored as 52, 53, 54.

All three are about a cube cut into 64 smaller equal cubes (4×4×4).

Answer key
──────────────────────────────────────────────────────────────────────
Q52  A (8)   — No face coloured = interior cubes = (4−2)³ = 8
Q53  C (0)   — 4 red faces impossible; max coloured faces per small cube = 3
Q54  B (48)  — 1 or 2 faces coloured = edge(24) + face(24) = 48
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"
SOURCE  = "Piyush_Varshney_Cube_Cuboid"

# Shared preamble (Q52 & Q53 have the same setup)
PREAMBLE_64 = (
    "A cube is coloured red on all faces. It is cut into 64 smaller cubes of "
    "equal size."
)
PREAMBLE_64_HI = (
    "एक घन की सभी सतह लाल रंग से रंगी हुई है। इसे समान आकार के 64 छोटे "
    "घनों में काटा जाता है।"
)

QUESTIONS = [

    # ── Q52 (book Q1) ───────────────────────────────────────────────────────
    # 4×4×4 = 64 cubes. All 6 faces painted red.
    # No face coloured = interior cubes = (n−2)³ = (4−2)³ = 2³ = 8.
    {
        "question_number": 52,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PREAMBLE_64} "
            "How many cubes have no face coloured?"
        ),
        "question_hi": (
            f"{PREAMBLE_64_HI} "
            "कितने घनों की कोई सतह रंगी नहीं होगी?"
        ),
        "image_url": None,
        "option_a": "8",
        "option_b": "0",
        "option_c": "24",
        "option_d": "16",
        "correct_answer": "A",   # 8 cubes (interior)
    },

    # ── Q53 (book Q2) ───────────────────────────────────────────────────────
    # Same 4×4×4 cube. How many cubes have four red faces?
    # In any n×n×n cut, a small cube can have at most 3 faces coloured
    # (corner cubes). No cube can have 4 coloured faces. Answer = 0.
    {
        "question_number": 53,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PREAMBLE_64} "
            "How many cubes have four red faces?"
        ),
        "question_hi": (
            f"{PREAMBLE_64_HI} "
            "कितने घन हैं जिनकी चार सतह लाल रंग से रंगी हुई है?"
        ),
        "image_url": None,
        "option_a": "16",
        "option_b": "24",
        "option_c": "0",
        "option_d": "8",
        "correct_answer": "C",   # 0 cubes (impossible — max 3 coloured faces)
    },

    # ── Q54 (book Q3) ───────────────────────────────────────────────────────
    # A solid cube: 2 adjacent faces = Red, opposite 2 faces = Black,
    # remaining 2 faces = Green. Cut into 64 smaller cubes (4×4×4).
    # Cubes with 1 OR 2 faces coloured (but NOT 3):
    #   Edge cubes (2 faces): 12 edges × (4−2) = 12×2 = 24
    #   Face cubes (1 face) : 6 faces × (4−2)² = 6×4  = 24
    #   Total = 24 + 24 = 48.
    {
        "question_number": 54,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "A solid cube's two adjacent sides are coloured Red, the sides "
            "directly opposite to these are coloured Black, and the remaining "
            "two sides are coloured Green. It is then cut into 64 equal small "
            "cubes. How many such cubes are there of which one or two sides are "
            "coloured but not three sides?"
        ),
        "question_hi": (
            "एक ठोस घन की दो समीपवर्ती भुजाएँ लाल रंग से रंगी होती हैं और "
            "उनके ठीक विपरीत काले रंग से रंगी होती है तथा शेष भुजाएँ हरे रंग "
            "से रंगी होती हैं। इसे बाद में 64 छोटे घनों में बदला जाता है। ऐसे "
            "कितने घन हैं जिनकी एक या दो सतह रंगी हैं लेकिन तीन सतह रंगी नहीं हैं?"
        ),
        "image_url": None,
        "option_a": "3",
        "option_b": "48",
        "option_c": "8",
        "option_d": "24",
        "correct_answer": "B",   # 48 cubes (24 edge + 24 face)
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        existing_qnums = {
            row[0]
            for row in db.query(Question.question_number)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }
        for d in QUESTIONS:
            qn = d["question_number"]
            if qn in existing_qnums:
                print(f"  SKIP  Q{qn}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
            inserted += 1
            print(f"  INSERT Q{qn}")
        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped: {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
