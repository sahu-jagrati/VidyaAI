"""
seed_reasoning_classification_sheet4.py
=========================================
Seeds Classification (Odd One Out) Q46-Q50 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Classification
Run     : python seed_reasoning_classification_sheet4.py

Answer key (solution images provided by user — logic verified):
  Q46  187:11, 194:12, 195:13, 224:14  → B  (194:12)  194÷12=16.16 not exact; others exactly divisible
  Q47  121:341, 183:392, 235:427,289:501→ B  (183:392) odd+even mix; others both-odd pairs
  Q48  120, 145, 37, 50                 → C  (37)      37 is prime; 120,145,50 are composite
  Q49  (9,36,81),(32,64,88),(55,135,165),(35,63,78) → A  (9,36,81) all perfect squares; others NOT
  Q50  163, 131, 137, 166              → D  (166)     166=2×83 even composite; 163,131,137 are prime

  Note Q48: solution also mentions n²±1 pattern; exam key = C (37) ✓
  Note Q49: PDF key = B, but solution image clearly states A (all-perfect-squares group) → stored A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Classification_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Classification"

QUESTIONS = [
    # ── Q46 ── 194:12 → 194÷12=16.16 (not exactly divisible); others are ──────
    {
        "question_number": 46,
        "difficulty": "medium",
        "question_en": "Find the odd ratio: 187:11, 194:12, 195:13, 224:14",
        "question_hi": "विषम अनुपात ज्ञात कीजिए: 187:11, 194:12, 195:13, 224:14",
        "option_a": "187 : 11",
        "option_b": "194 : 12",
        "option_c": "195 : 13",
        "option_d": "224 : 14",
        "correct_answer": "B",   # 194÷12=16.16 (not divisible); 187÷11=17✓, 195÷13=15✓, 224÷14=16✓
    },
    # ── Q47 ── 183:392 → odd+even mix; others are both-odd pairs ────────────
    {
        "question_number": 47,
        "difficulty": "easy",
        "question_en": "Find the odd ratio: 121:341, 183:392, 235:427, 289:501",
        "question_hi": "विषम अनुपात ज्ञात कीजिए: 121:341, 183:392, 235:427, 289:501",
        "option_a": "121 : 341",
        "option_b": "183 : 392",
        "option_c": "235 : 427",
        "option_d": "289 : 501",
        "correct_answer": "B",   # 183(odd)+392(even); others: 121&341 both odd✓, 235&427 both odd✓, 289&501 both odd✓
    },
    # ── Q48 ── 37 is prime; 120,145,50 are composite ─────────────────────────
    {
        "question_number": 48,
        "difficulty": "easy",
        "question_en": "Find the odd one out: 120, 145, 37, 50",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 120, 145, 37, 50",
        "option_a": "120",
        "option_b": "145",
        "option_c": "37",
        "option_d": "50",
        "correct_answer": "C",   # 37 is prime; 120=8×15✗, 145=5×29✗, 50=2×25✗ (all composite)
    },
    # ── Q49 ── (9,36,81) all perfect squares; others are NOT ─────────────────
    {
        "question_number": 49,
        "difficulty": "hard",
        "question_en": "Find the odd group: (9,36,81), (32,64,88), (55,135,165), (35,63,78)",
        "question_hi": "विषम समूह ज्ञात कीजिए: (9,36,81), (32,64,88), (55,135,165), (35,63,78)",
        "option_a": "9, 36, 81",
        "option_b": "32, 64, 88",
        "option_c": "55, 135, 165",
        "option_d": "35, 63, 78",
        "correct_answer": "A",   # 9=3²,36=6²,81=9² — all perfect squares; others are NOT all perfect squares
    },
    # ── Q50 ── 166=2×83 (even composite); 163,131,137 are all prime ───────────
    {
        "question_number": 50,
        "difficulty": "easy",
        "question_en": "Find the odd one out: 163, 131, 137, 166",
        "question_hi": "विषम संख्या ज्ञात कीजिए: 163, 131, 137, 166",
        "option_a": "163",
        "option_b": "131",
        "option_c": "137",
        "option_d": "166",
        "correct_answer": "D",   # 166=2×83 (even composite); 163,131,137 are all prime numbers
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
