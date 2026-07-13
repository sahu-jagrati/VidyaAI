"""
seed_reasoning_clock_sheet2.py
====================================
Seeds questions 11-19 (Clock) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Clock
Run     : python seed_reasoning_clock_sheet2.py

Answer key verification:
  Q11: water reflection = 6:30 - 3:13 = 3:17                                       -> A
  Q12: at 5:00 gap=150°; 2nd right-angle: 5.5t=240 -> t=480/11=43 7/11 min        -> D
  Q13: at 6:20 angle=70°; minute@NE(45°); hour=45+70=115°≈SE                      -> D
  Q14: upside-down+mirror adds 180° each hand; 4:50 seen -> actual 10:20           -> D
  Q15: hour = 0.5°/min = 1/120° per sec; 36s = 36/120 = 3/10°                     -> D
  Q16: |120-5.5t|=90 -> t=420/11≈38.18 min -> 4:38 am                             -> D
  Q17: 12 strikes = 11 intervals in 33s -> 3s each; 6 strikes = 5×3 = 15s         -> D
  Q18: |120-5.5t|=90 -> t=60/11 or t=420/11=38 2/11 min past 4                   -> A
  Q19: at 5:00 gap=25 min-marks; 3 marks behind: gain 22; t=22×12/11=24 min       -> B
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Clock_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Clock"

QUESTIONS = [
    # Q11
    {
        "question_number": 11,
        "difficulty": "medium",
        "question_en": (
            "Time in a clock is 3:13. What time will appear in water?"
        ),
        "question_hi": (
            "एक घड़ी में समय 3:13 है, पानी में क्या समय दिखाई देगा?"
        ),
        "option_a": "3:17",
        "option_b": "2:17",
        "option_c": "3:23",
        "option_d": "2:13",
        "correct_answer": "A",
    },
    # Q12
    {
        "question_number": 12,
        "difficulty": "hard",
        "question_en": (
            "At what time between 5:30 and 6 will the hands of a clock "
            "be at right angle?"
        ),
        "question_hi": (
            "5:30 और 6 के बीच किस समय घड़ी की सुइयाँ समकोण पर होंगी?"
        ),
        "option_a": "40 min past 5/5 बजकर 40 मिनट",
        "option_b": "45 min past 5/5 बजकर 45 मिनट",
        "option_c": "43⁵/₁₁ minutes past 5/5 बजकर 43⁵/₁₁ मिनट",
        "option_d": "43⁷/₁₁ minutes past 5/5 बजकर 43⁷/₁₁ मिनट",
        "correct_answer": "D",
    },
    # Q13
    {
        "question_number": 13,
        "difficulty": "hard",
        "question_en": (
            "If the clock reads 6:20 and if the minute hand points North-East, "
            "in which direction will the hour hand point?"
        ),
        "question_hi": (
            "यदि घड़ी में 6:20 बजे हैं और मिनट की सुई उत्तर-पूर्व दिशा की ओर "
            "इशारा करती है, तो घंटे की सुई किस दिशा की ओर इशारा करेगी?"
        ),
        "option_a": "East/पूर्व",
        "option_b": "West/पश्चिम",
        "option_c": "North-West/उत्तर-पश्चिम",
        "option_d": "South-East/दक्षिण-पूर्व",
        "correct_answer": "D",
    },
    # Q14
    {
        "question_number": 14,
        "difficulty": "hard",
        "question_en": (
            "A clock with only dots marking 3, 6, 9 and 12 positions has been "
            "kept upside down in front of a mirror. A person reads the time in "
            "the reflection of the clock as 4:50. What is the actual time?"
        ),
        "question_hi": (
            "एक घड़ी जिसमें केवल 3, 6, 9 और 12 स्थान अंकित हैं, को दर्पण के सामने "
            "उल्टा रखा गया है। एक व्यक्ति प्रतिबिंब में समय 4:50 देखता है। "
            "वास्तविक समय क्या है?"
        ),
        "option_a": "08:10",
        "option_b": "01:40",
        "option_c": "04:50",
        "option_d": "10:20",
        "correct_answer": "D",
    },
    # Q15
    {
        "question_number": 15,
        "difficulty": "medium",
        "question_en": (
            "What is angle made by hour hand in 36 seconds?"
        ),
        "question_hi": (
            "घंटे की सुई द्वारा 36 सेकंड में बनाया गया कोण कितना होगा?"
        ),
        "option_a": "3°",
        "option_b": "120°",
        "option_c": "10/3°",
        "option_d": "3/10°",
        "correct_answer": "D",
    },
    # Q16
    {
        "question_number": 16,
        "difficulty": "medium",
        "question_en": (
            "At what approximate time between 4 and 5 am will the hands "
            "of a clock be at right angle?"
        ),
        "question_hi": (
            "प्रातः 4 से 5 बजे के बीच लगभग किस समय घड़ी की सुइयाँ समकोण पर होंगी?"
        ),
        "option_a": "4:35 am",
        "option_b": "4:39 am",
        "option_c": "4:40 am",
        "option_d": "4:38 am",
        "correct_answer": "D",
    },
    # Q17
    {
        "question_number": 17,
        "difficulty": "medium",
        "question_en": (
            "If a clock strikes 12 in 33 seconds, it will strike 6 in how many seconds?"
        ),
        "question_hi": (
            "यदि एक घड़ी 33 सेकंड में 12 बजाती है, तो वह कितने सेकंड में 6 बजाएगी?"
        ),
        "option_a": "12",
        "option_b": "22",
        "option_c": "33/2",
        "option_d": "15",
        "correct_answer": "D",
    },
    # Q18
    {
        "question_number": 18,
        "difficulty": "hard",
        "question_en": (
            "At what time between 4 and 5 o'clock will the hands of a clock "
            "be at a right angle?"
        ),
        "question_hi": (
            "4 और 5 बजे के बीच किस समय घड़ी की सुइयाँ समकोण पर होंगी?"
        ),
        "option_a": "38²/₁₁ min. past 4/4 बजकर 38²/₁₁ मिनट",
        "option_b": "50½ min. past 4/4 बजकर 50½ मिनट",
        "option_c": "51¼ min. past 4/4 बजकर 51¼ मिनट",
        "option_d": "None/कोई नहीं",
        "correct_answer": "A",
    },
    # Q19
    {
        "question_number": 19,
        "difficulty": "hard",
        "question_en": (
            "At what time between 5 and 6 O'clock will the hands be 3 minutes apart?"
        ),
        "question_hi": (
            "5 और 6 बजे के बीच किस समय दोनों सुइयां 3 मिनट के अंतर पर होंगी?"
        ),
        "option_a": "32⁵/₁₁ min. past 5/5 बजकर 32⁵/₁₁ मिनट",
        "option_b": "24 min. past 5/5 बजकर 24 मिनट",
        "option_c": "33⁵/₁₁ min. past 5/5 बजकर 33⁵/₁₁ मिनट",
        "option_d": "34⁵/₁₁ min. past 5/5 बजकर 34⁵/₁₁ मिनट",
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
