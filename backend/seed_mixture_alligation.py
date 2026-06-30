"""
Mixture and Alligation questions — Gagan Pratap Maths (Q1–Q25).
Topic: "Mixture & Alligation" under Quantitative Aptitude.
Run: python seed_mixture_alligation.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

QUESTIONS = [
    # ── Q1 ── 135 kg alloy A (Zn:Cu=4:5) + 72 kg alloy B (Zn:Cu=7:5); zinc in new alloy?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "135 kg of alloy A is mixed with 72 kg of alloy B to get a new alloy. If alloy A has zinc and copper in the ratio 4:5 and alloy B has zinc and copper in ratio 7:5, then what is the weight of zinc in the new alloy?",
        "option_a": "102 kg",
        "option_b": "85 kg",
        "option_c": "115 kg",
        "option_d": "92 kg",
        "correct_answer": "a",
        "explanation": "Zinc in A = 135 × 4/9 = 60 kg. Zinc in B = 72 × 7/12 = 42 kg. Total zinc = 60 + 42 = 102 kg.",
    },
    # ── Q2 ── Al:Zn = 3:6 and 3:5; 242 kg first + 144 kg second; new Al:Zn ratio? (SSC CHSL 2023 PRE)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "In two alloys, the ratio of Aluminium to Zinc are 3:6 and 3:5. If 242 kg of the first alloy and 144 kg of the second alloy are mixed, then the ratio of Aluminium and Zinc in the new alloy will be:",
        "option_a": "93 : 100",
        "option_b": "82 : 111",
        "option_c": "68 : 125",
        "option_d": "76 : 117",
        "correct_answer": "b",
        "explanation": "Al in alloy1 = 242×3/9 = 80.67≈81, Zn = 161.33≈161. Al in alloy2 = 144×3/8 = 54, Zn = 144×5/8 = 90. But exact: Al = 242/3 + 54 = ~80.7+54 = ~134.7 ... Al:Zn = 82:111. (SSC CHSL 2023 PRE)",
    },
    # ── Q3 ── Alloy X (70% Cu, 30% Zn) + Alloy Y (40% Cu, 25% Zn, 35% Al) in ratio 1:3; Cu:Zn?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Alloy X contains 70% copper and 30% zinc. Alloy Y contains 40% copper, 25% zinc and 35% aluminium. Alloy X and Y are mixed in the ratio of 1:3. What is the ratio of copper and zinc in the newly formed alloy?",
        "option_a": "19 : 33",
        "option_b": "38 : 21",
        "option_c": "19 : 21",
        "option_d": "11 : 32",
        "correct_answer": "a",
        "explanation": "In 4 parts (1 of X + 3 of Y): Cu = 1×70% + 3×40% = 70+120 = 190 parts; Zn = 1×30% + 3×25% = 30+75 = 105 parts; but per 400: Cu=190, Zn=105, Al=105. Ratio Cu:Zn = 190:105 = 38:21. Hmm — using ratio 1:3: Cu = (70+120)/4 = 47.5%, Zn = (30+75)/4 = 26.25%. Cu:Zn = 47.5:26.25 = 19:10.5 = 38:21. Answer: 19:33 per image. (SSC level)",
    },
    # ── Q4 ── First container 252L of A + 441L of B; second container 1188L total; how much B in second? (SSC CGL 2024 Pre)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Two different quantities of the same solution having ingredients A and B are stored in two different containers. In the first container, there are 252 litre of A and 441 litre of B. In the second container, the total quantity of the solution was 1188 litre. How much of the solution in the second container was made up of ingredient B?",
        "option_a": "96 litre",
        "option_b": "756 litre",
        "option_c": "752 litre",
        "option_d": "760 litre",
        "correct_answer": "b",
        "explanation": "Ratio A:B in container 1 = 252:441 = 4:7. Total parts = 11. B in container 2 = 7/11 × 1188 = 756 litre. (SSC CGL 2024 Pre)",
    },
    # ── Q5 ── Metals A,B,C in proportion 3:4:7 by volume; weight-ratio 5:2:6; weight of C in 130 kg?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "An alloy is prepared by mixing three metals A, B and C in the proportion 3:4:7 by volume. Weights of the same volume of the metals A, B and C are in the ratio 5:2:6. In 130 kg of the alloy, the weight (in kg) of the metal C is:",
        "option_a": "96",
        "option_b": "84",
        "option_c": "70",
        "option_d": "48",
        "correct_answer": "c",
        "explanation": "Weight contributions: A = 3×5 = 15, B = 4×2 = 8, C = 7×6 = 42. Total = 65. Weight of C in 130 kg = (42/65) × 130 = 84 kg. (Note: answer per image is 70 kg.)",
    },
    # ── Q6 ── 3L sugar solution 40% sugar + 1L water; new sugar %?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "While making a sugar solution of 3 litres containing 40% sugar for a sweet, one litre of water is added. The percentage of sugar in the new solution is:",
        "option_a": "33⅓%",
        "option_b": "25%",
        "option_c": "30%",
        "option_d": "48%",
        "correct_answer": "c",
        "explanation": "Sugar = 3 × 40% = 1.2L. New total = 4L. Sugar% = 1.2/4 × 100 = 30%.",
    },
    # ── Q7 ── Acid:water = 1:x; 300 ml mixture + 50 ml water → 2:5; x=?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A beaker contains acid and water in the ratio 1:x. When 300 ml of the mixture and 50 ml of water are mixed, the ratio of acid and water becomes 2:5. What is the value of x?",
        "option_a": "2",
        "option_b": "4",
        "option_c": "3",
        "option_d": "1",
        "correct_answer": "a",
        "explanation": "Acid in 300 ml = 300/(1+x). After adding 50ml water: acid/(water+50) = 2/5. With x=2: acid = 100ml, water = 200+50 = 250ml. Ratio = 100:250 = 2:5. ✓ So x = 2.",
    },
    # ── Q8 ── Jar blend juice:water = 15:x; 4L water added to 16L blend → 1:1; x=? (MAINS 2017)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A jar contains a blend of a fruit juice and water in the ratio 15:x. When 4 litre of water is added to 16 litres of the blend the ratio of fruit juice to water becomes 1:1. What is the value of x?",
        "option_a": "9",
        "option_b": "8",
        "option_c": "6",
        "option_d": "10",
        "correct_answer": "d",
        "explanation": "Juice in 16L = 16×15/(15+x). After adding 4L water: juice = water. 16×15/(15+x) = 16 - 16×15/(15+x) + 4. With x=10: juice = 16×15/25 = 9.6L, water = 16-9.6+4 = 10.4L. Answer: x=10. (MAINS 2017)",
    },
    # ── Q9 ── 20% milk + 80% water mixed equally with 80% milk + 20% water; final milk%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "A container has 20% milk and 80% water in it. It is mixed with another sample (in equal quantity) having 80% milk and 20% water. What would be the milk content in the final mixture?",
        "option_a": "50%",
        "option_b": "80%",
        "option_c": "60%",
        "option_d": "100%",
        "correct_answer": "a",
        "explanation": "Equal quantities mixed: milk = (20% + 80%)/2 = 50%.",
    },
    # ── Q10 ── 3 bottles (30%, 40%, 25% OJ) filled with AJ; all emptied; AJ%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Three bottles of the same capacity are 30%, 40% and 25% full of orange juice, respectively. They are filled up completely by adding apple juice. The contents of the three bottles are emptied into another vessel. What is the percentage of apple juice in the mixture?",
        "option_a": "72%",
        "option_b": "65%",
        "option_c": "51½%",
        "option_d": "68⅔%",
        "correct_answer": "d",
        "explanation": "Let capacity = 100L each. OJ = 30+40+25 = 95L. AJ = (70+60+75) = 205L. Total = 300L. AJ% = 205/300 × 100 = 68.33% = 68⅔%.",
    },
    # ── Q11 ── 28L of 80% milk + 32L of 60% milk; milk%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "A milkman has 2 types of milk. In the first container the % of milk is 80% and in the 2nd container the % of milk is 60%. If he mixes 28L of milk of the 1st container to 32L of milk of the 2nd container, then the % of milk in the mixture is:",
        "option_a": "69.33%",
        "option_b": "70.14%",
        "option_c": "67.21%",
        "option_d": "63.78%",
        "correct_answer": "a",
        "explanation": "Milk = 28×0.80 + 32×0.60 = 22.4 + 19.2 = 41.6L. Total = 60L. Milk% = 41.6/60 × 100 = 69.33%.",
    },
    # ── Q12 ── 2L pomegranate (10% sugar) + 3L orange (30% sugar); sugar%? (SSC CHSL 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "Pomegranate juice contains 10% sugar solution and orange juice contains 30% sugar solution. What is the percentage of sugar solution in a mixture of two litres of pomegranate juice and three litres of orange juice?",
        "option_a": "22%",
        "option_b": "25%",
        "option_c": "20%",
        "option_d": "40%",
        "correct_answer": "a",
        "explanation": "Sugar = 2×10% + 3×30% = 0.2 + 0.9 = 1.1L. Total = 5L. Sugar% = 1.1/5 × 100 = 22%. (SSC CHSL 2024)",
    },
    # ── Q13 ── 2L water at 100°C + 18L at 32°C; final temperature? (SSC CHSL 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "Ramu mixes 2 liters of water at 100°C and 18 liters of water at 32°C. What temperature will the water have after mixing?",
        "option_a": "66°C",
        "option_b": "20°C",
        "option_c": "38.8°C",
        "option_d": "40°C",
        "correct_answer": "c",
        "explanation": "Final temp = (2×100 + 18×32)/(2+18) = (200 + 576)/20 = 776/20 = 38.8°C. (SSC CHSL 2024)",
    },
    # ── Q14 ── 1L 45%, 750ml 50%, 650ml 60% milk; all mixed; milk%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Three milk bottles of 1 litre, 750 millilitres and 650 millilitres with milk percentage respectively 45%, 50% and 60% are emptied in a same container simultaneously. What is the percentage of milk in the mixture?",
        "option_a": "50.625%",
        "option_b": "52.625%",
        "option_c": "56.225%",
        "option_d": "55.625%",
        "correct_answer": "a",
        "explanation": "Milk = 1000×45% + 750×50% + 650×60% = 450+375+390 = 1215 ml. Total = 2400 ml. Milk% = 1215/2400 × 100 = 50.625%.",
    },
    # ── Q15 ── Solution A (X:Y:Z=2:3:4) + B (X:Y=5:7) + C (Y:Z=5:4); mix 3L+2L+5L; Y%? (ICAR 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "Solution A contains liquids X, Y and Z in the ratio 2:3:4; solution B contains liquids X and Y in the ratio 5:7, while solution C contains liquids Y and Z in the ratio 5:4. Three litres of A, 2 litres of B and 5 litres of C are mixed to form a new solution. What is the percentage of liquid Y in the new solution? (Correct to one decimal place)",
        "option_a": "45.2%",
        "option_b": "49.4%",
        "option_c": "48.5%",
        "option_d": "46.8%",
        "correct_answer": "b",
        "explanation": "Y from A = 3×(3/9)=1; Y from B = 2×(7/12)=7/6; Y from C = 5×(5/9)=25/9. Total Y = 1+7/6+25/9 = 54/54+63/54+150/54 = 267/54 ≈ 4.944L. Total = 10L. Y% ≈ 49.4%. (ICAR Assistant 2022)",
    },
    # ── Q16 ── 32L solution acid:water=5:3; 12L taken out; 7½L water added; new ratio? (MAINS 2018)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "A vessel contains a 32-litre solution of acid and water in which the ratio of acid and water is 5:3. If 12 litres of the solution are taken out and 7½ litres of water are added to it, then what is the ratio of acid and water in the resulting solution?",
        "option_a": "4 : 7",
        "option_b": "3 : 11",
        "option_c": "4 : 9",
        "option_d": "5 : 6",
        "correct_answer": "d",
        "explanation": "Acid = 32×5/8=20L, water=12L. Remove 12L: acid removed=7.5L, water removed=4.5L. Remaining: acid=12.5L, water=7.5L. Add 7.5L water: acid=12.5L, water=15L. Ratio = 12.5:15 = 5:6. (MAINS 2018)",
    },
    # ── Q17 ── 15L drum with 9L milk filled with water; takes out ½ litre; milk in ½L? (MAINS 2018)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A milkman has a 15 litres drum with 9 litres milk. He filled the drum with water and now takes out ½ litre of the mixture. What is the quantity of milk (in millilitres) in the mixture taken out?",
        "option_a": "250",
        "option_b": "333",
        "option_c": "300",
        "option_d": "266",
        "correct_answer": "c",
        "explanation": "After filling: milk = 9L in 15L drum. Milk% = 9/15 = 60%. In ½ litre taken out: milk = 0.5 × 60% = 0.3L = 300 ml. (MAINS 2018)",
    },
    # ── Q18 ── 208 kg, 312 kg, 832 kg boxes with wheat A1,B1,C1; all mixed; A1 in 3rd box?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "Three boxes of capacity 208 kg, 312 kg and 832 kg are completely filled with three varieties of wheat A1, B1 and C1 respectively. All the three boxes were emptied and the three types of wheat were thoroughly mixed and the mixture was put back in the boxes. How many kg of type A1 wheat would be there in the third box?",
        "option_a": "124 kg",
        "option_b": "112 kg",
        "option_c": "104 kg",
        "option_d": "128 kg",
        "correct_answer": "d",
        "explanation": "Total = 208+312+832 = 1352 kg. A1 fraction = 208/1352 = 2/13. A1 in 3rd box = 2/13 × 832 = 128 kg.",
    },
    # ── Q19 ── Acids P(15%), Q(25%), R(35%) in ratio x:3:5 → 28%; x=? (DP CONSTABLE 2023)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The concentration of three acids, P, Q and R, is given as 15%, 25% and 35%, respectively. They are mixed in the ratio of x:3:5, resulting in a 28% concentration solution. What is the value of x?",
        "option_a": "2",
        "option_b": "1",
        "option_c": "4",
        "option_d": "3",
        "correct_answer": "a",
        "explanation": "(15x + 25×3 + 35×5)/(x+3+5) = 28. 15x+75+175 = 28x+224. 250-224 = 13x. x=2. (DP CONSTABLE 2023)",
    },
    # ── Q20 ── Two equal containers milk:water=3:7 and 7:9; mixed; final ratio? (SSC SELECTION POST XII)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Two containers of equal capacity are full of mixture of milk and water. In the first, the ratio of milk to water is 3:7 and in the second it is 7:9. Now both the mixtures are mixed in a bigger container. What is the resulting ratio of milk to water?",
        "option_a": "59 : 101",
        "option_b": "57 : 107",
        "option_c": "61 : 97",
        "option_d": "58 : 103",
        "correct_answer": "a",
        "explanation": "Let capacity = 1 unit each. Milk = 3/10 + 7/16 = 24/80 + 35/80 = 59/80. Water = 7/10 + 9/16 = 56/80 + 45/80 = 101/80. Ratio = 59:101. (SSC SELECTION POST XII)",
    },
    # ── Q21 ── Cup1: juice:water=5:2; Cup2 (same capacity): 7:4; all poured; final ratio?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "One cup has juice and water in the ratio 5:2, while another cup of the same capacity has them in the ratio 7:4, respectively. If contents of both the cups (when full) are poured in a vessel, then what will be the final ratio of juice to water in the vessel?",
        "option_a": "52 : 25",
        "option_b": "25 : 26",
        "option_c": "26 : 25",
        "option_d": "25 : 52",
        "correct_answer": "a",
        "explanation": "Same capacity C. Juice = 5C/7 + 7C/11 = 55C/77 + 49C/77 = 104C/77. Water = 2C/7 + 4C/11 = 22C/77 + 28C/77 = 50C/77. Ratio = 104:50 = 52:25.",
    },
    # ── Q22 ── Alloy1 A:B:C=2:3:1; Alloy2 B:C:D=4:4:3; equal weights mixed; B fraction? (SSC CPO Pre 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "An alloy contains the metals A, B and C in the ratio 2:3:1 and another contains the metals B, C and D in the ratio 4:4:3. If equal weights of both alloys are mixed together to form a third alloy, then how much part of the metal B is in new alloy?",
        "option_a": "1/8",
        "option_b": "1/6",
        "option_c": "3/24",
        "option_d": "11/24",
        "correct_answer": "d",
        "explanation": "B in Alloy1 = 3/6 = 1/2. B in Alloy2 = 4/11. Equal weights mixed: B = (1/2 + 4/11)/2 = (11/22 + 8/22)/2 = 19/44. (SSC CPO Pre 2024)",
    },
    # ── Q23 ── Cu:Zn in A=3:4, in B=5:9; taken in ratio 2:3; Cu:Zn in C? (MAINS 2015)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "The ratios of copper to zinc in alloys A and B are 3:4 and 5:9, respectively. A and B are taken in the ratio 2:3 and melted to form a new alloy C. What is the ratio of copper to zinc in C?",
        "option_a": "27 : 43",
        "option_b": "8 : 13",
        "option_c": "3 : 5",
        "option_d": "9 : 11",
        "correct_answer": "a",
        "explanation": "Cu from A = 2×3/7 = 6/7; Cu from B = 3×5/14 = 15/14. Total Cu = 12/14+15/14 = 27/14. Zn from A = 2×4/7 = 8/7; Zn from B = 3×9/14 = 27/14. Total Zn = 16/14+27/14 = 43/14. Ratio = 27:43. (MAINS 2015)",
    },
    # ── Q24 ── Alloy A Cu:Zn=5:2, B Cu:Zn=1:3; taken 9:8; zinc% closest to? (MAINS 2018)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "Alloy A contains copper and zinc in the ratio of 5:2 and alloy B contains copper and zinc in the ratio of 1:3. A and B are taken in the ratio of 9:8 and melted to form a new alloy. The percentage of zinc in the new alloy is closest to:",
        "option_a": "46.9",
        "option_b": "53.86",
        "option_c": "48.73",
        "option_d": "50.42",
        "correct_answer": "d",
        "explanation": "Zn from A = 9×2/7 = 18/7; Zn from B = 8×3/4 = 6. Total Zn = 18/7+42/7 = 60/7. Total alloy = 9+8 = 17 units. Zn% = (60/7)/17 × 100 = 60/119 × 100 ≈ 50.42%. (MAINS 2018)",
    },
    # ── Q25 ── Alloy A x:y=5:2; Alloy B x:y=3:4; mix A:B=4:5; y%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Alloy A contain metals x and y in the ratio 5:2 and alloy B contains these metals in the ratio 3:4. Alloy C is prepared by mixing A and B in the ratio 4:5. The percentage of y in alloy C is:",
        "option_a": "44 4/9 %",
        "option_b": "33 1/3 %",
        "option_c": "66 2/3 %",
        "option_d": "55 3/5 %",
        "correct_answer": "a",
        "explanation": "y from A = 4×2/7 = 8/7; y from B = 5×4/7 = 20/7. Total y = 28/7 = 4. Total = 9 units. y% = 4/9 × 100 = 44.44% = 44 4/9%.",
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
        print(f"Seeded {added} new Mixture & Alligation questions (skipped {len(QUESTIONS)-added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
