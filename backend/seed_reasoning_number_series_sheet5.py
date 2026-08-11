"""
seed_reasoning_number_series_sheet5.py
========================================
Seeds Number Series Q34-Q42 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Number Series
Run     : python seed_reasoning_number_series_sheet5.py

Answer key (verified via Python):
  Q34  165,195,255,285,345,?           alternating +30,+60                     → A  375
  Q35  9,27,31,155,161,1127,?          ops ×3,+4,×5,+6,×7,+8                  → B  1135
  Q36  2,3,3,5,10,13,?,43,172,177      ops +1,×1,+2,×2,+3,×3,+4,×4,+5        → C  39
  Q37  3,15,?,63,99,143                diffs 12,20,28,36,44 (2nd-diff +8)      → B  35
  Q38  7,26,63,124,215,342,?           n³−1 for n=2..8                         → D  511
  Q39  3,7,15,?,63,127                 2ⁿ−1 for n=2..7                        → B  31
  Q40  4,10,?,82,244,730               3ⁿ+1 for n=1..6                        → B  28
  Q41  6,13,25,51,101,?               alternating ×2+1, ×2−1                  → C  203
  Q42  8,28,116,584,?                  each term = prev×(n+2)+4               → D  3508
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Number_Series_Sheet5"
SUBJECT = "Reasoning"
TOPIC   = "Number Series"

QUESTIONS = [
    # ── Q34 ── alternating +30, +60 ──────────────────────────────────────────────
    # 165→195(+30)→255(+60)→285(+30)→345(+60)→375(+30)
    {
        "question_number": 34,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 165, 195, 255, 285, 345, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 165, 195, 255, 285, 345, ?",
        "option_a": "375",
        "option_b": "390",
        "option_c": "420",
        "option_d": "435",
        "correct_answer": "A",   # alternating +30,+60 → 345+30=375
    },
    # ── Q35 ── alternating ×odd, +even ───────────────────────────────────────────
    # ×3,+4,×5,+6,×7,+8 → 1127+8=1135
    {
        "question_number": 35,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 9, 27, 31, 155, 161, 1127, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 9, 27, 31, 155, 161, 1127, ?",
        "option_a": "316",
        "option_b": "1135",
        "option_c": "1288",
        "option_d": "2254",
        "correct_answer": "B",   # ops ×3,+4,×5,+6,×7,+8 → 1127+8=1135
    },
    # ── Q36 ── alternating +n, ×n for n=1,2,3,4,5 ────────────────────────────────
    # +1,×1,+2,×2,+3,×3,+4,×4,+5 → 13×3=39
    {
        "question_number": 36,
        "difficulty": "hard",
        "question_en": "Find the missing number in the series: 2, 3, 3, 5, 10, 13, ?, 43, 172, 177",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 2, 3, 3, 5, 10, 13, ?, 43, 172, 177",
        "option_a": "23",
        "option_b": "38",
        "option_c": "39",
        "option_d": "40",
        "correct_answer": "C",   # ops +1,×1,+2,×2,+3,×3,+4,×4,+5 → 13×3=39
    },
    # ── Q37 ── second difference = +8 ────────────────────────────────────────────
    # diffs: 12,20,28,36,44 → 3+12=15, 15+20=35, 35+28=63, …
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 3, 15, ?, 63, 99, 143",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 3, 15, ?, 63, 99, 143",
        "option_a": "27",
        "option_b": "35",
        "option_c": "45",
        "option_d": "56",
        "correct_answer": "B",   # diffs 12,20,28,36,44 (2nd-diff +8) → 15+20=35
    },
    # ── Q38 ── n³ − 1 for n = 2, 3, 4 … 8 ───────────────────────────────────────
    # 2³−1=7, 3³−1=26, …, 7³−1=342, 8³−1=511
    {
        "question_number": 38,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 7, 26, 63, 124, 215, 342, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 7, 26, 63, 124, 215, 342, ?",
        "option_a": "391",
        "option_b": "421",
        "option_c": "481",
        "option_d": "511",
        "correct_answer": "D",   # n³−1 (n=2→8) → 8³−1=511
    },
    # ── Q39 ── 2ⁿ − 1 for n = 2, 3 … 7 ─────────────────────────────────────────
    # 2²−1=3, 2³−1=7, 2⁴−1=15, 2⁵−1=31, 2⁶−1=63, 2⁷−1=127
    {
        "question_number": 39,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 3, 7, 15, ?, 63, 127",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 3, 7, 15, ?, 63, 127",
        "option_a": "30",
        "option_b": "31",
        "option_c": "47",
        "option_d": "52",
        "correct_answer": "B",   # 2ⁿ−1 (n=2→7) → 2⁵−1=31
    },
    # ── Q40 ── 3ⁿ + 1 for n = 1, 2 … 6 ─────────────────────────────────────────
    # 3¹+1=4, 3²+1=10, 3³+1=28, 3⁴+1=82, 3⁵+1=244, 3⁶+1=730
    {
        "question_number": 40,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 4, 10, ?, 82, 244, 730",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 4, 10, ?, 82, 244, 730",
        "option_a": "24",
        "option_b": "28",
        "option_c": "77",
        "option_d": "218",
        "correct_answer": "B",   # 3ⁿ+1 (n=1→6) → 3³+1=28
    },
    # ── Q41 ── alternating ×2+1, ×2−1 ───────────────────────────────────────────
    # 6→13(×2+1)→25(×2−1)→51(×2+1)→101(×2−1)→203(×2+1)
    {
        "question_number": 41,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 6, 13, 25, 51, 101, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 6, 13, 25, 51, 101, ?",
        "option_a": "201",
        "option_b": "202",
        "option_c": "203",
        "option_d": "205",
        "correct_answer": "C",   # alternating ×2+1,×2−1 → 101×2+1=203
    },
    # ── Q42 ── prev × (n+2) + 4 for n = 1,2,3,4,5 ───────────────────────────────
    # 8×3+4=28, 28×4+4=116, 116×5+4=584, 584×6+4=3508
    {
        "question_number": 42,
        "difficulty": "hard",
        "question_en": "Find the missing number in the series: 8, 28, 116, 584, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 8, 28, 116, 584, ?",
        "option_a": "1752",
        "option_b": "3502",
        "option_c": "3504",
        "option_d": "3508",
        "correct_answer": "D",   # ×(n+2)+4 pattern → 584×6+4=3508
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
