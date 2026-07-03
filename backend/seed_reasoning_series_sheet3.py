"""
seed_reasoning_series_sheet3.py
=================================
Seeds questions 22–32 (Series) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Series
Run     : python seed_reasoning_series_sheet3.py

Answer key verification:
  Q22: NRHD→RVLH→VZPL→ZDTP; each letter +4 → DHXT                               → A
  Q23: 14,13,15,12,16,11,? — odd+1/even-1 → 17                                   → B
  Q24: 126,147,?,189,210,231 — diff=+21 → 168                                     → C
  Q25: r_tuvrstuv_tuvrstuv_r — repeating rstuv → suvt                             → B
  Q26: NRT,OSU,PTV,QUW,? — each letter +1 → RVX                                   → B
  Q27: xx_yyyzzzzxxxyyy_zzzzzxx_yyyyzzzz — groups increment; blanks x,y,x,z       → A
  Q28: 5,48,7,44,13,? — diff 43,37,31 (−6); 13+31=44                             → C
  Q29: 750,715,680,645,610,? — each −35 → 575                                     → D
  Q30: 86,107,82,111,78,115,? — odd−4; 78−4=74                                    → A
  Q31: MQ,SO,QU,WS,? — 1st+6/−2 alt→U; 2nd−2/+6 alt→Y → UY                     → C
  Q32: 6075,2025,?,225,75 — ÷3 → 675                                              → A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Reasoning_Series_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Series"

QUESTIONS = [
    # Q22
    {
        "question_number": 22,
        "difficulty": "medium",
        "question_en": "A series is given with one term missing. Select the correct alternative from the given ones that will complete the series. NRHD, RVLH, VZPL, ZDTP, ? [GD Con - 29 Feb 2024 - Shift 2]",
        "question_hi": "एक श्रृंखला दी गई है जिसमें एक पद लुप्त है। दिए गए विकल्पों में से वह सही विकल्प चुनिए जो श्रृंखला को पूरा करेगा। NRHD, RVLH, VZPL, ZDTP, ?",
        "option_a": "DHXT",
        "option_b": "DTCM",
        "option_c": "DQPT",
        "option_d": "DTNR",
        "correct_answer": "A",
    },
    # Q23
    {
        "question_number": 23,
        "difficulty": "easy",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 14, 13, 15, 12, 16, 11, ? [GD Con - 29 Feb 2024 - Shift 2]",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 14, 13, 15, 12, 16, 11, ?",
        "option_a": "15",
        "option_b": "17",
        "option_c": "18",
        "option_d": "16",
        "correct_answer": "B",
    },
    # Q24
    {
        "question_number": 24,
        "difficulty": "easy",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 126, 147, ?, 189, 210, 231 [GD Con - 29 Feb 2024 - Shift 2]",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 126, 147, ?, 189, 210, 231",
        "option_a": "176",
        "option_b": "152",
        "option_c": "168",
        "option_d": "160",
        "correct_answer": "C",
    },
    # Q25
    {
        "question_number": 25,
        "difficulty": "hard",
        "question_en": "Which of the following groups of letters when sequentially placed from left to right will complete the given series? r_tuvrstuv_tuvrstuv_r [GD Con - 29 Feb 2024 - Shift 2]",
        "question_hi": "निम्नलिखित में से अक्षरों का कौन सा समूह बाएं से दाएं क्रमवार रखने पर दी गई श्रृंखला को पूरा करेगा? r_tuvrstuv_tuvrstuv_r",
        "option_a": "tust",
        "option_b": "suvt",
        "option_c": "sssu",
        "option_d": "utvu",
        "correct_answer": "B",
    },
    # Q26
    {
        "question_number": 26,
        "difficulty": "easy",
        "question_en": "A series is given with one term missing. Select the correct alternative from the given ones that will complete the series. NRT, OSU, PTV, QUW, ? [GD Con - 29 Feb 2024 - Shift 3]",
        "question_hi": "एक श्रृंखला दी गई है जिसमें एक पद लुप्त है। दिए गए विकल्पों में से वह सही विकल्प चुनिए जो श्रृंखला को पूरा करेगा। NRT, OSU, PTV, QUW, ?",
        "option_a": "PQR",
        "option_b": "RVX",
        "option_c": "MHD",
        "option_d": "RXM",
        "correct_answer": "B",
    },
    # Q27
    {
        "question_number": 27,
        "difficulty": "hard",
        "question_en": "Which of the following groups of letters when sequentially placed from left to right will complete the given series? xx_yyyzzzzxxxyyy_zzzzzxx_yyyyzzzz [GD Con - 29 Feb 2024 - Shift 3]",
        "question_hi": "निम्नलिखित में से अक्षरों का कौन सा समूह बाएं से दाएं क्रमवार रखने पर दी गई श्रृंखला को पूरा करेगा? xx_yyyzzzzxxxyyy_zzzzzxx_yyyyzzzz",
        "option_a": "xyxz",
        "option_b": "yzzy",
        "option_c": "xxyy",
        "option_d": "xyzy",
        "correct_answer": "A",
    },
    # Q28
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": "In the following question, select the missing number from the given series. 5, 48, 7, 44, 13, ? [GD Con - 29 Feb 2024 - Shift 3]",
        "question_hi": "निम्नलिखित प्रश्न में, दी गई श्रृंखला से लुप्त संख्या का चयन कीजिए। 5, 48, 7, 44, 13, ?",
        "option_a": "36",
        "option_b": "48",
        "option_c": "44",
        "option_d": "41",
        "correct_answer": "C",
    },
    # Q29
    {
        "question_number": 29,
        "difficulty": "easy",
        "question_en": "In the following question, select the missing number from the given series. 750, 715, 680, 645, 610, ? [GD Con - 29 Feb 2024 - Shift 3]",
        "question_hi": "निम्नलिखित प्रश्न में, दी गई श्रृंखला से लुप्त संख्या का चयन कीजिए। 750, 715, 680, 645, 610, ?",
        "option_a": "574",
        "option_b": "570",
        "option_c": "573",
        "option_d": "575",
        "correct_answer": "D",
    },
    # Q30
    {
        "question_number": 30,
        "difficulty": "medium",
        "question_en": "In the following question, select the missing number from the given series. 86, 107, 82, 111, 78, 115, ? [GD Con - 20 Feb 2024 - Shift 4]",
        "question_hi": "निम्नलिखित प्रश्न में, दी गई श्रृंखला से लुप्त संख्या का चयन कीजिए। 86, 107, 82, 111, 78, 115, ?",
        "option_a": "74",
        "option_b": "72",
        "option_c": "71",
        "option_d": "78",
        "correct_answer": "A",
    },
    # Q31
    {
        "question_number": 31,
        "difficulty": "medium",
        "question_en": "A series is given with one term missing. Select the correct alternative from the given ones that will complete the series. MQ, SO, QU, WS, ? [GD Con - 20 Feb 2024 - Shift 4]",
        "question_hi": "एक श्रृंखला दी गई है जिसमें एक पद लुप्त है। दिए गए विकल्पों में से वह सही विकल्प चुनिए जो श्रृंखला को पूरा करेगा। MQ, SO, QU, WS, ?",
        "option_a": "XT",
        "option_b": "UX",
        "option_c": "UY",
        "option_d": "MH",
        "correct_answer": "C",
    },
    # Q32
    {
        "question_number": 32,
        "difficulty": "easy",
        "question_en": "In the following question, select the missing number from the given series. 6075, 2025, ?, 225, 75 [GD Con - 20 Feb 2024 - Shift 4]",
        "question_hi": "निम्नलिखित प्रश्न में, दी गई श्रृंखला से लुप्त संख्या का चयन कीजिए। 6075, 2025, ?, 225, 75",
        "option_a": "675",
        "option_b": "690",
        "option_c": "700",
        "option_d": "680",
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
