"""
seed_reasoning_calendar_sheet1.py
===================================
Seeds Calendar Q1-Q11 from Gagan Pratap Reasoning PDFs (Sheet 1).
Subject : Reasoning
Topic   : Calendar

Answer key:
  Q1   A — 1992 (the only leap year; 1900, 1800 are century years not ÷400;
             1882 is not ÷4)
  Q2   A — 2  (2012 and 2016 between 2009 and 2019)
  Q3   C — 24 (first century 1–100: 25 multiples of 4, minus 100 which is not leap)
  Q4   C — 24 (second century 101–200: 25 multiples of 4, minus 200 not leap)
  Q5   B — 25 (fourth century 301–400: 25 multiples of 4, 400 IS leap → all 25)
  Q6   C — 97 (29 Feb in 400 yrs = 100 – 3 non-leap centuries = 97)
  Q7   D — 4497 (29th date in 400 yrs: 11×400 + 97 = 4400 + 97)
  Q8   B — Thursday (37 days after Tuesday: 37÷7=5r2, Tue+2=Thu)
  Q9   A — Wednesday (22 days before Thursday: 22÷7=3r1, Thu−1=Wed)
  Q10  C — Wednesday (4 Aug=Tue; 26 Aug = 22 days later; Tue+1=Wed)
  Q11  A — Saturday (30th=Sunday; 30−1=29 days from 1st; 29÷7=4r1; Sun−1=Sat)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Calendar_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Calendar"

QUESTIONS = [
    # ── Q1 ── Odd one out (leap years) ──────────────────────────────────────────────
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": (
            "Find the odd one out.\n\n"
            "(a) 1992   (b) 1900   (c) 1800   (d) 1882"
        ),
        "question_hi": (
            "निम्नलिखित में से विषम छाँटिए।\n\n"
            "(a) 1992   (b) 1900   (c) 1800   (d) 1882"
        ),
        "option_a": "1992",
        "option_b": "1900",
        "option_c": "1800",
        "option_d": "1882",
        "correct_answer": "A",
        # 1992: 1992÷4=498 → leap year ✓ (only leap year in the list)
        # 1900: century year, 1900÷400≠integer → NOT a leap year ✗
        # 1800: century year, 1800÷400≠integer → NOT a leap year ✗
        # 1882: 1882÷4=470.5 → not divisible by 4 → NOT a leap year ✗
        # 1992 is the ODD one out — the only year that IS a leap year.
    },
    # ── Q2 ── Leap years between 2009 and 2019 ───────────────────────────────────────
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": (
            "How many leap years are there between year 2009 and 2019?\n\n"
            "(a) 2   (b) 3   (c) 4   (d) 1"
        ),
        "question_hi": (
            "वर्ष 2009 और 2019 के बीच अधिवर्षों की संख्या बताइए?\n\n"
            "(a) 2   (b) 3   (c) 4   (d) 1"
        ),
        "option_a": "2",
        "option_b": "3",
        "option_c": "4",
        "option_d": "1",
        "correct_answer": "A",
        # Leap years between 2009 and 2019 (exclusive of endpoints):
        # 2012 (÷4 ✓, not century) and 2016 (÷4 ✓, not century) → 2 leap years.
    },
    # ── Q3 ── Leap years in the first century (1–100) ────────────────────────────────
    {
        "question_number": 3,
        "difficulty": "medium",
        "question_en": (
            "How many leap years were there in the first century?\n\n"
            "(a) 25   (b) 23   (c) 24   (d) 26"
        ),
        "question_hi": (
            "पहली शताब्दी में कुल कितने अधिवर्ष थे?\n\n"
            "(a) 25   (b) 23   (c) 24   (d) 26"
        ),
        "option_a": "25",
        "option_b": "23",
        "option_c": "24",
        "option_d": "26",
        "correct_answer": "C",
        # First century = year 1 to 100.
        # Multiples of 4 from 1 to 100: 4, 8, 12, …, 96, 100 → 100÷4 = 25 numbers.
        # But 100 is a century year: 100÷400 ≠ integer → NOT a leap year.
        # Leap years = 25 − 1 = 24.
    },
    # ── Q4 ── Leap years in the second century (101–200) ─────────────────────────────
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": (
            "How many leap years were there in the second century?\n\n"
            "(a) 48   (b) 72   (c) 24   (d) 25"
        ),
        "question_hi": (
            "दूसरी शताब्दी में कुल कितने अधिवर्ष थे?\n\n"
            "(a) 48   (b) 72   (c) 24   (d) 25"
        ),
        "option_a": "48",
        "option_b": "72",
        "option_c": "24",
        "option_d": "25",
        "correct_answer": "C",
        # Second century = year 101 to 200.
        # Multiples of 4 from 104 to 200: (200−104)÷4 + 1 = 25 numbers.
        # 200 is a century year: 200÷400 ≠ integer → NOT a leap year.
        # Leap years = 25 − 1 = 24.
    },
    # ── Q5 ── Leap years in the fourth century (301–400) ─────────────────────────────
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": (
            "How many leap years were there in the fourth century?\n\n"
            "(a) 24   (b) 25   (c) 97   (d) 72"
        ),
        "question_hi": (
            "चौथी शताब्दी में कुल कितने अधिवर्ष थे?\n\n"
            "(a) 24   (b) 25   (c) 97   (d) 72"
        ),
        "option_a": "24",
        "option_b": "25",
        "option_c": "97",
        "option_d": "72",
        "correct_answer": "B",
        # Fourth century = year 301 to 400.
        # Multiples of 4 from 304 to 400: (400−304)÷4 + 1 = 25 numbers.
        # 400 IS a leap year (400÷400 = 1, integer ✓) → all 25 multiples of 4 count.
        # Leap years = 25.
        # (Compare: 1st, 2nd, 3rd centuries each have 24 leap years because their
        # terminal century year — 100, 200, 300 — is NOT divisible by 400.)
    },
    # ── Q6 ── How many times does 29 February come in 400 years? ─────────────────────
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": (
            "How many times does 29th February come in 400 years?\n\n"
            "(a) 400   (b) 100   (c) 97   (d) 96"
        ),
        "question_hi": (
            "400 वर्षों में कुल कितनी बार 29 फ़रवरी आती है?\n\n"
            "(a) 400   (b) 100   (c) 97   (d) 96"
        ),
        "option_a": "400",
        "option_b": "100",
        "option_c": "97",
        "option_d": "96",
        "correct_answer": "C",
        # 29 February occurs once per leap year.
        # Leap years in 400 years:
        #   Multiples of 4: 400÷4 = 100
        #   Subtract century years not ÷400: 100÷100 = 4 centuries; 400÷400 = 1 IS leap
        #   Non-leap centuries = 4 − 1 = 3
        #   Leap years = 100 − 3 = 97
        # So 29 February comes 97 times in 400 years.
    },
    # ── Q7 ── How many times does the 29th date come in 400 years? ───────────────────
    {
        "question_number": 7,
        "difficulty": "hard",
        "question_en": (
            "How many times does 29th date come in 400 years?\n\n"
            "(a) 96   (b) 97   (c) 4800   (d) 4497"
        ),
        "question_hi": (
            "400 वर्षों में कुल कितनी बार 29 तारीख आती है?\n\n"
            "(a) 96   (b) 97   (c) 4800   (d) 4497"
        ),
        "option_a": "96",
        "option_b": "97",
        "option_c": "4800",
        "option_d": "4497",
        "correct_answer": "D",
        # The 29th date occurs in every month that has at least 29 days.
        # All 12 months have 29+ days EXCEPT February in non-leap years.
        # • 11 months (Jan, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec):
        #   each has ≥29 days every year → 11 × 400 = 4400 occurrences.
        # • February: 29th date appears only in leap years → 97 times in 400 years.
        # Total = 4400 + 97 = 4497.
    },
    # ── Q8 ── Day after 37 days from Tuesday ─────────────────────────────────────────
    {
        "question_number": 8,
        "difficulty": "easy",
        "question_en": (
            "If today is Tuesday, then what day will it be after 37 days?\n\n"
            "(a) Wednesday   (b) Thursday   (c) Tuesday   (d) Friday"
        ),
        "question_hi": (
            "यदि आज मंगलवार है तो आज से 37 दिन बाद कौन सा दिन होगा?\n\n"
            "(a) बुधवार   (b) गुरुवार   (c) मंगलवार   (d) शुक्रवार"
        ),
        "option_a": "Wednesday / बुधवार",
        "option_b": "Thursday / गुरुवार",
        "option_c": "Tuesday / मंगलवार",
        "option_d": "Friday / शुक्रवार",
        "correct_answer": "B",
        # 37 ÷ 7 = 5 weeks + 2 days remainder.
        # Tuesday + 2 days = Thursday.
    },
    # ── Q9 ── Day 22 days before Thursday ────────────────────────────────────────────
    {
        "question_number": 9,
        "difficulty": "easy",
        "question_en": (
            "If today is Thursday, then what was the day before 22 days?\n\n"
            "(a) Wednesday   (b) Thursday   (c) Monday   (d) Tuesday"
        ),
        "question_hi": (
            "यदि आज गुरुवार है तो आज से 22 दिन पहले कौन सा दिन था?\n\n"
            "(a) बुधवार   (b) गुरुवार   (c) सोमवार   (d) मंगलवार"
        ),
        "option_a": "Wednesday / बुधवार",
        "option_b": "Thursday / गुरुवार",
        "option_c": "Monday / सोमवार",
        "option_d": "Tuesday / मंगलवार",
        "correct_answer": "A",
        # 22 ÷ 7 = 3 weeks + 1 day remainder.
        # Going BACK 1 day from Thursday = Wednesday.
    },
    # ── Q10 ── 4th August is Tuesday; find day on 26th August ────────────────────────
    {
        "question_number": 10,
        "difficulty": "easy",
        "question_en": (
            "Today on 4th August it is Tuesday. What day will it be on the 26th of "
            "this month?\n\n"
            "(a) Thursday   (b) Tuesday   (c) Wednesday   (d) Monday"
        ),
        "question_hi": (
            "आज 4 अगस्त मंगलवार का दिन है तब इसी माह की 26 तारीख को कौनसा दिन होगा?\n\n"
            "(a) गुरुवार   (b) मंगलवार   (c) बुधवार   (d) सोमवार"
        ),
        "option_a": "Thursday / गुरुवार",
        "option_b": "Tuesday / मंगलवार",
        "option_c": "Wednesday / बुधवार",
        "option_d": "Monday / सोमवार",
        "correct_answer": "C",
        # 26th August − 4th August = 22 days later.
        # 22 ÷ 7 = 3 weeks + 1 day remainder.
        # Tuesday + 1 day = Wednesday.
    },
    # ── Q11 ── 30th = Sunday; find day on 1st ────────────────────────────────────────
    {
        "question_number": 11,
        "difficulty": "medium",
        "question_en": (
            "If it is Sunday on the 30th of a month, then what day was it on the "
            "1st of that month?\n\n"
            "(a) Saturday   (b) Friday   (c) Sunday   (d) Monday"
        ),
        "question_hi": (
            "किसी महीने की 30 तारीख को रविवार है तो उस महीने की 1 तारीख को कौनसा "
            "दिन था?\n\n"
            "(a) शनिवार   (b) शुक्रवार   (c) रविवार   (d) सोमवार"
        ),
        "option_a": "Saturday / शनिवार",
        "option_b": "Friday / शुक्रवार",
        "option_c": "Sunday / रविवार",
        "option_d": "Monday / सोमवार",
        "correct_answer": "A",
        # From 1st to 30th = 29 days (30 − 1 = 29).
        # 29 ÷ 7 = 4 weeks + 1 day remainder.
        # So 30th is 1 day AHEAD of 1st in the weekly cycle.
        # 30th = Sunday → 1st = Sunday − 1 = Saturday.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        existing_qnums = {
            row[0]
            for row in db.query(Question.question_number)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        for d in QUESTIONS:
            if d["question_number"] in existing_qnums:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
            inserted += 1
            print(f"  INSERT Q{d['question_number']}")

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped: {skipped}")

    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
