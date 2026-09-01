"""
seed_reasoning_venn_diagram_sheet1.py
=======================================
Seeds Reasoning → Venn Diagram  Q1–Q9.

NOTE: All image_url fields are None — user will upload images to Supabase later.
      Run update_venn_diagram_image_urls_batch1.py once images are uploaded.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q1  A  (Pigeon, Birds, Dogs)
     Pigeon ⊂ Birds (pigeons are birds).
     Dogs ∩ (Birds ∪ Pigeon) = ∅ (dogs are not birds).
     Diagram: large circle (Birds) containing small circle (Pigeon);
              separate unconnected circle (Dogs). → Option A.

Q2  B  (Cabbage, Vegetables, Beans)
     Cabbage ⊂ Vegetables;  Beans ⊂ Vegetables;  Cabbage ∩ Beans = ∅.
     Diagram: large circle (Vegetables) with two separate smaller
              circles inside (Cabbage, Beans). → Option B.

Q3  A  (Minutes, Days, Months)
     Minutes ⊂ Days ⊂ Months (strict time-unit hierarchy).
     Diagram: three concentric circles — Months (outermost),
              Days (middle), Minutes (innermost). → Option A.

Q4  B  (Rice, Wheat, Grain)
     Rice ⊂ Grain;  Wheat ⊂ Grain;  Rice ∩ Wheat = ∅.
     Same pattern as Q2. → Option B.

Q5  B  (Husband, Wife, Family)
     Husband ⊂ Family;  Wife ⊂ Family;  Husband ∩ Wife = ∅.
     Same pattern as Q2. → Option B.

Q6  D  (Shirts, Bed sheets, Towels)
     All three are distinct fabric items — no subset/overlap relationship.
     Diagram: three completely separate, non-overlapping circles. → Option D.

Q7  A  (Students: Law & Music / Music & Dance / Law & Dance)
     The three groups partially overlap (a student studying all three
     subjects belongs to all three groups simultaneously).
     Diagram: three intersecting / overlapping circles. → Option A.

Q8  B  (Family, Sons, Daughters)
     Sons ⊂ Family;  Daughters ⊂ Family;  Sons ∩ Daughters = ∅.
     Same pattern as Q2 / Q4 / Q5. → Option B.

Q9  C  (Illiterates, Poor people, Unemployed)
     All three groups partially overlap with each other but none is
     a strict subset of another.
     Diagram: three intersecting / overlapping circles. → Option C.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Venn Diagram"

QUESTIONS = [

    # ── Q1 ───────────────────────────────────────────────────────────────────
    # Pigeon ⊂ Birds;  Dogs ∩ (Birds ∪ Pigeon) = ∅.
    # Correct diagram: large circle (Birds) with small circle (Pigeon) inside,
    # plus a completely separate circle (Dogs).
    {
        "question_number": 1,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which one of the following diagrams represents correct relationship "
            "among pigeon, birds, dogs?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा आरेख कबूतर, पक्षी, कुत्ते के बीच "
            "सही संबंध दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Pigeon inside Birds circle; Dogs as a completely separate circle.
    },

    # ── Q2 ───────────────────────────────────────────────────────────────────
    # Cabbage ⊂ Vegetables;  Beans ⊂ Vegetables;  Cabbage ∩ Beans = ∅.
    # Correct: Vegetables (big circle) containing Cabbage & Beans (two
    # separate smaller circles inside).
    {
        "question_number": 2,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the following represents Cabbage, Vegetables and Beans?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा पत्तागोभी, सब्जियाँ और फलियाँ दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
        # Vegetables (large) containing Cabbage and Beans as two separate
        # non-overlapping circles.
    },

    # ── Q3 ───────────────────────────────────────────────────────────────────
    # Minutes ⊂ Days ⊂ Months (strict time hierarchy).
    # Correct: three concentric circles — Months outermost, Days middle,
    # Minutes innermost.
    {
        "question_number": 3,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Choose from the given four diagrams (A), (B), (C), (D) the one "
            "that best illustrates the relationship among three classes: "
            "Minutes, Days, Months."
        ),
        "question_hi": (
            "दिए गए चार आरेखों (A), (B), (C), (D) में से वह चुनें जो तीन "
            "वर्गों के बीच संबंध को सबसे अच्छा दर्शाता है। "
            "मिनट, दिन, महीने।"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Three concentric circles: Months (outer) > Days (middle) > Minutes (inner).
    },

    # ── Q4 ───────────────────────────────────────────────────────────────────
    # Rice ⊂ Grain;  Wheat ⊂ Grain;  Rice ∩ Wheat = ∅.
    # Same diagram pattern as Q2.
    {
        "question_number": 4,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which one of the following represents Rice, Wheat and Grain?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा चावल, गेहूँ और अनाज का "
            "प्रतिनिधित्व करता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
        # Grain (large) containing Rice and Wheat as two separate circles.
    },

    # ── Q5 ───────────────────────────────────────────────────────────────────
    # Husband ⊂ Family;  Wife ⊂ Family;  Husband ∩ Wife = ∅.
    # Same diagram pattern as Q2 / Q4.
    {
        "question_number": 5,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the diagrams given below correctly represents the "
            "relationship among husband, wife and family?"
        ),
        "question_hi": (
            "नीचे दिया गया कौन सा आरेख पति, पत्नी और परिवार के बीच "
            "संबंधों को सही ढंग से दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
        # Family (large) containing Husband and Wife as two separate circles.
    },

    # ── Q6 ───────────────────────────────────────────────────────────────────
    # Shirts, Bed sheets, Towels are three distinct fabric items with no
    # subset or overlap relationship among them.
    # Correct: three completely separate, non-overlapping circles.
    {
        "question_number": 6,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which one of the following figures represents the relationship "
            "among Shirts, Bed sheets and Towels?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा चित्र शर्ट, चादर और तौलिये के "
            "बीच संबंध को दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "D",
        # Three completely separate, non-overlapping circles (no parent set mentioned).
    },

    # ── Q7 ───────────────────────────────────────────────────────────────────
    # Three groups of students:
    #   Group A: learn Law AND Music
    #   Group B: learn Music AND Dance
    #   Group C: learn Law AND Dance
    # A student who studies all three subjects belongs to all three groups
    # → the groups partially overlap each other.
    # Correct: three intersecting / overlapping circles.
    {
        "question_number": 7,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the diagrams given below correctly represents the students "
            "who learn law and music, music and dance, law and dance?"
        ),
        "question_hi": (
            "नीचे दिया गया कौन सा आरेख कानून और संगीत, संगीत और नृत्य, "
            "और कानून और नृत्य सीखने वाले छात्रों को सही ढंग से दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Three overlapping/intersecting circles (each pair shares students
        # who study all three subjects).
    },

    # ── Q8 ───────────────────────────────────────────────────────────────────
    # Sons ⊂ Family;  Daughters ⊂ Family;  Sons ∩ Daughters = ∅.
    # Same diagram pattern as Q2 / Q4 / Q5.
    {
        "question_number": 8,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which one of the following figures represents family, sons and daughters?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा चित्र परिवार, बेटे और बेटियों को दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
        # Family (large) containing Sons and Daughters as two separate circles.
    },

    # ── Q9 ───────────────────────────────────────────────────────────────────
    # Illiterates, Poor people, Unemployed — all three groups partially
    # overlap each other, but none is a strict subset of another.
    # (Some poor people are illiterate; some unemployed are poor; etc.)
    # Correct: three intersecting / overlapping circles.
    {
        "question_number": 9,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Identify the diagram that correctly represents the relationship "
            "among illiterates, poor people and unemployed."
        ),
        "question_hi": (
            "उस आरेख को पहचानें जो निरक्षर, गरीब लोगों और बेरोजगारों के "
            "बीच संबंधों को सही ढंग से दर्शाता है।"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "C",
        # Three overlapping/intersecting circles (partial overlaps, no subset).
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
            if row[0] is not None
        }
        print(
            f"Topic '{TOPIC}' (subject='{SUBJECT}') — "
            f"existing question_numbers: {len(existing_qnums)}"
        )

        for d in QUESTIONS:
            qn = d["question_number"]
            if qn in existing_qnums:
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
                f"\n  Topic 'Venn Diagram' created automatically "
                f"(stored as the 'topic' field on each question)."
            )
            print(
                "  Run update_venn_diagram_image_urls_batch1.py "
                "after uploading images to Supabase."
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
