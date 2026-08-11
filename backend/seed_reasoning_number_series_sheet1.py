"""
seed_reasoning_number_series_sheet1.py
========================================
Seeds Number Series Q1-Q7 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Number Series
Run     : python seed_reasoning_number_series_sheet1.py

Answer key (verified via Python pattern check):
  Q1   1,9,25,49,?,121           squares of odd numbers (1²,3²,5²,7²,9²,11²)  → B  81
  Q2   4,7,12,19,28,?            diffs: 3,5,7,9,11 (+2 each)                   → C  39
  Q3   11,13,17,19,23,25,?       alternating +2,+4                             → C  29
  Q4   6,12,21,?,48              diffs: 6,9,12,15 (+3 each)                    → A  33
  Q5   2,5,9,?,20,27             diffs: 3,4,5,6,7 (+1 each)                   → A  14
  Q6   6,11,21,36,56,?           diffs: 5,10,15,20,25 (+5 each)               → C  81
  Q7   10,18,28,40,54,70,?       diffs: 8,10,12,14,16,18 (+2 each)            → D  88
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Number_Series_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Number Series"

QUESTIONS = [
    # ── Q1 ── squares of odd numbers ─────────────────────────────────────────────
    # 1²=1, 3²=9, 5²=25, 7²=49, 9²=81, 11²=121
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 1, 9, 25, 49, ?, 121",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 1, 9, 25, 49, ?, 121",
        "option_a": "64",
        "option_b": "81",
        "option_c": "91",
        "option_d": "100",
        "correct_answer": "B",   # 9² = 81 (squares of 1,3,5,7,9,11)
    },
    # ── Q2 ── increasing odd differences ─────────────────────────────────────────
    # diffs: 3,5,7,9,11  → next = 28+11 = 39
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 4, 7, 12, 19, 28, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 4, 7, 12, 19, 28, ?",
        "option_a": "30",
        "option_b": "36",
        "option_c": "39",
        "option_d": "49",
        "correct_answer": "C",   # diffs 3,5,7,9,11 → 28+11=39
    },
    # ── Q3 ── alternating +2, +4 ─────────────────────────────────────────────────
    # 11→13(+2)→17(+4)→19(+2)→23(+4)→25(+2)→29(+4)
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 11, 13, 17, 19, 23, 25, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 11, 13, 17, 19, 23, 25, ?",
        "option_a": "26",
        "option_b": "27",
        "option_c": "29",
        "option_d": "37",
        "correct_answer": "C",   # alternating +2,+4 → 25+4=29
    },
    # ── Q4 ── diffs increasing by 3 ──────────────────────────────────────────────
    # 6→12(+6)→21(+9)→33(+12)→48(+15)
    {
        "question_number": 4,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 6, 12, 21, ?, 48",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 6, 12, 21, ?, 48",
        "option_a": "33",
        "option_b": "38",
        "option_c": "40",
        "option_d": "45",
        "correct_answer": "A",   # diffs 6,9,12,15 → 21+12=33
    },
    # ── Q5 ── diffs increasing by 1 ──────────────────────────────────────────────
    # 2→5(+3)→9(+4)→14(+5)→20(+6)→27(+7)
    {
        "question_number": 5,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 2, 5, 9, ?, 20, 27",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 2, 5, 9, ?, 20, 27",
        "option_a": "14",
        "option_b": "16",
        "option_c": "18",
        "option_d": "24",
        "correct_answer": "A",   # diffs 3,4,5,6,7 → 9+5=14
    },
    # ── Q6 ── diffs increasing by 5 ──────────────────────────────────────────────
    # 6→11(+5)→21(+10)→36(+15)→56(+20)→81(+25)
    {
        "question_number": 6,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 6, 11, 21, 36, 56, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 6, 11, 21, 36, 56, ?",
        "option_a": "42",
        "option_b": "51",
        "option_c": "81",
        "option_d": "91",
        "correct_answer": "C",   # diffs 5,10,15,20,25 → 56+25=81
    },
    # ── Q7 ── diffs increasing by 2 ──────────────────────────────────────────────
    # 10→18(+8)→28(+10)→40(+12)→54(+14)→70(+16)→88(+18)
    {
        "question_number": 7,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 10, 18, 28, 40, 54, 70, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 10, 18, 28, 40, 54, 70, ?",
        "option_a": "85",
        "option_b": "86",
        "option_c": "87",
        "option_d": "88",
        "correct_answer": "D",   # diffs 8,10,12,14,16,18 → 70+18=88
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
