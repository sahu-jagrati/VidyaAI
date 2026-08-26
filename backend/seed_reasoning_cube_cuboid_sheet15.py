"""
seed_reasoning_cube_cuboid_sheet15.py
======================================
Seeds Reasoning → Cube & Cuboid  book Q26–Q30 (Piyush Varshney source).
Stored as question_numbers 77–81.

Answer key
──────────────────────────────────────────────────────────────────────
Q77 (book Q26)  C (16)  — Cube split into two 4×4×2 slabs (32 cubes each).
                          Piece-1: Red=top+bottom, Green=4 sides.
                          Piece-2: Green=2 adjacent 4×2 faces, Red=rest.
                          Cubes with exactly 1 coloured face:
                           P1: x∈{2,3},y∈{2,3},z∈{1,2} → 8; P2: same → 8. Total=16.
Q78 (book Q27)  D (4)   — Same setup. Cubes with 2 red + 1 green:
                          P1: max 1 red face per cube → 0.
                          P2: (4,1,1),(4,1,2),(1,4,1),(1,4,2) → 4. Total=4.
Q79 (book Q28)  D (None)— Same setup. All cubes touch z=1 or z=2 (red in both
                          pieces) → every cube has ≥1 coloured face → 0 uncoloured.
Q80 (book Q29)  C (16)  — Cuboid 4×3×3; Yellow=4×3 opp. pair, Red=other 4×3 pair,
                          Green=3×3 pair; cut into 1cm cubes.
                          Edge cubes (2 faces): 4×(4-2)+4×(3-2)+4×(3-2)=8+4+4=16.
Q81 (book Q30)  B (2)   — Same cuboid. Interior = (4-2)(3-2)(3-2) = 2×1×1 = 2.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"
SOURCE  = "Piyush_Varshney_Cube_Cuboid"

# ── Shared preamble for Q77–Q79 ───────────────────────────────────────────────
# A cube is cut in half → two 4×4×2 slabs, each cut into 32 unit cubes (64 total).
# Piece-1: Red on two LARGER faces (top+bottom, 4×4), Green on remaining 4 sides.
# Piece-2: Green on two SMALLER ADJACENT faces (two 4×2 adjacent sides),
#           Red on the remaining 4 faces.
PRE_SPLIT = (
    "A cube is cut into two equal parts along a plane parallel to one of its "
    "faces. One piece is then coloured red on the two larger faces and green "
    "on the remaining, while the other is coloured green on two smaller "
    "adjacent faces and red on the remaining. Each is then cut into 32 cubes "
    "of same size and mixed up. "
)
PRE_SPLIT_HI = (
    "एक घन को उसके सतह के समानांतर एक समतल के साथ दो बराबर भागों में काटा "
    "जाता है। फिर एक टुकड़े की दो बड़ी सतह पर लाल और शेष पर हरा रंग किया "
    "जाता है, जबकि दूसरे टुकड़े की दो छोटी सटी सतह पर हरा रंग और शेष पर "
    "लाल रंग किया जाता है। प्रत्येक को फिर एक ही आकार के 32 घनों में काटकर "
    "मिलाया जाता है। "
)

# ── Shared preamble for Q80–Q81 ───────────────────────────────────────────────
# Cuboid 4cm(L) × 3cm(W) × 3cm(H) = 36 unit cubes.
# Yellow: opposite 4×3 faces (top z=3 + bottom z=1)
# Red:    opposite 4×3 faces (front y=1 + back y=3)
# Green:  opposite 3×3 faces (left x=1 + right x=4)
PRE_443 = (
    "There is a cuboid whose dimensions are 4×3×3 cm. "
    "The opposite faces of dimensions 4×3 are coloured yellow. "
    "The opposite faces of other dimensions 4×3 are coloured red. "
    "The opposite faces of dimensions 3×3 are coloured green. "
    "Now the cuboid is cut into small cubes of side 1 cm. "
)
PRE_443_HI = (
    "एक घनाभ है जिसका परिमाण 4 × 3 × 3 सेमी है। "
    "परिमाण 4 × 3 के विपरीत चेहरे पीले रंग के होते हैं। "
    "अन्य परिमाण 4 × 3 के विपरीत चेहरे लाल रंग के होते हैं। "
    "परिमाण 3 × 3 के विपरीत चेहरे हरे रंग के होते हैं। "
    "अब घनाभ को 1 सेमी भुजा के छोटे घनों में काट दिया जाता है। "
)

QUESTIONS = [

    # ── Q77 (book Q26) ──────────────────────────────────────────────────────
    # Piece-1 (Red top+bottom, Green all sides):
    #   Exactly 1 coloured face = x∈{2,3}, y∈{2,3}, z∈{1,2} → 2×2×2 = 8 cubes.
    # Piece-2 (Green 2 adjacent sides e.g. x=1+y=1, Red rest):
    #   All cubes touch z=1 or z=2 (red). Exactly 1 face: x∈{2,3}, y∈{2,3} → 8 cubes.
    # Total = 8 + 8 = 16.
    {
        "question_number": 77,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_SPLIT}"
            "How many cubes have only one coloured face each?"
        ),
        "question_hi": (
            f"{PRE_SPLIT_HI}"
            "किनते घनों में केवल एक रंगीन सतह होगी?"
        ),
        "image_url": None,
        "option_a": "32",
        "option_b": "8",
        "option_c": "16",
        "option_d": "None/ कोई नहीं",
        "correct_answer": "C",   # 16 = 8 (piece-1) + 8 (piece-2)
    },

    # ── Q78 (book Q27) ──────────────────────────────────────────────────────
    # "2 red + 1 green" cubes:
    # Piece-1: Red only on top+bottom → each cube has ≤1 red face → 0.
    # Piece-2: Red = top+bottom+back+right; Green = front+left.
    #   Need 2 red + 1 green:
    #   (4,1,1): red(x=4)+red(z=1)+green(y=1) ✓
    #   (4,1,2): red(x=4)+red(z=2)+green(y=1) ✓
    #   (1,4,1): red(y=4)+red(z=1)+green(x=1) ✓
    #   (1,4,2): red(y=4)+red(z=2)+green(x=1) ✓ → 4 cubes.
    # Total = 0 + 4 = 4.
    {
        "question_number": 78,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_SPLIT}"
            "How many cubes have two red and one green face on each?"
        ),
        "question_hi": (
            f"{PRE_SPLIT_HI}"
            "किनते घनों में प्रत्येक पर दो लाल और एक हरी सतह होगी?"
        ),
        "image_url": None,
        "option_a": "0",
        "option_b": "8",
        "option_c": "16",
        "option_d": "4",
        "correct_answer": "D",   # 4 cubes in piece-2
    },

    # ── Q79 (book Q28) ──────────────────────────────────────────────────────
    # "No coloured face":
    # In BOTH pieces, every unit cube touches either z=1 (bottom) or z=2 (top),
    # both of which are painted faces (red in piece-1, red in piece-2).
    # Therefore every cube has ≥1 coloured face → 0 uncoloured cubes.
    {
        "question_number": 79,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_SPLIT}"
            "How many cubes have no coloured face at all?"
        ),
        "question_hi": (
            f"{PRE_SPLIT_HI}"
            "कितने घनों में कोई रंगीन सतह नहीं होगी?"
        ),
        "image_url": None,
        "option_a": "32",
        "option_b": "8",
        "option_c": "16",
        "option_d": "None/ कोई नहीं",
        "correct_answer": "D",   # None — every cube has ≥1 painted face
    },

    # ── Q80 (book Q29) ──────────────────────────────────────────────────────
    # Cuboid 4(L)×3(W)×3(H) = 36 unit cubes; Yellow/Red/Green as above.
    # Edge cubes (exactly 2 painted faces):
    #   4 edges ∥ x (length 4): (4-2)=2 non-corner each → 4×2 = 8
    #   4 edges ∥ y (breadth 3): (3-2)=1 each → 4×1 = 4
    #   4 edges ∥ z (height 3):  (3-2)=1 each → 4×1 = 4
    #   Total = 8+4+4 = 16.
    {
        "question_number": 80,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_443}"
            "How many small cubes will have only two faces coloured?"
        ),
        "question_hi": (
            f"{PRE_443_HI}"
            "कितने छोटे घनों में केवल दो सतह रंगी होंगी?"
        ),
        "image_url": None,
        "option_a": "8",
        "option_b": "24",
        "option_c": "16",
        "option_d": "12",
        "correct_answer": "C",   # 16 = 4×(4-2) + 4×(3-2) + 4×(3-2)
    },

    # ── Q81 (book Q30) ──────────────────────────────────────────────────────
    # Same cuboid. Interior cubes (no painted face):
    # (L-2)(W-2)(H-2) = (4-2)(3-2)(3-2) = 2×1×1 = 2.
    {
        "question_number": 81,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_443}"
            "How many small cubes will have no face coloured?"
        ),
        "question_hi": (
            f"{PRE_443_HI}"
            "कितने छोटे घनों में कोई सतह रंगी नहीं होगी?"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "2",
        "option_c": "4",
        "option_d": "8",
        "correct_answer": "B",   # 2 = (4-2)(3-2)(3-2) interior cubes
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
