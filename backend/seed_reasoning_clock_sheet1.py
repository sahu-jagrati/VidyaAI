"""
seed_reasoning_clock_sheet1.py
====================================
Seeds questions 1-10 (Clock) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Clock
Run     : python seed_reasoning_clock_sheet1.py

Answer key verification:
  Q1:  7:30 -> hour=7×30+30×0.5=225°; min=180°; |225-180|=45°                     -> B
  Q2:  mirror of 12:23 = 12:00-0:23 = 11:37                                        -> C
  Q3:  9:30 -> hour=270+15=285°; min=180°; |285-180|=105°                          -> C
  Q4:  hands at 90° = 22 times per 12h → 44 times in 24h                           -> B
  Q5:  2:20 -> hour=60+10=70°; min=120°; |120-70|=50°                              -> B
  Q6:  3:10 -> hour=90+5=95°; min=60°; |95-60|=35°                                 -> B
  Q7:  7:35 -> hour=210+17.5=227.5°; min=210°; |227.5-210|=17.5°                  -> C
  Q8:  at 7:00 gap=210°; need 180°; 5.5t=30 -> t=60/11=5 5/11 min past 7          -> D
  Q9:  upside-down (horizontal flip) + mirror = +180° to each hand angle;
       person reads 12:30 → actual: min@0°, hour@195°≈180° → 6:00                  -> A
  Q10: 10:00 -> hour=300°; min=0°; smaller angle=360-300=60°                       -> C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Clock_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Clock"

QUESTIONS = [
    # Q1
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": (
            "What is angle between both the hands of clock at 7:30?"
        ),
        "question_hi": (
            "7:30 बजे घड़ी की दोनों सुइयों के बीच का कोण क्या होगा?"
        ),
        "option_a": "35°",
        "option_b": "45°",
        "option_c": "37.5°",
        "option_d": "47.5°",
        "correct_answer": "B",
    },
    # Q2
    {
        "question_number": 2,
        "difficulty": "medium",
        "question_en": (
            "If the time in clock is 12:23. "
            "What is the time in the mirror?"
        ),
        "question_hi": (
            "यदि घड़ी में समय 12:23 है, तो दर्पण में समय क्या है?"
        ),
        "option_a": "1:23",
        "option_b": "12:37",
        "option_c": "11:37",
        "option_d": "1:32",
        "correct_answer": "C",
    },
    # Q3
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": (
            "What is angle between minute hand and hour hand at 9:30?"
        ),
        "question_hi": (
            "9:30 बजे मिनट की सुई और घंटे की सुई के बीच का कोण क्या होगा?"
        ),
        "option_a": "90°",
        "option_b": "100°",
        "option_c": "105°",
        "option_d": "110°",
        "correct_answer": "C",
    },
    # Q4
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": (
            "How many times will the hands of clock be at right angle in a day?"
        ),
        "question_hi": (
            "एक दिन में घड़ी की सुइयां कितनी बार समकोण पर होंगी?"
        ),
        "option_a": "22",
        "option_b": "44",
        "option_c": "42",
        "option_d": "24",
        "correct_answer": "B",
    },
    # Q5
    {
        "question_number": 5,
        "difficulty": "easy",
        "question_en": (
            "What is angle between minute hand & hour hand at 2:20?"
        ),
        "question_hi": (
            "2:20 पर मिनट की सुई और घंटे की सुई के बीच का कोण क्या है?"
        ),
        "option_a": "105°",
        "option_b": "50°",
        "option_c": "35°",
        "option_d": "120°",
        "correct_answer": "B",
    },
    # Q6
    {
        "question_number": 6,
        "difficulty": "easy",
        "question_en": (
            "What is angle between hour hand and minute hand at 3:10?"
        ),
        "question_hi": (
            "3:10 पर घंटे की सुई और मिनट की सुई के बीच का कोण क्या है?"
        ),
        "option_a": "40°",
        "option_b": "35°",
        "option_c": "45°",
        "option_d": "27°",
        "correct_answer": "B",
    },
    # Q7
    {
        "question_number": 7,
        "difficulty": "easy",
        "question_en": (
            "What is the angle between minute and hour hand at 7:35?"
        ),
        "question_hi": (
            "7:35 पर मिनट और घंटे की सुई के बीच का कोण क्या है?"
        ),
        "option_a": "10°",
        "option_b": "12.5°",
        "option_c": "17.5°",
        "option_d": "15°",
        "correct_answer": "C",
    },
    # Q8
    {
        "question_number": 8,
        "difficulty": "hard",
        "question_en": (
            "At what time between 7 and 8 o'clock will the hands of a clock "
            "be in the same straight line but, not together?"
        ),
        "question_hi": (
            "7 और 8 बजे के बीच किस समय एक घड़ी की सुइयाँ "
            "एक ही सीधी रेखा में होंगी लेकिन एक साथ नहीं?"
        ),
        "option_a": "5 min. past 7/7 बजकर 5 मिनट पर",
        "option_b": "5²/₁₁ minutes past 7/7 बजकर 5²/₁₁ मिनट पर",
        "option_c": "5³/₁₁ minutes past 7/7 बजकर 5³/₁₁ मिनट पर",
        "option_d": "5⁵/₁₁ minutes past 7/7 बजकर 5⁵/₁₁ मिनट पर",
        "correct_answer": "D",
    },
    # Q9
    {
        "question_number": 9,
        "difficulty": "hard",
        "question_en": (
            "A clock with only dot markings 3, 6, 9 and 12 positions has been "
            "kept upside down in front of a mirror. A person reads the time in "
            "the reflection of the clock as 12:30. The actual time will be?"
        ),
        "question_hi": (
            "एक घड़ी जिसमें केवल 3, 6, 9 और 12 स्थान अंकित हैं, को दर्पण के सामने "
            "उल्टा रखा गया है। एक व्यक्ति घड़ी के प्रतिबिंब में समय 12:30 पढ़ता है। "
            "वास्तविक समय होगा?"
        ),
        "option_a": "6:00",
        "option_b": "03:45",
        "option_c": "12:00",
        "option_d": "11:30",
        "correct_answer": "A",
    },
    # Q10
    {
        "question_number": 10,
        "difficulty": "easy",
        "question_en": (
            "What is the measure of the angle formed by the hour and minute "
            "hand when the time is 10 o'clock?"
        ),
        "question_hi": (
            "जब समय 10 बजे हो तो घंटे और मिनट की सुइयों के बीच बनने वाले "
            "कोण का माप क्या है?"
        ),
        "option_a": "30°",
        "option_b": "45°",
        "option_c": "60°",
        "option_d": "90°",
        "correct_answer": "C",
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        existing_short = {
            row[0][:80]
            for row in db.query(Question.question_en)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        for d in QUESTIONS:
            if d["question_en"][:80] in existing_short:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue

            db.add(Question(
                subject    = SUBJECT,
                topic      = TOPIC,
                source_pdf = SOURCE,
                **d,
            ))
            inserted += 1

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
