import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

# Permutation and Combination Q11-Q21 verified answers:
# Q11: 4-digit, no repetition, digits 0-9 → 9×9×8×7 = 4536 (A)
# Q12: 3-digit all even digits → 4×5×5 = 100 (B)
# Q13: between 3000-4000, digits {3-8}, div by 5, no repeat → 3_5 → P(4,2)=12 (B)
# Q14: 5-digit div by 4, {1,2,3,4,5}, repetition → 5 pairs × 5^3 = 625 (A)
# Q15: 5-digit div by 4, {1,2,3,4,5,6}, no repeat → 8 pairs × P(4,3) = 192 (D)
# Q16: 1000-5000, digits {0-6}, no repeat → 4×P(6,3) = 480 (B)
# Q17: odd <2000, {0,1,3,4,7,8}, repeat allowed → 3+15+90+108 = 216 (D)
# Q18: 6-digit, 1st=4, 3rd=5, div by 9, any digit → (10000+8)/9 = 1112 (B)
# Q19: arrangements of MANISH (6 distinct) → 6! = 720 (A)
# Q20: arrangements of RUMOUR (R×2,U×2) → 6!/(2!×2!) = 180 (A)
# Q21: permutations of ALLAHABAD (A×4,L×2) → 9!/(4!×2!) = 7560 (C)

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "How many 4-digit numbers are there with no digit repeated?",
        "option_a": "4536",
        "option_b": "1728",
        "option_c": "9000",
        "option_d": "8999",
        "correct_answer": "A",
        "explanation": "First digit: 9 choices (1–9). Remaining 3 from 9 remaining digits: P(9,3) = 504. Total = 9 × 504 = 4536.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "How many 3-digit numbers are possible where all 3 digits are even?",
        "option_a": "175",
        "option_b": "100",
        "option_c": "500",
        "option_d": "96",
        "correct_answer": "B",
        "explanation": "Even digits: {0,2,4,6,8}. First digit (non-zero even): 4 choices. Second: 5 choices. Third: 5 choices. Total = 4×5×5 = 100.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "How many numbers can be made with the digits 3, 4, 5, 6, 7, 8 lying between 3000 and 4000 which are divisible by 5, while repetition of any digit is not allowed?",
        "option_a": "60",
        "option_b": "12",
        "option_c": "120",
        "option_d": "24",
        "correct_answer": "B",
        "explanation": "First digit = 3 (to lie in 3000–3999). For divisibility by 5, last digit = 5 (only 5 is available; 0 not in set). Middle 2 from remaining {4,6,7,8}: P(4,2) = 12.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "The number of 5-digit numbers which are divisible by 4, with digits from the set {1, 2, 3, 4, 5} and the repetition of digits is allowed, is ____?",
        "option_a": "625",
        "option_b": "600",
        "option_c": "525",
        "option_d": "500",
        "correct_answer": "A",
        "explanation": "For div by 4, last 2 digits must form a multiple of 4: {12,24,32,44,52} = 5 valid pairs. First 3 digits: 5³ = 125 choices. Total = 5 × 125 = 625.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "N is the total number of 5-digit numbers which are divisible by 4 and the numbers are formed using the digits 1, 2, 3, 4, 5 and 6. No digit is repeated in the number. What is the value of N?",
        "option_a": "144",
        "option_b": "162",
        "option_c": "NOT",
        "option_d": "192",
        "correct_answer": "D",
        "explanation": "Valid 2-digit endings (from {1–6}, no repeat, div by 4): 12,16,24,32,36,52,56,64 = 8 pairs. First 3 digits from remaining 4: P(4,3) = 24. N = 8 × 24 = 192.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "How many numbers between 1000 and 5000 can be formed with the digits 0, 1, 2, 3, 4, 5, 6 if repetition is not allowed?",
        "option_a": "240",
        "option_b": "480",
        "option_c": "120",
        "option_d": "500",
        "correct_answer": "B",
        "explanation": "First digit ∈ {1,2,3,4} (4 choices, to stay < 5000). Remaining 3 positions from 6 remaining digits: P(6,3) = 120. Total = 4 × 120 = 480.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "How many odd numbers less than 2000 can be formed using the digits 0, 1, 3, 4, 8, 7 if repetition of digits is allowed?",
        "option_a": "317",
        "option_b": "126",
        "option_c": "108",
        "option_d": "216",
        "correct_answer": "D",
        "explanation": "Odd digits in set: {1,3,7}=3. 1-digit: 3. 2-digit: 5×3=15. 3-digit: 5×6×3=90. 4-digit (<2000, first=1): 1×6×6×3=108. Total = 3+15+90+108 = 216.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "How many 6-digit numbers can be formed which are divisible by 9 and have '4' as the first digit and '5' as the 3rd digit?",
        "option_a": "1111",
        "option_b": "1112",
        "option_c": "1110",
        "option_d": "3334",
        "correct_answer": "B",
        "explanation": "Format: 4_5___. Digit sum = 9 + (d₂+d₄+d₅+d₆). For div by 9: d₂+d₄+d₅+d₆ ≡ 0 (mod 9). Using roots of unity: (10⁴+8)/9 = 10008/9 = 1112 such 4-tuples.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "How many words can be framed by the letters of the word MANISH?",
        "option_a": "720",
        "option_b": "480",
        "option_c": "360",
        "option_d": "240",
        "correct_answer": "A",
        "explanation": "MANISH has 6 distinct letters (M,A,N,I,S,H). Total arrangements = 6! = 720.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "In how many ways can the letters of the word RUMOUR be arranged?",
        "option_a": "180",
        "option_b": "360",
        "option_c": "90",
        "option_d": "720",
        "correct_answer": "A",
        "explanation": "RUMOUR = R(2), U(2), M(1), O(1) — 6 letters with two pairs of repeated letters. Arrangements = 6!/(2!×2!) = 720/4 = 180.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Find the number of permutations of the letters of the word ALLAHABAD.",
        "option_a": "9!",
        "option_b": "5880",
        "option_c": "7560",
        "option_d": "6!",
        "correct_answer": "C",
        "explanation": "ALLAHABAD = A(4), L(2), H(1), B(1), D(1) — 9 letters. Permutations = 9!/(4!×2!) = 362880/48 = 7560.",
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
        print(f"Seeded {added} new P&C questions Q11-Q21 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
