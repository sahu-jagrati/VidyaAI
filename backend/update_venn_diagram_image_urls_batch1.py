"""
update_venn_diagram_image_urls_batch1.py
=========================================
Sets image_url for Venn Diagram Q1–Q9 after images are uploaded to Supabase.

Expected Supabase bucket:  question_image_venn_diagram
Expected filename pattern: venn_{N}.png   (e.g. venn_1.png … venn_9.png)

Upload your images to:
  https://app.supabase.com → Storage → question_image_venn_diagram bucket

Then run this script.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT  = "Reasoning"
TOPIC    = "Venn Diagram"
BASE_URL = (
    "https://mlzcmlopkddsdwcmiujq.supabase.co"
    "/storage/v1/object/public/question_image_Venn_Diagram"
)

IMAGE_MAP = {
    1:  "venn_1.png",
    2:  "venn_2.png",
    3:  "venn_3.png",
    4:  "venn_4.png",
    5:  "venn_5.png",
    6:  "venn_6.png",
    7:  "venn_7.png",
    8:  "venn_8.png",
    9:  "venn_9.png",
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
