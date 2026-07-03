"""
seed_reasoning_series_sheet5.py
=================================
Seeds questions 44–53 (Series) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Series
Run     : python seed_reasoning_series_sheet5.py

Answer key verification:
  Q44: TDQR,SFNV,?,QJHD,PLEH — col1:-1,col2:+2,col3:-3,col4:+4 → RHKZ          → A
  Q45: 324,722,1200,?,2420 — pattern n×(n+17)² → 4×21²=1764                      → A
  Q46: 29,30,26,35,19,? — diffs +1²,-2²,+3²,-4²,+5²=25 → 44                    → C
  Q47: 12,13,30,99,412,? — n×(n-1)+n²: 412×5+25=2085                             → C
  Q48: 115,140,160,175,185,? — diffs 25,20,15,10,5 → 190                          → D
  Q49: FPW,FPPPWWW,FFFFFPPPPPWWWWW,? — each F/P/W +2 (odd series) → option B    → B
  Q50: AFM,DIP,GLS,? — each letter +3 → JOV                                       → C
  Q51: G,Z,I,X,K,V,?,? — odd+2→M; even-2→T → M,T                                → B
  Q52: 2,?,?,17,26,37,50,65,82 — diffs 3,5,7,9... → blanks 5 and 10             → B
  Q53: 1,2,4,8,10,20,? — ×2 then +2 alternating after 8 → 22                    → C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Reasoning_Series_Sheet5"
SUBJECT = "Reasoning"
TOPIC   = "Series"

QUESTIONS = [
    # Q44
    {
        "question_number": 44,
        "difficulty": "medium",
        "question_en": "Which of the following letter cluster will replace the blank in the given series? TDQR, SFNV, ?, QJHD, PLEH [CPO - 27 Jun 2024 - Shift 3]",
        "question_hi": "निम्नलिखित में से कौन सा अक्षर समूह दी गई श्रृंखला में रिक्त स्थान को प्रतिस्थापित करेगा? TDQR, SFNV, ?, QJHD, PLEH",
        "option_a": "RHKZ",
        "option_b": "RGJZ",
        "option_c": "FJCQ",
        "option_d": "IDBZ",
        "correct_answer": "A",
    },
    # Q45
    {
        "question_number": 45,
        "difficulty": "hard",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 324, 722, 1200, ?, 2420 [CPO - 27 Jun 2024 - Shift 3]",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 324, 722, 1200, ?, 2420",
        "option_a": "1764",
        "option_b": "1632",
        "option_c": "1634",
        "option_d": "1736",
        "correct_answer": "A",
    },
    # Q46
    {
        "question_number": 46,
        "difficulty": "medium",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 29, 30, 26, 35, 19, ? [CPO - 27 Jun 2024 - Shift 3]",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 29, 30, 26, 35, 19, ?",
        "option_a": "41",
        "option_b": "42",
        "option_c": "44",
        "option_d": "43",
        "correct_answer": "C",
    },
    # Q47
    {
        "question_number": 47,
        "difficulty": "hard",
        "question_en": "Which of the following numbers will replace the question mark (?) in the given series? 12, 13, 30, 99, 412, ? [CPO - 27 Jun 2024 - Shift 3]",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 12, 13, 30, 99, 412, ?",
        "option_a": "2065",
        "option_b": "2075",
        "option_c": "2085",
        "option_d": "2055",
        "correct_answer": "C",
    },
    # Q48
    {
        "question_number": 48,
        "difficulty": "easy",
        "question_en": "Select the number from among the given options that can replace the question mark (?) in the following series. 115, 140, 160, 175, 185, ? [CPO - 27 Jun 2024 - Shift 3]",
        "question_hi": "दिए गए विकल्पों में से वह संख्या चुनिए जो निम्नलिखित श्रृंखला में प्रश्वाचक चिह्न (?) को प्रतिस्थापित कर सकती है। 115, 140, 160, 175, 185, ?",
        "option_a": "193",
        "option_b": "195",
        "option_c": "192",
        "option_d": "190",
        "correct_answer": "D",
    },
    # Q49
    {
        "question_number": 49,
        "difficulty": "hard",
        "question_en": "Which letter-cluster will complete the given series? FPW, FPPPWWW, FFFFFPPPPPWWWWW, ______ [CPO - 27 Jun 2024 - Shift 3]",
        "question_hi": "कौन-सा अक्षर-समूह दी गई श्रृंखला को पूरा करेगा? FPW, FPPPWWW, FFFFFPPPPPWWWWW, ______",
        "option_a": "FFFFFFFFFPPPPPWWWWWWWWWWWWWWW",
        "option_b": "FFFFFFFPPPPPPPWWWWWWW",
        "option_c": "FFFFFFFFFFFFFFFPPPPPPPWWWWWWWWWWWWWWWWWWWWW",
        "option_d": "FFFFFFFFFFFFFPPPPPWWWWWWWWWWWWW",
        "correct_answer": "B",
    },
    # Q50
    {
        "question_number": 50,
        "difficulty": "easy",
        "question_en": "Which of the following terms will replace the question mark (?) in the given series? AFM, DIP, GLS, ? [CPO - 27 Jun 2024 - Shift 2]",
        "question_hi": "निम्नलिखित में से कौन सा पद दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगा? AFM, DIP, GLS, ?",
        "option_a": "OST",
        "option_b": "REW",
        "option_c": "JOV",
        "option_d": "FHG",
        "correct_answer": "C",
    },
    # Q51
    {
        "question_number": 51,
        "difficulty": "medium",
        "question_en": "Which of the following letters will sequentially replace the question marks (?) in the given series? G, Z, I, X, K, V, ?, ? [CPO - 27 Jun 2024 - Shift 2]",
        "question_hi": "निम्नलिखित में से कौन सा अक्षर दी गई श्रृंखला में क्रमिक रूप से प्रश्न चिह्न (?) को प्रतिस्थापित करेगा? G, Z, I, X, K, V, ?, ?",
        "option_a": "Q, R",
        "option_b": "M, T",
        "option_c": "L, N",
        "option_d": "A, M, S",
        "correct_answer": "B",
    },
    # Q52
    {
        "question_number": 52,
        "difficulty": "medium",
        "question_en": "Which of the following will replace the question marks (?) in the given series? 2, ?, ?, 17, 26, 37, 50, 65, 82 [CPO - 27 Jun 2024 - Shift 2]",
        "question_hi": "निम्नलिखित में से कौन सी संख्या दी गई श्रृंखला में प्रश्न चिह्न (?) को प्रतिस्थापित करेगी? 2, ?, ?, 17, 26, 37, 50, 65, 82",
        "option_a": "3, 4",
        "option_b": "5, 10",
        "option_c": "2, 5",
        "option_d": "3, 5",
        "correct_answer": "B",
    },
    # Q53
    {
        "question_number": 53,
        "difficulty": "medium",
        "question_en": "Select the number from among the given options that can replace the question mark (?) in the following series. 1, 2, 4, 8, 10, 20, ? [CPO - 27 Jun 2024 - Shift 2]",
        "question_hi": "दिए गए विकल्पों में से वह संख्या चुनिए जो निम्नलिखित श्रृंखला में प्रश्वाचक चिह्न (?) को प्रतिस्थापित कर सकती है। 1, 2, 4, 8, 10, 20, ?",
        "option_a": "40",
        "option_b": "24",
        "option_c": "22",
        "option_d": "42",
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
        print(f"\nDone -- inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
