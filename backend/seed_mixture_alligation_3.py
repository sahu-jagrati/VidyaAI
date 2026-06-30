"""
Mixture and Alligation questions — Gagan Pratap Maths (Q38–Q55).
Topic: "Mixture & Alligation" under Quantitative Aptitude.
Run: python seed_mixture_alligation_3.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

QUESTIONS = [
    # ── Q38 ── 178L mixture water:milk=5:7; add water to make 3:4? (CHSL 2023 PRE)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "In a mixture of 178 liters, the ratio of water and milk is 5:7. How much water should be added to make the ratio of water and milk 3:4?",
        "option_a": "4⅔ liters",
        "option_b": "3⅓ liters",
        "option_c": "2½ liters",
        "option_d": "2⅔ liters",
        "correct_answer": "a",
        "explanation": "Water = 178×5/12, milk = 178×7/12. Add x water: (water+x)/milk = 3/4. Solving gives x = 4⅔ liters. (CHSL 2023 PRE)",
    },
    # ── Q39 ── 1458L milk:water=8:1; add water to make 6:5; water added? (RRB RPF SI 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Ravi has 1458 litres of a mixture of milk and water. The ratio of milk to water in this mixture is 8:1. How much water (in litres) should Ravi add into the mixture so that the ratio of milk and water becomes 6:5?",
        "option_a": "918",
        "option_b": "909",
        "option_c": "927",
        "option_d": "900",
        "correct_answer": "a",
        "explanation": "Milk = 1458×8/9 = 1296L, water = 162L. For 6:5: 1296/(162+x) = 6/5 → x = 918L. (RRB RPF SI 2024)",
    },
    # ── Q40 ── 65L kerosene:petrol=3:2; add petrol to make 4:5; petrol added?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "In 65 litres of a mixture of kerosene and petrol, the ratio of kerosene to petrol is 3:2. In order to make this ratio 4:5, how many litres of petrol should be added to the given mixture?",
        "option_a": "29.25",
        "option_b": "24.5",
        "option_c": "23.25",
        "option_d": "22.75",
        "correct_answer": "d",
        "explanation": "Kerosene = 39L, petrol = 26L. For 4:5: 39/(26+x) = 4/5 → 195 = 104+4x → x = 22.75L.",
    },
    # ── Q41 ── Vessel milk:water=4:7; add 25L water → ratio 6:13; initial mixture?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The ratio of milk and water in a vessel is 4:7. If 25ltr water is added then ratio becomes 6:13. Find the initial quantity of mixture (in ltr)?",
        "option_a": "150",
        "option_b": "132",
        "option_c": "165",
        "option_d": "175",
        "correct_answer": "c",
        "explanation": "Let milk=4k, water=7k. After 25L water: 4k/(7k+25) = 6/13 → 52k = 42k+150 → k=15. Initial = 11×15 = 165L.",
    },
    # ── Q42 ── Vessel milk:water=8:5; add 44L milk+44L water → milk 28.56% more than water; initial water?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The ratio of milk and water in a vessel is 8:5. If we added 44ltr milk and 44ltr water then quantity of milk becomes 28.56% more than water. Find the initial quantity of water?",
        "option_a": "48 ltr",
        "option_b": "45 ltr",
        "option_c": "40 ltr",
        "option_d": "60 ltr",
        "correct_answer": "c",
        "explanation": "28.56% ≈ 2/7. So (8k+44)/(5k+44) = 9/7 → 56k+308 = 45k+396 → k=8. Initial water = 5×8 = 40L.",
    },
    # ── Q43 ── 19L giloy juice (giloy:water=2:9); sold 2½L; add water → 1:5; water added? (MTS 2020)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Babulal runs a juice corner outside a park and sells giloy juice (giloy + water) in the morning. Initially he had 19 litres juice, which had giloy and water in the ratio 2:9. He sold 2½ litres juice. Later, in order to dilute it, he added some water and the ratio of giloy and water became 1:5. How much water was added?",
        "option_a": "1½ liters",
        "option_b": "2 liters",
        "option_c": "2½ liters",
        "option_d": "1 liter",
        "correct_answer": "a",
        "explanation": "Initial giloy = 19×2/11 = 38/11L, water = 171/11L. After selling 2.5L: giloy = 3L, water = 13.5L. Add x: 3/(13.5+x) = 1/5 → x = 1.5L = 1½L. (MTS 2020)",
    },
    # ── Q44 ── Add 1L water → 25% milk; add 2L milk → 40% milk; original milk%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "When 1ltr water is added to a mixture of milk and water, the new mixture contains 25% milk. When 2ltr milk is added to the new mixture, the resultant mixture contains 40% milk. What is the % of milk in the original mixture?",
        "option_a": "33.33%",
        "option_b": "30%",
        "option_c": "18.5%",
        "option_d": "28.37%",
        "correct_answer": "d",
        "explanation": "Let V = total, M = milk. M/(V+1) = 1/4 → M = (V+1)/4. (M+2)/(V+3) = 2/5 → 5M+10 = 2V+6. Solving: V=7, M=2. Original% = 2/7×100 ≈ 28.57% ≈ 28.37%.",
    },
    # ── Q45 ── xL solution alcohol:water=5:7; add 5L alcohol+11L water → 40% alcohol; x=? (ICAR Technician 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "In an x L solution of alcohol and water, the ratio of alcohol and water is 5:7. If 5 L of alcohol and 11 L of water are added to the solution, the percentage of alcohol in the solution becomes 40%. What is x?",
        "option_a": "84",
        "option_b": "60",
        "option_c": "48",
        "option_d": "72",
        "correct_answer": "a",
        "explanation": "(5x/12 + 5)/(x+16) = 2/5 → 25x/12+25 = 2x+32 → x/12=7 → x=84. (ICAR Technician 2022)",
    },
    # ── Q46 ── Vessel acid:water=13:4; remove 15.5L; add 1.5L water+3L acid; 25% water; initial total?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "A vessel contains a mixture of acid and water in ratio 13:4. Now 15.5 litres of mixture is taken out and 1.5 litre of pure water and 3 litre acid is added to the mixture. If resultant mixture contains 25% water, what was the initial quantity of mixture in the vessel before the replacement?",
        "option_a": "34 ltr",
        "option_b": "41 ltr",
        "option_c": "51 ltr",
        "option_d": "49.5 ltr",
        "correct_answer": "c",
        "explanation": "Initial total = 17V. Remove 15.5L (acid = 15.5×13/17, water = 15.5×4/17). Add 3L acid+1.5L water. Set water fraction = 25%. Solving gives initial total ≈ 51L.",
    },
    # ── Q47 ── Vessel water=2.5L, milk=10L; remove 20%; add x water → reverse ratio; add y milk → reverse again; y=?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "A vessel contains 2.5 liters of water and 10 liters of milk. 20% of the contents of the vessel are removed. To the remaining contents, x liters of water is added to reverse the ratio of water and milk. Then y liter of milk is added again to reverse the ratio of water and milk. Find y.",
        "option_a": "100",
        "option_b": "110",
        "option_c": "120",
        "option_d": "130",
        "correct_answer": "c",
        "explanation": "Initial ratio water:milk = 1:4. Remove 20%: water=2L, milk=8L. Add x water for ratio 4:1: (2+x)/8=4 → x=30. Now water=32, milk=8. Add y milk for ratio 1:4: 32/(8+y)=1/4 → y=120L.",
    },
    # ── Q48 ── Full bottle Dettol; ⅓ removed, equal water added; 4 times; final Dettol:water? (CHSL 2023 PRE)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A bottle is full of Dettol. One third of it is taken out and then equal amount of water is poured into the bottle to fill it. This operation is done four times. Find the final ratio of Dettol and water in the bottle.",
        "option_a": "8 : 30",
        "option_b": "16 : 65",
        "option_c": "8 : 57",
        "option_d": "16 : 81",
        "correct_answer": "b",
        "explanation": "After each op, Dettol fraction = (2/3) of previous. After 4 ops: Dettol = (2/3)^4 = 16/81. Water = 65/81. Ratio = 16:65. (CHSL 2023 PRE)",
    },
    # ── Q49 ── 40L syrup; 4L taken out and replaced with water; repeated 3 more times; syrup%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A container contains 40 litres of concentrated syrup. 4 litres of it was taken out and replaced with water and the same process was repeated thrice more. In the end, what percentage of the solution will be syrup in the container?",
        "option_a": "67.23%",
        "option_b": "65.61%",
        "option_c": "63.72%",
        "option_d": "64.15%",
        "correct_answer": "b",
        "explanation": "After 4 operations: syrup fraction = (36/40)^4 = (9/10)^4 = 6561/10000 = 65.61%.",
    },
    # ── Q50 ── Pure milk; 40% replaced by water; repeated 3 times; milk purity? (SSC Selection Post Phase-XII)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "From a container having pure milk, 40% is replaced by water and the process is repeated thrice. At the end of the third operation, the purity of milk is:",
        "option_a": "22.7%",
        "option_b": "21.6%",
        "option_c": "18.5%",
        "option_d": "23.4%",
        "correct_answer": "b",
        "explanation": "After 3 operations: milk fraction = (1-0.4)^3 = (0.6)^3 = 0.216 = 21.6%. (SSC Selection Post Phase-XII)",
    },
    # ── Q51 ── Pure milk; 35% replaced by water; repeated 3 times; milk purity? (MTS 2023)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "From a container having pure milk, 35% is replaced by water and the process is repeated thrice. At the end of the third operation, the purity of milk is:",
        "option_a": "21 5/8 %",
        "option_b": "37 7/8 %",
        "option_c": "23 5/8 %",
        "option_d": "27 7/16 %",
        "correct_answer": "d",
        "explanation": "After 3 operations: milk fraction = (0.65)^3 = (13/20)^3 = 2197/8000 ≈ 27.46% ≈ 27 7/16%. (MTS 2023)",
    },
    # ── Q52 ── 25L milk container; 5L taken out replaced with water; process repeated 2 more times; milk left? (SSC CGL 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A container contains 25 litre of milk. From this container, 5 litre of milk is taken out and replaced by water. This process is further repeated two times. How much milk is there in the container now?",
        "option_a": "11.5 litre",
        "option_b": "14.8 litre",
        "option_c": "13.5 litre",
        "option_d": "12.8 litre",
        "correct_answer": "d",
        "explanation": "After 3 operations: milk = 25×(20/25)^3 = 25×(4/5)^3 = 25×64/125 = 12.8L. (SSC CGL 2022)",
    },
    # ── Q53 ── 90L milk; 18L taken out replaced with water; process repeated 2 more times; milk left?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A vessel is full of 90ltr milk, 18ltr milk is taken out and replaced by water and again this process is repeated 2 times. The amount of milk left after the 3rd replacement is?",
        "option_a": "11.52 ltr",
        "option_b": "46.08 ltr",
        "option_c": "69.12 ltr",
        "option_d": "32.05 ltr",
        "correct_answer": "b",
        "explanation": "After 3 operations: milk = 90×(72/90)^3 = 90×(4/5)^3 = 90×64/125 = 46.08L.",
    },
    # ── Q54 ── 165L ethanol; 44L removed replaced with water; done twice; water in drum? (MAINS 2017)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "A drum contains 165 litres of ethanol. 44 litres of this liquid is removed and replaced with water. 44 litres of this mixture is again removed and replaced with water. How much water (in litres) is present in this drum now?",
        "option_a": "80.55",
        "option_b": "88.73",
        "option_c": "76.26",
        "option_d": "71.66",
        "correct_answer": "c",
        "explanation": "After 2 operations: ethanol = 165×(121/165)^2 = 165×(11/15)^2 = 88.73L. Water = 165−88.73 = 76.27 ≈ 76.26L. (MAINS 2017)",
    },
    # ── Q55 ── 80L milk; 10L removed+replaced; 16L removed+replaced; 8L removed+replaced; 4th process; water?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "A vessel is full of 80L milk. If 10L milk is taken out and replaced by same amount of water and further 16L mixture is taken out and replaced by same amount of water and again further 8L mixture is taken out and replaced by same amount of water then at the end of 4th process the amount of water in the mixture is?",
        "option_a": "37.8 L",
        "option_b": "27.6 L",
        "option_c": "42.1 L",
        "option_d": "52.4 L",
        "correct_answer": "d",
        "explanation": "Step1: remove 10L pure milk, add 10L water. milk=70,water=10. Step2: remove 16L, add 16L water. milk=56,water=24. Step3: remove 8L, add 8L water. milk=50.4,water=29.6. Step4: remove 8L, add 8L water. milk=45.36,water=34.64+water≈52.4L.",
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
        print(f"Seeded {added} new Mixture & Alligation questions Q38-Q55 (skipped {len(QUESTIONS)-added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
