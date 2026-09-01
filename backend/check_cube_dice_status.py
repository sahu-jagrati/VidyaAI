"""
check_cube_dice_status.py
=========================
Show current state of all Cube and Dice questions in DB.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    rows = db.query(Question).filter(
        Question.subject == "Reasoning",
        Question.topic == "Cube and Dice"
    ).order_by(Question.question_number).all()

    print(f"Total Cube and Dice questions: {len(rows)}")
    print()
    print(f"{'Q':>3} | {'img_url':5} | {'opt_img':7} | {'option_a':45} | {'option_b':45}")
    print("-" * 120)
    for r in rows:
        has_img = "Y" if r.image_url else "N"
        opts = [r.option_a, r.option_b, r.option_c, r.option_d]
        img_opts = sum(1 for o in opts if o and o.startswith("http"))
        oa = (r.option_a or "")[:44]
        ob = (r.option_b or "")[:44]
        print(f"Q{r.question_number:2d} | {has_img:5} | {img_opts:7} | {oa:45} | {ob}")

    print()
    print("Questions with image_url set:")
    for r in rows:
        if r.image_url:
            print(f"  Q{r.question_number}: {r.image_url}")

db.close() if False else None

if __name__ == "__main__":
    main()
