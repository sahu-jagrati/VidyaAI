"""
seed_ratio_proportion_sheet5.py
================================
Seeds questions 29–36 (Ratio & Proportion) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Ratio & Proportion
Run     : python seed_ratio_proportion_sheet5.py

Answer key verification:
  Q29: a=13k/2,b=59k/5,c=12k; (a+c)/b=116k/5÷59k/5=116/59                  → B
  Q30: l=770,n=1008; m=2772-1778=994 (ICAR Technician 2023)                   → D
  Q31: a+b=21,b+c=18,c+a=15→a=9,b=12,c=6; 1/a:1/b:1/c=4:3:6                → A
  Q32: a=54,b=81,c=45; 3a+b-4c=162+81-180=63 (MTS 2020)                      → D
  Q33: a²=9k,b²=25k,c²=36k→a=3,b=5,c=6; b-a:c-b:c-a=2:1:3                  → B
  Q34: 2a=13k,2b=9k,c=7k; (a-b):(c-b):(c-a)=4:5:1 (SSC GD 2021)            → C
  Q35: a=3/2,b=3,c=3/2 (from chain); abc=27/4                                 → C
  Q36: a:b=c:d=e:f=5:7; (3+5+11)×5:(3+5+11)×7=5:7 (SSC CGL 2024 Pre)       → C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Ratio_Proportion_Sheet5"
SUBJECT = "Quant"
TOPIC   = "Ratio & Proportion"

QUESTIONS = [
    # Q29
    {
        "question_number": 29,
        "difficulty": "hard",
        "question_en": "If (a+b)/c = 23/12 and (b+c)/a = 17/8, then what is the value of (a+c)/b?",
        "question_hi": "यदि (a+b)/c = 23/12 तथा (b+c)/a = 17/8 है, तो (a+c)/b का मान क्या है?",
        "option_a": "9/5",
        "option_b": "116/59",
        "option_c": "107/68",
        "option_d": "16/11",
        "correct_answer": "B",
    },
    # Q30 — ICAR Technician 2023
    {
        "question_number": 30,
        "difficulty": "hard",
        "question_en": "If l+m+n = 2772, l:(m+n) = 5:13 and n:(l+m) = 4:7, then what is the value of m? (ICAR Technician 2023)",
        "question_hi": "यदि l+m+n = 2772, l:(m+n) = 5:13 और n:(l+m) = 4:7 है, तो m का मान क्या है? (ICAR Technician 2023)",
        "option_a": "991",
        "option_b": "990",
        "option_c": "995",
        "option_d": "994",
        "correct_answer": "D",
    },
    # Q31
    {
        "question_number": 31,
        "difficulty": "medium",
        "question_en": "If (a+b):(b+c):(c+a) = 7:6:5 and a+b+c = 27, then what will be the value of 1/a : 1/b : 1/c?",
        "question_hi": "यदि (a+b):(b+c):(c+a) = 7:6:5 और a+b+c = 27 है, तो 1/a : 1/b : 1/c का मान क्या होगा?",
        "option_a": "4:3:6",
        "option_b": "3:4:2",
        "option_c": "3:2:4",
        "option_d": "3:6:4",
        "correct_answer": "A",
    },
    # Q32 — MTS 2020
    {
        "question_number": 32,
        "difficulty": "medium",
        "question_en": "If (a+b):(b+c):(c+a) = 15:14:11 and a+b+c = 180, then what is the value of (3a+b−4c)? (MTS 2020)",
        "question_hi": "यदि (a+b):(b+c):(c+a) = 15:14:11 और a+b+c = 180 है, तो (3a+b−4c) का मान ज्ञात करें। (MTS 2020)",
        "option_a": "98",
        "option_b": "77",
        "option_c": "45",
        "option_d": "63",
        "correct_answer": "D",
    },
    # Q33
    {
        "question_number": 33,
        "difficulty": "hard",
        "question_en": "If a, b and c are positive numbers such that (a²+b²):(b²+c²):(c²+a²) = 34:61:45, then b−a : c−b : c−a = ___",
        "question_hi": "यदि a, b और c तीन ऐसी धनात्मक संख्याएं हैं कि (a²+b²):(b²+c²):(c²+a²) = 34:61:45 है, तो b−a : c−b : c−a = ___",
        "option_a": "1:2:3",
        "option_b": "2:1:3",
        "option_c": "3:1:2",
        "option_d": "3:2:1",
        "correct_answer": "B",
    },
    # Q34 — SSC GD 2021
    {
        "question_number": 34,
        "difficulty": "hard",
        "question_en": "If (a+b−c):(b+c−a):(a+c−b) = 4:5:9, then find (a−b):(c−b):(c−a)? (SSC GD 2021)",
        "question_hi": "यदि (a+b−c):(b+c−a):(a+c−b) = 4:5:9 है, तो (a−b):(c−b):(c−a) ज्ञात कीजिए? (SSC GD 2021)",
        "option_a": "4:1:5",
        "option_b": "1:4:5",
        "option_c": "4:5:1",
        "option_d": "5:1:4",
        "correct_answer": "C",
    },
    # Q35
    {
        "question_number": 35,
        "difficulty": "hard",
        "question_en": "If a/b = 2, b/c = 2, c/d = 1/2, d/e = 3 and e/f = 1/4, then what is the value of abc/def?",
        "question_hi": "यदि a/b = 2, b/c = 2, c/d = 1/2, d/e = 3 और e/f = 1/4 है, तो abc/def का मान क्या है?",
        "option_a": "3/8",
        "option_b": "1/7",
        "option_c": "27/4",
        "option_d": "9/4",
        "correct_answer": "C",
    },
    # Q36 — SSC CGL 2024 Pre
    {
        "question_number": 36,
        "difficulty": "easy",
        "question_en": "If a:b = c:d = e:f = 5:7, then what is the ratio (3a+5c+11e):(3b+5d+11f)? (SSC CGL 2024 Pre)",
        "question_hi": "यदि a:b = c:d = e:f = 5:7 है, तो अनुपात (3a+5c+11e):(3b+5d+11f) क्या है? (SSC CGL 2024 Pre)",
        "option_a": "7:11",
        "option_b": "3:7",
        "option_c": "5:7",
        "option_d": "11:7",
        "correct_answer": "C",
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
