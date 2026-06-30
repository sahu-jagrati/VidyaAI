import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

# Permutation and Combination Q1-Q10 (Q4 has 2 sub-parts = 11 entries)
# Q1:  Select 11 from 17 AND arrange in a row → 17P11 → B
# Q2:  Captain + vice-captain from 11 → 11×10=110 → A
# Q3:  2 members for 2 different positions from 8 → P(8,2)=56 → D
# Q4-I:  3-digit from {1-5} WITH repetition → 5^3=125 → A
# Q4-II: 3-digit from {1-5} WITHOUT repetition → P(5,3)=60 → B
# Q5:  5-digit numbers with all odd digits → 5^5=3125 → A
# Q6:  100-digit positive numbers → 9×10^99 → A
# Q7:  4-letter words from ROSE, no repetition → 4!=24 → B
# Q8:  4-letter code from first 10 letters, no repetition → P(10,4)=5040 → B
# Q9:  4-digit even from {1-8} without repetition → 4×P(7,3)=840 → B
# Q10: 4-digit even from {1,2,3,4,5} with repetition → 2×5^3=250 → A

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In how many ways can one select a cricket team of 11 players from 17 players and arrange them in a row?",
        "option_a": "17C11",
        "option_b": "17P11",
        "option_c": "11C7",
        "option_d": "11P11",
        "correct_answer": "B",
        "explanation": "We must select 11 from 17 AND arrange them in order. This is a permutation: 17P11 = 17!/(17-11)! = 17!/6!.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "Out of 11 members of a team, two players have to be selected such that one is captain and another is vice-captain. In how many ways can this be done?",
        "option_a": "110",
        "option_b": "115",
        "option_c": "120",
        "option_d": "100",
        "correct_answer": "A",
        "explanation": "Since captain and vice-captain are distinct roles, order matters. P(11,2) = 11×10 = 110.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "From a committee of 8 persons, in how many ways can we choose 2 members, assuming one person cannot hold more than one position?",
        "option_a": "28",
        "option_b": "14",
        "option_c": "112",
        "option_d": "56",
        "correct_answer": "D",
        "explanation": "Since the 2 members are for 2 different positions, order matters. P(8,2) = 8×7 = 56.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "How many 3-digit numbers can be formed from the digits 1, 2, 3, 4 and 5, assuming that repetition of the digits is allowed?",
        "option_a": "125",
        "option_b": "60",
        "option_c": "100",
        "option_d": "None of these",
        "correct_answer": "A",
        "explanation": "Each of the 3 positions can be filled with any of 5 digits (repetition allowed): 5×5×5 = 5³ = 125.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "How many 3-digit numbers can be formed from the digits 1, 2, 3, 4 and 5, assuming that repetition of the digits is NOT allowed?",
        "option_a": "125",
        "option_b": "60",
        "option_c": "100",
        "option_d": "None of these",
        "correct_answer": "B",
        "explanation": "Without repetition: P(5,3) = 5×4×3 = 60.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "How many five-digit numbers are there in which all the digits are odd?",
        "option_a": "3125",
        "option_b": "120",
        "option_c": "625",
        "option_d": "3000",
        "correct_answer": "A",
        "explanation": "Odd digits: {1,3,5,7,9} = 5 choices per position. With repetition allowed: 5⁵ = 3125.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "How many 100-digit positive numbers are there?",
        "option_a": "9 × 10^99",
        "option_b": "9 × 10^100",
        "option_c": "10^100",
        "option_d": "11 × 10^98",
        "correct_answer": "A",
        "explanation": "100-digit numbers range from 10^99 to (10^100 - 1). Count = 10^100 - 10^99 = 9 × 10^99.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "Find the number of 4-letter words, with or without meaning, which can be formed using the letters of the word ROSE, where repetition of letters is not allowed.",
        "option_a": "20",
        "option_b": "24",
        "option_c": "12",
        "option_d": "6",
        "correct_answer": "B",
        "explanation": "ROSE has 4 distinct letters. 4-letter arrangements without repetition = P(4,4) = 4! = 24.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "How many 4-letter codes can be formed using the first 10 letters of the English alphabet, if no letter can be repeated?",
        "option_a": "4536",
        "option_b": "5040",
        "option_c": "1996",
        "option_d": "120",
        "correct_answer": "B",
        "explanation": "First 10 letters = {a,b,c,...,j}. 4-letter codes without repetition: P(10,4) = 10×9×8×7 = 5040.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "From the digits 1, 2, 3, 4, 5, 6, 7, 8, how many four-digit even numbers can be formed if repetition is not allowed?",
        "option_a": "841",
        "option_b": "840",
        "option_c": "843",
        "option_d": "742",
        "correct_answer": "B",
        "explanation": "Units place (even): 4 choices (2,4,6,8). Remaining 3 positions from 7 remaining digits: P(7,3)=210. Total = 4×210 = 840.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "How many 4-digit even numbers can be formed from the digits 1, 2, 3, 4, 5 if the digits can be repeated?",
        "option_a": "250",
        "option_b": "120",
        "option_c": "240",
        "option_d": "160",
        "correct_answer": "A",
        "explanation": "Units place (even digits from set): 2 choices (2 or 4). First 3 positions: 5 choices each = 5³=125. Total = 2×125 = 250.",
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
        print(f"Seeded {added} new P&C questions Q1-Q10 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
