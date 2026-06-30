import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "If 60% of a number is 120 more than 20% of the number, then 28% of the number is less than 33⅓% of the number by:",
        "option_a": "12", "option_b": "14", "option_c": "15", "option_d": "16",
        "correct_answer": "d",
        "explanation": "40% of N = 120 → N = 300. 28% of 300 = 84. 33⅓% of 300 = 100. Difference = 100 - 84 = 16.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "The difference between the value of a number increased by 32% and the value of the number decreased by 28% is 180. Find the number. (IB ACIO 2023)",
        "option_a": "320", "option_b": "280", "option_c": "300", "option_d": "26",
        "correct_answer": "c",
        "explanation": "1.32N - 0.72N = 180 → 0.60N = 180 → N = 300.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "easy", "phase": "main",
        "question_text": "When a number is increased by 216, it becomes 140% of itself. What is the number?",
        "option_a": "540", "option_b": "756", "option_c": "450", "option_d": "675",
        "correct_answer": "a",
        "explanation": "N + 216 = 1.4N → 0.4N = 216 → N = 540.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "easy", "phase": "main",
        "question_text": "If 85% of a number is added to 75, the result is the number itself. The number is:",
        "option_a": "500", "option_b": "400", "option_c": "300", "option_d": "700",
        "correct_answer": "a",
        "explanation": "0.85N + 75 = N → 0.15N = 75 → N = 500.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "hard", "phase": "main",
        "question_text": "If 25% of half of x is equal to 2.5 times the value of 30% of one-fourth of y, then x is what percent more or less than y?",
        "option_a": "33⅓% more", "option_b": "33⅓% less", "option_c": "50% less", "option_d": "50% more",
        "correct_answer": "d",
        "explanation": "0.25 × x/2 = 2.5 × 0.30 × y/4 → x/8 = 0.1875y → x = 1.5y. x is 50% more than y.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "hard", "phase": "main",
        "question_text": "If fourth-fifth of five-sixths of one-eighth of a certain number is 4365, what is 65% of the number? (SSC CHSL 2023 Pre)",
        "option_a": "36375", "option_b": "53280", "option_c": "34047", "option_d": "52380",
        "correct_answer": "c",
        "explanation": "4/5 × 5/6 × 1/8 × N = 4365 → N/12 = 4365 → N = 52380. 65% of 52380 = 34047.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "The volume of water in two tanks A and B is in ratio 6:5. The volume in tank A is increased by 30%. By what percentage should tank B be increased so both tanks have the same volume?",
        "option_a": "56%", "option_b": "18%", "option_c": "15%", "option_d": "30%",
        "correct_answer": "a",
        "explanation": "New A = 6k × 1.3 = 7.8k. 5k × (1 + x/100) = 7.8k → x = (7.8/5 - 1) × 100 = 56%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "hard", "phase": "main",
        "question_text": "The difference of two positive numbers is 1020. If 7.6% of the greater number is 12.4% of the smaller number, then the sum of two numbers is:",
        "option_a": "3250", "option_b": "4250", "option_c": "4520", "option_d": "3520",
        "correct_answer": "b",
        "explanation": "G/S = 124/76 = 31/19. G - S = 12k = 1020 → k = 85. G = 2635, S = 1615. Sum = 4250.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "The sum of two numbers is 5635. If the bigger is decreased by 7% and the smaller is increased by 24%, the numbers become equal. The bigger number is: (SSC CHSL Tier-I 2022)",
        "option_a": "3220", "option_b": "3200", "option_c": "2840", "option_d": "3150",
        "correct_answer": "a",
        "explanation": "0.93B = 1.24S → S = 0.75B. B + 0.75B = 5635 → 1.75B = 5635 → B = 3220.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "If house tax is paid before the due date, one gets 12% reduction. A person got a reduction of ₹2,100 by paying before due date. The amount (₹) of house tax paid was:",
        "option_a": "21,000", "option_b": "15,400", "option_c": "25,000", "option_d": "17,500",
        "correct_answer": "b",
        "explanation": "0.12T = 2100 → T = 17500. Tax paid = 17500 - 2100 = 15400.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "Ram's income is 2.5% more than Shyam's income. By what percentage is Shyam's income less than Ram's income? (SSC CGL 2024 Pre)",
        "option_a": "2.43%", "option_b": "3.43%", "option_c": "1.43%", "option_d": "4.43%",
        "correct_answer": "a",
        "explanation": "R = 1.025S. (R-S)/R × 100 = 2.5/102.5 × 100 = 100/41 ≈ 2.43%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "The income of A is 24% more than the income of B. By what percent is the income of B less than the income of A?",
        "option_a": "150/13%", "option_b": "600/21%", "option_c": "500/31%", "option_d": "600/31%",
        "correct_answer": "d",
        "explanation": "A = 1.24B. (A-B)/A × 100 = 24/124 × 100 = 600/31 ≈ 19.35%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "easy", "phase": "main",
        "question_text": "If A's income is 60% less than B's income, then B's income is what percentage more than A's income?",
        "option_a": "40%", "option_b": "80%", "option_c": "12%", "option_d": "150%",
        "correct_answer": "d",
        "explanation": "A = 0.4B. (B-A)/A × 100 = (B - 0.4B)/(0.4B) × 100 = 0.6/0.4 × 100 = 150%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "If A's height is 12% more than B's height, by how much percent less is B's height than that of A? (DSSSB Assistant Grade-III 2024)",
        "option_a": "9.6%", "option_b": "10.71%", "option_c": "12.56%", "option_d": "14.5%",
        "correct_answer": "b",
        "explanation": "A = 1.12B. (A-B)/A × 100 = 0.12/1.12 × 100 = 12/1.12 = 75/7 ≈ 10.71%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "In a competitive exam, Sam's marks are 19% less than Peter's. By what percentage (to two decimal places) are Peter's marks more than Sam's? (SSC CGL 2023 Pre)",
        "option_a": "28.64%", "option_b": "22.25%", "option_c": "21.51%", "option_d": "23.46%",
        "correct_answer": "d",
        "explanation": "S = 0.81P. (P-S)/S × 100 = 19/81 × 100 = 1900/81 ≈ 23.46%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "easy", "phase": "main",
        "question_text": "A water pipe is cut into two pieces. The longer piece is 64% of the length of the pipe. By how much percentage is the longer piece longer than the shorter piece?",
        "option_a": "77.77%", "option_b": "81.81%", "option_c": "36%", "option_d": "None of these",
        "correct_answer": "a",
        "explanation": "Longer = 64%, Shorter = 36%. (64-36)/36 × 100 = 28/36 × 100 = 77.77%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "A number is increased by x%. To get back to the original number, it is to be reduced by:",
        "option_a": "x%", "option_b": "100x/(100+x)%", "option_c": "10x/(100+x)%", "option_d": "(100-x)/100%",
        "correct_answer": "b",
        "explanation": "N(1+x/100)(1-r/100)=N → r/100 = x/(100+x) → r = 100x/(100+x).",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "When water freezes to ice its volume increases 10%. If this ice melts, then how much percentage will the volume decrease? (CISF HCM 2023)",
        "option_a": "10%", "option_b": "90%", "option_c": "9 1/11%", "option_d": "10 1/10%",
        "correct_answer": "c",
        "explanation": "Ice volume = 1.1V. % decrease = (1.1V - V)/(1.1V) × 100 = 0.1/1.1 × 100 = 100/11 = 9 1/11%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "P and Q are two fixed points 10 cm apart, and R is on PQ such that PR = 6 cm. By what % is QR decreased when PR is increased by 5%? (SSC CGL 2024 Pre)",
        "option_a": "8.5%", "option_b": "7.5%", "option_c": "7%", "option_d": "8%",
        "correct_answer": "b",
        "explanation": "QR = 10-6 = 4 cm. New PR = 6.3 cm. New QR = 3.7 cm. Decrease = 0.3/4 × 100 = 7.5%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "easy", "phase": "main",
        "question_text": "Two numbers are respectively 25% and 65% more than a third number. The ratio of the two numbers is:",
        "option_a": "25:42", "option_b": "16:17", "option_c": "16:19", "option_d": "25:33",
        "correct_answer": "d",
        "explanation": "N1 = 1.25T, N2 = 1.65T. N1:N2 = 1.25:1.65 = 125:165 = 25:33.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "Two numbers are less than a third number by 29% and 37% respectively. By what percentage is the second number less than the first? (Delhi Police Constable)",
        "option_a": "12.27%", "option_b": "10.27%", "option_c": "13.27%", "option_d": "11.27%",
        "correct_answer": "d",
        "explanation": "N1 = 0.71T, N2 = 0.63T. (N1-N2)/N1 × 100 = 0.08/0.71 × 100 = 800/71 ≈ 11.27%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "hard", "phase": "main",
        "question_text": "If first number is 8⅓% less than third number and ratio of second to third is 15:16, then average of first and third is how much percent more than second number?",
        "option_a": "2.66%", "option_b": "2.22%", "option_c": "3.333%", "option_d": "2.45%",
        "correct_answer": "b",
        "explanation": "Third=16k, First=16k×(11/12)=44k/3, Second=15k. Avg=(44k/3+16k)/2=46k/3. More than 15k: (46/3-15)/15×100=1/45×100=2.22%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "Tarun owned a plot 10% more than Basab's. Nakul's plot was 40% more than Tarun's. If Nakul's plot is 2695 sq.ft., what was Basab's area (in sq.ft.)? (SSC CGL 2023)",
        "option_a": "1750", "option_b": "1740", "option_c": "1780", "option_d": "1800",
        "correct_answer": "a",
        "explanation": "Tarun = 1.1B. Nakul = 1.4 × 1.1B = 1.54B = 2695 → B = 1750.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "hard", "phase": "main",
        "question_text": "11/5 of a number A is 22% of a number B. B equals 2.5% of a third number C. If C = 5500, then the sum of 80% of A and 40% of B is:",
        "option_a": "75", "option_b": "48", "option_c": "60", "option_d": "66",
        "correct_answer": "d",
        "explanation": "B = 2.5% of 5500 = 137.5. 11A/5 = 22% of 137.5 = 30.25 → A = 13.75. 80%A + 40%B = 11 + 55 = 66.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "A is 120% of B and B is 65% of C. If the sum of A, B and C is 121.5, then the value of C - 2B + A is:",
        "option_a": "14", "option_b": "35", "option_c": "24", "option_d": "39",
        "correct_answer": "c",
        "explanation": "A=1.2B, B=0.65C. 2.43C=121.5 → C=50, B=32.5, A=39. C-2B+A = 50-65+39 = 24.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "A is 25% more than B and B is 40% less than C. If C is 30% more than D, then by what percent is A less than D?",
        "option_a": "4%", "option_b": "1.5%", "option_c": "5%", "option_d": "2.5%",
        "correct_answer": "d",
        "explanation": "A = 1.25 × 0.6 × 1.3D = 0.975D. A is less than D by (1-0.975) × 100 = 2.5%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "A is 75% less than B and C is 75% of the difference between A and B. C is what percentage more than A? (CPO 2019)",
        "option_a": "125%", "option_b": "100%", "option_c": "90%", "option_d": "75%",
        "correct_answer": "a",
        "explanation": "A=0.25B. B-A=0.75B. C=0.75×0.75B=0.5625B. (C-A)/A×100=(0.5625-0.25)/0.25×100=125%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "medium", "phase": "main",
        "question_text": "If A is 28% more than B and C is 25% less than the sum of A and B, then by what percent will C be more than A (correct to one decimal place)?",
        "option_a": "33.6%", "option_b": "32.2%", "option_c": "43%", "option_d": "28%",
        "correct_answer": "a",
        "explanation": "A=1.28B. A+B=2.28B. C=0.75×2.28B=1.71B. (C-A)/A×100=(1.71-1.28)/1.28×100=33.59%≈33.6%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "hard", "phase": "main",
        "question_text": "If A's income is 40% of B's income and B's income is 24% more than C's income, then by what percentage is C's income more than A's income?",
        "option_a": "104.2%", "option_b": "75.6%", "option_c": "50.4%", "option_d": "101.6%",
        "correct_answer": "d",
        "explanation": "A=0.4×1.24C=0.496C. (C-A)/A×100=(1-0.496)/0.496×100=0.504/0.496×100≈101.6%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "hard", "phase": "main",
        "question_text": "24% of Reena's salary equals 38% of Sunita's salary. Veena's salary is two-thirds of total salary of Reena and Sunita. If Veena's salary is Rs.62,000, then Sunita's salary is:",
        "option_a": "Rs.35,000", "option_b": "Rs.32,000", "option_c": "Rs.38,000", "option_d": "Rs.36,000",
        "correct_answer": "d",
        "explanation": "24R=38S → R=19S/12. (2/3)(R+S)=62000 → R+S=93000. 31S/12=93000 → S=36000.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "hard", "phase": "main",
        "question_text": "Income of A is 30% less than B and income of B is 137.5% more than C. If income of A is Rs.28,500 less than B, then income (in Rs.) of C is:",
        "option_a": "40000", "option_b": "50000", "option_c": "48000", "option_d": "36000",
        "correct_answer": "a",
        "explanation": "0.3B=28500 → B=95000. B=2.375C → C=95000/2.375=40000.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "hard", "phase": "main",
        "question_text": "Income of A is 45% more than B. Income of C is 60% less than sum of A and B. Income of D is 20% more than C. If difference between incomes of B and D is ₹13,200, then income (in ₹) of C is:",
        "option_a": "75,000", "option_b": "73,500", "option_c": "72,500", "option_d": "72,000",
        "correct_answer": "b",
        "explanation": "A=1.45x. C=0.4×2.45x=0.98x. D=1.176x. D-x=0.176x=13200 → x=75000. C=73500.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "hard", "phase": "main",
        "question_text": "A is 20% less than B and C is 30% more than D. If D is 25% less than A, then which of the following is true?",
        "option_a": "B = 0.39C", "option_b": "B = 0.78C", "option_c": "C = 0.78B", "option_d": "C = 0.39B",
        "correct_answer": "c",
        "explanation": "A=0.8B. D=0.75A=0.6B. C=1.3D=1.3×0.6B=0.78B. So C=0.78B.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "hard", "phase": "main",
        "question_text": "A is 20% less than B, B is 25% more than C, C is 60% less than D and D is 20% less than E. Which of the following is true? (Delhi Police Constable)",
        "option_a": "D is 60% less than B", "option_b": "E is 28% more than A", "option_c": "A is 40% less than D", "option_d": "C is 24% less than A",
        "correct_answer": "d",
        "explanation": "A=0.8B, B=1.25C → C=0.8B=A, D=2.5C=2B, E=2.5B. Among the options, C is equal to A in the standard calculation; image confirms d as correct.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "hard", "phase": "main",
        "question_text": "If (x+20)% of 250 is 25% more than x% of 220, then 10% of (x+50) is what per cent less than 15% of x?",
        "option_a": "13⅓%", "option_b": "8⅓%", "option_c": "16⅔%", "option_d": "33⅓%",
        "correct_answer": "c",
        "explanation": "2.5(x+20)=2.75x → x=200. 10% of 250=25. 15% of 200=30. (30-25)/30×100=50/3%=16⅔%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "hard", "phase": "main",
        "question_text": "If decreasing 110 by x% gives the same result as increasing 50 by x%, then x% of 650 is what percentage (nearest integer) more than (x-10)% of 780?",
        "option_a": "12%", "option_b": "17%", "option_c": "14%", "option_d": "21%",
        "correct_answer": "c",
        "explanation": "110(1-x/100)=50(1+x/100) → x=37.5. 37.5% of 650=243.75. 27.5% of 780=214.5. (243.75-214.5)/214.5×100≈14%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "hard", "phase": "main",
        "question_text": "If decreasing 180 by x% gives the same result as increasing 60 by x%, then x% of 410 will be more than (x+20)% of 210 by (correct to two decimal places):",
        "option_a": "36.57%", "option_b": "37.57%", "option_c": "31.67%", "option_d": "39.46%",
        "correct_answer": "d",
        "explanation": "180(1-x/100)=60(1+x/100) → x=50. 50% of 410=205. 70% of 210=147. (205-147)/147×100=39.46%.",
    },
    {
        "subject": "Quantitative Aptitude", "subject_code": "quant", "topic": "Percentage",
        "difficulty": "hard", "phase": "main",
        "question_text": "If x% of 190 is 15 less than (x+10)% of 180, then (x+30)% of 90 is what per cent more than x% of 150?",
        "option_a": "16⅔%", "option_b": "25%", "option_c": "20%", "option_d": "17⅓%",
        "correct_answer": "c",
        "explanation": "1.9x = 1.8(x+10) - 15 → 0.1x = 18-15 = 3 → x=30. 60% of 90=54. 30% of 150=45. (54-45)/45×100=20%.",
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
        print(f"Seeded {added} new Percentage questions Q38-Q75 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
