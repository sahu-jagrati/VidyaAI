"""
seed_permcomb_sheet6.py
========================
Seeds questions 46–50 (Permutation & Combination) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Permutation & Combination
Run     : python seed_permcomb_sheet6.py

Answer key verification:
  Q46: 17C4 + 17C14 = 17C4 + 17C3 = 18C4  (Pascal's identity)                  → A
  Q47: C(9,5) = 9!/(5!·4!) = 126                                                → B
  Q48: C(12,2) = 12·11/2 = 66                                                   → C
  Q49: P(11,2) = 11×10 = 110  (directed hug pairs per image answer key)         → B
  Q50: n(n-1)/2 = 28 → n=8                                                      → D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_PermComb_Sheet6"
SUBJECT = "Quant"
TOPIC   = "Permutation & Combination"

QUESTIONS = [
    # Q46
    {
        "question_number": 46,
        "difficulty": "easy",
        "question_en": "The value of ¹⁷C₄ + ¹⁷C₁₄ is?",
        "question_hi": "¹⁷C₄ + ¹⁷C₁₄ का मान है?",
        "option_a": "¹⁸C₄",
        "option_b": "³⁰C₁₆",
        "option_c": "¹⁷C₁₀",
        "option_d": "¹⁸C₁₅",
        "correct_answer": "A",
    },
    # Q47
    {
        "question_number": 47,
        "difficulty": "easy",
        "question_en": "In how many ways can 5 students be selected out of 9 students?",
        "question_hi": "9 छात्रों में से 5 छात्रों का चयन कितने तरीकों से किया जा सकता है?",
        "option_a": "125",
        "option_b": "126",
        "option_c": "128",
        "option_d": "None of these",
        "correct_answer": "B",
    },
    # Q48
    {
        "question_number": 48,
        "difficulty": "easy",
        "question_en": "There are 12 people in a party. If each of them shakes hands with each other, then how many handshakes are there in the party?",
        "question_hi": "एक पार्टी में 12 लोग होते हैं। यदि उनमें से प्रत्येक एक दूसरे से हाथ मिलाते हैं, तो पार्टी में कितने हाथ मिलाते हैं?",
        "option_a": "54",
        "option_b": "72",
        "option_c": "66",
        "option_d": "75",
        "correct_answer": "C",
    },
    # Q49
    {
        "question_number": 49,
        "difficulty": "easy",
        "question_en": "There are 11 people in a party and if each of them hugs with each other, how often do they hug?",
        "question_hi": "एक पार्टी में 11 लोग हैं और यदि उनमें से प्रत्येक एक दूसरे से गले मिलते हैं, तो वे कितनी बार गले लगाते हैं?",
        "option_a": "55",
        "option_b": "110",
        "option_c": "64",
        "option_d": "None of these",
        "correct_answer": "B",
    },
    # Q50
    {
        "question_number": 50,
        "difficulty": "medium",
        "question_en": "A total of 28 handshakes were exchanged at the conclusion of a party. Assuming that each participant was equally polite towards all the others, the number of people present was:",
        "question_hi": "एक पार्टी के समापन पर कुल 28 बार हाथ मिलाने का आदान-प्रदान हुआ। यह मानते हुए कि प्रत्येक प्रतिभागी अन्य सभी के प्रति समान रूप से विनम्र था, उपस्थित लोगों की संख्या थी:",
        "option_a": "14",
        "option_b": "7",
        "option_c": "9",
        "option_d": "8",
        "correct_answer": "D",
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
