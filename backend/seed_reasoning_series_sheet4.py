"""
seed_reasoning_series_sheet4.py
=================================
Seeds questions 33–43 (Series) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Series
Run     : python seed_reasoning_series_sheet4.py

Answer key verification:
  Q33: PRQ,QSR,?,SUT,TVU — each letter +1 per term → RTS                         → C
  Q34: defgh_defghidefg_hidefghidefghi_hidefgh_de_ghi — defghi repeat → ihgf      → A
  Q35: LMRC,PQVG,TUZK,XYDO,? — each letter +4 → BCHS                             → A
  Q36: 74,61,82,53,90,? — odd+8; even−8 → 45                                     → B
  Q37: 8,16,7,14,5,10,1,2,? — pattern alternates −9 with decreasing adds → −7    → D
  Q38: ghijkg_ijk_hijkg_ijkghijkg_ijk — ghijk repeat; blanks h,g,h,g → hghg      → A
  Q39: 2673,891,297,99,?,11 — ÷3 → 33                                             → B
  Q40: 0,1,5,14,30,? — diffs 1²,2²,3²,4²,5² → 55                                → C
  Q41: TJM10,ULP12,VNS14,WPV16,XRY18,? — 1st+1,2nd+2,3rd+3,num+2 → YTB20       → D
  Q42: 12,60,20,100,60,300,260,? — 2-col grid diffs ×5 → 1300                    → C
  Q43: CHO,DIP,EJQ,? — each letter +1 → FKR                                      → B
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Reasoning_Series_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Series"

QUESTIONS = [
    # Q33
    {
        "question_number": 33,
        "difficulty": "easy",
        "question_en": "Which of the following letter cluster will replace the blank in the given series? PRQ, QSR, _____, SUT, TVU [GD Con - 20 Feb 2024 - Shift 4]",
        "question_hi": "निम्नलिखित में से कौन सा अक्षर समूह दी गई श्रृंखला में रिक्त स्थान को प्रतिस्थापित करेगा? PRQ, QSR, _____, SUT, TVU",
        "option_a": "RST",
        "option_b": "RUS",
        "option_c": "RTS",
        "option_d": "QTS",
        "correct_answer": "C",
    },
    # Q34
    {
        "question_number": 34,
        "difficulty": "hard",
        "question_en": "Which of the following groups of letters when sequentially placed from left to right will complete the given series? defgh_defghidefg_hidefghidefghi_hidefgh_de_ghi [GD Con - 21 Feb 2024 - Shift 1]",
        "question_hi": "निम्नलिखित में से अक्षरों का कौन सा समूह बाएं से दाएं क्रमवार रखने पर दी गई श्रृंखला को पूरा करेगा? defgh_defghidefg_hidefghidefghi_hidefgh_de_ghi",
        "option_a": "ihgf",
        "option_b": "ehgf",
        "option_c": "ihhf",
        "option_d": "defg",
        "correct_answer": "A",
    },
    # Q35
    {
        "question_number": 35,
        "difficulty": "medium",
        "question_en": "A series is given with one term missing. Select the correct alternative from the given ones that will complete the series. LMRC, PQVG, TUZK, XYDO, ? [GD Con - 21 Feb 2024 - Shift 1]",
        "question_hi": "एक श्रृंखला दी गई है जिसमें एक पद लुप्त है। दिए गए विकल्पों में से वह सही विकल्प चुनिए जो श्रृंखला को पूरा करेगा। LMRC, PQVG, TUZK, XYDO, ?",
        "option_a": "BCHS",
        "option_b": "BMRN",
        "option_c": "BTSQ",
        "option_d": "RBMN",
        "correct_answer": "A",
    },
    # Q36
    {
        "question_number": 36,
        "difficulty": "easy",
        "question_en": "In the following question, select the missing number from the given series. 74, 61, 82, 53, 90, ? [GD Con - 21 Feb 2024 - Shift 1]",
        "question_hi": "निम्नलिखित प्रश्न में, दी गई श्रृंखला से लुप्त संख्या का चयन कीजिए। 74, 61, 82, 53, 90, ?",
        "option_a": "44",
        "option_b": "45",
        "option_c": "43",
        "option_d": "40",
        "correct_answer": "B",
    },
    # Q37
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 8, 16, 7, 14, 5, 10, 1, 2, ? [GD Con - 21 Feb 2024 - Shift 1]",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 8, 16, 7, 14, 5, 10, 1, 2, ?",
        "option_a": "7",
        "option_b": "9",
        "option_c": "4",
        "option_d": "-7",
        "correct_answer": "D",
    },
    # Q38
    {
        "question_number": 38,
        "difficulty": "hard",
        "question_en": "Which of the following groups of letters when sequentially placed from left to right will complete the given series? ghijkg_ijk_hijkg_ijkghijkg_ijk [GD Con - 21 Feb 2024 - Shift 2]",
        "question_hi": "निम्नलिखित में से अक्षरों का कौन सा समूह बाएं से दाएं क्रमवार रखने पर दी गई श्रृंखला को पूरा करेगा? ghijkg_ijk_hijkg_ijkghijkg_ijk",
        "option_a": "hghg",
        "option_b": "khih",
        "option_c": "ijkg",
        "option_d": "hhgk",
        "correct_answer": "A",
    },
    # Q39
    {
        "question_number": 39,
        "difficulty": "easy",
        "question_en": "In the following question, select the missing number from the given series. 2673, 891, 297, 99, ?, 11 [GD Con - 21 Feb 2024 - Shift 2]",
        "question_hi": "निम्नलिखित प्रश्न में, दी गई श्रृंखला से लुप्त संख्या का चयन कीजिए। 2673, 891, 297, 99, ?, 11",
        "option_a": "43",
        "option_b": "33",
        "option_c": "23",
        "option_d": "10",
        "correct_answer": "B",
    },
    # Q40
    {
        "question_number": 40,
        "difficulty": "medium",
        "question_en": "In the following question, select the missing number from the given series. 0, 1, 5, 14, 30, ? [GD Con - 21 Feb 2024 - Shift 2]",
        "question_hi": "निम्नलिखित प्रश्न में, दी गई श्रृंखला से लुप्त संख्या का चयन कीजिए। 0, 1, 5, 14, 30, ?",
        "option_a": "66",
        "option_b": "69",
        "option_c": "55",
        "option_d": "57",
        "correct_answer": "C",
    },
    # Q41
    {
        "question_number": 41,
        "difficulty": "medium",
        "question_en": "Which of the following letter-number cluster will replace the question mark (?) in the given series? TJM10, ULP12, VNS14, WPV16, XRY18, ? [GD Con - 21 Feb 2024 - Shift 1]",
        "question_hi": "निम्नलिखित में से कौन सा अक्षर-संख्या समूह दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगा? TJM10, ULP12, VNS14, WPV16, XRY18, ?",
        "option_a": "YSZ20",
        "option_b": "YSZ21",
        "option_c": "YTB21",
        "option_d": "YTB20",
        "correct_answer": "D",
    },
    # Q42
    {
        "question_number": 42,
        "difficulty": "hard",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 12, 60, 20, 100, 60, 300, 260, ? [CHSL - 2 July 2024 - Shift 4]",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 12, 60, 20, 100, 60, 300, 260, ?",
        "option_a": "1160",
        "option_b": "1240",
        "option_c": "1300",
        "option_d": "1280",
        "correct_answer": "C",
    },
    # Q43
    {
        "question_number": 43,
        "difficulty": "easy",
        "question_en": "Which of the following terms will replace the question mark (?) in the given series? CHO, DIP, EJQ, ? [CPO - 27 Jun 2024 - Shift 1]",
        "question_hi": "निम्नलिखित में से कौन सा पद दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगा? CHO, DIP, EJQ, ?",
        "option_a": "EJL",
        "option_b": "FKR",
        "option_c": "DIL",
        "option_d": "HMR",
        "correct_answer": "B",
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
