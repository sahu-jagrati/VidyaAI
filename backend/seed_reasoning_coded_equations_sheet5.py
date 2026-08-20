"""
seed_reasoning_coded_equations_sheet5.py
==========================================
Seeds Coded Equations Q16-Q20 from Gagan Pratap Reasoning PDFs (Sheet 5).
Subject : Reasoning
Topic   : Coded Equations

Answer key:
  Q16 D — 8+6÷2×15−3=51
           After change (+→×,×→+,÷→−,−→÷): 8×6−2+15÷3 = 48−2+5 = 51 ✓

  Q17 A — 6 (rules: +→−, −→×, ×→÷, ÷→+)
           3÷6+3−4×4 → 3+6−3×4÷4 = 3+6−3 = 6 ✓

  Q18 D — 62 (rules: +→−, −→×, ×→÷, ÷→+)
           45×9÷12−5+3 → 45÷9+12×5−3 = 5+60−3 = 62 ✓

  Q19 B — ÷ − × + (fill-in operators)
           268÷4−8×5+14 = 67−40+14 = 41 ✓

  Q20 D — 189 (rules: ÷→−, −→×, ×→+, +→÷)
           77÷7×17−49+7 → 77−7+17×49÷7 = 70+119 = 189 ✓
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Coded_Equations_Sheet5"
SUBJECT = "Reasoning"
TOPIC   = "Coded Equations"

QUESTIONS = [
    # ── Q16 ── Select option correct after changing signs (+→×, ×→+, ÷→−, −→÷) ─────
    {
        "question_number": 16,
        "difficulty": "medium",
        "question_en": (
            'If "+" means "×", "×" means "+", "÷" means "−" and "−" means "÷", '
            "then select the option which is correct after changing signs.\n\n"
            "(A) 5×6−5+3÷2 = 20\n"
            "(B) 15+12÷4−2×4 = 180\n"
            "(C) 10−5×3+4÷1 = 15\n"
            "(D) 8+6÷2×15−3 = 51"
        ),
        "question_hi": (
            'यदि "+" का अर्थ "×" है, "×" का अर्थ "+" है, "÷" का अर्थ "−" है और '
            '"−" का अर्थ "÷" है, तो बताइए कौनसे विकल्प का उत्तर चिन्ह बदलने के '
            "बाद सही होगा?\n\n"
            "(A) 5×6−5+3÷2 = 20\n"
            "(B) 15+12÷4−2×4 = 180\n"
            "(C) 10−5×3+4÷1 = 15\n"
            "(D) 8+6÷2×15−3 = 51"
        ),
        "option_a": "5×6−5+3÷2 = 20",
        "option_b": "15+12÷4−2×4 = 180",
        "option_c": "10−5×3+4÷1 = 15",
        "option_d": "8+6÷2×15−3 = 51",
        "correct_answer": "D",
        # After sign change on option D (+→×, ÷→−, ×→+, −→÷):
        # 8+6÷2×15−3 → 8×6−2+15÷3
        # BODMAS: 8×6=48; 15÷3=5
        # 48 − 2 + 5 = 51 ✓
        # (A): 5+6÷5×3−2 = 5+1.2×3−2 = 5+3.6−2=6.6 ≠ 20 ✗
        # (B): 15×12−4÷2+4 = 180−2+4=182 ≠ 180 ✗
        # (C): 10÷5+3×4−1 = 2+12−1=13 ≠ 15 ✗
    },
    # ── Q17 ── Find value (+ → −, − → ×, × → ÷, ÷ → +) ─────────────────────────────
    {
        "question_number": 17,
        "difficulty": "easy",
        "question_en": (
            'If "+" means "−", "−" means "×", "×" means "÷" and "÷" means "+", '
            "then find the value of:\n\n"
            "3 ÷ 6 + 3 − 4 × 4 = ?\n\n"
            "(a) 6\n"
            "(b) 8\n"
            "(c) 4\n"
            "(d) 5"
        ),
        "question_hi": (
            'यदि + का अर्थ − है, − का अर्थ × है, × का अर्थ ÷ है, और ÷ का अर्थ + है, '
            "तो निम्नलिखित व्यंजक का मान क्या होगा?\n\n"
            "3 ÷ 6 + 3 − 4 × 4 = ?\n\n"
            "(a) 6\n"
            "(b) 8\n"
            "(c) 4\n"
            "(d) 5"
        ),
        "option_a": "6",
        "option_b": "8",
        "option_c": "4",
        "option_d": "5",
        "correct_answer": "A",
        # After substitution (÷→+, +→−, −→×, ×→÷):
        # 3 + 6 − 3 × 4 ÷ 4
        # BODMAS: 3×4=12; 12÷4=3
        # 3 + 6 − 3 = 6 ✓
    },
    # ── Q18 ── Find value (same rules as Q17: +→−, −→×, ×→÷, ÷→+) ───────────────────
    {
        "question_number": 18,
        "difficulty": "medium",
        "question_en": (
            'If "+" means "−", "−" means "×", "×" means "÷" and "÷" means "+", '
            "then find the value of:\n\n"
            "45 × 9 ÷ 12 − 5 + 3 = ?\n\n"
            "(a) 34\n"
            "(b) 27\n"
            "(c) 36\n"
            "(d) 62"
        ),
        "question_hi": (
            'यदि + का अर्थ − है, − का अर्थ × है, × का अर्थ ÷ है, और ÷ का अर्थ + है, '
            "तो निम्नलिखित व्यंजक का मान क्या होगा?\n\n"
            "45 × 9 ÷ 12 − 5 + 3 = ?\n\n"
            "(a) 34\n"
            "(b) 27\n"
            "(c) 36\n"
            "(d) 62"
        ),
        "option_a": "34",
        "option_b": "27",
        "option_c": "36",
        "option_d": "62",
        "correct_answer": "D",
        # After substitution (×→÷, ÷→+, −→×, +→−):
        # 45 ÷ 9 + 12 × 5 − 3
        # BODMAS: 45÷9=5; 12×5=60
        # 5 + 60 − 3 = 62 ✓
    },
    # ── Q19 ── Fill-in operators so equation balances ────────────────────────────────
    {
        "question_number": 19,
        "difficulty": "medium",
        "question_en": (
            "Select the correct combination of mathematical signs which, when "
            "placed sequentially in place of * signs in the given equation, "
            "makes the equation balanced.\n\n"
            "268 * 4 * 8 * 5 * 14 = 41\n\n"
            "(a) ÷ × + −\n"
            "(b) ÷ − × +\n"
            "(c) + × − ÷\n"
            "(d) × ÷ + −"
        ),
        "question_hi": (
            "गणितीय चिन्हों के उस सही संयोजन का चयन करें, जिसे दिए गए समीकरण में "
            "* चिन्हों के स्थान पर क्रमिक रूप से रखे जाने पर समीकरण संतुलित हो जाए।\n\n"
            "268 * 4 * 8 * 5 * 14 = 41\n\n"
            "(a) ÷ × + −\n"
            "(b) ÷ − × +\n"
            "(c) + × − ÷\n"
            "(d) × ÷ + −"
        ),
        "option_a": "÷ × + −",
        "option_b": "÷ − × +",
        "option_c": "+ × − ÷",
        "option_d": "× ÷ + −",
        "correct_answer": "B",
        # (b) ÷ − × +: 268÷4−8×5+14
        # BODMAS: 268÷4=67; 8×5=40
        # 67 − 40 + 14 = 41 ✓
        # (a): 268÷4×8+5−14 = 67×8+5−14 = 536+5−14 = 527 ≠ 41 ✗
    },
    # ── Q20 ── Find value (÷→−, −→×, ×→+, +→÷) ──────────────────────────────────────
    {
        "question_number": 20,
        "difficulty": "medium",
        "question_en": (
            'If "÷" means "−", "−" means "×", "×" means "+" and "+" means "÷", '
            "then find what comes in place of the question mark (?):\n\n"
            "77 ÷ 7 × 17 − 49 + 7 = ?\n\n"
            "(a) 169\n"
            "(b) 145\n"
            "(c) 119\n"
            "(d) 189"
        ),
        "question_hi": (
            'यदि ÷ का अर्थ − है, − का अर्थ × है, × का अर्थ + है, + का अर्थ ÷ है, '
            "तो प्रश्न-चिन्ह (?) के स्थान पर क्या आएगा?\n\n"
            "77 ÷ 7 × 17 − 49 + 7 = ?\n\n"
            "(a) 169\n"
            "(b) 145\n"
            "(c) 119\n"
            "(d) 189"
        ),
        "option_a": "169",
        "option_b": "145",
        "option_c": "119",
        "option_d": "189",
        "correct_answer": "D",
        # After substitution (÷→−, ×→+, −→×, +→÷):
        # 77 − 7 + 17 × 49 ÷ 7
        # BODMAS: 17×49=833; 833÷7=119
        # 77 − 7 + 119 = 189 ✓
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
