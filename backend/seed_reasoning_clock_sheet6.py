"""
seed_reasoning_clock_sheet6.py
====================================
Seeds questions 42-49 (Clock) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Clock
Run     : python seed_reasoning_clock_sheet6.py

Answer key verification:
  Q42: 8AM to 2PM=6h; hour hand=6×30°=180°                                        -> A
  Q43: minute 7 ahead: t-(15+t/12)=7 -> t=24 min past 3                           -> B
  Q44: 5 to 5:30 right angle: |150-5.5t|=90 -> t=120/11=10 10/11 min past 5      -> A
  Q45: one-third right angle=30°: |90-5.5t|=30 -> t=120/11=10 10/11 min past 3   -> A
  Q46: 4:30 -> |120-165|=45°                                                       -> A
  Q47: 4-5 hands 3 min apart: |11t/12-20|=3 -> t=204/11=18 6/11 min past 4       -> A
  Q48: 5:20 -> |150-110|=40°                                                       -> D
  Q49: 9-10 opposite: |270-5.5t|=180 -> t=180/11=16 4/11 min past 9              -> A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Clock_Sheet6"
SUBJECT = "Reasoning"
TOPIC   = "Clock"

QUESTIONS = [
    # Q42
    {
        "question_number": 42,
        "difficulty": "easy",
        "question_en": (
            "An accurate clock shows 8 o'clock in the morning. Through how many "
            "degrees will the hour hand rotate when the clock shows 2 o'clock "
            "in the afternoon?"
        ),
        "question_hi": (
            "एक सटीक घड़ी सुबह के 8 बजे दिखाती है। जब घड़ी दोपहर के 2 बजे "
            "दिखाएगी तो घंटे की सुई कितने डिग्री घूमेगी?"
        ),
        "option_a": "180°",
        "option_b": "150°",
        "option_c": "168°",
        "option_d": "144°",
        "correct_answer": "A",
    },
    # Q43
    {
        "question_number": 43,
        "difficulty": "medium",
        "question_en": (
            "At what time between 3 and 4 is the minute-hand 7 minutes "
            "ahead of the hour-hand?"
        ),
        "question_hi": (
            "3 और 4 के बीच किस समय मिनट की सुई घंटे की सुई से 7 "
            "मिनट आगे होगी?"
        ),
        "option_a": "8⁸/₁₁ min. past 3/3 बजकर 8⁸/₁₁ मिनट",
        "option_b": "24 min. past 3/3 बजकर 24 मिनट",
        "option_c": "25 min. past 3/3 बजकर 25 मिनट",
        "option_d": "22 min. past 3/3 बजकर 22 मिनट",
        "correct_answer": "B",
    },
    # Q44
    {
        "question_number": 44,
        "difficulty": "hard",
        "question_en": (
            "At what time between 5 and 5:30, will the hands of a clock "
            "be at right angle?"
        ),
        "question_hi": (
            "5 से 5:30 के बीच किस समय घड़ी की सुइयाँ समकोण पर होंगी?"
        ),
        "option_a": "10¹⁰/₁₁ min. past 5/5 बजकर 10¹⁰/₁₁ मिनट",
        "option_b": "10⁹/₁₀ min. past 5/5 बजकर 10⁹/₁₀ मिनट",
        "option_c": "11¹⁰/₁₁ min. past 5/5 बजकर 11¹⁰/₁₁ मिनट",
        "option_d": "None of these/इनमें से कोई नहीं",
        "correct_answer": "A",
    },
    # Q45
    {
        "question_number": 45,
        "difficulty": "hard",
        "question_en": (
            "At which of the following time between 3 and 4 O'clock when the "
            "angle between the hands of a watch is one-third of a right angle?"
        ),
        "question_hi": (
            "3 और 4 बजे के बीच निम्नलिखित में से किस समय घड़ी की सुइयों "
            "के बीच का कोण समकोण का एक-तिहाई होता है।"
        ),
        "option_a": "10¹⁰/₁₁ min. past 3/3 बजकर 10¹⁰/₁₁ मिनट",
        "option_b": "10⁹/₁₁ min. past 3/3 बजकर 10⁹/₁₁ मिनट",
        "option_c": "11¹⁰/₁₁ min. past 3/3 बजकर 11¹⁰/₁₁ मिनट",
        "option_d": "21⁸/₁₁ min. past 3/3 बजकर 21⁸/₁₁ मिनट",
        "correct_answer": "A",
    },
    # Q46
    {
        "question_number": 46,
        "difficulty": "easy",
        "question_en": (
            "Find the angle between the two hands of a clock at 4.30 pm."
        ),
        "question_hi": (
            "अपराह्न 4.30 बजे घड़ी की दोनों सुइयों के बीच का कोण ज्ञात कीजिए।"
        ),
        "option_a": "45°",
        "option_b": "30°",
        "option_c": "60°",
        "option_d": "None of these/इनमें से कोई नहीं",
        "correct_answer": "A",
    },
    # Q47
    {
        "question_number": 47,
        "difficulty": "hard",
        "question_en": (
            "At which of the following time between 4 and 5 are the hands "
            "of a clock 3 minutes apart?"
        ),
        "question_hi": (
            "निम्नलिखित में से 4 और 5 के बीच किस समय घड़ी की सुइयाँ 3 "
            "मिनट के अंतर पर होती हैं?"
        ),
        "option_a": "18⁶/₁₁ min. past 4/4 बजकर 18⁶/₁₁ मिनट",
        "option_b": "26⁵/₁₁ min. past 4/4 बजकर 26⁵/₁₁ मिनट",
        "option_c": "25⁵/₁₁ min. past 4/4 बजकर 25⁵/₁₁ मिनट",
        "option_d": "None of these/इनमें से कोई नहीं",
        "correct_answer": "A",
    },
    # Q48
    {
        "question_number": 48,
        "difficulty": "easy",
        "question_en": (
            "At what angle are the two hands of a clock inclined at "
            "20 minutes past 5?"
        ),
        "question_hi": (
            "5 बजकर 20 मिनट पर घड़ी की दोनों सुइयाँ किस कोण पर झुकी हुई हैं?"
        ),
        "option_a": "30°",
        "option_b": "45°",
        "option_c": "50°",
        "option_d": "40°",
        "correct_answer": "D",
    },
    # Q49
    {
        "question_number": 49,
        "difficulty": "hard",
        "question_en": (
            "Find at what time between 9 and 10 O'clock will the hands of a clock "
            "be in the same straight line but not together."
        ),
        "question_hi": (
            "9 और 10 बजे के बीच किस समय घड़ी की सुइयाँ एक ही सीधी रेखा "
            "में होंगी लेकिन एक साथ नहीं होंगी।"
        ),
        "option_a": "16⁴/₁₁ min. past 9/9 बजकर 16⁴/₁₁ मिनट",
        "option_b": "16⁵/₁₁ min. past 9/9 बजकर 16⁵/₁₁ मिनट",
        "option_c": "16³/₁₁ min. past 9/9 बजकर 16³/₁₁ मिनट",
        "option_d": "None of these/इनमें से कोई नहीं",
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
