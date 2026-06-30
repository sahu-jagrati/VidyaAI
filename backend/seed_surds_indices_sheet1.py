"""
seed_surds_indices_sheet1.py
============================
Seeds questions 1–8 (Surds & Indices) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Surds & Indices
Run     : python seed_surds_indices_sheet1.py

Answer key verification:
  Q1: (0.04)^(-1.5) = (1/25)^(-3/2) = 25^(3/2) = 125                     → D
  Q2: 8^x/2^y = 2^(3x)/2^y = 2^(3x-y) = 2^12 = 4096                      → B
  Q3: 8^(3x-5)=32^(-(7-4x)) → 2^(9x-15)=2^(20x-35) → 11x=20 → x=20/11   → B
  Q4: 625^(2x-3)=25^(6x-12) → 5^(8x-12)=5^(12x-24) → x=3                 → B
  Q5: (x/y)^(5a-3)=(x/y)^(-(17-3a)) → 5a-3=3a-17 → 2a=-14 → a=-7        → C
  Q6: x^(x√x)=(x√x)^x → x^(3/2)=3x/2 → √x=3/2 → x=9/4                   → D
  Q7: x+y=2021 (odd) → one even, one odd → (-1)^x+(-1)^y=1+(-1)=0         → C
  Q8: x²=y^z → 2×0.27=z×0.15 → z=0.54/0.15=3.6 ≈ 3.33 (closest option)  → D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Surds_Indices_Sheet1"
SUBJECT = "Quant"
TOPIC   = "Surds & Indices"

QUESTIONS = [
    # Q1 — RRB ALP 2024
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": "The value of (0.04)^(-1.5) is? (RRB ALP 2024)",
        "question_hi": "(0.04)^(-1.5) का मान क्या है? (RRB ALP 2024)",
        "option_a": "25",
        "option_b": "250",
        "option_c": "625",
        "option_d": "125",
        "correct_answer": "D",
    },
    # Q2
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": "If 3x − y = 12, then find 8^x / 2^y?",
        "question_hi": "यदि 3x − y = 12 है, तो 8^x / 2^y ज्ञात कीजिये?",
        "option_a": "2021",
        "option_b": "4096",
        "option_c": "8192",
        "option_d": "2048",
        "correct_answer": "B",
    },
    # Q3
    {
        "question_number": 3,
        "difficulty": "medium",
        "question_en": "If 8^(3x−5) = 1/32^(7−4x), then x = ?",
        "question_hi": "यदि 8^(3x−5) = 1/32^(7−4x) है, तो x = ?",
        "option_a": "16/9",
        "option_b": "20/11",
        "option_c": "25/13",
        "option_d": "2",
        "correct_answer": "B",
    },
    # Q4 — UPSI exam 2011
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": "If 625^(2x−3) = 25^(6x−12), then x = ? (UPSI exam 2011)",
        "question_hi": "यदि 625^(2x−3) = 25^(6x−12) है, तो x = ? (UPSI exam 2011)",
        "option_a": "2",
        "option_b": "3",
        "option_c": "4",
        "option_d": "5",
        "correct_answer": "B",
    },
    # Q5
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": "If (x/y)^(5a−3) = (y/x)^(17−3a), what is the value of a?",
        "question_hi": "यदि (x/y)^(5a−3) = (y/x)^(17−3a) है, तो a का मान क्या है?",
        "option_a": "−6",
        "option_b": "−5",
        "option_c": "−7",
        "option_d": "−8",
        "correct_answer": "C",
    },
    # Q6
    {
        "question_number": 6,
        "difficulty": "hard",
        "question_en": "If x^(x√x) = (x√x)^x, then x equals?",
        "question_hi": "यदि x^(x√x) = (x√x)^x है, तो x बराबर है?",
        "option_a": "4/9",
        "option_b": "16/9",
        "option_c": "3/2",
        "option_d": "9/4",
        "correct_answer": "D",
    },
    # Q7
    {
        "question_number": 7,
        "difficulty": "easy",
        "question_en": "If x and y are natural numbers such that x + y = 2021, then what is the value of (-1)^x + (-1)^y?",
        "question_hi": "यदि x तथा y प्राकृतिक संख्याएं इस प्रकार हैं कि x + y = 2021 है, तो (-1)^x + (-1)^y का मान क्या होगा?",
        "option_a": "2",
        "option_b": "−2",
        "option_c": "0",
        "option_d": "1",
        "correct_answer": "C",
    },
    # Q8 — RRB RPF SI 2024
    {
        "question_number": 8,
        "difficulty": "hard",
        "question_en": "Given that 87^0.27 = x, 87^0.15 = y and x^2 = y^z, then the value of z is close to: (RRB RPF SI 2024)",
        "question_hi": "यह देखते हुए कि 87^0.27 = x, 87^0.15 = y और x^2 = y^z है, तो z का मान करीब है: (RRB RPF SI 2024)",
        "option_a": "5.77",
        "option_b": "2.15",
        "option_c": "3.16",
        "option_d": "3.33",
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
        print(f"\nDone — inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
