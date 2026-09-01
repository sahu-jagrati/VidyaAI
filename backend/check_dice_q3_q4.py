"""Check current Q3 and Q4 content in Dice topic"""
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
        Question.topic == "Dice",
        Question.question_number.in_([3, 4])
    ).order_by(Question.question_number).all()
    for r in rows:
        print(f"Q{r.question_number} (id={r.id})")
        print(f"  source : {r.source_pdf}")
        print(f"  en     : {r.question_en[:120]}")
        print(f"  opt_a  : {r.option_a}")
        print(f"  opt_b  : {r.option_b}")
        print(f"  opt_c  : {r.option_c}")
        print(f"  opt_d  : {r.option_d}")
        print(f"  answer : {r.correct_answer}")
        print(f"  img    : {r.image_url}")
        print()
    db.close()

if __name__ == "__main__":
    main()
