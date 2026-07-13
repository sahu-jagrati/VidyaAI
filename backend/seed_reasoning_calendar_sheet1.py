"""
seed_reasoning_calendar_sheet1.py
====================================
Seeds questions 1-11 (Calendar) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Calendar
Run     : python seed_reasoning_calendar_sheet1.py

Answer key verification:
  Q1:  1992=leap year; 1900,1800 not leap (century÷100 not÷400); 1882 not÷4
       -> 1992 is the only leap year = odd one out                                    -> A
  Q2:  Leap years between 2009-2019: 2012, 2016 -> 2                                 -> A
  Q3:  1st century (1-100 AD): 100÷4=25, minus 100 (not÷400) -> 24                  -> C
  Q4:  2nd century (101-200 AD): same rule, 200 not÷400 -> 24                        -> C
  Q5:  4th century (301-400 AD): 400 IS÷400 -> all 25 are leap years -> 25           -> B
  Q6:  400 yrs: 100(div by 4) - 4(century) + 1(div by 400) = 97 leap yrs -> 97      -> C
  Q7:  29th date in 400 yrs: 11 months×400 + Feb(97 times) = 4400+97 = 4497          -> D
  Q8:  Tuesday + (37 mod 7 = 2) = Thursday                                           -> B
  Q9:  Thursday - (22 mod 7 = 1) = Wednesday                                         -> A
  Q10: Aug 4 = Tuesday; 26-4=22 days; 22 mod 7=1; Tuesday+1 = Wednesday             -> C
  Q11: 30th=Sunday; 30-1=29 days; 29 mod 7=1; Sunday-1 = Saturday                   -> A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401 — registers Subscription with SQLAlchemy

SOURCE  = "Gagan_Pratap_Reasoning_Calendar_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Calendar"

QUESTIONS = [
    # Q1
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": "Find the odd one out: 1992, 1900, 1800, 1882",
        "question_hi": "निम्नलिखित में से विषम छाँटिए: 1992, 1900, 1800, 1882",
        "option_a": "1992",
        "option_b": "1900",
        "option_c": "1800",
        "option_d": "1882",
        "correct_answer": "A",
    },
    # Q2
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": "How many leap years are there between year 2009 and 2019?",
        "question_hi": "वर्ष 2009 और 2019 के बीच अधिवर्षों की संख्या बताइए?",
        "option_a": "2",
        "option_b": "3",
        "option_c": "4",
        "option_d": "1",
        "correct_answer": "A",
    },
    # Q3
    {
        "question_number": 3,
        "difficulty": "medium",
        "question_en": "How many leap years were there in the first century?",
        "question_hi": "पहली शताब्दी में कुल कितने अधिवर्ष थे?",
        "option_a": "25",
        "option_b": "23",
        "option_c": "24",
        "option_d": "26",
        "correct_answer": "C",
    },
    # Q4
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": "How many leap years were there in the second century?",
        "question_hi": "दूसरी शताब्दी में कुल कितने अधिवर्ष थे?",
        "option_a": "48",
        "option_b": "72",
        "option_c": "24",
        "option_d": "25",
        "correct_answer": "C",
    },
    # Q5
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": "How many leap years were there in the fourth century?",
        "question_hi": "चौथी शताब्दी में कुल कितने अधिवर्ष थे?",
        "option_a": "24",
        "option_b": "25",
        "option_c": "97",
        "option_d": "72",
        "correct_answer": "B",
    },
    # Q6
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": "How many times does 29th February come in 400 years?",
        "question_hi": "400 वर्षों में कुल कितनी बार 29 फरवरी आती है?",
        "option_a": "400",
        "option_b": "100",
        "option_c": "97",
        "option_d": "96",
        "correct_answer": "C",
    },
    # Q7
    {
        "question_number": 7,
        "difficulty": "hard",
        "question_en": "How many times does 29th date come in 400 years?",
        "question_hi": "400 वर्षों में कुल कितनी बार 29 तारीख आती है?",
        "option_a": "96",
        "option_b": "97",
        "option_c": "4800",
        "option_d": "4497",
        "correct_answer": "D",
    },
    # Q8
    {
        "question_number": 8,
        "difficulty": "easy",
        "question_en": "If today is Tuesday then what day will it be after 37 days?",
        "question_hi": "यदि आज मंगलवार है तो आज से 37 दिन बाद कौन सा दिन होगा?",
        "option_a": "Wednesday/बुधवार",
        "option_b": "Thursday/गुरुवार",
        "option_c": "Tuesday/मंगलवार",
        "option_d": "Friday/शुक्रवार",
        "correct_answer": "B",
    },
    # Q9
    {
        "question_number": 9,
        "difficulty": "easy",
        "question_en": "If today is Thursday then what was the day before 22 days?",
        "question_hi": "यदि आज गुरूवार है तो आज से 22 दिन पहले कौन सा दिन था?",
        "option_a": "Wednesday/बुधवार",
        "option_b": "Thursday/गुरुवार",
        "option_c": "Monday/सोमवार",
        "option_d": "Tuesday/मंगलवार",
        "correct_answer": "A",
    },
    # Q10
    {
        "question_number": 10,
        "difficulty": "easy",
        "question_en": (
            "Today on 4th August it is Tuesday. "
            "What day will it be on the 26th of this month?"
        ),
        "question_hi": (
            "आज 4 अगस्त मंगलवार का दिन है तब इसी माह की 26 तारीख को कौनसा दिन होगा?"
        ),
        "option_a": "Thursday/गुरुवार",
        "option_b": "Tuesday/मंगलवार",
        "option_c": "Wednesday/बुधवार",
        "option_d": "Monday/सोमवार",
        "correct_answer": "C",
    },
    # Q11
    {
        "question_number": 11,
        "difficulty": "easy",
        "question_en": (
            "If it is Sunday on the 30th of a month, "
            "then what day was it on the 1st of that month?"
        ),
        "question_hi": (
            "किसी महीने की 30 तारीख को रविवार है तो उस महीने की 1 तारीख को कौनसा दिन था?"
        ),
        "option_a": "Saturday/शनिवार",
        "option_b": "Friday/शुक्रवार",
        "option_c": "Sunday/रविवार",
        "option_d": "Monday/सोमवार",
        "correct_answer": "A",
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
