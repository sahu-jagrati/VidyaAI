"""
seed_reasoning_clock_sheet7.py
====================================
Seeds questions 50-57 (Clock) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Clock
Run     : python seed_reasoning_clock_sheet7.py

Answer key verification:
  Q50: 9:32 -> |270-176|=94°                                                       -> A
  Q51: hour moves 10° in 20 min; minute=20×6=120°                                  -> C
  Q52: 5-6 coincide: t=5×60/11=300/11=27 3/11 min past 5                           -> D
  Q53: 7:38 -> |210-209|=1°                                                         -> A
  Q54: second moves 300° in 50s; minute=50×0.1=5°                                  -> D
  Q55: hour 135° at 0.5°/min=270min=4h30m; 3:00+4:30=7:30                          -> A
  Q56: hands opposite 11 times in 12 hours                                          -> C
  Q57: true elapsed=1740×(1440/1450)=1728min=28h48min                              -> B
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Clock_Sheet7"
SUBJECT = "Reasoning"
TOPIC   = "Clock"

QUESTIONS = [
    # Q50
    {
        "question_number": 50,
        "difficulty": "easy",
        "question_en": (
            "At what angle are the two hands of a clock inclined at "
            "32 minutes past 9?"
        ),
        "question_hi": (
            "9 बजकर 32 मिनट पर घड़ी की दोनों सुइयाँ किस कोण पर झुकी हुई हैं?"
        ),
        "option_a": "94°",
        "option_b": "95°",
        "option_c": "93°",
        "option_d": "92°",
        "correct_answer": "A",
    },
    # Q51
    {
        "question_number": 51,
        "difficulty": "medium",
        "question_en": (
            "How many degrees will the minute hand move, in the same time, "
            "in which the hour hand moves 10°?"
        ),
        "question_hi": (
            "उसी समय में मिनट की सुई कितने डिग्री घूमेगी, जिसमें घंटे की सुई "
            "10° घूमती है?"
        ),
        "option_a": "130°",
        "option_b": "115°",
        "option_c": "120°",
        "option_d": "None of these/इनमें से कोई नहीं",
        "correct_answer": "C",
    },
    # Q52
    {
        "question_number": 52,
        "difficulty": "hard",
        "question_en": (
            "At what time between 5 and 6 are the hands of a clock "
            "coinciding each other?"
        ),
        "question_hi": (
            "5 और 6 के बीच किस समय घड़ी की सुइयाँ एक दूसरे से मिलती हैं?"
        ),
        "option_a": "22 minutes past 5/5 बजकर 22 मिनट",
        "option_b": "30 minutes past 5/5 बजकर 30 मिनट",
        "option_c": "22⁸/₁₁ minutes past 5/5 बजकर 22⁸/₁₁ मिनट",
        "option_d": "27³/₁₁ minutes past 5/5 बजकर 27³/₁₁ मिनट",
        "correct_answer": "D",
    },
    # Q53
    {
        "question_number": 53,
        "difficulty": "medium",
        "question_en": (
            "At what angle are the two hands of a clock inclined at "
            "38 minutes past 7?"
        ),
        "question_hi": (
            "7 बजकर 38 मिनट पर घड़ी की दोनों सुइयाँ किस कोण पर झुकी हुई हैं?"
        ),
        "option_a": "01°",
        "option_b": "02°",
        "option_c": "03°",
        "option_d": "1½°",
        "correct_answer": "A",
    },
    # Q54
    {
        "question_number": 54,
        "difficulty": "medium",
        "question_en": (
            "How many degrees will the minute hand move, in the same time, "
            "in which the second hand moves 300°?"
        ),
        "question_hi": (
            "उसी समय में मिनट की सुई कितने डिग्री घूमेगी, जिसमें सेकंड की "
            "सुई 300° घूमेगी?"
        ),
        "option_a": "6°",
        "option_b": "10°",
        "option_c": "8°",
        "option_d": "5°",
        "correct_answer": "D",
    },
    # Q55
    {
        "question_number": 55,
        "difficulty": "medium",
        "question_en": (
            "A clock shows 3:00 Hrs. What will be the time after "
            "hour needle moves 135°?"
        ),
        "question_hi": (
            "एक घड़ी 3:00 बजे दिखा रही है। घंटे की सुई 135° घूमने के बाद "
            "समय क्या होगा?"
        ),
        "option_a": "7:30",
        "option_b": "8:30",
        "option_c": "7:40",
        "option_d": "6:30",
        "correct_answer": "A",
    },
    # Q56
    {
        "question_number": 56,
        "difficulty": "easy",
        "question_en": (
            "How many times do the hands of a clock point opposite "
            "to each other in 12 hours?"
        ),
        "question_hi": (
            "12 घंटे में एक घड़ी की सुइयाँ कितनी बार एक दूसरे के विपरीत होती हैं?"
        ),
        "option_a": "6 times/6 बार",
        "option_b": "10 times/10 बार",
        "option_c": "11 times/11 बार",
        "option_d": "12 times/12 बार",
        "correct_answer": "C",
    },
    # Q57
    {
        "question_number": 57,
        "difficulty": "hard",
        "question_en": (
            "A clock is set right at 8 am. The clock gains 10 minutes in 24 hours. "
            "What will be the true time when the clock indicates 1 pm on the "
            "following day?"
        ),
        "question_hi": (
            "एक घड़ी को सुबह 8 बजे ठीक किया गया है। घड़ी 24 घंटे में 10 मिनट "
            "आगे बढ़ जाती है। अगले दिन जब घड़ी दोपहर 1 बजे दिखाएगी तो सही "
            "समय क्या होगा?"
        ),
        "option_a": "28 hrs./28 घंटे",
        "option_b": "28 hrs. 48 min/28 बजकर 48 मिनट",
        "option_c": "28 hrs. 42 min/28 बजकर 42 मिनट",
        "option_d": "None of these/इनमें से कोई नहीं",
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
