"""
seed_reasoning_number_series_sheet3.py
========================================
Seeds Number Series Q16-Q24 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Number Series
Run     : python seed_reasoning_number_series_sheet3.py

Answer key (verified via Python):
  Q16  2,15,41,80,?              diffs 13,26,39,52 (+13 each)          → D  132
  Q17  6,17,39,72,?              diffs 11,22,33,44 (+11 each)          → C  116
  Q18  325,259,204,160,127,105,? diffs -66,-55,-44,-33,-22,-11         → A  94
  Q19  1,4,10,22,46,?            diffs 3,6,12,24,48 (doubling)         → C  94
  Q20  0.5,0.55,0.65,0.8,?       diffs 0.05,0.10,0.15,0.20 (+0.05)    → C  1
  Q21  5,6,9,15,?,40             diffs 1,3,6,10,15 (triangular)        → B  25
  Q22  2,3,5,7,11,?,17           consecutive prime numbers              → B  13
  Q23  4,9,25,?,121,169,289,361  squares of consecutive primes          → A  49
  Q24  1,9,25,49,81,?            squares of odd numbers (1²,3²,…,11²)  → C  121
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Number_Series_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Number Series"

QUESTIONS = [
    # ── Q16 ── diffs increase by 13 ──────────────────────────────────────────────
    # 2→15(+13)→41(+26)→80(+39)→132(+52)
    {
        "question_number": 16,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 2, 15, 41, 80, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 2, 15, 41, 80, ?",
        "option_a": "111",
        "option_b": "120",
        "option_c": "121",
        "option_d": "132",
        "correct_answer": "D",   # diffs 13,26,39,52 → 80+52=132
    },
    # ── Q17 ── diffs increase by 11 ──────────────────────────────────────────────
    # 6→17(+11)→39(+22)→72(+33)→116(+44)
    {
        "question_number": 17,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 6, 17, 39, 72, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 6, 17, 39, 72, ?",
        "option_a": "83",
        "option_b": "94",
        "option_c": "116",
        "option_d": "127",
        "correct_answer": "C",   # diffs 11,22,33,44 → 72+44=116
    },
    # ── Q18 ── diffs decrease by 11 (−66,−55,−44,−33,−22,−11) ───────────────────
    {
        "question_number": 18,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 325, 259, 204, 160, 127, 105, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 325, 259, 204, 160, 127, 105, ?",
        "option_a": "94",
        "option_b": "96",
        "option_c": "98",
        "option_d": "100",
        "correct_answer": "A",   # diffs -66,-55,-44,-33,-22,-11 → 105-11=94
    },
    # ── Q19 ── doubling differences ──────────────────────────────────────────────
    # diffs: 3,6,12,24,48 → 46+48=94
    {
        "question_number": 19,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 1, 4, 10, 22, 46, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 1, 4, 10, 22, 46, ?",
        "option_a": "64",
        "option_b": "86",
        "option_c": "94",
        "option_d": "122",
        "correct_answer": "C",   # diffs double 3,6,12,24,48 → 46+48=94
    },
    # ── Q20 ── diffs increase by 0.05 ────────────────────────────────────────────
    # 0.5→0.55(+0.05)→0.65(+0.10)→0.80(+0.15)→1.0(+0.20)
    {
        "question_number": 20,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 0.5, 0.55, 0.65, 0.8, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 0.5, 0.55, 0.65, 0.8, ?",
        "option_a": "0.9",
        "option_b": "0.82",
        "option_c": "1",
        "option_d": "0.95",
        "correct_answer": "C",   # diffs 0.05,0.10,0.15,0.20 → 0.8+0.20=1.0
    },
    # ── Q21 ── triangular-number differences (1,3,6,10,15) ───────────────────────
    # 5→6(+1)→9(+3)→15(+6)→25(+10)→40(+15)
    {
        "question_number": 21,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 5, 6, 9, 15, ?, 40",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 5, 6, 9, 15, ?, 40",
        "option_a": "21",
        "option_b": "25",
        "option_c": "27",
        "option_d": "33",
        "correct_answer": "B",   # triangular diffs 1,3,6,10,15 → 15+10=25
    },
    # ── Q22 ── consecutive prime numbers ─────────────────────────────────────────
    # 2,3,5,7,11,13,17
    {
        "question_number": 22,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 2, 3, 5, 7, 11, ?, 17",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 2, 3, 5, 7, 11, ?, 17",
        "option_a": "12",
        "option_b": "13",
        "option_c": "14",
        "option_d": "15",
        "correct_answer": "B",   # consecutive primes → 13
    },
    # ── Q23 ── squares of consecutive primes ─────────────────────────────────────
    # 2²=4, 3²=9, 5²=25, 7²=49, 11²=121, 13²=169, 17²=289, 19²=361
    {
        "question_number": 23,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 4, 9, 25, ?, 121, 169, 289, 361",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 4, 9, 25, ?, 121, 169, 289, 361",
        "option_a": "49",
        "option_b": "64",
        "option_c": "81",
        "option_d": "87",
        "correct_answer": "A",   # squares of primes 2,3,5,7,11,... → 7²=49
    },
    # ── Q24 ── squares of odd numbers ────────────────────────────────────────────
    # 1²=1, 3²=9, 5²=25, 7²=49, 9²=81, 11²=121
    {
        "question_number": 24,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 1, 9, 25, 49, 81, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 1, 9, 25, 49, 81, ?",
        "option_a": "100",
        "option_b": "112",
        "option_c": "121",
        "option_d": "144",
        "correct_answer": "C",   # squares of odd numbers 1,3,5,7,9,11 → 11²=121
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
