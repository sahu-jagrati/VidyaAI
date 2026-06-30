"""
seed_lcm_hcf_sheet1.py
======================
Seeds 21 LCM & HCF questions from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : LCM & HCF
Run     : python seed_lcm_hcf_sheet1.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_LCM_HCF_Sheet1"
SUBJECT = "Quant"
TOPIC   = "LCM & HCF"

QUESTIONS = [
    # Q1 — RRB NTPC 12th LEVEL 2025
    {
        "question_number": 1,
        "difficulty": "hard",
        "question_en": "The LCM of 4³ × 6² × 15, 4² × 15² × 19 and 6³ × 15² × 19² is:",
        "question_hi": "4³ × 6² × 15, 4² × 15² × 19 और 6³ × 15² × 19² का लघुत्तम समापवर्त्य (LCM) ज्ञात कीजिए। (RRB NTPC 12th LEVEL 2025)",
        "option_a": "2⁵ × 3⁵ × 5² × 19²",
        "option_b": "2⁸ × 3⁴ × 5² × 19²",
        "option_c": "2⁵ × 3⁵ × 5³ × 19²",
        "option_d": "2⁸ × 3⁵ × 5² × 19²",
        "correct_answer": "D",
    },
    # Q2 — IB ACIO grade-2 2023
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": "The product of two co-prime numbers is 1073. Find their LCM?",
        "question_hi": "दो सह-अभाज्य संख्याओं का गुणनफल 1073 है। उनका LCM ज्ञात करें? (IB ACIO grade-2 2023)",
        "option_a": "29",
        "option_b": "1",
        "option_c": "1073",
        "option_d": "37",
        "correct_answer": "C",
    },
    # Q3 — RRB NTPC 2021
    {
        "question_number": 3,
        "difficulty": "medium",
        "question_en": "The least common multiple (LCM) of two prime numbers a and b (a > b) is 697. Find the value of a − 2b.",
        "question_hi": "दो अभाज्य संख्याओं a और b (a > b) का लघुत्तम समापवर्त्य (LCM) 697 है। a − 2b का मान ज्ञात कीजिए। (RRB NTPC 2021)",
        "option_a": "8",
        "option_b": "6",
        "option_c": "7",
        "option_d": "5",
        "correct_answer": "C",
    },
    # Q4
    {
        "question_number": 4,
        "difficulty": "easy",
        "question_en": "The LCM of 148 and 185 is ______.",
        "question_hi": "148 और 185 का ल.स.प. (LCM) कितना है?",
        "option_a": "37",
        "option_b": "940",
        "option_c": "740",
        "option_d": "87",
        "correct_answer": "C",
    },
    # Q5 — SSC CPO 2023
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": "Find the LCM of 15, 24, 35 and 54.",
        "question_hi": "15, 24, 35 और 54 का LCM ज्ञात कीजिए। (SSC CPO 2023)",
        "option_a": "7650",
        "option_b": "7560",
        "option_c": "6570",
        "option_d": "5670",
        "correct_answer": "B",
    },
    # Q6 — RRB RPF SI 2024
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": "The LCM of 27, 48, 276 and 368 is:",
        "question_hi": "27, 48, 276 और 368 का LCM है: (RRB RPF SI 2024)",
        "option_a": "9855",
        "option_b": "9936",
        "option_c": "9927",
        "option_d": "9988",
        "correct_answer": "B",
    },
    # Q7 — SSC GD 2025
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": "The LCM of 42, 36, 312 and 126 is:",
        "question_hi": "42, 36, 312 और 126 का LCM है: (SSC GD 2025)",
        "option_a": "6587",
        "option_b": "6616",
        "option_c": "6520",
        "option_d": "6552",
        "correct_answer": "D",
    },
    # Q8 — SSC CGL 2022
    {
        "question_number": 8,
        "difficulty": "medium",
        "question_en": "The LCM of 96, 136 and 504 is:",
        "question_hi": "96, 136 और 504 का लघुत्तम समापवर्तक क्या है? (SSC CGL 2022)",
        "option_a": "34272",
        "option_b": "36548",
        "option_c": "25872",
        "option_d": "28564",
        "correct_answer": "A",
    },
    # Q9 — SSC GD 2025
    {
        "question_number": 9,
        "difficulty": "medium",
        "question_en": "The LCM of 672 and 7056 is _______.",
        "question_hi": "672 और 7056 का LCM ज्ञात कीजिए। (SSC GD 2025)",
        "option_a": "14112",
        "option_b": "42336",
        "option_c": "28224",
        "option_d": "7056",
        "correct_answer": "A",
    },
    # Q10
    {
        "question_number": 10,
        "difficulty": "easy",
        "question_en": "If a positive integer 'n' is divisible by 3, 5 and 7, then what is the next larger integer divisible by all these numbers?",
        "question_hi": "यदि एक धन पूर्णांक 'n', 3, 5 और 7 से विभाज्य है, तो इन सभी संख्याओं से विभाजित होने वाला अगला बड़ा पूर्णांक क्या होगा?",
        "option_a": "n + 21",
        "option_b": "n + 35",
        "option_c": "n + 105",
        "option_d": "n + 110",
        "correct_answer": "C",
    },
    # Q11
    {
        "question_number": 11,
        "difficulty": "medium",
        "question_en": "What is the least 5-digit number that is divisible by 91?",
        "question_hi": "कम से कम 5-अंकीय संख्या ज्ञात करें जो 91 से विभाज्य है?",
        "option_a": "10283",
        "option_b": "10101",
        "option_c": "10000",
        "option_d": "10192",
        "correct_answer": "B",
    },
    # Q12 — SSC CGL 2023 PRE
    {
        "question_number": 12,
        "difficulty": "medium",
        "question_en": "The largest 5 digit number exactly divisible by 88 is:",
        "question_hi": "88 से पूर्णतः विभाज्य 5 अंकीय सबसे बड़ी संख्या ज्ञात कीजिए: (SSC CGL 2023 PRE)",
        "option_a": "99990",
        "option_b": "99984",
        "option_c": "99968",
        "option_d": "99880",
        "correct_answer": "C",
    },
    # Q13 — SSC CPO 2023
    {
        "question_number": 13,
        "difficulty": "hard",
        "question_en": "Find the least number which is exactly divisible by 20, 28, 34, 60 and 75.",
        "question_hi": "वह छोटी से छोटी संख्या ज्ञात कीजिए, जो 20, 28, 34, 60 और 75 से पूर्णतः विभाज्य हो। (SSC CPO 2023)",
        "option_a": "34500",
        "option_b": "35900",
        "option_c": "35700",
        "option_d": "36220",
        "correct_answer": "C",
    },
    # Q14
    {
        "question_number": 14,
        "difficulty": "easy",
        "question_en": "The smallest four-digit number which is divisible by 4, 8, 12 and 16 is:",
        "question_hi": "चार अंकों की वह सबसे छोटी संख्या कौन-सी है, जो 4, 8, 12, 16 से विभाज्य है?",
        "option_a": "1008",
        "option_b": "1006",
        "option_c": "1012",
        "option_d": "1010",
        "correct_answer": "A",
    },
    # Q15 — ICAR Technician 2023
    {
        "question_number": 15,
        "difficulty": "medium",
        "question_en": "What is the largest four-digit number that is exactly divisible by 15, 21, 36 and 42?",
        "question_hi": "चार अंकों की वह सबसे बड़ी संख्या कौन सी है जो 15, 21, 36 और 42 से पूर्णतः विभाज्य हो? (ICAR Technician 2023)",
        "option_a": "8820",
        "option_b": "8930",
        "option_c": "8970",
        "option_d": "8860",
        "correct_answer": "A",
    },
    # Q16
    {
        "question_number": 16,
        "difficulty": "hard",
        "question_en": "The least number of 5 digits which is exactly divisible by 52, 56, 78 and 91 is:",
        "question_hi": "5 अंकों की सबसे छोटी संख्या जो 52, 56, 78 और 91 से पूर्णतः विभाज्य है:",
        "option_a": "10290",
        "option_b": "10860",
        "option_c": "10920",
        "option_d": "10580",
        "correct_answer": "C",
    },
    # Q17
    {
        "question_number": 17,
        "difficulty": "medium",
        "question_en": "Find the greatest 5-digit number which is divisible by 11, 33, 99 and 121.",
        "question_hi": "5 अंकों की सबसे बड़ी संख्या ज्ञात कीजिए जो 11, 33, 99 और 121 से विभाज्य हो।",
        "option_a": "90099",
        "option_b": "99990",
        "option_c": "99099",
        "option_d": "90909",
        "correct_answer": "C",
    },
    # Q18
    {
        "question_number": 18,
        "difficulty": "hard",
        "question_en": "10A5A is a five-digit number which is exactly divisible by 2, 3, 4, 6, 8, 9, and 24 among other numbers. What is the value of the digit A?",
        "question_hi": "10A5A एक पाँच अंकों की संख्या है जो 2, 3, 4, 6, 8, 9 और 24 से पूर्णतः विभाज्य है। अंक A का मान क्या है?",
        "option_a": "8",
        "option_b": "4",
        "option_c": "2",
        "option_d": "6",
        "correct_answer": "D",
    },
    # Q19
    {
        "question_number": 19,
        "difficulty": "hard",
        "question_en": "Find the number between 22000 and 23000 that is divisible by each of 12, 18, 21 and 32.",
        "question_hi": "22000 और 23000 के बीच वह संख्या ज्ञात करें जो 12, 18, 21 और 32 से विभाजित हो।",
        "option_a": "22176",
        "option_b": "22536",
        "option_c": "22032",
        "option_d": "22276",
        "correct_answer": "A",
    },
    # Q20 — MTS 2020
    {
        "question_number": 20,
        "difficulty": "hard",
        "question_en": "What is the sum of the numbers between 300 and 500 such that when they are divided by 6, 12 and 16, it leaves no remainder?",
        "question_hi": "300 और 500 के मध्य की उन संख्याओं का योगफल कितना होगा जिन्हें 6, 12 और 16 से विभाजित करने पर शेषफल शून्य बचता है? (MTS 2020)",
        "option_a": "1586",
        "option_b": "1632",
        "option_c": "1764",
        "option_d": "1618",
        "correct_answer": "B",
    },
    # Q21
    {
        "question_number": 21,
        "difficulty": "hard",
        "question_en": "What is the least square number that is divisible by 8, 12 and 20?",
        "question_hi": "वह सबसे छोटी वर्ग संख्या कौन सी है जो 8, 12 और 20 से विभाज्य हो?",
        "option_a": "3600",
        "option_b": "4000",
        "option_c": "1000",
        "option_d": "5600",
        "correct_answer": "A",
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        existing = {
            row[0]
            for row in db.query(Question.question_en)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }
        existing_short = {q[:80] for q in existing}

        for d in QUESTIONS:
            if d["question_en"][:80] in existing_short:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue

            db.add(Question(
                subject        = SUBJECT,
                topic          = TOPIC,
                source_pdf     = SOURCE,
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
