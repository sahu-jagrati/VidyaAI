"""
seed_reasoning_non_verbal_sheet5.py
========================================
Seeds Reasoning → Non-Verbal  Q19, Q21, Q22.

(Q18 and Q20 not yet provided — gaps intentional.)

Question types:
  Q19  = Paper folding & punching (triangular paper)
  Q21  = Embedded / Hidden figures (find question figure inside answer figure)
  Q22  = Embedded / Hidden figures

NOTE: image_url = None; upload images to Supabase and run
      update_non_verbal_image_urls_batch5.py.

Bucket  : question_image_Non_Verbal
Pattern : non_verbal_{N}.png

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q19 B  Triangular (equilateral) paper folded once along its vertical
     median (right half onto left half) → small circular punch near
     the top-right corner of the folded right-triangle shape.
     When unfolded: punch appears at original position AND its mirror
     → 2 holes symmetric about the fold axis.
     Option (b) shows the correct symmetric hole pattern. → B.

Q21 B  Question figure: 3D rectangular cuboid (perspective view).
     The cuboid's outline — front rectangle + back rectangle +
     connecting diagonals — is embedded in the complex crossed-diagonal
     grid of option (b). → B.

Q22 A  Question figure: right-angled / equilateral triangle with a
     small upward-pointing triangle (flag / pennant shape) inside it.
     This compound shape is embedded within the larger triangle
     subdivided into smaller triangles shown in option (a). → A.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Non-Verbal"

QUESTIONS = [

    # ── Q19 ──────────────────────────────────────────────────────────────────
    # Triangular paper. Folded once along vertical median → punch near top.
    # Unfolded: 2 symmetric holes. → B.
    {
        "question_number": 19,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "A piece of paper is folded and punched as shown below. "
            "From the given Answer Figures indicate how it will appear when opened."
        ),
        "question_hi": (
            "कागज के एक टुकड़े को नीचे दिखाए अनुसार मोड़कर छेद किया जाता "
            "है। दिए गए उत्तर आकृतियों से पता चलता है कि खोलने पर यह कैसा "
            "दिखाई देगा।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Equilateral triangle folded once (vertical median) → punch near top-right
        # corner → 2 symmetric holes when unfolded; option (b) shows this. → B.
    },

    # ── Q21 ──────────────────────────────────────────────────────────────────
    # Embedded figure. Question figure: 3D rectangular cuboid (perspective).
    # Hidden in complex crossed-diagonal grid of option (b). → B.
    {
        "question_number": 21,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "From the given answer figures, select the one in which the "
            "question figure is hidden/embedded."
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
        "correct_answer": "B",
        # 3D cuboid outline (front rect + back rect + diagonals) embedded
        # in the crossed-diagonal grid pattern of option (b). → B.
    },

    # ── Q22 ──────────────────────────────────────────────────────────────────
    # Embedded figure. Question figure: triangle with small inner triangle
    # (flag/pennant shape). Hidden in subdivided large triangle of option (a). → A.
    {
        "question_number": 22,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "From the given answer figures, select the one in which the "
            "question figure is hidden/embedded."
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
        # Triangle with small upward-pointing inner triangle (pennant) embedded
        # in the larger triangle subdivided into smaller triangles of option (a). → A.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Non-Verbal Q19, Q21, Q22 into '{TOPIC}' / '{SUBJECT}'")
        print("(Q18 and Q20 are gaps — not provided yet)")

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
                "\n  Upload non_verbal_19.png, non_verbal_21.png, non_verbal_22.png "
                "to Supabase bucket 'question_image_Non_Verbal', then run:\n"
                "  python update_non_verbal_image_urls_batch5.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
