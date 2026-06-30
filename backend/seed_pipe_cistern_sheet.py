import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A tank is normally filled in 20 hours by a pipe, but it takes 8 hours more to fill the tank due to a leakage at its bottom. The leakage point can empty the tank when it is 60% full in _____ hours. (SSC GD 2023)",
        "option_a": "42",
        "option_b": "35",
        "option_c": "56",
        "option_d": "49",
        "correct_answer": "A",
        "explanation": "Fill rate = 1/20. With leak, fill rate = 1/28. Leak rate = 1/20 - 1/28 = 1/70. Leak empties full tank in 70 hours. 60% of tank = 0.6 × 70 = 42 hours.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A pump can fill a tank with water in 7.5 hours. Because of a leak in the tank it takes 50 minutes more to fill the tank. The leak can empty the tank in how many hours? (SSC CPO 2023)",
        "option_a": "75 hrs",
        "option_b": "25 hrs",
        "option_c": "80 hrs",
        "option_d": "50 hrs",
        "correct_answer": "A",
        "explanation": "Fill time = 7.5h. With leak = 7.5h + 50min = 25/3 h. Leak rate = 1/7.5 - 3/25 = 2/15 - 3/25 = (10-9)/75 = 1/75. Leak empties full tank in 75 hours.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Pipes A and B can fill a tank in 16 hours and 24 hours respectively, whereas pipe C alone can empty the full tank in x hours. When all the 3 pipes are opened together, the tank is full in 20 4/7 hours. What is the value of x?",
        "option_a": "12",
        "option_b": "18",
        "option_c": "15",
        "option_d": "20",
        "correct_answer": "B",
        "explanation": "A+B rate = 1/16+1/24 = 5/48. Net rate = 7/144 (since time = 144/7 h). 5/48 - 1/x = 7/144 → 1/x = 15/144 - 7/144 = 8/144 = 1/18. So x = 18.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "Pipes A and B are emptying pipes and can empty a tank in 6 hours and 16 hours respectively. C is a filling pipe. All the three pipes were opened together. They took 80 minutes to empty 5/18th of the tank. Pipe C alone can fill the tank in: (SSC CGL 2022 PRE)",
        "option_a": "48 hours",
        "option_b": "40 hours",
        "option_c": "44 hours",
        "option_d": "36 hours",
        "correct_answer": "A",
        "explanation": "A+B drain rate = 1/6+1/16 = 11/48. Net drain = (5/18)/(80/60) = (5/18)×(3/4) = 5/24 = 10/48. 1/c = 11/48-10/48 = 1/48. C fills in 48 hours.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Pipe A can fill a tank in 20 hours and Pipe B can fill it in 25 hours. Pipe C is an emptying pipe. When all three pipes are opened for 15 hours, then 1/10 part of the tank is filled. How much time (in hours) will pipe C take to empty one-third part of the tank? (ICAR Technician 2023)",
        "option_a": "2",
        "option_b": "4",
        "option_c": "5",
        "option_d": "6",
        "correct_answer": "B",
        "explanation": "A+B rate = 9/100. Net fill = (1/10)/15 = 1/150. 1/c = 9/100 - 1/150 = 27/300 - 2/300 = 25/300 = 1/12. C empties full in 12h. One-third in 12/3 = 4 hours.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "Pipe A can fill a tank in 12 hours. Pipe B can fill 33⅓% of the same tank in 6 hours, whereas pipe C alone can empty the full tank in x hours. When all three pipes are opened together, 13/15 part of the tank is filled in 12 hours. How much time (in hours) will A and C together take to fill 40% part of the tank? (ICAR Assistant 2022)",
        "option_a": "22",
        "option_b": "24",
        "option_c": "28",
        "option_d": "20",
        "correct_answer": "B",
        "explanation": "B fills 1/3 in 6h → full in 18h. 12×(1/12+1/18-1/x) = 13/15 → 5/36-1/x = 13/180 → 1/x = 25/180-13/180 = 12/180 = 1/15. A+C rate = 1/12-1/15 = 1/60. Time for 40% = 0.4×60 = 24h.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "Pipes A and B can fill a tank in 6 hours and 15 hours respectively. Pipe C is a drain pipe. When all the three pipes are opened together for 6 hours, then 65% of the tank is filled. Initially, pipes A and C are opened for 8 hours and then C is closed and B is opened. Pipes A and B together will fill the remaining part of tank in _____ hours? (IB ACIO GRAE-2 2023)",
        "option_a": "20/7",
        "option_b": "2/7",
        "option_c": "3/2",
        "option_d": "2/5",
        "correct_answer": "A",
        "explanation": "A+B = 7/30. 6×(7/30-1/c) = 13/20 → 1/c = 1/8. C empties in 8h. A+C for 8h: rate=1/24, fills 1/3. Remaining 2/3. A+B rate=7/30. Time = (2/3)/(7/30) = 20/7 hours.",
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
        print(f"Seeded {added} new Pipe & Cistern questions Q25-Q31 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
