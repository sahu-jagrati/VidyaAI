"""
seed_reasoning_number_series_sheet2.py
========================================
Seeds Number Series Q8-Q15 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Number Series
Run     : python seed_reasoning_number_series_sheet2.py

Answer key (verified via Python pattern check):
  Q8   120,99,80,63,48,?         diffs: -21,-19,-17,-15,-13 (+2 each step)     → A  35
  Q9   22,24,28,?,52,84          diffs: 2,4,8,16,32 (doubling)                 → A  36
  Q10  4832,5840,6848,?          constant diff 1008                             → C  7856
  Q11  10,100,200,310,?          diffs: 90,100,110,120 (+10 each)              → D  430
  Q12  0,2,8,14,?,34             diffs: 2,6,6,10,10 (each diff appears twice)  → C  24
  Q13  28,33,31,36,?,39          alternating +5,-2                             → B  34
  Q14  125,80,45,20,?            diffs: -45,-35,-25,-15 (+10 each step)        → A  5
  Q15  1,5,13,25,41,?            diffs: 4,8,12,16,20 (+4 each)                → C  61
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Number_Series_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Number Series"

QUESTIONS = [
    # ── Q8 ── decreasing diffs, each less negative by 2 ─────────────────────────
    # diffs: -21,-19,-17,-15,-13 → 48-13=35
    {
        "question_number": 8,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 120, 99, 80, 63, 48, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 120, 99, 80, 63, 48, ?",
        "option_a": "35",
        "option_b": "38",
        "option_c": "39",
        "option_d": "40",
        "correct_answer": "A",   # diffs -21,-19,-17,-15,-13 → 48-13=35
    },
    # ── Q9 ── doubling differences ───────────────────────────────────────────────
    # diffs: 2,4,8,16,32 → 28+8=36 → 36+16=52 → 52+32=84 ✓
    {
        "question_number": 9,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 22, 24, 28, ?, 52, 84",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 22, 24, 28, ?, 52, 84",
        "option_a": "36",
        "option_b": "38",
        "option_c": "42",
        "option_d": "46",
        "correct_answer": "A",   # diffs double: 2,4,8,16,32 → 28+8=36
    },
    # ── Q10 ── constant difference 1008 ──────────────────────────────────────────
    # 4832+1008=5840, 5840+1008=6848, 6848+1008=7856
    {
        "question_number": 10,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 4832, 5840, 6848, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 4832, 5840, 6848, ?",
        "option_a": "7815",
        "option_b": "7846",
        "option_c": "7856",
        "option_d": "7887",
        "correct_answer": "C",   # constant diff 1008 → 6848+1008=7856
    },
    # ── Q11 ── differences increasing by 10 ──────────────────────────────────────
    # diffs: 90,100,110,120 → 310+120=430
    {
        "question_number": 11,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 10, 100, 200, 310, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 10, 100, 200, 310, ?",
        "option_a": "400",
        "option_b": "410",
        "option_c": "420",
        "option_d": "430",
        "correct_answer": "D",   # diffs 90,100,110,120 → 310+120=430
    },
    # ── Q12 ── each diff appears twice: 2,6,6,10,10 ─────────────────────────────
    # 0→2(+2)→8(+6)→14(+6)→24(+10)→34(+10)
    {
        "question_number": 12,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 0, 2, 8, 14, ?, 34",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 0, 2, 8, 14, ?, 34",
        "option_a": "20",
        "option_b": "23",
        "option_c": "24",
        "option_d": "25",
        "correct_answer": "C",   # diffs 2,6,6,10,10 → 14+10=24
    },
    # ── Q13 ── alternating +5, -2 ────────────────────────────────────────────────
    # 28→33(+5)→31(-2)→36(+5)→34(-2)→39(+5)
    {
        "question_number": 13,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 28, 33, 31, 36, ?, 39",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 28, 33, 31, 36, ?, 39",
        "option_a": "32",
        "option_b": "34",
        "option_c": "38",
        "option_d": "40",
        "correct_answer": "B",   # alternating +5,-2 → 36-2=34
    },
    # ── Q14 ── differences decrease by 10 ────────────────────────────────────────
    # diffs: -45,-35,-25,-15 → 20-15=5
    {
        "question_number": 14,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 125, 80, 45, 20, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 125, 80, 45, 20, ?",
        "option_a": "5",
        "option_b": "8",
        "option_c": "10",
        "option_d": "12",
        "correct_answer": "A",   # diffs -45,-35,-25,-15 → 20-15=5
    },
    # ── Q15 ── differences increase by 4 ─────────────────────────────────────────
    # diffs: 4,8,12,16,20 → 41+20=61
    {
        "question_number": 15,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 1, 5, 13, 25, 41, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 1, 5, 13, 25, 41, ?",
        "option_a": "51",
        "option_b": "57",
        "option_c": "61",
        "option_d": "63",
        "correct_answer": "C",   # diffs 4,8,12,16,20 → 41+20=61
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
