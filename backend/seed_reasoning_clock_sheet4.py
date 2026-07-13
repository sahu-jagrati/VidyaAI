"""
seed_reasoning_clock_sheet4.py
====================================
Seeds questions 29-35 (Clock) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Clock
Run     : python seed_reasoning_clock_sheet4.py

Answer key verification:
  Q29: leave home 6:40AM; +25=7:05(Kunal); +15=7:20(breakfast done); leave=7:20AM -> B
  Q30: 4-5 opposite: 11t/12=50 -> t=600/11=54 6/11 min past 4                    -> C
  Q31: 9:17 -> |270-93.5|=176.5°=176½°                                             -> D
  Q32: 9-10 coincide: t=45×12/11=540/11=49 1/11 min past 9                        -> C
  Q33: 7-8 right angles: |210-5.5t|=90 -> t=240/11=21 9/11 & t=600/11=54 6/11    -> A
  Q34: 2-3 coincide: t=10×12/11=120/11=10 10/11 min past 2                        -> B
  Q35: 8:24 -> |240-132|=108°                                                      -> B
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Clock_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Clock"

QUESTIONS = [
    # Q29
    {
        "question_number": 29,
        "difficulty": "easy",
        "question_en": (
            "Ram leaves his house at 20 minutes to seven in the morning, reaches "
            "Kunal's house in 25 minutes. They finish their breakfast in another "
            "15 minutes and leave for their office which takes another 35 minutes. "
            "At what time do they leave Kunal's house to reach their office?"
        ),
        "question_hi": (
            "राम सुबह सात बजकर 20 मिनट पर अपने घर से निकलता है, 25 मिनट में "
            "कुणाल के घर पहुँचता है। वे अपना नाश्ता अगले 15 मिनट में खत्म करते "
            "हैं और अपने ऑफिस के लिए निकल जाते हैं जिसमें 35 मिनट लगते हैं। "
            "वे अपने ऑफिस पहुँचने के लिए कुणाल के घर से किस समय निकलते हैं?"
        ),
        "option_a": "7:40 A.M.",
        "option_b": "7:20 A.M.",
        "option_c": "7:45 A.M.",
        "option_d": "8:15 A.M.",
        "correct_answer": "B",
    },
    # Q30
    {
        "question_number": 30,
        "difficulty": "hard",
        "question_en": (
            "At what time between 4 and 5 o'clock will the hands of a watch "
            "point in opposite directions?"
        ),
        "question_hi": (
            "4 से 5 बजे के बीच किस समय घड़ी की सुइयाँ विपरीत दिशा में होंगी?"
        ),
        "option_a": "46 min. past 4/4 बजकर 46 मिनट",
        "option_b": "40 min. past 5/5 बजकर 40 मिनट",
        "option_c": "54⁶/₁₁ min. past 4/4 बजकर 54⁶/₁₁ मिनट",
        "option_d": "52¼ min. past 4/4 बजकर 52¼ मिनट",
        "correct_answer": "C",
    },
    # Q31
    {
        "question_number": 31,
        "difficulty": "medium",
        "question_en": (
            "At what angle are the two hands of a clock inclined at "
            "17 minutes past 9?"
        ),
        "question_hi": (
            "9 बजकर 17 मिनट पर घड़ी की दोनों सुइयाँ किस कोण पर झुकी हुई हैं?"
        ),
        "option_a": "167½°",
        "option_b": "172½°",
        "option_c": "166½°",
        "option_d": "176½°",
        "correct_answer": "D",
    },
    # Q32
    {
        "question_number": 32,
        "difficulty": "hard",
        "question_en": (
            "At what time between 9 and 10 will the hands of a clock be together?"
        ),
        "question_hi": (
            "9 और 10 के बीच किस समय घड़ी की सुइयाँ एक साथ होंगी?"
        ),
        "option_a": "45 min. past 9/9 बजकर 45 मिनट",
        "option_b": "50 min. past 9/9 बजकर 50 मिनट",
        "option_c": "49¹/₁₁ min. past 9/9 बजकर 49¹/₁₁ मिनट",
        "option_d": "48²/₁₁ min. past 9/9 बजकर 48²/₁₁ मिनट",
        "correct_answer": "C",
    },
    # Q33
    {
        "question_number": 33,
        "difficulty": "hard",
        "question_en": (
            "At what time are the hands of a clock at right angle between "
            "7 am and 8 am?"
        ),
        "question_hi": (
            "प्रातः 7 बजे से 8 बजे के बीच किस समय घड़ी की सुइयाँ समकोण पर होती हैं?"
        ),
        "option_a": "54⁶/₁₁ min. past 7, 21⁹/₁₁ min. past 7/7 बजकर 54⁶/₁₁ मिनट, 7 बजकर 21⁹/₁₁ मिनट",
        "option_b": "52⁵/₁₁ min. past 7, 21⁸/₁₁ min. past 7/7 बजकर 52⁵/₁₁ मिनट, 7 बजकर 21⁸/₁₁ मिनट",
        "option_c": "56⁶/₁₁ min. past 7, 21⁸/₁₁ min. past 7/7 बजकर 56⁶/₁₁ मिनट, 7 बजकर 21⁸/₁₁ मिनट",
        "option_d": "None of these/इनमें से कोई नहीं",
        "correct_answer": "A",
    },
    # Q34
    {
        "question_number": 34,
        "difficulty": "hard",
        "question_en": (
            "At what time are the hands of a clock together between 2 and 3?"
        ),
        "question_hi": (
            "किस समय घड़ी की सुइयाँ 2 और 3 के बीच होती हैं?"
        ),
        "option_a": "10⁹/₁₁ min. past 2/2 बजकर 10⁹/₁₁ मिनट",
        "option_b": "10¹⁰/₁₁ min. past 2/2 बजकर 10¹⁰/₁₁ मिनट",
        "option_c": "10⁸/₁₁ min. past 2/2 बजकर 10⁸/₁₁ मिनट",
        "option_d": "None of these/इनमें से कोई नहीं",
        "correct_answer": "B",
    },
    # Q35
    {
        "question_number": 35,
        "difficulty": "easy",
        "question_en": (
            "What is the angle between the two hands of the clock at 8:24 pm?"
        ),
        "question_hi": (
            "रात्रि 4:24 बजे घड़ी की दोनों सुइयों के बीच का कोण क्या होगा?"
        ),
        "option_a": "100°",
        "option_b": "108°",
        "option_c": "106°",
        "option_d": "107°",
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
