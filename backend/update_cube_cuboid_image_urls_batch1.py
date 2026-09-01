"""
update_cube_cuboid_image_urls_batch1.py
=========================================
Sets image_url for Cube & Cuboid Q1–Q4.

Bucket : TBD — set BASE_URL below once the Supabase bucket is created.
Pattern: cube_{N}.png
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT  = "Reasoning"
TOPIC    = "Cube & Cuboid"

# ── UPDATE THIS once the Supabase bucket is confirmed ──────────────────────
BASE_URL = (
    "https://mlzcmlopkddsdwcmiujq.supabase.co"
    "/storage/v1/object/public/question_image_Cube_Cuboid"
)
# ───────────────────────────────────────────────────────────────────────────

IMAGE_MAP = {
    1: "cube_1.png",
    2: "cube_2.png",
    3: "cube_3.png",
    4: "cube_4.png",
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
