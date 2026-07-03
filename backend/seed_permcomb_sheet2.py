"""
seed_permcomb_sheet2.py
========================
Seeds questions 16–21 (Permutation & Combination) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Permutation & Combination
Run     : python seed_permcomb_sheet2.py

Answer key verification:
  Q16: 1st digit {1,2,3,4}=4 choices; remaining P(6,3)=120; total=4×120=480    → B
  Q17: odd(<2000), digits {0,1,3,4,7,8}, repeat allowed:
       1-dig=3, 2-dig=5×3=15, 3-dig=5×6×3=90, 4-dig(first=1)=1×6×6×3=108; total=216 → D
  Q18: format 4_5___; 4 free digits each 0-9, sum≡0(mod9);
       roots-of-unity filter: (10^4+8)/9=1112                                   → B
  Q19: MANISH = 6 distinct → 6!=720                                             → A
  Q20: RUMOUR = R×2,U×2,M,O → 6!/(2!×2!)=180                                  → A
  Q21: ALLAHABAD = A×4,L×2,H,B,D → 9!/(4!×2!)=7560                            → C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_PermComb_Sheet2"
SUBJECT = "Quant"
TOPIC   = "Permutation & Combination"

QUESTIONS = [
    # Q16
    {
        "question_number": 16,
        "difficulty": "medium",
        "question_en": "How many numbers between 1000 and 5000 can be formed with the digits 0, 1, 2, 3, 4, 5, 6 if repetition is not allowed?",
        "question_hi": "0, 1, 2, 3, 4, 5, 6 अंकों से 1000 और 5000 के बीच कितनी संख्याएँ बनाई जा सकती हैं यदि पुनरावृत्ति की अनुमति नहीं है?",
        "option_a": "240",
        "option_b": "480",
        "option_c": "120",
        "option_d": "500",
        "correct_answer": "B",
    },
    # Q17
    {
        "question_number": 17,
        "difficulty": "hard",
        "question_en": "How many odd numbers less than 2000 can be formed using the digits 0, 1, 3, 4, 8, 7 if repetition of digits is allowed?",
        "question_hi": "अंक 0, 1, 3, 4, 8, 7 का उपयोग करके 2000 से कम कितनी विषम संख्याएँ बनाई जा सकती हैं यदि अंकों की पुनरावृत्ति की अनुमति है?",
        "option_a": "317",
        "option_b": "126",
        "option_c": "108",
        "option_d": "216",
        "correct_answer": "D",
    },
    # Q18
    {
        "question_number": 18,
        "difficulty": "hard",
        "question_en": "How many 6-digit numbers can be formed which are divisible by 9 and have '4' as its first digit and '5' as the 3rd digit?",
        "question_hi": "6 अंकों की ऐसी कितनी संख्याएँ बनाई जा सकती हैं जो 9 से विभाज्य हों और जिनका पहला अंक '4' और तीसरा अंक '5' हो?",
        "option_a": "1111",
        "option_b": "1112",
        "option_c": "1110",
        "option_d": "3334",
        "correct_answer": "B",
    },
    # Q19
    {
        "question_number": 19,
        "difficulty": "easy",
        "question_en": "How many words can be framed by the letters of the word MANISH?",
        "question_hi": "MANISH शब्द के अक्षर से कितने शब्द बनाये जा सकते हैं?",
        "option_a": "720",
        "option_b": "480",
        "option_c": "360",
        "option_d": "240",
        "correct_answer": "A",
    },
    # Q20
    {
        "question_number": 20,
        "difficulty": "easy",
        "question_en": "In how many ways can the letters of the word RUMOUR be arranged?",
        "question_hi": "RUMOUR शब्द के अक्षरों को कितने तरीकों से व्यवस्थित किया जा सकता है?",
        "option_a": "180",
        "option_b": "720",
        "option_c": "360",
        "option_d": "90",
        "correct_answer": "A",
    },
    # Q21
    {
        "question_number": 21,
        "difficulty": "medium",
        "question_en": "Find the number of permutations of the letters of the word ALLAHABAD?",
        "question_hi": "ALLAHABAD शब्द के अक्षरों के क्रमचयों की संख्या ज्ञात कीजिए?",
        "option_a": "9!",
        "option_b": "5880",
        "option_c": "7560",
        "option_d": "6!",
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
