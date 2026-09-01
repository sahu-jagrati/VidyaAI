"""
seed_reasoning_non_verbal_sheet2.py
========================================
Seeds Reasoning → Non-Verbal  Q5 and Q6.
(Q7 and Q8 images not yet provided — add separately.)

All questions are mirror-image (looking-glass) type.
Mirror line MN is a left-side vertical line (N at top, M at bottom)
→ left-right flip of the figure.

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_non_verbal_image_urls_batch2.py.

Bucket  : question_image_Non_Verbal
Pattern : non_verbal_{N}.png

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q5  B  Mirror at MN (left-side vertical; N=top, M=bottom).
     Original: decorative floral/vine design curling in one direction.
     Left-right reflection → vine/leaf curls to opposite side. → B.

Q6  B  Mirror at MN (left-side vertical; N=top).
     Original: geometric figure with diamond/kite shapes arranged.
     Left-right reflection → shapes appear on swapped sides. → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Non-Verbal"

QUESTIONS = [

    # ── Q5 ───────────────────────────────────────────────────────────────────
    # Floral/vine design. Mirror at MN (left-side vertical; N=top, M=bottom).
    # Left-right flip: vine/leaf curls to opposite direction. Answer: (b).
    {
        "question_number": 5,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "If a mirror is placed on the line MN, then which of the answer "
            "figures is the right image of the given figure?"
        ),
        "question_hi": (
            "यदि एक दर्पण को रेखा MN पर रखा जाए, तो दी गई उत्तर आकृतियों "
            "में से कौन सी आकृति का सही प्रतिबिम्ब है?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Left-side vertical mirror flips the floral/vine design left-right;
        # option (b) shows the correct mirror image.
    },

    # ── Q6 ───────────────────────────────────────────────────────────────────
    # Geometric diamond/kite shapes. Mirror at MN (left-side vertical; N=top).
    # Left-right flip: shapes swap sides. Answer: (b).
    {
        "question_number": 6,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "If a mirror is placed on the line MN, then which of the answer "
            "figures is the right image of the given question figure?"
        ),
        "question_hi": (
            "यदि एक दर्पण को रेखा MN पर रखा जाए, तो कौन सी उत्तर आकृति "
            "दी गई प्रश्न आकृति की सही छवि है?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Left-side vertical mirror flips the geometric diamond/kite pattern
        # left-right; option (b) shows the correct mirror image.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Non-Verbal Q5–Q6 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload non_verbal_5.png and non_verbal_6.png to Supabase bucket "
                "'question_image_Non_Verbal', then run:\n"
                "  python update_non_verbal_image_urls_batch2.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
