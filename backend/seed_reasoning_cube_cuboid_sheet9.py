"""
seed_reasoning_cube_cuboid_sheet9.py
=====================================
Seeds Reasoning → Cube & Cuboid  book Q4–Q7 (Piyush Varshney source).
Stored as question_numbers 55–58 (52–54 already taken by book Q1–Q3).

Book Q4 & Q5 share this preamble:
  "A solid cube's two adjacent sides → Red, opposites → Black, rest → Green.
   Cut into 64 small cubes (4×4×4)."

Book Q6 & Q7 share this preamble:
  "A cube of 8×8×8 cm coloured on OPPOSITE surfaces: Red, Green, Yellow.
   Cut into 2 cm small cubes → 4×4×4 = 64 cubes."

Answer key
──────────────────────────────────────────────────────────────────────
Q55 (book Q4)  A (8)   — no side coloured = interior = (4−2)³ = 8
Q56 (book Q5)  C (28)  — at least 1 red = front(16)+right(16)−shared_edge(4) = 28
Q57 (book Q6)  D (8)   — 3 surfaces coloured = corner cubes = 8
Q58 (book Q7)  A (32)  — at least 1 green (2 opposite green faces) = 16+16 = 32
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"
SOURCE  = "Piyush_Varshney_Cube_Cuboid"

# ── Shared preambles ─────────────────────────────────────────────────────────
PRE_RBG = (
    "A solid cube's two adjacent sides are coloured Red, the sides directly "
    "opposite are coloured Black, and the remaining two sides are coloured "
    "Green. It is then cut into 64 equal small cubes (4×4×4). "
)
PRE_RBG_HI = (
    "एक ठोस घन की दो समीपवर्ती भुजाएँ लाल रंग से, उनके ठीक विपरीत काले रंग "
    "से और शेष दो भुजाएँ हरे रंग से रंगी होती हैं। इसे 64 छोटे समान घनों "
    "(4×4×4) में काटा जाता है। "
)

PRE_OPP = (
    "A cube of 8×8×8 cm. side is coloured on opposite surfaces with Red, "
    "Green and Yellow. After that it is cut into 2 cm small cubes "
    "(giving a 4×4×4 = 64 cube grid). "
)
PRE_OPP_HI = (
    "एक 8×8×8 सेमी का घन है जिसकी विपरीत सतहें लाल, हरे और पीले रंग से "
    "रंगी हैं। उसके बाद घन को 2 सेमी छोटे घनों में काट दिया जाता है "
    "(4×4×4 = 64 छोटे घन)। "
)

QUESTIONS = [

    # ── Q55 (book Q4) ───────────────────────────────────────────────────────
    # Preamble: 2 adj Red + 2 opp Black + 2 Green → 64 cubes.
    # No side coloured = interior cubes = (n−2)³ = (4−2)³ = 8.
    {
        "question_number": 55,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_RBG}"
            "How many cubes are there of which no side is coloured?"
        ),
        "question_hi": (
            f"{PRE_RBG_HI}"
            "ऐसे कितने घन हैं जिनकी कोई सतह रंगी नहीं हैं?"
        ),
        "image_url": None,
        "option_a": "8",
        "option_b": "16",
        "option_c": "0",
        "option_d": "4",
        "correct_answer": "A",   # 8 interior cubes
    },

    # ── Q56 (book Q5) ───────────────────────────────────────────────────────
    # Same preamble.
    # At least 1 red face: Red is on 2 ADJACENT faces (say front & right).
    # Cubes with ≥1 red = |front layer| + |right layer| − |shared edge|
    #                    = 16 + 16 − 4 = 28.
    {
        "question_number": 56,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_RBG}"
            "How many cubes are there of which at least one side is coloured "
            "with red colour?"
        ),
        "question_hi": (
            f"{PRE_RBG_HI}"
            "ऐसे कितने घन हैं जिनकी कम से कम एक सतह लाल रंग से रंगी हैं?"
        ),
        "image_url": None,
        "option_a": "4",
        "option_b": "16",
        "option_c": "28",
        "option_d": "32",
        "correct_answer": "C",   # 28 cubes (inclusion-exclusion: 16+16−4)
    },

    # ── Q57 (book Q6) ───────────────────────────────────────────────────────
    # Preamble: 8×8×8 cube, opposite faces Red/Green/Yellow, cut into 2 cm
    # → 4×4×4 = 64 small cubes.
    # 3 surfaces coloured = corner cubes (touch one face from each colour pair).
    # Corner cubes = 8.
    {
        "question_number": 57,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_OPP}"
            "The number of small cubes which have three surfaces coloured "
            "with red, green and yellow?"
        ),
        "question_hi": (
            f"{PRE_OPP_HI}"
            "छोटे घनों की संख्या जिनमें तीन सतह लाल, हरे और पीले रंग के साथ "
            "रंगी हैं?"
        ),
        "image_url": None,
        "option_a": "32",
        "option_b": "56",
        "option_c": "64",
        "option_d": "8",
        "correct_answer": "D",   # 8 corner cubes
    },

    # ── Q58 (book Q7) ───────────────────────────────────────────────────────
    # Same preamble (8×8×8 → 4×4×4 = 64 cubes, opposite faces Red/Green/Yellow).
    # At least 1 green: Green is on 2 OPPOSITE faces.
    # Cubes with ≥1 green = top_green_layer(16) + bottom_green_layer(16) = 32
    # (no overlap since they are on opposite faces).
    {
        "question_number": 58,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_OPP}"
            "Number of small cubes which have at least one surface green?"
        ),
        "question_hi": (
            f"{PRE_OPP_HI}"
            "छोटे घनों की संख्या जिनमें कम से कम एक सतह हरे रंग की हो?"
        ),
        "image_url": None,
        "option_a": "32",
        "option_b": "56",
        "option_c": "64",
        "option_d": "8",
        "correct_answer": "A",   # 32 cubes (16+16, opposite faces, no overlap)
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
            print(f"  INSERT Q{qn}  (book Q{qn - 51})")
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
