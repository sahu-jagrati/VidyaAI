"""
seed_reasoning_clock_sheet10.py
====================================
Seeds questions 79-86 (Clock) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Clock
Run     : python seed_reasoning_clock_sheet10.py

Answer key verification:
  Q79: 11:00-4:00=5h; coincide at 12:00,1:05,2:10,3:16 (next 4:21>4:00)=4 times  -> C
  Q80: 4:00-11:00=7h; coincide at 4:21,5:27,6:32,7:38,8:43,9:49,10:54=7 times    -> C
  Q81: 4PM-11PM=7h; opposite at 4:54,6:00,7:05,8:10,9:16,10:21(next 11:27>11)=6  -> B
  Q82: 2PM-10PM=8h; perpendicular 14 times                                         -> D
  Q83: second 480° in 80s; minute=80×0.1=8°                                        -> C
  Q84: upside-down+mirror; actual=18:30-10:20=8:10                                 -> A
  Q85: chairman 12:20; others 12:40; 30 min late; scheduled=12:40-30=12:10        -> A
  Q86: buses every 30 min; next 10:30; last 10:00; 10 min ago; now=10:10 AM       -> B
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Clock_Sheet10"
SUBJECT = "Reasoning"
TOPIC   = "Clock"

QUESTIONS = [
    # Q79
    {
        "question_number": 79,
        "difficulty": "medium",
        "question_en": (
            "For how many times, both the hands of a clock will overlap each other "
            "between 11:00 to 4:00?"
        ),
        "question_hi": (
            "11:00 बजे से 4:00 बजे के बीच एक घड़ी की दोनों सुइयाँ कितनी बार "
            "एक दूसरे के ऊपर आएंगी?"
        ),
        "option_a": "5 times/5 बार",
        "option_b": "6 times/6 बार",
        "option_c": "4 times/4 बार",
        "option_d": "8 times/8 बार",
        "correct_answer": "C",
    },
    # Q80
    {
        "question_number": 80,
        "difficulty": "medium",
        "question_en": (
            "For how many times, both the hands of a clock will overlap each other "
            "between 4:00 to 11:00?"
        ),
        "question_hi": (
            "4:00 बजे से 11:00 बजे के बीच एक घड़ी की दोनों सुइयाँ कितनी बार "
            "एक दूसरे को ओवरलैप करेंगी?"
        ),
        "option_a": "4 times/4 बार",
        "option_b": "5 times/5 बार",
        "option_c": "7 times/7 बार",
        "option_d": "8 times/8 बार",
        "correct_answer": "C",
    },
    # Q81
    {
        "question_number": 81,
        "difficulty": "medium",
        "question_en": (
            "From 4 pm. to 11 pm., for how many times both the hands of a clock "
            "will be in the opposite direction?"
        ),
        "question_hi": (
            "शाम 4 बजे से रात 11 बजे तक, कितनी बार घड़ी की दोनों सुइयाँ "
            "विपरीत दिशा में होंगी?"
        ),
        "option_a": "5 times/5 बार",
        "option_b": "6 times/6 बार",
        "option_c": "7 times/7 बार",
        "option_d": "8 times/8 बार",
        "correct_answer": "B",
    },
    # Q82
    {
        "question_number": 82,
        "difficulty": "hard",
        "question_en": (
            "From 2 pm to 10 pm., for how many times both the hands of a clock "
            "will be perpendicular to each other?"
        ),
        "question_hi": (
            "दोपहर 2 बजे से रात 10 बजे तक, घड़ी की दोनों सुइयाँ कितनी बार "
            "एक दूसरे के लंबवत रहेंगी?"
        ),
        "option_a": "7 times/7 बार",
        "option_b": "8 times/8 बार",
        "option_c": "13 times/13 बार",
        "option_d": "14 times/14 बार",
        "correct_answer": "D",
    },
    # Q83
    {
        "question_number": 83,
        "difficulty": "medium",
        "question_en": (
            "How many degrees will the minute hand move, in the same time "
            "in which the second hand move 480°?"
        ),
        "question_hi": (
            "मिनट की सुई उसी समय में कितने डिग्री घूमेगी, जिसमें सेकंड की "
            "सुई 480° घूमेगी?"
        ),
        "option_a": "6°",
        "option_b": "9°",
        "option_c": "8°",
        "option_d": "4°",
        "correct_answer": "C",
    },
    # Q84
    {
        "question_number": 84,
        "difficulty": "hard",
        "question_en": (
            "A clock only with dots marking 3, 6, 9 and 12 O'clock position has "
            "been kept upside down in front of a mirror. A person reads the time "
            "in the reflection of the clock as 10:20. What is the actual time?"
        ),
        "question_hi": (
            "एक घड़ी जिसमें केवल 3, 6, 9 और 12 बजे के बिन्दु अंकित हैं, को "
            "दर्पण के सामने उल्टा रखा गया है। एक व्यक्ति घड़ी के प्रतिबिंब में "
            "समय 10:20 देखता है। वास्तविक समय क्या है?"
        ),
        "option_a": "08:10",
        "option_b": "02:40",
        "option_c": "04:50",
        "option_d": "10:20",
        "correct_answer": "A",
    },
    # Q85
    {
        "question_number": 85,
        "difficulty": "medium",
        "question_en": (
            "The Chairman of the Selection Committee arrived at the Interview room "
            "for conducting an interview at 10 minutes to 12:30 hrs. He was earlier "
            "by twenty minutes than the other members of the board, who arrived late "
            "by 30 minutes. At what time were the interview scheduled?"
        ),
        "question_hi": (
            "चयन समिति के अध्यक्ष साक्षात्कार के लिए साक्षात्कार कक्ष में "
            "12:30 बजे से 10 मिनट पहले पहुँचे। वे बोर्ड के अन्य सदस्यों से "
            "बीस मिनट पहले पहुँचे, जो 30 मिनट देरी से पहुँचे। साक्षात्कार किस "
            "समय निर्धारित किया गया था?"
        ),
        "option_a": "12:10",
        "option_b": "12:20",
        "option_c": "12:30",
        "option_d": "12:40",
        "correct_answer": "A",
    },
    # Q86
    {
        "question_number": 86,
        "difficulty": "easy",
        "question_en": (
            "The bus for Chennai leaves every 30 minutes from a bus depot. "
            "The enquiry clerk told a passenger that the bus for Chennai left "
            "10 minutes ago, and the next bus will leave at 10:30 a.m. "
            "What was the time when enquiry clerk told this?"
        ),
        "question_hi": (
            "एक बस डिपो से चेन्नई के लिए बस हर 30 मिनट में निकलती है। "
            "पूछताछ क्लर्क ने एक यात्री को बताया कि चेन्नई के लिए बस 10 मिनट "
            "पहले निकल गई है, और अगली बस सुबह 10:30 बजे निकलेगी। पूछताछ "
            "क्लर्क ने यह बात किस समय बताई?"
        ),
        "option_a": "10:20 a.m.",
        "option_b": "10:10 a.m.",
        "option_c": "10:00 a.m.",
        "option_d": "09:50 a.m.",
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
