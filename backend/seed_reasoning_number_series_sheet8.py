"""
seed_reasoning_number_series_sheet8.py
========================================
Seeds Number Series Q61-Q68 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Number Series
Run     : python seed_reasoning_number_series_sheet8.py

Answer key (verified via Python):
  Q61  3,8,13,24,41,?            a(n)=a(n-2)+a(n-1)+n (n=2,3,4,5)         → A  70
  Q62  45,54,47,?,49,56,51,57,53 pairs (9,8,7,6 within-pair diffs)          → C  55
  Q63  Three series → a=160,b=140,c=160                                     → A  b < a = c
  Q64  2,15,4,12,6,7,?,?         two interleaved: +2 / diffs −3,−5,−7       → B  8, 0
  Q65  20,20,19,16,17,13,14,11,?,? two interleaved with mirror diffs         → A  10, 10
  Q66  0,2,3,5,8,10,15,17,24,26,?  n²−1 and n²+1 interleaved               → D  35
  Q67  13,35,57,79,911,?          consecutive odd numbers concatenated        → C  1113
  Q68  625,5,125,25,25,?,5        two interleaved ÷5 and ×5                  → C  125
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Number_Series_Sheet8"
SUBJECT = "Reasoning"
TOPIC   = "Number Series"

QUESTIONS = [
    # ── Q61 ── a(n) = a(n-2) + a(n-1) + n ────────────────────────────────────────
    # 3+8+2=13, 8+13+3=24, 13+24+4=41, 24+41+5=70
    {
        "question_number": 61,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 3, 8, 13, 24, 41, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 3, 8, 13, 24, 41, ?",
        "option_a": "70",
        "option_b": "75",
        "option_c": "80",
        "option_d": "85",
        "correct_answer": "A",   # a(n)=a(n-2)+a(n-1)+n → 24+41+5=70
    },
    # ── Q62 ── two interleaved APs, within-pair diffs 9,8,7,6 ────────────────────
    # A-series (odd pos): 45,47,49,51,53  d=+2
    # B-series (even pos): 54,55,56,57    d=+1 → missing 4th term = 55
    {
        "question_number": 62,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 45, 54, 47, ?, 49, 56, 51, 57, 53",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 45, 54, 47, ?, 49, 56, 51, 57, 53",
        "option_a": "48",
        "option_b": "50",
        "option_c": "55",
        "option_d": "None of these",
        "correct_answer": "C",   # pair diffs 9,8,7,6 → 47+8=55
    },
    # ── Q63 ── three series: find a, b, c then their relation ─────────────────────
    # Series I: 102,107,117,134,(a) -- 2nd-diffs +2 each → a=160
    # Series II: 130,115,135,110,(b) -- magnitudes 15,20,25,30 alt ±  → b=140
    # Series III: (c),80,120,300,1050 -- ratios 0.5,1.5,2.5,3.5 → c=160
    # a=160, b=140, c=160 → b < a = c
    {
        "question_number": 63,
        "difficulty": "hard",
        "question_en": "Find a,b,c in: I.102,107,117,134,(a) II.130,115,135,110,(b) III.(c),80,120,300,1050. Identify the relation.",
        "question_hi": "a,b,c ज्ञात कीजिए: I.102,107,117,134,(a) II.130,115,135,110,(b) III.(c),80,120,300,1050. संबंध बताइए।",
        "option_a": "b < a = c",
        "option_b": "b > a = c",
        "option_c": "b = a > c",
        "option_d": "None of these",
        "correct_answer": "A",   # a=160, b=140, c=160 → b<a=c
    },
    # ── Q64 ── two interleaved: +2 / decreasing odd diffs ────────────────────────
    # Odd positions(2,4,6,8): +2 each → 2,4,6,8
    # Even positions(15,12,7): diffs −3,−5,−7 → 7−7=0
    {
        "question_number": 64,
        "difficulty": "easy",
        "question_en": "Find the missing numbers in the series: 2, 15, 4, 12, 6, 7, ?, ?",
        "question_hi": "श्रृंखला में लुप्त संख्याएँ ज्ञात कीजिए: 2, 15, 4, 12, 6, 7, ?, ?",
        "option_a": "8, 8",
        "option_b": "8, 0",
        "option_c": "3, 8",
        "option_d": "None of these",
        "correct_answer": "B",   # odd→8(+2 each), even→0(diffs −3,−5,−7)
    },
    # ── Q65 ── two interleaved with mirror-image difference patterns ───────────────
    # Odd positions: 20,19,17,14,? diffs −1,−2,−3,−4 → 10
    # Even positions: 20,16,13,11,? diffs −4,−3,−2,−1 → 10
    {
        "question_number": 65,
        "difficulty": "easy",
        "question_en": "Find the missing numbers in the series: 20, 20, 19, 16, 17, 13, 14, 11, ?, ?",
        "question_hi": "श्रृंखला में लुप्त संख्याएँ ज्ञात कीजिए: 20, 20, 19, 16, 17, 13, 14, 11, ?, ?",
        "option_a": "10, 10",
        "option_b": "10, 11",
        "option_c": "13, 14",
        "option_d": "13, 16",
        "correct_answer": "A",   # odd→10(diffs−1,−2,−3,−4), even→10(diffs−4,−3,−2,−1)
    },
    # ── Q66 ── two interleaved: n²−1 and n²+1 ────────────────────────────────────
    # Odd positions: n²−1 for n=1..6 → 0,3,8,15,24,35
    # Even positions: n²+1 for n=1..5 → 2,5,10,17,26
    # 11th term (6th odd-position) = 6²−1 = 35
    {
        "question_number": 66,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 0, 2, 3, 5, 8, 10, 15, 17, 24, 26, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 0, 2, 3, 5, 8, 10, 15, 17, 24, 26, ?",
        "option_a": "28",
        "option_b": "30",
        "option_c": "32",
        "option_d": "35",
        "correct_answer": "D",   # n²−1 and n²+1 interleaved → 6²−1=35
    },
    # ── Q67 ── consecutive odd numbers concatenated ───────────────────────────────
    # 1&3=13, 3&5=35, 5&7=57, 7&9=79, 9&11=911, 11&13=1113
    {
        "question_number": 67,
        "difficulty": "medium",
        "question_en": "Find the missing number in the series: 13, 35, 57, 79, 911, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 13, 35, 57, 79, 911, ?",
        "option_a": "1110",
        "option_b": "1112",
        "option_c": "1113",
        "option_d": "1315",
        "correct_answer": "C",   # consecutive odd numbers joined: 11||13=1113
    },
    # ── Q68 ── two interleaved: ÷5 and ×5 ────────────────────────────────────────
    # Odd positions: 625,125,25,5 (÷5 each) → 5⁴,5³,5²,5¹
    # Even positions: 5,25,? (×5 each) → 5¹,5²,5³=125
    {
        "question_number": 68,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 625, 5, 125, 25, 25, ?, 5",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 625, 5, 125, 25, 25, ?, 5",
        "option_a": "5",
        "option_b": "25",
        "option_c": "125",
        "option_d": "625",
        "correct_answer": "C",   # even-pos: 5,25,125 (×5 each) → missing = 125
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
