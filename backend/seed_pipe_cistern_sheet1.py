import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

# Pipe & Cistern Q1-Q12 verified answers:
# Q1:  15 taps × 36 min = n × 60 → n = 9  (B)
# Q2:  8 × 100 = 10 × t → t = 80 min  (B)  [SSC CHSL 2022]
# Q3:  A=100 L/min, B=90 L/min; 1615/190 = 8.5 min  (C)  [SSC CGL 2020 PRE]
# Q4:  f(f+10)=2000 → f=40, e=50 m³/min  (B)  [SSC CPO 2019]
# Q5:  A 1/3 faster → A=56min, B=224/3 min; 1/56+3/224=7/224→32 min ✓  (C)
# Q6:  net fill rate = 1/p − 1/q = 1/r  (B)  [SSC CGL 2016 PRE]
# Q7:  ratio B = (1/25)/(23/200) = 8/23  (C)  [SSC CPO 2019]
# Q8:  P alone T/2 + P+Q T/2 → T/40+T/24 = T/15 → 15 min  (D)  [UP POLICE 2024]
# Q9:  B(20min) alone 2T/5 + both 3T/5 → 3T/40=1 → T=40/3=13⅓ min  (B)  [SSC CGL 2023 PRE]
# Q10: 1/18+1/24 = 7/72 → T = 72/7 hr  (B)
# Q11: 1/12 − 1/16 = 1/48 → leak empties in 48 hr  (C)
# Q12: 1/6+1/8+1/12 = 9/24 = 3/8 → T = 8/3 = 2⅔ hr  (C)

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "If 15 taps of the same size can fill a tank in 36 minutes, then how many taps of the same type are needed to fill the tank in 1 hour?",
        "option_a": "10",
        "option_b": "9",
        "option_c": "12",
        "option_d": "6",
        "correct_answer": "B",
        "explanation": "Total tap-minutes needed = 15 × 36 = 540. In 60 minutes: n × 60 = 540 → n = 9.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "8 pipes are required to fill a tank in 1 hour 40 minutes. How long will it take if only 10 pipes of the same type are used? [SSC CHSL 2022]",
        "option_a": "1 hr 10 min",
        "option_b": "1 hr 20 min",
        "option_c": "1 hr 30 min",
        "option_d": "2 hr",
        "correct_answer": "B",
        "explanation": "Total pipe-minutes = 8 × 100 = 800. With 10 pipes: t = 800/10 = 80 min = 1 hr 20 min.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Pipe A can fill 350 litres in 3½ minutes and Pipe B can fill 780 litres in 8⅔ minutes. In how many minutes can they together fill 1615 litres? [SSC CGL 2020 PRE]",
        "option_a": "8 min",
        "option_b": "8 min 15 sec",
        "option_c": "8.5 min",
        "option_d": "9 min",
        "correct_answer": "C",
        "explanation": "Rate A = 350 ÷ 3.5 = 100 L/min. Rate B = 780 ÷ (26/3) = 90 L/min. Combined rate = 190 L/min. Time = 1615 ÷ 190 = 8.5 min.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "The capacity of a tank is 1800 m³. The emptying rate of a pipe is 10 m³/min more than its filling rate. If the tank takes 9 minutes less to empty than to fill, what is the emptying rate of the pipe? [SSC CPO 2019]",
        "option_a": "40 m³/min",
        "option_b": "50 m³/min",
        "option_c": "30 m³/min",
        "option_d": "60 m³/min",
        "correct_answer": "B",
        "explanation": "Let fill rate = f, empty rate = e = f+10. Fill time − empty time = 9 → 1800/f − 1800/(f+10) = 9 → 18000 = 9f(f+10) → f(f+10) = 2000 → f=40, e=50 m³/min.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Pipe A fills a tank 1/3 faster than Pipe B. If both pipes together fill the tank in 32 minutes, how long does Pipe A alone take to fill the tank?",
        "option_a": "44 min",
        "option_b": "52 min",
        "option_c": "56 min",
        "option_d": "64 min",
        "correct_answer": "C",
        "explanation": "A is 1/3 faster → Rate_A = (4/3) × Rate_B. Let A take t min; B takes 4t/3 min. Together: 1/t + 3/(4t) = 7/(4t) = 1/32 → t = 7×32/4 = 56 min.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "A tap can fill a cistern in p hours and a leakage pipe can empty it in q hours, where p < q. If both are opened simultaneously, the cistern fills in r hours. Which relation is correct? [SSC CGL 2016 PRE]",
        "option_a": "1/r = 1/p + 1/q",
        "option_b": "1/r = 1/p − 1/q",
        "option_c": "r = p − q",
        "option_d": "r = p + q",
        "correct_answer": "B",
        "explanation": "Net fill rate = fill rate − drain rate → 1/r = 1/p − 1/q. (p < q ensures 1/p > 1/q, so net rate is positive.)",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "Pipes X, Y and Z can fill a tank in 20, 25 and 40 minutes respectively, releasing chemicals A, B and C. All three are opened simultaneously. What fraction of the tank's contents is chemical B when the tank is full? [SSC CPO 2019]",
        "option_a": "5/23",
        "option_b": "10/23",
        "option_c": "8/23",
        "option_d": "4/23",
        "correct_answer": "C",
        "explanation": "Total fill rate = 1/20+1/25+1/40 = (10+8+5)/200 = 23/200. Pipe Y (chemical B) rate = 1/25 = 8/200. Fraction of B = (8/200)/(23/200) = 8/23.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Pipe P can fill a tank in 20 minutes and Pipe Q can fill it in 30 minutes. Pipe P works alone for half of the total time, then both P and Q work together for the remaining half. How long does it take to fill the tank? [UP POLICE 2024]",
        "option_a": "12 min",
        "option_b": "10 min",
        "option_c": "18 min",
        "option_d": "15 min",
        "correct_answer": "D",
        "explanation": "Let total time = T. P alone for T/2: work = T/40. P+Q together for T/2: work = (T/2)(1/20+1/30) = T/24. Total: T/40 + T/24 = (3T+5T)/120 = T/15 = 1 → T = 15 min.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Pipe A fills a tank in 24 minutes and Pipe B fills it in 20 minutes. Only Pipe B is used for 2/5 of the total time, then both pipes work together. Find the total time to fill the tank. [SSC CGL 2023 PRE]",
        "option_a": "12 min",
        "option_b": "13⅓ min",
        "option_c": "14 min",
        "option_d": "15 min",
        "correct_answer": "B",
        "explanation": "Let total time = T. B alone for 2T/5: work = (2T/5)(1/20) = T/50. Both for 3T/5: work = (3T/5)(1/24+1/20) = (3T/5)(11/120) = 11T/200. Total: T/50 + 11T/200 = (4T+11T)/200 = 15T/200 = 3T/40 = 1 → T = 40/3 = 13⅓ min.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "Pipe A can fill a tank in 18 hours and Pipe B can fill it in 24 hours. If both pipes are opened simultaneously, how many hours will it take to fill the tank?",
        "option_a": "8 hrs",
        "option_b": "72/7 hrs",
        "option_c": "10 hrs",
        "option_d": "12 hrs",
        "correct_answer": "B",
        "explanation": "Combined rate = 1/18 + 1/24 = (4+3)/72 = 7/72 per hour. Time = 72/7 = 10 2/7 hours.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A pipe can fill a tank in 12 hours. Due to a leak at the bottom, it takes 16 hours to fill the full tank. In how many hours will the leak alone empty a full tank?",
        "option_a": "24 hrs",
        "option_b": "36 hrs",
        "option_c": "48 hrs",
        "option_d": "64 hrs",
        "correct_answer": "C",
        "explanation": "Fill rate = 1/12. Effective fill rate (with leak) = 1/16. Leak rate = 1/12 − 1/16 = (4−3)/48 = 1/48. Leak alone empties in 48 hours.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "Pipes A, B and C can fill a tank in 6 hours, 8 hours and 12 hours respectively. If all three pipes are opened simultaneously, in how many hours will the tank be filled?",
        "option_a": "3 hrs",
        "option_b": "2 hrs",
        "option_c": "8/3 hrs",
        "option_d": "4 hrs",
        "correct_answer": "C",
        "explanation": "Combined rate = 1/6+1/8+1/12 = (4+3+2)/24 = 9/24 = 3/8 per hour. Time = 8/3 = 2⅔ hours.",
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
        print(f"Seeded {added} new Pipe & Cistern questions Q1-Q12 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
