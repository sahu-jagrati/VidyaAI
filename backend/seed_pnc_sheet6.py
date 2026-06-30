import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

# Permutation and Combination Q60-Q65 verified answers:
# Q60: 13 players (4 bowlers), team of 11, at least 2 bowlers
#      → Since only 9 non-bowlers, every team of 11 automatically has ≥2 bowlers.
#      = C(13,11) = C(13,2) = 78 (C)
# Q61: 52-card deck, 5 cards with exactly 1 king
#      = C(4,1) × C(48,4) = 4 × C(48,4) (A)
# Q62-i:  4G+7B, team of 5, no girl → C(7,5) = 21 (A)
# Q62-ii: 4G+7B, team of 5, at least 1B and 1G → C(11,5)-C(7,5) = 462-21 = 441 (A)
# Q62-iii:4G+7B, team of 5, at least 3G → C(4,3)×C(7,2)+C(4,4)×C(7,1) = 84+7 = 91 (B)
# Q63: 4 officers+8 constables, select 6, at least 1 officer
#      = C(12,6) - C(8,6) = 924 - 28 = 896 (C)
# Q64: 6 boys+4 girls, select 4, at least 1 boy
#      = C(10,4) - C(4,4) = 210 - 1 = 209 (B)
# Q65: 20 breads, 4 persons, each eats at least 3
#      Let yi=xi-3, sum yi=8, yi≥0 → C(11,3) = 165 (C)

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In the 13 cricket players 4 are bowlers. In how many ways can a cricket team of 11 players be formed in which at least 2 bowlers are included?",
        "option_a": "55",
        "option_b": "72",
        "option_c": "78",
        "option_d": "None of these",
        "correct_answer": "C",
        "explanation": "Since only 9 non-bowlers exist, any team of 11 must include at least 11-9=2 bowlers. So 0-bowler and 1-bowler teams are impossible. Total valid teams = C(13,11) = C(13,2) = 78.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "Determine the number of 5-card combinations out of a deck of 52 cards if each selection of 5 cards has exactly one king.",
        "option_a": "4 × C(48,4)",
        "option_b": "360 × 48 × 46",
        "option_c": "365 × 48 × 47",
        "option_d": "None of these",
        "correct_answer": "A",
        "explanation": "Choose 1 king from 4: C(4,1)=4. Choose 4 non-kings from 48: C(48,4)=194,580. Total = 4 × C(48,4) = 778,320.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A group consists of 4 girls and 7 boys. In how many ways can a team of 5 members be selected if the team has no girl?",
        "option_a": "21",
        "option_b": "35",
        "option_c": "56",
        "option_d": "7",
        "correct_answer": "A",
        "explanation": "No girl means all 5 from 7 boys: C(7,5) = C(7,2) = 21.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A group consists of 4 girls and 7 boys. In how many ways can a team of 5 members be selected if the team has at least one boy and one girl?",
        "option_a": "441",
        "option_b": "420",
        "option_c": "462",
        "option_d": "21",
        "correct_answer": "A",
        "explanation": "Total C(11,5)=462. All boys C(7,5)=21. All girls C(4,5)=0. At least 1B and 1G = 462 - 21 - 0 = 441.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A group consists of 4 girls and 7 boys. In how many ways can a team of 5 members be selected if the team has at least 3 girls?",
        "option_a": "441",
        "option_b": "91",
        "option_c": "35",
        "option_d": "11",
        "correct_answer": "B",
        "explanation": "3G+2B: C(4,3)×C(7,2)=4×21=84. 4G+1B: C(4,4)×C(7,1)=1×7=7. Total = 84+7 = 91.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "In how many ways can 6 persons be selected from 4 officers and 8 constables, if at least one officer is to be included?",
        "option_a": "234",
        "option_b": "672",
        "option_c": "896",
        "option_d": "576",
        "correct_answer": "C",
        "explanation": "Total C(12,6)=924. Select with NO officer (all from 8 constables): C(8,6)=28. At least 1 officer = 924-28 = 896.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In how many ways can 4 children be selected from a group of 6 boys and 4 girls so that at least one boy is always there in the group?",
        "option_a": "159",
        "option_b": "209",
        "option_c": "194",
        "option_d": "185",
        "correct_answer": "B",
        "explanation": "Total C(10,4)=210. All girls (no boys): C(4,4)=1. At least 1 boy = 210-1 = 209.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "The number of ways in which 20 breads can be eaten by 4 persons such that each person eats at least 3 breads is?",
        "option_a": "130",
        "option_b": "166",
        "option_c": "165",
        "option_d": "120",
        "correct_answer": "C",
        "explanation": "Let yᵢ = xᵢ-3 (each person gets ≥3). Then y₁+y₂+y₃+y₄ = 20-12 = 8, yᵢ≥0. Non-negative integer solutions = C(8+3,3) = C(11,3) = 165.",
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
        print(f"Seeded {added} new P&C questions Q60-Q65 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
