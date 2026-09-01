"""
replace_venn_diagram_q13_q19.py
================================
Replaces existing Venn Diagram Q13–Q19 (which had stale data from a
previous session) with the correct questions from the current image sheet.

Steps:
  1. DELETE all Venn Diagram rows with question_number in {13..19}.
  2. INSERT the new Q13–Q19 rows with correct content.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q13 D  (Sharks, Whales, Turtles)
     Sharks: Chondrichthyes  |  Whales: Mammalia  |  Turtles: Testudines.
     All three are completely different taxonomic classes; none is a
     subset of another; no overlap.
     Diagram: three completely separate, non-overlapping circles. → D.

Q14 C  (Blue-eyed, Females, Doctors)
     Blue-eyed ∩ Females ≠ ∅; Females ∩ Doctors ≠ ∅; Blue-eyed ∩ Doctors ≠ ∅.
     None is a subset of another; all three partially overlap.
     Diagram: three partially overlapping / intersecting circles. → C.

Q15 B  (Insects, Flies and Dogs)
     Flies ⊂ Insects; Dogs ∩ Insects = ∅; Dogs ∩ Flies = ∅.
     Diagram: Insects (large) with Flies inside + Dogs separate. → B.

Q16 A  (Colour, Cloth, Merchant)
     Within the Cloth domain, "Colour" (dyeing) and "Merchant" (selling)
     are both sub-domains of Cloth, but distinct from each other.
     Colour ∩ Merchant = ∅.
     Diagram: Cloth (large) containing Colour and Merchant as two separate
              circles. → A.

Q17 A  (Politicians, Poets, Women)
     All three groups partially overlap; none is a subset of another.
     Diagram: three partially overlapping / intersecting circles. → A.

Q18 B  (Snake, Lizard, Reptiles)
     Snake ⊂ Reptiles; Lizard ⊂ Reptiles; Snake ∩ Lizard = ∅.
     Diagram: Reptiles (large) with Snake and Lizard as two separate
              non-overlapping smaller circles inside. → B.

Q19 B  (Village, District, State)
     Village ⊂ District ⊂ State (strict three-level administrative hierarchy).
     Diagram: three concentric circles — State (outer), District (middle),
              Village (inner). → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Venn Diagram"

NEW_QUESTIONS = [
    {
        "question_number": 13,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Find out which of the diagrams given in the alternatives correctly "
            "represents the relationship stated in the question. "
            "Sharks, Whales, Turtles."
        ),
        "question_hi": (
            "पता लगाएं कि विकल्पों में दिए गए आरेखों में से कौन सा चित्र "
            "प्रश्न में बताए गए संबंध को सही ढंग से दर्शाता है। "
            "शार्क, व्हेल, कछुए।"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "D",
    },
    {
        "question_number": 14,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Choose the correct figure that represents the given relation: "
            "Blue eyed, females, doctors."
        ),
        "question_hi": (
            "दिए गए संबंध को दर्शाने वाली सही आँकड़ा चुनें। "
            "नीली आँखों वाले, महिलाएं, डॉक्टर।"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "C",
    },
    {
        "question_number": 15,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which one of the following diagrams represents Insects, "
            "Flies and Dogs?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा आरेख कीड़े, मक्खियों "
            "और कुत्तों को दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
    },
    {
        "question_number": 16,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the following diagrams represents Colour, Cloth and Merchant?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा आरेख रंग, कपड़ा "
            "और व्यापारी को दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
    },
    {
        "question_number": 17,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which diagram correctly represents the relationship between "
            "politicians, poets and women?"
        ),
        "question_hi": (
            "कौन सा आरेख राजनेताओं, कवियों और महिलाओं के बीच "
            "संबंधों को सही ढंग से दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
    },
    {
        "question_number": 18,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which one of the following Venn diagrams represents the best "
            "relationship between Snake, Lizard, Reptiles?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा वेन आरेख साँप, छिपकली, "
            "सरीसृप के बीच सबसे अच्छे संबंध को दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
    },
    {
        "question_number": 19,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which one of the following figures represents Village, District, State?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा चित्र गाँव, जिला, राज्य "
            "का प्रतिनिधित्व करता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
    },
]

TARGET_QNUMS = {d["question_number"] for d in NEW_QUESTIONS}


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    deleted = inserted = 0
    try:
        # ── Step 1: delete all existing rows for Q13–Q19 in this topic ──────
        stale = (
            db.query(Question)
            .filter(
                Question.subject == SUBJECT,
                Question.topic == TOPIC,
                Question.question_number.in_(TARGET_QNUMS),
            )
            .all()
        )
        for row in stale:
            print(f"  DELETE stale  Q{row.question_number}: {row.question_en[:55]}…")
            db.delete(row)
            deleted += 1

        db.flush()   # flush deletes before inserts

        # ── Step 2: insert new rows ──────────────────────────────────────────
        for d in NEW_QUESTIONS:
            db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
            inserted += 1
            print(f"  INSERT Q{d['question_number']}: {d['question_en'][:55]}…")

        db.commit()
        print(f"\nDone — deleted: {deleted}, inserted: {inserted}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
