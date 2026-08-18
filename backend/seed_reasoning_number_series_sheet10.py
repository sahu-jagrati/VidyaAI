"""
seed_reasoning_number_series_sheet10.py
=========================================
Seeds Number Series Q78-Q85 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Number Series
Run     : python seed_reasoning_number_series_sheet10.py

Answer key (verified via Python):
  Q78  2/√5, 3/5, 4/5√5, 5/25, ?      nums +1; dens = (√5)ⁿ              → B  6/25√5
  Q79  11(1/9),12(1/2),14(2/7),16(2/3),?  each = 100/n; n=9,8,7,6,5      → C  20
  Q80  3,10,29,66,127,?                n³+2 for n=1..6                    → D  218
  Q81  2,12,36,80,150,?               n³+n² for n=1..6                   → C  252
  Q82  2,9,28,?,126,217,344           n³+1 for n=1..7                    → B  65
  Q83  10,17,24,31,38,...             AP a=10 d=7; Tₙ=7n+3               → B  346
  Q84  1,8,27,64,125,...              perfect cubes; 256 is not a cube    → A  256
  Q85  3,9,15,...                     AP a=3 d=6; T₂₁=3+20×6             → C  123
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Number_Series_Sheet10"
SUBJECT = "Reasoning"
TOPIC   = "Number Series"

QUESTIONS = [
    # ── Q78 ── numerators +1; denominators are successive powers of √5 ────────────
    # 2/(√5)¹, 3/(√5)², 4/(√5)³, 5/(√5)⁴, 6/(√5)⁵
    # (√5)⁵ = 25√5 → answer = 6/25√5
    {
        "question_number": 78,
        "difficulty": "medium",
        "question_en": "Find the missing fraction in the series: 2/√5, 3/5, 4/5√5, 5/25, ?",
        "question_hi": "श्रृंखला में लुप्त पद ज्ञात कीजिए: 2/√5, 3/5, 4/5√5, 5/25, ?",
        "option_a": "6/5√5",
        "option_b": "6/25√5",
        "option_c": "6/125",
        "option_d": "7/25",
        "correct_answer": "B",   # nums +1; den=(√5)^5=25√5 → 6/25√5
    },
    # ── Q79 ── mixed fractions all equal 100/n; n = 9,8,7,6,5 ───────────────────
    # 11(1/9)=100/9, 12(1/2)=100/8, 14(2/7)=100/7, 16(2/3)=100/6
    # next n=5 → 100/5 = 20
    {
        "question_number": 79,
        "difficulty": "medium",
        "question_en": "Find the missing term in the series: 11(1/9), 12(1/2), 14(2/7), 16(2/3), ?",
        "question_hi": "श्रृंखला में लुप्त पद ज्ञात कीजिए: 11(1/9), 12(1/2), 14(2/7), 16(2/3), ?",
        "option_a": "8(1/3)",
        "option_b": "19(1/2)",
        "option_c": "20",
        "option_d": "22(1/3)",
        "correct_answer": "C",   # each term = 100/n (n=9→5) → 100/5=20
    },
    # ── Q80 ── n³ + 2 for n = 1 to 6 ────────────────────────────────────────────
    # 1+2=3, 8+2=10, 27+2=29, 64+2=66, 125+2=127, 216+2=218
    {
        "question_number": 80,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 3, 10, 29, 66, 127, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 3, 10, 29, 66, 127, ?",
        "option_a": "164",
        "option_b": "187",
        "option_c": "216",
        "option_d": "218",
        "correct_answer": "D",   # n³+2 → 6³+2=218
    },
    # ── Q81 ── n³ + n² for n = 1 to 6 ───────────────────────────────────────────
    # 1+1=2, 8+4=12, 27+9=36, 64+16=80, 125+25=150, 216+36=252
    {
        "question_number": 81,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 2, 12, 36, 80, 150, ?",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 2, 12, 36, 80, 150, ?",
        "option_a": "194",
        "option_b": "210",
        "option_c": "252",
        "option_d": "258",
        "correct_answer": "C",   # n³+n² → 6³+6²=252
    },
    # ── Q82 ── n³ + 1 for n = 1 to 7 ────────────────────────────────────────────
    # 1+1=2, 8+1=9, 27+1=28, 64+1=65, 125+1=126, 216+1=217, 343+1=344
    {
        "question_number": 82,
        "difficulty": "easy",
        "question_en": "Find the missing number in the series: 2, 9, 28, ?, 126, 217, 344",
        "question_hi": "श्रृंखला में लुप्त संख्या ज्ञात कीजिए: 2, 9, 28, ?, 126, 217, 344",
        "option_a": "50",
        "option_b": "65",
        "option_c": "70",
        "option_d": "82",
        "correct_answer": "B",   # n³+1 → 4³+1=65
    },
    # ── Q83 ── AP a=10, d=7; Tₙ=7n+3; valid term: (T−3) divisible by 7 ─────────
    # 346: (346−3)=343=7×49 ✓ → 49th term
    {
        "question_number": 83,
        "difficulty": "medium",
        "question_en": "The series 10, 17, 24, 31, 38, ... Which of the following is a term of this series?",
        "question_hi": "श्रृंखला 10, 17, 24, 31, 38, ... में निम्नलिखित में से कौन सी एक संख्या होगी?",
        "option_a": "48",
        "option_b": "346",
        "option_c": "574",
        "option_d": "1003",
        "correct_answer": "B",   # AP a=10 d=7: (346-3)/7=49 → 49th term ✓
    },
    # ── Q84 ── perfect cubes; 256 is not a cube (256=16², ∛256≈6.35) ─────────────
    # 512=8³, 729=9³, 1000=10³ are all perfect cubes
    {
        "question_number": 84,
        "difficulty": "easy",
        "question_en": "In the series 1, 8, 27, 64, 125, ... which of the following is NOT a term?",
        "question_hi": "श्रृंखला 1, 8, 27, 64, 125, ... में निम्नलिखित में से कौन सी संख्या नहीं होगी?",
        "option_a": "256",
        "option_b": "512",
        "option_c": "729",
        "option_d": "1000",
        "correct_answer": "A",   # 256=16² (NOT a perfect cube); 512=8³,729=9³,1000=10³
    },
    # ── Q85 ── AP a=3, d=6; T₂₁ = 3+(21-1)×6 = 123 ────────────────────────────
    {
        "question_number": 85,
        "difficulty": "easy",
        "question_en": "In the series 3, 9, 15, ... what is the 21st term?",
        "question_hi": "श्रृंखला 3, 9, 15, ... में 21वाँ पद क्या होगा?",
        "option_a": "117",
        "option_b": "121",
        "option_c": "123",
        "option_d": "129",
        "correct_answer": "C",   # T₂₁=3+20×6=123
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
