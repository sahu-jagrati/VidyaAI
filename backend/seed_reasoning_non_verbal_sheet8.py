"""
seed_reasoning_non_verbal_sheet8.py
========================================
Seeds Reasoning → Non-Verbal  Q34, Q35, Q37, Q38, Q39, Q40.

(Q36 not yet provided — gap intentional.)

All questions are Pattern Completion type:
"Which answer figure will complete the pattern in the question figure?"

NOTE: image_url = None; upload images to Supabase and run
      update_non_verbal_image_urls_batch8.py.

Bucket  : question_image_Non_Verbal
Pattern : non_verbal_{N}.png

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q34 B  Question figure: 3×3 grid; each cell divided diagonally —
     upper-left triangle has diagonal hatching lines, lower-right
     has a circle/dot. Missing cell must continue this pattern.
     Option (b) shows the correctly oriented hatching + dot for
     that cell's position in the grid. → B.

Q35 C  Question figure: large circle with pinwheel/fan segments
     (alternating black-and-white triangular wedges, like a
     compass rose). One quarter section is "?".
     Option (c) shows the correct continuation of the pinwheel
     pattern for that quarter. → C.

Q37 A  Question figure: 2×2 grid; each filled quadrant shows a
     nested diamond (rotated square with internal lines). Top-left
     quadrant is "?". Option (a) shows the matching diamond
     pattern for the top-left position. → A.

Q38 C  Question figure: 2×2 grid; each quadrant has a triangular
     section + diagonal hatching. Top-left quadrant is "?".
     Option (c) shows the correct triangular + diagonal-line piece
     for the top-left position. → C.

Q39 A  Question figure: large circle with radiating leaf/petal
     shapes (like a chrysanthemum / compass rose), one section
     missing. Option (a) shows the curved leaf/petal piece that
     correctly continues the radial symmetry. → A.

Q40 B  Question figure: curved band / quarter-circle region filled
     with a regular array of small circles (honeycomb/bubble grid).
     Missing piece must have the right circle density and position.
     Option (b) shows the correctly densified circle arrangement
     that completes the pattern. → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Non-Verbal"

QUESTIONS = [

    # ── Q34 ──────────────────────────────────────────────────────────────────
    # Pattern completion. 3×3 grid; diagonal hatching + circles per cell. → B.
    {
        "question_number": 34,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following questions, which answer figure will "
            "complete the pattern in the question figure?"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों में, कौन सी उत्तर आकृति प्रश्न आकृति "
            "के पैटर्न को पूरा करेगी?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # 3×3 grid: each cell split diagonally — upper-left has hatching lines,
        # lower-right has a circle. Missing cell → option (b). → B.
    },

    # ── Q35 ──────────────────────────────────────────────────────────────────
    # Pattern completion. Circle with pinwheel/fan triangular segments; ? → C.
    {
        "question_number": 35,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions, which answer figure "
            "will complete the pattern in the question figure?"
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में, कौन सी उत्तर आकृति प्रश्न "
            "आकृति के पैटर्न को पूरा करेगी?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "C",
        # Circle with pinwheel/fan segments (alternating black-white wedges);
        # missing quarter → option (c) continues the pattern. → C.
    },

    # ── Q37 ──────────────────────────────────────────────────────────────────
    # Pattern completion. 2×2 grid; nested diamonds; top-left "?" → A.
    {
        "question_number": 37,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which answer figure will complete the pattern in the "
            "question figure?"
        ),
        "question_hi": (
            "कौन सी उत्तर आकृति प्रश्न आकृति के पैटर्न को पूरा करेगी?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "A",
        # 2×2 grid; each filled quadrant has a nested diamond (rotated square
        # with inner lines). Top-left "?" → option (a) shows the matching
        # diamond piece. → A.
    },

    # ── Q38 ──────────────────────────────────────────────────────────────────
    # Pattern completion. 2×2 grid; triangular + diagonal sections; ? → C.
    {
        "question_number": 38,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which answer figure will complete the pattern in the "
            "question figure?"
        ),
        "question_hi": (
            "कौन सी उत्तर आकृति प्रश्न आकृति के पैटर्न को पूरा करेगी?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "C",
        # 2×2 grid; each quadrant has triangular section + diagonal hatching.
        # Top-left "?" → option (c) provides the correct triangular +
        # diagonal-line piece. → C.
    },

    # ── Q39 ──────────────────────────────────────────────────────────────────
    # Pattern completion. Circle with radiating leaf/petal shapes; ? → A.
    {
        "question_number": 39,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions, which answer figure "
            "will complete the pattern in the question figure?"
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में, कौन सी उत्तर आकृति प्रश्न "
            "आकृति के पैटर्न को पूरा करेगी?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "A",
        # Circle with radiating leaf/petal pattern (chrysanthemum / compass
        # rose); missing section → option (a) shows the correctly curved
        # petal piece to complete the radial symmetry. → A.
    },

    # ── Q40 ──────────────────────────────────────────────────────────────────
    # Pattern completion. Curved band filled with small circles; ? → B.
    {
        "question_number": 40,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions, which answer figure "
            "will complete the pattern in the question figure?"
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में, कौन सी उत्तर आकृति प्रश्न "
            "आकृति के पैटर्न को पूरा करेगी?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Curved quarter-circle region filled with a regular honeycomb/bubble
        # grid of small circles. Missing piece → option (b) shows the correct
        # circle density and arrangement. → B.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Non-Verbal Q34, Q35, Q37–Q40 into '{TOPIC}' / '{SUBJECT}'")
        print("(Q36 is a gap — not provided yet)")

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
                "\n  Upload non_verbal_34.png, non_verbal_35.png, "
                "non_verbal_37.png – non_verbal_40.png "
                "to Supabase bucket 'question_image_Non_Verbal', then run:\n"
                "  python update_non_verbal_image_urls_batch8.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
