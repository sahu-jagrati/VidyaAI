"""
seed_reasoning_non_verbal_sheet7.py
========================================
Seeds Reasoning → Non-Verbal  Q28, Q30, Q31, Q32, Q33.

(Q27 and Q29 not yet provided — gaps intentional.)

Question types:
  Q28  = Embedded / Hidden Figure
  Q30  = Embedded / Hidden Figure
  Q31  = Pattern Completion (complete the missing quadrant)
  Q32  = Pattern Completion
  Q33  = Pattern Completion

NOTE: image_url = None; upload images to Supabase and run
      update_non_verbal_image_urls_batch7.py.

Bucket  : question_image_Non_Verbal
Pattern : non_verbal_{N}.png

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q28 B  Question figure: M-shape / bowtie (two triangles touching at
     vertices or sharing a side). The shape's diagonal edges are
     embedded within option (b)'s X-diagonal + horizontal band
     pattern — the horizontal divider + two crossing diagonals
     create the exact M/bowtie outline. → B.

Q30 A  Question figure: irregular quadrilateral / rectangle with an
     internal step-line or diagonal (resembles a right-angled polygon
     with an interior mark). This compound shape is hidden within
     option (a)'s complex arrangement of diagonal lines and
     smaller rectangles. → A.

Q31 B  Pattern completion. Question figure: 2×2 arrangement;
     3 quadrants filled with a spiral/pinwheel pattern (black corner
     triangles rotating 90° per cell); bottom-right quadrant blank.
     The missing piece must continue the 90° rotation → option (b)
     shows the correctly oriented black-triangle piece. → B.

Q32 C  Pattern completion. Question figure: large square with 4 leaf/
     petal shapes arranged in a cross (pointing ↑↓←→ from centre);
     bottom-left quadrant is "?". The lower-left portion of the
     cross pattern (two petals) appears in option (c) at the
     correct orientation. → C.

Q33 B  Pattern completion. Question figure: 2×2 pattern with black
     triangle + diagonal stripe in each cell, rotating 90° per cell;
     missing piece (one quadrant) must complete the rotation.
     Option (b) shows the correctly oriented diagonal stripe +
     black triangle for that position. → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Non-Verbal"

QUESTIONS = [

    # ── Q28 ──────────────────────────────────────────────────────────────────
    # Embedded figure. Question: M-shape / bowtie (two triangles).
    # Hidden in X-diagonal + horizontal band of option (b). → B.
    {
        "question_number": 28,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Select the answer figure in which the question figure "
            "is hidden/embedded."
        ),
        "question_hi": (
            "उस उत्तर आकृति का चयन करें जिसमें प्रश्न आकृति "
            "छिपी/निहित है।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # M-shape/bowtie's diagonal edges match the X-diagonal + horizontal
        # divider structure of option (b). → B.
    },

    # ── Q30 ──────────────────────────────────────────────────────────────────
    # Embedded figure. Question: irregular polygon (rectangle + step/diagonal).
    # Hidden in complex diagonal + rectangle pattern of option (a). → A.
    {
        "question_number": 30,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions, from the given answer "
            "figures, select the one in which the question figure is "
            "hidden/embedded."
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में, दिए गए उत्तर आकृतियों में से, "
            "उस उत्तर आकृति का चयन करें जिसमें प्रश्न आकृति "
            "छिपी/अंतिनिहित है।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "A",
        # Irregular polygon's outline is traceable within option (a)'s
        # complex diagonal + rectangle arrangement. → A.
    },

    # ── Q31 ──────────────────────────────────────────────────────────────────
    # Pattern completion. 2×2 spiral pinwheel; missing bottom-right. → B.
    {
        "question_number": 31,
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
        # 2×2 spiral/pinwheel with black corner triangles rotating 90° per
        # cell; missing quadrant completed by option (b)'s correctly oriented
        # piece. → B.
    },

    # ── Q32 ──────────────────────────────────────────────────────────────────
    # Pattern completion. 4-leaf cross; bottom-left "?". → C.
    {
        "question_number": 32,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which answer figure will complete the pattern in the "
            "Question figure?"
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
        # Large square with 4 leaf/petal shapes in a cross pattern (↑↓←→);
        # bottom-left quadrant is "?". Option (c) shows the correct lower-left
        # petal pair orientation to complete the cross. → C.
    },

    # ── Q33 ──────────────────────────────────────────────────────────────────
    # Pattern completion. 2×2 diagonal stripe + black triangle; missing piece. → B.
    {
        "question_number": 33,
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
        # 2×2 pattern with black triangle + diagonal stripe rotating 90° per cell.
        # Missing quadrant completed by option (b)'s correctly oriented
        # diagonal stripe + black triangle piece. → B.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Non-Verbal Q28, Q30–Q33 into '{TOPIC}' / '{SUBJECT}'")
        print("(Q27 and Q29 are gaps — not provided yet)")

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
                "\n  Upload non_verbal_28.png, non_verbal_30.png – non_verbal_33.png "
                "to Supabase bucket 'question_image_Non_Verbal', then run:\n"
                "  python update_non_verbal_image_urls_batch7.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
