"""
seed_ratio_proportion_sheet2.py
================================
Seeds questions 8–15 (Ratio & Proportion) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Ratio & Proportion
Run     : python seed_ratio_proportion_sheet2.py

Answer key verification:
  Q8:  A=3,B=4,C=5; √(9+16):√(25-16)=5k:3k=5:3                               → C
  Q9:  a²=4,b²=3,c²=2,d²=1; (-4+3+2+1)/(4-3+2-1)=2/2=1                      → A
  Q10: m=1,n=2,p=3,q=4; (2+12):(2+12)=1:1 (CDS-1 2024)                       → A
  Q11: 5(10a³+4b³)=7(11a³-15b³)→b/a=3/5→a=5,b=3; 30:39=10:13                → A
  Q12: x=7,y=-8; (35+48):(42+56)=83:98                                         → D
  Q13: a:b=9:14,b:c=16:7; LCM(14,16)=112 → 72:112:49 (SSC CGL 2025 PRE)      → D
  Q14: α:β=15:22,β:γ=12:13; LCM(22,12)=132 → 90:132:143 (RRB NTPC 2025)     → C
  Q15: P:Q:R=6:4:7; (P+Q):(Q+R):(R+P)=10:11:13 (Mains 2023 SSC CGL)         → D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Ratio_Proportion_Sheet2"
SUBJECT = "Quant"
TOPIC   = "Ratio & Proportion"

QUESTIONS = [
    # Q8 — SSC MTS 2023
    {
        "question_number": 8,
        "difficulty": "easy",
        "question_en": "If A:B:C = 3:4:5, then √(A² + B²) : √(C² − B²) is? (SSC MTS 2023)",
        "question_hi": "यदि A:B:C = 3:4:5 है, तो √(A² + B²) : √(C² − B²) _____ है। (SSC MTS 2023)",
        "option_a": "3:2",
        "option_b": "4:5",
        "option_c": "5:3",
        "option_d": "3:5",
        "correct_answer": "C",
    },
    # Q9 — CDS-1 2024
    {
        "question_number": 9,
        "difficulty": "medium",
        "question_en": "If a:b:c:d = √4:√3:√2:√1, then what is the value of (−a²+b²+c²+d²)/(a²−b²+c²−d²)? (CDS-1 2024)",
        "question_hi": "यदि a:b:c:d = √4:√3:√2:√1 है, तो (−a²+b²+c²+d²)/(a²−b²+c²−d²) का मान क्या है? (CDS-1 2024)",
        "option_a": "1",
        "option_b": "2",
        "option_c": "3",
        "option_d": "6",
        "correct_answer": "A",
    },
    # Q10 — CDS-1 2024
    {
        "question_number": 10,
        "difficulty": "easy",
        "question_en": "If m:n = 1:2 and p:q = 3:4, then what is (2m + 4p):(n + 3q) equal to? (CDS-1 2024)",
        "question_hi": "यदि m:n = 1:2 और p:q = 3:4 है, तो (2m + 4p):(n + 3q) किसके बराबर है? (CDS-1 2024)",
        "option_a": "1:1",
        "option_b": "1:3",
        "option_c": "2:3",
        "option_d": "2:1",
        "correct_answer": "A",
    },
    # Q11
    {
        "question_number": 11,
        "difficulty": "hard",
        "question_en": "If (10a³ + 4b³):(11a³ − 15b³) = 7:5, then (3a + 5b):(9a − 2b) = ?",
        "question_hi": "यदि (10a³ + 4b³):(11a³ − 15b³) = 7:5 है, तो (3a + 5b):(9a − 2b) = ?",
        "option_a": "10:13",
        "option_b": "5:4",
        "option_c": "3:2",
        "option_d": "8:7",
        "correct_answer": "A",
    },
    # Q12 — MTS 2020
    {
        "question_number": 12,
        "difficulty": "hard",
        "question_en": "x and y are two numbers having opposite signs such that x²:y² = 49:64. What is the value of (5x − 6y):(6x − 7y)? (MTS 2020)",
        "question_hi": "x और y विपरीत चिह्नों वाली दो संख्याएं इस प्रकार हैं कि x²:y² = 49:64 है, तो (5x − 6y):(6x − 7y) का मान क्या होगा? (MTS 2020)",
        "option_a": "44:65",
        "option_b": "13:14",
        "option_c": "94:117",
        "option_d": "83:98",
        "correct_answer": "D",
    },
    # Q13 — SSC CGL 2025 PRE
    {
        "question_number": 13,
        "difficulty": "medium",
        "question_en": "If a:b = 9:14 and b:c = 16:7, then a:b:c = ? (SSC CGL 2025 PRE)",
        "question_hi": "यदि a:b = 9:14 और b:c = 16:7 है, तो a:b:c क्या है? (SSC CGL 2025 PRE)",
        "option_a": "9:112:7",
        "option_b": "72:102:49",
        "option_c": "9:112:49",
        "option_d": "72:112:49",
        "correct_answer": "D",
    },
    # Q14 — RRB NTPC 12th Level CBT-2 2025
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": "If α:β = 15:22 and β:γ = 12:13, then what is the value of α:β:γ? (RRB NTPC 12th Level CBT-2 2025)",
        "question_hi": "यदि α:β = 15:22 तथा β:γ = 12:13 है, तो α:β:γ का मान क्या होगा? (RRB NTPC 12th Level CBT-2 2025)",
        "option_a": "90:66:143",
        "option_b": "45:66:143",
        "option_c": "90:132:143",
        "option_d": "90:143:132",
        "correct_answer": "C",
    },
    # Q15 — Mains 2023 SSC CGL
    {
        "question_number": 15,
        "difficulty": "medium",
        "question_en": "If P:Q = 3:2 and Q:R = 4:7, then (P+Q):(Q+R):(R+P) = ? (Mains 2023 SSC CGL)",
        "question_hi": "यदि P:Q = 3:2 और Q:R = 4:7 है, तो (P+Q):(Q+R):(R+P) का मान ज्ञात कीजिए। (Mains 2023 SSC CGL)",
        "option_a": "10:13:11",
        "option_b": "11:4:17",
        "option_c": "3:4:7",
        "option_d": "10:11:13",
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
