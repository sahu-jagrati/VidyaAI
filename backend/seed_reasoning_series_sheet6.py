"""
seed_reasoning_series_sheet6.py
=================================
Seeds questions 54-65 (Series) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Series
Run     : python seed_reasoning_series_sheet6.py

Answer key verification:
  Q54: 31,33,37,43,51,? — diffs +2,+4,+6,+8,+10 → 61                              → A
  Q55: 45,90,154,?,347 — 2nd diffs +19,+21,+23 → 239                               → D
  Q56: TWEZ,XBYG,?,FLMU,JQGB — const col increments +4,+5,+20,+7 → BGSN           → C
  Q57: 1,6,15,28,?,?,91 — T_odd: n(2n-1); blanks n=5,6 → 45,66                    → D
  Q58: 1,1,2,3,5,8,13,? — Fibonacci → 21                                            → B
  Q59: HEWC,KIRI,?,QQHU,TUCA — col increments +3,+4,-5,+6 → NMMO                  → A
  Q60: 25,40,70,115,175,? — diffs 15,30,45,60,75 → 250                             → C
  Q61: 7,16,43,124,367,? — each x3-5 → 1096                                        → B
  Q62: FDKI,GCMG,?,IAQC — col increments +1,-1,+2,-2 → HBOE                        → B
  Q63: 14,6,5,6,12,? — up-diffs 1,6,17 (2nd diffs +5,+11) → 29                    → C
  Q64: 55,165,495,1485,?,13365 — each x3 → 4455                                    → A
  Q65: opq_stopqrsto_qrs_opqr_t — "opqrst" repeating; blanks → r,p,t,s            → A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Reasoning_Series_Sheet6"
SUBJECT = "Reasoning"
TOPIC   = "Series"

QUESTIONS = [
    # Q54
    {
        "question_number": 54,
        "difficulty": "easy",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 31, 33, 37, 43, 51, ? [CPO - 27 Jun 2024 - Shift 1]",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 31, 33, 37, 43, 51, ?",
        "option_a": "61",
        "option_b": "71",
        "option_c": "81",
        "option_d": "51",
        "correct_answer": "A",
    },
    # Q55
    {
        "question_number": 55,
        "difficulty": "medium",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 45, 90, 154, ?, 347 [CPO - 27 Jun 2024 - Shift 1]",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 45, 90, 154, ?, 347",
        "option_a": "256",
        "option_b": "273",
        "option_c": "248",
        "option_d": "239",
        "correct_answer": "D",
    },
    # Q56
    {
        "question_number": 56,
        "difficulty": "medium",
        "question_en": "Which of the following letter clusters will replace the blank in the given series? TWEZ, XBYG, ?, FLMU, JQGB [CPO - 27 Jun 2024 - Shift 1]",
        "question_hi": "निम्नलिखित में से कौन सा अक्षर समूह दी गई श्रृंखला में रिक्त स्थान को प्रतिस्थापित करेगा? TWEZ, XBYG, ?, FLMU, JQGB",
        "option_a": "BJEN",
        "option_b": "TWKN",
        "option_c": "BGSN",
        "option_d": "TWEH",
        "correct_answer": "C",
    },
    # Q57
    {
        "question_number": 57,
        "difficulty": "medium",
        "question_en": "Which of the following numbers will replace the question marks (?) in the given series? 1, 6, 15, 28, ?, ?, 91 [CPO - 27 Jun 2024 - Shift 2]",
        "question_hi": "निम्नलिखित में से कौन सी संख्याएं दी गई श्रृंखला में प्रश्न चिह्नों (?) को प्रतिस्थापित करेंगी? 1, 6, 15, 28, ?, ?, 91",
        "option_a": "40, 60",
        "option_b": "42, 54",
        "option_c": "44, 54",
        "option_d": "45, 66",
        "correct_answer": "D",
    },
    # Q58
    {
        "question_number": 58,
        "difficulty": "easy",
        "question_en": "Select the number that will replace the question mark (?) in the following series. 1, 1, 2, 3, 5, 8, 13, ? [GD Con - 21 Feb 2024 - Shift 1]",
        "question_hi": "निम्नलिखित श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करने वाली संख्या का चयन कीजिए। 1, 1, 2, 3, 5, 8, 13, ?",
        "option_a": "22",
        "option_b": "21",
        "option_c": "24",
        "option_d": "20",
        "correct_answer": "B",
    },
    # Q59
    {
        "question_number": 59,
        "difficulty": "hard",
        "question_en": "Which of the following letter clusters will replace the blank in the given series? HEWC, KIRI, ?, QQHU, TUCA [GD Con - 21 Feb 2024 - Shift 2]",
        "question_hi": "निम्नलिखित में से कौन सा अक्षर समूह दी गई श्रृंखला में रिक्त स्थान को प्रतिस्थापित करेगा? HEWC, KIRI, ?, QQHU, TUCA",
        "option_a": "NMMO",
        "option_b": "PRZO",
        "option_c": "NBTO",
        "option_d": "JLSO",
        "correct_answer": "A",
    },
    # Q60
    {
        "question_number": 60,
        "difficulty": "easy",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 25, 40, 70, 115, 175, ? [GD Con - 21 Feb 2024 - Shift 2]",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 25, 40, 70, 115, 175, ?",
        "option_a": "200",
        "option_b": "275",
        "option_c": "250",
        "option_d": "225",
        "correct_answer": "C",
    },
    # Q61
    {
        "question_number": 61,
        "difficulty": "medium",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 7, 16, 43, 124, 367, ? [GD Con - 21 Feb 2024 - Shift 2]",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 7, 16, 43, 124, 367, ?",
        "option_a": "1086",
        "option_b": "1096",
        "option_c": "1066",
        "option_d": "1076",
        "correct_answer": "B",
    },
    # Q62
    {
        "question_number": 62,
        "difficulty": "medium",
        "question_en": "Which of the following letter clusters will replace the blank in the given series? FDKI, GCMG, ?, IAQC [GD Con - 27 Jun 2024 - Shift 1]",
        "question_hi": "निम्नलिखित में से कौन सा अक्षर समूह दी गई श्रृंखला में रिक्त स्थान को प्रतिस्थापित करेगा? FDKI, GCMG, ?, IAQC",
        "option_a": "HBNF",
        "option_b": "HBOE",
        "option_c": "HBPF",
        "option_d": "HBLE",
        "correct_answer": "B",
    },
    # Q63
    {
        "question_number": 63,
        "difficulty": "medium",
        "question_en": "In the following question, select the missing number from the given series. 14, 6, 5, 6, 12, ? [GD Con - 27 Jun 2024 - Shift 3]",
        "question_hi": "निम्नलिखित प्रश्न में, दी गई श्रृंखला से लुप्त संख्या का चयन कीजिए। 14, 6, 5, 6, 12, ?",
        "option_a": "20",
        "option_b": "17",
        "option_c": "29",
        "option_d": "25",
        "correct_answer": "C",
    },
    # Q64
    {
        "question_number": 64,
        "difficulty": "easy",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 55, 165, 495, 1485, ?, 13365 [GD Con - 27 Jun 2024 - Shift 1]",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 55, 165, 495, 1485, ?, 13365",
        "option_a": "4455",
        "option_b": "5055",
        "option_c": "6000",
        "option_d": "7055",
        "correct_answer": "A",
    },
    # Q65
    {
        "question_number": 65,
        "difficulty": "hard",
        "question_en": "Which of the following groups of letters when sequentially placed from left to right will complete the given series? opq_stopqrsto_qrs_opqr_t [GD Con - 20 Feb 2024 - Shift 3]",
        "question_hi": "निम्नलिखित में से अक्षरों का कौन सा समूह बाएं से दाएं क्रमवार रखने पर दी गई श्रृंखला को पूरा करेगा? opq_stopqrsto_qrs_opqr_t",
        "option_a": "rpts",
        "option_b": "rptp",
        "option_c": "opqr",
        "option_d": "pqr",
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
        print(f"\nDone -- inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
