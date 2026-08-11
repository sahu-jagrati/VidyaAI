"""
seed_reasoning_number_series_sheet4.py
========================================
Seeds Number Series Q25-Q33 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Number Series
Run     : python seed_reasoning_number_series_sheet4.py

Answer key (verified via Python):
  Q25  1,1,4,8,9,27,16,?             alternating squares & cubes (n²,n³)     → B  64
  Q26  4,12,36,108,?                 GP, ratio ×3                             → D  324
  Q27  1,1,2,6,24,?,720              factorials (0! to 6!)                    → D  120
  Q28  240,?,120,40,10,2             divide by 1,2,3,4,5 successively         → B  240
  Q29  4,6,9,13½,?                   diffs ×1.5 each step (2,3,4.5,6.75)     → C  20¼
  Q30  5760,960,?,48,16,8            divide by 6,5,4,3,2 left-to-right        → C  192
  Q31  1,2,6,7,21,22,66,67,?         alternating +1,×3                        → C  201
  Q32  48,24,96,48,192,?             alternating ÷2,×4                        → C  96
  Q33  1,2,3,6,9,18,?,54             pairs (1,2)(3,6)(9,18)(27,54), first×3   → B  27
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Number_Series_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Number Series"

QUESTIONS = [
    # ── Q25 ── alternating squares and cubes ──────────────────────────────────────
    # 1²=1, 1³=1, 2²=4, 2³=8, 3²=9, 3³=27, 4²=16, 4³=64
    {
        "question_number": 25,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 1, 1, 4, 8, 9, 27, 16, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 1, 1, 4, 8, 9, 27, 16, ?",
        "option_a": "32",
        "option_b": "64",
        "option_c": "81",
        "option_d": "256",
        "correct_answer": "B",   # alternating n² and n³ → 4³=64
    },
    # ── Q26 ── geometric progression, ratio 3 ────────────────────────────────────
    # 4×3=12, 12×3=36, 36×3=108, 108×3=324
    {
        "question_number": 26,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 4, 12, 36, 108, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 4, 12, 36, 108, ?",
        "option_a": "144",
        "option_b": "216",
        "option_c": "304",
        "option_d": "324",
        "correct_answer": "D",   # GP ratio ×3 → 108×3=324
    },
    # ── Q27 ── factorials: 0! to 6! ──────────────────────────────────────────────
    # 0!=1, 1!=1, 2!=2, 3!=6, 4!=24, 5!=120, 6!=720
    {
        "question_number": 27,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 1, 1, 2, 6, 24, ?, 720",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 1, 1, 2, 6, 24, ?, 720",
        "option_a": "100",
        "option_b": "104",
        "option_c": "108",
        "option_d": "120",
        "correct_answer": "D",   # factorials 0!→6! → 5!=120
    },
    # ── Q28 ── divide by 1,2,3,4,5 successively ─────────────────────────────────
    # 240÷1=240(?), 240÷2=120, 120÷3=40, 40÷4=10, 10÷5=2
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 240, ?, 120, 40, 10, 2",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 240, ?, 120, 40, 10, 2",
        "option_a": "180",
        "option_b": "240",
        "option_c": "420",
        "option_d": "480",
        "correct_answer": "B",   # divisors 1,2,3,4,5 → 240÷1=240
    },
    # ── Q29 ── differences multiplied by 1.5 each step ───────────────────────────
    # diffs: 2, 3, 4.5, 6.75 → 13.5+6.75=20.25=20¼
    {
        "question_number": 29,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 4, 6, 9, 13 1/2, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 4, 6, 9, 13 1/2, ?",
        "option_a": "17 1/2",
        "option_b": "19",
        "option_c": "20 1/4",
        "option_d": "22 3/4",
        "correct_answer": "C",   # diffs ×1.5: 2,3,4.5,6.75 → 13.5+6.75=20.25=20¼
    },
    # ── Q30 ── divide by 6,5,4,3,2 left-to-right ─────────────────────────────────
    # 5760÷6=960, 960÷5=192, 192÷4=48, 48÷3=16, 16÷2=8
    {
        "question_number": 30,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 5760, 960, ?, 48, 16, 8",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 5760, 960, ?, 48, 16, 8",
        "option_a": "120",
        "option_b": "160",
        "option_c": "192",
        "option_d": "240",
        "correct_answer": "C",   # divide by 6,5,4,3,2 → 960÷5=192
    },
    # ── Q31 ── alternating +1, ×3 (8 terms given, find 9th) ──────────────────────
    # 1→2(+1)→6(×3)→7(+1)→21(×3)→22(+1)→66(×3)→67(+1)→201(×3)
    {
        "question_number": 31,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 1, 2, 6, 7, 21, 22, 66, 67, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 1, 2, 6, 7, 21, 22, 66, 67, ?",
        "option_a": "70",
        "option_b": "134",
        "option_c": "201",
        "option_d": "301",
        "correct_answer": "C",   # alternating +1,×3 → 67×3=201
    },
    # ── Q32 ── alternating ÷2, ×4 ────────────────────────────────────────────────
    # 48÷2=24, 24×4=96, 96÷2=48, 48×4=192, 192÷2=96
    {
        "question_number": 32,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 48, 24, 96, 48, 192, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 48, 24, 96, 48, 192, ?",
        "option_a": "76",
        "option_b": "90",
        "option_c": "96",
        "option_d": "98",
        "correct_answer": "C",   # alternating ÷2,×4 → 192÷2=96
    },
    # ── Q33 ── pairs where 2nd = 1st×2, pair-starts multiply by 3 ─────────────────
    # (1,2), (3,6), (9,18), (27,54) → pair-starts 1,3,9,27 (×3 each)
    {
        "question_number": 33,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 1, 2, 3, 6, 9, 18, ?, 54",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 1, 2, 3, 6, 9, 18, ?, 54",
        "option_a": "18",
        "option_b": "27",
        "option_c": "36",
        "option_d": "81",
        "correct_answer": "B",   # pairs (1,2)(3,6)(9,18)(27,54) → ?=27
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
