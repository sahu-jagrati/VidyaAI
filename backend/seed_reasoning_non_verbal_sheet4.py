"""
seed_reasoning_non_verbal_sheet4.py
========================================
Seeds Reasoning → Non-Verbal  Q14–Q17.

All questions are paper folding & punching type.

NOTE: image_url = None; upload images to Supabase and run
      update_non_verbal_image_urls_batch4.py.

Bucket  : question_image_Non_Verbal
Pattern : non_verbal_{N}.png

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q14 B  Square paper with circle. Paper folded in half (single fold).
     2 rectangular punch holes punched. When unfolded, 4 small squares
     appear symmetrically inside the circle. Option (b) shows this. → B.

Q15 B  Triangular paper (equilateral). Folded along its median twice
     to form a smaller triangle. 1 hole punched near corner. When
     unfolded, holes appear symmetrically in the lower region of the
     triangle. Option (b) shows the correct symmetric arrangement. → B.

Q16 B  Square paper. Folded diagonally (top-right corner to bottom-left).
     2 holes punched at specific positions on the folded triangle.
     When unfolded, holes appear at their positions and mirror positions
     along the diagonal fold line. Option (b) shows the correct pattern. → B.

Q17 A  Paper (circular shape / divided into sections) folded into
     quarters. A cross/compass-shaped punch mark in the center of the
     folded quarter. When fully unfolded, the compass cross (arrows
     pointing ↑↓←→) appears at the center. Option (a) matches. → A.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Non-Verbal"

QUESTIONS = [

    # ── Q14 ──────────────────────────────────────────────────────────────────
    # Square paper with circle. Single fold → 2 rectangular punches.
    # Unfolded: 4 squares symmetrically arranged inside circle. → B.
    {
        "question_number": 14,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "A piece of paper is folded and punched as shown below. "
            "From the given responses indicate how it will appear when opened."
        ),
        "question_hi": (
            "कागज के एक टुकड़े को नीचे दिखाए अनुसार मोड़कर छेद किया जाता "
            "है। दिए गए उत्तरों से पता चलता है कि खोलने पर यह कैसा दिखाई "
            "देगा।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Square paper with large circle; folded in half → 2 rectangular punches.
        # Unfolded: 4 small squares symmetrically inside the circle. → B.
    },

    # ── Q15 ──────────────────────────────────────────────────────────────────
    # Triangular paper. Folded twice → hole punched. Symmetric holes on unfold.
    {
        "question_number": 15,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "A triangular piece of paper is folded and punched as shown below. "
            "From the given responses indicate how it will appear when opened."
        ),
        "question_hi": (
            "कागज के एक त्रिकोणीय टुकड़े को नीचे दिखाए अनुसार मोड़कर छेद "
            "किया जाता है। दिए गए उत्तरों से पता चलता है कि खोलने पर यह "
            "कैसा दिखाई देगा।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Equilateral triangle folded twice → hole punched near corner.
        # Unfolded: holes appear symmetrically in lower region. → B.
    },

    # ── Q16 ──────────────────────────────────────────────────────────────────
    # Square paper. Diagonal fold (top-right → bottom-left). 2 holes punched.
    # Unfolded: holes + mirror holes along diagonal. → B.
    {
        "question_number": 16,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "A piece of paper is folded and punched as shown below. "
            "From the given Answer Figures indicate how it will appear when opened."
        ),
        "question_hi": (
            "कागज के एक टुकड़े को मोड़कर छेद किया जाता है जैसा कि नीचे "
            "दिए गए चित्र में दिखाया गया है। दिए गए आंकड़े दर्शाते हैं कि "
            "खोलने पर यह कैसा दिखाई देगा।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Square folded diagonally → 2 holes punched → mirror positions along
        # diagonal fold line appear when unfolded. → B.
    },

    # ── Q17 ──────────────────────────────────────────────────────────────────
    # Circular/quarter-folded paper. Cross/compass punch in center.
    # Unfolded: compass cross (↑↓←→ arrows) at center. → A.
    {
        "question_number": 17,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "A piece of paper is folded and punched as shown below. "
            "From the given Answer Figures indicate how it will appear when opened."
        ),
        "question_hi": (
            "कागज के एक टुकड़े को नीचे दिखाए अनुसार मोड़कर छेद किया जाता "
            "है। दिए गए उत्तर से आंकड़े दर्शाते हैं कि खोलने पर यह कैसा "
            "दिखाई देगा।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "A",
        # Paper folded into quarters (circular sections); compass/cross punch
        # in folded center → compass cross (↑↓←→) appears at center when
        # fully unfolded. Option (a) shows this. → A.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Non-Verbal Q14–Q17 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload non_verbal_14.png … non_verbal_17.png to Supabase bucket "
                "'question_image_Non_Verbal', then run:\n"
                "  python update_non_verbal_image_urls_batch4.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
