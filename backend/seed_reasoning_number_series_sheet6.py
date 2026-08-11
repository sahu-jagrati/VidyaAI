"""
seed_reasoning_number_series_sheet6.py
========================================
Seeds Number Series Q43-Q51 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Number Series
Run     : python seed_reasoning_number_series_sheet6.py

Answer key (verified via Python):
  Q43  6,13,28,59,?              each×2+n  (n=1,2,3,4)                  → D  122
  Q44  3,7,23,95,?               each×n+(n-1)  (n=2,3,4,5)              → C  479
  Q45  2,3,8,27,112,?            each×n+n  (n=1,2,3,4,5)                → D  565
  Q46  1,5,14,30,55,91,?         diffs 2²,3²,4²,5²,6²,7²               → B  140
  Q47  198,194,185,169,?         diffs −2²,−3²,−4²,−5²                  → D  144
  Q48  2,2,5,13,28,?             diffs n²−1 (n=1→5)                     → D  52
  Q49  2,7,27,107,427,?          each×4−1                               → B  1707
  Q50  24,60,120,210,?           n(n+1)(n+2) for n=2→6                  → B  336
  Q51  3,12,27,48,75,108,?       3n² for n=1→7                          → A  147
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Number_Series_Sheet6"
SUBJECT = "Reasoning"
TOPIC   = "Number Series"

QUESTIONS = [
    # ── Q43 ── each term = prev×2 + n (n=1,2,3,4) ───────────────────────────────
    # 6×2+1=13, 13×2+2=28, 28×2+3=59, 59×2+4=122
    {
        "question_number": 43,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 6, 13, 28, 59, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 6, 13, 28, 59, ?",
        "option_a": "201",
        "option_b": "202",
        "option_c": "203",
        "option_d": "122",
        "correct_answer": "D",   # ×2+n pattern → 59×2+4=122
    },
    # ── Q44 ── each term = prev×n + (n−1) for n=2,3,4,5 ─────────────────────────
    # 3×2+1=7, 7×3+2=23, 23×4+3=95, 95×5+4=479
    {
        "question_number": 44,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 3, 7, 23, 95, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 3, 7, 23, 95, ?",
        "option_a": "62",
        "option_b": "128",
        "option_c": "479",
        "option_d": "575",
        "correct_answer": "C",   # ×n+(n-1) → 95×5+4=479
    },
    # ── Q45 ── each term = prev×n + n for n=1,2,3,4,5 ───────────────────────────
    # 2×1+1=3, 3×2+2=8, 8×3+3=27, 27×4+4=112, 112×5+5=565
    {
        "question_number": 45,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 2, 3, 8, 27, 112, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 2, 3, 8, 27, 112, ?",
        "option_a": "226",
        "option_b": "339",
        "option_c": "452",
        "option_d": "565",
        "correct_answer": "D",   # ×n+n → 112×5+5=565
    },
    # ── Q46 ── differences are 2²,3²,4²,5²,6²,7² ────────────────────────────────
    # 1+4=5, 5+9=14, 14+16=30, 30+25=55, 55+36=91, 91+49=140
    {
        "question_number": 46,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 1, 5, 14, 30, 55, 91, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 1, 5, 14, 30, 55, 91, ?",
        "option_a": "130",
        "option_b": "140",
        "option_c": "150",
        "option_d": "160",
        "correct_answer": "B",   # diffs 4,9,16,25,36,49 (n²) → 91+49=140
    },
    # ── Q47 ── differences are −2²,−3²,−4²,−5² ──────────────────────────────────
    # 198−4=194, 194−9=185, 185−16=169, 169−25=144
    {
        "question_number": 47,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 198, 194, 185, 169, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 198, 194, 185, 169, ?",
        "option_a": "92",
        "option_b": "112",
        "option_c": "136",
        "option_d": "144",
        "correct_answer": "D",   # diffs −2²,−3²,−4²,−5² → 169−25=144
    },
    # ── Q48 ── differences are n²−1 for n=1,2,3,4,5 ─────────────────────────────
    # diffs: 0,3,8,15,24 → 2+0=2, 2+3=5, 5+8=13, 13+15=28, 28+24=52
    {
        "question_number": 48,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 2, 2, 5, 13, 28, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 2, 2, 5, 13, 28, ?",
        "option_a": "49",
        "option_b": "50",
        "option_c": "51",
        "option_d": "52",
        "correct_answer": "D",   # diffs n²−1 (0,3,8,15,24) → 28+24=52
    },
    # ── Q49 ── each term = prev×4 − 1 ────────────────────────────────────────────
    # 2×4−1=7, 7×4−1=27, 27×4−1=107, 107×4−1=427, 427×4−1=1707
    {
        "question_number": 49,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 2, 7, 27, 107, 427, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 2, 7, 27, 107, 427, ?",
        "option_a": "1262",
        "option_b": "1707",
        "option_c": "4027",
        "option_d": "4207",
        "correct_answer": "B",   # ×4−1 → 427×4−1=1707
    },
    # ── Q50 ── n×(n+1)×(n+2) for n = 2, 3, 4, 5, 6 ─────────────────────────────
    # 2×3×4=24, 3×4×5=60, 4×5×6=120, 5×6×7=210, 6×7×8=336
    {
        "question_number": 50,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 24, 60, 120, 210, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 24, 60, 120, 210, ?",
        "option_a": "300",
        "option_b": "336",
        "option_c": "420",
        "option_d": "525",
        "correct_answer": "B",   # n(n+1)(n+2) → 6×7×8=336
    },
    # ── Q51 ── 3n² for n = 1, 2, 3, 4, 5, 6, 7 ──────────────────────────────────
    # 3×1=3, 3×4=12, 3×9=27, 3×16=48, 3×25=75, 3×36=108, 3×49=147
    {
        "question_number": 51,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 3, 12, 27, 48, 75, 108, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 3, 12, 27, 48, 75, 108, ?",
        "option_a": "147",
        "option_b": "162",
        "option_c": "183",
        "option_d": "192",
        "correct_answer": "A",   # 3n² → 3×7²=147
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
