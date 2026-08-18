"""
seed_reasoning_classification_sheet3.py
=========================================
Seeds Classification (Odd One Out) Q35-Q45 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Classification
Run     : python seed_reasoning_classification_sheet3.py

Answer key (solution images provided by user — logic verified):
  Q35  9, 13, 17, 19         → A  (9)       9=3² (composite); 13,17,19 are prime
  Q36  1625, 3649, 6481,5025 → D  (5025)   50 not a perfect square; others split AB|CD both squares
  Q37  8110, 1234,9100,1189  → D  (1189)   digit sum=19; others digit sum=10
  Q38  6898,6119,8118,6699   → C  (8118)   8118 IS a palindrome; others are NOT
  Q39  51530,2610,41220,3915 → A  (51530)  digit sum=14 (not ÷9); others ÷9
  Q40  162, 405, 567, 644    → D  (644)    644÷9=71.55 (not ÷9); others ÷9
  Q41  61-12,25-21,34-30,44-31 → D (44-31) diff=13 (not perfect square); others diffs are
  Q42  3/7, 7/2, 4/13, 13/16  → B  (7/2)   improper fraction (>1); others are proper (<1)
  Q43  26-62,36-63,46-64,56-18 → D (56-18) 56 reversed=65≠18; others are digit-reversal pairs
  Q44  34-43,62-71,55-62,83-92 → C (55-62) diff=62-55=7; others have diff=9
  Q45  9¹/₁₁, 7⁹/₁₃, 5¹⁵/₁₇, 5⁶/₁₉ → D (5⁶/₁₉) numerator=101≠100; others give 100/denom

  Note Q38: PDF answer key shows A(6898) but the logical pattern (palindrome) gives C(8118).
            Solution image confirms C — stored C.
  Note Q45: PDF shows option_b as "9 9/13" but solution shows 7×13+9=100/13 → stored as 7 9/13.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Classification_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Classification"

QUESTIONS = [
    # ── Q35 ── 9=3² (composite); 13,17,19 are prime ──────────────────────────
    {
        "question_number": 35,
        "difficulty": "easy",
        "question_en": "Find the odd one out: 9, 13, 17, 19",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 9, 13, 17, 19",
        "option_a": "9",
        "option_b": "13",
        "option_c": "17",
        "option_d": "19",
        "correct_answer": "A",   # 9=3² (composite); 13,17,19 are prime numbers
    },
    # ── Q36 ── 5025 → 50 is not a perfect square; others: AB & CD both squares
    {
        "question_number": 36,
        "difficulty": "hard",
        "question_en": "Find the odd one out: 1625, 3649, 6481, 5025",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 1625, 3649, 6481, 5025",
        "option_a": "1625",
        "option_b": "3649",
        "option_c": "6481",
        "option_d": "5025",
        "correct_answer": "D",   # 50 is NOT a perfect square; 16=4²&25=5²✓, 36=6²&49=7²✓, 64=8²&81=9²✓
    },
    # ── Q37 ── 1189: digit sum=1+1+8+9=19; others sum=10 ─────────────────────
    {
        "question_number": 37,
        "difficulty": "easy",
        "question_en": "Find the odd one out: 8110, 1234, 9100, 1189",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 8110, 1234, 9100, 1189",
        "option_a": "8110",
        "option_b": "1234",
        "option_c": "9100",
        "option_d": "1189",
        "correct_answer": "D",   # 1+1+8+9=19; others: 8+1+1+0=10✓, 1+2+3+4=10✓, 9+1+0+0=10✓
    },
    # ── Q38 ── 8118 is a palindrome; others (6898,6119,6699) are NOT ──────────
    {
        "question_number": 38,
        "difficulty": "medium",
        "question_en": "Find the odd one out: 6898, 6119, 8118, 6699",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 6898, 6119, 8118, 6699",
        "option_a": "6898",
        "option_b": "6119",
        "option_c": "8118",
        "option_d": "6699",
        "correct_answer": "C",   # 8118 reads same forwards & backwards (palindrome); others are NOT
    },
    # ── Q39 ── 51530: digit sum=14 (not ÷9); others digit sums divisible by 9 ─
    {
        "question_number": 39,
        "difficulty": "medium",
        "question_en": "Find the odd one out: 51530, 2610, 41220, 3915",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 51530, 2610, 41220, 3915",
        "option_a": "51530",
        "option_b": "2610",
        "option_c": "41220",
        "option_d": "3915",
        "correct_answer": "A",   # 5+1+5+3+0=14 (not ÷9); 2+6+1+0=9✓, 4+1+2+2+0=9✓, 3+9+1+5=18✓
    },
    # ── Q40 ── 644: 6+4+4=14 (not ÷9); others divisible by 9 ────────────────
    {
        "question_number": 40,
        "difficulty": "easy",
        "question_en": "Find the odd one out: 162, 405, 567, 644",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 162, 405, 567, 644",
        "option_a": "162",
        "option_b": "405",
        "option_c": "567",
        "option_d": "644",
        "correct_answer": "D",   # 644÷9=71.55 (not ÷9); 162÷9=18✓, 405÷9=45✓, 567÷9=63✓
    },
    # ── Q41 ── 44-31: diff=13 (not a perfect square); others diffs are squares ─
    {
        "question_number": 41,
        "difficulty": "medium",
        "question_en": "Find the odd pair: 61-12, 25-21, 34-30, 44-31",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 61-12, 25-21, 34-30, 44-31",
        "option_a": "61 - 12",
        "option_b": "25 - 21",
        "option_c": "34 - 30",
        "option_d": "44 - 31",
        "correct_answer": "D",   # 44-31=13 (not perfect square); 61-12=49=7²✓, 25-21=4=2²✓, 34-30=4=2²✓
    },
    # ── Q42 ── 7/2 is an improper fraction (>1); others are proper fractions ──
    {
        "question_number": 42,
        "difficulty": "easy",
        "question_en": "Find the odd fraction: 3/7, 7/2, 4/13, 13/16",
        "question_hi": "विषम भिन्न ज्ञात कीजिए: 3/7, 7/2, 4/13, 13/16",
        "option_a": "3/7",
        "option_b": "7/2",
        "option_c": "4/13",
        "option_d": "13/16",
        "correct_answer": "B",   # 7/2=3.5>1 (improper); 3/7<1✓, 4/13<1✓, 13/16<1✓ (proper fractions)
    },
    # ── Q43 ── 56-18: 56 reversed=65≠18; others are digit-reversal pairs ──────
    {
        "question_number": 43,
        "difficulty": "medium",
        "question_en": "Find the odd pair: 26-62, 36-63, 46-64, 56-18",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 26-62, 36-63, 46-64, 56-18",
        "option_a": "26 - 62",
        "option_b": "36 - 63",
        "option_c": "46 - 64",
        "option_d": "56 - 18",
        "correct_answer": "D",   # 56 reversed=65≠18; others: 26↔62✓, 36↔63✓, 46↔64✓
    },
    # ── Q44 ── 55-62: diff=62-55=7; others have diff=9 ───────────────────────
    {
        "question_number": 44,
        "difficulty": "easy",
        "question_en": "Find the odd pair: 34-43, 62-71, 55-62, 83-92",
        "question_hi": "विषम युग्म ज्ञात कीजिए: 34-43, 62-71, 55-62, 83-92",
        "option_a": "34 - 43",
        "option_b": "62 - 71",
        "option_c": "55 - 62",
        "option_d": "83 - 92",
        "correct_answer": "C",   # 62-55=7; others: 43-34=9✓, 71-62=9✓, 92-83=9✓
    },
    # ── Q45 ── 5⁶/₁₉: numerator=5×19+6=101≠100; others all give numerator=100 ─
    {
        "question_number": 45,
        "difficulty": "hard",
        "question_en": "Find the odd mixed number: 9 1/11, 7 9/13, 5 15/17, 5 6/19",
        "question_hi": "विषम मिश्र संख्या ज्ञात कीजिए: 9 1/11, 7 9/13, 5 15/17, 5 6/19",
        "option_a": "9 1/11",
        "option_b": "7 9/13",    # PDF shows "9 9/13" but solution confirms: 7×13+9=100 → 7 9/13
        "option_c": "5 15/17",
        "option_d": "5 6/19",
        "correct_answer": "D",   # 5×19+6=101≠100; others: 9×11+1=100✓, 7×13+9=100✓, 5×17+15=100✓
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
