"""
seed_reasoning_coded_equations_sheet6.py
==========================================
Seeds Coded Equations Q21-Q25 from Gagan Pratap Reasoning PDFs (Sheet 6).
Subject : Reasoning
Topic   : Coded Equations

Answer key:
  Q21 A — 5 (rules: +→−, −→×, ×→÷, ÷→+)
           5÷5+5−10×10 → 5+5−5×10÷10 = 5+5−5 = 5 ✓

  Q22 B — × − ÷ + (fill-in operators)
           33×4−15÷3+61 = 132−5+61 = 188 ✓

  Q23 D — 46 (pure math — nested brackets)
           30−[40−{56−(25−13−12)}] = 30−[40−56] = 30−(−16) = 46 ✓

  Q24 C — 4 (pure math — nested brackets with BODMAS)
           [76−{90÷5×(24−36÷3)÷3}] = 76−{18×12÷3} = 76−72 = 4 ✓

  Q25 A — −1 (pure math — signed numbers)
           3−(−6){−14}÷7{3} = 3−84÷21 = 3−4 = −1 ✓
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Coded_Equations_Sheet6"
SUBJECT = "Reasoning"
TOPIC   = "Coded Equations"

QUESTIONS = [
    # ── Q21 ── Find value (+ → −, − → ×, × → ÷, ÷ → +) — same rules as Q17 & Q18 ──
    {
        "question_number": 21,
        "difficulty": "medium",
        "question_en": (
            'If "+" means "−", "−" means "×", "×" means "÷" and "÷" means "+", '
            "then find the value of:\n\n"
            "5 ÷ 5 + 5 − 10 × 10 = ?\n\n"
            "(a) 5\n"
            "(b) 15\n"
            "(c) 10\n"
            "(d) 4"
        ),
        "question_hi": (
            'यदि + का अर्थ − है, − का अर्थ × है, × का अर्थ ÷ है, ÷ का अर्थ + है, '
            "तो निम्नलिखित व्यंजक का मान क्या होगा?\n\n"
            "5 ÷ 5 + 5 − 10 × 10 = ?\n\n"
            "(a) 5\n"
            "(b) 15\n"
            "(c) 10\n"
            "(d) 4"
        ),
        "option_a": "5",
        "option_b": "15",
        "option_c": "10",
        "option_d": "4",
        "correct_answer": "A",
        # After substitution (÷→+, +→−, −→×, ×→÷):
        # 5 + 5 − 5 × 10 ÷ 10
        # BODMAS: 5×10=50; 50÷10=5
        # 5 + 5 − 5 = 5 ✓
    },
    # ── Q22 ── Fill-in operators so equation balances ────────────────────────────────
    {
        "question_number": 22,
        "difficulty": "medium",
        "question_en": (
            "Select the correct combination of mathematical signs which, when "
            "placed sequentially in place of * signs in the given equation, "
            "makes the equation balanced.\n\n"
            "33 * 4 * 15 * 3 * 61 = 188\n\n"
            "(a) + − ÷ ×\n"
            "(b) × − ÷ +\n"
            "(c) + × − ÷\n"
            "(d) × ÷ + −"
        ),
        "question_hi": (
            "गणितीय चिन्हों के उस सही संयोजन का चयन करें, जिसे दिए गए समीकरण में "
            "* चिन्हों के स्थान पर क्रमिक रूप से रखे जाने पर समीकरण संतुलित हो जाए।\n\n"
            "33 * 4 * 15 * 3 * 61 = 188\n\n"
            "(a) + − ÷ ×\n"
            "(b) × − ÷ +\n"
            "(c) + × − ÷\n"
            "(d) × ÷ + −"
        ),
        "option_a": "+ − ÷ ×",
        "option_b": "× − ÷ +",
        "option_c": "+ × − ÷",
        "option_d": "× ÷ + −",
        "correct_answer": "B",
        # (b) × − ÷ +: 33×4−15÷3+61
        # BODMAS: 33×4=132; 15÷3=5
        # 132 − 5 + 61 = 188 ✓
        # (a): 33+4−15÷3×61 = 37−305 = −268 ≠ 188 ✗
        # (c): 33+4×15−3÷61 ≈ 93 ≠ 188 ✗
        # (d): 33×4÷15+3−61 ≈ −49 ≠ 188 ✗
    },
    # ── Q23 ── Find value of expression (nested brackets — pure math) ─────────────────
    {
        "question_number": 23,
        "difficulty": "medium",
        "question_en": (
            "Find the value of the given expression:\n\n"
            "30 − [40 − {56 − (25 − 13 − 12)}]\n\n"
            "(a) 38\n"
            "(b) 22\n"
            "(c) 14\n"
            "(d) 46"
        ),
        "question_hi": (
            "दिए गए व्यंजक का मान ज्ञात कीजिए:\n\n"
            "30 − [40 − {56 − (25 − 13 − 12)}]\n\n"
            "(a) 38\n"
            "(b) 22\n"
            "(c) 14\n"
            "(d) 46"
        ),
        "option_a": "38",
        "option_b": "22",
        "option_c": "14",
        "option_d": "46",
        "correct_answer": "D",
        # Step-by-step (innermost brackets first):
        # (25 − 13 − 12) = 0
        # {56 − 0} = 56
        # [40 − 56] = −16
        # 30 − (−16) = 30 + 16 = 46 ✓
    },
    # ── Q24 ── Find value of expression (nested brackets with BODMAS) ─────────────────
    {
        "question_number": 24,
        "difficulty": "hard",
        "question_en": (
            "Find the value of the given expression:\n\n"
            "[76 − {90 ÷ 5 × (24 − 36 ÷ 3) ÷ 3}]\n\n"
            "(a) 71.5\n"
            "(b) 75.5\n"
            "(c) 4\n"
            "(d) 77.5"
        ),
        "question_hi": (
            "दिए गए व्यंजक का मान ज्ञात कीजिए:\n\n"
            "[76 − {90 ÷ 5 × (24 − 36 ÷ 3) ÷ 3}]\n\n"
            "(a) 71.5\n"
            "(b) 75.5\n"
            "(c) 4\n"
            "(d) 77.5"
        ),
        "option_a": "71.5",
        "option_b": "75.5",
        "option_c": "4",
        "option_d": "77.5",
        "correct_answer": "C",
        # Step-by-step (BODMAS, innermost brackets first):
        # Inner: (24 − 36÷3) = 24 − 12 = 12
        # Curly: {90÷5×12÷3} — left-to-right: 90÷5=18; 18×12=216; 216÷3=72
        # Square: [76 − 72] = 4 ✓
        # Common mistake (option b=75.5): treating 5×12 as a group → 90÷60÷3=0.5 → 76−0.5=75.5 ✗
    },
    # ── Q25 ── Find value (signed numbers in nested brackets) ────────────────────────
    {
        "question_number": 25,
        "difficulty": "hard",
        "question_en": (
            "Find the value of the given expression:\n\n"
            "3 − (−6){−2 − 9 − 3} ÷ 7{1 + (−2)(−1)}\n\n"
            "(a) −1\n"
            "(b) 15\n"
            "(c) 7\n"
            "(d) 1"
        ),
        "question_hi": (
            "दिए गए व्यंजक का मान ज्ञात कीजिए:\n\n"
            "3 − (−6){−2 − 9 − 3} ÷ 7{1 + (−2)(−1)}\n\n"
            "(a) −1\n"
            "(b) 15\n"
            "(c) 7\n"
            "(d) 1"
        ),
        "option_a": "−1",
        "option_b": "15",
        "option_c": "7",
        "option_d": "1",
        "correct_answer": "A",
        # Step-by-step:
        # Inner: (−2)(−1) = 2  →  {1+2} = 3
        # Inner: {−2−9−3} = −14
        # Expression: 3 − (−6)(−14) ÷ 7(3)
        #           = 3 − 84 ÷ 21        [(−6)(−14)=84; 7×3=21]
        #           = 3 − 4
        #           = −1 ✓
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
