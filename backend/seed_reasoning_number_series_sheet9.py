"""
seed_reasoning_number_series_sheet9.py
========================================
Seeds Number Series Q69-Q77 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Number Series
Run     : python seed_reasoning_number_series_sheet9.py

Answer key (verified via Python):
  Q69  3,4,7,7,13,13,21,22,31,34,?     two interleaved APs (even diffs)   → B  43
  Q70  11,10,?,100,1001,1000,10001      alternates 10ⁿ+1 and 10ⁿ          → A  101
  Q71  13,32,24,43,35,?,46,65,57,76    two interleaved APs d=+11           → C  54
  Q72  0,4,6,3,7,9,6,?,12              groups of 3 with +4,+2 pattern      → B  10
  Q73  2,1,2,4,4,5,6,7,8,8,10,11,?    three interleaved APs               → B  10
  Q74  8,9,8,7,10,9,6,11,10,?,12      triples: 1st−1, 2nd+1, 3rd+1       → A  5
  Q75  90,180,12,50,100,200,?,3,50,... triplet product: first=second×third  → A  150
  Q76  2/3,4/7,?,11/21,16/31           nums +2,+3,+4,+5; dens +4,+6,+8,+10 → C  7/13
  Q77  4/9,9/20,?,39/86                num 2Nₙ₋₁+1; den 2Dₙ₋₁+2           → B  19/42
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Number_Series_Sheet9"
SUBJECT = "Reasoning"
TOPIC   = "Number Series"

QUESTIONS = [
    # ── Q69 ── two interleaved APs with increasing even differences ───────────────
    # Odd(1,3,5,7,9,11): 3,7,13,21,31,43  diffs +4,+6,+8,+10,+12
    # Even(2,4,6,8,10):  4,7,13,22,34     diffs +3,+6,+9,+12
    {
        "question_number": 69,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 3, 4, 7, 7, 13, 13, 21, 22, 31, 34, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 3, 4, 7, 7, 13, 13, 21, 22, 31, 34, ?",
        "option_a": "42",
        "option_b": "43",
        "option_c": "51",
        "option_d": "52",
        "correct_answer": "B",   # odd-series: 31+12=43
    },
    # ── Q70 ── alternates 10ⁿ+1 and 10ⁿ for n=1,2,3,4 ──────────────────────────
    # 11(10¹+1), 10(10¹), ?(10²+1=101), 100(10²), 1001(10³+1), 1000(10³), 10001(10⁴+1)
    {
        "question_number": 70,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 11, 10, ?, 100, 1001, 1000, 10001",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 11, 10, ?, 100, 1001, 1000, 10001",
        "option_a": "101",
        "option_b": "110",
        "option_c": "111",
        "option_d": "None of these",
        "correct_answer": "A",   # 10²+1=101
    },
    # ── Q71 ── two interleaved APs each with d=+11 ───────────────────────────────
    # Odd positions: 13,24,35,46,57  (d=+11)
    # Even positions: 32,43,54,65,76  (d=+11) → 6th term (3rd even) = 54
    {
        "question_number": 71,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 13, 32, 24, 43, 35, ?, 46, 65, 57, 76",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 13, 32, 24, 43, 35, ?, 46, 65, 57, 76",
        "option_a": "45",
        "option_b": "52",
        "option_c": "54",
        "option_d": "55",
        "correct_answer": "C",   # even-series: 43+11=54
    },
    # ── Q72 ── groups of 3 with internal pattern +4, +2 ──────────────────────────
    # (0,4,6): 0+4=4, 4+2=6 ✓
    # (3,7,9): 3+4=7, 7+2=9 ✓
    # (6,?,12): 6+4=10, 10+2=12 ✓
    {
        "question_number": 72,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 0, 4, 6, 3, 7, 9, 6, ?, 12",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 0, 4, 6, 3, 7, 9, 6, ?, 12",
        "option_a": "8",
        "option_b": "10",
        "option_c": "11",
        "option_d": "14",
        "correct_answer": "B",   # group 3: 6+4=10 ✓
    },
    # ── Q73 ── three interleaved APs ─────────────────────────────────────────────
    # s1(pos 1,4,7,10,13): 2,4,6,8,10  (+2 each)
    # s2(pos 2,5,8,11):    1,4,7,10    (+3 each)
    # s3(pos 3,6,9,12):    2,5,8,11    (+3 each)
    # 13th term belongs to s1: 8+2=10
    {
        "question_number": 73,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 2, 1, 2, 4, 4, 5, 6, 7, 8, 8, 10, 11, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 2, 1, 2, 4, 4, 5, 6, 7, 8, 8, 10, 11, ?",
        "option_a": "9",
        "option_b": "10",
        "option_c": "11",
        "option_d": "12",
        "correct_answer": "B",   # s1's 5th term: 8+2=10
    },
    # ── Q74 ── non-overlapping triples: 1st−1, 2nd+1, 3rd+1 ─────────────────────
    # Triple 1: (8,9,8), Triple 2: (7,10,9), Triple 3: (6,11,10), Triple 4: (5,12,11)
    {
        "question_number": 74,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 8, 9, 8, 7, 10, 9, 6, 11, 10, ?, 12",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 8, 9, 8, 7, 10, 9, 6, 11, 10, ?, 12",
        "option_a": "5",
        "option_b": "7",
        "option_c": "8",
        "option_d": "11",
        "correct_answer": "A",   # 1st of triple 4: 6−1=5
    },
    # ── Q75 ── triplet product pattern: first = second × third ───────────────────
    # Groups: (90,180,12),(50,100,200),(?,3,50),(4,25,2),(6,30,3)
    # For (?,3,50): ? = 3×50 = 150
    {
        "question_number": 75,
        "difficulty": "hard",
        "question_en": "Find the missing number in the series: 90, 180, 12, 50, 100, 200, ?, 3, 50, 4, 25, 2, 6, 30, 3",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 90, 180, 12, 50, 100, 200, ?, 3, 50, 4, 25, 2, 6, 30, 3",
        "option_a": "150",
        "option_b": "175",
        "option_c": "225",
        "option_d": "250",
        "correct_answer": "A",   # triplet (?,3,50): ?=3×50=150
    },
    # ── Q76 ── fraction series: numerators and denominators follow separate APs ──
    # Full series: 2/3, 4/7, 7/13, 11/21, 16/31  (middle term missing)
    # Numerators: 2,4,7,11,16  diffs +2,+3,+4,+5
    # Denominators: 3,7,13,21,31  diffs +4,+6,+8,+10
    # Missing 3rd term: 7/13
    {
        "question_number": 76,
        "difficulty": "medium",
        "question_en": "Find the missing fraction in the series: 2/3, 4/7, ?, 11/21, 16/31",
        "question_hi": "श्रृंखला में लुप्त भिन्न ज्ञात कीजिए: 2/3, 4/7, ?, 11/21, 16/31",
        "option_a": "5/9",
        "option_b": "6/11",
        "option_c": "7/13",
        "option_d": "9/17",
        "correct_answer": "C",   # nums:2,4,7 (+2,+3) dens:3,7,13 (+4,+6) → 7/13
    },
    # ── Q77 ── fraction series with recursive formulas ────────────────────────────
    # Full series: 4/9, 9/20, 19/42, 39/86  (3rd term missing)
    # Numerators:   N_n = 2×N_{n-1}+1: 4,9,19,39
    # Denominators: D_n = 2×D_{n-1}+2: 9,20,42,86
    # Missing 3rd term: 19/42
    {
        "question_number": 77,
        "difficulty": "medium",
        "question_en": "Find the missing fraction in the series: 4/9, 9/20, ?, 39/86",
        "question_hi": "श्रृंखला में लुप्त भिन्न ज्ञात कीजिए: 4/9, 9/20, ?, 39/86",
        "option_a": "17/40",
        "option_b": "19/42",
        "option_c": "20/45",
        "option_d": "29/53",
        "correct_answer": "B",   # N=2×9+1=19, D=2×20+2=42 → 19/42
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

            db.add(Question(
                subject    = SUBJECT,
                topic      = TOPIC,
                source_pdf = SOURCE,
                **d,
            ))
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
