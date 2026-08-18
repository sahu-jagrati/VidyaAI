"""
seed_reasoning_missing_number_sheet2.py
=========================================
Seeds Missing Number Q11-Q19 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Missing Number
Run     : python seed_reasoning_missing_number_sheet2.py

Answer key (all verified via Python):
  Q11  5 7 9 || 9 6 4 || 36 36 ?         (R1×R2)−R2=R3; (9×4)−4=32        → B  32
  Q12  5 17 9 || 3 21 7 || 7 16 8 || ... row sum=31; 6+10+?=31→15          → C  15
  Q13  header 874, rows 1 3 5 / 2 4 6...  3-digit sum=874; 174→?=4         → A  4
  Q14  4 3 2 8 32 || ... 2 9 4 12 ?      (C1×C2×C3)+C4=C5; (2×9×4)+12=84 → B  84
  Q15  2 3 8 || 4 5 10 || ... 32 50 ?    (R1+R3)×R2=R4; (8+12)×10=200    → A  200
  Q16  1 216 343 || 8 125 512 || 27 64 ? cubes: 9³=729                    → C  729
  Q17  circle: 5,10,?,50,122 (clockwise) p²+1 primes; 5²+1=26             → A  26
  Q18  two circles: (TL×TR)−(BL×BR)=ctr (14×10)−(7×8)=84                → A  84
  Q19  9 11 13 || 13 15 17 || ... 11 13 ? each row +2 across; 11→13→15    → B  15
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Missing_Number_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Missing Number"

QUESTIONS = [
    # ── Q11 ── (Row1 × Row2) − Row2 = Row3 per column ────────────────────────
    # C1:(5×9)−9=36 ✓  C2:(7×6)−6=36 ✓  C3:(9×4)−4=32
    {
        "question_number": 11,
        "difficulty": "easy",
        "question_en": "Find the missing number in the matrix: 5 7 9 || 9 6 4 || 36 36 ?",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 5 7 9 || 9 6 4 || 36 36 ?",
        "option_a": "40",
        "option_b": "32",
        "option_c": "36",
        "option_d": "42",
        "correct_answer": "B",   # (9×4)−4=32
    },
    # ── Q12 ── sum of each row = 31 ──────────────────────────────────────────
    # R1:5+17+9=31 ✓  R2:3+21+7=31 ✓  R3:7+16+8=31 ✓  R4:6+10+?=31→?=15
    {
        "question_number": 12,
        "difficulty": "easy",
        "question_en": "Find the missing number in the matrix: 5 17 9 || 3 21 7 || 7 16 8 || 6 10 ?",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 5 17 9 || 3 21 7 || 7 16 8 || 6 10 ?",
        "option_a": "10",
        "option_b": "12",
        "option_c": "15",
        "option_d": "16",
        "correct_answer": "C",   # row sum=31: 6+10+?=31 → ?=15
    },
    # ── Q13 ── 3-digit numbers formed by rows sum to header 874 ───────────────
    # 135+246+319+17?=874 → 700+17?=874 → 17?=174 → ?=4
    {
        "question_number": 13,
        "difficulty": "medium",
        "question_en": (
            "Header number is 874. Find the missing digit in the table: "
            "1 3 5 || 2 4 6 || 3 1 9 || 1 7 ? "
            "(each row forms a 3-digit number; their sum equals 874)"
        ),
        "question_hi": (
            "हेडर संख्या 874 है। तालिका में लुप्त अंक ज्ञात कीजिए: "
            "1 3 5 || 2 4 6 || 3 1 9 || 1 7 ? "
            "(प्रत्येक पंक्ति एक 3-अंकीय संख्या बनाती है; उनका योग 874 होता है)"
        ),
        "option_a": "4",
        "option_b": "6",
        "option_c": "8",
        "option_d": "2",
        "correct_answer": "A",   # 135+246+319+174=874 → ?=4
    },
    # ── Q14 ── (Col1 × Col2 × Col3) + Col4 = Col5 ────────────────────────────
    # R1:(4×3×2)+8=32 ✓  R2:(5×3×1)+9=24 ✓  R3:(7×3×3)+7=70 ✓  R4:(2×9×4)+12=84
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": "Find the missing number in the matrix: 4 3 2 8 32 || 5 3 1 9 24 || 7 3 3 7 70 || 2 9 4 12 ?",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 4 3 2 8 32 || 5 3 1 9 24 || 7 3 3 7 70 || 2 9 4 12 ?",
        "option_a": "60",
        "option_b": "84",
        "option_c": "120",
        "option_d": "27",
        "correct_answer": "B",   # (2×9×4)+12=72+12=84
    },
    # ── Q15 ── (Row1 + Row3) × Row2 = Row4 per column ────────────────────────
    # C1:(2+6)×4=32 ✓  C2:(3+7)×5=50 ✓  C3:(8+12)×10=200
    {
        "question_number": 15,
        "difficulty": "medium",
        "question_en": "Find the missing number in the matrix: 2 3 8 || 4 5 10 || 6 7 12 || 32 50 ?",
        "question_hi": "आव्यूह में लुप्त संख्या ज्ञात कीजिए: 2 3 8 || 4 5 10 || 6 7 12 || 32 50 ?",
        "option_a": "200",
        "option_b": "92",
        "option_c": "128",
        "option_d": "30",
        "correct_answer": "A",   # (8+12)×10=200
    },
    # ── Q16 ── each cell is n³; col bases: (1,2,3),(6,5,4),(7,8,9) ───────────
    # C1:1³,2³,3³=1,8,27  C2:6³,5³,4³=216,125,64  C3:7³,8³,9³=343,512,729
    # Bottom row = sum of col − row_index² (verification): 35,401,1575
    {
        "question_number": 16,
        "difficulty": "hard",
        "question_en": "Find the missing number in the cube matrix: 1 216 343 || 8 125 512 || 27 64 ? || 35 401 1575",
        "question_hi": "घन आव्यूह में लुप्त संख्या ज्ञात कीजिए: 1 216 343 || 8 125 512 || 27 64 ? || 35 401 1575",
        "option_a": "615",
        "option_b": "575",
        "option_c": "729",
        "option_d": "340",
        "correct_answer": "C",   # 9³=729 (col3 bases are 7,8,9)
    },
    # ── Q17 ── circle divided into 5 sections; clockwise: p²+1 for primes ────
    # Primes 2,3,5,7,11 → p²+1: 5,10,26,50,122 (clockwise)
    # Given: 5,10,?,50,122 → missing = 5²+1 = 26
    {
        "question_number": 17,
        "difficulty": "hard",
        "question_en": (
            "In the circular diagram, numbers are placed in 5 sections clockwise as: "
            "5, 10, ?, 50, 122. Find the missing number."
        ),
        "question_hi": (
            "वृत्ताकार आरेख में 5 खंडों में दक्षिणावर्त संख्याएँ हैं: "
            "5, 10, ?, 50, 122। लुप्त संख्या ज्ञात कीजिए।"
        ),
        "option_a": "26",
        "option_b": "27",
        "option_c": "25",
        "option_d": "23",
        "correct_answer": "A",   # p²+1 for primes: 5²+1=26
    },
    # ── Q18 ── two circles: (TL×TR)−(BL×BR) = center ──────────────────────
    # Circle1: (11×12)−(6×9)=132−54=78 ✓  Circle2: (14×10)−(7×8)=140−56=84
    {
        "question_number": 18,
        "difficulty": "medium",
        "question_en": (
            "Two circles: Circle 1 has top-left=11, top-right=12, bottom-left=6, "
            "bottom-right=9, center=78. Circle 2 has top-left=14, top-right=10, "
            "bottom-left=7, bottom-right=8, center=?. Find the missing center value."
        ),
        "question_hi": (
            "दो वृत्त: वृत्त 1 में ऊपर-बाएँ=11, ऊपर-दाएँ=12, नीचे-बाएँ=6, "
            "नीचे-दाएँ=9, केंद्र=78। वृत्त 2 में ऊपर-बाएँ=14, ऊपर-दाएँ=10, "
            "नीचे-बाएँ=7, नीचे-दाएँ=8, केंद्र=?। लुप्त केंद्र मान ज्ञात कीजिए।"
        ),
        "option_a": "84",
        "option_b": "74",
        "option_c": "94",
        "option_d": "104",
        "correct_answer": "A",   # (14×10)−(7×8)=140−56=84
    },
    # ── Q19 ── 5×3 grid; each row increases by +2 across columns ─────────────
    # Cols increase +4,−3,+4,−3 down; rows always +2 across
    # R1:9,11,13  R2:13,15,17  R3:10,12,14  R4:14,16,18  R5:11,13,?=15
    {
        "question_number": 19,
        "difficulty": "easy",
        "question_en": "Find the missing number in the grid: 9 11 13 || 13 15 17 || 10 12 14 || 14 16 18 || 11 13 ?",
        "question_hi": "ग्रिड में लुप्त संख्या ज्ञात कीजिए: 9 11 13 || 13 15 17 || 10 12 14 || 14 16 18 || 11 13 ?",
        "option_a": "14",
        "option_b": "15",
        "option_c": "21",
        "option_d": "22",
        "correct_answer": "B",   # row5: 11+2+2=15
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
