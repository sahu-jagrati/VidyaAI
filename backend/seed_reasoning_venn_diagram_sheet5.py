"""
seed_reasoning_venn_diagram_sheet5.py
=======================================
Seeds Reasoning → Venn Diagram  Q35–Q37.

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_venn_diagram_image_urls_batch5.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q35 A  (Mountains, Forests, Earth)
     Mountains ⊂ Earth (mountains are on Earth).
     Forests   ⊂ Earth (forests are on Earth).
     Mountains ∩ Forests = ∅  (treated as separate in exam context).
     Diagram: Earth (large circle) with Mountains and Forests as two
              separate non-overlapping smaller circles inside. → A.

Q36 B  (Building material, Cement, Wood)
     Cement ⊂ Building material; Wood ⊂ Building material.
     Cement ∩ Wood = ∅ (different materials).
     Diagram: Building material (large circle) with Cement and Wood as
              two separate non-overlapping smaller circles inside. → B.

Q37 B  (Brinjal, Meat, Vegetables)
     Brinjal ⊂ Vegetables (brinjal is a vegetable).
     Meat ∩ Vegetables = ∅; Meat ∩ Brinjal = ∅.
     Diagram: Vegetables (large circle) with Brinjal (small circle inside)
              + Meat (completely separate circle outside). → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Venn Diagram"

QUESTIONS = [

    # ── Q35 ──────────────────────────────────────────────────────────────────
    # Mountains ⊂ Earth; Forests ⊂ Earth; Mountains ∩ Forests = ∅.
    # Diagram: Earth (large) with Mountains & Forests (two separate inside).
    {
        "question_number": 35,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Find out which of the diagrams as given in the alternatives "
            "correctly represents the relationship stated in the question: "
            "Mountains, Forests, Earth."
        ),
        "question_hi": (
            "पता लगाएँ कि विकल्पों में दिए गए आरेखों में से कौन सा "
            "चित्र प्रश्न में बताए गए संबंध को सही ढंग से दर्शाता है: "
            "पहाड़, जंगल, धरती।"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Earth (large circle) with Mountains and Forests as two separate
        # non-overlapping smaller circles inside.
    },

    # ── Q36 ──────────────────────────────────────────────────────────────────
    # Cement ⊂ Building material; Wood ⊂ Building material; C ∩ W = ∅.
    # Diagram: Building material (large) with Cement & Wood (two separate inside).
    {
        "question_number": 36,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the following figures represents the relationship "
            "between Building material, Cement and Wood?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा चित्र भवन निर्माण सामग्री, "
            "सीमेंट और लकड़ी के बीच संबंध को दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
        # Building material (large circle) with Cement and Wood as two
        # separate non-overlapping smaller circles inside.
    },

    # ── Q37 ──────────────────────────────────────────────────────────────────
    # Brinjal ⊂ Vegetables; Meat is completely separate from both.
    # Diagram: Vegetables (large) with Brinjal inside + Meat separate.
    {
        "question_number": 37,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which one of the following figures represents the relationship "
            "among Brinjal, Meat, Vegetables?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा चित्र बैंगन, मांस, सब्जियों के "
            "बीच संबंध को दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
        # Vegetables (large circle) with Brinjal (small circle inside)
        # + Meat (completely separate circle outside).
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Venn Diagram Q35–Q37 into '{TOPIC}' / '{SUBJECT}'")

        for d in QUESTIONS:
            qn = d["question_number"]
            exists = (
                db.query(Question)
                .filter(
                    Question.subject == SUBJECT,
                    Question.topic == TOPIC,
                    Question.question_number == qn,
                )
                .first()
            )
            if exists:
                print(f"  SKIP  Q{qn}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
            inserted += 1
            print(f"  INSERT Q{qn}")

        db.commit()
        print(f"\nDone — inserted: {inserted}, skipped: {skipped}")
        if inserted:
            print(
                "\n  Upload venn_35.png … venn_37.png to Supabase bucket "
                "'question_image_Venn_Diagram', then run:\n"
                "  python update_venn_diagram_image_urls_batch5.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
