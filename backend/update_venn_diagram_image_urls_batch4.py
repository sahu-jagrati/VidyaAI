"""
update_venn_diagram_image_urls_batch4.py
=========================================
Sets image_url for Venn Diagram Q27–Q34.
Bucket: question_image_Venn_Diagram  |  Pattern: venn_{N}.png
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
    27: "venn_27.png",
    28: "venn_28.png",
    29: "venn_29.png",
    30: "venn_30.png",
    31: "venn_31.png",
    32: "venn_32.png",
    33: "venn_33.png",
    34: "venn_34.png",
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
