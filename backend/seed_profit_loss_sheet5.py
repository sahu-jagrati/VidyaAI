import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

# Q43-Q52 Profit & Loss verified answers:
# Q43: SP=20240, loss=8% → CP=22000; 12% gain → SP=24640
# Q44: SP=655000, loss=20% → CP=818750; 15% gain → SP=941562.50
# Q45: SP=640, loss=15% of SP → CP=736; 15% gain on CP → SP=846.40
# Q46: CP & SP both decrease by same k → profit amount unchanged, CP smaller → Z increases
# Q47: 330 bananas (990/3), CP/banana=6; 10 bananas at 18% gain → SP=70.80
# Q48: n×2.5-CP=120 & CP-n×1.85=62 → n×0.65=182 → n=280
# Q49: CP×(1.05-0.83)=1056 → CP×0.22=1056 → CP=4800
# Q50: CP×(1.08-0.85)=2553 → CP=11100; 18% gain → SP=13098
# Q51: CP×(1.14-0.92)=121 → CP=550; sold at 536.25 → (536.25-550)/550×100 = -2.5% (loss)
# Q52: 99CP=100X, (100+P)CP=100Y → subtract → (P+1)CP=100(Y-X) → CP=100(Y-X)/(P+1)

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "By selling an article for ₹20,240, a shopkeeper loses 8%. For what price (in ₹) should he sell it to make a profit of 12%? (SSC GD 2025)",
        "option_a": "₹26,640",
        "option_b": "₹24,640",
        "option_c": "₹26,044",
        "option_d": "₹24,660",
        "correct_answer": "B",
        "explanation": "CP = 20240/0.92 = ₹22,000. New SP for 12% gain = 22000 × 1.12 = ₹24,640.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Ram sold a plot for Rs 6,55,000 at 20% loss. For what price should he sell the plot to gain 15% profit?",
        "option_a": "Rs 7,41,562.50",
        "option_b": "Rs 6,41,562.50",
        "option_c": "Rs 8,41,562.50",
        "option_d": "Rs 9,41,562.50",
        "correct_answer": "D",
        "explanation": "CP = 655000/0.80 = Rs 8,18,750. New SP for 15% gain = 818750 × 1.15 = Rs 9,41,562.50.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "By selling an article for Rs 640, a person loses 15% of its selling price. What price (in Rs) should he sell it to gain 15% on its cost price?",
        "option_a": "835",
        "option_b": "832",
        "option_c": "836.60",
        "option_d": "846.40",
        "correct_answer": "D",
        "explanation": "Loss = 15% of SP = 0.15×640 = 96. CP = 640+96 = 736. New SP for 15% gain = 736×1.15 = Rs 846.40.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "CP of an article is C and SP is S, and Z is profit % or loss %. If CP and SP both decreased by the same amount, then Z will:",
        "option_a": "Increase",
        "option_b": "Decrease",
        "option_c": "Remain constant",
        "option_d": "Cannot be determined",
        "correct_answer": "A",
        "explanation": "Profit/loss amount = S−C stays unchanged, but CP decreases to C−k. New Z = (S−C)/(C−k)×100 > (S−C)/C×100. So Z increases.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "The difference between selling price of some bananas, if sold at Rs 10 per banana instead of Rs 7 per banana, is Rs 990. If the cost price of all the bananas is Rs 1980, then find the selling price (in Rs) of ten bananas if profit earned is 18%. (SSC GD 2021)",
        "option_a": "Rs 99.00",
        "option_b": "Rs 70.80",
        "option_c": "Rs 90.20",
        "option_d": "Rs 60.00",
        "correct_answer": "B",
        "explanation": "Bananas = 990/(10−7) = 330. CP/banana = 1980/330 = Rs 6. SP of 10 at 18% gain = 60×1.18 = Rs 70.80.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Dipesh makes a profit of Rs 120 if he sells certain number of pencils at Rs 2.5 per pencil and incurs a loss of Rs 62 if he sells the same number of pencils for Rs 1.85 per pencil. How many pencils does Dipesh have?",
        "option_a": "260",
        "option_b": "280",
        "option_c": "300",
        "option_d": "320",
        "correct_answer": "B",
        "explanation": "n×2.5−CP=120 and CP−n×1.85=62. Adding: n×0.65=182 → n=280. Verify: CP=580; 580−280×1.85=62 ✓",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A man sold his cycle at 17% loss. If he had sold it for Rs 1056 more, he would have made 5% profit. The cost price of the cycle is: (MTS 2023)",
        "option_a": "Rs 4,700",
        "option_b": "Rs 4,800",
        "option_c": "Rs 5,100",
        "option_d": "Rs 4,500",
        "correct_answer": "B",
        "explanation": "CP×(0.05+0.17)=1056 → CP×0.22=1056 → CP=Rs 4,800. Verify: 4800×0.83=3984 (loss SP), 3984+1056=5040=4800×1.05 ✓",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A TV is sold at 8% gain. Had it been sold for Rs 2553 less, there would have been a loss of 15%. To gain 18%, the selling price (in ₹) of TV would be:",
        "option_a": "₹11,100",
        "option_b": "₹13,098",
        "option_c": "₹15,000",
        "option_d": "₹9,102",
        "correct_answer": "B",
        "explanation": "CP×(1.08−0.85)=2553 → CP×0.23=2553 → CP=₹11,100. For 18% gain: SP=11100×1.18=₹13,098.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "An article was sold at a profit of 14%. Had it been sold for Rs 121 less, a loss of 8% would have been incurred. If the same article would have been sold for Rs 536.25, then the profit/loss percent would have been:",
        "option_a": "Loss, 2.5%",
        "option_b": "Profit, 2.5%",
        "option_c": "Profit, 5%",
        "option_d": "Loss, 5%",
        "correct_answer": "A",
        "explanation": "CP×(1.14−0.92)=121 → CP×0.22=121 → CP=Rs 550. At 536.25: (536.25−550)/550×100 = −2.5% → Loss 2.5%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "When an article is sold for Rs X, loss percentage is equal to 1%. However, when the same article is sold for Rs Y, profit percentage is equal to P%. What is the CP of that article?",
        "option_a": "(Y−X)/(P+1)",
        "option_b": "100(P+1)/(Y−X)",
        "option_c": "100(Y−X)/(P+1)",
        "option_d": "100(Y−X)/(P−1)",
        "correct_answer": "C",
        "explanation": "Loss: 99×CP=100X. Gain: (100+P)×CP=100Y. Subtracting: (P+1)×CP=100(Y−X). So CP=100(Y−X)/(P+1).",
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
        print(f"Seeded {added} new Profit & Loss questions Q43-Q52 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
