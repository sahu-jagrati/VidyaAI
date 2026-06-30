import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

# Probability Sheet-1 (SSC CGL MAINS BATCH 2023) — Q1-Q6
# Q1: P(prize) = 10/35 = 2/7
# Q2: P(vowel from alphabet) = 5/26
# Q3: PROBABILITY(11 letters, vowels O,A,I,I=4) → P = 4/11
# Q4: Non-leap year = 365 = 52 weeks + 1 day; P(extra day=Sunday) = 1/7
# Q5: 1-30 divisible by 4(7) or 6(5) minus common(2) = 10 → P = 10/30 = 1/3
# Q6: Odd(6) + Even(5) from 1-11; even sum: C(6,2)+C(5,2)=25; both odd: C(6,2)=15 → 15/25=3/5

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "In a lottery, there are 10 prizes and 25 blanks. A lottery is drawn at random. What is the probability of getting a prize?",
        "option_a": "1/10",
        "option_b": "2/5",
        "option_c": "2/7",
        "option_d": "5/7",
        "correct_answer": "C",
        "explanation": "Total outcomes = 10 + 25 = 35. P(prize) = 10/35 = 2/7.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "A letter of the English alphabet is chosen at random. What is the probability of getting a vowel?",
        "option_a": "5/26",
        "option_b": "6/25",
        "option_c": "1/4",
        "option_d": "5/21",
        "correct_answer": "A",
        "explanation": "Total letters = 26. Vowels (a,e,i,o,u) = 5. P(vowel) = 5/26.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "A single letter is selected at random from the word 'PROBABILITY'. The probability that the selected letter is a vowel is?",
        "option_a": "2/11",
        "option_b": "3/11",
        "option_c": "4/11",
        "option_d": "5/11",
        "correct_answer": "C",
        "explanation": "PROBABILITY = 11 letters (P,R,O,B,A,B,I,L,I,T,Y). Vowels: O,A,I,I = 4. P(vowel) = 4/11.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "The probability that an ordinary (non-leap) year has 53 Sundays is?",
        "option_a": "2/7",
        "option_b": "1/7",
        "option_c": "3/7",
        "option_d": "None of these",
        "correct_answer": "B",
        "explanation": "A non-leap year = 365 days = 52 complete weeks + 1 extra day. The extra day can be any of 7 days. P(extra day is Sunday) = 1/7.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A bag contains balls numbered 1, 2, 3, ...... 30. One ball is drawn from the bag at random. What is the probability that the number on the ball drawn is divisible by 4 or 6?",
        "option_a": "1/5",
        "option_b": "1/3",
        "option_c": "3/10",
        "option_d": "2/5",
        "correct_answer": "B",
        "explanation": "Divisible by 4: {4,8,12,16,20,24,28} = 7. Divisible by 6: {6,12,18,24,30} = 5. Divisible by LCM(4,6)=12: {12,24} = 2. By inclusion-exclusion: 7+5−2 = 10. P = 10/30 = 1/3.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "Two integers are selected at random from the first 11 natural numbers. If the sum of the integers is even, then the probability that both the numbers are odd is?",
        "option_a": "13/121",
        "option_b": "3/5",
        "option_c": "4/9",
        "option_d": "5/11",
        "correct_answer": "B",
        "explanation": "In 1-11: 6 odd, 5 even. Even sum: both odd C(6,2)=15 or both even C(5,2)=10 → total=25 ways. P(both odd | even sum) = 15/25 = 3/5.",
    },
]


def seed():
    db = SessionLocal()
    try:
        added = 0
        for q in QUESTIONS:
            exists = db.query(Question).filter(
                Question.question_text == q["question_text"]
            ).first()
            if not exists:
                db.add(Question(**q))
                added += 1
        db.commit()
        print(f"Seeded {added} new Probability questions Q1-Q6 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
