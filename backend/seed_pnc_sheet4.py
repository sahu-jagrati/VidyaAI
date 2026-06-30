import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

# Permutation and Combination Q33-Q45 verified answers:
# Q33: PRACTICE(C×2), 3 vowels on 4 even places → C(4,3)×3!×5!/2! = 4×6×60 = 1440 (B)
# Q34: EQUATION (5V,3C all distinct), no two consonants together → 5!×P(6,3) = 14400 (A)
# Q35-I: DAUGHTER (8 distinct), vowels A,U,E together → 6!×3! = 4320 (A)
# Q35-II: DAUGHTER vowels NOT together → 8!-4320 = 36000 (A)
# Q36: 7 students, 2 English medium NOT together → 7!-6!×2! = 3600 (C)
# Q37: 8 candidates (3 Maths), no two Maths adjacent → 5!×P(6,3) = 14400 (A)
# Q38: 7 boys + 5 girls, no two girls together → 7!×P(8,5) = 7!×8!/3! (A)
# Q39: 6 men + 4 women round table → (10-1)! = 9! (C)
# Q40: 12 beads necklace → (12-1)!/2 = 11!/2 (A)
# Q41-A: 20 delegates, no restriction → 19! (A)
# Q41-B: 2 delegates always together → 18!×2! = 2×18! (A)
# Q41-C: 2 delegates never together → 19!-2×18! = 17×18! (A)
# Q42: 21 people (host fixed), 2 on either side of host → 2!×18! = 2×18! (A)
# Q43: 13 members circular (principal fixed), teacher+secretary flanking → 2!×10! = 2×10! (A)
# Q44: 6 men + 5 women round table, no two women adjacent → 5!×P(6,5) = 5!×6! (A)
# Q45: 19C(3r) = 19C(r+3) → 3r+(r+3)=19 → r=4 (B)

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "How many words can be formed with the letters of the word 'PRACTICE' so that vowels always occupy the even places?",
        "option_a": "4320",
        "option_b": "1440",
        "option_c": "360",
        "option_d": "120",
        "correct_answer": "B",
        "explanation": "PRACTICE = P,R,A,C,T,I,C,E (C×2). Vowels: A,I,E (3); Even places: 2,4,6,8 (4 places). Choose 3 of 4 even places: C(4,3)=4; Arrange vowels: 3!=6; Arrange 5 consonants (C×2) in remaining 5 places: 5!/2!=60. Total = 4×6×60 = 1440.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In how many ways can the letters of the word EQUATION be arranged such that no two consonants come together?",
        "option_a": "14400",
        "option_b": "7200",
        "option_c": "5040",
        "option_d": "720",
        "correct_answer": "A",
        "explanation": "EQUATION: vowels E,U,A,I,O (5 distinct), consonants Q,T,N (3 distinct). Arrange 5 vowels: 5!=120 ways, creating 6 gaps. Place 3 consonants in 6 gaps: P(6,3)=120. Total = 120×120 = 14400.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Find the number of different 8-letter arrangements from the word DAUGHTER such that all vowels occur together.",
        "option_a": "4320",
        "option_b": "2160",
        "option_c": "8640",
        "option_d": "1440",
        "correct_answer": "A",
        "explanation": "DAUGHTER: 8 distinct letters; vowels A,U,E (3), consonants D,G,H,T,R (5). Treat [AUE] as one unit → 6 distinct units. Arrangements = 6!×3! = 720×6 = 4320.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Find the number of different 8-letter arrangements from the word DAUGHTER such that all vowels do NOT occur together.",
        "option_a": "36000",
        "option_b": "38160",
        "option_c": "40320",
        "option_d": "4320",
        "correct_answer": "A",
        "explanation": "Total arrangements of DAUGHTER = 8! = 40320. Arrangements with all vowels together = 4320. Vowels NOT together = 40320 - 4320 = 36000.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "7 students take an exam. Two of them are from English medium. Find the possible number of ways when both English medium students do not sit together.",
        "option_a": "2400",
        "option_b": "1200",
        "option_c": "3600",
        "option_d": "4800",
        "correct_answer": "C",
        "explanation": "Total arrangements = 7! = 5040. Both English students together = 6!×2! = 1440. NOT together = 5040 - 1440 = 3600.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "8 candidates are to be examined, 3 in Mathematics and the remaining in different subjects. In how many ways can they be seated in a row so that no two Mathematics examinees sit together?",
        "option_a": "14400",
        "option_b": "7200",
        "option_c": "3600",
        "option_d": "10800",
        "correct_answer": "A",
        "explanation": "Arrange 5 non-Maths candidates: 5!=120 ways, creating 6 gaps. Place 3 Maths candidates in 6 gaps (no two adjacent): P(6,3)=120. Total = 120×120 = 14400.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "In how many ways can 7 boys and 5 girls be seated in a row so that no two girls sit together?",
        "option_a": "7! × P(8,5)",
        "option_b": "6! × 7!",
        "option_c": "5! × 8!",
        "option_d": "7! × C(8,5)",
        "correct_answer": "A",
        "explanation": "Arrange 7 boys: 7! = 5040 ways, creating 8 gaps. Place 5 girls in 8 gaps (no two adjacent): P(8,5) = 8!/3! = 6720. Total = 7! × P(8,5) = 5040 × 6720 = 33,868,800.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "At a dinner party 6 men and 4 women sit at a round table. In how many ways can they sit?",
        "option_a": "11!",
        "option_b": "8!",
        "option_c": "9!",
        "option_d": "10!",
        "correct_answer": "C",
        "explanation": "Total 10 people (6 men + 4 women) arranged in a circle: (10-1)! = 9!",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "Find the number of ways in which 12 different beads can be arranged to form a necklace.",
        "option_a": "11!/2",
        "option_b": "12!/2",
        "option_c": "10!/2",
        "option_d": "11!",
        "correct_answer": "A",
        "explanation": "For a necklace, clockwise and anticlockwise arrangements are identical. Arrangements = (12-1)!/2 = 11!/2.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A round table conference is to be held among 20 delegates from 20 different countries. In how many ways can they be seated without any restriction?",
        "option_a": "19!",
        "option_b": "20!",
        "option_c": "18!",
        "option_d": "17!",
        "correct_answer": "A",
        "explanation": "20 people in a circular arrangement (no restriction): (20-1)! = 19!",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A round table conference is to be held among 20 delegates from 20 different countries. In how many ways can they be seated when two particular delegates must always sit together?",
        "option_a": "2 × 18!",
        "option_b": "18!",
        "option_c": "19!",
        "option_d": "2 × 17!",
        "correct_answer": "A",
        "explanation": "Treat 2 specific delegates as one unit → 19 units in circular arrangement: (19-1)! = 18!. The 2 delegates can swap within their unit: 2!. Total = 2 × 18!.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A round table conference is to be held among 20 delegates from 20 different countries. In how many ways can they be seated when two particular delegates must never sit together?",
        "option_a": "17 × 18!",
        "option_b": "19! - 18!",
        "option_c": "17!",
        "option_d": "18!",
        "correct_answer": "A",
        "explanation": "Total = 19!. Always together = 2×18!. Never together = 19! - 2×18! = 18!(19-2) = 17×18!.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "20 persons are invited to a party. In how many different ways can they be seated at a circular table with two particular persons seated on either side of the host?",
        "option_a": "2 × 18!",
        "option_b": "18!",
        "option_c": "2 × 19!",
        "option_d": "2 × 17!",
        "correct_answer": "A",
        "explanation": "Total 21 people (20 invitees + 1 host). Fix host's position. 2 specific invitees on immediate sides of host: 2! = 2 ways. Remaining 18 invitees in 18 seats: 18!. Total = 2 × 18!.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In how many ways can 13 members of a school sit along a circular table when the teacher is to sit on one side of the principal and the secretary on the other side?",
        "option_a": "2 × 10!",
        "option_b": "11!",
        "option_c": "10!",
        "option_d": "2 × 12!",
        "correct_answer": "A",
        "explanation": "Fix principal's position (circular arrangement). Teacher and secretary must be on immediate sides of principal: 2! = 2 ways (can swap which side). Remaining 10 members in 10 seats: 10!. Total = 2 × 10!.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Find the number of ways in which 6 men and 5 women can dine at a round table if no two women can sit together.",
        "option_a": "5! × 6!",
        "option_b": "5! × 5!",
        "option_c": "4! × 5!",
        "option_d": "6!",
        "correct_answer": "A",
        "explanation": "Arrange 6 men in circle: (6-1)! = 5! ways, creating 6 gaps. Place 5 women in 6 gaps (no two adjacent): P(6,5) = 6!/1! = 6!. Total = 5! × 6! = 86400.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "If 19C₃ᵣ = 19Cᵣ₊₃, then find the value of r.",
        "option_a": "3",
        "option_b": "4",
        "option_c": "5",
        "option_d": "8",
        "correct_answer": "B",
        "explanation": "Using nCₐ = nCᵦ ⟹ a+b=n (when a≠b): 3r + (r+3) = 19 ⟹ 4r = 16 ⟹ r = 4. Check: 19C₁₂ = 19C₇ ✓.",
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
        print(f"Seeded {added} new P&C questions Q33-Q45 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
