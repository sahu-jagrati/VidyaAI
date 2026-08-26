"""
seed_reasoning_cube_cuboid_sheet10.py
=====================================
Seeds Reasoning → Cube & Cuboid  book Q8–Q10 (Piyush Varshney source).
Stored as question_numbers 59–61.

Answer key
──────────────────────────────────────────────────────────────────────
Q59 (book Q8)   A (8)   — 9×9×9 → 3cm = 3×3×3; three surfaces = corner = 8
Q60 (book Q9)   D (4)   — Cuboid 6×4×1; all cubes have green (h=1);
                          red+green+black only at 4 corners of 6×4 face
Q61 (book Q10)  D (2)   — 5×5×5; adjacent coloring (green+white+blue each
                          on 2 adjacent faces); only 2 diagonally-opposite
                          corners have all 3 colours simultaneously
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"
SOURCE  = "Piyush_Varshney_Cube_Cuboid"

QUESTIONS = [

    # ── Q59 (book Q8) ───────────────────────────────────────────────────────
    # A 9×9×9 cm cube is coloured green on all surfaces.
    # Cut into 3 cm small cubes → 9/3 = 3 → 3×3×3 = 27 small cubes.
    # Three surfaces painted = corner cubes = 8.
    {
        "question_number": 59,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            "A bigger cube of 9×9×9 cm size is coloured all surfaces with green. "
            "After that it is cut into 3 cm small cubes. "
            "The number of small cubes which have three surfaces painted?"
        ),
        "question_hi": (
            "एक 9 × 9 × 9 सेमी आकार का बड़ा घन है जिसकी सभी सतह हरे रंग से "
            "रंगी हुई हैं। इसके बाद इसे 3 सेमी छोटे घनों में काटा जाता है। "
            "छोटे घनों की संख्या जिसमें तीन सतहों को रंगीन किया गया है?"
        ),
        "image_url": None,
        "option_a": "8",
        "option_b": "27",
        "option_c": "9",
        "option_d": "3",
        "correct_answer": "A",   # 8 corner cubes
    },

    # ── Q60 (book Q9) ───────────────────────────────────────────────────────
    # Cuboid 6 cm × 4 cm × 1 cm cut into 1×1×1 cm cubes = 24 cubes.
    # Face colours:
    #   4×1 cm faces (left & right ends): Black
    #   6×1 cm faces (front & back sides): Red
    #   6×4 cm faces (top & bottom): Green
    # Since height = 1 unit, EVERY cube touches both top and bottom → all 24 are green.
    # Cubes with Red: on front(y=1) or back(y=4) row → 6+6 = 12 cubes
    # Cubes with Black: on left(x=1) or right(x=6) column → 4+4 = 8 cubes
    # Cubes with ALL THREE (green+red+black) = corners of 6×4 face:
    #   (1,1), (6,1), (1,4), (6,4) → 4 cubes.
    {
        "question_number": 60,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "A cuboid shaped wooden block has 6 cm length, 4 cm breadth and "
            "1 cm height. Two faces measuring 4 cm × 1 cm are coloured in black. "
            "Two faces measuring 6 cm × 1 cm are coloured in red. "
            "Two faces measuring 6 cm × 4 cm are coloured in green. "
            "The block is divided into 24 equal cubes of side 1 cm. "
            "How many cubes having red, green and black colours on at least one "
            "side of the cube will be formed?"
        ),
        "question_hi": (
            "एक घनाभ के आकार के लकड़ी के ब्लॉक की 6 सेमी लंबाई, 4 सेमी चौड़ाई "
            "और 1 सेमी ऊंचाई है। 4 सेमी × 1 सेमी मापने वाले दो सतह काले रंग से "
            "रंगी होती हैं। 6 सेमी × 1 सेमी मापने वाले दो सतह लाल रंग से रंगी "
            "होती हैं। 6 सेमी × 4 सेमी मापने वाले दो सतह हरे रंग से रंगी होती "
            "हैं। ब्लॉक को 24 बराबर घनों में बांटा गया है। ऐसे कितने घन होंगे "
            "जिनकी कम से कम एक सतह लाल, हरे और काले रंग की होगी?"
        ),
        "image_url": None,
        "option_a": "16",
        "option_b": "12",
        "option_c": "10",
        "option_d": "4",
        "correct_answer": "D",   # 4 corner cubes (touching all 3 colours)
    },

    # ── Q61 (book Q10) ──────────────────────────────────────────────────────
    # A big cube is cut into 125 tiny equal cubes (5×5×5).
    # Coloring on ADJACENT faces:
    #   2 adjacent faces: Green
    #   2 other adjacent faces: White
    #   2 remaining adjacent faces: Blue
    # With this arrangement, only 2 diagonally-opposite corner cubes touch
    # one face of each colour (green ∩ white ∩ blue).
    # (The specific grouping ensures that the "all-3-colours" constraint is
    # satisfied at exactly 2 corners.)
    {
        "question_number": 61,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Two adjacent portions of a big cube are varnished in green and "
            "other two adjacent portions are varnished in white and the rest of "
            "the two portions are varnished in blue. The cube is segmented into "
            "125 tiny and equal cubes. "
            "How many tiny cubes will be formed having all the three colours?"
        ),
        "question_hi": (
            "एक बड़े घन के दो आसन्न हिस्सों को हरे रंग में रंगे गए हैं और "
            "अन्य दो आसन्न हिस्सों को सफ़ेद में रंगे हैं और बाक़ी के दो हिस्से "
            "नीले रंग में रंगे होते हैं। घन को 125 छोटे और बराबर घनों में "
            "विभाजित किया जाता है। ऐसे कितने छोटे घन बनेंगे जिनमें सभी तीन "
            "रंग हों?"
        ),
        "image_url": None,
        "option_a": "7",
        "option_b": "9",
        "option_c": "10",
        "option_d": "2",
        "correct_answer": "D",   # 2 cubes (only 2 diagonally-opposite corners
                                 # touch one green, one white and one blue face)
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
