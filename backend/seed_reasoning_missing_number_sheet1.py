"""
seed_reasoning_missing_number_sheet1.py
=========================================
Seeds Missing Number Q1-Q10 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Missing Number
Run     : python seed_reasoning_missing_number_sheet1.py

Matrix format in question_en: rows separated by " || ", elements by spaces.
Answers verified via Python (all correct).

Answer key:
  Q1   4 8 20 || 9 3 15 || 6 6 ?       (mid×2)+first=last; (6×2)+6=18        → B  18
  Q2   18 16 7 || 35 25 ? || ...        col sum: 1st+4th=2nd+3rd; ?=14        → D  14
  Q3   2 4 6 || 6 2 4 || 4 ? 2         row sum=12; 4+?+2=12→?=6              → C  6
  Q4   15 225 30 || 7 70 20 || 3 ? 8   (first×third)/2=mid; (3×8)/2=12       → A  12
  Q5   4 7 9 || 8 6 8 || 3 7 9 || ...  (R1×R2)+R3=R4; (9×8)+9=81            → B  81
  Q6   7 6 8 || 5 4 9 || 3 2 1 || ...  sum of squares top3=bottom; 8²+9²+1²  → D  146
  Q7   4 5 6 || 2 3 7 || 1 8 3 || ...  sum of squares top3=bottom; 6²+7²+3²  → C  94
  Q8   36 25 64 || 16 9 36 || 4 1 ?    √col decreases by 2; (√64→6→4)→4²=16  → D  16
  Q9   108 17 9 || 208 31 8 || 245 ? 7 (first/third)+5=mid; (245/7)+5=40     → C  40
  Q10  5 1 25 || 6 2 18 || 10 4 25 ...  first²/second=third; 3²/3=3          → C  3
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Missing_Number_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Missing Number"

QUESTIONS = [
    # ── Q1 ── (middle×2) + first = last ──────────────────────────────────────
    # R1:(8×2)+4=20 ✓  R2:(3×2)+9=15 ✓  R3:(6×2)+6=18
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": "Find the missing number in the matrix: 4 8 20 || 9 3 15 || 6 6 ?",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 4 8 20 || 9 3 15 || 6 6 ?",
        "option_a": "22",
        "option_b": "18",
        "option_c": "16",
        "option_d": "20",
        "correct_answer": "B",   # (6×2)+6=18
    },
    # ── Q2 ── sum(1st,4th col) = sum(2nd,3rd col) ────────────────────────────
    # C1: 18+24=42, 35+7=42 ✓  C2: 16+32=48, 25+23=48 ✓  C3: 7+65=72, ?+58=72→14
    {
        "question_number": 2,
        "difficulty": "medium",
        "question_en": "Find the missing number in the matrix: 18 16 7 || 35 25 ? || 7 23 58 || 24 32 65",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 18 16 7 || 35 25 ? || 7 23 58 || 24 32 65",
        "option_a": "17",
        "option_b": "15",
        "option_c": "13",
        "option_d": "14",
        "correct_answer": "D",   # col sum: (7+65)-(58)=14
    },
    # ── Q3 ── sum of each row = 12 ────────────────────────────────────────────
    # R1:2+4+6=12 ✓  R2:6+2+4=12 ✓  R3:4+?+2=12→?=6
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": "Find the missing number in the matrix: 2 4 6 || 6 2 4 || 4 ? 2",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 2 4 6 || 6 2 4 || 4 ? 2",
        "option_a": "2",
        "option_b": "4",
        "option_c": "6",
        "option_d": "8",
        "correct_answer": "C",   # row sum=12: 4+?+2=12 → ?=6
    },
    # ── Q4 ── (first × third) / 2 = middle ────────────────────────────────────
    # R1:(15×30)/2=225 ✓  R2:(7×20)/2=70 ✓  R3:(3×8)/2=12
    {
        "question_number": 4,
        "difficulty": "easy",
        "question_en": "Find the missing number in the matrix: 15 225 30 || 7 70 20 || 3 ? 8",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 15 225 30 || 7 70 20 || 3 ? 8",
        "option_a": "12",
        "option_b": "16",
        "option_c": "24",
        "option_d": "70",
        "correct_answer": "A",   # (3×8)/2=12
    },
    # ── Q5 ── (Row1 × Row2) + Row3 = Row4 per column ─────────────────────────
    # C1:(4×8)+3=35 ✓  C2:(7×6)+7=49 ✓  C3:(9×8)+9=81
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": "Find the missing number in the matrix: 4 7 9 || 8 6 8 || 3 7 9 || 35 49 ?",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 4 7 9 || 8 6 8 || 3 7 9 || 35 49 ?",
        "option_a": "89",
        "option_b": "81",
        "option_c": "64",
        "option_d": "63",
        "correct_answer": "B",   # (9×8)+9=81
    },
    # ── Q6 ── sum of squares of top 3 = bottom number ────────────────────────
    # C1:7²+5²+3²=49+25+9=83 ✓  C2:6²+4²+2²=36+16+4=56 ✓  C3:8²+9²+1²=64+81+1=146
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": "Find the missing number in the matrix: 7 6 8 || 5 4 9 || 3 2 1 || 83 56 ?",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 7 6 8 || 5 4 9 || 3 2 1 || 83 56 ?",
        "option_a": "128",
        "option_b": "136",
        "option_c": "148",
        "option_d": "146",
        "correct_answer": "D",   # 8²+9²+1²=64+81+1=146
    },
    # ── Q7 ── sum of squares of top 3 = bottom number ────────────────────────
    # C1:4²+2²+1²=16+4+1=21 ✓  C2:5²+3²+8²=25+9+64=98 ✓  C3:6²+7²+3²=36+49+9=94
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": "Find the missing number in the matrix: 4 5 6 || 2 3 7 || 1 8 3 || 21 98 ?",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 4 5 6 || 2 3 7 || 1 8 3 || 21 98 ?",
        "option_a": "73",
        "option_b": "16",
        "option_c": "94",
        "option_d": "76",
        "correct_answer": "C",   # 6²+7²+3²=36+49+9=94
    },
    # ── Q8 ── √col decreases by 2; next value → squared ─────────────────────
    # C1:√36=6,√16=4,√4=2 (step-2) ✓  C2:√25=5,√9=3,√1=1 (step-2) ✓
    # C3:√64=8,√36=6→next=4→4²=16
    {
        "question_number": 8,
        "difficulty": "medium",
        "question_en": "Find the missing number in the matrix: 36 25 64 || 16 9 36 || 4 1 ?",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 36 25 64 || 16 9 36 || 4 1 ?",
        "option_a": "49",
        "option_b": "64",
        "option_c": "25",
        "option_d": "16",
        "correct_answer": "D",   # √col decreases by 2: √64=8,√36=6→4→4²=16
    },
    # ── Q9 ── (first / third) + 5 = middle ────────────────────────────────────
    # R1:(108/9)+5=12+5=17 ✓  R2:(208/8)+5=26+5=31 ✓  R3:(245/7)+5=35+5=40
    {
        "question_number": 9,
        "difficulty": "medium",
        "question_en": "Find the missing number in the matrix: 108 17 9 || 208 31 8 || 245 ? 7",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 108 17 9 || 208 31 8 || 245 ? 7",
        "option_a": "35",
        "option_b": "25",
        "option_c": "40",
        "option_d": "32",
        "correct_answer": "C",   # (245/7)+5=35+5=40
    },
    # ── Q10 ── first² / second = third ────────────────────────────────────────
    # R1:5²/1=25 ✓  R2:6²/2=18 ✓  R3:10²/4=25 ✓  R4:3²/3=3
    {
        "question_number": 10,
        "difficulty": "easy",
        "question_en": "Find the missing number in the matrix: 5 1 25 || 6 2 18 || 10 4 25 || 3 3 ?",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 5 1 25 || 6 2 18 || 10 4 25 || 3 3 ?",
        "option_a": "10",
        "option_b": "9",
        "option_c": "3",
        "option_d": "5",
        "correct_answer": "C",   # 3²/3=9/3=3
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
            fp = d["question_en"][:80]
            if fp in existing_short:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
            inserted += 1

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
