"""
seed_simplification_sheet1.py
==============================
Seeds questions 2–9 (Simplification — recurring decimals / vulgar fractions)
from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Simplification
Run     : python seed_simplification_sheet1.py

Answer key verification:
  Q2: 0.41̄ → (41-4)/90 = 37/90                                      → A
  Q3: 0.5|87̄| → (587-5)/990 = 582/990 = 97/165 (CISF HCM 2023)      → B
  Q4: 0.4|68̄| → (468-4)/990 = 464/990 (UP S.I. 2021)                → C
  Q5: 0.51|345̄| → (51345-51)/99900 = 51294/99900                     → A
  Q6: 6.195̄ → fractional part = 176/900 = 44/225 → 6+44/225          → D
  Q7: 2.7̄ = 25/9; √(25/9) = 5/3 = 1.6̄                               → B
  Q8: SKIPPED — expression unclear in image
  Q9: 0.3|72̄| = (372-3)/990 = 369/990 = 41/110; x+y=41+110=151       → A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Simplification_Sheet1"
SUBJECT = "Quant"
TOPIC   = "Simplification"

QUESTIONS = [
    # Q2
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": "Express 0.41̄ (0.4111...) as a vulgar fraction.",
        "question_hi": "0.41̄ को साधारण भिन्न के रूप में व्यक्त करें।",
        "option_a": "37/90",
        "option_b": "41/90",
        "option_c": "47/90",
        "option_d": "31/90",
        "correct_answer": "A",
    },
    # Q3 — CISF HCM 2023
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": "Convert 0.5̄87̄ (0.58787...) into vulgar fraction. (CISF HCM 2023)",
        "question_hi": "0.5̄87̄ (0.58787...) को साधारण भिन्न (वल्गर फेक्शन) में परिवर्तित करें। (CISF HCM 2023)",
        "option_a": "91/165",
        "option_b": "97/165",
        "option_c": "95/167",
        "option_d": "93/167",
        "correct_answer": "B",
    },
    # Q4 — UP S.I. 13/11/2021 Morning
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": "Find the fraction of 0.4̄68̄ (0.4686868...). (UP S.I. 13/11/2021 Morning)",
        "question_hi": "0.4̄68̄ (0.4686868...) का भिन्न ज्ञात कीजिए। (UP S.I. 13/11/2021 Morning)",
        "option_a": "462/990",
        "option_b": "463/990",
        "option_c": "464/990",
        "option_d": "465/990",
        "correct_answer": "C",
    },
    # Q5
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": "What is the value of 0.51̄345̄ (0.51345345...) in vulgar fraction?",
        "question_hi": "0.51̄345̄ (0.51345345...) का मान साधारण भिन्न में कितना है?",
        "option_a": "51294/99900",
        "option_b": "51294/90000",
        "option_c": "51294/99000",
        "option_d": "52194/99000",
        "correct_answer": "A",
    },
    # Q6
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": "Express the number 6.19̄5̄ (6.1955555...) as a vulgar fraction.",
        "question_hi": "संख्या 6.19̄5̄ (6.1955555...) को एक साधारण भिन्न के रूप में व्यक्त कीजिए।",
        "option_a": "6 + 125/225",
        "option_b": "6 + 21/225",
        "option_c": "6 + 40/225",
        "option_d": "6 + 44/225",
        "correct_answer": "D",
    },
    # Q7
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": "Find the value of √(2.7̄) (where 7 is recurring)?",
        "question_hi": "√(2.7̄) का मान ज्ञात कीजिए?",
        "option_a": "1.6",
        "option_b": "1.6̄",
        "option_c": "1.55",
        "option_d": "1.8",
        "correct_answer": "B",
    },
    # Q9 — RRB Group D 2022
    {
        "question_number": 9,
        "difficulty": "medium",
        "question_en": "If 0.3̄72̄ = x/y, where x and y are co-prime, then what will be the value of (x + y)? (RRB Group D-2022)",
        "question_hi": "यदि 0.3̄72̄ = x/y है, जहाँ x और y सह-अभाज्य हैं, तो (x + y) का मान क्या होगा? (RRB Group D-2022)",
        "option_a": "151",
        "option_b": "134",
        "option_c": "186",
        "option_d": "143",
        "correct_answer": "A",
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
