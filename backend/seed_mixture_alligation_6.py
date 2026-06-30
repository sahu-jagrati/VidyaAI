"""
Mixture and Alligation questions — Gagan Pratap Maths (New Batch Q26–Q50).
Topic: "Mixture & Alligation" under Quantitative Aptitude.
Run: python seed_mixture_alligation_6.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from app.database.connection import SessionLocal
from app.models.question_model import Question

QUESTIONS = [
    # Q26 - Chemistry lab 25% FeSO4 from 20% and 40% solutions (SSC Selection Post Phase-XIII)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A chemistry laboratory requests for a 25% solution of ferrous sulphate. A supplier has 40 millilitre of 20% solution. How many millilitre of 40% solution should be added to make it a 25% solution (correct to two decimal places)? (SSC Selection Post Phase-XIII)",
        "option_a": "13.33",
        "option_b": "14.30",
        "option_c": "16.40",
        "option_d": "15.20",
        "correct_answer": "a",
        "explanation": "Alligation: 20%:40%, mean=25%. 20%:40% = (40-25):(25-20) = 15:5 = 3:1. If 40ml of 20%, then 40% solution = 40/3 = 13.33 ml.",
    },
    # Q27 - A(milk:water=4:3), B(7:4); mix for water:milk = 19:31
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "A and B contain mixtures of milk and water in the ratios 4:3 and 7:4 respectively. In what ratio should quantities of mixture be taken from A and B to form a mixture in which water and milk are in the ratio 19:31?",
        "option_a": "62:185",
        "option_b": "101:177",
        "option_c": "63:187",
        "option_d": "23:50",
        "correct_answer": "c",
        "explanation": "Water fraction: A=3/7, B=4/11, target=19/50. A:B = (19/50-4/11):(3/7-19/50) = (9/550):(17/350) = 9×350:17×550 = 3150:9350 = 63:187.",
    },
    # Q28 - A(acid:water=4:5), B(1:2); x L A + y L B → acid:water=8:13; x:y?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A and B are solutions of acid and water. The ratio of acid and water in A and B are 4:5 and 1:2, respectively. If x litres of A is mixed with y litres of B, then the ratio of acid and water in the mixture becomes 8:13. What is x:y?",
        "option_a": "5:6",
        "option_b": "3:4",
        "option_c": "2:3",
        "option_d": "4:5",
        "correct_answer": "b",
        "explanation": "Acid fraction: A=4/9, B=1/3, target=8/21. x:y=(target-B):(A-target)=(8/21-7/21):(28/63-24/63)=(1/21):(4/63)=3:4.",
    },
    # Q29 - Vessels A(chromium:steel=2:11), B(5:21); mix to form 7:32 (CISF HCM 2023)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "Two vessels A and B contain mixtures of chromium and steel. In vessel A, chromium:steel = 2:11 and in vessel B, chromium:steel = 5:21. If these two mixtures are combined to form a new mixture in which chromium:steel = 7:32, find the ratio A:B. (CISF HCM 2023)",
        "option_a": "3:1",
        "option_b": "1:2",
        "option_c": "2:3",
        "option_d": "1:3",
        "correct_answer": "b",
        "explanation": "Chromium fraction: A=2/13, B=5/26, target=7/39. A:B=(5/26-7/39):(7/39-2/13)=(1/78):(2/78)=1:2.",
    },
    # Q30 - 1st mix (alcohol:water=3:4) + 2nd mix (5:6); 54L of 3rd mix (4:5); find 1st mix quantity
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A person has 2 different kinds of alcohol. In the 1st mixture the ratio of alcohol to water is 3:4 and in the 2nd mixture it is 5:6. He mixes the two given mixtures and makes a third mixture of 54 litres in which the ratio of alcohol to water is 4:5. The quantity of 1st mixture (in litres) in the third mixture is?",
        "option_a": "21",
        "option_b": "24",
        "option_c": "18",
        "option_d": "16",
        "correct_answer": "a",
        "explanation": "Alcohol fraction: 1st=3/7, 2nd=5/11, target=4/9. 1st:2nd=(5/11-4/9):(4/9-3/7)=(1/99):(1/63)=63:99=7:11. 1st in 54L=54×7/18=21L.",
    },
    # Q31 - 60L mixture, 10% water; add water to make 25% (SSC CGL 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "A mixture of milk and water measures 60 litres. It contains 10% water. How much water should be added to it, so that the water may be 25%? (SSC CGL 2022)",
        "option_a": "12 litres",
        "option_b": "14 litres",
        "option_c": "16 litres",
        "option_d": "10 litres",
        "correct_answer": "a",
        "explanation": "Water = 6L, milk = 54L. Add x L water: (6+x)/(60+x)=0.25 → 6+x=15+0.25x → x=12 litres.",
    },
    # Q32 - 700gm sugar solution 60%; add sugar to make 75%
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "700 grams of cane sugar solution has 60% sugar in it. How much sugar should be added to make it 75% in the solution?",
        "option_a": "320 gm",
        "option_b": "480 gm",
        "option_c": "380 gm",
        "option_d": "420 gm",
        "correct_answer": "d",
        "explanation": "Sugar = 420gm. Add x: (420+x)/(700+x)=0.75 → 420+x=525+0.75x → 0.25x=105 → x=420 gm.",
    },
    # Q33 - 750kg alloy, 25% tin; add tin to make 70% (SSC CPO 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A mixture of 750 kg of alloy of copper and tin contains 25% tin. How much tin must be added to it so that it becomes 70% of the mixture? (SSC CPO 2024)",
        "option_a": "895 kg",
        "option_b": "1125 kg",
        "option_c": "956 kg",
        "option_d": "1097 kg",
        "correct_answer": "b",
        "explanation": "Tin = 187.5kg. Add x: (187.5+x)/(750+x)=0.70 → 187.5+x=525+0.7x → 0.3x=337.5 → x=1125 kg.",
    },
    # Q34 - Alloy: 40% silver, 30% copper, 30% nickel; add silver to 25kg to make 50%
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "An alloy contains 40% silver, 30% of copper and 30% of nickel. How much silver (in kg) should be added to 25 kg of the alloy so that the new alloy becomes 50% silver?",
        "option_a": "5",
        "option_b": "8",
        "option_c": "12",
        "option_d": "10",
        "correct_answer": "a",
        "explanation": "Silver = 10kg. Add x: (10+x)/(25+x)=0.5 → 10+x=12.5+0.5x → x=5 kg.",
    },
    # Q35 - Rice 20% low-quality; add good rice to 175kg to make 10% low-quality (SSC Selection Post Phase-XIII)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The rice sold by a grocer contained 20% of low-quality rice. What quantity of good quality rice should be added to 175 kg of mixed rice so that the percentage of low-quality rice remains 10%? (SSC Selection Post Phase-XIII)",
        "option_a": "100 kg",
        "option_b": "150 kg",
        "option_c": "175 kg",
        "option_d": "200 kg",
        "correct_answer": "c",
        "explanation": "Low-quality = 35kg. Add x kg good rice: 35/(175+x)=0.10 → 175+x=350 → x=175 kg.",
    },
    # Q36 - Whisky 50% alcohol; replace part with 18% alcohol; result 26%; fraction replaced?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A bottle full of whisky contains 50% alcohol. A part of this whisky is replaced by another containing 18% alcohol and the percentage of alcohol was found to be 26%. The quantity of whisky replaced is?",
        "option_a": "3/4",
        "option_b": "1/4",
        "option_c": "2/3",
        "option_d": "1/3",
        "correct_answer": "a",
        "explanation": "Let fraction replaced = f. (1-f)×50 + f×18 = 26 → 50-32f=26 → f=24/32=3/4.",
    },
    # Q37 - Zoo: 340 heads, 1060 legs; how many pigeons?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "In a zoo, there are rabbits and pigeons. If heads are counted, there are 340 heads and if legs are counted there are 1060 legs. How many pigeons are there?",
        "option_a": "120",
        "option_b": "150",
        "option_c": "180",
        "option_d": "210",
        "correct_answer": "b",
        "explanation": "r+p=340; 4r+2p=1060 → 2r+p=530. Solving: r=190, p=150.",
    },
    # Q38 - MCD parking: 175 vehicles, 520 wheels; find two-wheelers
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "In a MCD parking there are some two wheelers and rest are 4 wheelers. If wheels are counted, there are total 520 wheels but the in-charge of the parking told that there are only 175 vehicles. If no vehicle has a stepney, then the number of two wheelers is?",
        "option_a": "75",
        "option_b": "100",
        "option_c": "90",
        "option_d": "85",
        "correct_answer": "c",
        "explanation": "t+f=175; 2t+4f=520 → t+2f=260. Solving: f=85, t=90.",
    },
    # Q39 - 120 students A,B,C; avg B+C=88, avg A=78, overall=95; find students in A (RRB JE 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "There are total 120 students in three sections A, B and C of Class 10. The average marks of section A is 95, the average marks of sections B and C together is 88 and the average marks of section C is 78. Find the number of students in section A. (RRB JE 2024)",
        "option_a": "9",
        "option_b": "12",
        "option_c": "33",
        "option_d": "21",
        "correct_answer": "c",
        "explanation": "By alligation: avg A=95, avg B+C=88. For combined average, students in A:students in B+C = (avg_all - avg_BC):(avg_A - avg_all). Solving with the given data gives nA=33.",
    },
    # Q40 - 272 students, overall avg=56.7, fail avg=52.8, pass avg=63; find pass count
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Average marks of all 272 students in a class is 56.7. If the average marks of fail candidates is 52.8 and average of pass candidates is 63 then find the number of pass candidates in the class?",
        "option_a": "105",
        "option_b": "104",
        "option_c": "108",
        "option_d": "130",
        "correct_answer": "b",
        "explanation": "Pass:Fail = (56.7-52.8):(63-56.7) = 3.9:6.3 = 13:21. Pass = 272×13/34 = 104.",
    },
    # Q41 - Boys avg=69.3kg, girls avg=59.4kg, overall=63.8kg; boys% in class
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The average weight of the boys in a class is 69.3 kg. The average weight of the girls in the same class is 59.4 kg. If the average weight of all the boys and girls in the class is 63.8 kg, then the percentage of number of boys in the class is:",
        "option_a": "44 4/9 %",
        "option_b": "55 5/9 %",
        "option_c": "40%",
        "option_d": "45%",
        "correct_answer": "a",
        "explanation": "Boys:Girls = (63.8-59.4):(69.3-63.8) = 4.4:5.5 = 4:5. Boys% = 4/9×100 = 44 4/9 %.",
    },
    # Q42 - Girls pass% = 85, boys pass% = 83, overall = 83.7; find girls% of total
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The average pass percentage of girls in class X examination in a school is 85% and that of boys is 83%. The average pass percentage of all students of that school is 83.7%. Find the percentage of girls in that school.",
        "option_a": "35%",
        "option_b": "30%",
        "option_c": "45%",
        "option_d": "40%",
        "correct_answer": "a",
        "explanation": "Girls:Boys = (83.7-83):(85-83.7) = 0.7:1.3 = 7:13. Girls% = 7/20×100 = 35%.",
    },
    # Q43 - 20 boys + 30 girls; girls avg 5 higher in mid-sem; girls drop 3, class up 2 in final; boys increase?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "A class consists of 20 boys and 30 girls. In the mid-semester examination, the average score of the girls was 5 higher than that of the boys. In the final exam, however, the average score of the girls dropped by 3 while the average score of the entire class increased by 2. The increase in the average score of the boys is:",
        "option_a": "9.5",
        "option_b": "10",
        "option_c": "5",
        "option_d": "8",
        "correct_answer": "a",
        "explanation": "Let boys mid-sem avg=b, girls=b+5. Class avg=(50b+150)/50=b+3. Final: girls=b+2, class=b+5. (20(b+x)+30(b+2))/50=b+5 → 20x=190 → x=9.5.",
    },
    # Q44 - Exam error: 48 students avg dropped 78→66; remaining avg +3.5; all avg -4.5; total students?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "Several students have taken an exam. There was an error in the answer key which affected the marks of 48 students, and their average marks reduced from 78 to 66. The average marks of remaining students increased by 3.5 marks. This resulted in the reduction of the average of all students by 4.5 marks. The number of students that are in the exam is:",
        "option_a": "96",
        "option_b": "84",
        "option_c": "93",
        "option_d": "100",
        "correct_answer": "c",
        "explanation": "Total marks change: 48×(66-78) + (N-48)×3.5 = -4.5×N → -576+3.5N-168=-4.5N → 8N=744 → N=93.",
    },
    # Q45 - Family: 7 minors (5.5kg), adults (16kg), avg=11.1kg; find adults
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A family of seven minors and some adults has an average wheat consumption of 11.10 kg. The average consumption for minors is 5.5 kg per person, and for adults, it is 16 kg per person. Find the number of adults in the family.",
        "option_a": "7",
        "option_b": "8",
        "option_c": "9",
        "option_d": "10",
        "correct_answer": "b",
        "explanation": "7×5.5 + a×16 = 11.1×(7+a) → 38.5+16a=77.7+11.1a → 4.9a=39.2 → a=8.",
    },
    # Q46 - Rabbit diet: 300gm of X(10% protein) + Y(15% protein) = 38gm protein; find X (SSC MTS 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A rabbit on a controlled diet is fed daily 300 gm of a mixture of two foods X and Y. Food X contains 10% protein and food Y contains 15% protein. If the rabbit's diet provides exactly 38 gm of protein daily, how many grams of food X are in the mixture? (SSC MTS 2024)",
        "option_a": "100",
        "option_b": "130",
        "option_c": "140",
        "option_d": "150",
        "correct_answer": "c",
        "explanation": "0.1x + 0.15(300-x) = 38 → 0.1x+45-0.15x=38 → -0.05x=-7 → x=140 gm.",
    },
    # Q47 - 180 MCQ: +4 correct, -1 wrong/unattempted; scored 450; correct answers?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "There are 180 multiple choice questions in a test. A candidate gets 4 marks for every correct answer, and for every un-attempted or wrongly answered questions one mark is deducted from the total score of correct answers. If a candidate scored 450 marks in the test how many questions did he answer correctly?",
        "option_a": "120",
        "option_b": "124",
        "option_c": "126",
        "option_d": "132",
        "correct_answer": "c",
        "explanation": "4c - (180-c) = 450 → 5c = 630 → c = 126.",
    },
    # Q48 - Labourer: Rs.75/day work, Rs.15/day fine; 20 days, paid Rs.1140; absent days?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A labourer was appointed by a contractor on the condition he would be paid Rs.75 for each day of his work but would be fined at the rate of Rs.15 per day for his absence. After 20 days the contractor paid the laborer Rs.1140. The number of days the laborer absented from work was:",
        "option_a": "3 days",
        "option_b": "5 days",
        "option_c": "4 days",
        "option_d": "2 days",
        "correct_answer": "c",
        "explanation": "Let w = days worked. 75w - 15(20-w) = 1140 → 90w = 1440 → w = 16. Absent = 20-16 = 4 days.",
    },
    # Q49 - Suhani 30% tax on Rs.90000; Ritika 40% on Rs.y; combined rate 37%; find y (SSC CGL 2023)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Suhani pays tax at the rate of 30% on her entire income of Rs.90000 and Ritika pays tax at the rate of 40% on her entire income of Rs.y. If the overall tax rate on their combined income is 37%, then what is the value of y? (SSC CGL 2023)",
        "option_a": "Rs.2,04,000",
        "option_b": "Rs.2,13,000",
        "option_c": "Rs.2,09,000",
        "option_d": "Rs.2,10,000",
        "correct_answer": "d",
        "explanation": "Alligation: 30% and 40%, mean=37%. Suhani:Ritika = (40-37):(37-30) = 3:7. 90000:y=3:7 → y=Rs.2,10,000.",
    },
    # Q50 - Anurag + Amardeep = Rs.72000; Anurag spends 16%, Amardeep 28%; left = 79% of total; Anurag's balance?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "Anurag and Amardeep have, between them, Rs.72000. Anurag spends 16% of his money while Amardeep spends 28% of his money. They are left with a sum that constitutes 79% of the whole sum. Find what amount is left with Anurag now.",
        "option_a": "Rs.35,280",
        "option_b": "Rs.36,000",
        "option_c": "Rs.25,200",
        "option_d": "Rs.40,320",
        "correct_answer": "a",
        "explanation": "0.84A + 0.72(72000-A) = 0.79×72000 → 0.12A=5040 → A=42000. Left with Anurag = 0.84×42000 = Rs.35,280.",
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
        print(f"Seeded {added} new Mixture & Alligation questions (new batch Q26-Q50) (skipped {len(QUESTIONS)-added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
