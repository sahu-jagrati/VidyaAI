"""
seed_reasoning_clock_sheet8.py
====================================
Seeds questions 58-64 (Clock) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Clock
Run     : python seed_reasoning_clock_sheet8.py

Answer key verification:
  Q58: correct=720/11 min; actual=64 min; gain=(720/11-64)×(1440/64)/11
       =22.5×(16/11)=360/11=32 8/11 min gain                                      -> A
  Q59: boy swaps hands; minute at 30(=6h pos); hour at 12:30 reads ~2min; time=12:30 -> D
  Q60: loses 20min/day; 3 days→60min loss; clock shows 3PM→true=4PM               -> A
  Q61: noon Mon to 2PM next Mon=170h; gain=34/5 min; rate=1/25 min/h;
       2 min to correct at 1/25 min/h=50h from noon Mon=2PM Wednesday             -> B
  Q62: straight line=coincide(22)+opposite(22)=44 times/day                       -> C
  Q63: rate=37/36; clock shows 4:15PM=555 clock min; true=555×36/37=540min=4PM   -> B
  Q64: 5=25 min mark; |t-25|=|20+t/12-25| -> t=360/13=27 9/13 min past 4        -> C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Clock_Sheet8"
SUBJECT = "Reasoning"
TOPIC   = "Clock"

QUESTIONS = [
    # Q58
    {
        "question_number": 58,
        "difficulty": "hard",
        "question_en": (
            "How much does a watch gain or lose per day, if its hand coincide "
            "every 64 minutes of correct time?"
        ),
        "question_hi": (
            "यदि एक घड़ी की सुई हर 64 मिनट पर सही समय पर आती है, तो "
            "उसे प्रतिदिन कितना लाभ या हानि होगी?"
        ),
        "option_a": "32⁸/₁₁ min. gain/32⁸/₁₁ मिनट आगे",
        "option_b": "31⁸/₁₁ min. gain/31⁸/₁₁ मिनट आगे",
        "option_c": "32³/₁₁ min. gain/32³/₁₁ मिनट आगे",
        "option_d": "32⁸/₁₁ min. lose/32⁸/₁₁ मिनट पीछे",
        "correct_answer": "A",
    },
    # Q59
    {
        "question_number": 59,
        "difficulty": "hard",
        "question_en": (
            "A boy understood the larger needle as smaller and vice-versa. "
            "He saw that it was 6 hours 2 minutes in clock. "
            "What was the actual time?"
        ),
        "question_hi": (
            "एक लड़के ने बड़ी सुई को छोटी सुई समझा और छोटी सुई को बड़ी सुई। "
            "उसने देखा कि घड़ी में 6 घंटे 2 मिनट हो रहे थे। वास्तविक समय क्या था?"
        ),
        "option_a": "11:30",
        "option_b": "1:30",
        "option_c": "2:30",
        "option_d": "12:30",
        "correct_answer": "D",
    },
    # Q60
    {
        "question_number": 60,
        "difficulty": "medium",
        "question_en": (
            "A clock is set right at 4 pm. The clock loses 20 min. in 24 hours. "
            "What will be the true time when the clock indicates 3 pm on 4th day?"
        ),
        "question_hi": (
            "एक घड़ी को ठीक 4 बजे सेट किया गया है। घड़ी 24 घंटे में 20 मिनट "
            "पीछे हो जाती है। जब 4 तारीख को घड़ी 3 बजे का समय दिखाएगी तो "
            "सही समय क्या होगा?"
        ),
        "option_a": "4 pm",
        "option_b": "5 am",
        "option_c": "3 am",
        "option_d": "4 am",
        "correct_answer": "A",
    },
    # Q61
    {
        "question_number": 61,
        "difficulty": "hard",
        "question_en": (
            "A watch, which gains uniformly is 2 min. slow at noon on Monday, "
            "and is 4 min. 48 seconds fast at 2 pm on the following Monday. "
            "When was it correct?"
        ),
        "question_hi": (
            "एक घड़ी, जो समान रूप से चलती है, सोमवार को दोपहर 12 बजे 2 मिनट "
            "धीमी है, तथा अगले सोमवार को दोपहर 2 बजे 4 मिनट 48 सेकंड तेज है। "
            "यह कब सही थी?"
        ),
        "option_a": "2 pm on Tuesday/मंगलवार को दोपहर 2 बजे",
        "option_b": "2 pm on Wednesday/बुधवार को दोपहर 2 बजे",
        "option_c": "3 pm on Thursday/गुरूवार को दोपहर 3 बजे",
        "option_d": "1 pm on Friday/शुक्रवार को दोपहर 1 बजे",
        "correct_answer": "B",
    },
    # Q62
    {
        "question_number": 62,
        "difficulty": "easy",
        "question_en": (
            "How many times in a day are the hands of a clock in a straight line?"
        ),
        "question_hi": (
            "एक दिन में कितनी बार घड़ी की सुइयाँ एक सीधी रेखा में होती हैं?"
        ),
        "option_a": "48 times/48 बार",
        "option_b": "24 times/24 बार",
        "option_c": "44 times/44 बार",
        "option_d": "22 times/22 बार",
        "correct_answer": "C",
    },
    # Q63
    {
        "question_number": 63,
        "difficulty": "hard",
        "question_en": (
            "A watch which gains 5 seconds in 3 minutes was set right at 7 am. "
            "In the afternoon of the same day when the watch indicated quarter "
            "past 4 O'clock, the true time is-"
        ),
        "question_hi": (
            "एक घड़ी जो 3 मिनट में 5 सेकंड आगे हो जाती है, उसे सुबह 7 बजे "
            "सही समय पर सेट किया गया। उसी दिन दोपहर में जब घड़ी ने 4 बजकर "
            "15 मिनट दिखाए, तो सही समय है-"
        ),
        "option_a": "59⁷/₁₂ minutes past 3/3 बजकर 59⁷/₁₂ मिनट",
        "option_b": "4 pm/शाम 4 बजे",
        "option_c": "58⁷/₁₁ minutes past 3/3 बजकर 58⁷/₁₁ मिनट",
        "option_d": "2³/₁₁ minutes past 4/4 बजकर 2³/₁₁ मिनट",
        "correct_answer": "B",
    },
    # Q64
    {
        "question_number": 64,
        "difficulty": "hard",
        "question_en": (
            "At what time between 4 and 5 will the hands of a watch "
            "be equidistant from the figure 5?"
        ),
        "question_hi": (
            "4 और 5 के बीच किस समय घड़ी की सुइयाँ अंक 5 से समान दूरी पर होंगी?"
        ),
        "option_a": "27⁹/₁₁ min. past 4/4 बजकर 27⁹/₁₁ मिनट",
        "option_b": "27⁸/₁₃ min. past 4/4 बजकर 27⁸/₁₃ मिनट",
        "option_c": "27⁹/₁₃ min. past 4/4 बजकर 27⁹/₁₃ मिनट",
        "option_d": "None of these/इनमें से कोई नहीं",
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
