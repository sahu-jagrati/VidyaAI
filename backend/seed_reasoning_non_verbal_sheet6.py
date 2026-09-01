"""
seed_reasoning_non_verbal_sheet6.py
========================================
Seeds Reasoning → Non-Verbal  Q23, Q24, Q25, Q26.

All four are Embedded / Hidden Figure questions:
"From the given answer figures, select the one in which the
 question figure is hidden/embedded."

NOTE: image_url = None; upload images to Supabase and run
      update_non_verbal_image_urls_batch6.py.

Bucket  : question_image_Non_Verbal
Pattern : non_verbal_{N}.png

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q23 C  Question figure: angular kite/arrow shape.
     Its straight-line edges appear as chords within option (c) —
     the circular pattern with the most complex internal chord lines.
     Tracing the arrow's outline within those chords reveals the match. → C.

Q24 C  Question figure: inverted T (cross) shape inside a rectangle.
     The T's perpendicular line structure (one horizontal + one vertical)
     is traceable within option (c)'s line arrangement. → C.

Q25 A  Question figure: square with upper-right corner notched
     (creating an L-shape — 3/4 of a square).
     Option (a) shows a 2×2 grid of 4 equal cells.
     The L-shape outline can be traced exactly along the grid lines
     of 3 of those 4 cells (omitting the top-right cell). → A.

Q26 B  Question figure: letter-F shape (vertical bar on left +
     horizontal bar at top + horizontal bar at middle).
     The F's three perpendicular line segments are embedded within
     option (b)'s diagonal pattern — the vertical and horizontal
     elements of F appear as part of the combined line structure. → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Non-Verbal"

QUESTIONS = [

    # ── Q23 ──────────────────────────────────────────────────────────────────
    # Embedded figure. Question: angular kite/arrow shape.
    # Hidden in circular pattern with complex internal chord lines. → C.
    {
        "question_number": 23,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In following questions from the given answer figures, "
            "select the one in which the question figure is hidden/embedded."
        ),
        "question_hi": (
            "दिए गए उत्तर आकृतियों में से, उस उत्तर आकृति का चयन करें "
            "जिसमें प्रश्न आकृति छिपी/अंतिनिहित है।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "C",
        # Angular kite/arrow shape's straight edges appear as chords in the
        # most complex circular chord-line pattern of option (c). → C.
    },

    # ── Q24 ──────────────────────────────────────────────────────────────────
    # Embedded figure. Question: inverted T / cross shape inside a rectangle.
    # Hidden in option (c)'s line arrangement. → C.
    {
        "question_number": 24,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In following questions from the given answer figures, "
            "select the one in which the question figure is hidden/embedded."
        ),
        "question_hi": (
            "दिए गए उत्तर आकृतियों में से, उस उत्तर आकृति का चयन करें "
            "जिसमें प्रश्न आकृति छिपी/अंतिनिहित है।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "C",
        # Inverted T's horizontal + vertical line structure is traceable
        # within option (c)'s line arrangement. → C.
    },

    # ── Q25 ──────────────────────────────────────────────────────────────────
    # Embedded figure. Question: square with upper-right corner notched (L-shape).
    # L-shape outline traceable in 2×2 grid of option (a). → A.
    {
        "question_number": 25,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In following questions from the given answer figures, "
            "select the one in which the question figure is hidden/embedded."
        ),
        "question_hi": (
            "दिए गए उत्तर आकृतियों में से, उस उत्तर आकृति का चयन करें "
            "जिसमें प्रश्न आकृति छिपी/अंतिनिहित है।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "A",
        # L-shape (square with upper-right corner notched = 3 cells of a 2×2 grid).
        # Outline traced exactly along the grid lines of option (a)'s 2×2 grid
        # (omitting the top-right cell). → A.
    },

    # ── Q26 ──────────────────────────────────────────────────────────────────
    # Embedded figure. Question: letter-F shape.
    # F's three line segments embedded in option (b)'s diagonal pattern. → B.
    {
        "question_number": 26,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Select the answer figure in which the question figure is "
            "hidden/embedded."
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
        # Letter F: vertical bar (left) + horizontal bar (top) + horizontal
        # bar (middle). These three perpendicular segments are embedded within
        # option (b)'s diagonal and straight-line pattern. → B.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Non-Verbal Q23–Q26 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload non_verbal_23.png … non_verbal_26.png to Supabase bucket "
                "'question_image_Non_Verbal', then run:\n"
                "  python update_non_verbal_image_urls_batch6.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
