import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal
from app.models.question_model import Question

# Pipe & Cistern Q13-Q24 verified answers:
# Q13: Net=5/18−10/63=5/42 → 42/5=8.4 hrs  (D)  [SSC CPO 2023]
# Q14: 8/120−3/54=1/15−1/18=1/90 → 90 hrs  (D)  [SSC CGL 2023 PRE]
# Q15: Net drain=1/20−1/36=1/45; 1/5 full → 9 hrs  (C)  [DSSSB 2024]
# Q16: Net=1/X+1/Y−1/Z; Time=XYZ/(YZ+XZ−XY)  (D)  [Group D 2022]
# Q17: Net=1/12+1/18−1/36=4/36=1/9 → 9 min  (B)  [SSC CGL 2023 PRE]
# Q18: Net=(16+10−25)/400=1/400 → 400 hrs=16d16hr  (C)  [RRB ALP 2018]
# Q19: C drains 2/3 in 20min→rate=1/30; Net=1/450; 3/5 tank=270min=4.5hr  (D)
# Q20: A=1/120,C=1/60,B=1/40; 35%×40=14 hrs  (B)  [POST 2023]
# Q21: A=7/18,B=5/18 → B alone=18/5=3h36m  (B)  [SSC CGL 2023 PRE]
# Q22: Net=1/20; in 3hr: 3/20 filled; unfilled=17/20  (A)  [MITS 2020]
# Q23: Net=13/72; in 7min: 91/72; overflow=19/72=26 7/18 %  (A)
# Q24: Drain=1/40; half tank=20 hrs  (A)  [UP SI DAROGA 2021]

