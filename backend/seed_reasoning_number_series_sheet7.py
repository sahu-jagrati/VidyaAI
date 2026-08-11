"""
seed_reasoning_number_series_sheet7.py
========================================
Seeds Number Series Q52-Q60 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Number Series
Run     : python seed_reasoning_number_series_sheet7.py

Answer key (verified via Python):
  Q52  563,647,479,815,?          diffs ×(−2): +84,−168,+336,−672        → D  143
  Q53  5,2,7,9,16,25,?            Fibonacci-like (each = prev two sum)    → A  41
  Q54  10,14,26,42,70,?           diffs also Fibonacci: 4,12,16,28,44    → D  114
  Q55  2,8,16,128,?               each = product of previous two          → C  2048
  Q56  3,10,101,?                 each = prev²+1                          → C  10202
  Q57  589654237,89654237,...,?   alternately remove 1st / last digit     → D  96542
  Q58  5824,5242,?,4247,3823      subtract number with last digit removed  → B  4718
  Q59  1,3,4,8,15,27,?            each = sum of previous three terms      → C  50
  Q60  66,36,18,?                 multiply the digits of each term        → C  8
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Number_Series_Sheet7"
SUBJECT = "Reasoning"
TOPIC   = "Number Series"

QUESTIONS = [
    # ── Q52 ── differences multiply by −2 each step ───────────────────────────────
    # diffs: +84, −168, +336, −672 → 815+(−672)=143
    {
        "question_number": 52,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 563, 647, 479, 815, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 563, 647, 479, 815, ?",
        "option_a": "672",
        "option_b": "386",
        "option_c": "279",
        "option_d": "143",
        "correct_answer": "D",   # diffs ×(−2) → +84,−168,+336,−672 → 815−672=143
    },
    # ── Q53 ── Fibonacci-like: each term = sum of previous two ────────────────────
    # 5,2,7(5+2),9(2+7),16(7+9),25(9+16),41(16+25)
    {
        "question_number": 53,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 5, 2, 7, 9, 16, 25, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 5, 2, 7, 9, 16, 25, ?",
        "option_a": "41",
        "option_b": "45",
        "option_c": "48",
        "option_d": "52",
        "correct_answer": "A",   # Fibonacci-like → 16+25=41
    },
    # ── Q54 ── differences follow Fibonacci pattern ───────────────────────────────
    # diffs: 4,12,16(4+12),28(12+16),44(16+28) → 70+44=114
    {
        "question_number": 54,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 10, 14, 26, 42, 70, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 10, 14, 26, 42, 70, ?",
        "option_a": "100",
        "option_b": "102",
        "option_c": "106",
        "option_d": "114",
        "correct_answer": "D",   # Fibonacci diffs 4,12,16,28,44 → 70+44=114
    },
    # ── Q55 ── each term = product of previous two terms ─────────────────────────
    # 2×8=16, 8×16=128, 16×128=2048
    {
        "question_number": 55,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 2, 8, 16, 128, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 2, 8, 16, 128, ?",
        "option_a": "2042",
        "option_b": "2046",
        "option_c": "2048",
        "option_d": "2056",
        "correct_answer": "C",   # each = prev two product → 16×128=2048
    },
    # ── Q56 ── each term = previous term squared + 1 ─────────────────────────────
    # 3²+1=10, 10²+1=101, 101²+1=10202
    {
        "question_number": 56,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 3, 10, 101, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 3, 10, 101, ?",
        "option_a": "10101",
        "option_b": "10201",
        "option_c": "10202",
        "option_d": "11012",
        "correct_answer": "C",   # prev²+1 → 101²+1=10202
    },
    # ── Q57 ── alternately remove first digit / last digit ───────────────────────
    # 589654237→89654237(−1st)→8965423(−last)→965423(−1st)→96542(−last)
    {
        "question_number": 57,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 589654237, 89654237, 8965423, 965423, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 589654237, 89654237, 8965423, 965423, ?",
        "option_a": "58965",
        "option_b": "65423",
        "option_c": "89654",
        "option_d": "96542",
        "correct_answer": "D",   # alternately remove 1st/last digit → 96542
    },
    # ── Q58 ── subtract the number formed by removing the last digit ──────────────
    # 5824−582=5242, 5242−524=4718, 4718−471=4247, 4247−424=3823
    {
        "question_number": 58,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 5824, 5242, ?, 4247, 3823",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 5824, 5242, ?, 4247, 3823",
        "option_a": "4467",
        "option_b": "4718",
        "option_c": "4856",
        "option_d": "5164",
        "correct_answer": "B",   # subtract n//10 each step → 5242−524=4718
    },
    # ── Q59 ── each term = sum of previous THREE terms ────────────────────────────
    # 1+3+4=8, 3+4+8=15, 4+8+15=27, 8+15+27=50
    {
        "question_number": 59,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 1, 3, 4, 8, 15, 27, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 1, 3, 4, 8, 15, 27, ?",
        "option_a": "37",
        "option_b": "44",
        "option_c": "50",
        "option_d": "55",
        "correct_answer": "C",   # sum of prev 3 → 8+15+27=50
    },
    # ── Q60 ── multiply the digits of each term ───────────────────────────────────
    # 6×6=36, 3×6=18, 1×8=8
    {
        "question_number": 60,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 66, 36, 18, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 66, 36, 18, ?",
        "option_a": "3",
        "option_b": "6",
        "option_c": "8",
        "option_d": "9",
        "correct_answer": "C",   # multiply digits: 1×8=8
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
