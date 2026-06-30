import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "The ratio of the cost price of an article to its selling price is 432:612. The profit percentage (rounded off to 2 decimal places) on it is: (SSC POST XII MATRICULATION LEVEL)",
        "option_a": "41.66%",
        "option_b": "40.25%",
        "option_c": "42.33%",
        "option_d": "38.26%",
        "correct_answer": "A",
        "explanation": "CP:SP = 432:612 = 12:17. Profit% = (17-12)/12 × 100 = 5/12 × 100 = 41.666...% ≈ 41.66%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "In a medical transaction, 17 times the cost price is equal to 8 times the sum of the cost price and the selling price. What is the gain or loss percentage?",
        "option_a": "Loss 15%",
        "option_b": "Gain 17.5%",
        "option_c": "Gain 12.5%",
        "option_d": "Loss 30%",
        "correct_answer": "C",
        "explanation": "17c = 8(c+s) → 9c = 8s → SP/CP = 9/8. Gain% = (9-8)/8 × 100 = 12.5%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "The selling price of 84 items is equal to the cost price of 105 items. What is the percentage of profit gained in the transaction? (SSC SELECTION POST XII HIGHER SECONDARY LEVEL)",
        "option_a": "28%",
        "option_b": "20%",
        "option_c": "25%",
        "option_d": "21%",
        "correct_answer": "C",
        "explanation": "SP of 84 = CP of 105. SP per item = 105/84 = 5/4 of CP. Profit% = (5/4 - 1) × 100 = 25%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "The selling price of 32 items is equal to the cost price of 45 items. What is the percentage of profit made on the sale of each item? (DP CONSTABLE 2023)",
        "option_a": "40.75%",
        "option_b": "40.5%",
        "option_c": "40.625%",
        "option_d": "40.25%",
        "correct_answer": "C",
        "explanation": "SP of 32 = CP of 45. SP per item = 45/32 of CP. Profit% = (45-32)/32 × 100 = 13/32 × 100 = 40.625%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "A fruit vendor recovers the cost of 95 oranges by selling 80 oranges. What is his profit percentage?",
        "option_a": "18.75%",
        "option_b": "20.75%",
        "option_c": "21.25%",
        "option_d": "24.25%",
        "correct_answer": "A",
        "explanation": "SP of 80 = CP of 95. SP per orange = 95/80 = 19/16 of CP. Profit% = (19-16)/16 × 100 = 3/16 × 100 = 18.75%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "If the cost price of 850 articles is equal to the selling price of 595 articles, then the gain or loss % is:",
        "option_a": "51%",
        "option_b": "42.84%",
        "option_c": "35%",
        "option_d": "44.44%",
        "correct_answer": "B",
        "explanation": "SP of 595 = CP of 850. Gain% = (850-595)/595 × 100 = 255/595 × 100 ≈ 42.86% ≈ 42.84%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "The cost price of 33 books is the same as the selling price of x books. If the profit is 10%, then the value of x is:",
        "option_a": "30",
        "option_b": "20",
        "option_c": "10",
        "option_d": "40",
        "correct_answer": "A",
        "explanation": "CP of 33 = SP of x. With 10% profit: SP = 1.1 × CP. So 1.1 × CP × x = 33 × CP → x = 33/1.1 = 30.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "The selling price of y items is equal to the cost price of 540 items. If the profit made is 44%, then find the value of y. (SSC SELECTION POST XII GRADUATE LEVEL)",
        "option_a": "375",
        "option_b": "400",
        "option_c": "360",
        "option_d": "380",
        "correct_answer": "A",
        "explanation": "SP of y = CP of 540. With 44% profit: SP = 1.44 × CP. So 1.44 × CP × y = 540 × CP → y = 540/1.44 = 375.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A man buys 10 identical articles for a total of ₹15. If he sells each of them for ₹1.7, his profit percentage will be ____% (rounded off to two decimal places). (SSC CGL MAINS 2024)",
        "option_a": "14.33",
        "option_b": "12.76",
        "option_c": "13.33",
        "option_d": "11.76",
        "correct_answer": "C",
        "explanation": "CP per article = 15/10 = ₹1.5. SP = ₹1.7. Profit% = (1.7-1.5)/1.5 × 100 = 0.2/1.5 × 100 = 13.33%.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Profit & Loss",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A man buys a machine for Rs 5000. After one year, he sold it for Rs 6000. After two years, he again buys the same machine for Rs 8000 and sells it for Rs 10000. Find his overall profit percentage for both the transactions.",
        "option_a": "42%",
        "option_b": "15.23%",
        "option_c": "20.23%",
        "option_d": "23.08%",
        "correct_answer": "D",
        "explanation": "Total CP = 5000+8000 = 13000. Total SP = 6000+10000 = 16000. Profit = 3000. Profit% = 3000/13000 × 100 = 23.08%.",
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
        print(f"Seeded {added} new Profit & Loss questions (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
