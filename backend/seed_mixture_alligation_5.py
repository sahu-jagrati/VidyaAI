"""
Mixture and Alligation questions — Gagan Pratap Maths (New Batch Q1–Q25).
Topic: "Mixture & Alligation" under Quantitative Aptitude.
Run: python seed_mixture_alligation_5.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from app.database.connection import SessionLocal
from app.models.question_model import Question

QUESTIONS = [
    # Q1 - Ratio of boys:girls NOT possible combined
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The ratio of boys and girls in class A is 2:5. Ratio of boys to girls in class B is 7:4. Which of the following cannot be the ratio of girls to boys in class A and B together?",
        "option_a": "5:8",
        "option_b": "7:15",
        "option_c": "1:1",
        "option_d": "4:5",
        "correct_answer": "b",
        "explanation": "Girls proportion in A = 5/7 ≈ 0.714, in B = 4/11 ≈ 0.364. Combined girls proportion must lie between 0.364 and 0.714. Option B: 7/22 ≈ 0.318 < 4/11, hence NOT possible.",
    },
    # Q2 - Coffee powder Rs.2500 and Rs.1500 → Rs.2250
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "In what ratio should coffee powder costing Rs.2500 per kg be mixed with coffee powder costing Rs.1500 per kg so that the cost of the mixture is Rs.2250 per kg?",
        "option_a": "1:4",
        "option_b": "4:1",
        "option_c": "3:1",
        "option_d": "1:3",
        "correct_answer": "c",
        "explanation": "By alligation: cheaper(1500):dearer(2500) = (2500-2250):(2250-1500) = 250:750 = 1:3. So Rs.2500:Rs.1500 = 3:1.",
    },
    # Q3 - Rice varieties Rs.128 and Rs.143 → Rs.137.75 (SSC MTS 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "In what ratio must a grocer mix two varieties of rice costing ₹128 and ₹143 per kg, respectively, to get a mixture of rice worth ₹137.75 per kg? (SSC MTS 2024)",
        "option_a": "5:4",
        "option_b": "7:13",
        "option_c": "3:1",
        "option_d": "6:7",
        "correct_answer": "b",
        "explanation": "By alligation: ₹128:₹143 = (143-137.75):(137.75-128) = 5.25:9.75 = 21:39 = 7:13.",
    },
    # Q4 - Tea Rs.72/kg and Rs.90/kg, sell Rs.99.6/kg for 20% gain
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "In what ratio should a grocer mix tea at Rs.72 per kg and Rs.90 per kg, so that by selling the mixture at Rs.99.6 per kg, he may gain 20%?",
        "option_a": "2:3",
        "option_b": "7:11",
        "option_c": "3:7",
        "option_d": "11:7",
        "correct_answer": "b",
        "explanation": "SP = Rs.99.6, gain 20%, CP = 99.6/1.2 = Rs.83/kg. By alligation: Rs.72:Rs.90 = (90-83):(83-72) = 7:11.",
    },
    # Q5 - Sugar Rs.83/kg and Rs.46/kg, sell Rs.80.3/kg for 46% profit
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "In what ratio should sugar costing Rs.83 per kg be mixed with sugar costing Rs.46 per kg so that by selling the mixture at Rs.80.3 per kg, there is a profit of 46%?",
        "option_a": "10:27",
        "option_b": "8:30",
        "option_c": "30:8",
        "option_d": "9:28",
        "correct_answer": "d",
        "explanation": "SP = Rs.80.3, profit 46%, CP = 80.3/1.46 = Rs.55/kg. By alligation: Rs.83:Rs.46 = (55-46):(83-55) = 9:28.",
    },
    # Q6 - 25% gain on sugar Rs.560 and Rs.280; 185 kg of Rs.280 mixed
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A 25% gain is made by selling the mixture of two types of sugar at Rs.450 per kg. If one type of sugar costing Rs.560 per kg was mixed with 185 kg of other type of sugar which costs Rs.280 per kg, how many kilograms of the former (Rs.560/kg) was mixed?",
        "option_a": "75",
        "option_b": "76",
        "option_c": "74",
        "option_d": "70",
        "correct_answer": "c",
        "explanation": "SP=450, gain 25%, CP=360. Alligation: Rs.560:Rs.280 = (360-280):(560-360) = 80:200 = 2:5. If 185 kg of Rs.280, then Rs.560 kg = 185×2/5 = 74 kg.",
    },
    # Q7 - Rice Rs.42/kg and Rs.50/kg, sell Rs.53.10 for 18% gain, 7.5 kg of Rs.50
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "How many kg of rice costing ₹42 per kg should be mixed with 7½ kg rice costing ₹50 per kg so that by selling the mixture at ₹53.10 per kg, there is a gain of 18%?",
        "option_a": "12½ kg",
        "option_b": "10 kg",
        "option_c": "9 kg",
        "option_d": "8 kg",
        "correct_answer": "a",
        "explanation": "SP=₹53.10, gain 18%, CP=53.10/1.18=₹45/kg. Alligation: ₹42:₹50=(50-45):(45-42)=5:3. If 7.5 kg of ₹50, then ₹42 kg = 7.5×5/3 = 12.5 kg.",
    },
    # Q8 - Raj 60gm mixture of X(Rs.80/5gm) and Y(Rs.80/10gm) → Rs.14/gm (SSC MTS 2024)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Raj prepares a 60 gm mixture by combining two ingredients X and Y. The cost of ingredient X is Rs.80 per 5 gm, and the cost of ingredient Y is Rs.80 per 10 gm. Ingredients X and Y are mixed in a manner that the cost of the resulting mixture is Rs.14 per gm. What is the quantity of ingredient X (in gm) in the mixture? (SSC MTS 2024)",
        "option_a": "30",
        "option_b": "15",
        "option_c": "45",
        "option_d": "60",
        "correct_answer": "c",
        "explanation": "Cost X=80/5=Rs.16/gm; Cost Y=80/10=Rs.8/gm. Let X=x gm: 16x+8(60-x)=14×60 → 8x=360 → x=45 gm.",
    },
    # Q9 - Trader 640kg rice, 20% profit / 5% loss, overall 15%
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A trader bought 640 kg of rice. He sold a part of rice at 20% profit and the rest at 5% loss. He earned a profit of 15% in the entire transaction. What is the quantity (in kg) of rice that he sold at 5% loss?",
        "option_a": "128",
        "option_b": "132",
        "option_c": "154",
        "option_d": "256",
        "correct_answer": "a",
        "explanation": "Alligation: 20% and -5%, mean 15%. Ratio at 20%:at 5%loss = (15-(-5)):(20-15) = 20:5 = 4:1. At 5% loss = 640×1/5 = 128 kg.",
    },
    # Q10 - Shopkeeper 100kg; 25kg at p%, 75kg at 8%, overall 10% profit
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A shopkeeper has 100 kg of rice. He sells 25 kg at some profit% and the remaining 75 kg at 8% profit. If he earns 10% profit on the whole transaction, then find at what % profit does he sell the 25 kg rice?",
        "option_a": "16%",
        "option_b": "20%",
        "option_c": "18%",
        "option_d": "14%",
        "correct_answer": "a",
        "explanation": "By weighted average: (25×p + 75×8)/100 = 10 → 25p + 600 = 1000 → p = 16%.",
    },
    # Q11 - Average cost pen tab Rs.2500, white board Rs.1200, combined Rs.2000; whiteboard % (DSSSB HEAD CLERK 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "The average cost of some pen tabs is Rs.2500 while the average cost of some white boards is Rs.1200. If the average cost of both the items (pen tab and white board) is Rs.2000, then find the percentage of number of white boards out of the total items (correct to two decimal places). (DSSSB HEAD CLERK 2022)",
        "option_a": "40.46%",
        "option_b": "39.46%",
        "option_c": "38.46%",
        "option_d": "35.46%",
        "correct_answer": "c",
        "explanation": "Alligation: whiteboard(1200):pen tab(2500) = (2500-2000):(2000-1200) = 500:800 = 5:8. Pen tabs:White boards = 8:5. White boards% = 5/13 × 100 = 38.46%.",
    },
    # Q12 - Rs.50000 on desktop (20% profit) and laptop (10% loss), overall 2% profit; find desktop price
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A person spent Rs.50000 on purchasing a desktop computer and a laptop computer. He sold the desktop at 20% profit and the laptop at 10% loss. If overall he made a 2% profit, then the purchase price (in Rs) of the desktop is:",
        "option_a": "Rs.20,000",
        "option_b": "Rs.25,000",
        "option_c": "Rs.24,000",
        "option_d": "Rs.18,000",
        "correct_answer": "a",
        "explanation": "Alligation: 20% and -10%, mean 2%. Desktop:Laptop = (2-(-10)):(20-2) = 12:18 = 2:3. Desktop = 50000×2/5 = Rs.20,000.",
    },
    # Q13 - Ramesh: table+chair=Rs.3900; table 8%/chair 16% profit; total profit Rs.540; find difference
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Ramesh purchases a table and a chair for Rs.3,900. He sells the table at a profit of 8% and the chair at a profit of 16%. He earns a profit of Rs.540. What is the difference between the original price of the table and the chair?",
        "option_a": "Rs.2,000",
        "option_b": "Rs.1,800",
        "option_c": "Rs.1,900",
        "option_d": "Rs.1,700",
        "correct_answer": "b",
        "explanation": "Let table=t, chair=3900-t. 0.08t + 0.16(3900-t) = 540 → -0.08t = -84 → t = Rs.1050. Chair = Rs.2850. Difference = 2850-1050 = Rs.1,800.",
    },
    # Q14 - Kewal: 5 tables + 13 chairs = Rs.14220; 15% profit / 10% loss; profit Rs.378; diff 2T vs 3C (SSC CGL)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "Kewal bought 5 tables and 13 chairs for a total of Rs.14220. He sold the tables at a profit of 15% and the chairs at a loss of 10%. If his profit in the entire transaction is Rs.378, then what is the difference (in Rs) between the cost price of 2 tables and the cost price of 3 chairs? (SSC CGL)",
        "option_a": "1260",
        "option_b": "1280",
        "option_c": "1250",
        "option_d": "1620",
        "correct_answer": "a",
        "explanation": "5T+13C=14220; 0.75T-1.3C=378. Solving: C=540, T=1440. 2 tables=2880, 3 chairs=1620. Difference = 2880-1620 = 1260.",
    },
    # Q15 - Two grain varieties Rs.202 and Rs.250 in ratio 1:7; cost per kg (MTS 2023)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "Two grain varieties worth Rs.202 per kg and Rs.250 per kg are mixed in the ratio 1:7. What is the cost (in Rs) of the resulting mixture per kg? (MTS 2023)",
        "option_a": "218",
        "option_b": "222",
        "option_c": "244",
        "option_d": "226",
        "correct_answer": "c",
        "explanation": "Weighted average = (1×202 + 7×250)/8 = (202+1750)/8 = 1952/8 = Rs.244/kg.",
    },
    # Q16 - Sri Ganesh: 40kg@Rs.12.50 + 25kg@Rs.15.10; sell for 10% profit
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Sri Ganesh bought 40 kg of wheat at Rs.12.50 per kg and 25 kg at Rs.15.10 per kg. He mixed them together. At what rate should he sell the mixture to earn 10% profit?",
        "option_a": "Rs.13.50",
        "option_b": "Rs.13.25",
        "option_c": "Rs.14.75",
        "option_d": "Rs.14.85",
        "correct_answer": "d",
        "explanation": "Total cost = 40×12.50 + 25×15.10 = 500+377.5 = 877.5. Total qty = 65 kg. CP/kg = 877.5/65 = 13.50. SP/kg = 13.50×1.10 = Rs.14.85.",
    },
    # Q17 - Three tea varieties Rs.108, Rs.120, Rs.x mixed 2:3:5; mix worth Rs.125/kg
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "Tea leaves worth Rs.108 per kg and Rs.120 per kg are mixed with a third variety in the ratio 2:3:5. If the mixture is worth Rs.125 per kg, find the price (rounded to nearest integer, in Rs) of the third variety of tea leaves per kg.",
        "option_a": "130",
        "option_b": "132",
        "option_c": "135",
        "option_d": "133",
        "correct_answer": "c",
        "explanation": "(2×108 + 3×120 + 5×x)/10 = 125 → 216+360+5x = 1250 → 5x = 674 → x = 134.8 ≈ Rs.135.",
    },
    # Q18 - Beer 750ml 9% alcohol + wine 500ml 14%; 2 bottles beer + 3 bottles wine; alcohol%?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "If a beer of 750 ml bottle has 9% alcohol and a wine bottle of 500 ml has 14% alcohol in it. If 2 bottles of beer and 3 bottles of wine are mixed together, then find the percentage of alcohol in the solution?",
        "option_a": "12.5%",
        "option_b": "12%",
        "option_c": "10.5%",
        "option_d": "11.5%",
        "correct_answer": "d",
        "explanation": "Alcohol = 2×750×0.09 + 3×500×0.14 = 135+210 = 345 ml. Total = 2×750+3×500 = 3000 ml. Alcohol% = 345/3000×100 = 11.5%.",
    },
    # Q19 - 80ml syrup chloroquine:hydroxychloroquine = 2:3; mixed with 120ml; resultant 38.5% chloroquine; find ratio in 120ml
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "hard", "phase": "main",
        "question_text": "In 80 ml of a syrup, chloroquine and hydroxychloroquine are in ratio of 2:3. This syrup is mixed with 120 ml of another syrup of chloroquine and hydroxychloroquine. In the resultant syrup, chloroquine is 38.5%. Find the ratio of chloroquine and hydroxychloroquine in the 120 ml syrup.",
        "option_a": "4:7",
        "option_b": "2:3",
        "option_c": "3:5",
        "option_d": "5:9",
        "correct_answer": "c",
        "explanation": "Chloroquine in 80ml = 80×2/5 = 32ml. Total = 200ml. Chloroquine total = 200×0.385 = 77ml. Chloroquine in 120ml = 77-32 = 45ml. Hydroxychloroquine = 75ml. Ratio = 45:75 = 3:5.",
    },
    # Q20 - Gold: 13-carat + 19-carat → 15-carat ornament; ratio?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A gold smith has two qualities of gold, one of 13 carats and another of 19 carats purity. In what proportion should he mix both to make an ornament of 15 carats purity?",
        "option_a": "1:3",
        "option_b": "2:1",
        "option_c": "3:2",
        "option_d": "1:2",
        "correct_answer": "b",
        "explanation": "By alligation: 13-carat:19-carat = (19-15):(15-13) = 4:2 = 2:1.",
    },
    # Q21 - Cow milk 10% fat + buffalo milk 20% fat; mixture = 120/7% fat; ratio?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "If a dairy mixes cow's milk which contains 10% fat with buffalo's milk which contains 20% fat, then the resulting mixture has fat (120/7)%. What ratio was the cow's milk mixed with buffalo's milk?",
        "option_a": "1:3",
        "option_b": "2:5",
        "option_c": "3:2",
        "option_d": "5:2",
        "correct_answer": "b",
        "explanation": "By alligation: cow(10):buffalo(20), mean=120/7. Cow:Buffalo = (20-120/7):(120/7-10) = (20/7):(50/7) = 2:5.",
    },
    # Q22 - Liquid1=1000gm/L, Liquid2=800gm/L; 0.5L of mix weighs 480gm; Liquid1 % by volume?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A chemist mixes two liquids 1 and 2. One litre of liquid 1 weighs 1 kg and one litre of liquid 2 weighs 800 gm. If half litre of the mixture weighs 480 gm, then the percentage of liquid 1 in the mixture, in terms of volume, is",
        "option_a": "70%",
        "option_b": "85%",
        "option_c": "75%",
        "option_d": "80%",
        "correct_answer": "d",
        "explanation": "1 litre of mixture weighs 960 gm. Alligation: L1(1000):L2(800), mean=960. L1:L2 = (960-800):(1000-960) = 160:40 = 4:1. L1% = 4/5×100 = 80%.",
    },
    # Q23 - Metal A=19× water, B=15× water; mix = 16× water; ratio A:B? (SSC CHSL PRE 2023)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "In an experiment, it was observed that metal A is 19 times heavier than water and metal B is 15 times heavier than water. In what ratio should metal A and B be mixed so that the mixture thus obtained is 16 times heavier than water? (SSC CHSL PRE 2023)",
        "option_a": "3:1",
        "option_b": "1:3",
        "option_c": "2:3",
        "option_d": "1:2",
        "correct_answer": "b",
        "explanation": "By alligation: A(19):B(15), mean=16. A:B = (16-15):(19-16) = 1:3.",
    },
    # Q24 - Solution A=10% acid, B=30% acid; mix for 25% acid; ratio A:B?
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "easy", "phase": "main",
        "question_text": "Solution A contains 10% acid and solution B contains 30% acid. In what ratio should solution A be mixed with solution B to obtain a mixture with 25% acid?",
        "option_a": "2:1",
        "option_b": "1:2",
        "option_c": "1:3",
        "option_d": "3:1",
        "correct_answer": "c",
        "explanation": "By alligation: A(10%):B(30%), mean=25%. A:B = (30-25):(25-10) = 5:15 = 1:3.",
    },
    # Q25 - H2SO4: 100ml at 20% + x ml at 50% = 30%; find x (SSC CGL 2022)
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant",
        "topic": "Mixture & Alligation", "difficulty": "medium", "phase": "main",
        "question_text": "A 100 ml solution of H₂SO₄ having concentration of 20% is mixed with a 50% concentrated x ml mixture such that the net mixture is 30% concentrated. Determine x. (SSC CGL 2022)",
        "option_a": "70 ml",
        "option_b": "80 ml",
        "option_c": "50 ml",
        "option_d": "60 ml",
        "correct_answer": "c",
        "explanation": "By alligation: 20% and 50%, mean=30%. 20%:50% = (50-30):(30-20) = 20:10 = 2:1. So 100:x = 2:1 → x = 50 ml.",
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
        print(f"Seeded {added} new Mixture & Alligation questions (new batch Q1-Q25) (skipped {len(QUESTIONS)-added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
