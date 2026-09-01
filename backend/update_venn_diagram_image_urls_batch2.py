"""
update_venn_diagram_image_urls_batch2.py
=========================================
Sets image_url for Venn Diagram Q11–Q12 and Q13–Q19.
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
    11: "venn_11.png",
    12: "venn_12.png",
    13: "venn_13.png",
    14: "venn_14.png",
    15: "venn_15.png",
    16: "venn_16.png",
    17: "venn_17.png",
    18: "venn_18.png",
    19: "venn_19.png",
}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    updated = skipped = not_found = 0
    try:
        for qnum, filename in sorted(IMAGE_MAP.items()):
            url = f"{BASE_URL}/{filename}"
            rows = (
                db.query(Question)
                .filter(
                    Question.subject         == SUBJECT,
                    Question.topic           == TOPIC,
                    Question.question_number == qnum,
                )
                .all()
            )
            if not rows:
                print(f"  NOT FOUND  Q{qnum}")
                not_found += 1
                continue
            for row in rows:
                if row.image_url == url:
                    print(f"  SKIP (already set)  Q{qnum}")
                    skipped += 1
                else:
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
