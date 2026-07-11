"""
seed_reasoning_blood_relation_sheet1.py
========================================
Seeds questions 1-8 (Blood Relation) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Blood Relation
Run     : python seed_reasoning_blood_relation_sheet1.py

Answer key verification:
  Q1: A is B's daughter, B is C's mother, D is C's brother -> D is A's brother       -> C
  Q2: P-Q brother, R=Q's mother, S=R's father, T=S's mother -> P is T's great-grandson -> B
  Q3: A is B's sister, B is C's brother, C is D's son -> D is A's mother             -> A
  Q4: B is A's brother, A's only sister is C's mother, D is C's maternal grandmother -> A is D's daughter -> B
  Q5: E is B's sister, A is C's father, B is C's son -> A is E's grandfather         -> A
  Q6: A is B's brother, C is A's mother, D is C's father -> D is A's grandfather     -> C
  Q7: A is B's mother, C is A's son, E is B's daughter, D is E's brother -> A is D's grandmother -> A
  Q8: A is B's sister, C is B's mother, D is C's father -> A is D's granddaughter    -> D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401 — registers Subscription with SQLAlchemy

SOURCE  = "Gagan_Pratap_Reasoning_Blood_Relation_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Blood Relation"

QUESTIONS = [
    # Q1
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": "A is B's daughter. B is C's mother. D is C's brother. How is D related to A?",
        "question_hi": "A, B की बेटी है। B, C की माँ है। D, C का भाई है। D, A से कैसे संबंधित है?",
        "option_a": "Father/पिता",
        "option_b": "Grandfather/दादा",
        "option_c": "Brother/भाई",
        "option_d": "Son/पुत्र",
        "correct_answer": "C",
    },
    # Q2
    {
        "question_number": 2,
        "difficulty": "medium",
        "question_en": "P is Q's brother. R is Q's mother. S is R's father. T is S's mother. How is P related to T?",
        "question_hi": "P, Q का भाई है। R, Q की माँ है। S, R का पिता है। T, S की माँ है। P, T से कैसे संबंधित है?",
        "option_a": "Granddaughter/पोती",
        "option_b": "Great grandson/परपोता",
        "option_c": "Grandson/पोता",
        "option_d": "Grandmother/दादी",
        "correct_answer": "B",
    },
    # Q3
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": "A is the sister of B. B is the brother of C. C is the son of D. How is D related to A?",
        "question_hi": "A, B की बहन है। B, C का भाई है। C, D का पुत्र है। D, A से कैसे संबंधित है?",
        "option_a": "Mother/माँ",
        "option_b": "Daughter/बेटी",
        "option_c": "Son/बेटा",
        "option_d": "Uncle/चाचा",
        "correct_answer": "A",
    },
    # Q4
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": "B is the brother of A, whose only sister is mother of C. D is maternal grandmother of C. How is A related to D?",
        "question_hi": "B, A का भाई है, जिसकी एकमात्र बहन C की माँ है। D, C की नानी है। A, D से कैसे संबंधित है?",
        "option_a": "Daughter-in-law/पुत्रवधू",
        "option_b": "Daughter/बेटी",
        "option_c": "Aunt/चाची",
        "option_d": "Nephew/भतीजा",
        "correct_answer": "B",
    },
    # Q5
    {
        "question_number": 5,
        "difficulty": "easy",
        "question_en": "E is the sister of B. A is the father of C. B is the son of C. How is A related to E?",
        "question_hi": "E, B की बहन है। A, C का पिता है। B, C का पुत्र है। A, E से कैसे संबंधित है?",
        "option_a": "Grandfather/दादा",
        "option_b": "Granddaughter/पोती",
        "option_c": "Father/पिता",
        "option_d": "Great-grandfather/परदादा",
        "correct_answer": "A",
    },
    # Q6
    {
        "question_number": 6,
        "difficulty": "easy",
        "question_en": "A is B's brother. C is A's mother. D is C's father. E is B's son. How is D related to A?",
        "question_hi": "A, B का भाई है। C, A की माँ है। D, C का पिता है। E, B का पुत्र है। D, A से कैसे संबंधित है?",
        "option_a": "Son/पुत्र",
        "option_b": "Grandson/पोता",
        "option_c": "Grandfather/नाना",
        "option_d": "Great Grandfather/परदादा",
        "correct_answer": "C",
    },
    # Q7
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": "A is the mother of B. C is the son of A. D is the brother of E. E is the daughter of B. Who is the grandmother of D?",
        "question_hi": "A, B की माँ है। C, A का पुत्र है। D, E का भाई है। E, B की बेटी है। D की दादी कौन है?",
        "option_a": "A",
        "option_b": "B",
        "option_c": "C",
        "option_d": "D",
        "correct_answer": "A",
    },
    # Q8
    {
        "question_number": 8,
        "difficulty": "easy",
        "question_en": "A is B's sister. C is B's mother. D is C's father. E is D's mother. Then how is A related to D?",
        "question_hi": "A, B की बहन है। C, B की माँ है। D, C का पिता है। E, D की माँ है। तो A, D से कैसे संबंधित है?",
        "option_a": "Grandfather/दादा",
        "option_b": "Daughter/बेटी",
        "option_c": "Grandmother/दादी",
        "option_d": "Grand daughter/नातिन",
        "correct_answer": "D",
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        existing_short = {
            row[0][:80]
            for row in db.query(Question.question_en)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        for d in QUESTIONS:
            if d["question_en"][:80] in existing_short:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue

            db.add(Question(
                subject    = SUBJECT,
                topic      = TOPIC,
                source_pdf = SOURCE,
                **d,
            ))
            inserted += 1

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
