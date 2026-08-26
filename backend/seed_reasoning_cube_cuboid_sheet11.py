"""
seed_reasoning_cube_cuboid_sheet11.py
======================================
Seeds Reasoning → Cube & Cuboid  book Q11–Q13 (Piyush Varshney source).
Stored as question_numbers 62–64.

Answer key
──────────────────────────────────────────────────────────────────────
Q62 (book Q11)  A (3)   — 3×3×3 = 27 cubes; 2-adj Black, 2-adj Maroon, 2-Pink.
                          Cubes with exactly 1 maroon + 1 black (no other colour):
                          standard asymmetric adjacent arrangement → 3 intersection
                          edges, each contributing 1 non-corner middle cube = 3.
Q63 (book Q12)  A (6)   — 9×9×9 → 3 cm = 3×3×3; only 1 side coloured
                          = face-only cubes = 6 × (3-2)² = 6 × 1 = 6.
Q64 (book Q13)  C (20)  — same 3×3×3 cube; at least 2 surfaces coloured
                          = edge cubes (12×1=12) + corner cubes (8) = 20.
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

# Q62: 3×3×3 cube with 3-colour adjacent-face coloring
PRE_3COL = (
    "Two adjacent portions of a big cube are varnished in black and other two "
    "adjacent portions are varnished in maroon and the rest of the two portions "
    "are varnished in pink. The cube is segmented into 27 tiny and equal cubes. "
)
PRE_3COL_HI = (
    "एक बड़े घन के दो आसन्न हिस्सों को काले रंग में रंगे गए हैं और अन्य दो "
    "आसन्न हिस्सों को मैरून में रंगे हैं और बाक़ी के दो हिस्से गुलाबी रंग में "
    "रंगे होते हैं। घन को 27 छोटे और बराबर घनों में विभाजित किया गया है। "
)

# Q63 & Q64: 9×9×9 cube all-green, cut into 3 cm cubes → 3×3×3 = 27 small cubes
PRE_9_GREEN = (
    "A bigger cube of 9×9×9 cm size is coloured all surface with green. "
    "After that it is cut into three cm small cubes. "
)
PRE_9_GREEN_HI = (
    "एक 9 × 9 × 9 सेमी आकार का बड़ा घन है जिसकी सभी सतह हरे रंग से रंगी हुई "
    "हैं। इसके बाद इसे 3 सेमी छोटे घनों में काटा जाता है। "
)

QUESTIONS = [

    # ── Q62 (book Q11) ──────────────────────────────────────────────────────
    # 3×3×3 = 27 cubes; 3-colour adjacent-face coloring.
    # Cubes with exactly 1 maroon AND exactly 1 black face (no pink):
    # With the standard asymmetric adjacent arrangement:
    #   Black: e.g. Front(x=1) + Top(z=3)
    #   Maroon: e.g. Back(x=3) + Right(y=3)  [each maroon face is adjacent
    #                                          to BOTH black faces]
    #   Pink: Bottom(z=1) + Left(y=1)
    # 3 maroon-black adjacent edges → 3 non-corner edge cubes → answer = 3.
    {
        "question_number": 62,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_3COL}"
            "How many tiny cubes will be formed having one portion maroon and "
            "one portion black only?"
        ),
        "question_hi": (
            f"{PRE_3COL_HI}"
            "केवल एक सतह मैरून और दूसरी सतह काले रंग के कितने छोटे घन बनेंगे?"
        ),
        "image_url": None,
        "option_a": "3",
        "option_b": "20",
        "option_c": "16",
        "option_d": "24",
        "correct_answer": "A",   # 3 edge cubes (one per maroon-black intersection edge)
    },

    # ── Q63 (book Q12) ──────────────────────────────────────────────────────
    # 9×9×9 cm cube, all-green, cut into 3 cm → 3×3×3 = 27 small cubes.
    # Only 1 side coloured = face-only cubes = 6 × (n−2)² = 6 × 1² = 6.
    {
        "question_number": 63,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_9_GREEN}"
            "Number of small cubes which have only one side coloured?"
        ),
        "question_hi": (
            f"{PRE_9_GREEN_HI}"
            "छोटे घनों की संख्या जिनकी केवल एक सतह रंगीन है?"
        ),
        "image_url": None,
        "option_a": "6",
        "option_b": "26",
        "option_c": "8",
        "option_d": "12",
        "correct_answer": "A",   # 6 face-only cubes (one per face of 3×3×3)
    },

    # ── Q64 (book Q13) ──────────────────────────────────────────────────────
    # Same 9×9×9 → 3 cm = 3×3×3 cube.
    # At least 2 surfaces coloured:
    #   Edge cubes (2 faces): 12 edges × (n−2) = 12 × 1 = 12
    #   Corner cubes (3 faces): 8
    #   Total = 12 + 8 = 20.
    {
        "question_number": 64,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_9_GREEN}"
            "The number of small cubes which have at least two surfaces coloured?"
        ),
        "question_hi": (
            f"{PRE_9_GREEN_HI}"
            "कम से कम दो रंगीन सतहों वाले छोटे घनों की संख्या?"
        ),
        "image_url": None,
        "option_a": "27",
        "option_b": "8",
        "option_c": "20",
        "option_d": "12",
        "correct_answer": "C",   # 20 = 12 edge + 8 corner
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
