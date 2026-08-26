"""
update_counting_figures_image_urls.py
======================================
Sets image_url for Counting Figures Q1–Q7 using the images uploaded to
Supabase Storage bucket: question_image_Counting_figure

Run from backend/ directory:
    python update_counting_figures_image_urls.py
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

# Q_NUMBER → image filename
IMAGE_MAP = {
    1: "figure_1.png",
    2: "figure_2.png",
    3: "figure_3.png",
    4: "figure_4.png",
    5: "figure_5.png",
    6: "figure_6.png",
    7: "figure_7.png",
}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    updated = not_found = 0
    try:
        for qnum, filename in IMAGE_MAP.items():
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
