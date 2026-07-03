"""
seed_simplification_sheet3.py
==============================
Seeds questions 20–27 (Simplification — recurring decimals / squares)
from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Simplification
Q25 skipped — multi-part sub-question (no single answer)
Run     : python seed_simplification_sheet3.py

Answer key verification:
  Q20: 3.7̄6̄ − 1.4̄5̄7̄6̄ = 373/99 − 14563/9999 = 37373/9999 − 14563/9999 = 22810/9999 ≈ 2.3101... → B
  Q21: 22.4̄ + 11.56̄7̄ − 33.5̄9̄ = 202/9 + (11567-115)/999... = 0.41̄2̄                        → B
  Q22: 0.47 + 0.50̄3̄ − 0.39 × 0.8̄ = 47/100 + 498/990 − 39/100×8/9 ≈ 0.6̄2̄5̄              → C
  Q23: 0.xȳx + 0.zȳx = 164/99; number of possible values of y = 2                             → A
  Q24: 5625=75², 7225=85², 3625≠perfect square, 9025=95² → not square: 3625                   → C
  Q26: 147² = (150−3)² = 22500−900+9 = 21609                                                   → D
  Q27: 1801 × 1801 = (1800+1)² = 3240000+3600+1 = 3243601                                     → B
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Simplification_Sheet3"
SUBJECT = "Quant"
TOPIC   = "Simplification"

QUESTIONS = [
    # Q20
    {
        "question_number": 20,
        "difficulty": "hard",
        "question_en": "What is 3.7̄6̄ − 1.4̄5̄7̄6̄ equal to? (3.767676... − 1.457645764576...)",
        "question_hi": "3.7̄6̄ − 1.4̄5̄7̄6̄ किसके बराबर है?",
        "option_a": "2.3̄1̄0̄0̄1̄9̄1̄",
        "option_b": "2.3̄1̄0̄1̄0̄9̄1̄",
        "option_c": "2.3̄1̄1̄0̄0̄9̄1̄",
        "option_d": "2.3̄1̄1̄0̄9̄0̄1̄",
        "correct_answer": "B",
    },
    # Q21
    {
        "question_number": 21,
        "difficulty": "hard",
        "question_en": "The value of 22.4̄ + 11.56̄7̄ − 33.5̄9̄ is: (22.444... + 11.5676767... − 33.5959...)",
        "question_hi": "22.4̄ + 11.56̄7̄ − 33.5̄9̄ का मान है:",
        "option_a": "0.3̄2̄",
        "option_b": "0.41̄2̄",
        "option_c": "0.34",
        "option_d": "0.412",
        "correct_answer": "B",
    },
    # Q22
    {
        "question_number": 22,
        "difficulty": "hard",
        "question_en": "The value of 0.47 + 0.50̄3̄ − 0.39 × 0.8̄ is: (0.47 + 0.503303... − 0.39 × 0.888...)",
        "question_hi": "0.47 + 0.50̄3̄ − 0.39 × 0.8̄ का मान क्या है।",
        "option_a": "0.61̄5̄",
        "option_b": "0.6̄1̄5̄",
        "option_c": "0.6̄2̄5̄",
        "option_d": "0.62̄5̄",
        "correct_answer": "C",
    },
    # Q23
    {
        "question_number": 23,
        "difficulty": "hard",
        "question_en": "How many values of y are possible if 0.xȳx + 0.zȳx = 164/99? (where x, y, z are single digits)",
        "question_hi": "y के कितने मान संभव हैं यदि 0.xȳx + 0.zȳx = 164/99 है? (जहाँ x, y, z एकल अंक हैं)",
        "option_a": "2",
        "option_b": "3",
        "option_c": "4",
        "option_d": "5",
        "correct_answer": "A",
    },
    # Q24 — UP Constable 2018
    {
        "question_number": 24,
        "difficulty": "easy",
        "question_en": "Which of the following options is not a square number? (UP Constable 2018)",
        "question_hi": "निम्नलिखित में से कौन सा विकल्प एक वर्ग संख्या नहीं है? (UP Constable 2018)",
        "option_a": "5625",
        "option_b": "7225",
        "option_c": "3625",
        "option_d": "9025",
        "correct_answer": "C",
    },
    # Q26 — RRB RPF SI 2024
    {
        "question_number": 26,
        "difficulty": "easy",
        "question_en": "Evaluate 147²? (RRB RPF SI 2024)",
        "question_hi": "147² का मूल्यांकन करें? (RRB RPF SI 2024)",
        "option_a": "21629",
        "option_b": "21639",
        "option_c": "21669",
        "option_d": "21609",
        "correct_answer": "D",
    },
    # Q27
    {
        "question_number": 27,
        "difficulty": "easy",
        "question_en": "The value of 1801 × 1801 is:",
        "question_hi": "1801 × 1801 का मान ............... है।",
        "option_a": "3423601",
        "option_b": "3243601",
        "option_c": "2343601",
        "option_d": "3243106",
        "correct_answer": "B",
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
