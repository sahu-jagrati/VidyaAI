"""
update_counting_figures_image_urls_batch3.py
=============================================
Sets image_url for Counting Figures Q52–Q57 (and their sub-question rows).

Upload filenames expected in Supabase Storage bucket
    question_image_Counting_figure:
        figure_52.png
        figure_53.png   (shared by Q53, Q5302, Q5303)
        figure_54.png   (shared by Q54, Q5402)
        figure_55.png   (shared by Q55, Q5502)
        figure_56.png
        figure_57.png   (shared by Q57, Q5702)

Run from backend/ directory:
    python update_counting_figures_image_urls_batch3.py
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

# Map each DB question_number to its image filename
# Sub-questions share the same figure as the parent question
IMAGE_MAP = {
    52:   "figure_52.png",
    53:   "figure_53.png",
    5302: "figure_53.png",
    5303: "figure_53.png",
    54:   "figure_54.png",
    5402: "figure_54.png",
    55:   "figure_55.png",
    5502: "figure_55.png",
    56:   "figure_56.png",
    57:   "figure_57.png",
    5702: "figure_57.png",
}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    updated = not_found = 0
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
            row.image_url = url
            updated += 1
            print(f"  UPDATED  Q{qnum}  →  {filename}")

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
