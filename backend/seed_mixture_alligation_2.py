"""
Mixture and Alligation questions — Gagan Pratap Maths (Q26–Q37).
Topic: "Mixture & Alligation" under Quantitative Aptitude.
Run: python seed_mixture_alligation_2.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

QUESTIONS = [
    # ── Q26 ── Jar A (P:Q=2:19) + Jar B (P:Q=1:11); 7L of A + 4L of B; P:Q ratio? (CHSL 2023 PRE)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Two jars A and B are containing the solution of two liquids P and Q. The ratio of the liquids P and Q in the jars A and B are 2:19 and 1:11, respectively. If 7 liters of the solution of jar A and 4 liters of the solution of jar B are mixed, what is the ratio of the solutions P and Q in the new mixture?",
        "option_a": "10 : 1",
        "option_b": "1 : 9",
        "option_c": "9 : 1",
        "option_d": "1 : 10",
        "correct_answer": "d",
        "explanation": "P from A = 7×2/21 = 2/3; P from B = 4×1/12 = 1/3. Total P = 1. Q from A = 7×19/21 = 19/3; Q from B = 4×11/12 = 11/3. Total Q = 10. Ratio P:Q = 1:10. (CHSL 2023 PRE)",
    },
    # ── Q27 ── Cu:Au in alloy1=3:4, alloy2=2:5; 26 kg + 39 kg mixed; Cu:Au in new alloy?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Ratio of Copper and Gold in first and second alloy are 3:4 and 2:5 respectively. 26 kg of the first alloy is mixed with 39 kg of the second alloy. Find the ratio of Copper and Gold, respectively, in the new mixture.",
        "option_a": "23 : 12",
        "option_b": "17 : 13",
        "option_c": "5 : 9",
        "option_d": "12 : 23",
        "correct_answer": "d",
        "explanation": "Cu from alloy1 = 26×3/7 = 78/7; Cu from alloy2 = 39×2/7 = 78/7. Total Cu = 156/7. Au from alloy1 = 26×4/7 = 104/7; Au from alloy2 = 39×5/7 = 195/7. Total Au = 299/7. Ratio = 156:299 = 12:23.",
    },
    # ── Q28 ── Alcohol:water A=7:8, B=3:2; 9L of A + 6L of B + 1L alcohol + 2L water; alcohol%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "The ratio of alcohol and water in solutions A and B are 7:8 and 3:2, respectively. If 9 litres of A is mixed with 6 litres of B and then 1 litre of alcohol and 2 litres of water are added to the resulting mixture, what is the percentage of alcohol in the final mixture so obtained (correct to one decimal place)?",
        "option_a": "46.7%",
        "option_b": "47.8%",
        "option_c": "47.4%",
        "option_d": "48.9%",
        "correct_answer": "d",
        "explanation": "Alcohol from A = 9×7/15 = 4.2L; from B = 6×3/5 = 3.6L. Total alcohol after adding 1L = 8.8L. Total volume = 9+6+1+2 = 18L. Alcohol% = 8.8/18 × 100 = 48.9%.",
    },
    # ── Q29 ── Acid:water A=5:4, B=7:11; 10L A + 8L B; in 324ml, add x ml water for 33⅓% acid (ICAR 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "The ratio of acid and water in solution A is 5:4 and 7:11 in solution B. 10 liters of A is mixed with 8 liters of B. In 324 ml of the resulting solution, how much water (in ml) should be added to get a solution containing 33⅓% acid?",
        "option_a": "145",
        "option_b": "148",
        "option_c": "144",
        "option_d": "162",
        "correct_answer": "c",
        "explanation": "Acid in mixture: A gives 50/9L, B gives 56/18=28/9L. Total acid = 78/9L in 18L. Acid fraction = 78/162 = 13/27. In 324ml: acid = 324×13/27 = 156ml. For 33⅓% acid: 156/(324+x) = 1/3 → x = 468−324 = 144 ml. (ICAR Assistant 2022)",
    },
    # ── Q30 ── Alcohol:water A=3:5, B=5:7; 2L A + 5L B + 3L alcohol = soln C; in 1.5L C add alcohol for 2:1 (IB ACIO 2023)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "The ratio of alcohol and water in solutions A and B is 3:5 and 5:7, respectively. Two liters of A is mixed with 5 liters of B and 3 liters of alcohol is also added to it to get a new solution C. How much alcohol in 1.5L of solution C (in ml) should be mixed so that the ratio of alcohol and water in the final solution becomes 2:1?",
        "option_a": "405",
        "option_b": "385",
        "option_c": "395",
        "option_d": "375",
        "correct_answer": "a",
        "explanation": "Alcohol in C: 2×3/8 + 5×5/12 + 3 = 0.75+2.083+3 = 5.833L. Water = 1.25+2.917 = 4.167L. Total C = 10L. In 1.5L: alcohol = 875ml, water = 625ml. For ratio 2:1: (875+x)/625 = 2 → x = 375ml. (IB ACIO 2023)",
    },
    # ── Q31 ── 3 equal bottles milk:water=5:7, 7:9, 2:1; all emptied; milk%? (CGL 2017)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Three bottles of equal capacity have mixture of milk and water in ratio 5:7, 7:9 and 2:1 respectively. These three bottles are emptied into a large bottle. What is the percentage of milk in the new mixture?",
        "option_a": "49.6",
        "option_b": "52.3",
        "option_c": "51.2",
        "option_d": "50.7",
        "correct_answer": "d",
        "explanation": "Equal capacity C. Milk = C(5/12 + 7/16 + 2/3) = C(20+21+32)/48 = 73C/48. Total = 3C. Milk% = 73/(3×48) × 100 = 73/144 × 100 ≈ 50.7%. (CGL 2017)",
    },
    # ── Q32 ── 3 containers A(1:3), B(2:3), C(2:5) milk:water; capacity ratio 2:3:5; all mixed; milk:water?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "Three containers A, B and C are having mixture of milk and water in the ratio 1:3, 2:3 and 2:5 respectively. If the capacities of the containers are in the ratio 2:3:5, find the ratio of milk to water, if the mixture of all 3 containers are mixed together.",
        "option_a": "143 : 296",
        "option_b": "438 : 962",
        "option_c": "348 : 962",
        "option_d": "481 : 219",
        "correct_answer": "b",
        "explanation": "Milk: 2×1/4 + 3×2/5 + 5×2/7 = 1/2+6/5+10/7 = (35+84+100)/140 = 219/140. Water: 2×3/4+3×3/5+5×5/7 = 3/2+9/5+25/7 = (105+126+250)/140 = 481/140. Ratio milk:water = 219:481 = 438:962.",
    },
    # ── Q33 ── Containers P(1:4), Q(2:3), R(3:5) milk:water; capacity ratio 5:4:8; all mixed; milk:water? (MTS 2020)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "The capacities of three containers P, Q and R are in the proportion of 5:4:8. They are completely filled with a mixture of milk and water in the proportions of 1:4, 2:3 and 3:5, respectively. If the mixtures of all the three containers are mixed together, then what will be the proportion of milk to water in the final mixture?",
        "option_a": "1 : 2",
        "option_b": "16 : 81",
        "option_c": "25 : 64",
        "option_d": "28 : 57",
        "correct_answer": "d",
        "explanation": "Milk: 5×1/5 + 4×2/5 + 8×3/8 = 1+8/5+3 = 28/5. Total = 17. Water = 17−28/5 = 57/5. Ratio = 28:57. (MTS 2020)",
    },
    # ── Q34 ── Drum1 A:B=18:7; mix drum1 and drum2 in 3:4 → final A:B=13:7; drum2 A:B=?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "There are two drums, each containing a mixture of paints A and B. In drum 1, A and B are in the ratio 18:7. The mixtures from drums 1 and 2 are mixed in the ratio 3:4 and in this final mixture, A and B are in the ratio 13:7. If in drum 2, then A and B were in the ratio:",
        "option_a": "229 : 141",
        "option_b": "220 : 149",
        "option_c": "239 : 161",
        "option_d": "251 : 163",
        "correct_answer": "c",
        "explanation": "A fraction in drum1 = 18/25. Final A fraction = 13/20. (3×18/25 + 4×a)/7 = 13/20 → 4a = 91/20−54/25 = 1195/500 → a = 239/400. Drum2: A:B = 239:161.",
    },
    # ── Q35 ── Mango juice water:mango=9:7; add x water + 3x mango to 160L → ratio 13:14; new volume? (SSC CGL 2024 Pre)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "A mango juice is made by mixing water and mango concentrate in the ratio 9:7. If x litres of water and 3x litres of mango concentrate is mixed in 160 litres of mango juice, then the new ratio becomes 13:14. What is the quantity of the new mango juice (in litres)?",
        "option_a": "197",
        "option_b": "212",
        "option_c": "206",
        "option_d": "216",
        "correct_answer": "d",
        "explanation": "Original 160L: water=90L, mango=70L. New: (90+x)/(70+3x) = 13/14 → 1260+14x = 910+39x → x=14. New total = 160+4×14 = 216L. (SSC CGL 2024 Pre)",
    },
    # ── Q36 ── Water + 4× milk = 7.5L; add milk to get 90% milk; extra milk? (SSC MTS 2023)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "In some quantity of water, four times the quantity of milk is added and the quantity of the mixture is now 7.5 liters. How much more milk to be added to the mixture to have 90% milk in the mixture?",
        "option_a": "9.5 liters",
        "option_b": "6 liters",
        "option_c": "4.5 liters",
        "option_d": "7.5 liters",
        "correct_answer": "d",
        "explanation": "Let water = w, milk = 4w. Total = 5w = 7.5 → w=1.5L, milk=6L. For 90% milk: (6+x)/(7.5+x) = 0.9 → 6+x = 6.75+0.9x → 0.1x = 0.75 → x = 7.5L. (SSC MTS 2023)",
    },
    # ── Q37 ── 200L mixture milk:water=17:3; add milk until ratio=7:1; milk added?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "200 liters of a mixture contains milk and water in the ratio 17:3. After the addition of some more milk to it, the ratio of milk to water in the resulting mixture becomes 7:1. The quantity of milk added to it was?",
        "option_a": "20 liters",
        "option_b": "40 liters",
        "option_c": "60 liters",
        "option_d": "80 liters",
        "correct_answer": "b",
        "explanation": "Milk = 200×17/20 = 170L, water = 30L. New ratio 7:1 means milk = 7×30 = 210L. Milk added = 210−170 = 40L.",
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
        print(f"Seeded {added} new Mixture & Alligation questions Q26-Q37 (skipped {len(QUESTIONS)-added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
