import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

# Probability Sheet-1 Q7-Q18 (SSC CGL MAINS BATCH 2023)
# Q7:  cards 33-92 exclusive → 58 cards; perfect squares 36,49,64,81=4 → P=4/58=2/29
# Q8:  10 at round table; 2 together → P=(8!×2!)/9! = 2/9
# Q9:  coin+die sample space = 2×6 = 12
# Q10: 3 coin tosses → 2^3 = 8 outcomes
# Q11-I:   3 coins, exactly 1 head → C(3,1)/8 = 3/8
# Q11-II:  3 coins, no head → 1/8
# Q11-III: 3 coins, at least 2 heads → (3+1)/8 = 1/2
# Q12: 3 coins, no head → 1/8
# Q13: 4 heads in 8 throws → C(8,4)/2^8 = 70/256 = 35/128
# Q14: 2 coins, at least 1 tail → 1 - 1/4 = 3/4
# Q15: 2 coins, heads both times → (1/2)^2 = 1/4
# Q16: 4 throws, at least 1 tail → 1 - (1/2)^4 = 15/16
# Q17: 5 tosses, at least 3 heads → (C(5,3)+C(5,4)+C(5,5))/32 = 16/32 = 1/2
# Q18: 6 coins, at least 4 heads → (C(6,4)+C(6,5)+C(6,6))/64 = 22/64 = 11/32

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A bag contains cards numbered between 33 and 92. If one card is drawn from the bag, the probability that the number on the drawn card is a perfect square is?",
        "option_a": "5/59",
        "option_b": "4/59",
        "option_c": "2/29",
        "option_d": "1/12",
        "correct_answer": "C",
        "explanation": "Numbers between 33 and 92 (exclusive) = 34 to 91 = 58 cards. Perfect squares: 36(6²),49(7²),64(8²),81(9²) = 4. P = 4/58 = 2/29.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "10 persons are seated at a round table. The probability that two particular persons sit together is?",
        "option_a": "1/5",
        "option_b": "2/9",
        "option_c": "3/7",
        "option_d": "4/9",
        "correct_answer": "B",
        "explanation": "Total circular arrangements = 9!. Treat 2 persons as 1 unit: (8! × 2!) arrangements. P = (8! × 2!)/9! = 2/9.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "Describe the sample space for the experiment in which a coin is tossed and a die is thrown. How many elements does the sample space have?",
        "option_a": "12",
        "option_b": "14",
        "option_c": "16",
        "option_d": "None of these",
        "correct_answer": "A",
        "explanation": "Coin has 2 outcomes (H/T), die has 6 outcomes. Total sample space = 2 × 6 = 12.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "A coin is tossed 3 times and the outcomes are recorded. How many possible outcomes are there?",
        "option_a": "4",
        "option_b": "6",
        "option_c": "8",
        "option_d": "10",
        "correct_answer": "C",
        "explanation": "Each toss has 2 outcomes. For 3 tosses: 2³ = 8 possible outcomes.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "A coin is tossed 3 times. Find the probability of getting exactly one head.",
        "option_a": "1/8",
        "option_b": "3/8",
        "option_c": "7/8",
        "option_d": "5/8",
        "correct_answer": "B",
        "explanation": "Total outcomes = 8. Exactly 1 head: HTT, THT, TTH = C(3,1) = 3. P = 3/8.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "A coin is tossed 3 times. Find the probability of getting no head.",
        "option_a": "1/8",
        "option_b": "1/4",
        "option_c": "1/6",
        "option_d": "None of these",
        "correct_answer": "A",
        "explanation": "Total outcomes = 8. No head means TTT = 1 outcome. P = 1/8.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "A coin is tossed 3 times. Find the probability of getting at least 2 heads.",
        "option_a": "1/2",
        "option_b": "7/8",
        "option_c": "1/8",
        "option_d": "None of these",
        "correct_answer": "A",
        "explanation": "Total = 8. At least 2 heads: 2H(HHT,HTH,THH)=3, 3H(HHH)=1 → 4 outcomes. P = 4/8 = 1/2.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "3 coins are tossed. Find the probability of getting no heads.",
        "option_a": "1/8",
        "option_b": "1/4",
        "option_c": "3/8",
        "option_d": "None of these",
        "correct_answer": "A",
        "explanation": "Total outcomes = 2³ = 8. No heads = all tails (TTT) = 1 outcome. P = 1/8.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "The probability of getting 4 heads in 8 throws of a coin is?",
        "option_a": "1/2",
        "option_b": "1/64",
        "option_c": "35/128",
        "option_d": "1/32",
        "correct_answer": "C",
        "explanation": "P(4 heads in 8 throws) = C(8,4)/2⁸ = 70/256 = 35/128.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "When two coins are tossed simultaneously, what are the chances of getting at least one tail?",
        "option_a": "3/4",
        "option_b": "1/5",
        "option_c": "4/5",
        "option_d": "1/4",
        "correct_answer": "A",
        "explanation": "Sample space = {HH, HT, TH, TT}. At least 1 tail: HT, TH, TT = 3. P = 3/4.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "A coin is tossed twice. The probability of getting head both the times is?",
        "option_a": "1/2",
        "option_b": "1/4",
        "option_c": "3/4",
        "option_d": "1",
        "correct_answer": "B",
        "explanation": "P(HH) = 1/2 × 1/2 = 1/4.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "The probability of getting at least one tail in 4 throws of a coin is?",
        "option_a": "15/16",
        "option_b": "1/16",
        "option_c": "1/2",
        "option_d": "None of these",
        "correct_answer": "A",
        "explanation": "P(at least 1 tail) = 1 − P(no tails) = 1 − (1/2)⁴ = 1 − 1/16 = 15/16.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A coin is tossed 5 times one after the other. Find the probability of getting at least 3 heads.",
        "option_a": "1/4",
        "option_b": "3/32",
        "option_c": "1/2",
        "option_d": "1/5",
        "correct_answer": "C",
        "explanation": "P(≥3 heads) = [C(5,3)+C(5,4)+C(5,5)]/2⁵ = (10+5+1)/32 = 16/32 = 1/2.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "6 coins are thrown together. What is the probability of getting at least 4 heads?",
        "option_a": "21/32",
        "option_b": "11/32",
        "option_c": "11/64",
        "option_d": "7/32",
        "correct_answer": "B",
        "explanation": "P(≥4 heads) = [C(6,4)+C(6,5)+C(6,6)]/2⁶ = (15+6+1)/64 = 22/64 = 11/32.",
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
        print(f"Seeded {added} new Probability questions Q7-Q18 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
