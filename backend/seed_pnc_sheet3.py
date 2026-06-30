import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

# Permutation and Combination Q22-Q31 verified answers:
# Q22: PERMUTATIONS (12 letters, T×2), fix P(start) S(end) → 10!/2! (B)
# Q23: 4 boys 3 girls alternate → BGBGBGB → 4!×3! = 144 (A)
# Q24: EQUATION vowels(5)+consonants(3) in same positions, rearrange each → 5!×3! = 720 (D)
# Q25: MONDAY, start M not end Y → 5! - 4! = 96 (B)
# Q26: JANUARY (A×2), fix J(start) Y(end) → 5!/2! = 60 (A)
# Q27-1: ARRANGE (A×2,R×2), two R's together → 6!/2! = 360 (A)
# Q27-2: ARRANGE, two R's NOT together → 7!/(2!×2!) - 360 = 1260-360 = 900 (C)
# Q27-3: ARRANGE, two R's AND two A's together → 5! = 120 (A)
# Q29: PUZZLE (Z×2), vowels U,E together → (5!/2!)×2! = 120 (D)
# Q30: SOFTWARE, vowels O,A,E together → 6!×3! = 4320 (A)
# Q31: ADJUST, vowels A,U NOT together → 6! - (5!×2!) = 720-240 = 480 (C)

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In how many ways can the letters of the word PERMUTATIONS be arranged if the word starts with P and ends with S?",
        "option_a": "12!/2!",
        "option_b": "10!/2!",
        "option_c": "8!",
        "option_d": "10!",
        "correct_answer": "B",
        "explanation": "PERMUTATIONS has 12 letters with T repeated twice. Fix P at start and S at end. Remaining 10 letters {E,R,M,U,T,A,T,I,O,N} have T×2. Arrangements = 10!/2! = 1,814,400.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In how many ways can 4 boys and 3 girls be seated in a row so that they are alternate?",
        "option_a": "144",
        "option_b": "720",
        "option_c": "256",
        "option_d": "120",
        "correct_answer": "A",
        "explanation": "With 4 boys and 3 girls alternating, the only valid pattern is BGBGBGB. Boys fill 4 positions in 4!=24 ways; Girls fill 3 positions in 3!=6 ways. Total = 24×6 = 144.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "How many different words can be formed from the letters of the word 'EQUATION' without changing the relative order of vowels and consonants?",
        "option_a": "120",
        "option_b": "240",
        "option_c": "360",
        "option_d": "720",
        "correct_answer": "D",
        "explanation": "EQUATION has 5 vowels (E,U,A,I,O) at 5 fixed positions and 3 consonants (Q,T,N) at 3 fixed positions. Keeping the vowel/consonant slots fixed: vowels arrange in 5!=120 ways, consonants in 3!=6 ways. Total = 120×6 = 720.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In how many ways can the letters of the word MONDAY be arranged such that they begin with M and do not end with Y?",
        "option_a": "72",
        "option_b": "96",
        "option_c": "84",
        "option_d": "90",
        "correct_answer": "B",
        "explanation": "MONDAY has 6 distinct letters. Arrangements starting with M = 5!=120. Arrangements starting with M and ending with Y = 4!=24. Starting with M, not ending with Y = 120-24 = 96.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In how many ways can the letters of the word 'JANUARY' be arranged if the arrangement begins with J and ends with Y?",
        "option_a": "60",
        "option_b": "120",
        "option_c": "30",
        "option_d": "180",
        "correct_answer": "A",
        "explanation": "JANUARY = J,A,N,U,A,R,Y — 7 letters with A repeated twice. Fix J(start) and Y(end). Remaining 5 letters: A,N,U,A,R with A×2. Arrangements = 5!/2! = 60.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In how many arrangements of the letters of the word 'ARRANGE' do the two R's come together?",
        "option_a": "360",
        "option_b": "720",
        "option_c": "900",
        "option_d": "1260",
        "correct_answer": "A",
        "explanation": "ARRANGE = A(2),R(2),N,G,E. Treat [RR] as one unit → 6 units with A×2. Arrangements = 6!/2! = 720/2 = 360.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In how many arrangements of the letters of the word 'ARRANGE' do the two R's NOT come together?",
        "option_a": "360",
        "option_b": "720",
        "option_c": "900",
        "option_d": "1260",
        "correct_answer": "C",
        "explanation": "Total arrangements of ARRANGE = 7!/(2!×2!) = 1260. Arrangements with R's together = 360. R's NOT together = 1260-360 = 900.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In how many arrangements of the letters of the word 'ARRANGE' do the two R's and the two A's come together?",
        "option_a": "120",
        "option_b": "240",
        "option_c": "360",
        "option_d": "60",
        "correct_answer": "A",
        "explanation": "Treat [RR] and [AA] each as one unit. Units: [RR],[AA],N,G,E = 5 distinct units. Arrangements = 5! = 120.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In how ways can the letters of the word 'PUZZLE' be arranged to form different new words such that the vowels always come together?",
        "option_a": "280",
        "option_b": "450",
        "option_c": "630",
        "option_d": "120",
        "correct_answer": "D",
        "explanation": "PUZZLE = P,U,Z,Z,L,E — Z×2, vowels U,E. Treat [UE] as one unit → 5 units with Z×2. Arrangements = 5!/2! = 60. Vowel arrangements = 2! = 2. Total = 60×2 = 120.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In how many different ways can the letters of the word 'SOFTWARE' be arranged in such a way that the vowels always come together?",
        "option_a": "4320",
        "option_b": "1440",
        "option_c": "360",
        "option_d": "120",
        "correct_answer": "A",
        "explanation": "SOFTWARE has 8 distinct letters; vowels: O,A,E (3), consonants: S,F,T,W,R (5). Treat [OAE] as one unit → 6 distinct units. Arrangements = 6!×3! = 720×6 = 4320.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Permutation and Combination",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In how many ways can the letters of the word ADJUST be arranged so that the vowels do not come together?",
        "option_a": "720",
        "option_b": "240",
        "option_c": "480",
        "option_d": "360",
        "correct_answer": "C",
        "explanation": "ADJUST = 6 distinct letters; vowels: A,U (2). Total = 6!=720. Vowels together: treat [AU] as unit → 5!×2! = 240. Vowels NOT together = 720-240 = 480.",
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
        print(f"Seeded {added} new P&C questions Q22-Q31 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
