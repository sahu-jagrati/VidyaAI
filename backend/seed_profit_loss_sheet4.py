import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

# Q33-Q42 Profit & Loss verified answers:
# Q33: SP=1452, loss=12% → CP=1452/0.88=1650
# Q34: SP=70150, loss=23.33%(=7/30) → CP=70150×30/23=91500
# Q35: SP-CP=575, profit%=23% → CP=575/0.23=2500, SP=3075
# Q36: SP=614856, gain%=36% on CP → Profit=614856×36/136=162756
# Q37: SP=167.40, profit=24% → CP=135; for 38%: new SP=186.30, increase=18.90
# Q38: SP=70000, gain=25% → CP=56000; for 30%: new SP=56000×1.3=72800
# Q39: SP=355, loss=29% → CP=500; for 21% gain: new SP=500×1.21=605
# Q40: SP=46068, loss=12% → CP=52350; for 18% gain: new SP=52350×1.18=61773
# Q41: SP=11250, loss=10% → CP=12500; for 6% gain: new SP=12500×1.06=13250
# Q42: SP=1596, loss=24% → CP=2100; for 24% gain: new SP=2100×1.24=2604

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "By selling a pendrive for Rs 1452, a shopkeeper incurs a loss of 12%. Find the cost price of the pendrive for the shopkeeper (in Rs). (UP POLICE SI 2021)",
        "option_a": "Rs 1,647",
        "option_b": "Rs 1,650",
        "option_c": "Rs 1,652",
        "option_d": "Rs 1,645",
        "correct_answer": "B",
        "explanation": "CP = SP/(1 - loss%) = 1452/0.88 = Rs 1,650. Verify: 1650 × 0.88 = 1452 ✓",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Find the cost price of an article which is sold at Rs 70,150 at a loss of 23.33%.",
        "option_a": "Rs 91,500",
        "option_b": "Rs 90,000",
        "option_c": "Rs 90,500",
        "option_d": "Rs 94,650",
        "correct_answer": "A",
        "explanation": "23.33% = 7/30. CP × (1 - 7/30) = 70150 → CP × 23/30 = 70150 → CP = 70150 × 30/23 = Rs 91,500.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "The difference between cost price and selling price is Rs 575. If profit percentage is 23%, then what is the selling price (in Rs)?",
        "option_a": "Rs 3,225",
        "option_b": "Rs 1,925",
        "option_c": "Rs 2,500",
        "option_d": "Rs 3,075",
        "correct_answer": "D",
        "explanation": "Profit = 23% of CP → 575 = 0.23 × CP → CP = 2500. SP = CP + Profit = 2500 + 575 = Rs 3,075.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A shopkeeper expects a gain of 36% on his cost price. In a month, his sale was Rs 6,14,856. What was his profit (in ₹)? (SSC SELECTION POST XII MATRICULATION LEVEL)",
        "option_a": "Rs 1,62,756",
        "option_b": "Rs 1,63,900",
        "option_c": "Rs 1,61,235",
        "option_d": "Rs 1,62,800",
        "correct_answer": "A",
        "explanation": "Profit = SP × gain%/(100+gain%) = 614856 × 36/136 = 614856 × 9/34 = Rs 1,62,756.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Amit earns a profit of 24% by selling an article for ₹167.40. By how much (in ₹) should he increase the selling price of the article to get a profit of 38%?",
        "option_a": "18.90",
        "option_b": "19.80",
        "option_c": "17.40",
        "option_d": "19.20",
        "correct_answer": "A",
        "explanation": "CP = 167.40/1.24 = Rs 135. New SP for 38% = 135 × 1.38 = 186.30. Increase = 186.30 - 167.40 = Rs 18.90.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "Ram sold a motorcycle for ₹70,000 at 25% profit. For what price should he sell a motorcycle to gain 30% profit?",
        "option_a": "₹72,900",
        "option_b": "₹72,800",
        "option_c": "₹72,600",
        "option_d": "₹72,700",
        "correct_answer": "B",
        "explanation": "CP = 70000/1.25 = Rs 56,000. New SP for 30% gain = 56000 × 1.30 = ₹72,800.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "When an article is sold for Rs 355, there is a loss of 29%. To gain 21%, it should be sold for Rs ___.",
        "option_a": "Rs 605",
        "option_b": "Rs 635",
        "option_c": "Rs 603",
        "option_d": "Rs 600",
        "correct_answer": "A",
        "explanation": "CP = 355/(1-0.29) = 355/0.71 = Rs 500. New SP for 21% gain = 500 × 1.21 = Rs 605.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Sofia sold an iPhone at the cost of Rs 46,068 at a loss of 12%. What cost will she have to sell it at to get a profit of 18%?",
        "option_a": "Rs 61,773",
        "option_b": "Rs 65,773",
        "option_c": "Rs 58,350",
        "option_d": "Rs 52,350",
        "correct_answer": "A",
        "explanation": "CP = 46068/0.88 = Rs 52,350. New SP for 18% gain = 52350 × 1.18 = Rs 61,773.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "A person incurs 10% loss by selling a mobile phone for ₹11,250. At what price (in ₹) should the mobile phone be sold to earn a 6% profit? (ICAR Technician 2023)",
        "option_a": "₹13,250",
        "option_b": "₹13,500",
        "option_c": "₹13,300",
        "option_d": "₹13,350",
        "correct_answer": "A",
        "explanation": "CP = 11250/0.90 = ₹12,500. New SP for 6% gain = 12500 × 1.06 = ₹13,250.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "By selling a table for Rs 1596, Aarav loses 24%. At what price (in Rs) should it be sold to gain 24%? (SSC CPO 2023)",
        "option_a": "Rs 2,604",
        "option_b": "Rs 1,979",
        "option_c": "Rs 3,196",
        "option_d": "Rs 3,024",
        "correct_answer": "A",
        "explanation": "CP = 1596/0.76 = Rs 2,100. New SP for 24% gain = 2100 × 1.24 = Rs 2,604.",
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
        print(f"Seeded {added} new Profit & Loss questions Q33-Q42 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
