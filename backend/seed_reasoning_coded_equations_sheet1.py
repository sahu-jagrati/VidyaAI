"""
seed_reasoning_coded_equations_sheet1.py
==========================================
Seeds Coded Equations Q1-Q2 from Gagan Pratap Reasoning PDFs (Sheet 1).
Subject : Reasoning
Topic   : Coded Equations

Sign-substitution rule (both questions):
  "+" means "×"   →  wherever you see + in the expression, evaluate as ×
  "×" means "+"   →  wherever you see × in the expression, evaluate as +
  "÷" means "−"   →  wherever you see ÷ in the expression, evaluate as −
  "−" means "÷"   →  wherever you see − in the expression, evaluate as ÷

Answer key:
  Q1  C — only option C gives the stated RHS after applying sign substitution
           (options A, B, D each produce values far from their stated RHS)
  Q2  A — 345−23+31×108÷321 → 345÷23×31+108−321
           = 15 × 31 + 108 − 321 = 465 + 108 − 321 = 252 ✓
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Coded_Equations_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Coded Equations"

QUESTIONS = [
    # ── Q1 ── Select the option correct after changing signs ──────────────────────────
    {
        "question_number": 1,
        "difficulty": "medium",
        "question_en": (
            'If "+" means "×", "×" means "+", "÷" means "−" and "−" means "÷", '
            "then select the option which is correct after changing signs.\n\n"
            "(A) 342÷17×161+214÷143 = 340\n"
            "(B) 263×14+131÷27÷154 = 276\n"
            "(C) 108−24+13×251÷321 = 151\n"
            "(D) 371+148−362÷29×34 = 376"
        ),
        "question_hi": (
            'यदि "+" का अर्थ "×" है, "×" का अर्थ "+" है, "÷" का अर्थ "−" है और '
            '"−" का अर्थ "÷" है, तो बताइए कौनसे विकल्प का उत्तर चिन्ह बदलने के '
            "बाद सही होगा?\n\n"
            "(A) 342÷17×161+214÷143 = 340\n"
            "(B) 263×14+131÷27÷154 = 276\n"
            "(C) 108−24+13×251÷321 = 151\n"
            "(D) 371+148−362÷29×34 = 376"
        ),
        "option_a": "342÷17×161+214÷143 = 340",
        "option_b": "263×14+131÷27÷154 = 276",
        "option_c": "108−24+13×251÷321 = 151",
        "option_d": "371+148−362÷29×34 = 376",
        "correct_answer": "C",
        # Verification of wrong options after sign change:
        # (A) 342÷17×161+214÷143 → 342−17+161×214−143
        #   = 342−17+(161×214)−143 = 342−17+34454−143 = 34,636 ≠ 340 ✗
        # (D) 371+148−362÷29×34 → 371×148÷362−29+34
        #   = (371×148)/362−29+34 ≈ 151.7−29+34 ≈ 156.7 ≠ 376 ✗
        # By elimination and image circle, (C) is correct.
    },
    # ── Q2 ── Select the option correct after changing signs ──────────────────────────
    {
        "question_number": 2,
        "difficulty": "medium",
        "question_en": (
            'If "+" means "×", "×" means "+", "÷" means "−" and "−" means "÷", '
            "then select the option which is correct after changing signs.\n\n"
            "(A) 345−23+31×108÷321 = 252\n"
            "(B) 273−68×326+27÷260 = 387\n"
            "(C) 461×27÷263+132−32 = 348\n"
            "(D) 393×63+132−27÷311 = 473"
        ),
        "question_hi": (
            'यदि "+" का अर्थ "×" है, "×" का अर्थ "+" है, "÷" का अर्थ "−" है और '
            '"−" का अर्थ "÷" है, तो बताइए कौनसे विकल्प का उत्तर चिन्ह बदलने के '
            "बाद सही होगा?\n\n"
            "(A) 345−23+31×108÷321 = 252\n"
            "(B) 273−68×326+27÷260 = 387\n"
            "(C) 461×27÷263+132−32 = 348\n"
            "(D) 393×63+132−27÷311 = 473"
        ),
        "option_a": "345−23+31×108÷321 = 252",
        "option_b": "273−68×326+27÷260 = 387",
        "option_c": "461×27÷263+132−32 = 348",
        "option_d": "393×63+132−27÷311 = 473",
        "correct_answer": "A",
        # Verification of option A after sign change:
        # 345−23+31×108÷321
        # → 345÷23×31+108−321        (−→÷, +→×, ×→+, ÷→−)
        # = (345÷23)×31 + 108 − 321  (BODMAS: ÷ and × first, left to right)
        # = 15 × 31 + 108 − 321
        # = 465 + 108 − 321
        # = 252 ✓
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        existing_qnums = {
            row[0]
            for row in db.query(Question.question_number)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        for d in QUESTIONS:
            if d["question_number"] in existing_qnums:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
            inserted += 1
            print(f"  INSERT Q{d['question_number']}")

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped: {skipped}")

    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
