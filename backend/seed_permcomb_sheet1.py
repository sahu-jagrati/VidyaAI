"""
seed_permcomb_sheet1.py
========================
Seeds questions 11–15 (Permutation & Combination) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Permutation & Combination
Run     : python seed_permcomb_sheet1.py

Answer key verification:
  Q11: 9×9×8×7=4536 (first digit 9 options, then 9,8,7 for remaining)         → A
  Q12: first digit 4 options (2,4,6,8), others 5 each; 4×5×5=100              → B
  Q13: first=3,last=5; middle 3 from {4,6,7,8}: P(4,3)=24                     → D
  Q14: valid endings={12,24,32,44,52}=5; first 3 digits: 5³=125; total=625    → A
  Q15: valid endings from {1-6}=8 pairs; P(4,3)=24 each; 8×24=192             → D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_PermComb_Sheet1"
SUBJECT = "Quant"
TOPIC   = "Permutation & Combination"

QUESTIONS = [
    # Q11
    {
        "question_number": 11,
        "difficulty": "easy",
        "question_en": "How many 4-digit numbers are there with no digit repeated?",
        "question_hi": "4 अंकों की कितनी संख्याएँ हैं जिनमें कोई अंक दोहराया नहीं गया है?",
        "option_a": "4536",
        "option_b": "1728",
        "option_c": "9000",
        "option_d": "8999",
        "correct_answer": "A",
    },
    # Q12
    {
        "question_number": 12,
        "difficulty": "easy",
        "question_en": "How many 3-digit numbers are possible where all the 3 digits are even?",
        "question_hi": "3 अंकों की कितनी संख्याएँ संभव हैं जहाँ सभी 3 अंक सम हों?",
        "option_a": "175",
        "option_b": "100",
        "option_c": "500",
        "option_d": "96",
        "correct_answer": "B",
    },
    # Q13
    {
        "question_number": 13,
        "difficulty": "medium",
        "question_en": "How many numbers can be made with the digits 3, 4, 5, 6, 7, 8 lying between 3000 and 4000 which are divisible by 5 while repetition of any digit is not allowed in any number?",
        "question_hi": "3000 और 4000 के बीच पड़ने वाले अंक 3, 4, 5, 6, 7, 8 से कितनी संख्याएँ बनाई जा सकती हैं जो 5 से विभाज्य हों जबकि किसी भी संख्या में किसी भी अंक की पुनरावृत्ति की अनुमति नहीं है?",
        "option_a": "60",
        "option_b": "8",
        "option_c": "120",
        "option_d": "24",
        "correct_answer": "D",
    },
    # Q14
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": "The number of 5-digit numbers which are divisible by 4, with digits from the set {1,2,3,4,5} and the repetition of digits is allowed, is ___?",
        "question_hi": "1, 2, 3, 4, 5 से, यदि दोहराव की अनुमति है तो 4 से विभाज्य कितनी पाँच अंकों की संख्याएँ बनती हैं?",
        "option_a": "625",
        "option_b": "600",
        "option_c": "525",
        "option_d": "500",
        "correct_answer": "A",
    },
    # Q15
    {
        "question_number": 15,
        "difficulty": "hard",
        "question_en": "N is the total number of 5-digit numbers which are divisible by 4 and the numbers are formed using the digits 1, 2, 3, 4, 5 and 6. No digit is repeated in the number. What is the value of N?",
        "question_hi": "N, 5 अंकों की कुल संख्या है जो 4 से विभाज्य है और संख्याएँ 1, 2, 3, 4, 5 और 6 अंकों का उपयोग करके बनाई गई हैं। संख्या में कोई अंक दोहराया नहीं जाता है। N का मान क्या है?",
        "option_a": "144",
        "option_b": "162",
        "option_c": "Not possible",
        "option_d": "192",
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
