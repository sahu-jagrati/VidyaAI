"""
seed_reasoning_cube_cuboid_sheet14.py
======================================
Seeds Reasoning → Cube & Cuboid  book Q22–Q25 (Piyush Varshney source).
Stored as question_numbers 73–76.

Answer key
──────────────────────────────────────────────────────────────────────
Q73 (book Q22)  B (8)   — 4×4×4=64 cube; all 6 faces painted (red/black/green
                          opposite pairs). Three faces coloured = corner cubes = 8.
Q74 (book Q23)  B (56)  — Same cube. At most 2 faces coloured = 64 − 8 = 56.
Q75 (book Q24)  B (8)   — Cuboid 4×3×5 cm; Red=5×4 faces, Blue=4×3 faces,
                          Green=5×3 faces; cut into 1cm cubes (60 total).
                          Three faces coloured = corner cubes = 8 (always).
Q76 (book Q25)  A (12)  — Same cuboid. Red-AND-Green only (no Blue) cubes:
                          edges at red-green intersections excluding corners
                          (which also touch blue). 4 edges × (5−2)=3 = 12.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"
SOURCE  = "Piyush_Varshney_Cube_Cuboid"

# ── Shared preamble for Q73 & Q74 ─────────────────────────────────────────────
# 4×4×4=64 cubes; all 6 faces painted with 3 colour pairs.
PRE_4_3COL = (
    "All the opposite faces of a big cube are coloured with red, black and "
    "green colours. After that it is cut into 64 small equal cubes. "
)
PRE_4_3COL_HI = (
    "एक बड़े घन के सभी विपरीत सतह लाल, काले और हरे रंगों से रंगी हैं। "
    "उसके बाद इसे 64 छोटे बराबर घनों में काटा जाता है। "
)

# ── Shared preamble for Q75 & Q76 ─────────────────────────────────────────────
# Cuboid 4cm (L) × 3cm (W) × 5cm (H) → 60 unit cubes.
# Red   = two 5×4 faces (front & back, the L×H faces)
# Blue  = two 4×3 faces (top & bottom, the L×W faces)
# Green = two 5×3 faces (left & right, the W×H faces)
PRE_CUBOID = (
    "A cuboid shaped wooden block has 4 cm length, 3 cm breadth and 5 cm height. "
    "Two faces measuring 5 cm × 4 cm are coloured in red. "
    "Two faces measuring 4 cm × 3 cm are coloured in blue. "
    "Two faces measuring 5 cm × 3 cm are coloured in green. "
    "Now the block is divided into small cubes of side 1 cm each. "
)
PRE_CUBOID_HI = (
    "एक घना आकार की लकड़ी के ब्लॉक की 4 सेमी लंबाई, 3 सेमी चौड़ाई और "
    "5 सेमी ऊँचाई होती है। "
    "5 सेमी ×4 सेमी मापने वाले दो सतह लाल रंग के होते हैं। "
    "4 सेमी ×3 सेमी मापने वाले दो सतह नीले रंग के होते हैं। "
    "5 सेमी ×3 सेमी मापने वाले दो सतह हरे रंग के होते हैं। "
    "अब ब्लॉक को 1 सेमी भुजा के छोटे घनों में काट दिया जाता है। "
)

QUESTIONS = [

    # ── Q73 (book Q22) ──────────────────────────────────────────────────────
    # 4×4×4 = 64 cubes; all 6 faces painted.
    # 3 faces coloured = corner cubes = 8 (constant for any n×n×n cube).
    {
        "question_number": 73,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_4_3COL}"
            "How many small cubes are there whose 3 faces are coloured?"
        ),
        "question_hi": (
            f"{PRE_4_3COL_HI}"
            "ऐसे कितने छोटे घन हैं जिनकी 3 सतह रंगीन हैं?"
        ),
        "image_url": None,
        "option_a": "14",
        "option_b": "8",
        "option_c": "16",
        "option_d": "24",
        "correct_answer": "B",   # 8 corner cubes (always 8 for any cube size)
    },

    # ── Q74 (book Q23) ──────────────────────────────────────────────────────
    # Same cube. At most 2 faces coloured = total − 3-face cubes = 64 − 8 = 56.
    {
        "question_number": 74,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_4_3COL}"
            "How many small cubes are there whose at most two faces are coloured?"
        ),
        "question_hi": (
            f"{PRE_4_3COL_HI}"
            "ऐसे कितने छोटे घन हैं जिनकी अधिक से अधिक दो सतह रंगीन हैं?"
        ),
        "image_url": None,
        "option_a": "48",
        "option_b": "56",
        "option_c": "28",
        "option_d": "24",
        "correct_answer": "B",   # 56 = 64 − 8 (corner cubes)
    },

    # ── Q75 (book Q24) ──────────────────────────────────────────────────────
    # Cuboid 4×3×5 = 60 unit cubes.
    # Three faces coloured = corner cubes = 8 (always 8 for any cuboid).
    {
        "question_number": 75,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_CUBOID}"
            "How many small cubes will have three faces coloured?"
        ),
        "question_hi": (
            f"{PRE_CUBOID_HI}"
            "कितने छोटे घनों में तीन सतह रंगीन हैं?"
        ),
        "image_url": None,
        "option_a": "14",
        "option_b": "8",
        "option_c": "10",
        "option_d": "12",
        "correct_answer": "B",   # 8 corner cubes (constant for any cuboid)
    },

    # ── Q76 (book Q25) ──────────────────────────────────────────────────────
    # Same cuboid 4(L)×3(W)×5(H).
    # Red   = front(y=1) + back(y=3)  [the 5×4 = L×H faces]
    # Blue  = top(z=5)  + bottom(z=1) [the 4×3 = L×W faces]
    # Green = left(x=1) + right(x=4)  [the 5×3 = W×H faces]
    #
    # "Only two faces coloured with red and green" =
    # edge cubes at red-green intersecting edges, NOT touching a blue face:
    #   Edges along the height axis (z) where a red face meets a green face:
    #     front-left  (y=1,x=1): z∈{2,3,4} → 3 cubes
    #     front-right (y=1,x=4): z∈{2,3,4} → 3 cubes
    #     back-left   (y=3,x=1): z∈{2,3,4} → 3 cubes
    #     back-right  (y=3,x=4): z∈{2,3,4} → 3 cubes
    #   Total = 4 × 3 = 12 cubes.
    {
        "question_number": 76,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_CUBOID}"
            "How many small cubes will have only two faces coloured with red "
            "and green colours?"
        ),
        "question_hi": (
            f"{PRE_CUBOID_HI}"
            "कितने छोटे घनों में केवल दो सतह लाल और हरे रंग से रंगी होंगी?"
        ),
        "image_url": None,
        "option_a": "12",
        "option_b": "8",
        "option_c": "16",
        "option_d": "20",
        "correct_answer": "A",   # 12 = 4 red-green edges × (5−2)=3 non-corner cubes
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
