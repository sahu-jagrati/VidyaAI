"""
seed_reasoning_venn_diagram_sheet2.py
=======================================
Seeds Reasoning → Venn Diagram  Q11–Q19.
(Q10 not provided — skipped.)

NOTE: image_url = None for all rows; user will upload images to Supabase later.
      Run update_venn_diagram_image_urls_batch2.py once images are uploaded.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q11 B  (Actors, Animals, Birds)
     Actors (humans) are biologically animals → Actors ⊂ Animals.
     Birds are also animals → Birds ⊂ Animals.
     Actors ∩ Birds = ∅ (no actor is a bird).
     Diagram: Animals (large circle/rectangle) containing Actors and Birds
              as two separate non-overlapping smaller circles. → Option B.

Q12 A  (Zebra, Grass eating animals, Lions)
     Zebra eats grass → Zebra ⊂ Grass eating animals.
     Lions are carnivores → Lions ∩ Grass eating animals = ∅.
     Zebra ∩ Lions = ∅ (different animals).
     Diagram: large circle (Grass eaters) with Zebra (small circle inside)
              + Lions (completely separate circle). → Option A.

Q13 D  (Sharks, Whales, Turtles)
     Sharks: cartilaginous fish (Chondrichthyes).
     Whales: mammals (Mammalia).
     Turtles: reptiles (Testudines).
     All three are from completely different taxonomic classes.
     None is a subset of another; no overlap.
     Diagram: three completely separate, non-overlapping circles. → Option D.

Q14 C  (Blue-eyed, Females, Doctors)
     Blue-eyed ∩ Females ≠ ∅ (some women have blue eyes).
     Females ∩ Doctors ≠ ∅ (some doctors are female).
     Blue-eyed ∩ Doctors ≠ ∅ (some doctors have blue eyes).
     All three can intersect simultaneously (a blue-eyed female doctor exists).
     None is a subset of another.
     Diagram: three partially overlapping / intersecting circles. → Option C.

Q15 B  (Insects, Flies and Dogs)
     Flies are insects → Flies ⊂ Insects.
     Dogs are not insects → Dogs ∩ Insects = ∅, Dogs ∩ Flies = ∅.
     Diagram: large circle (Insects) with Flies (small circle inside)
              + Dogs (completely separate circle). → Option B.

Q16 A  (Colour, Cloth, Merchant)
     Within the Cloth domain:
       • "Colour" refers to the colouring / dyeing side of cloth.
       • "Merchant" refers to the cloth-selling side.
     Both Colour and Merchant belong to the Cloth domain, but they are
     distinct from each other (Colour ∩ Merchant = ∅).
     Diagram: Cloth (large rectangle/circle) containing Colour and Merchant
              as two separate non-overlapping circles. → Option A.

Q17 A  (Politicians, Poets, Women)
     Politicians ∩ Poets ≠ ∅ (some politicians write poetry).
     Politicians ∩ Women ≠ ∅ (some politicians are women).
     Poets ∩ Women ≠ ∅ (some poets are women).
     None is a subset of another; all three partially overlap.
     Diagram: three partially overlapping / intersecting circles. → Option A.

Q18 B  (Snake, Lizard, Reptiles)
     Snakes are reptiles → Snake ⊂ Reptiles.
     Lizards are reptiles → Lizard ⊂ Reptiles.
     Snake ∩ Lizard = ∅ (snakes and lizards are different animals).
     Same pattern as Q2 / Q4 / Q5 / Q8.
     Diagram: Reptiles (large circle) with Snake and Lizard as two separate
              non-overlapping smaller circles inside. → Option B.

Q19 B  (Village, District, State)
     Every Village is part of a District → Village ⊂ District.
     Every District is part of a State → District ⊂ State.
     Strict three-level hierarchy: Village ⊂ District ⊂ State.
     Same pattern as Q3 (Minutes, Days, Months).
     Diagram: three concentric circles — State (outermost), District (middle),
              Village (innermost). → Option B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Venn Diagram"

QUESTIONS = [

    # ── Q11 ──────────────────────────────────────────────────────────────────
    # Actors ⊂ Animals;  Birds ⊂ Animals;  Actors ∩ Birds = ∅.
    # Diagram: Animals (large) containing Actors and Birds (two separate
    # non-overlapping smaller circles).
    {
        "question_number": 11,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the following figures represents actor, animals, birds?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सी आकृति अभिनेताओं, जानवरों, "
            "पक्षियों को दर्शाती है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
        # Animals (large) with Actors and Birds as two separate circles inside.
    },

    # ── Q12 ──────────────────────────────────────────────────────────────────
    # Zebra ⊂ Grass eating animals;  Lions ∩ Grass eating animals = ∅.
    # Diagram: large circle (Grass eaters) + small circle inside (Zebra)
    #          + completely separate circle (Lions).
    {
        "question_number": 12,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which one of the following figures represents the relationship "
            "among Zebra, Grass eating animals, Lions?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा चित्र ज़ेबरा, घास खाने वाले "
            "जानवरों, शेरों के बीच संबंध को दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Large circle (Grass eaters) with Zebra inside + Lions as separate circle.
    },

    # ── Q13 ──────────────────────────────────────────────────────────────────
    # Sharks (Chondrichthyes), Whales (Mammalia), Turtles (Testudines) —
    # three different taxonomic classes; none overlaps or is a subset of another.
    # Diagram: three completely separate, non-overlapping circles.
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
        # Three completely separate non-overlapping circles (mutually exclusive classes).
    },

    # ── Q14 ──────────────────────────────────────────────────────────────────
    # Blue-eyed ∩ Females ≠ ∅;  Females ∩ Doctors ≠ ∅;
    # Blue-eyed ∩ Doctors ≠ ∅;  all three can intersect simultaneously.
    # None is a subset of another.
    # Diagram: three partially overlapping / intersecting circles.
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
        # Three partially overlapping circles (all pairwise intersections exist).
    },

    # ── Q15 ──────────────────────────────────────────────────────────────────
    # Flies ⊂ Insects;  Dogs ∩ Insects = ∅;  Dogs ∩ Flies = ∅.
    # Diagram: large circle (Insects) with Flies (small circle inside)
    #          + Dogs (completely separate circle outside Insects).
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
        # Large circle (Insects) with Flies (small inside) + Dogs (separate outside).
    },

    # ── Q16 ──────────────────────────────────────────────────────────────────
    # Within the Cloth domain: "Colour" (dyeing side) and "Merchant"
    # (selling side) are both parts of Cloth, but distinct from each other.
    # Colour ∩ Merchant = ∅.
    # Diagram: Cloth (large rectangle/circle) containing Colour and Merchant
    #          as two separate non-overlapping circles.
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
        # Cloth (large) containing Colour and Merchant as two separate circles.
    },

    # ── Q17 ──────────────────────────────────────────────────────────────────
    # Politicians ∩ Poets ≠ ∅;  Politicians ∩ Women ≠ ∅;  Poets ∩ Women ≠ ∅.
    # None is a subset of another; all three partially overlap.
    # Diagram: three partially overlapping / intersecting circles.
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
        # Three partially overlapping circles (all pairwise intersections exist).
    },

    # ── Q18 ──────────────────────────────────────────────────────────────────
    # Snake ⊂ Reptiles;  Lizard ⊂ Reptiles;  Snake ∩ Lizard = ∅.
    # Same pattern as Q2 / Q4 / Q5 / Q8 / Q11.
    # Diagram: Reptiles (large circle) with Snake and Lizard as two separate
    #          non-overlapping smaller circles inside.
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
        # Reptiles (large) with Snake and Lizard as two separate circles inside.
    },

    # ── Q19 ──────────────────────────────────────────────────────────────────
    # Village ⊂ District ⊂ State (strict three-level administrative hierarchy).
    # Same pattern as Q3 (Minutes, Days, Months).
    # Diagram: three concentric circles — State (outermost), District (middle),
    #          Village (innermost).
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
        # Three concentric circles: State (outer) > District (middle) > Village (inner).
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
                "\n  After uploading images (venn_11.png … venn_19.png) to Supabase "
                "bucket 'question_image_venn_diagram', run:\n"
                "  python update_venn_diagram_image_urls_batch2.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
