"""
update_counting_figures_image_urls_batch2.py
=============================================
Sets image_url for Counting Figures Q8–Q37 using images uploaded to
Supabase Storage bucket: question_image_Counting_figure

Assumes filenames: figure_8.png, figure_9.png, … figure_37.png

Run from backend/ directory:
    python update_counting_figures_image_urls_batch2.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Counting Figures"

BASE_URL = (
    "https://mlzcmlopkddsdwcmiujq.supabase.co"
    "/storage/v1/object/public/question_image_Counting_figure"
)

# Q_NUMBER → image filename  (Q1–Q7 already updated separately)
IMAGE_MAP = {q: f"figure_{q}.png" for q in range(8, 38)}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    updated = not_found = 0
    try:
        for qnum in sorted(IMAGE_MAP):
            filename = IMAGE_MAP[qnum]
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
            row.image_url = url
            updated += 1
            print(f"  UPDATED  Q{qnum}  →  {url}")

        db.commit()
        print(f"\nDone — updated: {updated}, not found: {not_found}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
