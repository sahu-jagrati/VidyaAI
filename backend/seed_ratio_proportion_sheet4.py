"""
seed_ratio_proportion_sheet4.py
================================
Seeds questions 22–28 (Ratio & Proportion) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Ratio & Proportion
Run     : python seed_ratio_proportion_sheet4.py

Answer key verification:
  Q22: 3A=4B=5C=k→A:B:C=k/3:k/4:k/5=20:15:12 (SSC CHSL PRE 2025)           → C
  Q23: 15x=24y=32z→x:y:z=LCM480×(1/15:1/24:1/32)=32:20:15 (MTS 2023)       → C
  Q24: 0.4A=0.6B=C/6→A=5k/2,B=5k/3,C=6k→15:10:36 (SSC CPO 2024)            → C
  Q25: 3P/5=7Q/9=4R/5=k→P:Q:R=5k/3:9k/7:5k/4=140:108:105                   → B
  Q26: a=18,b=15,c=16 satisfies 2a/3=4b/5=3c/4=12; √(a²+c²-b²)=√355 (CDS 2023) → B
  Q27: 1/a:1/b:1/c=2:3:5→a:b:c=1/2:1/3:1/5=15:10:6 (DP Constable 2023)     → B
  Q28: A=2,B=3,C=5; A/B:B/C:C/A=2/3:3/5:5/2=20:18:75 (DP Constable 2023)   → B
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Ratio_Proportion_Sheet4"
SUBJECT = "Quant"
TOPIC   = "Ratio & Proportion"

QUESTIONS = [
    # Q22 — SSC CHSL PRE 2025
    {
        "question_number": 22,
        "difficulty": "easy",
        "question_en": "If 3A = 4B = 5C, then A:B:C is equal to? (SSC CHSL PRE 2025)",
        "question_hi": "यदि 3A = 4B = 5C है, तो A:B:C का मान क्या होगा? (SSC CHSL PRE 2025)",
        "option_a": "10:7:6",
        "option_b": "10:5:4",
        "option_c": "20:15:12",
        "option_d": "20:15:16",
        "correct_answer": "C",
    },
    # Q23 — MTS 2023
    {
        "question_number": 23,
        "difficulty": "easy",
        "question_en": "If 15x = 24y = 32z, then x:y:z is equal to? (MTS 2023)",
        "question_hi": "यदि 15x = 24y = 32z है, तो x:y:z किसके बराबर है? (MTS 2023)",
        "option_a": "32:15:20",
        "option_b": "15:24:32",
        "option_c": "32:20:15",
        "option_d": "24:15:4",
        "correct_answer": "C",
    },
    # Q24 — SSC CPO 2024
    {
        "question_number": 24,
        "difficulty": "medium",
        "question_en": "If 40% of A = 60% of B = 1/6 of C, find A:B:C? (SSC CPO 2024)",
        "question_hi": "यदि A का 40% = B का 60% = C का 1/6 है, तो A:B:C ज्ञात करें? (SSC CPO 2024)",
        "option_a": "15:10:18",
        "option_b": "36:10:15",
        "option_c": "15:10:36",
        "option_d": "10:15:36",
        "correct_answer": "C",
    },
    # Q25
    {
        "question_number": 25,
        "difficulty": "hard",
        "question_en": "If (3/5)P = (7/9)Q = (4/5)R, then what is the ratio of P, Q and R respectively?",
        "question_hi": "यदि (3/5)P = (7/9)Q = (4/5)R है, तो क्रमशः P, Q तथा R का अनुपात क्या है?",
        "option_a": "35:36:15",
        "option_b": "140:108:105",
        "option_c": "135:140:105",
        "option_d": "70:45:63",
        "correct_answer": "B",
    },
    # Q26 — CDS 2023
    {
        "question_number": 26,
        "difficulty": "hard",
        "question_en": "If 2a/3 = 4b/5 = 3c/4, then what is the value of √(a² + c² − b²)? (CDS 2023)",
        "question_hi": "यदि 2a/3 = 4b/5 = 3c/4 है, तो √(a² + c² − b²) का मान क्या है? (CDS 2023)",
        "option_a": "3√5",
        "option_b": "√355",
        "option_c": "√375",
        "option_d": "3√15",
        "correct_answer": "B",
    },
    # Q27 — DP Constable 2023
    {
        "question_number": 27,
        "difficulty": "medium",
        "question_en": "If 1/a : 1/b : 1/c = 2 : 3 : 5, then a : b : c is equal to? (DP Constable 2023)",
        "question_hi": "यदि 1/a : 1/b : 1/c = 2 : 3 : 5 है, तो a : b : c किसके बराबर है? (DP Constable 2023)",
        "option_a": "15:10:12",
        "option_b": "15:10:6",
        "option_c": "2:4:5",
        "option_d": "6:10:15",
        "correct_answer": "B",
    },
    # Q28 — DP Constable 2023
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": "If A:B:C = 2:3:5, then the ratio A/B : B/C : C/A is equal to? (DP Constable 2023)",
        "question_hi": "यदि A:B:C = 2:3:5 है, तो अनुपात A/B : B/C : C/A किसके बराबर है? (DP Constable 2023)",
        "option_a": "20:25:39",
        "option_b": "20:18:75",
        "option_c": "18:20:79",
        "option_d": "75:20:29",
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
