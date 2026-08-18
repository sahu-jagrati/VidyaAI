"""
seed_reasoning_number_series_sheet11.py
=========================================
Seeds Number Series Q86-Q92 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Number Series
Run     : python seed_reasoning_number_series_sheet11.py

Answer key (verified via Python):
  Q86  GP 2,6,18,54... 8th term           a=2, r=3; T₈=2×3^7=4374        → B  4374
  Q87  AP 5,8,11,14... position of 320    a=5, d=3; n=(320-5)/3+1=106     → C  106th
  Q88  GP 5,10,20,40... position of 1280  a=5, r=2; 2^(n-1)=256→n=9      → B  9th
  Q89  196,169,144,121,101  (wrong term)  squares of 14,13,12,11,10 → 101 should be 100  → A  101
  Q90  3,10,27,4,16,64,5,25,125 (wrong)  triplets (n,n²,n³); 10 should be 9 → C  10
  Q91  25,36,49,81,121,169,225 (wrong)   squares of odd nos; 36=6² out of place → A  36
  Q92  2,5,10,17,26,37,50,64 (wrong)     n²+1; 64 should be 65            → D  64
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Number_Series_Sheet11"
SUBJECT = "Reasoning"
TOPIC   = "Number Series"

QUESTIONS = [
    # ── Q86 ── GP a=2, r=3; find 8th term ───────────────────────────────────────
    # T₈ = 2 × 3^7 = 2 × 2187 = 4374
    {
        "question_number": 86,
        "difficulty": "easy",
        "question_en": "In the series 2, 6, 18, 54, ... what is the 8th term?",
        "question_hi": "श्रृंखला 2, 6, 18, 54, ... में 8वाँ पद क्या होगा?",
        "option_a": "4370",
        "option_b": "4374",
        "option_c": "7443",
        "option_d": "7434",
        "correct_answer": "B",   # GP r=3: T₈=2×3^7=4374
    },
    # ── Q87 ── AP a=5, d=3; find position of 320 ─────────────────────────────────
    # 320 = 5+(n-1)×3 → n-1=105 → n=106
    {
        "question_number": 87,
        "difficulty": "easy",
        "question_en": "In the series 5, 8, 11, 14, ... which position is the number 320?",
        "question_hi": "श्रृंखला 5, 8, 11, 14, ... में संख्या 320 कौन सा पद है?",
        "option_a": "104th",
        "option_b": "105th",
        "option_c": "106th",
        "option_d": "64th",
        "correct_answer": "C",   # AP d=3: (320-5)/3+1=106
    },
    # ── Q88 ── GP a=5, r=2; find position of 1280 ────────────────────────────────
    # 1280 = 5×2^(n-1) → 2^(n-1)=256=2^8 → n=9
    {
        "question_number": 88,
        "difficulty": "easy",
        "question_en": "In the series 5, 10, 20, 40, ... which position is the number 1280?",
        "question_hi": "श्रृंखला 5, 10, 20, 40, ... में संख्या 1280 कौन सा पद है?",
        "option_a": "10th",
        "option_b": "9th",
        "option_c": "8th",
        "option_d": "None of these",
        "correct_answer": "B",   # GP r=2: 1280=5×2^8 → 9th term
    },
    # ── Q89 ── wrong term in decreasing perfect squares ───────────────────────────
    # Correct: 14²=196, 13²=169, 12²=144, 11²=121, 10²=100
    # Given:   196, 169, 144, 121, 101  → 101 should be 100
    {
        "question_number": 89,
        "difficulty": "easy",
        "question_en": "Find the wrong term in the series: 196, 169, 144, 121, 101",
        "question_hi": "श्रृंखला में गलत पद ज्ञात कीजिए: 196, 169, 144, 121, 101",
        "option_a": "101",
        "option_b": "121",
        "option_c": "169",
        "option_d": "196",
        "correct_answer": "A",   # 10²=100, not 101
    },
    # ── Q90 ── wrong term in triplet (n, n², n³) groups ──────────────────────────
    # Correct: (3,9,27), (4,16,64), (5,25,125)
    # Given:   3,10,27,4,16,64,5,25,125 → 10 should be 9 (=3²)
    {
        "question_number": 90,
        "difficulty": "medium",
        "question_en": "Find the wrong term in the series: 3, 10, 27, 4, 16, 64, 5, 25, 125",
        "question_hi": "श्रृंखला में गलत पद ज्ञात कीजिए: 3, 10, 27, 4, 16, 64, 5, 25, 125",
        "option_a": "3",
        "option_b": "4",
        "option_c": "10",
        "option_d": "27",
        "correct_answer": "C",   # triplets (n,n²,n³): 10 should be 9=3²
    },
    # ── Q91 ── wrong term in squares of odd numbers ───────────────────────────────
    # Correct: 5²=25, 7²=49, 9²=81, 11²=121, 13²=169, 15²=225
    # Given:   25,36,49,81,121,169,225 → 36=6² is even, doesn't belong
    {
        "question_number": 91,
        "difficulty": "easy",
        "question_en": "Find the wrong term in the series: 25, 36, 49, 81, 121, 169, 225",
        "question_hi": "श्रृंखला में गलत पद ज्ञात कीजिए: 25, 36, 49, 81, 121, 169, 225",
        "option_a": "36",
        "option_b": "49",
        "option_c": "169",
        "option_d": "225",
        "correct_answer": "A",   # 36=6² (even square); series is squares of odd nos
    },
    # ── Q92 ── wrong term in n²+1 series ─────────────────────────────────────────
    # Correct: 1²+1=2, 2²+1=5, 3²+1=10, 4²+1=17, 5²+1=26, 6²+1=37, 7²+1=50, 8²+1=65
    # Given:   2,5,10,17,26,37,50,64 → 64 should be 65
    {
        "question_number": 92,
        "difficulty": "easy",
        "question_en": "Find the wrong term in the series: 2, 5, 10, 17, 26, 37, 50, 64",
        "question_hi": "श्रृंखला में गलत पद ज्ञात कीजिए: 2, 5, 10, 17, 26, 37, 50, 64",
        "option_a": "17",
        "option_b": "26",
        "option_c": "37",
        "option_d": "64",
        "correct_answer": "D",   # n²+1: 8²+1=65, not 64
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
