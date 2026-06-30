"""
seed_lcm_hcf_sheet3.py
======================
Seeds questions 34–49 (LCM & HCF) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : LCM & HCF
Run     : python seed_lcm_hcf_sheet3.py

Answer key verification:
  Q34: LCM(5,6,7,8)=840 → x=840×2+3=1683, div by 9? 1683/9=187 ✓ → digit sum=18      → B
  Q35: LCM(15,18,42)=630 → x=630×3+8=1898, 1898/13=146 ✓ → digit sum=26              → C
  Q36: LCM(12,16,18,20,25)=3600 → x=3600×5+4=18004, 18004/7=2572 ✓ → thousands=8     → A
  Q37: LCM(17,19,34,95)=3230 → x=3230×3+16=9706, 9706/46=211 ✓ → digit sum=22        → D
  Q38: LCM(15,18,20,27)=540 → x=540×4+10=2170, 2170/31=70 ✓ → 47²-2170=39           → C
  Q39: LCM(8,9,11,12)=792 → x=792×6+3=4755, 4755/15=317 ✓ (>1000)                    → B
  Q40: LCM(10,14,16,35)=560 → x=560×21+1=11761, 11761/19=619 ✓ → digit sum=16        → B
  Q41: x+1 div by LCM(12,15,75)=300 → x=299                                           → C
  Q42: x+6 div by LCM(20,25,35,40)=1400 → x=1394                                      → D
  Q43: x+2 div by LCM(3,5,6,9)=90 → x=90×12-2=1078 (smallest 4-digit)                → C
  Q44: x+8 div by LCM(15,20,25)=300 → x=300×34-8=10192 (smallest 5-digit)             → A
  Q45: x+4 div by LCM(12,15,20,24,30)=120 → x=999960-4=999956 (largest 6-digit)       → B
  Q46: x+7 div by LCM(10,12,14,16)=1680 → x=4×1680-7=6713 ∈[6500,7000] → sum=17      → D
  Q47: x+7 div by LCM(12,16,35,42)=1680 → x=6×1680-7=10073 (smallest 5-digit) sum=11 → C
  Q48: x+8 div by LCM(16,24,30,36)=720 → x=720×6-8=4312, div by 7 ✓ → digit sum=10   → B
  Q49: x+9 div by LCM(34,38,85)=3230 → x=3230×3-9=9681, 9681/21=461 ✓ → sum=24       → D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_LCM_HCF_Sheet3"
SUBJECT = "Quant"
TOPIC   = "LCM & HCF"

QUESTIONS = [
    # Q34
    {
        "question_number": 34,
        "difficulty": "hard",
        "question_en": "Let x be the least number, which when divided by 5, 6, 7 and 8 leaves a remainder 3 in each case but when divided by 9 leaves no remainder. The sum of digits of x is:",
        "question_hi": "x सबसे छोटी संख्या है, जिसे 5, 6, 7 और 8 से विभाजित करने पर प्रत्येक स्थिति में 3 शेष बचता है, लेकिन जब इसे 9 से विभाजित किया जाता है तो शेष नहीं बचता है। x के अंकों का योग है:",
        "option_a": "17",
        "option_b": "18",
        "option_c": "19",
        "option_d": "20",
        "correct_answer": "B",
    },
    # Q35
    {
        "question_number": 35,
        "difficulty": "hard",
        "question_en": "What is the sum of the smallest number of digits, which divides by 15, 18 and 42, in each case the remainder remains 8 and which is completely divisible by 13?",
        "question_hi": "उस छोटी से छोटी संख्या के अंकों का योग क्या है, जिसे 15, 18 तथा 42 से विभाजित करने पर प्रत्येक दशा में शेषफल 8 बचता है और जो 13 से पूर्णतः विभाज्य है?",
        "option_a": "24",
        "option_b": "22",
        "option_c": "26",
        "option_d": "25",
        "correct_answer": "C",
    },
    # Q36
    {
        "question_number": 36,
        "difficulty": "hard",
        "question_en": "When 12, 16, 18, 20 and 25 divide the least number x, the remainder in each case is 4 but x is divisible by 7. What is the digit at the thousands place in x?",
        "question_hi": "जब 12, 16, 18, 20 और 25 छोटी से छोटी संख्या x को विभाजित करते हैं, तो प्रत्येक मामले में 4 शेष बचता है, लेकिन x, 7 से विभाज्य है। x में एक हजार वें स्थान पर कौन सा अंक है?",
        "option_a": "8",
        "option_b": "3",
        "option_c": "4",
        "option_d": "5",
        "correct_answer": "A",
    },
    # Q37
    {
        "question_number": 37,
        "difficulty": "hard",
        "question_en": "Let x be the least number that when divided by 17, 19, 34 and 95, the remainder in each case is 16, and x is divisible by 46. What is the sum of the digits of x?",
        "question_hi": "मान लिजिए x सबसे छोटी संख्या है जिसे 17, 19, 34 और 95 से विभाजित करने पर प्रत्येक स्थिति में शेषफल 16 आता है, और x, 46 से विभाज्य है। x के अंकों का योग क्या है?",
        "option_a": "20",
        "option_b": "21",
        "option_c": "23",
        "option_d": "22",
        "correct_answer": "D",
    },
    # Q38
    {
        "question_number": 38,
        "difficulty": "hard",
        "question_en": "Let x be the least number which when divided by 15, 18, 20 and 27, the remainder in each case is 10 and x is a multiple of 31. What least number should be added to x to make it a perfect square?",
        "question_hi": "बता दें कि x सबसे छोटी संख्या है जिसे 15, 18, 20 और 27 से विभाजित किये जाने पर प्रत्येक मामले में शेष 10 है और x, 31 का गुणक है। x को एक पूर्ण वर्ग बनाने के लिए इसमें क्या कम से कम संख्या जोड़ी जानी चाहिए?",
        "option_a": "43",
        "option_b": "36",
        "option_c": "39",
        "option_d": "37",
        "correct_answer": "C",
    },
    # Q39
    {
        "question_number": 39,
        "difficulty": "hard",
        "question_en": "There are some students to be seated in an auditorium. When they were seated in rows of 8, 9, 11, and 12, there always were 3 students left out. But when they were seated in 15 a row none were left. Find the minimum number of students in the auditorium, if the number of students was more than 1000.",
        "question_hi": "एक सभागार में कुछ छात्रों को बैठाया जाना है। जब वे 8, 9, 11, और 12 की पंक्तियों में बैठे थे, तो बैठने के लिए हमेशा 3 छात्र छूट जाते थे। लेकिन जब उन्हें 15 कतार में बैठाया गया तो कोई भी नहीं बचा। सभागार में छात्रों की न्यूनतम संख्या ज्ञात कीजिए, यदि छात्रों की संख्या 1000 से अधिक थी।",
        "option_a": "3225",
        "option_b": "4755",
        "option_c": "3660",
        "option_d": "4185",
        "correct_answer": "B",
    },
    # Q40 — ICAR Assistant 2022
    {
        "question_number": 40,
        "difficulty": "hard",
        "question_en": "What is the sum of the digits of the least 5-digit number which when divided by 10, 14, 16 and 35, the remainder in each is 1 and the number is divisible by 19? (ICAR Assistant 2022)",
        "question_hi": "5 अंकों की छोटी से छोटी संख्या के अंकों का योग क्या है जिसे 10, 14, 16 और 35 से विभाजित करने पर प्रत्येक में शेषफल 1 आता है और संख्या 19 से विभाज्य होती है? (ICAR Assistant 2022)",
        "option_a": "14",
        "option_b": "16",
        "option_c": "13",
        "option_d": "17",
        "correct_answer": "B",
    },
    # Q41
    {
        "question_number": 41,
        "difficulty": "medium",
        "question_en": "Find the smallest number that leaves a remainder of 11 on division by 12, a remainder of 14 on division by 15 and a remainder of 74 on division by 75.",
        "question_hi": "वह छोटी से छोटी संख्या ज्ञात कीजिए जिसे 12 से भाग देने पर 11, 15 से भाग देने पर 14 और 75 से भाग देने पर 74 शेष बचे।",
        "option_a": "599",
        "option_b": "899",
        "option_c": "299",
        "option_d": "598",
        "correct_answer": "C",
    },
    # Q42
    {
        "question_number": 42,
        "difficulty": "medium",
        "question_en": "Find the least number, which, when divided by 20, 25, 35 and 40 leaves remainders 14, 19, 29 and 34, respectively.",
        "question_hi": "वह सबसे छोटी संख्या ज्ञात कीजिए जिसे 20, 25, 35 और 40 से भाग देने पर क्रमशः 14, 19, 29 और 34 शेषफल प्राप्त होते हैं।",
        "option_a": "1238",
        "option_b": "1498",
        "option_c": "1389",
        "option_d": "1394",
        "correct_answer": "D",
    },
    # Q43 — UPSC CSAT 2025
    {
        "question_number": 43,
        "difficulty": "medium",
        "question_en": "A 4-digit number N is such that when divided by 3, 5, 6, 9 leaves a remainder 1, 3, 4, 7 respectively. What is the smallest value of N? (UPSC CSAT 2025)",
        "question_hi": "कोई 4-अंकों की संख्या N इस प्रकार है कि उसे 3, 5, 6, 9 से भाग देने पर क्रमशः 1, 3, 4, 7 शेषफल रहता है। N का लघुतम मान क्या है? (UPSC CSAT 2025)",
        "option_a": "1068",
        "option_b": "1072",
        "option_c": "1078",
        "option_d": "1082",
        "correct_answer": "C",
    },
    # Q44
    {
        "question_number": 44,
        "difficulty": "medium",
        "question_en": "Find the smallest 5-digit number which when divided by 15, 20 and 25 leaves remainders 7, 12 and 17, respectively.",
        "question_hi": "5 अंकों की वह सबसे छोटी संख्या ज्ञात करें जिसे 15, 20 और 25 से विभाजित करने पर क्रमशः 7, 12 और 17 शेषफल प्राप्त होते हैं।",
        "option_a": "10192",
        "option_b": "10194",
        "option_c": "10195",
        "option_d": "10193",
        "correct_answer": "A",
    },
    # Q45
    {
        "question_number": 45,
        "difficulty": "hard",
        "question_en": "Which is the largest six-digit number, which when divided by 12, 15, 20, 24 and 30 leaves the remainders 8, 11, 16, 20 and 26 respectively?",
        "question_hi": "छह अंकों वाली वह बड़ी से बड़ी संख्या कौन सी है जिसे 12, 15, 20, 24 और 30 से विभाजित करने पर शेषफल क्रमशः 8, 11, 16, 20 और 26 बचता है?",
        "option_a": "999982",
        "option_b": "999956",
        "option_c": "999960",
        "option_d": "999964",
        "correct_answer": "B",
    },
    # Q46
    {
        "question_number": 46,
        "difficulty": "hard",
        "question_en": "Let x be the number between 6500 and 7000 that when divided by 10, 12, 14 and 16, the remainders are 3, 5, 7 and 9, respectively. What is the sum of the digits of x?",
        "question_hi": "मान लिजिए x, 6500 और 7000 के बीच की वह संख्या है जिसे 10, 12, 14 और 16 से भाग देने पर क्रमशः शेषफल 3, 5, 7 और 9 आता है। x के अंकों का योग कितना है?",
        "option_a": "16",
        "option_b": "18",
        "option_c": "14",
        "option_d": "17",
        "correct_answer": "D",
    },
    # Q47
    {
        "question_number": 47,
        "difficulty": "hard",
        "question_en": "Let x be the least number of 5 digits which when divided by 12, 16, 35 and 42, the remainders are 5, 9, 28 and 35, respectively. What is the sum of digits of x?",
        "question_hi": "मान लीजिए x, 5 अंकों की सबसे छोटी संख्या है जिसे 12, 16, 35 और 42 से विभाजित करने पर क्रमशः 5, 9, 28 और 35 शेषफल आता है। x के अंकों का योग कितना है?",
        "option_a": "13",
        "option_b": "12",
        "option_c": "11",
        "option_d": "10",
        "correct_answer": "C",
    },
    # Q48
    {
        "question_number": 48,
        "difficulty": "hard",
        "question_en": "Find the sum of digits of a smallest number which when divided by 16, 24, 30 and 36 leaves remainder 8, 16, 22 and 28 respectively but exactly divisible by 7.",
        "question_hi": "उस छोटी से छोटी संख्या के अंकों का योग क्या है, जिसे 16, 24, 30 तथा 36 से विभाजित करने पर क्रमशः 8, 16, 22 और 28 शेषफल बचता है और जो 7 से पूर्णतः विभाज्य है?",
        "option_a": "9",
        "option_b": "10",
        "option_c": "13",
        "option_d": "11",
        "correct_answer": "B",
    },
    # Q49 — ICAR Technician 2023
    {
        "question_number": 49,
        "difficulty": "hard",
        "question_en": "Let x be the least number which when divided by 34, 38 and 85, the remainders are 25, 29 and 76, respectively, and x is divisible by 21. What is the sum of the digits of x? (ICAR Technician 2023)",
        "question_hi": "माना x वह सबसे छोटी संख्या है जिसे 34, 38 और 85 से भाग देने पर क्रमशः 25, 29 और 76 शेषफल बचता है और x, 21 से विभाज्य है। x के अंकों का योगफल कितना होगा? (ICAR Technician 2023)",
        "option_a": "26",
        "option_b": "25",
        "option_c": "23",
        "option_d": "24",
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
