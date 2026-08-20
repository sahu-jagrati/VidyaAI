"""
seed_reasoning_coded_equations_sheet2.py
==========================================
Seeds Coded Equations Q3-Q6 from Gagan Pratap Reasoning PDFs (Sheet 2).
Subject : Reasoning
Topic   : Coded Equations

Answer key:
  Q3  B — 504−36+21×213÷325=182
           After change: 504÷36×21+213−325 = 14×21+213−325 = 294+213−325 = 182 ✓
           (sign rules: +→×, ×→+, ÷→−, −→÷)

  Q4  B — 908
           Expression: 442+92×18÷186−6 (sign rules DIFFER: +→−, ×→+, ÷→×, −→÷)
           After change: 442−92+18×186÷6 = 350+558 = 908 ✓

  Q5  D — 4
           Numerator: 26+16−8×120÷56 → 26×16÷8+120−56 = 52+120−56 = 116
           Denominator: 343−49×22 → 343÷49+22 = 7+22 = 29
           Result: 116÷29 = 4 ✓
           (sign rules: +→×, ×→+, ÷→−, −→÷)

  Q6  B — 338−26+31×124÷243=284
           After change: 338÷26×31+124−243 = 13×31+124−243 = 403+124−243 = 284 ✓
           (sign rules: +→×, ×→+, ÷→−, −→÷)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Coded_Equations_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Coded Equations"

QUESTIONS = [
    # ── Q3 ── Select option correct after changing signs (+→×, ×→+, ÷→−, −→÷) ──────
    {
        "question_number": 3,
        "difficulty": "medium",
        "question_en": (
            'If "+" means "×", "×" means "+", "÷" means "−" and "−" means "÷", '
            "then select the option which is correct after changing signs.\n\n"
            "(A) 487+287÷18×273−196 = 473\n"
            "(B) 504−36+21×213÷325 = 182\n"
            "(C) 387×43+189÷290−190 = 384\n"
            "(D) 471+68−29÷321×29 = 287"
        ),
        "question_hi": (
            'यदि "+" का अर्थ "×" है, "×" का अर्थ "+" है, "÷" का अर्थ "−" है और '
            '"−" का अर्थ "÷" है, तो बताइए कौनसे विकल्प का उत्तर चिन्ह बदलने के '
            "बाद सही होगा?\n\n"
            "(A) 487+287÷18×273−196 = 473\n"
            "(B) 504−36+21×213÷325 = 182\n"
            "(C) 387×43+189÷290−190 = 384\n"
            "(D) 471+68−29÷321×29 = 287"
        ),
        "option_a": "487+287÷18×273−196 = 473",
        "option_b": "504−36+21×213÷325 = 182",
        "option_c": "387×43+189÷290−190 = 384",
        "option_d": "471+68−29÷321×29 = 287",
        "correct_answer": "B",
        # Verification of option B after sign change (−→÷, +→×, ×→+, ÷→−):
        # 504 − 36 + 21 × 213 ÷ 325
        # → 504 ÷ 36 × 21 + 213 − 325    (BODMAS: ÷ and × first, left-to-right)
        # = (504÷36) × 21 + 213 − 325
        # = 14 × 21 + 213 − 325
        # = 294 + 213 − 325
        # = 182 ✓
    },
    # ── Q4 ── Find the value (DIFFERENT sign rules) ───────────────────────────────────
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": (
            'If "+" means "−", "−" means "÷", "×" means "+" and "÷" means "×", '
            "then find the value of:\n\n"
            "442 + 92 × 18 ÷ 186 − 6 = ?\n\n"
            "(A) 900\n"
            "(B) 908\n"
            "(C) 980\n"
            "(D) 1092"
        ),
        "question_hi": (
            'यदि "+" का अर्थ "−" है, "−" का अर्थ "÷" है, "×" का अर्थ "+" है तथा '
            '"÷" का अर्थ "×" हो तो मान ज्ञात कीजिए:\n\n'
            "442 + 92 × 18 ÷ 186 − 6 = ?\n\n"
            "(A) 900\n"
            "(B) 908\n"
            "(C) 980\n"
            "(D) 1092"
        ),
        "option_a": "900",
        "option_b": "908",
        "option_c": "980",
        "option_d": "1092",
        "correct_answer": "B",
        # Sign rules for Q4 (different from Q1-Q3): +→−, −→÷, ×→+, ÷→×
        # Expression: 442 + 92 × 18 ÷ 186 − 6
        # After change: 442 − 92 + 18 × 186 ÷ 6
        # BODMAS: 18 × 186 = 3348; 3348 ÷ 6 = 558
        # 442 − 92 + 558 = 908 ✓
    },
    # ── Q5 ── Fraction expression (+→×, ×→+, ÷→−, −→÷) ──────────────────────────────
    {
        "question_number": 5,
        "difficulty": "hard",
        "question_en": (
            'If "+" means "×", "×" means "+", "÷" means "−" and "−" means "÷", '
            "then find the value of:\n\n"
            "  26 + 16 − 8 × 120 ÷ 56\n"
            "  ─────────────────────────  = ?\n"
            "      343 − 49 × 22\n\n"
            "(A) 3\n"
            "(B) 1\n"
            "(C) 2\n"
            "(D) 4"
        ),
        "question_hi": (
            'यदि "+" का अर्थ "×" है, "×" का अर्थ "+" है, "÷" का अर्थ "−" है और '
            '"−" का अर्थ "÷" है तो बताइए:\n\n'
            "  26 + 16 − 8 × 120 ÷ 56\n"
            "  ─────────────────────────  = ?\n"
            "      343 − 49 × 22\n\n"
            "(A) 3\n"
            "(B) 1\n"
            "(C) 2\n"
            "(D) 4"
        ),
        "option_a": "3",
        "option_b": "1",
        "option_c": "2",
        "option_d": "4",
        "correct_answer": "D",
        # After sign change (+→×, −→÷, ×→+, ÷→−):
        # Numerator: 26+16−8×120÷56 → 26×16÷8+120−56
        #   BODMAS: 26×16=416; 416÷8=52; 52+120−56=116
        # Denominator: 343−49×22 → 343÷49+22
        #   BODMAS: 343÷49=7; 7+22=29
        # Result: 116 ÷ 29 = 4 ✓
    },
    # ── Q6 ── Select option correct after changing signs (+→×, ×→+, ÷→−, −→÷) ──────
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": (
            'If "+" means "×", "×" means "+", "÷" means "−" and "−" means "÷", '
            "then select the option which is correct after changing signs.\n\n"
            "(A) 243÷127+361÷24×270 = 194\n"
            "(B) 338−26+31×124÷243 = 284\n"
            "(C) 136×142+217÷126−312 = 384\n"
            "(D) 197÷368+219−184×24 = 327"
        ),
        "question_hi": (
            'यदि "+" का अर्थ "×" है, "×" का अर्थ "+" है, "÷" का अर्थ "−" है और '
            '"−" का अर्थ "÷" है, तो बताइए कौनसे विकल्प का उत्तर चिन्ह बदलने के '
            "बाद सही होगा?\n\n"
            "(A) 243÷127+361÷24×270 = 194\n"
            "(B) 338−26+31×124÷243 = 284\n"
            "(C) 136×142+217÷126−312 = 384\n"
            "(D) 197÷368+219−184×24 = 327"
        ),
        "option_a": "243÷127+361÷24×270 = 194",
        "option_b": "338−26+31×124÷243 = 284",
        "option_c": "136×142+217÷126−312 = 384",
        "option_d": "197÷368+219−184×24 = 327",
        "correct_answer": "B",
        # Verification of option B after sign change (−→÷, +→×, ×→+, ÷→−):
        # 338 − 26 + 31 × 124 ÷ 243
        # → 338 ÷ 26 × 31 + 124 − 243    (BODMAS: ÷ and × first, left-to-right)
        # = (338÷26) × 31 + 124 − 243
        # = 13 × 31 + 124 − 243           (338÷26=13 exactly: 13×26=338 ✓)
        # = 403 + 124 − 243
        # = 284 ✓
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
