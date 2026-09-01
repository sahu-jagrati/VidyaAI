"""
update_non_verbal_image_urls_batch14.py
==========================================
Sets image_url for Non-Verbal Q83, Q84, Q85, Q86, Q88, Q89, Q90.
Bucket : question_image_Non_Verbal
Pattern: non_verbal_{N}.png

Run after uploading the images to Supabase.
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
    83: "non_verbal_83.png",
    84: "non_verbal_84.png",
    85: "non_verbal_85.png",
    86: "non_verbal_86.png",
    88: "non_verbal_88.png",
    89: "non_verbal_89.png",
    90: "non_verbal_90.png",
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
