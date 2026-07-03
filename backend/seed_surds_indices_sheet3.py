"""
seed_surds_indices_sheet3.py
============================
Seeds questions 16–24 (Surds & Indices) from Gagan Pratap Sir PDFs.
(Q20 skipped — answer not provided)
Subject : Quant
Topic   : Surds & Indices
Run     : python seed_surds_indices_sheet3.py

Answer key verification:
  Q16: a^(7-9)×b^(8-5)×c^(7-4) = a^-2 × b^3 × c^3                        → C
  Q17: Simplify ratio→3^(6-2n)×2^(18-n)×5^(-10-n)=4/15^26 → n=16;√25=5    → C
  Q18: 3^(2-n)−8×3^(3n-3m)=1/729 → n=6,m=8; m-n=2                         → C
  Q19: Eq2→y=4z; Eq3→x=5z/2; Eq1→z=2 → x=5,y=8,z=2; 10+24+10=44          → B
  Q21: (5√7-3√5)^2 = 175+45-30√35 = 220-30√35 ✓                            → A
  Q22: [½(√7-√5)]^2 = (12-2√35)/4 = (6-√35)/2 ✓                           → A
  Q23: √(11-6√2)=3-√2; 9-2(3-√2)=3+2√2; √(3+2√2)=1+√2≈2.414               → C
  Q24: √(7+4√3)=2+√3; 3+8(2+√3)=19+8√3=(4+√3)^2; -√3+4+√3=4; √4=2        → A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Surds_Indices_Sheet3"
SUBJECT = "Quant"
TOPIC   = "Surds & Indices"

QUESTIONS = [
    # Q16 — SSC CGL Mains 2024
    {
        "question_number": 16,
        "difficulty": "easy",
        "question_en": "(a^7 × b^8 × c^7) / (a^9 × b^5 × c^4) in simplified form is: (SSC CGL Mains 2024)",
        "question_hi": "(a^7 × b^8 × c^7) / (a^9 × b^5 × c^4) का सरलीकृत रूप ज्ञात कीजिए। (SSC CGL Mains 2024)",
        "option_a": "(a^2) × (b^3) × (c^3)",
        "option_b": "(a^-7) × (b^3) × (c^-4)",
        "option_c": "(a^-2) × (b^3) × (c^3)",
        "option_d": "(a^-3) × (b^-5) × (c^0)",
        "correct_answer": "C",
    },
    # Q17
    {
        "question_number": 17,
        "difficulty": "hard",
        "question_en": "If (3^(n+3) × 4^(n+6) × 25^(n+1)) / (27^(n-1) × 8^(n-2) × 125^(n+4)) = 4 / 15^26, then the value of √(n+9) is:",
        "question_hi": "यदि (3^(n+3) × 4^(n+6) × 25^(n+1)) / (27^(n-1) × 8^(n-2) × 125^(n+4)) = 4 / 15^26 है, तो √(n+9) का मान ज्ञात कीजिए:",
        "option_a": "4",
        "option_b": "6",
        "option_c": "5",
        "option_d": "8",
        "correct_answer": "C",
    },
    # Q18
    {
        "question_number": 18,
        "difficulty": "hard",
        "question_en": "If 9^n × 3^2 × (3^(3/2))^(-2n) - 27^n × 2^3 / 3^(3m) = 1/729, then m − n = ?",
        "question_hi": "यदि 9^n × 3^2 × (3^(3/2))^(-2n) - 27^n × 2^3 / 3^(3m) = 1/729 है, तो m − n = ?",
        "option_a": "3",
        "option_b": "1",
        "option_c": "2",
        "option_d": "-2",
        "correct_answer": "C",
    },
    # Q19
    {
        "question_number": 19,
        "difficulty": "hard",
        "question_en": "If 2^(x+y-2x) = 8^(8z-5-y); 5^(4y-6z) = 25^(y+z); 3^(4x-3z) = 9^(x+z), then the value of 2x + 3y + 5z is:",
        "question_hi": "यदि 2^(x+y-2x) = 8^(8z-5-y); 5^(4y-6z) = 25^(y+z); 3^(4x-3z) = 9^(x+z) है तो 2x + 3y + 5z का मान बताइए।",
        "option_a": "56",
        "option_b": "44",
        "option_c": "32",
        "option_d": "28",
        "correct_answer": "B",
    },
    # Q21
    {
        "question_number": 21,
        "difficulty": "medium",
        "question_en": "Evaluate √(220 - 30√35)?",
        "question_hi": "√(220 - 30√35) मूल्यांकन करें?",
        "option_a": "5√7 - 3√5",
        "option_b": "7√5 - 3√7",
        "option_c": "5√5 - 3√7",
        "option_d": "3√7 - 5√5",
        "correct_answer": "A",
    },
    # Q22
    {
        "question_number": 22,
        "difficulty": "medium",
        "question_en": "√(6 - √35) = ?",
        "question_hi": "√(6 - √35) = ?",
        "option_a": "1/2 × (√7 - √5)",
        "option_b": "1/2 × (√5 - √7)",
        "option_c": "1/4 × (√7 - √5)",
        "option_d": "1/4 × (√7 + √3)",
        "correct_answer": "A",
    },
    # Q23
    {
        "question_number": 23,
        "difficulty": "hard",
        "question_en": "The value of √(9 - 2√(11 - 6√2)) is closest to:",
        "question_hi": "√(9 - 2√(11 - 6√2)) का मान किसके निकटतम है?",
        "option_a": "2.7",
        "option_b": "2.9",
        "option_c": "2.4",
        "option_d": "2.1",
        "correct_answer": "C",
    },
    # Q24
    {
        "question_number": 24,
        "difficulty": "hard",
        "question_en": "If x = √(-√3 + √(3 + 8√(7 + 4√3))), where x > 0, then the value of x is equal to:",
        "question_hi": "यदि x = √(-√3 + √(3 + 8√(7 + 4√3))), जहाँ x > 0 है, तो x का मान ज्ञात कीजिए:",
        "option_a": "2",
        "option_b": "3",
        "option_c": "4",
        "option_d": "1",
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
