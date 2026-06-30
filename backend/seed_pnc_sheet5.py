import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

# Permutation and Combination Q46-Q59 verified answers:
# Q46: 17C4 + 17C14 = 17C4 + 17C3 = 18C4 (Pascal's rule) (A)
# Q47: C(9,5) = 126 (B)
# Q48: Handshakes among 12 = C(12,2) = 66 (C)
# Q49: Hugs among 11 = C(11,2) = 55 (B)
# Q50: C(n,2)=28 → n(n-1)=56 → n=8 (D)
# Q51: n(n-1)=600 → n=25 (A)
# Q52: Chords from 20 points = C(20,2) = 190 (B)
# Q53: Triangles from 15 points (no 3 collinear) = C(15,3) = 455 (b)
# Q54: Triangles from 10 points (4 collinear) = C(10,3)-C(4,3) = 120-4 = 116 (C)
# Q55: 9 courses, 2 compulsory, choose 5 → C(7,3) = 35 (B)
# Q56: 7 men + 5 women, group of 5M+2W → C(7,5)×C(5,2) = 21×10 = 210 (A)
# Q57: 17 players (5 bowlers), select 11 with exactly 4 bowlers → C(5,4)×C(12,7)=3960 (a)
# Q58: 22 players, must include 2, exclude 4 → C(16,9)=C(16,7) (B)
# Q59: 16 players (5 bowlers, 2 WK), select 11 with 3B+1WK → C(5,3)×C(2,1)×C(9,7)=720 (B)

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "The value of 17C₄ + 17C₁₄ is?",
        "option_a": "18C4",
        "option_b": "30C16",
        "option_c": "17C10",
        "option_d": "18C15",
        "correct_answer": "A",
        "explanation": "17C₁₄ = 17C₃ (complementary property). By Pascal's rule: nCᵣ + nCᵣ₋₁ = (n+1)Cᵣ → 17C₄ + 17C₃ = 18C₄.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "In how many ways can 5 students be selected out of 9 students?",
        "option_a": "125",
        "option_b": "126",
        "option_c": "128",
        "option_d": "None of these",
        "correct_answer": "B",
        "explanation": "C(9,5) = 9!/(5!×4!) = (9×8×7×6)/(4×3×2×1) = 126.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "There are 12 people in a party. If each of them shakes hands with each other, how many handshakes are there in the party?",
        "option_a": "54",
        "option_b": "72",
        "option_c": "66",
        "option_d": "75",
        "correct_answer": "C",
        "explanation": "Each handshake involves 2 people: C(12,2) = 12×11/2 = 66.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "There are 11 people in a party and if each of them hugs with each other, how often do they hug?",
        "option_a": "45",
        "option_b": "55",
        "option_c": "64",
        "option_d": "None of these",
        "correct_answer": "B",
        "explanation": "Each hug involves 2 people (mutual): C(11,2) = 11×10/2 = 55.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A total of 28 handshakes were exchanged at the conclusion of a party. Assuming each participant was equally polite towards all the others, the number of people present was:",
        "option_a": "14",
        "option_b": "7",
        "option_c": "9",
        "option_d": "8",
        "correct_answer": "D",
        "explanation": "C(n,2) = 28 → n(n-1)/2 = 28 → n(n-1) = 56 = 8×7 → n = 8.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "On a new year day every student of a class sends a card to every other student. The postman delivers 600 cards. How many students are there in the class?",
        "option_a": "25",
        "option_b": "20",
        "option_c": "30",
        "option_d": "60",
        "correct_answer": "A",
        "explanation": "Each student sends (n-1) cards, total = n(n-1) = 600. Solving: n=25 (since 25×24 = 600).",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "How many chords can be drawn through 20 points on a circle?",
        "option_a": "10",
        "option_b": "190",
        "option_c": "200",
        "option_d": "270",
        "correct_answer": "B",
        "explanation": "A chord is determined by 2 points: C(20,2) = 20×19/2 = 190.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "There are 15 points in a plane, no three of which are collinear. Find the number of triangles formed by joining them.",
        "option_a": "435",
        "option_b": "455",
        "option_c": "420",
        "option_d": "441",
        "correct_answer": "B",
        "explanation": "A triangle needs 3 non-collinear points. Since no 3 are collinear, all combinations are valid: C(15,3) = 15×14×13/6 = 455.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "There are 10 points on a surface, 4 of them are collinear (linear). How many triangles can be formed from these points?",
        "option_a": "120",
        "option_b": "110",
        "option_c": "116",
        "option_d": "800",
        "correct_answer": "C",
        "explanation": "Total triangles = C(10,3) = 120. Subtract triangles from collinear points (no triangle): C(4,3) = 4. Valid triangles = 120 - 4 = 116.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In how many ways can a student choose a programme of 5 courses if 9 courses are available and 2 specific courses are compulsory for every student?",
        "option_a": "25",
        "option_b": "35",
        "option_c": "70",
        "option_d": "65",
        "correct_answer": "B",
        "explanation": "2 courses are fixed (compulsory). Student must choose 3 more from remaining 7 courses: C(7,3) = 35.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "There are 7 men and 5 women. In how many ways can a group of 5 men and 2 women be formed?",
        "option_a": "210",
        "option_b": "114",
        "option_c": "126",
        "option_d": "90",
        "correct_answer": "A",
        "explanation": "Choose 5 men from 7: C(7,5) = 21. Choose 2 women from 5: C(5,2) = 10. Total = 21 × 10 = 210.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "In how many ways can one select a cricket team of 11 from 17 players in which only 5 persons can bowl, if each cricket team of 11 must include exactly 4 bowlers?",
        "option_a": "3960",
        "option_b": "4040",
        "option_c": "5100",
        "option_d": "3850",
        "correct_answer": "A",
        "explanation": "Choose 4 bowlers from 5: C(5,4) = 5. Choose 7 non-bowlers from 12: C(12,7) = 792. Total = 5 × 792 = 3960.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "The number of ways in which a team of 11 players can be selected from 22 players, including 2 of them and excluding 4 of them, is:",
        "option_a": "16C6",
        "option_b": "16C7",
        "option_c": "16C8",
        "option_d": "20C7",
        "correct_answer": "B",
        "explanation": "2 players must be included (fixed). 4 players must be excluded. Pool = 22-2-4 = 16 players. Need 11-2 = 9 more: C(16,9) = C(16,7).",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "In a touring cricket team there are 16 players including 5 bowlers and 2 wicket-keepers. How many teams of 11 can be chosen so as to include three bowlers and one wicket-keeper?",
        "option_a": "650",
        "option_b": "720",
        "option_c": "750",
        "option_d": "640",
        "correct_answer": "B",
        "explanation": "Choose 3 bowlers from 5: C(5,3)=10. Choose 1 WK from 2: C(2,1)=2. Choose 7 others from 9: C(9,7)=C(9,2)=36. Total = 10×2×36 = 720.",
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
        print(f"Seeded {added} new P&C questions Q46-Q59 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
