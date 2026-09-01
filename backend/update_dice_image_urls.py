"""
update_dice_image_urls.py
=========================
Sets image_url for Dice questions that have images uploaded to Supabase Storage.
Bucket: question_image_dice
Pattern: dice_{N}.png

Run from backend/ directory:
    python update_dice_image_urls.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT  = "Reasoning"
TOPIC    = "Dice"
BASE_URL = (
    "https://mlzcmlopkddsdwcmiujq.supabase.co"
    "/storage/v1/object/public/question_image_dice"
)

# question_number → filename  (only those confirmed uploaded)
IMAGE_MAP = {
    3:  "dice_3.png",
    4:  "dice_4.png",
    6:  "dice_6.png",
    7:  "dice_7.png",
    8:  "dice_8.png",
    9:  "dice_9.png",
    10: "dice_10.png",
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
        print(
            f"\nDone — updated: {updated}, "
            f"already set: {skipped}, "
            f"not found: {not_found}"
        )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
