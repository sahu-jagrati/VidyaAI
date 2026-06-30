import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

# Q22-Q32 Profit & Loss verified answers:
# Q22: CP/toy=32, SP=34 → profit%=2/32×100=6.25%
# Q23: CP=65500, SP=89080 → profit%=23580/65500×100=36%
# Q24: CP=28500, SP=24800 → loss%=3700/28500×100=12.98%
# Q25: CP=6480, SP=6800 → profit=320 → 320/6480×100=400/81%=4 76/81%≈4.94%
# Q26: A gain=192/384×100=50%, B gain=418/1254×100=1/3×100=33.33% → ratio=3:2
# Q27: CP=2800, loss=12% → SP=2800×0.88=2464
# Q28: CP=25995, 32% off → SP=25995×0.68=17676.6≈17677
# Q29: price=7071.84 incl 8%GST → base=6548, new price with 10%GST=7202.80
# Q30: 400 guavas at ₹1240/100, profit=940 → SP=5900, per dozen=5900/400×12=177
# Q31: SP=22140 at 23% profit → CP=22140/1.23=18000
# Q32: SP=80500 at 15% gain → CP=80500/1.15=70000

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "Sanal purchased 16 dozens of toys at the rate of Rs 384 per dozen. He sold each one of them at the rate of Rs 34. What was his percentage profit? (DSSB ASSISTANT GRADE-III 2024)",
        "option_a": "7.66%",
        "option_b": "6.25%",
        "option_c": "4.5%",
        "option_d": "3.25%",
        "correct_answer": "B",
        "explanation": "CP per toy = 384/12 = Rs 32. SP = Rs 34. Profit% = 2/32 × 100 = 6.25%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "Ram purchased a TV for ₹65,500 and sold it for ₹89,080. What is the percentage profit he made on the TV?",
        "option_a": "34%",
        "option_b": "36%",
        "option_c": "42%",
        "option_d": "40%",
        "correct_answer": "B",
        "explanation": "Profit = 89080 - 65500 = 23580. Profit% = 23580/65500 × 100 = 36%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Mahesh buys a water cooler for ₹28,500 and sells it for ₹24,800. What is his loss percentage? (Correct to 2 decimal places)",
        "option_a": "12.98%",
        "option_b": "14.98%",
        "option_c": "25.75%",
        "option_d": "15.25%",
        "correct_answer": "A",
        "explanation": "Loss = 28500 - 24800 = 3700. Loss% = 3700/28500 × 100 = 12.98%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Ramesh Chandra purchased 360 bulbs for ₹18 each. However, 20 bulbs were fused and had to be thrown away. The remaining were sold at ₹20 each. Find the gain or loss per cent. (SSC MTS 2024)",
        "option_a": "40/9 % loss",
        "option_b": "4 76/81 % loss",
        "option_c": "4 76/81 % profit",
        "option_d": "40/9 % profit",
        "correct_answer": "C",
        "explanation": "CP = 360×18 = ₹6480. SP = 340×20 = ₹6800. Profit = 320. Profit% = 320/6480×100 = 400/81 = 4 76/81 % ≈ 4.94%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A bought an item for ₹384 and sold it at ₹576, and B bought another item for ₹1,254 and sold it at ₹1,672. What is the ratio of gain percentage of A to gain percentage of B? (SSC MTS 2024)",
        "option_a": "3/2",
        "option_b": "2/3",
        "option_c": "5/3",
        "option_d": "3/5",
        "correct_answer": "A",
        "explanation": "A gain% = 192/384×100 = 50%. B gain% = 418/1254×100 = 1/3×100 = 33.33%. Ratio = 50:(100/3) = 3:2.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "A person buys a table fan for ₹2,800 and sells it at a loss of 12%. What is the selling price of the table fan? (SSC 2023)",
        "option_a": "₹2,466",
        "option_b": "₹2,468",
        "option_c": "₹2,462",
        "option_d": "₹2,464",
        "correct_answer": "D",
        "explanation": "SP = CP × (1 - loss%) = 2800 × 0.88 = ₹2,464.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "In the last two weeks of a sale, prices are reduced by 32%. What is the sale price (to the nearest rupee) of a microwave oven which originally cost ₹25,995?",
        "option_a": "₹18,318",
        "option_b": "₹17,677",
        "option_c": "₹16,767",
        "option_d": "₹21,729",
        "correct_answer": "B",
        "explanation": "Sale price = 25995 × (1 - 0.32) = 25995 × 0.68 = 17676.6 ≈ ₹17,677.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Anuj bought a purse for Rs 7071.84 including 8% GST. If the GST increases to 10%, then find the new selling price. (SSC CHSL 2023)",
        "option_a": "Rs 7779.02",
        "option_b": "Rs 7302.50",
        "option_c": "Rs 7128.79",
        "option_d": "Rs 7202.80",
        "correct_answer": "D",
        "explanation": "Base price (excl GST) = 7071.84/1.08 = 6548. New price with 10% GST = 6548 × 1.10 = Rs 7202.80.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "400 guavas were bought at ₹1240 per hundred and were sold at a profit of ₹940. Find the selling price (in ₹) per dozen of guavas. (SSC GD 2025)",
        "option_a": "₹167",
        "option_b": "₹192",
        "option_c": "₹177",
        "option_d": "₹187",
        "correct_answer": "C",
        "explanation": "Total CP = 4×1240 = ₹4960. Total SP = 4960+940 = ₹5900. SP per guava = 5900/400 = 14.75. SP per dozen = 14.75×12 = ₹177.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "Anandi sold a mobile for Rs 22,140 at a profit of 23%. What was the cost price of the mobile?",
        "option_a": "Rs 18,500",
        "option_b": "Rs 18,000",
        "option_c": "Rs 20,000",
        "option_d": "Rs 18,550",
        "correct_answer": "B",
        "explanation": "CP = SP / (1 + profit%) = 22140 / 1.23 = Rs 18,000. Verify: 18000 × 1.23 = 22140 ✓",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "Amit earned a gain of 15% on selling his bike for Rs 80,500. At what price (in Rs) would Amit have bought his bike?",
        "option_a": "Rs 78,000",
        "option_b": "Rs 70,000",
        "option_c": "Rs 72,000",
        "option_d": "Rs 65,000",
        "correct_answer": "B",
        "explanation": "CP = SP / (1 + gain%) = 80500 / 1.15 = Rs 70,000. Verify: 70000 × 1.15 = 80500 ✓",
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
        print(f"Seeded {added} new Profit & Loss questions Q22-Q32 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