QUESTIONS = [
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "An inlet pipe can fill an empty tank in 3.6 hours, while an outlet pipe can drain a completely filled tank in 6.3 hours. If both pipes are opened simultaneously when the tank is empty, in how many hours will the tank get completely filled? [SSC CPO 2023]",
        "option_a": "8.7",
        "option_b": "8.1",
        "option_c": "9.0",
        "option_d": "8.4",
        "correct_answer": "D",
        "explanation": "Net fill rate = 1/3.6 − 1/6.3 = 5/18 − 10/63. LCM(18,63)=126: 35/126 − 20/126 = 15/126 = 5/42 per hr. Time = 42/5 = 8.4 hours.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "An inlet pipe can fill an empty tank in 120 hours while an outlet pipe drains a completely filled tank in 54 hours. If 8 inlet pipes and 3 outlet pipes are opened simultaneously, in how many hours will the tank get completely filled? [SSC CGL 2023 PRE]",
        "option_a": "81",
        "option_b": "96",
        "option_c": "72",
        "option_d": "90",
        "correct_answer": "D",
        "explanation": "8 inlets rate = 8/120 = 1/15 per hr. 3 outlets rate = 3/54 = 1/18 per hr. Net fill = 1/15 − 1/18 = (6−5)/90 = 1/90 per hr. Time = 90 hours.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A cistern has two pipes — one can fill it in 36 hours and the other can empty it in 20 hours. In how many hours will the cistern be emptied if both pipes are opened together when the cistern is already 1/5th full? [DSSSB Assistant Grade III 2024]",
        "option_a": "8",
        "option_b": "12",
        "option_c": "9",
        "option_d": "4",
        "correct_answer": "C",
        "explanation": "Drain rate (1/20) > fill rate (1/36), so net is draining. Net drain = 1/20 − 1/36 = (9−5)/180 = 4/180 = 1/45 per hr. 1/5 of tank empties in (1/5) ÷ (1/45) = 9 hours.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "Pipe A can fill a cistern in X hours, Pipe B can fill it in Y hours, and Pipe C can empty the full cistern in Z hours. If all three pipes are opened simultaneously, the time taken to fill the cistern is: [Group D 29/09/2022]",
        "option_a": "XYZ/(XY+YZ-XZ)",
        "option_b": "XYZ/(XZ+XY-YZ)",
        "option_c": "XYZ/(XZ-XY-YZ)",
        "option_d": "XYZ/(YZ+XZ-XY)",
        "correct_answer": "D",
        "explanation": "Net fill rate = 1/X + 1/Y − 1/Z = (YZ+XZ−XY)/XYZ. Time = XYZ/(YZ+XZ−XY). Verify: X=2,Y=3,Z=6 → 36/(18+12−6)=36/24=3/2 hr; net rate=1/2+1/3−1/6=2/3=1/(3/2) ✓.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "easy",
        "phase": "main",
        "question_text": "Pipe A can fill a tank in 12 minutes, Pipe B can fill it in 18 minutes, and Pipe C can empty the full tank in 36 minutes. If all the pipes are opened together, how much time will it take to fill the empty tank? [SSC CGL 2023 PRE]",
        "option_a": "7 minutes",
        "option_b": "9 minutes",
        "option_c": "12 minutes",
        "option_d": "6 minutes",
        "correct_answer": "B",
        "explanation": "Net rate = 1/12 + 1/18 − 1/36 = 3/36 + 2/36 − 1/36 = 4/36 = 1/9 per min. Time = 9 minutes.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "Two pipes fill a tank when working individually in 25 hours and 40 hours respectively, while a third pipe can drain the filled tank in 16 hours. If all three pipes are turned on at the same time when the tank is empty, how long will it take to fill the tank completely? [RRB ALP 17/08/2018]",
        "option_a": "15 days 15 hours",
        "option_b": "2 days 1 hour",
        "option_c": "16 days 16 hours",
        "option_d": "1 day 7 hours",
        "correct_answer": "C",
        "explanation": "LCM(25,40,16)=400. Net = 16/400+10/400−25/400 = 1/400 per hr. Time = 400 hours = 400÷24 = 16 days + 16 hours = 16 days 16 hours.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "Two pipes A and B can fill a tank in 45 minutes and 75 minutes respectively. A drain pipe C can empty two-thirds of the full tank in 20 minutes. In how many hours will three-fifth part of the tank be filled if all three pipes are opened simultaneously?",
        "option_a": "2.5",
        "option_b": "3.4",
        "option_c": "4",
        "option_d": "4.5",
        "correct_answer": "D",
        "explanation": "C drains 2/3 tank in 20 min → rate of C = (2/3)/20 = 1/30 per min. LCM(45,75,30)=450. Net fill = 10/450+6/450−15/450 = 1/450 per min. Time for 3/5 tank = (3/5)×450 = 270 min = 4.5 hours.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "Pipes A and B together can fill an empty tank in 30 hours, whereas pipes B and C together can fill it in 24 hours. A, B and C together can fill the tank in 20 hours. In how many hours can Pipe B alone fill 35% of the tank? [POST 2023]",
        "option_a": "10",
        "option_b": "14",
        "option_c": "20",
        "option_d": "17.5",
        "correct_answer": "B",
        "explanation": "A rate = 1/20−1/24 = 1/120. C rate = 1/20−1/30 = 1/60. B rate = 1/20−1/120−1/60 = (6−1−2)/120 = 3/120 = 1/40. B alone takes 40 hrs. 35% of tank = 0.35×40 = 14 hours.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "Inlet Pipes A and B can together fill an empty tank in 1.5 hours. Outlet Pipe C, when opened alone, can empty the completely filled tank in 4.5 hours. When only Pipes A and C are opened together, the empty tank is filled in 6 hours. Find the time taken by Pipe B, when opened alone, to fill the tank. [SSC CGL 2023 PRE]",
        "option_a": "3 hours 30 minutes",
        "option_b": "3 hours 36 minutes",
        "option_c": "3 hours 40 minutes",
        "option_d": "3 hours 45 minutes",
        "correct_answer": "B",
        "explanation": "A+B rate = 1/1.5 = 2/3. C rate = 1/4.5 = 2/9. A+C net fill = 1/6 → A rate = 1/6+2/9 = 3/18+4/18 = 7/18. B rate = 2/3−7/18 = 12/18−7/18 = 5/18. B alone = 18/5 = 3.6 hrs = 3 hours 36 minutes.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "Pipes A and B can fill a tank in 15 hours and 12 hours respectively. Pipe C alone can empty the full tank in 10 hours. If all the three pipes are opened together for 3 hours, what part of the tank will remain unfilled? [MITS 2020]",
        "option_a": "17/20",
        "option_b": "7/10",
        "option_c": "7/20",
        "option_d": "3/10",
        "correct_answer": "A",
        "explanation": "Net fill rate = 1/15+1/12−1/10 = 4/60+5/60−6/60 = 3/60 = 1/20 per hr. In 3 hours: 3×(1/20) = 3/20 filled. Remaining unfilled = 1−3/20 = 17/20.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "hard",
        "phase": "main",
        "question_text": "Three pipes A, B and C can fill a cistern in 12, 18 and 24 minutes respectively. If all the pipes are opened together for 7 minutes, what will be the volume of water that overflows as a percentage of the total volume of the cistern?",
        "option_a": "26 7/18 %",
        "option_b": "23 1/3 %",
        "option_c": "20 7/9 %",
        "option_d": "25 5/9 %",
        "correct_answer": "A",
        "explanation": "Net rate = 1/12+1/18+1/24 = 6/72+4/72+3/72 = 13/72 per min. In 7 min: 7×13/72 = 91/72. Overflow = 91/72−1 = 19/72. Overflow % = (19/72)×100 = 1900/72 = 26 7/18 %.",
    },
    {
        "subject": "Quantitative Aptitude",
        "subject_code": "quant",
        "topic": "Pipe & Cistern",
        "difficulty": "medium",
        "phase": "main",
        "question_text": "A tank has an inlet pipe and an outlet pipe. If the outlet pipe is closed, the inlet pipe fills the empty tank in 8 hours. If the outlet pipe is open, the inlet pipe fills the empty tank in 10 hours. If only the outlet pipe is open, in how many hours will the full tank be half emptied? [UP SI DAROGA 2021]",
        "option_a": "20",
        "option_b": "30",
        "option_c": "40",
        "option_d": "48",
        "correct_answer": "A",
        "explanation": "Outlet drain rate = 1/8−1/10 = (5−4)/40 = 1/40 per hr. Full tank drains in 40 hrs. Half tank drains in 40/2 = 20 hours.",
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
        print(f"Seeded {added} new Pipe & Cistern questions Q13-Q24 (skipped {len(QUESTIONS) - added} duplicates).")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
