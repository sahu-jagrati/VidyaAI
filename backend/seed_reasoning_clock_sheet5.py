"""
seed_reasoning_clock_sheet5.py
====================================
Seeds questions 36-41 (Clock) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Clock
Run     : python seed_reasoning_clock_sheet5.py

Answer key verification:
  Q36: correct interval=720/11; actual=63 min; gain/interval=27/11;
       in 24h: (1440/63)×(27/11)=4320/77=56 8/77 min gain                         -> A
  Q37: 10-11 right angle: |300-5.5t|=90 -> t=420/11=38 2/11 min past 10            -> A
  Q38: 8-9 opposite: |240-5.5t|=180 -> t=120/11=10 10/11 min past 8                -> A
  Q39: 3-4, minute 4 marks behind hour: 15+t/12-t=4 -> t=12 min past 3             -> A
  Q40: 4:15 -> |120-82.5|=37.5°                                                     -> C
  Q41: 2-3 opposite: |60-5.5t|=180 -> t=480/11=43 7/11 min past 2                  -> B
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Clock_Sheet5"
SUBJECT = "Reasoning"
TOPIC   = "Clock"

QUESTIONS = [
    # Q36
    {
        "question_number": 36,
        "difficulty": "hard",
        "question_en": (
            "The minute-hand of a clock overtakes the hour hand at intervals of "
            "63 minutes of correct time. How much in a day does the clock gain or lose?"
        ),
        "question_hi": (
            "एक घड़ी की मिनट की सुई, घंटे की सुई से 63 मिनट के अंतराल पर "
            "आगे निकल जाती है। एक दिन में घड़ी कितनी आगे या पीछे हो जाती है?"
        ),
        "option_a": "56⁸/₇₇ min. gain/56⁸/₇₇ मिनट आगे",
        "option_b": "56⁸/₇₇ min. lose/56⁸/₇₇ मिनट पीछे",
        "option_c": "57⁸/₇₇ min. gain/57⁸/₇₇ मिनट आगे",
        "option_d": "57⁸/₇₇ min. lose/57⁸/₇₇ मिनट पीछे",
        "correct_answer": "A",
    },
    # Q37
    {
        "question_number": 37,
        "difficulty": "hard",
        "question_en": (
            "At which of the following times between 10 and 11 O'clock will the "
            "hand of a clock be at right angle?"
        ),
        "question_hi": (
            "10 से 11 बजे के बीच निम्नलिखित में से किस समय घड़ी की सुई "
            "समकोण पर होगी?"
        ),
        "option_a": "38²/₁₁ min. past 10/10 बजकर 38²/₁₁ मिनट",
        "option_b": "6⁵/₁₁ min. past 10/10 बजकर 6⁵/₁₁ मिनट",
        "option_c": "38³/₁₁ min. past 10/10 बजकर 38³/₁₁ मिनट",
        "option_d": "8²/₁₁ min. past 10/10 बजकर 8²/₁₁ मिनट",
        "correct_answer": "A",
    },
    # Q38
    {
        "question_number": 38,
        "difficulty": "hard",
        "question_en": (
            "Find at what time between 8 and 9 O'clock will the hands of a clock "
            "be in the same straight line but not together."
        ),
        "question_hi": (
            "8 और 9 बजे के बीच किस समय घड़ी की सुइयाँ एक ही सीधी रेखा में "
            "होंगी लेकिन एक साथ नहीं होंगी।"
        ),
        "option_a": "10¹⁰/₁₁ min. past 8/8 बजकर 10¹⁰/₁₁ मिनट",
        "option_b": "10⁹/₁₁ min. past 8/8 बजकर 10⁹/₁₁ मिनट",
        "option_c": "11¹⁰/₁₁ min. past 8/8 बजकर 11¹⁰/₁₁ मिनट",
        "option_d": "None of these/इनमें से कोई नहीं",
        "correct_answer": "A",
    },
    # Q39
    {
        "question_number": 39,
        "difficulty": "medium",
        "question_en": (
            "At what time between 3 and 4 is the minute-hand 4 minutes "
            "behind the hour-hand?"
        ),
        "question_hi": (
            "3 और 4 के बीच किस समय मिनट की सुई घण्टा की सुई से 4 "
            "मिनट पीछे होगी?"
        ),
        "option_a": "12 minutes past 3/3 बजकर 12 मिनट",
        "option_b": "11 minutes past 3/3 बजकर 11 मिनट",
        "option_c": "19 minutes past 3/3 बजकर 19 मिनट",
        "option_d": "None of these/इनमें से कोई नहीं",
        "correct_answer": "A",
    },
    # Q40
    {
        "question_number": 40,
        "difficulty": "easy",
        "question_en": (
            "Find the angle between the two hands of a clock when it is "
            "15 minutes past 4 O'clock."
        ),
        "question_hi": (
            "एक घड़ी की दोनों सुइयों के बीच का कोण ज्ञात कीजिए जब 4 "
            "बजकर 15 मिनट हो रहे हों।"
        ),
        "option_a": "38.5°",
        "option_b": "36.5°",
        "option_c": "37.5°",
        "option_d": "None of these/इनमें से कोई नहीं",
        "correct_answer": "C",
    },
    # Q41
    {
        "question_number": 41,
        "difficulty": "hard",
        "question_en": (
            "Find at what time between 2 and 3 O'clock will the hands of a clock "
            "be in the same straight line but not together."
        ),
        "question_hi": (
            "2 और 3 बजे के बीच किस समय घड़ी की सुइयाँ एक ही सीधी रेखा "
            "में होंगी लेकिन एक साथ नहीं होंगी।"
        ),
        "option_a": "43⁶/₁₁ min. past 2/2 बजकर 43⁶/₁₁ मिनट",
        "option_b": "43⁷/₁₁ min. past 2/2 बजकर 43⁷/₁₁ मिनट",
        "option_c": "43³/₁₁ min. past 2/2 बजकर 43³/₁₁ मिनट",
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
