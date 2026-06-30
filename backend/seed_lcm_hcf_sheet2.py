"""
seed_lcm_hcf_sheet2.py
======================
Seeds questions 22–33 (LCM & HCF) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : LCM & HCF
Run     : python seed_lcm_hcf_sheet2.py

Answer key verification:
  Q22: LCM(16,24,30,36,45)=720 → least perfect square=3600 → 3600 mod 123=33          → B
  Q23: LCM(15,12,18,29)=5220   → 5220+8=5228                                           → C
  Q24: LCM(12,16,18,21)=1008   → 2×1008-2000=16 → digit sum=7                          → C
  Q25: LCM(45,60,75,120)=1800  → 6×1800-119=10681                                      → B
  Q26: LCM(19,36,54)=2052      → 2052+4=2056                                           → A
  Q27: LCM(8,12,15,24,25,40)=600 → 600+7=607 → 607 mod 29=27                          → B
  Q28: LCM(4,6,7,9)=252        → 252×4+3=1011                                          → D
  Q29: LCM(16,24,72,84)=1008   → 992×1008+15=999951                                    → B
  Q30: LCM(40,45,50,55)=19800  → 19800×3+23=59423 → digit sum=23                       → A
  Q31: LCM(12,16,24)=48, rem 5 → 581+629+677=1887                                      → B
  Q32: LCM(12,18,24,30)=360    → 360×1+4=364, 364÷7=52 (exact)                        → C
  Q33: LCM(8,16,18,20,25)=3600 → 3600×2+3=7203, 7203÷7=1029 (exact)                  → A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_LCM_HCF_Sheet2"
SUBJECT = "Quant"
TOPIC   = "LCM & HCF"

QUESTIONS = [
    # Q22
    {
        "question_number": 22,
        "difficulty": "hard",
        "question_en": "Let x be the least number divisible by 16, 24, 30, 36 and 45 and x is also a perfect square. What is the remainder when x is divided by 123?",
        "question_hi": "मान लिजिए x वह छोटी से छोटी संख्या है, जो 16, 24, 30, 36 और 45 से विभाज्य है तथा x एक पूर्ण वर्ग भी है। जब x को 123 से विभाजित किया जाता है तो शेषफल कितना बचता है?",
        "option_a": "103",
        "option_b": "33",
        "option_c": "100",
        "option_d": "40",
        "correct_answer": "B",
    },
    # Q23
    {
        "question_number": 23,
        "difficulty": "medium",
        "question_en": "The least number which, when diminished by 8, is divisible by 15, 12, 18 and 29 is:",
        "question_hi": "वह सबसे छोटी संख्या ज्ञात कीजिए, जिसमें से 8 घटाने पर वह 15, 12, 18 और 29 से विभाज्य हो।",
        "option_a": "5263",
        "option_b": "5275",
        "option_c": "5228",
        "option_d": "5187",
        "correct_answer": "C",
    },
    # Q24
    {
        "question_number": 24,
        "difficulty": "medium",
        "question_en": "Let x be the smallest number which when added to 2000 makes the resulting number divisible by 12, 16, 18 and 21. The sum of the digits of x is:",
        "question_hi": "मान लिजिए x वह सबसे छोटी संख्या है जिसमें यदि 2000 जोड़ दिया जाये तो प्राप्त संख्या 12, 16, 18 और 21 से पूरी-पूरी विभाजित होगी, तब x के अंकों का योगफल ज्ञात करें।",
        "option_a": "5",
        "option_b": "6",
        "option_c": "7",
        "option_d": "8",
        "correct_answer": "C",
    },
    # Q25
    {
        "question_number": 25,
        "difficulty": "hard",
        "question_en": "The least number of 5-digits which is divisible by 45, 60, 75 and 120 when it is added to 119 is:",
        "question_hi": "पाँच अंकों की सबसे छोटी संख्या क्या है जिसमें यदि 119 जोड़ दिया जाए तो प्राप्त संख्या 45, 60, 75 और 120 से पूरी-पूरी विभाजित होगी?",
        "option_a": "10800",
        "option_b": "10681",
        "option_c": "10321",
        "option_d": "10941",
        "correct_answer": "B",
    },
    # Q26 — SSC MTS 2023
    {
        "question_number": 26,
        "difficulty": "medium",
        "question_en": "Find the least number which when divided by 19, 36 and 54 leaves a remainder of 4 in each case. (SSC MTS 2023)",
        "question_hi": "वह सबसे छोटी संख्या ज्ञात कीजिए जिसे 19, 36 और 54 से भाग देने पर प्रत्येक स्थिति में 4 शेषफल बचता है। (SSC MTS 2023)",
        "option_a": "2056",
        "option_b": "1854",
        "option_c": "2172",
        "option_d": "1925",
        "correct_answer": "A",
    },
    # Q27 — MTS 2020
    {
        "question_number": 27,
        "difficulty": "hard",
        "question_en": "Let x be the least number which on being divided by 8, 12, 15, 24, 25 and 40 leaves a remainder of 7 in each case. What will be the remainder when x is divided by 29? (MTS 2020)",
        "question_hi": "माना x वह छोटी से छोटी संख्या है, जिसे 8, 12, 15, 24, 25 और 40 से विभाजित करने पर प्रत्येक स्थिति में 7 शेषफल प्राप्त होता है। जब x को 29 से विभाजित किया जाता है, तो प्राप्त होने वाला शेषफल ज्ञात करें। (MTS 2020)",
        "option_a": "18",
        "option_b": "27",
        "option_c": "19",
        "option_d": "20",
        "correct_answer": "B",
    },
    # Q28 — UPSC CDS-II 2025
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": "A number N is such that when divided by 4, 6, 7 or 9, it leaves 3 as remainder. What is the smallest 4-digit number that satisfies this property? (UPSC CDS-II 2025)",
        "question_hi": "एक संख्या N ऐसी है कि उसे 4, 6, 7 या 9 से विभाजित करने पर शेषफल 3 बचता है। वह सबसे छोटी 4-अंकीय संख्या कौन सी है जो इस गुण को संतुष्ट करती है? (UPSC CDS-II 2025)",
        "option_a": "1003",
        "option_b": "1005",
        "option_c": "1007",
        "option_d": "1011",
        "correct_answer": "D",
    },
    # Q29
    {
        "question_number": 29,
        "difficulty": "hard",
        "question_en": "What is the greatest number of six digits, which when divided by each of 16, 24, 72 and 84, leaves the remainder 15?",
        "question_hi": "छह अंकों की वह बड़ी से बड़ी संख्या कौन सी है, जिसे 16, 24, 72 और 84 में से प्रत्येक से विभाजित करने पर शेषफल 15 बचता है?",
        "option_a": "999981",
        "option_b": "999951",
        "option_c": "999963",
        "option_d": "999915",
        "correct_answer": "B",
    },
    # Q30 — MTS 2020
    {
        "question_number": 30,
        "difficulty": "hard",
        "question_en": "Let x be the least number between 56,000 and 60,000 which when divided by 40, 45, 50 and 55 leaves a remainder of 23 in each case. What is the sum of the digits of x? (MTS 2020)",
        "question_hi": "माना x, 56,000 और 60,000 के बीच वह छोटी से छोटी संख्या है, जिसे जब 40, 45, 50 और 55 से विभाजित किया जाता है, तो प्रत्येक स्थिति में शेषफल 23 प्राप्त होता है। x के अंकों का योगफल ज्ञात करें। (MTS 2020)",
        "option_a": "23",
        "option_b": "21",
        "option_c": "26",
        "option_d": "19",
        "correct_answer": "A",
    },
    # Q31
    {
        "question_number": 31,
        "difficulty": "hard",
        "question_en": "Find the sum of the numbers between 550 and 700 such that when they are divided by 12, 16 and 24, they leave a remainder of 5 in each case.",
        "question_hi": "550 और 700 के बीच की उन संख्याओं का योग ज्ञात कीजिए, जिन्हें 12, 16 और 24 से विभाजित करने पर प्रत्येक स्थिति में शेषफल 5 प्राप्त होगा।",
        "option_a": "1980",
        "option_b": "1887",
        "option_c": "1860",
        "option_d": "1867",
        "correct_answer": "B",
    },
    # Q32
    {
        "question_number": 32,
        "difficulty": "hard",
        "question_en": "Find the least number which when divided by 12, 18, 24 and 30 leaves 4 as remainder in each case, but when divided by 7 leaves no remainder.",
        "question_hi": "वह सबसे छोटी संख्या ज्ञात कीजिए, जिसे 12, 18, 24 और 30 से विभाजित करने पर हर मामले में शेषफल के रूप में 4 बचता है, लेकिन जब 7 से विभाजित किया जाता है, तब कोई शेषफल नहीं बचता है।",
        "option_a": "634",
        "option_b": "366",
        "option_c": "364",
        "option_d": "384",
        "correct_answer": "C",
    },
    # Q33 — SSC GD 2025
    {
        "question_number": 33,
        "difficulty": "hard",
        "question_en": "When 8, 16, 18, 20 and 25 divide the least number x, the remainder in each case is 3, but x is divisible by 7. What is the value of x? (SSC GD 2025)",
        "question_hi": "जब 8, 16, 18, 20 और 25 से सबसे छोटी संख्या x को भाग दिया जाता है, तो प्रत्येक स्थिति में शेषफल 3 होता है, लेकिन x, 7 से विभाज्य है। x का मान कितना है? (SSC GD 2025)",
        "option_a": "7203",
        "option_b": "7302",
        "option_c": "7320",
        "option_d": "7023",
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
