"""
seed_permcomb_sheet8.py
========================
Seeds questions 60, 61, 63, 64, 65 (Permutation & Combination)
from Gagan Pratap Sir PDFs. (Q62 not visible in source image)
Subject : Quant
Topic   : Permutation & Combination
Run     : python seed_permcomb_sheet8.py

Answer key verification:
  Q60: 13 players(4B+9N), team 11 with ≥2 bowlers:
       C(4,2)C(9,9)+C(4,3)C(9,8)+C(4,4)C(9,7)=6+36+36=78                     → C
  Q61: 1 king from 4 + 4 non-kings from 48:
       C(4,1)×C(48,4)=4×(48×47×46×45)/24=360×47×46=778320                     → A
  Q63: At least 1 officer from 4 officers & 8 constables (choose 6):
       C(12,6)-C(8,6)=924-28=896                                                → C
  Q64: At least 1 boy from 6 boys & 4 girls (choose 4):
       C(10,4)-C(4,4)=210-1=209                                                 → B
  Q65: 20 breads, 4 persons, each ≥3: give 3 each (12 fixed), distribute
       remaining 8 freely: C(8+3,3)=C(11,3)=165                                → C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_PermComb_Sheet8"
SUBJECT = "Quant"
TOPIC   = "Permutation & Combination"

QUESTIONS = [
    # Q60
    {
        "question_number": 60,
        "difficulty": "medium",
        "question_en": "In the 13 cricket players 4 are bowlers. In how many ways can a cricket team of 11 players be formed in which at least 2 bowlers are included?",
        "question_hi": "13 क्रिकेट खिलाड़ियों में 4 गेंदबाज हैं, तो 11 खिलाड़ियों की एक क्रिकेट टीम कितने तरीकों से बनाई जा सकती है जिसमें कम से कम 2 गेंदबाज शामिल हों?",
        "option_a": "55",
        "option_b": "72",
        "option_c": "78",
        "option_d": "None of these",
        "correct_answer": "C",
    },
    # Q61
    {
        "question_number": 61,
        "difficulty": "hard",
        "question_en": "Determine the number of 5-card combinations out of a deck of 52 cards if each selection of 5 cards has exactly one king.",
        "question_hi": "52 कार्डों की एक गड्डी में से 5 कार्ड संयोजनों की संख्या निर्धारित करें यदि 5 कार्डों के प्रत्येक चयन में ठीक एक बादशाह हो?",
        "option_a": "360×47×46",
        "option_b": "360×48×46",
        "option_c": "365×46×47",
        "option_d": "None",
        "correct_answer": "A",
    },
    # Q63
    {
        "question_number": 63,
        "difficulty": "medium",
        "question_en": "In how many ways can 6 persons be selected from 4 officers and 8 constables, if at least one officer is to be included?",
        "question_hi": "यदि कम से कम एक अधिकारी को शामिल करना हो तो 4 अधिकारियों और 8 कांस्टेबलों में से 6 व्यक्तियों को कितने तरीकों से चुना जा सकता है?",
        "option_a": "224",
        "option_b": "672",
        "option_c": "896",
        "option_d": "576",
        "correct_answer": "C",
    },
    # Q64
    {
        "question_number": 64,
        "difficulty": "medium",
        "question_en": "In how many ways can 4 children be selected from a group of 6 boys and 4 girls so that at least one boy is always there in the group?",
        "question_hi": "6 लड़कों और 4 लड़कियों के समूह में से 4 बच्चों को कितने तरीकों से चुना जा सकता है ताकि समूह में हमेशा कम से कम एक लड़का मौजूद रहे?",
        "option_a": "159",
        "option_b": "209",
        "option_c": "194",
        "option_d": "185",
        "correct_answer": "B",
    },
    # Q65
    {
        "question_number": 65,
        "difficulty": "hard",
        "question_en": "The number of ways in which 20 breads can be eaten by 4 persons such that each person eats at least 3 breads is?",
        "question_hi": "4 व्यक्तियों द्वारा 20 रोटियों को कितने प्रकार से खाया जा सकता है कि प्रत्येक व्यक्ति कम से कम 3 रोटियाँ खाए?",
        "option_a": "130",
        "option_b": "166",
        "option_c": "165",
        "option_d": "120",
        "correct_answer": "C",
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
