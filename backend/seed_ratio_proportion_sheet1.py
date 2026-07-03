"""
seed_ratio_proportion_sheet1.py
================================
Seeds questions 1–7 (Ratio & Proportion) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Ratio & Proportion
Run     : python seed_ratio_proportion_sheet1.py

Answer key verification:
  Q1: 2×5×33 : 5×11×8 = 330:440 = 3:4                                        → A
  Q2: compound(3:4, 6:7)=9:14; 36:x=9:14 → x=56                              → C
  Q3: inverse ratios yz:x, zx:y, xy:z; compound=x²y²z²:xyz=xyz:1              → B
  Q4: x=5k,y=7k; (30k-7k):(25k+21k)=23:46=1:2                                → D
  Q5: a=3k,b=√5k; (6+√5)/(9-2√5)=(64+21√5)/61                               → D
  Q6: a³-b³:a³+b³=(125-27):(125+27)=98:152=49:76 (DP Constable 2023)         → D
  Q7: 1.5x=0.04y → y/x=75/2; (y²-x²)/(y+x)²=(y-x)/(y+x)=73/77 (SSC CGL 2025) → A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Ratio_Proportion_Sheet1"
SUBJECT = "Quant"
TOPIC   = "Ratio & Proportion"

QUESTIONS = [
    # Q1 — SSC CGL PRE 2023
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": "What is the compounded ratio of (2:5), (5:11) and (33:8)? (SSC CGL PRE 2023)",
        "question_hi": "(2:5), (5:11) और (33:8) का मिश्रित अनुपात क्या है? (SSC CGL PRE 2023)",
        "option_a": "3:4",
        "option_b": "2:11",
        "option_c": "33:5",
        "option_d": "2:5",
        "correct_answer": "A",
    },
    # Q2 — SSC CGL PRE 2024
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": "The compound ratio of 3:4 and 6:7 is 36:x, find x? (SSC CGL PRE 2024)",
        "question_hi": "3:4 और 6:7 का मिश्रित अनुपात 36:x है। x ज्ञात करें? (SSC CGL PRE 2024)",
        "option_a": "64",
        "option_b": "75",
        "option_c": "56",
        "option_d": "48",
        "correct_answer": "C",
    },
    # Q3
    {
        "question_number": 3,
        "difficulty": "medium",
        "question_en": "The compound ratio of inverse ratios of the ratios x:yz, y:zx, z:xy is?",
        "question_hi": "x:yz, y:zx, z:xy अनुपातों के व्युत्क्रमी अनुपातों का मिश्र अनुपात बताइए?",
        "option_a": "1:xyz",
        "option_b": "xyz:1",
        "option_c": "1:1",
        "option_d": "x:yz",
        "correct_answer": "B",
    },
    # Q4 — SSC CGL PRE 2025
    {
        "question_number": 4,
        "difficulty": "easy",
        "question_en": "If x:y = 5:7, then (6x − y):(5x + 3y) is equal to? (SSC CGL PRE 2025)",
        "question_hi": "यदि x:y = 5:7 है, तो (6x − y):(5x + 3y) का मान ज्ञात करें। (SSC CGL PRE 2025)",
        "option_a": "1:4",
        "option_b": "11:2",
        "option_c": "4:1",
        "option_d": "1:2",
        "correct_answer": "D",
    },
    # Q5
    {
        "question_number": 5,
        "difficulty": "hard",
        "question_en": "If a:b = 3:√5, then the value of (2a + b):(3a − 2b) is?",
        "question_hi": "यदि a:b = 3:√5 है, तो (2a + b):(3a − 2b) का मान क्या होगा?",
        "option_a": "1/64 × (64 + 21√5)",
        "option_b": "1/62 × (64 + 21√5)",
        "option_c": "1/63 × (64 + 21√5)",
        "option_d": "1/61 × (64 + 21√5)",
        "correct_answer": "D",
    },
    # Q6 — DP Constable 2023
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": "If a:b = 5:3, then (a³ − b³):(a³ + b³)? (DP Constable 2023)",
        "question_hi": "यदि a:b = 5:3, तो (a³ − b³):(a³ + b³)? (DP Constable 2023)",
        "option_a": "25:76",
        "option_b": "49:16",
        "option_c": "11:25",
        "option_d": "49:76",
        "correct_answer": "D",
    },
    # Q7 — SSC CGL PRE 2025
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": "If 1.5x = 0.04y, then find (y² − x²) / (y² + 2xy + x²)? (SSC CGL PRE 2025)",
        "question_hi": "यदि 1.5x = 0.04y है, तो (y² − x²) / (y² + 2xy + x²) ज्ञात कीजिए? (SSC CGL PRE 2025)",
        "option_a": "73/77",
        "option_b": "77/73",
        "option_c": "11/12",
        "option_d": "2",
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
