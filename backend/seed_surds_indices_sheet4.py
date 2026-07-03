"""
seed_surds_indices_sheet4.py
============================
Seeds questions 25–30 (Surds & Indices) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Surds & Indices
Run     : python seed_surds_indices_sheet4.py

Answer key verification:
  Q25: √(55+12√21)=3√3+2√7; (2√7-3√3)(3√3+2√7)=28-27=1; ²⁰²¹√1=1       → B
  Q26: (a+b√3)^2=52+30√3 → a^2+3b^2=52, ab=15 → a=5,b=3; a+b=8           → C
  Q27: a^2+2b^2=86, ab=30 → a=6,b=5; √(a^2+b^2)=√61≈7.81≈7.8             → B
  Q28: √(97+56√3)=7+4√3; ⁴√x=(2+√3); 1/⁴√x=(2-√3); sum=4                → D
  Q29: (-3+√20)^2=29-12√5 (positive root); a=-3,b=1,n=20; -3+1+20=18      → C
  Q30: √(10-2√21)=√7-√3; √(8+2√15)=√5+√3; sum=√7+√5 → √(7×5)=√35≈5.9   → A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Surds_Indices_Sheet4"
SUBJECT = "Quant"
TOPIC   = "Surds & Indices"

QUESTIONS = [
    # Q25
    {
        "question_number": 25,
        "difficulty": "hard",
        "question_en": "Find the value of ²⁰²¹√((2√7 - 3√3)√(55 + 12√21))?",
        "question_hi": "²⁰²¹√((2√7 - 3√3)√(55 + 12√21)) का मान ज्ञात कीजिए?",
        "option_a": "-1",
        "option_b": "1",
        "option_c": "0",
        "option_d": "2",
        "correct_answer": "B",
    },
    # Q26 — CAT 2024
    {
        "question_number": 26,
        "difficulty": "medium",
        "question_en": "If (a + b√3)^2 = 52 + 30√3, where a and b are natural numbers, then a + b equals? (CAT 2024)",
        "question_hi": "यदि (a + b√3)^2 = 52 + 30√3 है, जहाँ a और b प्राकृतिक संख्याएं हैं, तो a + b बराबर है? (CAT 2024)",
        "option_a": "9",
        "option_b": "7",
        "option_c": "8",
        "option_d": "10",
        "correct_answer": "C",
    },
    # Q27
    {
        "question_number": 27,
        "difficulty": "medium",
        "question_en": "If √(86 - 60√2) = a - b√2, then what will be the value of √(a^2 + b^2), correct to one decimal place?",
        "question_hi": "यदि √(86 - 60√2) = a - b√2 है, तो √(a^2 + b^2) का मान क्या होगा, एक दशमलव स्थान पर सही मान होगा?",
        "option_a": "8.4",
        "option_b": "7.8",
        "option_c": "8.2",
        "option_d": "7.2",
        "correct_answer": "B",
    },
    # Q28 — CDS 2023
    {
        "question_number": 28,
        "difficulty": "hard",
        "question_en": "If x = 97 + 56√3, then what is the value of ⁴√x + 1/⁴√x? (CDS 2023)",
        "question_hi": "यदि x = 97 + 56√3 है, तो ⁴√x + 1/⁴√x का मान क्या है? (CDS 2023)",
        "option_a": "7",
        "option_b": "6",
        "option_c": "5",
        "option_d": "4",
        "correct_answer": "D",
    },
    # Q29 — CAT 2024
    {
        "question_number": 29,
        "difficulty": "hard",
        "question_en": "If (a + b√n) is the positive square root of (29 - 12√5), where a and b are integers, and n is a natural number, then the maximum possible value of (a + b + n) is? (CAT 2024)",
        "question_hi": "यदि (a + b√n), (29 - 12√5) का धनात्मक वर्गमूल है, जहाँ a और b पूर्णांक हैं, और n एक प्राकृतिक संख्या है, तो (a + b + n) का अधिकतम संभव मान है? (CAT 2024)",
        "option_a": "4",
        "option_b": "6",
        "option_c": "18",
        "option_d": "22",
        "correct_answer": "C",
    },
    # Q30
    {
        "question_number": 30,
        "difficulty": "medium",
        "question_en": "If √(10 - 2√21) + √(8 + 2√15) = √a + √b, where a and b are positive integers, then the value of √(ab) is closest to:",
        "question_hi": "यदि √(10 - 2√21) + √(8 + 2√15) = √a + √b है, जहाँ a और b धनात्मक पूर्णांक हैं, तो √(ab) का मान निकटतम है:",
        "option_a": "5.9",
        "option_b": "6.8",
        "option_c": "4.6",
        "option_d": "7.2",
        "correct_answer": "A",
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
