"""
seed_reasoning_cube_cuboid_sheet7.py
=====================================
Seeds questions Q1-Q5 (new batch) from Gagan Pratap Reasoning Cube & Cuboid PDFs.
Subject : Reasoning
Topic   : Cube & Cuboid
Run     : python seed_reasoning_cube_cuboid_sheet7.py

Answer key verification:
  Q1: 64=4^3 -> n=4; 3-face (corners) = 8                                        -> A
  Q2: 8x8x8, 2cm -> n=4; red+yellow only (no green) edge cubes = 4*(n-2)=8       -> C
  Q3: 6x4x1 cm cuboid, 1cm cuts -> total = 6*4*1 = 24                             -> D
  Q4: 216=6^3 -> n=6; >1 color = 216 - (6-2)^3 - 6*(6-2)^2 = 216-64-96 = 56     -> D
  Q5: 27=3^3; adj-face coloring (2 adj black, 2 adj maroon, 2 pink);
      exactly 2 corner small cubes touch all 3 colors                              -> D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Cube_Cuboid_Sheet7"
SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"

QUESTIONS = [
    # ── Q1 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": (
            "A cube is coloured red on all faces. It is cut into 64 smaller cubes "
            "of equal size. How many cubes have three face colored?"
        ),
        "question_hi": (
            "एक घन की सभी सतहों को लाल रंग से रंगी हुई है। इसे समान आकार के 64 "
            "छोटे घनों में काटा जाता है। अब इस कथन के आधार पर: कितने घन की तीन "
            "सतह रंगी होगी?"
        ),
        "option_a": "8",
        "option_b": "4",
        "option_c": "24",
        "option_d": "16",
        "correct_answer": "A",
    },
    # ── Q2 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 2,
        "difficulty": "medium",
        "question_en": (
            "A cube of 8×8×8 cm. side is coloured opposite surface with red, green "
            "and yellow. After that it is cut into 2 cm small cubes. The number of "
            "small cubes which have only two surface coloured and that too with red "
            "and yellow?"
        ),
        "question_hi": (
            "एक 8×8×8 सेमी का घन है, जिसकी विपरीत सतहें लाल, हरे और पीले रंग से "
            "रंगी हैं। उसके बाद घन को 2 सेमी में काट दिया जाता है। छोटे घनों की "
            "संख्या जिनकी केवल दो सतह रंगी हुई है वह एक लाल और दूसरी पीले रंग की "
            "है?"
        ),
        "option_a": "4",
        "option_b": "32",
        "option_c": "8",
        "option_d": "16",
        "correct_answer": "C",
    },
    # ── Q3 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": (
            "A cuboid shaped wooden block has 6 cm length, 4 cm breadth and 1 cm "
            "height. Two faces measuring 4cm×1cm are coloured in black. Two faces "
            "measuring 6cm×1cm are coloured in red. Two faces measuring 6cm×4cm "
            "are coloured in green. The block is divided into 6 equal cubes of side "
            "1cm (from 6cm side) and 4 equal cubes of side 1cm (from 4cm side). "
            "How many small cubes will be formed?"
        ),
        "question_hi": (
            "एक घनाभ के आकार के लकड़ी के ब्लॉक की 6 सेमी लंबाई, 4 सेमी चौड़ाई और "
            "1 सेमी ऊंचाई होती है। 4 सेमी×1 सेमी मापने वाले दो सतह काले रंग के "
            "होते हैं। 6 सेमी×1 सेमी मापने वाले दो सतह लाल रंग के होते हैं। "
            "6 सेमी×4 सेमी मापने वाले दो सतह हरे रंग के होते हैं। ब्लॉक को 1 "
            "सेमी भुजा के बराबर घनों में बांटा गया है। कितने छोटे घन बनेंगे?"
        ),
        "option_a": "6",
        "option_b": "12",
        "option_c": "16",
        "option_d": "24",
        "correct_answer": "D",
    },
    # ── Q4 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": (
            "A cube is segmented into 216 equal tiny cubes. Before dividing the "
            "cube, each face of it is varnished with different colours. How many "
            "tiny cubes will be formed having more than one colour?"
        ),
        "question_hi": (
            "एक घन को 216 बराबर छोटे घनों में विभाजित किया जाता है। घन को "
            "विभाजित करने से पहले, इसके प्रत्येक सतह को विभिन्न रंगों के साथ "
            "रंगा गया है। एक से अधिक रंग के कितने छोटे घन बनेंगे?"
        ),
        "option_a": "78",
        "option_b": "32",
        "option_c": "45",
        "option_d": "56",
        "correct_answer": "D",
    },
    # ── Q5 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 5,
        "difficulty": "hard",
        "question_en": (
            "Two adjacent portions of a big cube are varnished in black and other "
            "two adjacent portions are varnished in maroon and the rest of the two "
            "portions are varnished in pink. The cube is segmented into 27 tiny and "
            "equal cubes. How many tiny cubes will be formed having all the three "
            "colours?"
        ),
        "question_hi": (
            "एक बड़े घन के दो आसन्न हिस्से काले रंग से रंगे गए हैं और अन्य दो "
            "आसन्न हिस्से मैरून रंग से रंगे गए हैं और बाकी के दो हिस्से गुलाबी "
            "रंग से रंगे हुए हैं। घन को 27 छोटे और बराबर घनों में विभाजित किया "
            "गया है। ऐसे कितने छोटे घन बनेंगे जिनमें सभी तीन रंग हों?"
        ),
        "option_a": "7",
        "option_b": "9",
        "option_c": "10",
        "option_d": "2",
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
