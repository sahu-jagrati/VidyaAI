"""
seed_reasoning_classification_sheet2.py
=========================================
Seeds Classification (Odd One Out) Q23-Q34 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Classification
Run     : python seed_reasoning_classification_sheet2.py

Answer key (solutions provided by user — logic verified):
  Q23  64-73, 46-57, 38-49, 41-52  → A  (64,73)   diff=9; others diff=11
  Q24  5725, 6514, 3463, 8948       → C  (3463)    only prime; others composite
  Q25  7, 15, 31, 57                → D  (57)       57≠2⁶-1=63; others are 2ⁿ-1
  Q26  6378, 7689, 3245, 4367       → A  (6378)    d1+d3=13≠d2+d4=11; others equal
  Q27  428, 339, 326, 338           → D  (338)      3×3=9≠8; others: d1×d2=d3
  Q28  256671,257931,276471,265391  → D  (265391)  digit sum=26; others=27
  Q29  876321,742956,564327,368127  → B  (742956)  digit sum=33 (not ÷9); others=27
  Q30  399, 448, 449, 497           → C  (449)      not divisible by 7; others are
  Q31  4025, 7202, 6023, 5061       → D  (5061)    digit sum=12; others=11
  Q32  12-21, 57-75, 15-41, 34-43  → C  (15-41)   15 reversed=51≠41; others digit-reversal
  Q33  2:20, 4:50, 3:30, 1:10      → B  (4:50)    4×10=40≠50; others follow 1:10 ratio
  Q34  17, 19, 13, 21               → D  (21)       21=3×7 composite; others prime
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Classification_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Classification"

QUESTIONS = [
    # ── Q23 ── 64-73 has diff=9; others have diff=11 ─────────────────────────
    {
        "question_number": 23,
        "difficulty": "easy",
        "question_en": "Find the odd pair: 64-73, 46-57, 38-49, 41-52",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 64-73, 46-57, 38-49, 41-52",
        "option_a": "64 - 73",
        "option_b": "46 - 57",
        "option_c": "38 - 49",
        "option_d": "41 - 52",
        "correct_answer": "A",   # diff=9; others: 57-46=11, 49-38=11, 52-41=11
    },
    # ── Q24 ── 3463 is prime; 5725,6514,8948 are composite ───────────────────
    {
        "question_number": 24,
        "difficulty": "medium",
        "question_en": "Find the odd one out: 5725, 6514, 3463, 8948",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 5725, 6514, 3463, 8948",
        "option_a": "5725",
        "option_b": "6514",
        "option_c": "3463",
        "option_d": "8948",
        "correct_answer": "C",   # 3463 is prime; 5725÷5✓, 6514÷2✓, 8948÷2✓ (composite)
    },
    # ── Q25 ── 57 doesn't fit 2ⁿ−1 pattern; 7=2³−1, 15=2⁴−1, 31=2⁵−1 ──────
    {
        "question_number": 25,
        "difficulty": "medium",
        "question_en": "Find the odd one out: 7, 15, 31, 57",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 7, 15, 31, 57",
        "option_a": "7",
        "option_b": "15",
        "option_c": "31",
        "option_d": "57",
        "correct_answer": "D",   # 57≠2⁶-1=63; others: 7=2³-1, 15=2⁴-1, 31=2⁵-1
    },
    # ── Q26 ── 6378: (6+7)=13≠(3+8)=11; others: d1+d3=d2+d4 ─────────────────
    {
        "question_number": 26,
        "difficulty": "hard",
        "question_en": "Find the odd one out: 6378, 7689, 3245, 4367",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 6378, 7689, 3245, 4367",
        "option_a": "6378",
        "option_b": "7689",
        "option_c": "3245",
        "option_d": "4367",
        "correct_answer": "A",   # 6+7=13≠3+8=11; others: 7+8=15=6+9✓, 3+4=7=2+5✓, 4+6=10=3+7✓
    },
    # ── Q27 ── 338: d1×d2=3×3=9≠8=d3; others follow d1×d2=d3 ────────────────
    {
        "question_number": 27,
        "difficulty": "medium",
        "question_en": "Find the odd one out: 428, 339, 326, 338",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 428, 339, 326, 338",
        "option_a": "428",
        "option_b": "339",
        "option_c": "326",
        "option_d": "338",
        "correct_answer": "D",   # 3×3=9≠8; others: 4×2=8✓, 3×3=9✓, 3×2=6✓
    },
    # ── Q28 ── 265391: digit sum=2+6+5+3+9+1=26; others sum=27 ──────────────
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": "Find the odd one out: 256671, 257931, 276471, 265391",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 256671, 257931, 276471, 265391",
        "option_a": "256671",
        "option_b": "257931",
        "option_c": "276471",
        "option_d": "265391",
        "correct_answer": "D",   # 2+6+5+3+9+1=26; others: 2+5+6+6+7+1=27✓, 2+5+7+9+3+1=27✓, 2+7+6+4+7+1=27✓
    },
    # ── Q29 ── 742956: digit sum=33 (not ÷9); others sum=27 (÷9) ────────────
    {
        "question_number": 29,
        "difficulty": "medium",
        "question_en": "Find the odd one out: 876321, 742956, 564327, 368127",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 876321, 742956, 564327, 368127",
        "option_a": "876321",
        "option_b": "742956",
        "option_c": "564327",
        "option_d": "368127",
        "correct_answer": "B",   # 7+4+2+9+5+6=33 (not divisible by 9); others sum=27 (÷9)
    },
    # ── Q30 ── 449 not divisible by 7; others are ────────────────────────────
    {
        "question_number": 30,
        "difficulty": "easy",
        "question_en": "Find the odd one out: 399, 448, 449, 497",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 399, 448, 449, 497",
        "option_a": "399",
        "option_b": "448",
        "option_c": "449",
        "option_d": "497",
        "correct_answer": "C",   # 449÷7=64.14 (not divisible); 399÷7=57✓, 448÷7=64✓, 497÷7=71✓
    },
    # ── Q31 ── 5061: digit sum=5+0+6+1=12; others sum=11 ────────────────────
    {
        "question_number": 31,
        "difficulty": "easy",
        "question_en": "Find the odd one out: 4025, 7202, 6023, 5061",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 4025, 7202, 6023, 5061",
        "option_a": "4025",
        "option_b": "7202",
        "option_c": "6023",
        "option_d": "5061",
        "correct_answer": "D",   # 5+0+6+1=12; others: 4+0+2+5=11✓, 7+2+0+2=11✓, 6+0+2+3=11✓
    },
    # ── Q32 ── 15-41: 15 reversed=51≠41; others are digit-reversal pairs ─────
    {
        "question_number": 32,
        "difficulty": "medium",
        "question_en": "Find the odd pair: 12-21, 57-75, 15-41, 34-43",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 12-21, 57-75, 15-41, 34-43",
        "option_a": "12 - 21",
        "option_b": "57 - 75",
        "option_c": "15 - 41",
        "option_d": "34 - 43",
        "correct_answer": "C",   # 15 reversed=51≠41; others: 12↔21✓, 57↔75✓, 34↔43✓
    },
    # ── Q33 ── 4:50: 4×10=40≠50; others follow ratio 1:10 ───────────────────
    {
        "question_number": 33,
        "difficulty": "easy",
        "question_en": "Find the odd ratio: 2:20, 4:50, 3:30, 1:10",
        "question_hi": "विषम अनुपात ज्ञात कीजिए: 2:20, 4:50, 3:30, 1:10",
        "option_a": "2 : 20",
        "option_b": "4 : 50",
        "option_c": "3 : 30",
        "option_d": "1 : 10",
        "correct_answer": "B",   # 4×10=40≠50; others follow 1:10 ratio (2×10=20✓, 3×10=30✓, 1×10=10✓)
    },
    # ── Q34 ── 21=3×7 (composite); 17,19,13 are all prime ───────────────────
    {
        "question_number": 34,
        "difficulty": "easy",
        "question_en": "Find the odd one out: 17, 19, 13, 21",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 17, 19, 13, 21",
        "option_a": "17",
        "option_b": "19",
        "option_c": "13",
        "option_d": "21",
        "correct_answer": "D",   # 21=3×7 (composite); 17,19,13 are prime
    },
]

# Fix map for pre-existing records (ans=None)
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
