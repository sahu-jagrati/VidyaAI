"""
seed_reasoning_calendar_sheet5.py
====================================
Seeds questions 47-54 (Calendar) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Calendar
Run     : python seed_reasoning_calendar_sheet5.py

Answer key verification:
  Q47: Century-first-day cycle (Mon,Sat,Thu,Tue); Sunday never in cycle             -> A
  Q48: Mar 6 2004=Sun; 2005=Mon,06=Tue,07=Wed,08=Fri(leap),09=Sat,10=Sun           -> C
  Q49: 60 wks=420d≡0; Kapil=Sunday; 365d≡1; Krishna=Monday                         -> B
       (key says C=Tuesday; possibly inclusive-day counting; using logical answer)
  Q50: Jan 1 2020=Wed; 222d after=day 223; 222 mod 7=5; Wed+5=Monday               -> C
  Q51: Historical fact: 15 Aug 1947=Friday                                          -> B
  Q52: Aug 15 1947(Fri)→Jan 26 1948=164d≡3→Mon;
       +366d(1948 leap,Jan<Feb29)=Wed; +365d=Thursday                               -> A
  Q53: Jan 1 1900=Mon; 174 yrs back (42 leaps): 216≡6; Jan 1 1726=Tue;
       Jan→Mar 5: 63d≡0; Mar 5 1726=Tuesday (Zeller's formula confirmed)
       (key says C=Monday; key appears wrong; using Tuesday)                         -> B
  Q54: Diya: after 17 & before 21 → {18,19,20};
       brother: after 19 & before 24 → {20,21,22,23}; intersection=20 Feb          -> D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Calendar_Sheet5"
SUBJECT = "Reasoning"
TOPIC   = "Calendar"

QUESTIONS = [
    # Q47
    {
        "question_number": 47,
        "difficulty": "hard",
        "question_en": (
            "Which of the following days can never be "
            "the first day of any century?"
        ),
        "question_hi": (
            "इनमें से कौन सा दिन किसी शताब्दी का प्रथम दिन नहीं हो सकता?"
        ),
        "option_a": "Sunday/रविवार",
        "option_b": "Monday/सोमवार",
        "option_c": "Thursday/गुरुवार",
        "option_d": "Saturday/शनिवार",
        "correct_answer": "A",
    },
    # Q48
    {
        "question_number": 48,
        "difficulty": "medium",
        "question_en": (
            "Ankita celebrates her birthday on Sunday, 6 March 2004. "
            "When will she again celebrate her birthday on Sunday?"
        ),
        "question_hi": (
            "अंकिता अपना जन्मदिन 6 मार्च 2004 रविवार को मनाती है "
            "तो अगली बार वह अपना जन्मदिन रविवार को फिर से कब मनाएगी?"
        ),
        "option_a": "2008",
        "option_b": "2009",
        "option_c": "2010",
        "option_d": "2011",
        "correct_answer": "C",
    },
    # Q49
    {
        "question_number": 49,
        "difficulty": "medium",
        "question_en": (
            "Kapil is 365 days older than Krishna whereas Sudesh is 60 weeks "
            "older than Kapil. If Sudesh was born on Sunday, then on which "
            "day was Krishna born?"
        ),
        "question_hi": (
            "कपिल, कृष्णा से 365 दिन बड़ा है जबकि सुदेश, कपिल से 60 सप्ताह बड़ा है। "
            "यदि सुदेश का जन्म रविवार को हुआ तो कृष्णा का जन्म कौनसे दिन हुआ?"
        ),
        "option_a": "Sunday/रविवार",
        "option_b": "Monday/सोमवार",
        "option_c": "Tuesday/मंगलवार",
        "option_d": "Saturday/शनिवार",
        "correct_answer": "B",
    },
    # Q50
    {
        "question_number": 50,
        "difficulty": "easy",
        "question_en": "Which day was on 10 August 2020?",
        "question_hi": "10 अगस्त 2020 को कौनसा दिन था?",
        "option_a": "Saturday/शनिवार",
        "option_b": "Sunday/रविवार",
        "option_c": "Monday/सोमवार",
        "option_d": "Tuesday/मंगलवार",
        "correct_answer": "C",
    },
    # Q51
    {
        "question_number": 51,
        "difficulty": "easy",
        "question_en": "Which day was on 15 August 1947?",
        "question_hi": "15 अगस्त 1947 को कौनसा दिन था?",
        "option_a": "Thursday/गुरुवार",
        "option_b": "Friday/शुक्रवार",
        "option_c": "Saturday/शनिवार",
        "option_d": "Sunday/रविवार",
        "correct_answer": "B",
    },
    # Q52
    {
        "question_number": 52,
        "difficulty": "easy",
        "question_en": "Which day was on 26 January 1950?",
        "question_hi": "26 जनवरी 1950 को कौनसा दिन था?",
        "option_a": "Thursday/गुरुवार",
        "option_b": "Friday/शुक्रवार",
        "option_c": "Monday/सोमवार",
        "option_d": "Tuesday/मंगलवार",
        "correct_answer": "A",
    },
    # Q53
    {
        "question_number": 53,
        "difficulty": "hard",
        "question_en": "Which day was on 5 March 1726?",
        "question_hi": "5 मार्च 1726 को कौनसा दिन था?",
        "option_a": "Wednesday/बुधवार",
        "option_b": "Tuesday/मंगलवार",
        "option_c": "Monday/सोमवार",
        "option_d": "Friday/शुक्रवार",
        "correct_answer": "B",
    },
    # Q54
    {
        "question_number": 54,
        "difficulty": "easy",
        "question_en": (
            "Diya remembers that her brother's birthday comes after 17th but "
            "before 21st February, but her brother remembers that it is after "
            "19th and before 24th February. When does her brother's birthday come?"
        ),
        "question_hi": (
            "दीया को याद है कि उसके भाई का जन्मदिन 17 फरवरी के बाद लेकिन "
            "21 फरवरी के पहले आता है जबकि उसके भाई को याद है कि उसका जन्मदिन "
            "19 फरवरी के बाद लेकिन 24 फरवरी से पहले आता है। "
            "तब उसके भाई का जन्मदिन कब आता है?"
        ),
        "option_a": "22 February/22 फरवरी",
        "option_b": "18 February/18 फरवरी",
        "option_c": "21 February/21 फरवरी",
        "option_d": "20 February/20 फरवरी",
        "correct_answer": "D",
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
