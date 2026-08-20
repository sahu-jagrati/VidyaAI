"""
seed_reasoning_coded_equations_sheet3.py
==========================================
Seeds Coded Equations Q7-Q10 from Gagan Pratap Reasoning PDFs (Sheet 3).
Subject : Reasoning
Topic   : Coded Equations

Answer key:
  Q7  B — 294−21+25×130÷253=227
           After change (+→×,×→+,÷→−,−→÷):
           294÷21×25+130−253 = 14×25+130−253 = 350+130−253 = 227 ✓

  Q8  C — 32S8R9 = 180Q12R12 (P=+, Q=−, R=×, S=÷)
           LHS: 32÷8×9 = 36
           RHS: 180−12×12 = 180−144 = 36  →  36 = 36 ✓

  Q9  D — 44 (P→÷, R→+, T→−, V→×)
           12V4R16P8T6 → 12×4+16÷8−6 = 48+2−6 = 44 ✓

  Q10 D — 126 (P→×, R→+, T→−, W→÷)
           64W4P8T6R4 → 64÷4×8−6+4 = 16×8−6+4 = 128−6+4 = 126 ✓
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Coded_Equations_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Coded Equations"

QUESTIONS = [
    # ── Q7 ── Select option correct after changing signs (+→×, ×→+, ÷→−, −→÷) ──────
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": (
            'If "+" means "×", "×" means "+", "÷" means "−" and "−" means "÷", '
            "then select the option which is correct after changing signs.\n\n"
            "(A) 320×170÷34+168÷253 = 474\n"
            "(B) 294−21+25×130÷253 = 227\n"
            "(C) 312÷163×120+210−312 = 368\n"
            "(D) 284+364−132×21÷24 = 431"
        ),
        "question_hi": (
            'यदि "+" का अर्थ "×" है, "×" का अर्थ "+" है, "÷" का अर्थ "−" है और '
            '"−" का अर्थ "÷" है, तो बताइए कौनसे विकल्प का उत्तर चिन्ह बदलने के '
            "बाद सही होगा?\n\n"
            "(A) 320×170÷34+168÷253 = 474\n"
            "(B) 294−21+25×130÷253 = 227\n"
            "(C) 312÷163×120+210−312 = 368\n"
            "(D) 284+364−132×21÷24 = 431"
        ),
        "option_a": "320×170÷34+168÷253 = 474",
        "option_b": "294−21+25×130÷253 = 227",
        "option_c": "312÷163×120+210−312 = 368",
        "option_d": "284+364−132×21÷24 = 431",
        "correct_answer": "B",
        # After sign change on option B (−→÷, +→×, ×→+, ÷→−):
        # 294−21+25×130÷253 → 294÷21×25+130−253
        # BODMAS: 294÷21=14; 14×25=350
        # 350+130−253 = 227 ✓
    },
    # ── Q8 ── Which equation is correct? (P=+, Q=−, R=×, S=÷) ───────────────────────
    {
        "question_number": 8,
        "difficulty": "medium",
        "question_en": (
            'If P means "+", Q means "−", R means "×" and S means "÷", '
            "then which of the following equations is correct?\n\n"
            "(A) 36 R 4 S 8 Q 7 P 4 = 10\n"
            "(B) 16 R 12 P 49 S 7 Q 9 = 200\n"
            "(C) 32 S 8 R 9 = 180 Q 12 R 12\n"
            "(D) 8 R 18 P 8 S 18 Q 8 = 57"
        ),
        "question_hi": (
            'यदि P का अर्थ "+", Q का अर्थ "−", R का अर्थ "×" और S का अर्थ "÷" है, '
            "तो निम्न में से कौनसा कथन सही है?\n\n"
            "(A) 36 R 4 S 8 Q 7 P 4 = 10\n"
            "(B) 16 R 12 P 49 S 7 Q 9 = 200\n"
            "(C) 32 S 8 R 9 = 180 Q 12 R 12\n"
            "(D) 8 R 18 P 8 S 18 Q 8 = 57"
        ),
        "option_a": "36 R 4 S 8 Q 7 P 4 = 10",
        "option_b": "16 R 12 P 49 S 7 Q 9 = 200",
        "option_c": "32 S 8 R 9 = 180 Q 12 R 12",
        "option_d": "8 R 18 P 8 S 18 Q 8 = 57",
        "correct_answer": "C",
        # (A) 36×4÷8−7+4 = 15 ≠ 10 ✗
        # (B) 16×12+49÷7−9 = 192+7−9 = 190 ≠ 200 ✗
        # (C) LHS: 32÷8×9 = 4×9 = 36
        #     RHS: 180−12×12 = 180−144 = 36  →  36 = 36 ✓
        # (D) 8×18+8÷18−8 ≈ 136.4 ≠ 57 ✗
    },
    # ── Q9 ── Find the value (P→÷, R→+, T→−, V→×) ───────────────────────────────────
    {
        "question_number": 9,
        "difficulty": "medium",
        "question_en": (
            'If P means "÷", R means "+", T means "−" and V means "×", '
            "then find the value of:\n\n"
            "12 V 4 R 16 P 8 T 6 = ?\n\n"
            "(A) 138\n"
            "(B) 50\n"
            "(C) 28\n"
            "(D) 44\n"
            "(E) None of these"
        ),
        "question_hi": (
            'यदि P का अर्थ "÷" है, R का अर्थ "+" है, T का अर्थ "−" है और V का '
            'अर्थ "×" है तो\n\n'
            "12 V 4 R 16 P 8 T 6 = ?\n\n"
            "(A) 138\n"
            "(B) 50\n"
            "(C) 28\n"
            "(D) 44\n"
            "(E) None of these"
        ),
        "option_a": "138",
        "option_b": "50",
        "option_c": "28",
        "option_d": "44",
        "correct_answer": "D",
        # After substitution (P→÷, R→+, T→−, V→×):
        # 12 × 4 + 16 ÷ 8 − 6
        # BODMAS: 12×4=48; 16÷8=2
        # 48 + 2 − 6 = 44 ✓
        # (E) "None of these" is option E but answer is D=44.
    },
    # ── Q10 ── Find the value (P→×, R→+, T→−, W→÷) ──────────────────────────────────
    {
        "question_number": 10,
        "difficulty": "medium",
        "question_en": (
            'If P means "×", R means "+", T means "−" and W means "÷", '
            "then find the value of:\n\n"
            "64 W 4 P 8 T 6 R 4 = ?\n\n"
            "(A) 96\n"
            "(B) 2⅔\n"
            "(C) 130\n"
            "(D) 126\n"
            "(E) None of these"
        ),
        "question_hi": (
            'यदि P का अर्थ "×" है, R का अर्थ "+" है, T का अर्थ "−" है और W का '
            'अर्थ "÷" है तो\n\n'
            "64 W 4 P 8 T 6 R 4 = ?\n\n"
            "(A) 96\n"
            "(B) 2⅔\n"
            "(C) 130\n"
            "(D) 126\n"
            "(E) None of these"
        ),
        "option_a": "96",
        "option_b": "2⅔",
        "option_c": "130",
        "option_d": "126",
        "correct_answer": "D",
        # After substitution (P→×, R→+, T→−, W→÷):
        # 64 ÷ 4 × 8 − 6 + 4
        # BODMAS: 64÷4=16; 16×8=128 (left to right, ÷ then ×)
        # 128 − 6 + 4 = 126 ✓
        # (E) "None of these" is option E but answer is D=126.
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
