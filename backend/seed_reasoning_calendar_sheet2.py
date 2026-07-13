"""
seed_reasoning_calendar_sheet2.py
====================================
Seeds questions 12-22 (Calendar) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Calendar
Run     : python seed_reasoning_calendar_sheet2.py

Answer key verification:
  Q12: 60 weeks = 420 days; 420 mod 7 = 0 -> same day as Friday                     -> C
  Q13: today-4=Sun -> today=Thu; tomorrow+3=today+4=Thu+4=Monday                     -> B
  Q14: today-6=Mon -> today=Sun; tomorrow+8=today+9=Sun+9=Tue                        -> A
  Q15: today+6=Sat -> today=Sun; yesterday-9=today-10=Sun-10=Sun-3=Thursday          -> D
  Q16: today-11=Mon -> today=Fri; 5th day (today=day1)=Fri+4=Tuesday                 -> B
  Q17: today=Sun; 24th day (today=day1)=Sun+23=Sun+2=Tuesday                         -> A
  Q18: 4 Sep 1996 to 4 Aug 2020 = 23y 11m; 4 to 10 Aug = 6 days
       -> 23 years 11 months 6 days                                                   -> C
  Q19: 10 Oct 2000 to 10 Jun 2020 = 19y 8m; 10 Jun to 5 Jul = 25 days (incl=26)
       -> 19 years 8 months 26 days                                                   -> B
  Q20: 2003 to 2015 = 12 yrs; leaps 2004,2008,2012 = 3 leaps;
       odd days = 3×2 + 9×1 = 15 mod 7 = 1; Fri+1 = Saturday                        -> D
  Q21: 2010 to 2029 = 19 yrs; leaps 2012,2016,2020,2024,2028 = 5 leaps;
       odd days = 5×2 + 14×1 = 24 mod 7 = 3; Sat+3 = Tuesday                        -> A
  Q22: 2009 to 2019 = 10 yrs (forward); leaps 2012,2016 = 2 leaps;
       odd days = 2×2 + 8×1 = 12 mod 7 = 5; Tue-5 = Thursday                        -> C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Calendar_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Calendar"

QUESTIONS = [
    # Q12
    {
        "question_number": 12,
        "difficulty": "easy",
        "question_en": "If today is Friday then what day will it be after 60 weeks?",
        "question_hi": "यदि आज शुक्रवार है तो आज से 60 सप्ताह बाद कौनसा दिन होगा?",
        "option_a": "Monday/सोमवार",
        "option_b": "Tuesday/मंगलवार",
        "option_c": "Friday/शुक्रवार",
        "option_d": "Saturday/शनिवार",
        "correct_answer": "C",
    },
    # Q13
    {
        "question_number": 13,
        "difficulty": "medium",
        "question_en": (
            "If 3 days before yesterday was Sunday then "
            "what will be 3 days after tomorrow?"
        ),
        "question_hi": (
            "यदि बीते हुए कल से 3 दिन पहले रविवार था तब "
            "आने वाले कल के 3 दिन बाद क्या होगा?"
        ),
        "option_a": "Sunday/रविवार",
        "option_b": "Monday/सोमवार",
        "option_c": "Tuesday/मंगलवार",
        "option_d": "Wednesday/बुधवार",
        "correct_answer": "B",
    },
    # Q14
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": (
            "If 5 days before yesterday was Monday then "
            "what will be 8 days after tomorrow?"
        ),
        "question_hi": (
            "यदि बीते हुए कल से 5 दिन पहले सोमवार था तब "
            "आने वाले कल के 8 दिन बाद क्या होगा?"
        ),
        "option_a": "Tuesday/मंगलवार",
        "option_b": "Sunday/रविवार",
        "option_c": "Monday/सोमवार",
        "option_d": "Wednesday/बुधवार",
        "correct_answer": "A",
    },
    # Q15
    {
        "question_number": 15,
        "difficulty": "medium",
        "question_en": (
            "If it is Saturday after 6 days. What was 9 days before yesterday?"
        ),
        "question_hi": (
            "यदि 6 दिन बाद शनिवार है तो बीते हुए कल से 9 दिन पहले कौनसा दिन था?"
        ),
        "option_a": "Monday/सोमवार",
        "option_b": "Friday/शुक्रवार",
        "option_c": "Wednesday/बुधवार",
        "option_d": "Thursday/गुरुवार",
        "correct_answer": "D",
    },
    # Q16
    {
        "question_number": 16,
        "difficulty": "medium",
        "question_en": (
            "If 10 days before yesterday was Monday then "
            "what will be 5th day from today?"
        ),
        "question_hi": (
            "यदि बीते हुए कल से 10 दिन पहले सोमवार था तब "
            "आज से 5वाँ दिन कौनसा होगा?"
        ),
        "option_a": "Monday/सोमवार",
        "option_b": "Tuesday/मंगलवार",
        "option_c": "Saturday/शनिवार",
        "option_d": "Sunday/रविवार",
        "correct_answer": "B",
    },
    # Q17
    {
        "question_number": 17,
        "difficulty": "easy",
        "question_en": "If today is Sunday then what will be 24th day from today?",
        "question_hi": "यदि आज रविवार है तो आज से 24वाँ दिन कौनसा होगा?",
        "option_a": "Tuesday/मंगलवार",
        "option_b": "Wednesday/बुधवार",
        "option_c": "Thursday/गुरुवार",
        "option_d": "Friday/शुक्रवार",
        "correct_answer": "A",
    },
    # Q18
    {
        "question_number": 18,
        "difficulty": "medium",
        "question_en": (
            "Ankit was born on 4 September 1996. "
            "Then how old will he be on 10th August 2020?"
        ),
        "question_hi": (
            "अंकित का जन्म 4 सितंबर 1996 को हुआ। "
            "तब वह 10 अगस्त 2020 को कितने साल, माह और दिन का होगा?"
        ),
        "option_a": "23 years 11 months 4 days/23 साल 11 महीने 4 दिन",
        "option_b": "23 years 10 months 2 days/23 साल 10 महीने 2 दिन",
        "option_c": "23 years 11 months 6 days/23 साल 11 महीने 6 दिन",
        "option_d": "24 years 10 months 4 days/24 साल 10 महीने 4 दिन",
        "correct_answer": "C",
    },
    # Q19
    {
        "question_number": 19,
        "difficulty": "medium",
        "question_en": (
            "Riya was born on 10 October 2000. "
            "Then how old will she be on 5 July 2020?"
        ),
        "question_hi": (
            "रिया का जन्म 10 अक्टूबर 2000 को हुआ। "
            "तब वह 5 जुलाई 2020 को कितने साल, माह और दिन की होगी?"
        ),
        "option_a": "19 years 6 months 26 days/19 साल 6 महीने 26 दिन",
        "option_b": "19 years 8 months 26 days/19 साल 8 महीने 26 दिन",
        "option_c": "20 years 2 months 24 days/20 साल 2 महीने 24 दिन",
        "option_d": "20 years 8 months 26 days/20 साल 8 महीने 26 दिन",
        "correct_answer": "B",
    },
    # Q20
    {
        "question_number": 20,
        "difficulty": "hard",
        "question_en": (
            "If it was Friday on 15 August 2003, "
            "then what day would it be on 15 August 2015?"
        ),
        "question_hi": (
            "यदि 15 अगस्त 2003 को शुक्रवार था "
            "तब 15 अगस्त 2015 को कौनसा दिन होगा?"
        ),
        "option_a": "Sunday/रविवार",
        "option_b": "Monday/सोमवार",
        "option_c": "Wednesday/बुधवार",
        "option_d": "Saturday/शनिवार",
        "correct_answer": "D",
    },
    # Q21
    {
        "question_number": 21,
        "difficulty": "hard",
        "question_en": (
            "If it was Saturday on 10 January 2010, "
            "then what day would it be on 10 January 2029?"
        ),
        "question_hi": (
            "यदि 10 जनवरी 2010 को शनिवार था "
            "तो 10 जनवरी 2029 को कौनसा दिन होगा?"
        ),
        "option_a": "Tuesday/मंगलवार",
        "option_b": "Monday/सोमवार",
        "option_c": "Wednesday/बुधवार",
        "option_d": "Sunday/रविवार",
        "correct_answer": "A",
    },
    # Q22
    {
        "question_number": 22,
        "difficulty": "hard",
        "question_en": (
            "If it was Tuesday on 10 October 2019, "
            "then what day was it on 10 October 2009?"
        ),
        "question_hi": (
            "यदि 10 अक्टूबर 2019 को मंगलवार था "
            "तो 10 अक्टूबर 2009 को कौनसा दिन था?"
        ),
        "option_a": "Monday/सोमवार",
        "option_b": "Friday/शुक्रवार",
        "option_c": "Thursday/गुरुवार",
        "option_d": "Sunday/रविवार",
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
