"""
seed_permcomb_sheet3.py
========================
Seeds questions 22–25 (Permutation & Combination) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Permutation & Combination
Run     : python seed_permcomb_sheet3.py

Answer key verification:
  Q22: PERMUTATIONS (T×2), fix P & S → remaining 10 letters: 10!/2!             → B
  Q23: 4B 3G alternate → only BGBGBGB → 4!×3!=144                               → A
  Q24: EQUATION: vowels(E,U,A,I,O)=5, consonants(Q,T,N)=3 at fixed slots
       → 5!×3!=720                                                               → D
  Q25: MONDAY starts M: 5!=120; starts M ends Y: 4!=24; starts M not ends Y=96  → b
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_PermComb_Sheet3"
SUBJECT = "Quant"
TOPIC   = "Permutation & Combination"

QUESTIONS = [
    # Q22
    {
        "question_number": 22,
        "difficulty": "medium",
        "question_en": "In how many ways can the letters of the word PERMUTATIONS be arranged if the words start with P and end with S?",
        "question_hi": "PERMUTATIONS शब्द के अक्षरों को कितने प्रकार से व्यवस्थित किया जा सकता है यदि शब्द P से शुरू होते हैं और S से समाप्त होते हैं?",
        "option_a": "12!/2!",
        "option_b": "10!/2!",
        "option_c": "8!",
        "option_d": "10!",
        "correct_answer": "B",
    },
    # Q23
    {
        "question_number": 23,
        "difficulty": "medium",
        "question_en": "In how many ways can 4 boys and 3 girls be seated in a row so that they are alternate?",
        "question_hi": "कितने तरीकों से 4 लड़कों और 3 लड़कियों को एक पंक्ति में बैठाया जा सकता है ताकि वे वैकल्पिक हों?",
        "option_a": "144",
        "option_b": "720",
        "option_c": "256",
        "option_d": "120",
        "correct_answer": "A",
    },
    # Q24
    {
        "question_number": 24,
        "difficulty": "hard",
        "question_en": "How many different words can be formed from the letters of the word 'EQUATION' without changing the relative order of vowels and consonants?",
        "question_hi": "स्वर और व्यंजन के सापेक्ष क्रम को बदले बिना 'EQUATION' शब्द के अक्षरों से कितने अलग-अलग शब्द बनाए जा सकते हैं?",
        "option_a": "120",
        "option_b": "240",
        "option_c": "360",
        "option_d": "720",
        "correct_answer": "D",
    },
    # Q25
    {
        "question_number": 25,
        "difficulty": "medium",
        "question_en": "In how many ways can the letters of the word MONDAY be arranged? How many begin with M and don't end with Y?",
        "question_hi": "MONDAY शब्द के अक्षरों को कितने प्रकार से व्यवस्थित किया जा सकता है? ताकि M से शुरू होते हैं और Y पर खत्म नहीं होते?",
        "option_a": "72",
        "option_b": "96",
        "option_c": "84",
        "option_d": "90",
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
