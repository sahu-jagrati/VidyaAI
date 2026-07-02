"""
seed_surds_indices_sheet2.py
============================
Seeds questions 9–15 (Surds & Indices) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Surds & Indices
Run     : python seed_surds_indices_sheet2.py

Answer key verification:
  Q9:  Both equal (each simplifies by power-of-power rule)               → A
  Q10: 3^(x+y)=81→x+y=4; 81^(x-y)=3→x-y=1/4; x=17/8,y=15/8 → xy=255/64 → A
  Q11: (5/3)^(2x+2) × (5/3)^(-4x+4) = (5/3)^(-2) → -2x+6=-2 → x=4     → D
  Q12: (1/7)^-4+(1/9)^-4+(1/5)^-4 = 2401+6561+625 = 9587              → C
  Q13: (4096/9)^(-2/3) × (4/3)^5 + ⁴√(256^-3) = 1/36                   → C
  Q14: [(9261^(1/3)+81^(1/4))^2] × √1296; 9261^(1/3)=21,81^(1/4)=3     → D (294)
  Q15: Solve equation → x=-23/42 → 2-42x=25 → √25=5                    → A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Surds_Indices_Sheet2"
SUBJECT = "Quant"
TOPIC   = "Surds & Indices"

QUESTIONS = [
    # Q9 — MTS 2023
    {
        "question_number": 9,
        "difficulty": "medium",
        "question_en": "On comparing the following two numeric expressions [(2 7/9)^(2/3)]^3 and [(1 2/3)^5]^(3/5), we find that ________? (MTS 2023)",
        "question_hi": "निम्नलिखित दो संख्यात्मक व्यंजक [(2 7/9)^(2/3)]^3 और [(1 2/3)^5]^(3/5) की तुलना करने पर हम पाते हैं कि ________? (MTS 2023)",
        "option_a": "Both the expressions are equal",
        "option_b": "The first expression is smaller than the second",
        "option_c": "The first expression is larger than the second",
        "option_d": "The given two expressions cannot be compared",
        "correct_answer": "A",
    },
    # Q10
    {
        "question_number": 10,
        "difficulty": "medium",
        "question_en": "If 3^(x+y) = 81 and 81^(x-y) = 3, then x × y = ?",
        "question_hi": "यदि 3^(x+y) = 81 और 81^(x-y) = 3 है, तो x × y = ?",
        "option_a": "255/64",
        "option_b": "125/32",
        "option_c": "240/64",
        "option_d": "None of these",
        "correct_answer": "A",
    },
    # Q11 — RRB Group D 2022
    {
        "question_number": 11,
        "difficulty": "medium",
        "question_en": "If (25/9)^(x+1) × (81/625)^(x-1) = 9/25, then find the value of x. (RRB Group D 2022)",
        "question_hi": "यदि (25/9)^(x+1) × (81/625)^(x-1) = 9/25 है, तो x का मान ज्ञात कीजिए। (RRB Group D 2022)",
        "option_a": "8",
        "option_b": "6",
        "option_c": "5",
        "option_d": "4",
        "correct_answer": "D",
    },
    # Q12 — RRB Constable 2025
    {
        "question_number": 12,
        "difficulty": "easy",
        "question_en": "Find the value of (1/7)^(-4) + (1/9)^(-4) + (1/5)^(-4). (RRB Constable 2025)",
        "question_hi": "(1/7)^(-4) + (1/9)^(-4) + (1/5)^(-4) का मान ज्ञात करें। (RRB Constable 2025)",
        "option_a": "9584",
        "option_b": "9578",
        "option_c": "9587",
        "option_d": "9596",
        "correct_answer": "C",
    },
    # Q13
    {
        "question_number": 13,
        "difficulty": "hard",
        "question_en": "The value of (4096/9)^(-2/3) × (4/3)^5 + ⁴√(256)^(-3) is:",
        "question_hi": "(4096/9)^(-2/3) × (4/3)^5 + ⁴√(256)^(-3) का मान ज्ञात कीजिए:",
        "option_a": "1/41",
        "option_b": "1/43",
        "option_c": "1/36",
        "option_d": "1/37",
        "correct_answer": "C",
    },
    # Q14 — RRB Group D 2022
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": "Find the value of [{(9261)^(1/3) + 81^(1/4)}^2] × √1296. (RRB Group D 2022)",
        "question_hi": "[{(9261)^(1/3) + 81^(1/4)}^2] × √1296 का मान ज्ञात करें। (RRB Group D 2022)",
        "option_a": "249",
        "option_b": "174",
        "option_c": "147",
        "option_d": "294",
        "correct_answer": "D",
    },
    # Q15
    {
        "question_number": 15,
        "difficulty": "hard",
        "question_en": "If [{(2/3)^3}^(2x+3)]^(-3/4) = [{(2/3)^2}^(3x+7)]^(-6/5), then the value of √(2 - 42x) is:",
        "question_hi": "यदि [{(2/3)^3}^(2x+3)]^(-3/4) = [{(2/3)^2}^(3x+7)]^(-6/5) है, तो √(2 - 42x) का मान ज्ञात कीजिए:",
        "option_a": "5",
        "option_b": "6",
        "option_c": "3",
        "option_d": "4",
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
