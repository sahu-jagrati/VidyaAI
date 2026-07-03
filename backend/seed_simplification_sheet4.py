"""
seed_simplification_sheet4.py
==============================
Seeds questions 28–35 (Simplification — perfect squares / square roots)
from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Simplification
Q31 skipped — not visible in image.
Run     : python seed_simplification_sheet4.py

Answer key verification:
  Q28: 102²=10404; x=10424−10404=20=4×5; multiply by 5 → 100=10² (perfect sq) → C
  Q29: aabb=121(9a+1); 9a+1=64 → a=7,b=4; a−b=3                              → A
  Q30: xxyxx=11011x+100y; x=4,y=9 → 44944=212²; 4+9+4×9=49                   → A
  Q32: 27.12²=735.4944                                                          → A
  Q33: √645.8≈25.413 ≈ 25.41 (CISF HCM 2023)                                  → C
  Q34: √1354.24=36.8 (rational); others are irrational                         → C
  Q35: √304704=552 (rational); others are irrational                           → A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Simplification_Sheet4"
SUBJECT = "Quant"
TOPIC   = "Simplification"

QUESTIONS = [
    # Q28
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": "Let x be the least number which when subtracted from 10424 gives a perfect square number. What is the least number by which x should be multiplied to get a perfect square?",
        "question_hi": "मान x वह छोटी से छोटी संख्या है, जिसे 10424 में से घटाने पर एक पूर्ण वर्ग संख्या प्राप्त होती है। वह छोटी से छोटी संख्या ज्ञात करें, जिसे x से गुणा करते पर पूर्ण वर्ग संख्या प्राप्त हो।",
        "option_a": "3",
        "option_b": "6",
        "option_c": "5",
        "option_d": "2",
        "correct_answer": "C",
    },
    # Q29
    {
        "question_number": 29,
        "difficulty": "medium",
        "question_en": "A 4-digit number of the form aabb is a perfect square. What is the value of a − b?",
        "question_hi": "4-अंकीय संख्या aabb एक पूर्ण वर्ग है। a − b का मान क्या है?",
        "option_a": "3",
        "option_b": "2",
        "option_c": "4",
        "option_d": "1",
        "correct_answer": "A",
    },
    # Q30
    {
        "question_number": 30,
        "difficulty": "hard",
        "question_en": "If a 5-digit number in the form xxyxx is a perfect square, then find the value of x + y + x × y.",
        "question_hi": "यदि xxyxx रूप में 5 अंकों की संख्या एक पूर्ण वर्ग है, तो x + y + x × y का मान ज्ञात कीजिए।",
        "option_a": "49",
        "option_b": "51",
        "option_c": "48",
        "option_d": "50",
        "correct_answer": "A",
    },
    # Q32
    {
        "question_number": 32,
        "difficulty": "easy",
        "question_en": "What is the square root of 735.4944?",
        "question_hi": "735.4944 का वर्गमूल क्या है?",
        "option_a": "27.12",
        "option_b": "32.12",
        "option_c": "37.14",
        "option_d": "29.14",
        "correct_answer": "A",
    },
    # Q33 — CISF HCM 2023
    {
        "question_number": 33,
        "difficulty": "easy",
        "question_en": "Find the square root of 645.8 correct to two decimal places. (CISF HCM 2023)",
        "question_hi": "645.8 का वर्गमूल दो दशमलव स्थानों तक ज्ञात कीजिए। (CISF HCM 2023)",
        "option_a": "26.08",
        "option_b": "25.84",
        "option_c": "25.41",
        "option_d": "26.40",
        "correct_answer": "C",
    },
    # Q34
    {
        "question_number": 34,
        "difficulty": "medium",
        "question_en": "The square root of which of the following is a rational number?",
        "question_hi": "निम्नलिखित में से किसका वर्गमूल एक परिमेय संख्या है?",
        "option_a": "6250.49",
        "option_b": "1250.49",
        "option_c": "1354.24",
        "option_d": "5768.28",
        "correct_answer": "C",
    },
    # Q35
    {
        "question_number": 35,
        "difficulty": "medium",
        "question_en": "The square root of which of the following is a rational number?",
        "question_hi": "निम्नलिखित में से किसका वर्गमूल एक परिमेय संख्या है?",
        "option_a": "304704",
        "option_b": "524.176",
        "option_c": "344.96",
        "option_d": "19.4482",
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
