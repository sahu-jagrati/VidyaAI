"""
seed_reasoning_calendar_sheet4.py
====================================
Seeds questions 35-46 (Calendar) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Calendar
Run     : python seed_reasoning_calendar_sheet4.py

Answer key verification:
  Q35: 7 Feb 1996→7 Feb 2020 (24yrs,6 leaps): 6×2+18=30 mod 7=2.
       7 Feb→15 Jul 2020: 22+31+30+31+30+15=159 mod 7=5. Total=7=0.
       Wed=7 Feb 1996's day                                                           -> D
  Q36: 1 Feb 2008→1 Feb 2016 (8yrs, leaps 2008,2012): 2×2+6=10 mod 7=3;
       Mon-3=Fri. 1 Feb→29 Feb: 28 days=0; 29 Feb 2008=Friday                        -> B
  Q37: 1990 non-leap; 1990→2001 (11yrs, leaps 1992,96,2000=3): 3×2+8=14 mod 7=0;
       2001 non-leap -> same calendar                                                 -> D
  Q38: 2019 non-leap; 2019→2030 (11yrs, leaps 2020,2024,2028=3): 3×2+8=14 mod 7=0;
       2030 non-leap -> same calendar                                                 -> D
  Q39: 2005 non-leap; 2005→2011 (6yrs, leap 2008=1): 1×2+5=7 mod 7=0;
       2011 non-leap -> same calendar                                                 -> B
  Q40: 2017 non-leap; 2017→2023 (6yrs, leap 2020=1): 1×2+5=7 mod 7=0;
       2023 non-leap -> same calendar                                                 -> C
  Q41: 1997 non-leap; 1997→2003 (6yrs, leap 2000=1): 1×2+5=7 mod 7=0;
       2003 non-leap -> same calendar                                                 -> B
  Q42: 1897 non-leap; 1900 NOT leap (century); 1897→1909 (12yrs, leaps 1904,1908=2):
       2×2+10=14 mod 7=0; 1909 non-leap -> same calendar                             -> D
  Q43: 2016 leap; 2016→2044 (28yrs, 7 leaps): 7×2+21=35 mod 7=0;
       2044 leap -> same calendar                                                     -> A
  Q44: 2020 starts Wed; 366=52×7+2; extra days Wed & Thu; Wed appears 53 times        -> B
  Q45: Jan 1 2020=Wed; Aug 1=Wed+3=Sat; Sundays: 2,9,16,23,30 -> 5 times             -> B
  Q46: Century end days cycle: Fri(100),Wed(200),Mon(300),Sun(400);
       Tuesday can never be last day of a century                                     -> C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Calendar_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Calendar"

QUESTIONS = [
    # Q35
    {
        "question_number": 35,
        "difficulty": "hard",
        "question_en": (
            "If it was Wednesday on 15 July 2020, "
            "then what day was on 7 February 1996?"
        ),
        "question_hi": (
            "यदि 15 जुलाई 2020 को बुधवार था "
            "तो 7 फरवरी 1996 को कौनसा दिन था?"
        ),
        "option_a": "Monday/सोमवार",
        "option_b": "Tuesday/मंगलवार",
        "option_c": "Thursday/गुरुवार",
        "option_d": "Wednesday/बुधवार",
        "correct_answer": "D",
    },
    # Q36
    {
        "question_number": 36,
        "difficulty": "hard",
        "question_en": (
            "If it was Monday on 1 February 2016, "
            "then what day was on 29 February 2008?"
        ),
        "question_hi": (
            "यदि 1 फरवरी 2016 को सोमवार था "
            "तो 29 फरवरी 2008 को कौनसा दिन था?"
        ),
        "option_a": "Thursday/गुरुवार",
        "option_b": "Friday/शुक्रवार",
        "option_c": "Saturday/शनिवार",
        "option_d": "Monday/सोमवार",
        "correct_answer": "B",
    },
    # Q37
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": (
            "The calendar of the year 1990 will be equal to "
            "which of the following years?"
        ),
        "question_hi": (
            "वर्ष 1990 का कैलेंडर निम्न में से "
            "कौनसे वर्ष के समान होगा?"
        ),
        "option_a": "1997",
        "option_b": "1996",
        "option_c": "2000",
        "option_d": "2001",
        "correct_answer": "D",
    },
    # Q38
    {
        "question_number": 38,
        "difficulty": "medium",
        "question_en": (
            "The calendar of the year 2019 will be equal to "
            "which of the following years?"
        ),
        "question_hi": (
            "वर्ष 2019 का कैलेंडर निम्न में से "
            "कौनसे वर्ष के समान होगा?"
        ),
        "option_a": "2024",
        "option_b": "2025",
        "option_c": "2028",
        "option_d": "2030",
        "correct_answer": "D",
    },
    # Q39
    {
        "question_number": 39,
        "difficulty": "medium",
        "question_en": (
            "The calendar of the year 2005 will be equal to "
            "which of the following years?"
        ),
        "question_hi": (
            "वर्ष 2005 का कैलेंडर निम्न में से "
            "कौनसे वर्ष के समान होगा?"
        ),
        "option_a": "2016",
        "option_b": "2011",
        "option_c": "2010",
        "option_d": "2008",
        "correct_answer": "B",
    },
    # Q40
    {
        "question_number": 40,
        "difficulty": "medium",
        "question_en": (
            "The calendar of the year 2017 will be equal to "
            "which of the following years?"
        ),
        "question_hi": (
            "वर्ष 2017 निम्न में से कौनसे वर्ष के समान होगा?"
        ),
        "option_a": "2028",
        "option_b": "2024",
        "option_c": "2023",
        "option_d": "2025",
        "correct_answer": "C",
    },
    # Q41
    {
        "question_number": 41,
        "difficulty": "medium",
        "question_en": (
            "The calendar of the year 1997 will be equal to "
            "which of the following years?"
        ),
        "question_hi": (
            "वर्ष 1997 का कैलेंडर निम्न में से "
            "कौनसे वर्ष के समान होगा?"
        ),
        "option_a": "2008",
        "option_b": "2003",
        "option_c": "2004",
        "option_d": "2005",
        "correct_answer": "B",
    },
    # Q42
    {
        "question_number": 42,
        "difficulty": "hard",
        "question_en": (
            "The calendar of the year 1897 will be equal to "
            "which of the following years?"
        ),
        "question_hi": (
            "वर्ष 1897 का कैलेंडर निम्न में से "
            "कौनसे वर्ष के समान होगा?"
        ),
        "option_a": "1908",
        "option_b": "1903",
        "option_c": "1904",
        "option_d": "1909",
        "correct_answer": "D",
    },
    # Q43
    {
        "question_number": 43,
        "difficulty": "hard",
        "question_en": (
            "The calendar of the year 2016 will be equal to "
            "which of the following years?"
        ),
        "question_hi": (
            "वर्ष 2016 का कैलेंडर निम्न में से "
            "कौनसे वर्ष के समान होगा?"
        ),
        "option_a": "2044",
        "option_b": "2024",
        "option_c": "2032",
        "option_d": "2035",
        "correct_answer": "A",
    },
    # Q44
    {
        "question_number": 44,
        "difficulty": "medium",
        "question_en": "How many times will Wednesday come in the year 2020?",
        "question_hi": "वर्ष 2020 में कुल कितनी बार बुधवार आएगा?",
        "option_a": "52 times/52 बार",
        "option_b": "53 times/53 बार",
        "option_c": "54 times/54 बार",
        "option_d": "51 times/51 बार",
        "correct_answer": "B",
    },
    # Q45
    {
        "question_number": 45,
        "difficulty": "medium",
        "question_en": "How many times will Sunday come in August 2020?",
        "question_hi": "अगस्त 2020 में रविवार कुल कितनी बार आएगा?",
        "option_a": "4 times/4 बार",
        "option_b": "5 times/5 बार",
        "option_c": "6 times/6 बार",
        "option_d": "3 times/3 बार",
        "correct_answer": "B",
    },
    # Q46
    {
        "question_number": 46,
        "difficulty": "hard",
        "question_en": (
            "Which of the following days can never be the last day of any century?"
        ),
        "question_hi": (
            "इनमें से कौन सा दिन किसी शताब्दी का अंतिम दिन नहीं हो सकता?"
        ),
        "option_a": "Sunday/रविवार",
        "option_b": "Monday/सोमवार",
        "option_c": "Tuesday/मंगलवार",
        "option_d": "Wednesday/बुधवार",
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
