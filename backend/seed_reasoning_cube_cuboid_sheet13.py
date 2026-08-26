"""
seed_reasoning_cube_cuboid_sheet13.py
======================================
Seeds Reasoning → Cube & Cuboid  book Q19–Q21 (Piyush Varshney source).
Stored as question_numbers 70–72.

Answer key
──────────────────────────────────────────────────────────────────────
Q70 (book Q19)  B (Black)  — 6-colour cube; Red opposite Black; Red at bottom
                             ⟹ Black is at the TOP (upper face).
Q71 (book Q20)  C (Blue)   — Same 6-colour setup; 4 side faces: Green, White,
                             Blue, Brown. Blue adj White, Brown adj Blue ⟹
                             side ring: White–Blue–Brown–Green. Opposite pairs:
                             White↔Brown, Blue↔Green ⟹ Green opposite Blue.
Q72 (book Q21)  C (4)      — 4×4×4 = 64 cubes; all 6 faces painted (3 colour
                             pairs: red, black, green). Colourless (interior)
                             cubes = (n−2)³ = (4−2)³ = 8. NOTE: correct
                             mathematical answer is 8 but book options list (c) 4
                             (the book appears to use (n−2)² = 4 erroneously).
                             Answer stored as per the book: C (4).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"
SOURCE  = "Piyush_Varshney_Cube_Cuboid"

# ── Shared preamble for Q70 & Q71 ────────────────────────────────────────────
# 6 different-coloured faces with specific adjacency/opposition clues.
PRE_6COL = (
    "All the six faces of a cube are coloured with six different colours – "
    "black, brown, green, red, white and blue. "
    "Red face is opposite to the black face. "
    "Green face is between red and black faces. "
    "Blue face is adjacent to white face. "
    "Brown face is adjacent to blue face. "
    "Red face is in the bottom. "
)
PRE_6COL_HI = (
    "एक घन के सभी छः सतह छः अलग-अलग रंगों से रंगी हैं – काला, भूरे, हरे, "
    "काले, सफ़ेद और नीले। "
    "लाल सतह काले सतह के विपरीत है। "
    "हरी सतह लाल और काले सतह के बीच है। "
    "नीली सतह सफ़ेद सतह से सटी होती है। "
    "भूरी सतह नीले सतह से सटी होती है। "
    "लाल सतह काले सबसे नीचे है। "
)

QUESTIONS = [

    # ── Q70 (book Q19) ──────────────────────────────────────────────────────
    # Logic:
    #   Red = bottom  →  Black (opposite Red) = top (upper face).
    #   Green is a side face (between bottom-Red and top-Black).
    #   Remaining side faces: White, Blue, Brown (all lateral).
    # Answer: upper face = Black.
    {
        "question_number": 70,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_6COL}"
            "The upper face is ____?"
        ),
        "question_hi": (
            f"{PRE_6COL_HI}"
            "ऊपरी सतह ___ है?"
        ),
        "image_url": None,
        "option_a": "White/ सफ़ेद",
        "option_b": "Black/ काला",
        "option_c": "Brown/ भूरा",
        "option_d": "None of these/ इनमें से कोई नहीं",
        "correct_answer": "B",   # Black is at the top (opposite Red which is at bottom)
    },

    # ── Q71 (book Q20) ──────────────────────────────────────────────────────
    # Logic:
    #   Red = bottom, Black = top (from Q19 analysis).
    #   4 side faces: Green, White, Blue, Brown.
    #   Blue adj White AND Brown adj Blue ⟹ side ring: White–Blue–Brown–Green.
    #   Opposite pairs among side faces: White↔Brown and Blue↔Green.
    # Answer: face opposite to Green = Blue.
    {
        "question_number": 71,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_6COL}"
            "Which face is opposite to green?"
        ),
        "question_hi": (
            f"{PRE_6COL_HI}"
            "कौन सी सतह हरे रंग के विपरीत है?"
        ),
        "image_url": None,
        "option_a": "Red/ लाल",
        "option_b": "White/ सफ़ेद",
        "option_c": "Blue/ नीला",
        "option_d": "Brown/ भूरा",
        "correct_answer": "C",   # Blue (side-face ring: W–Blue–Brown–Green → Blue opp Green)
    },

    # ── Q72 (book Q21) ──────────────────────────────────────────────────────
    # A big cube; all OPPOSITE face pairs coloured: red pair, black pair, green pair.
    # All 6 faces painted. Cut into 64 = 4×4×4 small cubes.
    # Colourless (0 painted faces) = interior cubes.
    # Mathematically: (n−2)³ = (4−2)³ = 2³ = 8.
    # Book lists (c) 4 — likely a printing error using (n−2)² = 4.
    # Answer stored as per book: C (4).
    {
        "question_number": 72,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            "All the opposite faces of a big cube are coloured with red, black "
            "and green colours. After that it is cut into 64 small equal cubes. "
            "How many small cubes are there whose no faces are coloured?"
        ),
        "question_hi": (
            "एक बड़े घन के सभी विपरीत सतह लाल, काले और हरे रंगों से रंगी हैं। "
            "उसके बाद इसे 64 छोटे बराबर घनों में काटा जाता है। "
            "कितने छोटे-छोटे घन हैं जिनकी कोई सतह रंगी हुई नहीं है?"
        ),
        "image_url": None,
        "option_a": "10",
        "option_b": "40",
        "option_c": "4",
        "option_d": "18",
        "correct_answer": "C",   # Book answer: 4 (mathematical answer is 8 = (4−2)³)
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
