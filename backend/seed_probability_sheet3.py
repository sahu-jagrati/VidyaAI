import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

# Probability Q19-Q27 verified answers:
# Q19: 3 coins, exactly 2 heads → C(3,2)/8 = 3/8
# Q20: 4 coins, exactly 3 tails → C(4,3)/16 = 4/16 = 1/4
# Q21: 2 tosses, at most 1 head → (TT,HT,TH)/4 = 3/4
# Q22: 3 unbiased coins, at most 2 heads → (8-1)/8 = 7/8
# Q23: 3 coins, at least 1 head AND 1 tail → (8-2)/8 = 6/8 = 3/4
# Q24: 3 tosses alternating H&T → (HTH,THT)/8 = 2/8 = 1/4
# Q25: Coin tosses independent; P(head on 5th | tail on first 4) = 1/2
# Q26: 3 coins, P(exactly 1 head | both H and T appear) = 3/6 = 1/2
# Q27: P(4H)=P(7H) → C(n,4)=C(n,7) → n=11; P(2H)=C(11,2)/2^11=55/2048

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "3 coins are tossed. Find the probability of exactly 2 heads.",
        "option_a": "1/8",
        "option_b": "2/8",
        "option_c": "3/8",
        "option_d": "None of these",
        "correct_answer": "C",
        "explanation": "Total outcomes = 8. Exactly 2 heads: HHT, HTH, THH = C(3,2) = 3. P = 3/8.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "4 coins are tossed once. Find the probability of exactly 3 tails.",
        "option_a": "1/4",
        "option_b": "1/16",
        "option_c": "3/16",
        "option_d": "None of these",
        "correct_answer": "A",
        "explanation": "Total outcomes = 2⁴ = 16. Exactly 3 tails: C(4,3) = 4 ways. P = 4/16 = 1/4.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "A coin is tossed two times. Find the probability of getting at most one head.",
        "option_a": "1/4",
        "option_b": "2/3",
        "option_c": "3/4",
        "option_d": "1/3",
        "correct_answer": "C",
        "explanation": "Sample space = {HH, HT, TH, TT}. At most 1 head: TT, HT, TH = 3. P = 3/4.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "Three unbiased coins are tossed. What is the probability of getting at most two heads?",
        "option_a": "3/4",
        "option_b": "7/8",
        "option_c": "3/8",
        "option_d": "1/2",
        "correct_answer": "B",
        "explanation": "Total = 8. At most 2 heads = all except HHH = 7 outcomes. P = 7/8.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "3 coins are tossed. Find the probability of at least 1 head and 1 tail.",
        "option_a": "3/5",
        "option_b": "3/4",
        "option_c": "3/8",
        "option_d": "None of these",
        "correct_answer": "B",
        "explanation": "Total = 8. At least 1 head AND 1 tail = all except HHH and TTT = 6. P = 6/8 = 3/4.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "The probability of getting head and tail alternately in three throws of a coin (or throw of three coins) is?",
        "option_a": "1/8",
        "option_b": "1/4",
        "option_c": "1/3",
        "option_d": "3/8",
        "correct_answer": "B",
        "explanation": "Alternating patterns: HTH and THT = 2 outcomes. P = 2/8 = 1/4.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A fair coin is tossed repeatedly. If tail appears on first four tosses, then the probability of head appearing on fifth toss equals?",
        "option_a": "1/2",
        "option_b": "1/32",
        "option_c": "31/32",
        "option_d": "1/5",
        "correct_answer": "A",
        "explanation": "Each coin toss is independent. Previous outcomes do not affect the next. P(head on 5th toss) = 1/2.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "Three fair coins are tossed. If both heads and tails appear, then the probability that exactly one head appears is?",
        "option_a": "3/8",
        "option_b": "1/6",
        "option_c": "1/2",
        "option_d": "1/3",
        "correct_answer": "C",
        "explanation": "Condition: both H and T appear → 6 outcomes (all except HHH, TTT). Exactly 1 head: HTT, THT, TTH = 3. P = 3/6 = 1/2.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Probability",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "A coin is tossed a fixed number of times. If the probability of getting 4 heads equals the probability of getting 7 heads, then the probability of getting 2 heads is?",
        "option_a": "1/1024",
        "option_b": "55/2048",
        "option_c": "3/4096",
        "option_d": "None of these",
        "correct_answer": "B",
        "explanation": "P(4H)=P(7H) → C(n,4)=C(n,7) → n=4+7=11. P(2H) = C(11,2)/2¹¹ = 55/2048.",
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
        print(f"Seeded {added} new Probability questions Q19-Q27 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
