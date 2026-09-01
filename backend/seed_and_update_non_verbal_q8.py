"""
seed_and_update_non_verbal_q8.py
========================================
Seeds Non-Verbal Q8 and immediately sets its image URL.

⚠️  VERIFY the correct_answer below by looking at the uploaded image
    non_verbal_8.png and updating it if needed before running.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT  = "Reasoning"
TOPIC    = "Non-Verbal"
BASE_URL = (
    "https://mlzcmlopkddsdwcmiujq.supabase.co"
    "/storage/v1/object/public/question_image_Non_Verbal"
)

Q8 = {
    "question_number": 8,
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
    "image_url": f"{BASE_URL}/non_verbal_8.png",
    "option_a": "a",
    "option_b": "b",
    "option_c": "c",
    "option_d": "d",
    # ⚠️ Update this after visually verifying non_verbal_8.png
    "correct_answer": "B",
}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    try:
        exists = (
            db.query(Question)
            .filter(
                Question.subject == SUBJECT,
                Question.topic == TOPIC,
                Question.question_number == 8,
            )
            .first()
        )

        if exists:
            # Already seeded — just update image URL
            url = f"{BASE_URL}/non_verbal_8.png"
            if exists.image_url == url:
                print("  SKIP Q8: image_url already set")
            else:
                exists.image_url = url
                db.commit()
                print(f"  UPDATED Q8 image_url → non_verbal_8.png")
        else:
            db.add(Question(subject=SUBJECT, topic=TOPIC, **Q8))
            db.commit()
            print("  INSERT Q8 (with image_url set)")

        print("\nDone.")
        print("⚠️  Remember to verify correct_answer for Q8 by viewing non_verbal_8.png")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
