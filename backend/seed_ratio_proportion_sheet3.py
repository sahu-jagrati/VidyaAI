"""
seed_ratio_proportion_sheet3.py
================================
Seeds questions 16–21 (Ratio & Proportion) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Ratio & Proportion
Run     : python seed_ratio_proportion_sheet3.py

Answer key verification:
  Q16: 7A=5B→A:B=5:7; 6B=11C→B:C=11:6; LCM→55:77:42; total=174             → B
  Q17: A:B=8:13,B:C=5:8,C:D=4:5; LCM(13,5)=65,LCM(104,4)=104 → 40:65:104:130 → A
  Q18: A:B=5:2,B:C=8:3,C:D=21:10; LCM → 140:56:21:10 (SSC CHSL PRE 2025)    → D
  Q19: c/a=(7/5)×(3/2)=21/10 (SSC CGL Mains 2024)                             → C
  Q20: a:b:c:d=21:35:40:60; 2a:3d=42:180=7:30 (SSC CHSL PRE 2025)            → B
  Q21: a:b:c:d=105:35:28:24; (d+a)/(d-a)=129/(-81)=-43/27 (SSC CGL PRE 2025) → C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Ratio_Proportion_Sheet3"
SUBJECT = "Quant"
TOPIC   = "Ratio & Proportion"

QUESTIONS = [
    # Q16 — SSC CGL PRE 2025
    {
        "question_number": 16,
        "difficulty": "medium",
        "question_en": "A, B and C have coins. 7 times coins of A = 5 times coins of B, and 6 times coins of B = 11 times coins of C. What is the minimum total number of coins with A, B and C? (SSC CGL PRE 2025)",
        "question_hi": "A, B और C के पास कुछ सिक्के हैं। A के पास मौजूद सिक्कों की संख्या का 7 गुना, B के पास मौजूद सिक्कों की संख्या के 5 गुना के बराबर है; B के 6 गुना = C के 11 गुना। A, B और C के पास मौजूद सिक्कों की न्यूनतम संख्या कितनी है? (SSC CGL PRE 2025)",
        "option_a": "110",
        "option_b": "174",
        "option_c": "154",
        "option_d": "165",
        "correct_answer": "B",
    },
    # Q17 — SSC Selection Post XII Graduate Level
    {
        "question_number": 17,
        "difficulty": "medium",
        "question_en": "If A:B = 8:13, B:C = 5:8 and C:D = 4:5, then A:B:C:D is equal to? (SSC Selection Post XII Graduate Level)",
        "question_hi": "यदि A:B = 8:13, B:C = 5:8 और C:D = 4:5 है, तो A:B:C:D बराबर है? (SSC Selection Post XII Graduate Level)",
        "option_a": "40:65:104:130",
        "option_b": "38:65:111:120",
        "option_c": "38:65:111:120",
        "option_d": "40:60:103:112",
        "correct_answer": "A",
    },
    # Q18 — SSC CHSL PRE 2025
    {
        "question_number": 18,
        "difficulty": "hard",
        "question_en": "If A:B = 1/2 : 1/5, B:C = 1/3 : 1/8, C:D = 1/10 : 1/21, then A:B:C:D is? (SSC CHSL PRE 2025)",
        "question_hi": "यदि A:B = 1/2 : 1/5, B:C = 1/3 : 1/8, C:D = 1/10 : 1/21 है, तो A:B:C:D है? (SSC CHSL PRE 2025)",
        "option_a": "40:24:21:10",
        "option_b": "48:23:25:8",
        "option_c": "14:24:28:10",
        "option_d": "140:56:21:10",
        "correct_answer": "D",
    },
    # Q19 — SSC CGL Mains 2024
    {
        "question_number": 19,
        "difficulty": "medium",
        "question_en": "If a:b = 2:3, b:c = 5:7, then find the ratio c:a. (SSC CGL Mains 2024)",
        "question_hi": "यदि a:b = 2:3, b:c = 5:7 है, तो c:a का अनुपात ज्ञात कीजिए। (SSC CGL Mains 2024)",
        "option_a": "15:21",
        "option_b": "20:21",
        "option_c": "21:10",
        "option_d": "10:21",
        "correct_answer": "C",
    },
    # Q20 — SSC CHSL PRE 2025
    {
        "question_number": 20,
        "difficulty": "medium",
        "question_en": "If a:b = 3:5, b:c = 7:8 and c:d = 2:3, then 2a:3d is equal to? (SSC CHSL PRE 2025)",
        "question_hi": "यदि a:b = 3:5, b:c = 7:8 और c:d = 2:3 है, तो 2a:3d का मान ज्ञात करें। (SSC CHSL PRE 2025)",
        "option_a": "1:2",
        "option_b": "7:30",
        "option_c": "7:15",
        "option_d": "7:20",
        "correct_answer": "B",
    },
    # Q21 — SSC CGL PRE 2025
    {
        "question_number": 21,
        "difficulty": "hard",
        "question_en": "If a = 3b, 4b = 5c, 6c = 7d, then what is the value of (d + a) / (d − a)? (SSC CGL PRE 2025)",
        "question_hi": "यदि a = 3b, 4b = 5c, 6c = 7d है, तो (d + a) / (d − a) का मान क्या है? (SSC CGL PRE 2025)",
        "option_a": "27/43",
        "option_b": "43/27",
        "option_c": "-43/27",
        "option_d": "-27/43",
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
