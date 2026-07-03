"""
seed_reasoning_analogy_sheet1.py
==================================
Seeds questions 1-20 (Analogy) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Analogy
Run     : python seed_reasoning_analogy_sheet1.py

Answer key verification:
  Q1:  21:3::574:?    — 574/7=82   (21/3=7)                                        → B
  Q2:  18:30::36:?    — 2A-6=B; 2*36-6=66                                          → D
  Q3:  17:52::1:?     — 3A+1=B; 3*1+1=4                                            → B
  Q4:  3:243::5:?     — A^5: 3^5=243, 5^5=3125                                     → D
  Q5:  20:11::102:?   — (A+2)/2=B; (102+2)/2=52                                    → B
  Q6:  42:20::64:?    — A/2-1=B; 64/2-1=31                                         → A
  Q7:  121:12::25:?   — sqrt(A)+1=B; sqrt(25)+1=6                                  → C
  Q8:  6:222::7:?     — A^3+A=B; 7^3+7=350                                         → D
  Q9:  26:5::65:?     — sqrt(A-1)=B; sqrt(64)=8                                    → C
  Q10: 25:125::36:?   — sqrt(A)^3=B; 6^3=216                                       → C
  Q11: 14:9::26:?     — sum of prime factors: 2+7=9, 2+13=15                       → C
  Q12: 8:28::27:?     — n^3 -> n^2*7: 3^2*7=63                                     → B
  Q13: 68:130::?:350  — n(n^2+1): 6*37=222                                         → C
  Q14: 1:1::25:?      — n^2:n^3: 5^3=125                                           → B
  Q15: 6:18::4:?      — A^2/2=B; 4^2/2=8                                           → C
  Q16: 42:56::72:?    — n(n+1): 9*10=90                                            → B
  Q17: 49:81::100:?   — (n+2)^2: 12^2=144                                          → B
  Q18: 9:80::100:?    — A^2-1=B; 100^2-1=9999                                      → D
  Q19: 7584:5362::4673:? — each digit -2: 4673->2451                               → B
  Q20: 3265:4376::4673:? — each digit +1: 4673->5784                               → D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Reasoning_Analogy_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Analogy"

QUESTIONS = [
    # Q1
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": "Choose the best alternative. 21 : 3 :: 574 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 21 : 3 :: 574 : ?",
        "option_a": "23",
        "option_b": "82",
        "option_c": "97",
        "option_d": "113",
        "correct_answer": "B",
    },
    # Q2
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": "Choose the best alternative. 18 : 30 :: 36 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 18 : 30 :: 36 : ?",
        "option_a": "54",
        "option_b": "62",
        "option_c": "64",
        "option_d": "66",
        "correct_answer": "D",
    },
    # Q3
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": "Choose the best alternative. 17 : 52 :: 1 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 17 : 52 :: 1 : ?",
        "option_a": "3",
        "option_b": "4",
        "option_c": "5",
        "option_d": "51",
        "correct_answer": "B",
    },
    # Q4
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": "Choose the best alternative. 3 : 243 :: 5 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 3 : 243 :: 5 : ?",
        "option_a": "425",
        "option_b": "465",
        "option_c": "546",
        "option_d": "3125",
        "correct_answer": "D",
    },
    # Q5
    {
        "question_number": 5,
        "difficulty": "easy",
        "question_en": "Choose the best alternative. 20 : 11 :: 102 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 20 : 11 :: 102 : ?",
        "option_a": "49",
        "option_b": "52",
        "option_c": "61",
        "option_d": "98",
        "correct_answer": "B",
    },
    # Q6
    {
        "question_number": 6,
        "difficulty": "easy",
        "question_en": "Choose the best alternative. 42 : 20 :: 64 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 42 : 20 :: 64 : ?",
        "option_a": "31",
        "option_b": "32",
        "option_c": "33",
        "option_d": "34",
        "correct_answer": "A",
    },
    # Q7
    {
        "question_number": 7,
        "difficulty": "easy",
        "question_en": "Choose the best alternative. 121 : 12 :: 25 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 121 : 12 :: 25 : ?",
        "option_a": "1",
        "option_b": "2",
        "option_c": "6",
        "option_d": "7",
        "correct_answer": "C",
    },
    # Q8
    {
        "question_number": 8,
        "difficulty": "medium",
        "question_en": "Choose the best alternative. 6 : 222 :: 7 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 6 : 222 :: 7 : ?",
        "option_a": "210",
        "option_b": "336",
        "option_c": "343",
        "option_d": "350",
        "correct_answer": "D",
    },
    # Q9
    {
        "question_number": 9,
        "difficulty": "easy",
        "question_en": "Choose the best alternative. 26 : 5 :: 65 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 26 : 5 :: 65 : ?",
        "option_a": "6",
        "option_b": "7",
        "option_c": "8",
        "option_d": "9",
        "correct_answer": "C",
    },
    # Q10
    {
        "question_number": 10,
        "difficulty": "easy",
        "question_en": "Choose the best alternative. 25 : 125 :: 36 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 25 : 125 :: 36 : ?",
        "option_a": "180",
        "option_b": "206",
        "option_c": "216",
        "option_d": "318",
        "correct_answer": "C",
    },
    # Q11
    {
        "question_number": 11,
        "difficulty": "medium",
        "question_en": "Choose the best alternative. 14 : 9 :: 26 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 14 : 9 :: 26 : ?",
        "option_a": "12",
        "option_b": "13",
        "option_c": "15",
        "option_d": "31",
        "correct_answer": "C",
    },
    # Q12
    {
        "question_number": 12,
        "difficulty": "medium",
        "question_en": "Choose the best alternative. 8 : 28 :: 27 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 8 : 28 :: 27 : ?",
        "option_a": "55",
        "option_b": "63",
        "option_c": "64",
        "option_d": "65",
        "correct_answer": "B",
    },
    # Q13
    {
        "question_number": 13,
        "difficulty": "hard",
        "question_en": "Choose the best alternative. 68 : 130 :: ? : 350",
        "question_hi": "सबसे उचित विकल्प चुनिए। 68 : 130 :: ? : 350",
        "option_a": "210",
        "option_b": "216",
        "option_c": "222",
        "option_d": "240",
        "correct_answer": "C",
    },
    # Q14
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": "Choose the best alternative. 1 : 1 :: 25 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 1 : 1 :: 25 : ?",
        "option_a": "26",
        "option_b": "125",
        "option_c": "240",
        "option_d": "525",
        "correct_answer": "B",
    },
    # Q15
    {
        "question_number": 15,
        "difficulty": "easy",
        "question_en": "Choose the best alternative. 6 : 18 :: 4 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 6 : 18 :: 4 : ?",
        "option_a": "2",
        "option_b": "6",
        "option_c": "8",
        "option_d": "16",
        "correct_answer": "C",
    },
    # Q16
    {
        "question_number": 16,
        "difficulty": "easy",
        "question_en": "Choose the best alternative. 42 : 56 :: 72 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 42 : 56 :: 72 : ?",
        "option_a": "81",
        "option_b": "90",
        "option_c": "92",
        "option_d": "100",
        "correct_answer": "B",
    },
    # Q17
    {
        "question_number": 17,
        "difficulty": "easy",
        "question_en": "Choose the best alternative. 49 : 81 :: 100 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 49 : 81 :: 100 : ?",
        "option_a": "64",
        "option_b": "144",
        "option_c": "169",
        "option_d": "121",
        "correct_answer": "B",
    },
    # Q18
    {
        "question_number": 18,
        "difficulty": "medium",
        "question_en": "Choose the best alternative. 9 : 80 :: 100 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 9 : 80 :: 100 : ?",
        "option_a": "901",
        "option_b": "1009",
        "option_c": "9889",
        "option_d": "9999",
        "correct_answer": "D",
    },
    # Q19
    {
        "question_number": 19,
        "difficulty": "easy",
        "question_en": "Choose the best alternative. 7584 : 5362 :: 4673 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 7584 : 5362 :: 4673 : ?",
        "option_a": "2367",
        "option_b": "2451",
        "option_c": "2531",
        "option_d": "None of these",
        "correct_answer": "B",
    },
    # Q20
    {
        "question_number": 20,
        "difficulty": "easy",
        "question_en": "Choose the best alternative. 3265 : 4376 :: 4673 : ?",
        "question_hi": "सबसे उचित विकल्प चुनिए। 3265 : 4376 :: 4673 : ?",
        "option_a": "2154",
        "option_b": "3562",
        "option_c": "5487",
        "option_d": "5784",
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
        print(f"\nDone -- inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
