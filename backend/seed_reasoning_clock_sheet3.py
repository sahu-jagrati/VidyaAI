"""
seed_reasoning_clock_sheet3.py
====================================
Seeds questions 20-28 (Clock) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Clock
Run     : python seed_reasoning_clock_sheet3.py

Answer key verification:
  Q20: 8AM-10PM=840min; gain=5s/3min=1400s=23m20s; shows 10:23:20 PM              -> D
  Q21: 16 min × 5.5°/min = 88°                                                     -> C
  Q22: 3 divisions × 6°/div = 18°                                                  -> B
  Q23: 8:30 -> hour=255°, min=180°; |255-180|=75°                                  -> C
  Q24: straight-line opposite = 22 times per 12h = 22/day (each 12h)               -> B
  Q25: coincide = 22 times per 12h = 22/day                                        -> C
  Q26: 3→4 coincide: min gains 60 spaces in 12h=65.45min/round;
       at 3:00 gap=15 min-marks; gain 15: t=15×12/11=180/11=16 4/11 min            -> A
  Q27: 2:30 -> hour=75°, min=180°; |180-75|=105°                                   -> A
  Q28: upside-down+mirror; person reads 9:50; actual=18:30-9:50=8:40               -> B
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Clock_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Clock"

QUESTIONS = [
    # Q20
    {
        "question_number": 20,
        "difficulty": "medium",
        "question_en": (
            "A watch gains 5 seconds in every 3 minutes. The watch was set right "
            "at 8:00 AM. What time will it show at 10:00 PM on the same day?"
        ),
        "question_hi": (
            "एक घड़ी प्रत्येक 3 मिनट में 5 सेकंड आगे बढ़ जाती है। घड़ी को "
            "सुबह 8:00 बजे सही किया गया। उसी दिन रात 10:00 बजे यह घड़ी "
            "क्या समय दिखाएगी?"
        ),
        "option_a": "10:00 PM",
        "option_b": "10:22:20 PM",
        "option_c": "10:20 PM",
        "option_d": "10:23:20 PM",
        "correct_answer": "D",
    },
    # Q21
    {
        "question_number": 21,
        "difficulty": "easy",
        "question_en": (
            "Find the angle between the two hands of a clock when the "
            "minute hand is 16 minutes ahead of the hour hand."
        ),
        "question_hi": (
            "घड़ी की दोनों सुइयों के बीच का कोण ज्ञात कीजिए जब मिनट की सुई "
            "घंटे की सुई से 16 मिनट आगे हो।"
        ),
        "option_a": "80°",
        "option_b": "96°",
        "option_c": "88°",
        "option_d": "72°",
        "correct_answer": "C",
    },
    # Q22
    {
        "question_number": 22,
        "difficulty": "easy",
        "question_en": (
            "What is the angle made by the minute hand in 3 minutes?"
        ),
        "question_hi": (
            "मिनट की सुई 3 मिनट में कितना कोण बनाती है?"
        ),
        "option_a": "12°",
        "option_b": "18°",
        "option_c": "24°",
        "option_d": "30°",
        "correct_answer": "B",
    },
    # Q23
    {
        "question_number": 23,
        "difficulty": "easy",
        "question_en": (
            "What is the angle between the hour hand and minute hand at 8:30?"
        ),
        "question_hi": (
            "8:30 बजे घंटे की सुई और मिनट की सुई के बीच का कोण क्या होगा?"
        ),
        "option_a": "80°",
        "option_b": "90°",
        "option_c": "75°",
        "option_d": "85°",
        "correct_answer": "C",
    },
    # Q24
    {
        "question_number": 24,
        "difficulty": "medium",
        "question_en": (
            "How many times in a day are the hands of a clock in a straight "
            "line but opposite to each other?"
        ),
        "question_hi": (
            "एक दिन में घड़ी की सुइयाँ कितनी बार एक सीधी रेखा में लेकिन "
            "एक-दूसरे के विपरीत होती हैं?"
        ),
        "option_a": "20",
        "option_b": "22",
        "option_c": "24",
        "option_d": "44",
        "correct_answer": "B",
    },
    # Q25
    {
        "question_number": 25,
        "difficulty": "medium",
        "question_en": (
            "How many times do the hands of a clock coincide in a day?"
        ),
        "question_hi": (
            "एक दिन में घड़ी की सुइयाँ कितनी बार मिलती हैं?"
        ),
        "option_a": "20",
        "option_b": "21",
        "option_c": "22",
        "option_d": "24",
        "correct_answer": "C",
    },
    # Q26
    {
        "question_number": 26,
        "difficulty": "hard",
        "question_en": (
            "At what time between 3 and 4 o'clock will the hands of a clock "
            "be together?"
        ),
        "question_hi": (
            "3 और 4 बजे के बीच किस समय घड़ी की सुइयाँ एक साथ होंगी?"
        ),
        "option_a": "16⁴/₁₁ min. past 3/3 बजकर 16⁴/₁₁ मिनट",
        "option_b": "15 min. past 3/3 बजकर 15 मिनट",
        "option_c": "17¹/₁₁ min. past 3/3 बजकर 17¹/₁₁ मिनट",
        "option_d": "18 min. past 3/3 बजकर 18 मिनट",
        "correct_answer": "A",
    },
    # Q27
    {
        "question_number": 27,
        "difficulty": "easy",
        "question_en": (
            "What is the angle between the hour hand and minute hand at 2:30?"
        ),
        "question_hi": (
            "2:30 बजे घंटे की सुई और मिनट की सुई के बीच का कोण क्या होगा?"
        ),
        "option_a": "105°",
        "option_b": "90°",
        "option_c": "75°",
        "option_d": "115°",
        "correct_answer": "A",
    },
    # Q28
    {
        "question_number": 28,
        "difficulty": "hard",
        "question_en": (
            "A clock with only dots marking 3, 6, 9 and 12 positions has been "
            "kept upside down in front of a mirror. A person reads the time in "
            "the reflection of the clock as 9:50. What is the actual time?"
        ),
        "question_hi": (
            "एक घड़ी जिसमें केवल 3, 6, 9 और 12 स्थान अंकित हैं, को दर्पण के सामने "
            "उल्टा रखा गया है। एक व्यक्ति प्रतिबिंब में समय 9:50 देखता है। "
            "वास्तविक समय क्या है?"
        ),
        "option_a": "2:10",
        "option_b": "8:40",
        "option_c": "3:20",
        "option_d": "9:10",
        "correct_answer": "B",
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
