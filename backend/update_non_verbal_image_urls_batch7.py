"""
update_non_verbal_image_urls_batch7.py
=========================================
Sets image_url for Non-Verbal Q28, Q30, Q31, Q32, Q33.
Bucket : question_image_Non_Verbal
Pattern: non_verbal_{N}.png

Run after uploading non_verbal_28.png, non_verbal_30.png – non_verbal_33.png
to Supabase.
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

IMAGE_MAP = {
    28: "non_verbal_28.png",
    30: "non_verbal_30.png",
    31: "non_verbal_31.png",
    32: "non_verbal_32.png",
    33: "non_verbal_33.png",
}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    updated = skipped = not_found = 0
    try:
        for qnum, filename in sorted(IMAGE_MAP.items()):
            url = f"{BASE_URL}/{filename}"
            row = (
                db.query(Question)
                .filter(
                    Question.subject         == SUBJECT,
                    Question.topic           == TOPIC,
                    Question.question_number == qnum,
                )
                .first()
            )
            if row is None:
                print(f"  NOT FOUND  Q{qnum}")
                not_found += 1
                continue
            if row.image_url == url:
                print(f"  SKIP (already set)  Q{qnum}")
                skipped += 1
                continue
            row.image_url = url
            updated += 1
            print(f"  UPDATED  Q{qnum}  →  {filename}")

        db.commit()
        print(f"\nDone — updated: {updated}, skipped: {skipped}, not found: {not_found}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
