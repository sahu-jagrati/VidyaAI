"""
seed_reasoning_series_sheet2.py
=================================
Seeds questions 12–21 (Series) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Series
Run     : python seed_reasoning_series_sheet2.py

Answer key verification:
  Q12: 3,10,24,?,73,108,150,199 — diffs 7,14,21,28,35,42,49 → 24+21=45          → C
  Q13: ECF,JHK,OMP,TRU,? — each letter +5 each term → YWZ                        → C
  Q14: wwxxyyzz repeating; blanks fill → zxyw                                     → C
  Q15: HMP,JOR,LQT,NSV,? — 1st+2,2nd+2,3rd+2 → PUX                              → C
  Q16: 1095,1072,1049,1026,1003,? — each -23 → 980                               → B
  Q17: 68,69,77,74,168,? — per image answer key → 308                             → D
  Q18: 3,14,?,16,-18,-3 — per image answer key → 0                                → D
  Q19: SNTO,UNVO,WNXO,____,ANBO — 1st+2,3rd+2 each term → YNZO                  → C
  Q20: ?,N,K,H,E,B — each -3 backward: Q,N,K,H,E,B → Q                           → B
  Q21: 6,12,24,48,?,192 — ×2 each → 96                                            → D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Reasoning_Series_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Series"

QUESTIONS = [
    # Q12
    {
        "question_number": 12,
        "difficulty": "medium",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 3, 10, 24, ?, 73, 108, 150, 199",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 3, 10, 24, ?, 73, 108, 150, 199",
        "option_a": "35",
        "option_b": "40",
        "option_c": "45",
        "option_d": "50",
        "correct_answer": "C",
        "source_pdf": SOURCE,
    },
    # Q13
    {
        "question_number": 13,
        "difficulty": "easy",
        "question_en": "A series is given with one term missing. Select the correct alternative. ECF, JHK, OMP, TRU, ?",
        "question_hi": "एक श्रृंखला दी गई है, जिसमें एक पद लुप्त है। सही विकल्प चुनिए। ECF, JHK, OMP, TRU, ?",
        "option_a": "XYZ",
        "option_b": "YVZ",
        "option_c": "YWZ",
        "option_d": "YWY",
        "correct_answer": "C",
        "source_pdf": SOURCE,
    },
    # Q14
    {
        "question_number": 14,
        "difficulty": "hard",
        "question_en": "Select the combination of letters that when sequentially placed in the blanks will complete the series. wwxxyyzz_wwx_yyzz_wx_yyzz_wxx_yyzz",
        "question_hi": "अक्षरों के उस संयोजन का चयन कीजिए जो दी गई श्रृंखला की रिक्त स्थानों में क्रमिक रूप से रखे जाने पर श्रृंखला को पूरा करेगा। wwxxyyzz_wwx_yyzz_wx_yyzz_wxx_yyzz",
        "option_a": "xxwz",
        "option_b": "yywz",
        "option_c": "zxyw",
        "option_d": "wxyx",
        "correct_answer": "C",
        "source_pdf": SOURCE,
    },
    # Q15
    {
        "question_number": 15,
        "difficulty": "easy",
        "question_en": "A series is given with one term missing. Select the correct alternative. HMP, JOR, LQT, NSV, ?",
        "question_hi": "एक श्रृंखला दी गई है, जिसमें एक पद लुप्त है। सही विकल्प चुनिए। HMP, JOR, LQT, NSV, ?",
        "option_a": "PWY",
        "option_b": "PXV",
        "option_c": "PUX",
        "option_d": "WPX",
        "correct_answer": "C",
        "source_pdf": SOURCE,
    },
    # Q16
    {
        "question_number": 16,
        "difficulty": "easy",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 1095, 1072, 1049, 1026, 1003, ?",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 1095, 1072, 1049, 1026, 1003, ?",
        "option_a": "975",
        "option_b": "980",
        "option_c": "985",
        "option_d": "990",
        "correct_answer": "B",
        "source_pdf": SOURCE,
    },
    # Q17
    {
        "question_number": 17,
        "difficulty": "hard",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 68, 69, 77, 74, 168, ?",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 68, 69, 77, 74, 168, ?",
        "option_a": "250",
        "option_b": "272",
        "option_c": "296",
        "option_d": "308",
        "correct_answer": "D",
        "source_pdf": SOURCE,
    },
    # Q18
    {
        "question_number": 18,
        "difficulty": "hard",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 3, 14, ?, 16, -18, -3",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 3, 14, ?, 16, -18, -3",
        "option_a": "1",
        "option_b": "2",
        "option_c": "3",
        "option_d": "0",
        "correct_answer": "D",
        "source_pdf": SOURCE,
    },
    # Q19
    {
        "question_number": 19,
        "difficulty": "medium",
        "question_en": "A series is given with one term missing. Select the correct alternative. SNTO, UNVO, WNXO, ____, ANBO",
        "question_hi": "एक श्रृंखला दी गई है, जिसमें एक पद लुप्त है। सही विकल्प चुनिए। SNTO, UNVO, WNXO, ____, ANBO",
        "option_a": "YMZO",
        "option_b": "YNZP",
        "option_c": "YNZO",
        "option_d": "YNZQ",
        "correct_answer": "C",
        "source_pdf": SOURCE,
    },
    # Q20
    {
        "question_number": 20,
        "difficulty": "easy",
        "question_en": "A series is given with one term missing. Select the correct alternative. ?, N, K, H, E, B",
        "question_hi": "एक श्रृंखला दी गई है, जिसमें एक पद लुप्त है। सही विकल्प चुनिए। ?, N, K, H, E, B",
        "option_a": "P",
        "option_b": "Q",
        "option_c": "R",
        "option_d": "S",
        "correct_answer": "B",
        "source_pdf": SOURCE,
    },
    # Q21
    {
        "question_number": 21,
        "difficulty": "easy",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 6, 12, 24, 48, ?, 192",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 6, 12, 24, 48, ?, 192",
        "option_a": "72",
        "option_b": "84",
        "option_c": "90",
        "option_d": "96",
        "correct_answer": "D",
        "source_pdf": SOURCE,
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
            fp = d.pop("source_pdf")
            if d["question_en"][:80] in existing_short:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                d["source_pdf"] = fp
                continue

            db.add(Question(
                subject    = SUBJECT,
                topic      = TOPIC,
                source_pdf = fp,
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
