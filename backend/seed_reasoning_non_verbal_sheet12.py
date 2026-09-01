"""
seed_reasoning_non_verbal_sheet12.py
========================================
Seeds Reasoning → Non-Verbal  Q63, Q64, Q65, Q66, Q68, Q69, Q71, Q72, Q73.

(Q67 and Q70 not yet provided — gaps intentional.)

Question types:
  Q63–Q66, Q68–Q69  = Analogy ("select the related figure from alternatives")
  Q71–Q73           = Odd One Out ("find the odd figure from alternatives")

NOTE: image_url = None; upload images to Supabase and run
      update_non_verbal_image_urls_batch12.py.

Bucket  : question_image_Non_Verbal
Pattern : non_verbal_{N}.png

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q63 C  Analogy. Figure A (arrow+dot cluster) transforms to Figure B
     by rotation. Applying the same rotation to Figure C (larger
     arrow+dot cluster) gives Figure D = option (c): diagonal arrows
     in the correct orientation. → C.

Q64 B  Analogy. ∨ (angular V, vertex down) → < (angular, vertex right)
     = 90° clockwise rotation.
     ∪ (smooth curve opening up) rotated 90° CW = smooth curve
     opening to the right. Option (b) shows this. → B.

Q65 B  Analogy. ◇ (full diamond outline) → ⌢ (top half = dome).
     The same "keep upper half" transformation:
     ⌣ (arch/bottom-open curve) → lower-open half = option (b). → B.

Q66 D  Analogy. Concentric squares (3 rings) : concentric squares
     (2 rings) :: concentric circles (3 rings) : concentric circles
     (2 rings). Option (d) shows the concentric circle with 2 rings. → D.

Q68 B  Analogy. Figure 1 (triangle with hatching + small grid square) :
     Figure 2 (dots pattern) :: Figure 3 (same triangle arrangement,
     different orientation) : Figure 4. Applying the same transformation
     gives option (b) with the correct triangle + diagonal lines. → B.

Q69 B  Analogy. Figure 1 (L-bracket shapes in corners of box) :
     Figure 2 (dots at specific positions) :: Figure 3 (filled small
     square in box) : Figure 4. Same positional relationship gives
     option (b): small square placed at corresponding position. → B.

Q71 D  Odd one out. Options (a),(b),(c) each have exactly 2 internal
     line segments inside the circle (horizontal pair, vertical+horizontal
     cross, diagonal cross). Option (d) has both the + AND × crosses
     combined = 4 internal lines. → D is the odd one out.

Q72 B  Odd one out. Options (a),(c),(d) show consistent spoke+dot
     patterns (asterisk with dots at ends of equal-length spokes).
     Option (b) has a different structure (fewer spokes or asymmetric
     dot placement). → B is the odd one out.

Q73 D  Odd one out. Options (a),(b),(c) each contain the same set of
     symbols: ×, =, ○, +, △ (just rearranged in the box).
     Option (d) contains □ (square) instead of + — different symbol
     set. → D is the odd one out.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Non-Verbal"

QUESTIONS = [

    # ── Q63 ──────────────────────────────────────────────────────────────────
    # Analogy. Arrow+dot cluster rotated; same rotation applied to C. → C.
    {
        "question_number": 63,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following questions, select the related figure "
            "from the given alternatives."
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में, दिए गए विकल्पों में से "
            "संबंधित आकृति का चयन करें।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "C",
        # Arrow+dot figure A rotated to give B; same rotation on C → (c). → C.
    },

    # ── Q64 ──────────────────────────────────────────────────────────────────
    # Analogy. ∨→< (90° CW rotation); ∪→opening-right arc. → B.
    {
        "question_number": 64,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In following questions, select the related figure "
            "from the given alternatives."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों में, दिए गए विकल्पों में से संबंधित "
            "आकृति का चयन करें।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # ∨ rotated 90° CW → <; ∪ rotated 90° CW → opening-right arc → (b). → B.
    },

    # ── Q65 ──────────────────────────────────────────────────────────────────
    # Analogy. Diamond→dome (upper half kept); arch→lower half. → B.
    {
        "question_number": 65,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In following questions, select the related figure "
            "from the given alternatives."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों में, दिए गए विकल्पों में से संबंधित "
            "आकृति का चयन करें।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # ◇(diamond) → ⌢(dome/upper-half); ⌣(arch) → lower-open half → (b). → B.
    },

    # ── Q66 ──────────────────────────────────────────────────────────────────
    # Analogy. Concentric squares 3→2 rings :: concentric circles 3→2. → D.
    {
        "question_number": 66,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Select the related figure from the given alternatives."
        ),
        "question_hi": (
            "दिए गए विकल्पों में से संबंधित आकृति का चयन करें।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "D",
        # Concentric squares (3 rings) : (2 rings) :: concentric circles
        # (3 rings) : (2 rings) → option (d). → D.
    },

    # ── Q68 ──────────────────────────────────────────────────────────────────
    # Analogy. Triangle+hatching transforms to dots; same on new triangle. → B.
    {
        "question_number": 68,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Select the related figure from the given alternatives."
        ),
        "question_hi": (
            "दिए गए विकल्पों में से संबंधित आकृति का चयन करें।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Figure 1 (triangle+hatching+grid) : Figure 2 (dots) ::
        # Figure 3 (rotated triangle+hatching) : Figure 4 → (b). → B.
    },

    # ── Q69 ──────────────────────────────────────────────────────────────────
    # Analogy. L-bracket positions → dots :: filled square → same position. → B.
    {
        "question_number": 69,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Select the related figure from the given alternatives."
        ),
        "question_hi": (
            "दिए गए विकल्पों में से संबंधित आकृति का चयन करें।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # L-bracket (corners of box) : dots at same positions ::
        # filled square (top-left) : square at corresponding position → (b). → B.
    },

    # ── Q71 ──────────────────────────────────────────────────────────────────
    # Odd one out. (a),(b),(c) = 2 lines inside circle; (d) = 4 lines. → D.
    {
        "question_number": 71,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question find the odd figure "
            "from the given alternatives."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में दिए गए विकल्पों में से बेजोड़ आकृति "
            "ज्ञात कीजिए।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "D",
        # (a) 2 horizontal lines, (b) + cross (2 lines), (c) × cross (2 lines);
        # (d) has both + AND × = 4 lines — odd one out. → D.
    },

    # ── Q72 ──────────────────────────────────────────────────────────────────
    # Odd one out. (a),(c),(d) = consistent spoke+dot asterisk; (b) different. → B.
    {
        "question_number": 72,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question find the odd figure "
            "from the given alternatives."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में दिए गए विकल्पों में से बेजोड़ आकृति "
            "ज्ञात कीजिए।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # (a),(c),(d): asterisk with dots at equal-length spokes (symmetric);
        # (b): different spoke count or asymmetric dot placement — odd one. → B.
    },

    # ── Q73 ──────────────────────────────────────────────────────────────────
    # Odd one out. (a),(b),(c) contain {×,=,○,+,△}; (d) has □ instead of +. → D.
    {
        "question_number": 73,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question find the odd figure "
            "from the given alternatives."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में दिए गए विकल्पों में से बेजोड़ आकृति "
            "ज्ञात कीजिए।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "D",
        # (a),(b),(c): symbol sets {×,=,○,+,△} (same symbols, rearranged).
        # (d): contains □ replacing + — different symbol set → odd one. → D.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(
            f"Seeding Non-Verbal Q63–Q66, Q68–Q69, Q71–Q73 "
            f"into '{TOPIC}' / '{SUBJECT}'"
        )
        print("(Q67 and Q70 are gaps — not provided yet)")

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
                "\n  Upload non_verbal_63.png – non_verbal_66.png, "
                "non_verbal_68.png, non_verbal_69.png, "
                "non_verbal_71.png – non_verbal_73.png "
                "to Supabase bucket 'question_image_Non_Verbal', then run:\n"
                "  python update_non_verbal_image_urls_batch12.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
