"""
seed_reasoning_calendar_sheet3.py
====================================
Seeds questions 23-34 (Calendar) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Calendar
Run     : python seed_reasoning_calendar_sheet3.py

Answer key verification (all use odd-days method):
  Q23: Feb 20 base, 2004→2020 16 yrs; current-yr leaps 2004,08,12,16=4
       odd = 4×2+12×1=20 mod 7=6; Sun+6=Saturday                                    -> B
  Q24: Mar 20 base, 2012→2024 12 yrs backward; next-yr leaps 2016,20,24=3
       odd=3×2+9×1=15 mod 7=1; Sun-1=Saturday                                       -> A
  Q25: Aug 10 base, 2009→2020 11 yrs; next-yr leaps 2012,16,20=3
       odd=3×2+8×1=14 mod 7=0; same day=Monday                                      -> C
  Q26: Apr 29 to Aug 15: 1+31+30+31+15=108; 108 mod 7=3; Fri-3=Tuesday              -> D
  Q27: Jan 25 to Apr 30 (2004 leap): 6+29+31+30=96; mod 7=5; Sat-5=Monday           -> A
  Q28: Jan 1 to Aug 6 in 2020 (leap): 218 days; mod 7=1; Thu-1=Wednesday            -> C
  Q29: Feb 25 to Mar 25 (2005): 3+25=28; mod 7=0; same day=Monday                   -> A
  Q30: Aug 10 to Dec 31: 21+30+31+30+31=143; mod 7=3; Mon+3=Thursday                -> D
  Q31: Aug 15 2003→Aug 15 2014 (11 yrs)=14 mod 7=0 (Sun); then Aug 15 2014→
       May 27 2015=285 days; mod 7=5; Sun+5=Friday                                  -> A
  Q32: Oct 31 2007→Oct 31 2013 (6 yrs)=8 mod 7=1; then +61 mod 7=5; total+6;
       Sat-6=Sunday                                                                   -> C
  Q33: Feb 20 2004→Feb 20 2016 (12 yrs)=15 mod 7=1; Fri+1=Sat; then Feb 20→
       Mar 20 2016=29 days; mod 7=1; Sat+1=Sunday                                   -> B
  Q34: Jan 5 1997→Jan 5 2020 (23 yrs)=28 mod 7=0; then Jan 5→Aug 10 2020=218;
       mod 7=1; Mon-1=Sunday                                                          -> A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Calendar_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Calendar"

QUESTIONS = [
    # Q23
    {
        "question_number": 23,
        "difficulty": "hard",
        "question_en": (
            "If it was Sunday on 20 February 2004, "
            "then what day would it be on 20 February 2020?"
        ),
        "question_hi": (
            "यदि 20 फरवरी 2004 को रविवार था "
            "तो 20 फरवरी 2020 को कौनसा दिन होगा?"
        ),
        "option_a": "Monday/सोमवार",
        "option_b": "Saturday/शनिवार",
        "option_c": "Friday/शुक्रवार",
        "option_d": "Sunday/रविवार",
        "correct_answer": "B",
    },
    # Q24
    {
        "question_number": 24,
        "difficulty": "hard",
        "question_en": (
            "If it is Sunday on 20th March 2024, "
            "then what day was on 20 March 2012?"
        ),
        "question_hi": (
            "यदि 20 मार्च 2024 को रविवार था "
            "तो 20 मार्च 2012 को कौनसा दिन था?"
        ),
        "option_a": "Saturday/शनिवार",
        "option_b": "Sunday/रविवार",
        "option_c": "Monday/सोमवार",
        "option_d": "Tuesday/मंगलवार",
        "correct_answer": "A",
    },
    # Q25
    {
        "question_number": 25,
        "difficulty": "hard",
        "question_en": (
            "If it was Monday on 10 August 2020, "
            "then what day was on 10 August 2009?"
        ),
        "question_hi": (
            "यदि 10 अगस्त 2020 को सोमवार था "
            "तब 10 अगस्त 2009 को कौनसा दिन था?"
        ),
        "option_a": "Friday/शुक्रवार",
        "option_b": "Thursday/गुरुवार",
        "option_c": "Monday/सोमवार",
        "option_d": "Wednesday/बुधवार",
        "correct_answer": "C",
    },
    # Q26
    {
        "question_number": 26,
        "difficulty": "medium",
        "question_en": (
            "If it was Friday on 15 August 2005, "
            "then what day was on 29 April 2005?"
        ),
        "question_hi": (
            "यदि 15 अगस्त 2005 को शुक्रवार था "
            "तो 29 अप्रैल 2005 को कौनसा दिन था?"
        ),
        "option_a": "Thursday/गुरुवार",
        "option_b": "Monday/सोमवार",
        "option_c": "Friday/शुक्रवार",
        "option_d": "Tuesday/मंगलवार",
        "correct_answer": "D",
    },
    # Q27
    {
        "question_number": 27,
        "difficulty": "medium",
        "question_en": (
            "If 30 April 2004 was a Saturday. "
            "What day of the week was on 25 January 2004?"
        ),
        "question_hi": (
            "यदि 30 अप्रैल 2004 को शनिवार था "
            "तो 25 जनवरी 2004 को कौनसा दिन था?"
        ),
        "option_a": "Monday/सोमवार",
        "option_b": "Tuesday/मंगलवार",
        "option_c": "Wednesday/बुधवार",
        "option_d": "Thursday/गुरुवार",
        "correct_answer": "A",
    },
    # Q28
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": (
            "If 6 August 2020 is Thursday. "
            "What day of the week was on 1 January 2020?"
        ),
        "question_hi": (
            "यदि 6 अगस्त 2020 को गुरूवार था "
            "तो 1 जनवरी 2020 को कौनसा दिन था?"
        ),
        "option_a": "Sunday/रविवार",
        "option_b": "Thursday/गुरुवार",
        "option_c": "Wednesday/बुधवार",
        "option_d": "Friday/शुक्रवार",
        "correct_answer": "C",
    },
    # Q29
    {
        "question_number": 29,
        "difficulty": "easy",
        "question_en": (
            "If 25 February 2005 is a Monday. "
            "What day of the week was on 25 March 2005?"
        ),
        "question_hi": (
            "यदि 25 फरवरी 2005 को सोमवार था "
            "तो 25 मार्च 2005 का कौनसा दिन होगा?"
        ),
        "option_a": "Monday/सोमवार",
        "option_b": "Sunday/रविवार",
        "option_c": "Tuesday/मंगलवार",
        "option_d": "Wednesday/बुधवार",
        "correct_answer": "A",
    },
    # Q30
    {
        "question_number": 30,
        "difficulty": "medium",
        "question_en": (
            "If 10 August 2020 is a Monday. "
            "What day of the week will be on 31 December 2020?"
        ),
        "question_hi": (
            "यदि 10 अगस्त 2020 को सोमवार था "
            "तो 31 दिसंबर 2020 को कौनसा दिन होगा?"
        ),
        "option_a": "Monday/सोमवार",
        "option_b": "Wednesday/बुधवार",
        "option_c": "Friday/शुक्रवार",
        "option_d": "Thursday/गुरुवार",
        "correct_answer": "D",
    },
    # Q31
    {
        "question_number": 31,
        "difficulty": "hard",
        "question_en": (
            "If it was Sunday on 15 August 2003 "
            "then what day would it be on 27 May 2015?"
        ),
        "question_hi": (
            "यदि 15 अगस्त 2003 को रविवार था "
            "तो 27 मई 2015 को कौनसा दिन होगा?"
        ),
        "option_a": "Friday/शुक्रवार",
        "option_b": "Saturday/शनिवार",
        "option_c": "Thursday/गुरुवार",
        "option_d": "Monday/सोमवार",
        "correct_answer": "A",
    },
    # Q32
    {
        "question_number": 32,
        "difficulty": "hard",
        "question_en": (
            "If it was Saturday on 31 December 2013 "
            "then what day was on 31 October 2007?"
        ),
        "question_hi": (
            "यदि 31 दिसंबर 2013 को शनिवार था "
            "तो 31 अक्टूबर 2007 को कौनसा दिन था?"
        ),
        "option_a": "Monday/सोमवार",
        "option_b": "Tuesday/मंगलवार",
        "option_c": "Sunday/रविवार",
        "option_d": "Wednesday/बुधवार",
        "correct_answer": "C",
    },
    # Q33
    {
        "question_number": 33,
        "difficulty": "hard",
        "question_en": (
            "If it was Friday on 20 February 2004, "
            "then what day would it be on 20 March 2016?"
        ),
        "question_hi": (
            "यदि 20 फरवरी 2004 को शुक्रवार था "
            "तो 20 मार्च 2016 को कौनसा दिन होगा?"
        ),
        "option_a": "Tuesday/मंगलवार",
        "option_b": "Sunday/रविवार",
        "option_c": "Friday/शुक्रवार",
        "option_d": "Monday/सोमवार",
        "correct_answer": "B",
    },
    # Q34
    {
        "question_number": 34,
        "difficulty": "hard",
        "question_en": (
            "If it was Monday on 10 August 2020, "
            "then what day was on 5 January 1997?"
        ),
        "question_hi": (
            "यदि 10 अगस्त 2020 को सोमवार था "
            "तो 5 जनवरी 1997 को कौनसा दिन था?"
        ),
        "option_a": "Sunday/रविवार",
        "option_b": "Monday/सोमवार",
        "option_c": "Tuesday/मंगलवार",
        "option_d": "Saturday/शनिवार",
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
