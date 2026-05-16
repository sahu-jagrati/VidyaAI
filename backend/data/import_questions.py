"""
Import questions from data/questions.csv into the database.

Usage (from backend/ directory):
    python -m data.import_questions

Run AFTER:  python -m app.database.init_db
"""

import csv
import sys
import os

# Make sure app/ is on the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database.connection import SessionLocal
from app.models.question_model import Question


CSV_PATH = os.path.join(os.path.dirname(__file__), "questions.csv")


def import_questions():
    db = SessionLocal()

    existing = db.query(Question).count()
    if existing > 0:
        print(f"⚠️  Database already has {existing} questions.")
        ans = input("Re-import and replace all? (yes/no): ").strip().lower()
        if ans != "yes":
            print("Aborted.")
            db.close()
            return
        db.query(Question).delete()
        db.commit()
        print("🗑️  Cleared existing questions.")

    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            q = Question(
                subject        = row["subject"].strip(),
                subject_code   = row["subject_code"].strip(),
                topic          = row["topic"].strip() or None,
                difficulty     = row["difficulty"].strip().lower(),
                phase          = row["phase"].strip().lower(),
                question_text  = row["question_text"].strip(),
                option_a       = row["option_a"].strip(),
                option_b       = row["option_b"].strip(),
                option_c       = row["option_c"].strip(),
                option_d       = row["option_d"].strip(),
                correct_answer = row["correct_answer"].strip().upper(),
                explanation    = row["explanation"].strip(),
            )
            db.add(q)
            count += 1

    db.commit()
    db.close()
    print(f"✅ Imported {count} questions successfully.")


if __name__ == "__main__":
    import_questions()
