"""
seed_reasoning_coded_equations_sheet4.py
==========================================
Seeds Coded Equations Q11-Q15 from Gagan Pratap Reasoning PDFs (Sheet 4).
Subject : Reasoning
Topic   : Coded Equations

Answer key:
  Q11 C — interchange ÷ and −
           20−10÷2+3×4 = 20−5+12 = 27 ✓

  Q12 B — interchange − and ÷
           16÷8−4+5×2 = 2−4+10 = 8 ✓

  Q13 B — interchange − and +
           12÷2+6×3−8 = 6+18−8 = 16 ✓

  Q14 B — 4>3^8<1=6+2>24
           Rules: >=+, <=−, +=÷, ^=×, (literal = separates LHS/RHS)
           LHS: 4+3×8−1 = 27;  RHS: 6÷2+24 = 27  →  27 = 27 ✓

  Q15 B — 9>5>4=18+9>16
           Same rules as Q14.
           LHS: 9+5+4 = 18;  RHS: 18÷9+16 = 18  →  18 = 18 ✓
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Coded_Equations_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Coded Equations"

QUESTIONS = [
    # ── Q11 ── Which two signs to interchange to make equation correct? ───────────────
    {
        "question_number": 11,
        "difficulty": "medium",
        "question_en": (
            "In the following question, which two signs need to be interchanged "
            "in order to make the mathematical equation correct?\n\n"
            "20 ÷ 10 − 2 + 3 × 4 = 27\n\n"
            "(A) ÷ and ×\n"
            "(B) ÷ and +\n"
            "(C) ÷ and −\n"
            "(D) − and +"
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कौनसे दो चिन्हों को आपस में बदला जाए ताकि "
            "गणितीय समीकरण सही हो जाए?\n\n"
            "20 ÷ 10 − 2 + 3 × 4 = 27\n\n"
            "(A) ÷ और ×\n"
            "(B) ÷ और +\n"
            "(C) ÷ और −\n"
            "(D) − और +"
        ),
        "option_a": "÷ and ×",
        "option_b": "÷ and +",
        "option_c": "÷ and −",
        "option_d": "− and +",
        "correct_answer": "C",
        # Swap ÷ and −: 20 − 10 ÷ 2 + 3 × 4
        # BODMAS: 10÷2=5; 3×4=12
        # 20 − 5 + 12 = 27 ✓
    },
    # ── Q12 ── Which two signs to interchange? ────────────────────────────────────────
    {
        "question_number": 12,
        "difficulty": "medium",
        "question_en": (
            "In the following question, which two signs need to be interchanged "
            "in order to make the mathematical equation correct?\n\n"
            "16 − 8 ÷ 4 + 5 × 2 = 8\n\n"
            "(A) ÷ and ×\n"
            "(B) − and ÷\n"
            "(C) ÷ and +\n"
            "(D) − and ×"
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कौनसे दो चिन्हों को आपस में बदला जाए ताकि "
            "गणितीय समीकरण सही हो जाए?\n\n"
            "16 − 8 ÷ 4 + 5 × 2 = 8\n\n"
            "(A) ÷ और ×\n"
            "(B) − और ÷\n"
            "(C) ÷ और +\n"
            "(D) − और ×"
        ),
        "option_a": "÷ and ×",
        "option_b": "− and ÷",
        "option_c": "÷ and +",
        "option_d": "− and ×",
        "correct_answer": "B",
        # Swap − and ÷: 16 ÷ 8 − 4 + 5 × 2
        # BODMAS: 16÷8=2; 5×2=10
        # 2 − 4 + 10 = 8 ✓
    },
    # ── Q13 ── Which two signs to interchange? ────────────────────────────────────────
    {
        "question_number": 13,
        "difficulty": "medium",
        "question_en": (
            "In the following question, which two signs need to be interchanged "
            "in order to make the mathematical equation correct?\n\n"
            "12 ÷ 2 − 6 × 3 + 8 = 16\n\n"
            "(A) ÷ and +\n"
            "(B) − and +\n"
            "(C) × and +\n"
            "(D) ÷ and ×"
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कौनसे दो चिन्हों को आपस में बदला जाए ताकि "
            "गणितीय समीकरण सही हो जाए?\n\n"
            "12 ÷ 2 − 6 × 3 + 8 = 16\n\n"
            "(A) ÷ और +\n"
            "(B) − और +\n"
            "(C) × और +\n"
            "(D) ÷ और ×"
        ),
        "option_a": "÷ and +",
        "option_b": "− and +",
        "option_c": "× and +",
        "option_d": "÷ and ×",
        "correct_answer": "B",
        # Swap − and +: 12 ÷ 2 + 6 × 3 − 8
        # BODMAS: 12÷2=6; 6×3=18
        # 6 + 18 − 8 = 16 ✓
    },
    # ── Q14 ── Which statement is correct? (symbol substitution) ──────────────────────
    {
        "question_number": 14,
        "difficulty": "hard",
        "question_en": (
            'If ">" means "+", "<" means "−", "+" means "÷", "^" means "×", '
            '"−" means "=", "×" means ">" and "=" means "<", then which of '
            "the following statements will be correct?\n\n"
            "(A) 14>18+9=16+4<1\n"
            "(B) 4>3^8<1=6+2>24\n"
            "(C) 3<6^4>25=8+4>1\n"
            "(D) 12>9+3<6×25+5>6"
        ),
        "question_hi": (
            'यदि ">" का अर्थ "+" है, "<" का अर्थ "−" है, "+" का अर्थ "÷" है, '
            '"^" का अर्थ "×" है, "−" का अर्थ "=" है, "×" का अर्थ ">" है और '
            '"=" का अर्थ "<" है, तो निम्न में से कौनसा कथन सही होगा?\n\n'
            "(A) 14>18+9=16+4<1\n"
            "(B) 4>3^8<1=6+2>24\n"
            "(C) 3<6^4>25=8+4>1\n"
            "(D) 12>9+3<6×25+5>6"
        ),
        "option_a": "14>18+9=16+4<1",
        "option_b": "4>3^8<1=6+2>24",
        "option_c": "3<6^4>25=8+4>1",
        "option_d": "12>9+3<6×25+5>6",
        "correct_answer": "B",
        # Rules: > → +,  < → −,  + → ÷,  ^ → ×,  literal = separates LHS/RHS
        # (A) LHS: 14+18÷9 = 14+2 = 16; RHS: 16÷4−1 = 3;  16≠3 ✗
        # (B) LHS: 4+3×8−1 = 4+24−1 = 27
        #     RHS: 6÷2+24 = 3+24 = 27  →  27 = 27 ✓
        # (C) LHS: 3−6×4+25 = 3−24+25 = 4; RHS: 8÷4+1 = 3;  4≠3 ✗
        # (D) 12+9÷3−6 > 25÷5+6 → 9 > 11 → FALSE ✗
    },
    # ── Q15 ── Which statement is correct? (same symbol rules as Q14) ─────────────────
    {
        "question_number": 15,
        "difficulty": "hard",
        "question_en": (
            'If ">" means "+", "<" means "−", "+" means "÷", "^" means "×", '
            '"−" means "=", "×" means ">" and "=" means "<", then which of '
            "the following statements will be correct?\n\n"
            "(A) 13>7<6+2=3^4\n"
            "(B) 9>5>4=18+9>16\n"
            "(C) 9<3<2>1×8^2\n"
            "(D) 28+4^2=6^4+2"
        ),
        "question_hi": (
            'यदि ">" का अर्थ "+" है, "<" का अर्थ "−" है, "+" का अर्थ "÷" है, '
            '"^" का अर्थ "×" है, "−" का अर्थ "=" है, "×" का अर्थ ">" है और '
            '"=" का अर्थ "<" है, तो निम्न में से कौनसा कथन सही होगा?\n\n'
            "(A) 13>7<6+2=3^4\n"
            "(B) 9>5>4=18+9>16\n"
            "(C) 9<3<2>1×8^2\n"
            "(D) 28+4^2=6^4+2"
        ),
        "option_a": "13>7<6+2=3^4",
        "option_b": "9>5>4=18+9>16",
        "option_c": "9<3<2>1×8^2",
        "option_d": "28+4^2=6^4+2",
        "correct_answer": "B",
        # Rules same as Q14.
        # (A) LHS: 13+7−6÷2 = 13+7−3 = 17; RHS: 3×4 = 12;  17≠12 ✗
        # (B) LHS: 9+5+4 = 18
        #     RHS: 18÷9+16 = 2+16 = 18  →  18 = 18 ✓
        # (C) 9−3−2+1 > 8×2 → 5 > 16 → FALSE ✗
        # (D) LHS: 28÷4×2 = 7×2 = 14; RHS: 6×4÷2 = 12;  14≠12 ✗
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
