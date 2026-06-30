import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

# Q11-Q21 Profit & Loss verified answers:
# Q11: CP=0.72SP → profit%=0.28/0.72×100=38.89%
# Q12: CP=0.84SP → profit%=0.16/0.84×100=19.04%≈19%
# Q13: SP=4650, Loss=350, CP=5000 → loss%=7%
# Q14: Gain=2/7 SP, CP=5/7 SP → gain%=40%
# Q15: Aniket CP=112, SP=100 → loss=12/112×100=10.71% (CISF BCM 2022)
# Q16: Profit on CP=30% → profit on SP=30/130×100=23.1%
# Q17: Profit=22.5% of SP → on CP=22.5/77.5×100=29.03%
# Q18: Loss=13.33% of SP → on CP=2/17×100=11.76%
# Q19: Gain=SP/6 → gain%=1/5×100=20% (SSC CGL PRE 2024)
# Q20: SP-1275=0.15SP → 0.85SP=1275 → SP=1500 (MTS 2023)
# Q21: CP=2800 (source shows 2000, typo), profit=20% of SP → 0.8SP=2800→SP=3500→profit=700

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "If the cost price is 72% of the selling price, then what is the percentage of profit? (Correct to 2 decimal places)",
        "option_a": "38.89%",
        "option_b": "35.75%",
        "option_c": "32.25%",
        "option_d": "28.75%",
        "correct_answer": "A",
        "explanation": "CP = 0.72 × SP. Profit% = (SP-CP)/CP × 100 = 0.28/0.72 × 100 = 38.88...% ≈ 38.89%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "The cost price of an article is 16% less than its selling price. What is the profit or loss percentage (to the nearest integer)?",
        "option_a": "Loss 19%",
        "option_b": "Loss 16%",
        "option_c": "Profit 16%",
        "option_d": "Profit 19%",
        "correct_answer": "D",
        "explanation": "CP = SP - 16% of SP = 0.84SP. Profit% = 0.16/0.84 × 100 = 19.04% ≈ 19% profit.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "If a box was sold at a loss of ₹350 for ₹4,650, then the percentage loss is equal to: (DP CONSTABLE 2023)",
        "option_a": "5%",
        "option_b": "8%",
        "option_c": "7%",
        "option_d": "6%",
        "correct_answer": "C",
        "explanation": "SP = ₹4650, Loss = ₹350. CP = 4650+350 = ₹5000. Loss% = 350/5000 × 100 = 7%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "If the gain is two-seventh of the selling price, then the gain percentage is:",
        "option_a": "37.5%",
        "option_b": "40%",
        "option_c": "28.56%",
        "option_d": "25%",
        "correct_answer": "B",
        "explanation": "Gain = (2/7)SP. CP = SP - (2/7)SP = (5/7)SP. Gain% = (2/7)/(5/7) × 100 = 2/5 × 100 = 40%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Shantanu buys an article and sells it to Aniket at a profit of 12%. Aniket sells it back to Shantanu at the price which Shantanu paid for it. What is Aniket's percent loss? (CISF BCM 2022)",
        "option_a": "10%",
        "option_b": "10.71%",
        "option_c": "10.5%",
        "option_d": "8.9%",
        "correct_answer": "B",
        "explanation": "Let Shantanu's CP = 100. He sells to Aniket at 112. Aniket sells back at 100. Aniket's loss% = 12/112 × 100 = 10.71%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Ram makes a profit of 30% by selling an article. What would be the profit percent if it were calculated on the selling price instead of the cost price? (Correct to one decimal place)",
        "option_a": "20.5%",
        "option_b": "23.1%",
        "option_c": "25.5%",
        "option_d": "26.9%",
        "correct_answer": "B",
        "explanation": "Profit on CP = 30%. SP = 1.3CP. Profit% on SP = 0.3CP/1.3CP × 100 = 30/130 × 100 = 23.07% ≈ 23.1%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A shopkeeper sells his goods at 22.5% profit on selling price. Find actual profit percentage.",
        "option_a": "29.03%",
        "option_b": "32.5%",
        "option_c": "26.78%",
        "option_d": "28.53%",
        "correct_answer": "A",
        "explanation": "Profit = 22.5% of SP, so CP = 77.5% of SP. Profit% on CP = 22.5/77.5 × 100 = 29.03%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A shopkeeper sells his goods at 13.33% loss on selling price. Find his % loss on cost price.",
        "option_a": "11.76%",
        "option_b": "10.92%",
        "option_c": "9.85%",
        "option_d": "11.25%",
        "correct_answer": "A",
        "explanation": "Loss = (2/15)SP (since 13.33%=2/15). CP = SP + (2/15)SP = (17/15)SP. Loss% on CP = (2/15)/(17/15) × 100 = 2/17 × 100 = 11.76%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Find gain percentage, given that Anubha sold her scooter for Rs 31524 gaining 1/6th of the selling price. (SSC CGL PRE 2024)",
        "option_a": "8%",
        "option_b": "20%",
        "option_c": "30%",
        "option_d": "35%",
        "correct_answer": "B",
        "explanation": "Gain = SP/6. CP = SP - SP/6 = 5SP/6. Gain% = (SP/6)/(5SP/6) × 100 = 1/5 × 100 = 20%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Ramesh purchased a bag for Rs 1275 and sold it at a gain of 15% on the selling price. Find the selling price of the bag. (MTS 2023)",
        "option_a": "Rs 1325",
        "option_b": "Rs 1400",
        "option_c": "Rs 1475",
        "option_d": "Rs 1500",
        "correct_answer": "D",
        "explanation": "Gain = 15% of SP. SP - 1275 = 0.15SP → 0.85SP = 1275 → SP = 1500.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "The cost price of an article is ₹2800. Profit as a percentage of selling price is 20%. What is the actual profit (in ₹)?",
        "option_a": "Rs 504",
        "option_b": "Rs 700",
        "option_c": "Rs 560",
        "option_d": "Rs 416",
        "correct_answer": "B",
        "explanation": "Profit = 20% of SP → SP - CP = 0.2SP → 0.8SP = 2800 → SP = 3500. Profit = 3500 - 2800 = Rs 700.",
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
        print(f"Seeded {added} new Profit & Loss questions Q11-Q21 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
