"""
seed_reasoning_venn_diagram_sheet3.py
=======================================
Seeds Reasoning → Venn Diagram  Q21–Q25.
(Q20 not provided — skipped.)

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_venn_diagram_image_urls_batch3.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q21 A  (Feast scenario — Vegetarians, Non-veg, NV-no-meat, Meat-no-fish)
     Four MUTUALLY EXCLUSIVE groups at the feast:
       1. Vegetarians (eat nothing non-veg) → V
       2. Non-vegetarians eating meat AND fish → NV₂ (remainder of NV circle)
       3. Non-vegetarians NOT eating meat (fish/eggs only) → NV₃
       4. Eating MEAT but NOT fish → NV₄
     NV₂, NV₃, NV₄ are all sub-groups of the Non-vegetarian super-category.
     Diagram: outer boundary (all feast participants) → one large circle
     (Non-vegetarians) with two smaller non-overlapping circles inside
     (NV₃ and NV₄; NV₂ is the leftover area of the big circle) + one
     small separate circle (Vegetarians) outside the big circle but
     inside the outer boundary. → Option A.

Q22 B  (Dog, Animal, Pets)
     All dogs are pets (domestic); all pets are animals.
     Dog ⊂ Pets ⊂ Animals  (strict three-level hierarchy).
     Diagram: three concentric circles — Animals (outermost),
              Pets (middle), Dog (innermost). → Option B.

Q23 C  (Athletes, Football players, Cricket players)
     Football players ⊂ Athletes (all football players are athletes).
     Cricket players ⊂ Athletes (all cricket players are athletes).
     Football players ∩ Cricket players = ∅ (different sports).
     Diagram: Athletes (large circle) with Football and Cricket as two
              separate non-overlapping smaller circles inside. → Option C.

Q24 A  (Degree students, BA students, BSc students)
     BA students ⊂ Degree students;  BSc students ⊂ Degree students.
     BA students ∩ BSc students = ∅ (different degree programmes).
     Same pattern as Q2 (Cabbage / Vegetables / Beans).
     Diagram: Degree (large circle) with BA and BSc as two separate
              non-overlapping smaller circles inside. → Option A.

Q25 A  (Liquids, Metal, Gases)
     Liquids (water, oil …), Metals (iron, copper …), Gases (air, CO₂ …)
     are three distinct categories of matter with no subset relationship
     and no overlap (exam treats mercury's dual nature as edge case).
     Diagram: three completely separate, non-overlapping circles. → Option A.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Venn Diagram"

QUESTIONS = [

    # ── Q21 ──────────────────────────────────────────────────────────────────
    # Feast with 4 mutually exclusive dietary groups.
    # Diagram: outer boundary → big circle (NV) containing two small circles
    # (NV-no-meat, Meat-no-fish) + one small circle outside big circle (Veg).
    {
        "question_number": 21,
        "difficulty": "hard",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In a feast organised in connection with a marriage, some of the "
            "participants were vegetarians, some others were non-vegetarians. "
            "Another group was of non vegetarians not eating meat and yet another "
            "group of people eating meat but not fish. "
            "Which of the following represents this statistics?"
        ),
        "question_hi": (
            "एक विवाह के सिलसिले में आयोजित एक भोज में, भाग लेने वालों में से "
            "कुछ शाकाहारी थे, कुछ अन्य मांसाहारी थे। एक अन्य समूह मांसाहारी "
            "लोगों का था जो मांस नहीं खाते थे और कुछ अन्य समूह उन लोगों का "
            "था जो मांस खाते थे लेकिन मछली नहीं। "
            "निम्नलिखित में से कौन सा यह आँकड़ा दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Outer boundary → NV (big circle) with NV-no-meat & Meat-no-fish
        # (two circles inside) + Veg (separate circle outside NV, inside boundary).
    },

    # ── Q22 ──────────────────────────────────────────────────────────────────
    # Dog ⊂ Pets ⊂ Animals — strict three-level hierarchy.
    # Diagram: three concentric circles: Animals > Pets > Dog.
    {
        "question_number": 22,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which one of the following figures represents the relationship "
            "among Dog, Animal, Pets?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा चित्र कुत्ते, पशु, पालतू जानवर "
            "के बीच संबंध को दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
        # Three concentric circles: Animals (outer) > Pets (middle) > Dog (inner).
    },

    # ── Q23 ──────────────────────────────────────────────────────────────────
    # Football ⊂ Athletes;  Cricket ⊂ Athletes;  Football ∩ Cricket = ∅.
    # Diagram: Athletes (large) with Football & Cricket (two separate inside).
    {
        "question_number": 23,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Select the figure which represents the relationship between "
            "athletes, football players and cricket players."
        ),
        "question_hi": (
            "उस आकृति का चयन करें जो एथलीटों, फुटबॉल खिलाड़ियों और "
            "क्रिकेट खिलाड़ियों के बीच संबंध को दर्शाती है।"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "C",
        # Athletes (large circle) containing Football and Cricket as two
        # separate non-overlapping smaller circles.
    },

    # ── Q24 ──────────────────────────────────────────────────────────────────
    # BA ⊂ Degree;  BSc ⊂ Degree;  BA ∩ BSc = ∅.
    # Same pattern as Q2 (Cabbage / Vegetables / Beans).
    # Diagram: Degree (large) with BA & BSc (two separate inside).
    {
        "question_number": 24,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the following diagrams represents Degree students, "
            "BA students and BSc students?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा आरेख डिग्री छात्रों, बीए छात्रों "
            "और बीएससी छात्रों को दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Degree (large circle) with BA and BSc as two separate circles inside.
    },

    # ── Q25 ──────────────────────────────────────────────────────────────────
    # Liquids, Metals, Gases — three distinct categories of matter.
    # None is a subset of another; no overlap in exam context.
    # Diagram: three completely separate, non-overlapping circles.
    {
        "question_number": 25,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the following represents liquids, metal, gases?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन द्रव, धातु, गैस का प्रतिनिधित्व करता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Three completely separate, non-overlapping circles.
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
        # Show only the Venn Diagram specific count for clarity
        print(
            f"Seeding Venn Diagram Q21–Q25 into '{TOPIC}' / '{SUBJECT}'"
        )

        for d in QUESTIONS:
            qn = d["question_number"]
            # Check if this exact topic+question_number already exists
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
                "\n  Upload venn_21.png … venn_25.png to Supabase bucket "
                "'question_image_Venn_Diagram', then run:\n"
                "  python update_venn_diagram_image_urls_batch3.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
