"""
seed_reasoning_venn_diagram_sheet4.py
=======================================
Seeds Reasoning → Venn Diagram  Q27–Q34.
(Q26 not provided — skipped.)

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_venn_diagram_image_urls_batch4.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q27 B  (Judge, Thief, Criminal)
     Thief ⊂ Criminal (every thief is a criminal).
     Judge ∩ Criminal = ∅; Judge ∩ Thief = ∅ (in exam context).
     Diagram: Criminal (large circle) with Thief (small circle inside)
              + Judge (completely separate circle outside). → B.

Q28 A  (North America, United States of America, New York)
     New York ⊂ USA ⊂ North America — strict three-level geo hierarchy.
     Diagram: three concentric circles — North America (outer),
              USA (middle), New York (inner). → A.

Q29 B  (Cats, Rats, Animals)
     Cats ⊂ Animals; Rats ⊂ Animals; Cats ∩ Rats = ∅.
     Diagram: Animals (large circle) with Cats and Rats as two separate
              non-overlapping smaller circles inside. → B.

Q30 A  (Languages, English, Hindi)
     English ⊂ Languages; Hindi ⊂ Languages; English ∩ Hindi = ∅.
     Same pattern as Q29.
     Diagram: Languages (large circle) with English and Hindi as two
              separate non-overlapping smaller circles inside. → A.

Q31 D  (Sparrow, Birds, Mice)
     Sparrow ⊂ Birds (a sparrow is a bird).
     Mice ∩ Birds = ∅; Mice ∩ Sparrow = ∅.
     Diagram: Birds (large circle) with Sparrow (small circle inside)
              + Mice (completely separate circle outside). → D.

Q32 A  (Employers, Doctors, Women)
     A doctor can be an employer; a woman can be a doctor; a woman can
     be an employer — all three categories partially overlap.
     None is a strict subset of another.
     Diagram: three partially overlapping / intersecting circles. → A.

Q33 B  (Animals, Vegetables, Potatoes)
     Potatoes ⊂ Vegetables (potato is a vegetable).
     Animals ∩ Vegetables = ∅; Animals ∩ Potatoes = ∅.
     Diagram: Vegetables (large circle) with Potatoes (small circle inside)
              + Animals (completely separate circle outside). → B.

Q34 A  (Table, Chair, Furniture)
     Table ⊂ Furniture; Chair ⊂ Furniture; Table ∩ Chair = ∅.
     Same pattern as Q29.
     Diagram: Furniture (large circle) with Table and Chair as two
              separate non-overlapping smaller circles inside. → A.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Venn Diagram"

QUESTIONS = [

    # ── Q27 ──────────────────────────────────────────────────────────────────
    # Thief ⊂ Criminal; Judge is completely separate.
    # Diagram: Criminal (large) with Thief inside + Judge separate.
    {
        "question_number": 27,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which one of the following diagrams represents the correct "
            "relationship among 'Judge', 'Thief' and 'Criminal'?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा आरेख 'न्यायाधीश', 'चोर' और "
            "'अपराधी' के बीच सही संबंध दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
        # Criminal (large circle) with Thief inside + Judge separate.
    },

    # ── Q28 ──────────────────────────────────────────────────────────────────
    # NY ⊂ USA ⊂ North America — strict three-level hierarchy.
    # Diagram: three concentric circles.
    {
        "question_number": 28,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the following diagrams represents the relationship "
            "among three given classes: "
            "North America, United States of America, New York?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा आरेख तीन दिए गए वर्गों के बीच "
            "संबंध को दर्शाता है: "
            "उत्तरी अमेरिका, संयुक्त राज्य अमेरिका, न्यूयॉर्क?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Three concentric circles: North America (outer) > USA (middle) > New York (inner).
    },

    # ── Q29 ──────────────────────────────────────────────────────────────────
    # Cats ⊂ Animals; Rats ⊂ Animals; Cats ∩ Rats = ∅.
    # Diagram: Animals (large) with Cats & Rats (two separate circles inside).
    {
        "question_number": 29,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "If each circle represents a class of objects/ideas, "
            "find out the answer figure which illustrates the better "
            "relationship among them: Cats, Rats, Animals."
        ),
        "question_hi": (
            "यदि प्रत्येक वृत्त नीचे लिखी गई वस्तुओं/विचारों के एक वर्ग "
            "का प्रतिनिधित्व करता है, तो उस उत्तर आकृति का पता लगाएं "
            "जो उनके बीच के संबंध को बेहतर ढंग से दर्शाती है: "
            "बिल्लियाँ, चूहे, जानवर।"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
        # Animals (large) containing Cats and Rats as two separate smaller circles.
    },

    # ── Q30 ──────────────────────────────────────────────────────────────────
    # English ⊂ Languages; Hindi ⊂ Languages; English ∩ Hindi = ∅.
    # Diagram: Languages (large) with English & Hindi (two separate circles inside).
    {
        "question_number": 30,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Choose from the four diagrams given below, the one that "
            "illustrates the relationship among languages, English and Hindi."
        ),
        "question_hi": (
            "नीचे दिए गए चार आरेखों में से वह चुनें जो भाषाओं, "
            "अंग्रेज़ी और हिंदी के बीच संबंध को दर्शाता है।"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Languages (large) containing English and Hindi as two separate smaller circles.
    },

    # ── Q31 ──────────────────────────────────────────────────────────────────
    # Sparrow ⊂ Birds; Mice completely separate from both.
    # Diagram: Birds (large) with Sparrow inside + Mice separate.
    {
        "question_number": 31,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Out of four figures which figure will best represent the "
            "relationship amongst the classes: Sparrow, Birds, Mice?"
        ),
        "question_hi": (
            "चार आंकड़ों में से कौन सा आंकड़ा वर्गों के बीच संबंध का "
            "सबसे अच्छा प्रतिनिधित्व करेगा: गौरैया, पक्षी, चूहे?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "D",
        # Birds (large) with Sparrow inside + Mice completely separate.
    },

    # ── Q32 ──────────────────────────────────────────────────────────────────
    # Employers ∩ Doctors ≠ ∅; Doctors ∩ Women ≠ ∅; Women ∩ Employers ≠ ∅.
    # None is a subset of another — three partially overlapping circles.
    {
        "question_number": 32,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Find out which of the diagrams as given in the alternatives "
            "correctly represents the relationship among "
            "Employers, Doctors and Women."
        ),
        "question_hi": (
            "ज्ञात कीजिए कि विकल्पों में दिए गए आरेखों में से कौन "
            "सा आरेख नियोक्ता, डॉक्टरों और महिलाओं के बीच "
            "संबंधों को सही ढंग से दर्शाता है।"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Three partially overlapping / intersecting circles.
    },

    # ── Q33 ──────────────────────────────────────────────────────────────────
    # Potatoes ⊂ Vegetables; Animals completely separate from both.
    # Diagram: Vegetables (large) with Potatoes inside + Animals separate.
    {
        "question_number": 33,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which figure represents the relation among "
            "animals, vegetables and potatoes?"
        ),
        "question_hi": (
            "कौन सी आकृति जानवरों, सब्जियों और आलू के बीच "
            "संबंध को दर्शाती है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
        # Vegetables (large) with Potatoes inside + Animals completely separate.
    },

    # ── Q34 ──────────────────────────────────────────────────────────────────
    # Table ⊂ Furniture; Chair ⊂ Furniture; Table ∩ Chair = ∅.
    # Diagram: Furniture (large) with Table and Chair (two separate circles inside).
    {
        "question_number": 34,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which one of the following figures represents the relationship "
            "among Table, Chair, Furniture?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा चित्र टेबल, कुर्सी, फर्नीचर के "
            "बीच संबंध को दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Furniture (large) with Table and Chair as two separate smaller circles inside.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Venn Diagram Q27–Q34 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload venn_27.png … venn_34.png to Supabase bucket "
                "'question_image_Venn_Diagram', then run:\n"
                "  python update_venn_diagram_image_urls_batch4.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
