"""
seed_permcomb_sheet5.py
========================
Seeds questions 38–45 (visible) from Permutation & Combination,
Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Permutation & Combination
Run     : python seed_permcomb_sheet5.py

Answer key verification:
  Q38: 7 boys → 8 gaps; place 5 girls: 7! × ⁸P₅ = 7! × 8!/3!                 → A
  Q39: 10 people round table: (10-1)! = 9!                                      → C
  Q40: 12 beads necklace (clock+flip): (12-1)!/2 = 11!/2                       → A
  Q44: 6 men circular=5!; 6 gaps for 5 women: P(6,5)=6!; total=5!×6!          → A
  Q45: 19C(3r)=19C(r+3) → 3r+(r+3)=19 → 4r=16 → r=4                         → B
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_PermComb_Sheet5"
SUBJECT = "Quant"
TOPIC   = "Permutation & Combination"

QUESTIONS = [
    # Q38
    {
        "question_number": 38,
        "difficulty": "hard",
        "question_en": "In how many ways can 7 boys and 5 girls be seated in a row so that no two of the girls may sit together?",
        "question_hi": "कितने तरीकों से 7 लड़कों और 5 लड़कियों को एक पंक्ति में बैठाया जा सकता है ताकि कोई भी दो लड़कियाँ एक साथ न बैठें?",
        "option_a": "7! × ⁸P₅  (= 7! × 8!/3!)",
        "option_b": "3! × ⁶P₈ / 8!",
        "option_c": "2! × ⁸P₅",
        "option_d": "5! × 8!/2!",
        "correct_answer": "A",
    },
    # Q39
    {
        "question_number": 39,
        "difficulty": "easy",
        "question_en": "At a dinner party 6 men and 4 women sit at a round table. In how many ways can they sit?",
        "question_hi": "एक डिनर पार्टी में 6 पुरुष और 4 महिलाएँ एक गोल मेज पर बैठे हैं। वे कितने प्रकार से बैठ सकते हैं?",
        "option_a": "11!",
        "option_b": "8!",
        "option_c": "9!",
        "option_d": "10!",
        "correct_answer": "C",
    },
    # Q40
    {
        "question_number": 40,
        "difficulty": "medium",
        "question_en": "Find the number of ways in which 12 different beads can be arranged to form a necklace.",
        "question_hi": "एक हार बनाने के लिए 12 अलग-अलग मोतियों को कितने तरीकों से व्यवस्थित किया जा सकता है?",
        "option_a": "11!/2",
        "option_b": "12!/2",
        "option_c": "10!/2",
        "option_d": "13!/2",
        "correct_answer": "A",
    },
    # Q44
    {
        "question_number": 44,
        "difficulty": "hard",
        "question_en": "Find the number of ways in which 6 men and 5 women can dine at a round table if no two women can sit together.",
        "question_hi": "यदि कोई दो महिलाएं एक साथ नहीं बैठ सकती हैं, तो 6 पुरुष और 5 महिलाएं एक गोल मेज पर कितने तरीकों से भोजन कर सकते हैं?",
        "option_a": "5! × 6!",
        "option_b": "5! × 5!",
        "option_c": "4! × 5!",
        "option_d": "6!",
        "correct_answer": "A",
    },
    # Q45
    {
        "question_number": 45,
        "difficulty": "medium",
        "question_en": "If ¹⁹C₃ᵣ = ¹⁹Cᵣ₊₃, then the value of r is?",
        "question_hi": "यदि ¹⁹C₃ᵣ = ¹⁹Cᵣ₊₃, तो r का मान ज्ञात कीजिए?",
        "option_a": "3",
        "option_b": "4",
        "option_c": "5",
        "option_d": "8",
        "correct_answer": "B",
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
            if d["question_en"][:80] in existing_short:
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
        print(f"\nDone — inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
