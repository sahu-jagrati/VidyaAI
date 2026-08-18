"""
seed_reasoning_classification_sheet1.py
=========================================
Seeds Classification (Odd One Out) Q1-Q22 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Classification
Run     : python seed_reasoning_classification_sheet1.py

Type: Find the odd one out from 4 options.

Answer key (verified with patterns):
  Q1   1629,3418,2349,1834 → 1834 is odd                              → D
  Q2   4-16,8-24,14-26,16-26 → 14-26 (no clean ratio)                → C
  Q3   15-21,32-41,22-17,31-35 → 15-21 (GCD=3; others coprime)       → A
  Q4   13,17,29,87 → 87=3×29 (not prime; others are prime)            → D
  Q5   52-61,72-81,54-63,33-41 → 33-41 diff=8 (others diff=9)        → D
  Q6   85-136,34-85,102-153,63-162 → 63-162 diff=99 (others diff=51) → D
  Q7   24-42,36-63,37-73,35-51 → 35-51 (not digit-reversal pair)     → D
  Q8   2,4,16,36 → 2 (not a perfect square; 4=2²,16=4²,36=6²)        → A
  Q9   36-72,17-34,28-49,24-48 → 28-49 (49/28≠2; others b=2a)       → C
  Q10  8-11,1-4,7-10,3-5 → 3-5 diff=2 (others diff=3)                → D
  Q11  191,200,808,1331 → 1331 (4-digit; others are 3-digit)          → D
  Q12  8-15,25-36,49-64,81-100 → 8-15 (neither perfect square)       → A
       (25=5²,36=6²; 49=7²,64=8²; 81=9²,100=10²; 8 and 15 are NOT)
  Q13  729-27,361-19,476-32,676-26 → 476-32 (√476≠32)                → C
       (729=27², 361=19², 676=26²; pattern: b²=a)
  Q14  14-16,56-64,77-88,80-93 → 80-93 (ratio≠7:8)                   → D
       (14:16=7:8, 56:64=7:8, 77:88=7:8; 80:93 is not 7:8)
  Q15  13-21,19-27,15-23,16-24 → 16-24 (both even; others both odd)  → D
  Q16  29-45,48-68,71-87,5-21 → 48-68 diff=20 (others diff=16)       → B
  Q17  12-144,13-156,15-180,16-176 → 16-176 (176/16=11; others b=12a)→ D
  Q18  46-10,42-33,20-38,91-12 → 91-12 (diff=79; others |diff|÷9=0) → D
       (36=4×9, 9=1×9, 18=2×9; 79 not divisible by 9)
  Q19  (1,0),(2,3),(3,8),(4,27) → (4,27) (4²-1=15≠27; others b=a²-1)→ D
  Q20  (28,9),(31,10),(34,11),(36,12) → (36,12) (36≠3×12+1)          → D
       (28=3×9+1, 31=3×10+1, 34=3×11+1; 36≠3×12+1=37)
  Q21  8,9,27,64 → 9 (9=3², not a perfect cube; 8=2³,27=3³,64=4³)   → B
  Q22  853,734,751,532 → 751 (5≠7-1=6; others middle=first-last)     → C
       (8-3=5 ✓, 7-4=3 ✓, 5-2=3 ✓; 7-1=6≠5)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Classification_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Classification"

QUESTIONS = [
    # ── Q1 ── 1834 is the odd one out ─────────────────────────────────────────
    {
        "question_number": 1,
        "difficulty": "medium",
        "question_en": "Find the odd one out: 1629, 3418, 2349, 1834",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 1629, 3418, 2349, 1834",
        "option_a": "1629",
        "option_b": "3418",
        "option_c": "2349",
        "option_d": "1834",
        "correct_answer": "D",
    },
    # ── Q2 ── 14-26 has no clean ratio (b/a not integer) ─────────────────────
    {
        "question_number": 2,
        "difficulty": "medium",
        "question_en": "Find the odd pair: 4-16, 8-24, 14-26, 16-26",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 4-16, 8-24, 14-26, 16-26",
        "option_a": "4 - 16",
        "option_b": "8 - 24",
        "option_c": "14 - 26",
        "option_d": "16 - 26",
        "correct_answer": "C",
    },
    # ── Q3 ── 15-21 (GCD=3); others are coprime pairs ─────────────────────────
    {
        "question_number": 3,
        "difficulty": "medium",
        "question_en": "Find the odd pair: 15-21, 32-41, 22-17, 31-35",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 15-21, 32-41, 22-17, 31-35",
        "option_a": "15 - 21",
        "option_b": "32 - 41",
        "option_c": "22 - 17",
        "option_d": "31 - 35",
        "correct_answer": "A",   # GCD(15,21)=3; GCD of others=1 (coprime)
    },
    # ── Q4 ── 87=3×29 (not prime); 13, 17, 29 are prime ─────────────────────
    {
        "question_number": 4,
        "difficulty": "easy",
        "question_en": "Find the odd one out: 13, 17, 29, 87",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 13, 17, 29, 87",
        "option_a": "13",
        "option_b": "17",
        "option_c": "29",
        "option_d": "87",
        "correct_answer": "D",   # 87=3×29 (composite); others are prime
    },
    # ── Q5 ── 33-41 diff=8; others have diff=9 ───────────────────────────────
    {
        "question_number": 5,
        "difficulty": "easy",
        "question_en": "Find the odd pair: 52-61, 72-81, 54-63, 33-41",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 52-61, 72-81, 54-63, 33-41",
        "option_a": "52 - 61",
        "option_b": "72 - 81",
        "option_c": "54 - 63",
        "option_d": "33 - 41",
        "correct_answer": "D",   # diff=8; others have diff=9
    },
    # ── Q6 ── 63-162 diff=99; others have diff=51 ────────────────────────────
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": "Find the odd group: (85, 136), (34, 85), (102, 153), (63, 162)",
        "question_hi": "विषम समूह ज्ञात कीजिए: (85, 136), (34, 85), (102, 153), (63, 162)",
        "option_a": "85, 136",
        "option_b": "34, 85",
        "option_c": "102, 153",
        "option_d": "63, 162",
        "correct_answer": "D",   # diff=99; others have diff=51
    },
    # ── Q7 ── 35-51 is NOT a digit-reversal pair; others are ─────────────────
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": "Find the odd pair: 24-42, 36-63, 37-73, 35-51",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 24-42, 36-63, 37-73, 35-51",
        "option_a": "24 - 42",
        "option_b": "36 - 63",
        "option_c": "37 - 73",
        "option_d": "35 - 51",
        "correct_answer": "D",   # 35 reversed=53≠51; others are digit-reversal pairs
    },
    # ── Q8 ── 2 is not a perfect square; 4=2², 16=4², 36=6² ──────────────────
    {
        "question_number": 8,
        "difficulty": "easy",
        "question_en": "Find the odd one out: 2, 4, 16, 36",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 2, 4, 16, 36",
        "option_a": "2",
        "option_b": "4",
        "option_c": "16",
        "option_d": "36",
        "correct_answer": "A",   # 2 is not a perfect square; 4=2², 16=4², 36=6²
    },
    # ── Q9 ── 28-49: 49/28≠2; others follow b=2a ─────────────────────────────
    {
        "question_number": 9,
        "difficulty": "medium",
        "question_en": "Find the odd pair: 36-72, 17-34, 28-49, 24-48",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 36-72, 17-34, 28-49, 24-48",
        "option_a": "36 - 72",
        "option_b": "17 - 34",
        "option_c": "28 - 49",
        "option_d": "24 - 48",
        "correct_answer": "C",   # 49/28=1.75≠2; others have b=2a
    },
    # ── Q10 ── 3-5 diff=2; others have diff=3 ────────────────────────────────
    {
        "question_number": 10,
        "difficulty": "easy",
        "question_en": "Find the odd pair: 8-11, 1-4, 7-10, 3-5",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 8-11, 1-4, 7-10, 3-5",
        "option_a": "8 - 11",
        "option_b": "1 - 4",
        "option_c": "7 - 10",
        "option_d": "3 - 5",
        "correct_answer": "D",   # diff=2; others have diff=3
    },
    # ── Q11 ── 1331 is a 4-digit number; 191, 200, 808 are 3-digit ───────────
    {
        "question_number": 11,
        "difficulty": "easy",
        "question_en": "Find the odd one out: 191, 200, 808, 1331",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 191, 200, 808, 1331",
        "option_a": "191",
        "option_b": "200",
        "option_c": "808",
        "option_d": "1331",
        "correct_answer": "D",   # 1331 is 4-digit; others are 3-digit numbers
    },
    # ── Q12 ── 8-15: neither is a perfect square; others are consecutive sq pairs
    {
        "question_number": 12,
        "difficulty": "medium",
        "question_en": "Find the odd pair: 8-15, 25-36, 49-64, 81-100",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 8-15, 25-36, 49-64, 81-100",
        "option_a": "8 - 15",
        "option_b": "25 - 36",
        "option_c": "49 - 64",
        "option_d": "81 - 100",
        "correct_answer": "A",   # 8,15 are not perfect squares; others are (n²,(n+1)²) pairs
    },
    # ── Q13 ── 476-32: √476≠32; others satisfy b²=a ──────────────────────────
    {
        "question_number": 13,
        "difficulty": "medium",
        "question_en": "Find the odd pair: 729-27, 361-19, 476-32, 676-26",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 729-27, 361-19, 476-32, 676-26",
        "option_a": "729 - 27",
        "option_b": "361 - 19",
        "option_c": "476 - 32",
        "option_d": "676 - 26",
        "correct_answer": "C",   # 27²=729✓, 19²=361✓, 26²=676✓; but √476≠32
    },
    # ── Q14 ── 80-93: ratio≠7:8; others have ratio 7:8 ──────────────────────
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": "Find the odd pair: 14-16, 56-64, 77-88, 80-93",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 14-16, 56-64, 77-88, 80-93",
        "option_a": "14 - 16",
        "option_b": "56 - 64",
        "option_c": "77 - 88",
        "option_d": "80 - 93",
        "correct_answer": "D",   # 14:16=7:8, 56:64=7:8, 77:88=7:8; 80:93 is not 7:8
    },
    # ── Q15 ── 16-24: both even; others are both odd ──────────────────────────
    {
        "question_number": 15,
        "difficulty": "easy",
        "question_en": "Find the odd pair: 13-21, 19-27, 15-23, 16-24",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 13-21, 19-27, 15-23, 16-24",
        "option_a": "13 - 21",
        "option_b": "19 - 27",
        "option_c": "15 - 23",
        "option_d": "16 - 24",
        "correct_answer": "D",   # 16,24 both even; others are pairs of odd numbers
    },
    # ── Q16 ── 48-68 diff=20; others have diff=16 ────────────────────────────
    {
        "question_number": 16,
        "difficulty": "easy",
        "question_en": "Find the odd pair: 29-45, 48-68, 71-87, 5-21",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 29-45, 48-68, 71-87, 5-21",
        "option_a": "29 - 45",
        "option_b": "48 - 68",
        "option_c": "71 - 87",
        "option_d": "5 - 21",
        "correct_answer": "B",   # diff=20; others have diff=16
    },
    # ── Q17 ── 16-176: 176/16=11; others have b=12a ──────────────────────────
    {
        "question_number": 17,
        "difficulty": "medium",
        "question_en": "Find the odd pair: 12-144, 13-156, 15-180, 16-176",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 12-144, 13-156, 15-180, 16-176",
        "option_a": "12 - 144",
        "option_b": "13 - 156",
        "option_c": "15 - 180",
        "option_d": "16 - 176",
        "correct_answer": "D",   # 176/16=11; others: 144/12=156/13=180/15=12
    },
    # ── Q18 ── 91-12: diff=79 (not ÷9); others |diff| divisible by 9 ─────────
    {
        "question_number": 18,
        "difficulty": "medium",
        "question_en": "Find the odd pair: 46-10, 42-33, 20-38, 91-12",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 46-10, 42-33, 20-38, 91-12",
        "option_a": "46 - 10",
        "option_b": "42 - 33",
        "option_c": "20 - 38",
        "option_d": "91 - 12",
        "correct_answer": "D",   # |91-12|=79 (not divisible by 9); others: 36,9,18 are
    },
    # ── Q19 ── (4,27): 4²-1=15≠27; others follow b=a²-1 ─────────────────────
    {
        "question_number": 19,
        "difficulty": "hard",
        "question_en": "Find the odd pair: (1,0), (2,3), (3,8), (4,27)",
        "question_hi": "विषम युग्म ज्ञात कीजिए: (1,0), (2,3), (3,8), (4,27)",
        "option_a": "(1, 0)",
        "option_b": "(2, 3)",
        "option_c": "(3, 8)",
        "option_d": "(4, 27)",
        "correct_answer": "D",   # 1²-1=0✓, 2²-1=3✓, 3²-1=8✓; 4²-1=15≠27
    },
    # ── Q20 ── (36,12): 36≠3×12+1=37; others follow a=3b+1 ──────────────────
    {
        "question_number": 20,
        "difficulty": "hard",
        "question_en": "Find the odd pair: (28,9), (31,10), (34,11), (36,12)",
        "question_hi": "विषम युग्म ज्ञात कीजिए: (28,9), (31,10), (34,11), (36,12)",
        "option_a": "(28, 9)",
        "option_b": "(31, 10)",
        "option_c": "(34, 11)",
        "option_d": "(36, 12)",
        "correct_answer": "D",   # 28=3×9+1✓, 31=3×10+1✓, 34=3×11+1✓; 36≠3×12+1=37
    },
    # ── Q21 ── 9=3² (not a perfect cube); 8=2³, 27=3³, 64=4³ ────────────────
    {
        "question_number": 21,
        "difficulty": "easy",
        "question_en": "Find the odd one out: 8, 9, 27, 64",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 8, 9, 27, 64",
        "option_a": "8",
        "option_b": "9",
        "option_c": "27",
        "option_d": "64",
        "correct_answer": "B",   # 9=3² (not a perfect cube); 8=2³, 27=3³, 64=4³
    },
    # ── Q22 ── 751: middle digit 5 ≠ 7-1=6; others: middle = first - last ─────
    {
        "question_number": 22,
        "difficulty": "medium",
        "question_en": "Find the odd one out: 853, 734, 751, 532",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 853, 734, 751, 532",
        "option_a": "853",
        "option_b": "734",
        "option_c": "751",
        "option_d": "532",
        "correct_answer": "C",   # 8-3=5✓, 7-4=3✓, 5-2=3✓; 751: 7-1=6≠5 ✗
    },
]

# Fix map for any pre-existing records (ans=None)
_FIXES = {
    q["question_number"]: (q["correct_answer"], {
        "option_a": q["option_a"],
        "option_b": q["option_b"],
        "option_c": q["option_c"],
        "option_d": q["option_d"],
    })
    for q in QUESTIONS
}


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
                print(f"  SKIP  Q{d['question_number']}: already in DB (will update below)")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
            inserted += 1

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped (duplicate): {skipped}")

        updates = 0
        for qnum, (ans, fields) in _FIXES.items():
            q = db.query(Question).filter(
                Question.topic == TOPIC,
                Question.subject == SUBJECT,
                Question.question_number == qnum,
                Question.correct_answer == None,
            ).first()
            if q:
                q.correct_answer = ans
                for field, val in fields.items():
                    setattr(q, field, val)
                q.source_pdf = SOURCE
                updates += 1
                print(f"  UPDATE Q{qnum}: correct_answer={ans}")

        db.commit()
        if updates:
            print(f"Fixed {updates} pre-existing records.")

    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
