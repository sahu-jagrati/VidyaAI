"""
seed_reasoning_clock_sheet9.py
====================================
Seeds questions 65-67, 73-78 (Clock) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Clock
Run     : python seed_reasoning_clock_sheet9.py

Answer key verification:
  Q65: 4 min to 12=11:56; |330-308|=22°                                           -> A
  Q66: 180h; gain=54/5 min; rate=3/50 min/h; correct in 250/3h=83h20m from
       8AM Sun=7:20PM Wed=20 min past 7 pm Wed                                     -> B
  Q67: gain/interval=720/11-65=5/11; in 24h=(1440/65)×(5/11)=1440/143=10 10/143  -> B
  Q73: next bell 7:45, interval 45 -> last bell 7:00; 5 min ago -> now=7:05 AM    -> C
  Q74: left 15 min early; travel 10 min; arrived 8:40 -> departed 8:30;
       usual departure=8:30+15=8:45 AM                                             -> B
  Q75: Sanjay at 8:30 (20min before 8:50); late person at 8:30+30=9:00;
       scheduled=9:00-40=8:20                                                      -> C
  Q76: 10AM-1:27PM=207min; 4 periods+3 rests=4P+15=207 -> P=48 min              -> B
  Q77: sequence L•4Pβ∅N7@906P•D*EHT↓M>3#; pos6=∅, pos7=N, pos11=0             -> B
  Q78: C=1,D=2,...R=16                                                             -> D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Clock_Sheet9"
SUBJECT = "Reasoning"
TOPIC   = "Clock"

QUESTIONS = [
    # Q65
    {
        "question_number": 65,
        "difficulty": "easy",
        "question_en": (
            "At what angle are the two hands of a clock inclined at "
            "4 minutes to 12?"
        ),
        "question_hi": (
            "12 बजने से 4 मिनट पहले घड़ी की दोनों सुइयाँ किस कोण पर झुकी हुई हैं?"
        ),
        "option_a": "22°",
        "option_b": "20°",
        "option_c": "21°",
        "option_d": "23°",
        "correct_answer": "A",
    },
    # Q66
    {
        "question_number": 66,
        "difficulty": "hard",
        "question_en": (
            "A watch which gains uniformly, is 5 min. slow at 8 O'clock in the "
            "morning on Sunday, and is 5 min. 48 sec. fast at 8 pm on following "
            "Sunday. When was it correct?"
        ),
        "question_hi": (
            "एक घड़ी जो समान रूप से आगे बढ़ती है, रविवार को सुबह 8 बजे 5 मिनट "
            "धीमी है, और अगले रविवार को शाम 8 बजे 5 मिनट 48 सेकंड तेज है। "
            "यह कब सही थी?"
        ),
        "option_a": "20 min. past 7 pm on Tuesday/मंगलवार को शाम 7 बजे से 20 मिनट पहले",
        "option_b": "20 min. past 7 pm on Wednesday/बुधवार को शाम 7 बजे से 20 मिनट पहले",
        "option_c": "10 min. past 7 pm on Tuesday/मंगलवार को शाम 7 बजे से 10 मिनट पहले",
        "option_d": "10 min. past 7 pm on Wednesday/बुधवार को शाम 7 बजे से 10 मिनट पहले",
        "correct_answer": "B",
    },
    # Q67
    {
        "question_number": 67,
        "difficulty": "hard",
        "question_en": (
            "If the hands of a clock coincide every 65 minutes of correct time, "
            "how much does the clock gain or lose in 24 hours?"
        ),
        "question_hi": (
            "यदि किसी घड़ी की सुइयाँ प्रत्येक 65 मिनट पर सही समय पर मिलती हैं, "
            "तो 24 घंटे में घड़ी को कितना लाभ या हानि होगी?"
        ),
        "option_a": "11¹⁰/₁₄₃ min. gain/11¹⁰/₁₄₃ मिनट आगे",
        "option_b": "10¹⁰/₁₄₃ min. gain/10¹⁰/₁₄₃ मिनट आगे",
        "option_c": "11⁹/₁₄₃ min. gain/11⁹/₁₄₃ मिनट आगे",
        "option_d": "None of these/इनमें से कोई नहीं",
        "correct_answer": "B",
    },
    # Q73
    {
        "question_number": 73,
        "difficulty": "easy",
        "question_en": (
            "The priest told the devotes, 'The bell is rung at regular intervals "
            "of 45 min. The last bell was rung 5 min. ago. The next bell is due "
            "to be rung at 7:45 am.' At what time did the priest give the "
            "information to the devotes?"
        ),
        "question_hi": (
            "पुजारी ने भक्तों को बताया, 'घंटी 45 घंटेमिनट के नियमित अंतराल पर "
            "बजाई जाती है। पिछली घंटी 5 मिनट पहले बजाई गई थी। अगली घंटी सुबह "
            "7:45 बजे बजाई जाएगी।' पुजारी ने भक्तों को किस समय सूचना दी?"
        ),
        "option_a": "6:55 am",
        "option_b": "7:00 am",
        "option_c": "7:05 am",
        "option_d": "7:40 am",
        "correct_answer": "C",
    },
    # Q74
    {
        "question_number": 74,
        "difficulty": "easy",
        "question_en": (
            "Raveena left her house for the bus stop 15 minutes earlier than usual. "
            "It takes 10 min. to reach the stop. She reached the stop at 8:40 am. "
            "What time does she usually leave home for the bus stop?"
        ),
        "question_hi": (
            "रवीना अपने घर से बस स्टॉप के लिए सामान्य से 15 मिनट पहले निकली। "
            "बस स्टॉप तक पहुँचने में उसे 10 मिनट लगते हैं। वह बस स्टॉप पर "
            "8:40 बजे पहुँची। वह आमतौर पर किस समय घर से बस स्टॉप के लिए निकलती है?"
        ),
        "option_a": "8:55 am",
        "option_b": "8:45 am",
        "option_c": "8:30 am",
        "option_d": "8:05 am",
        "correct_answer": "B",
    },
    # Q75
    {
        "question_number": 75,
        "difficulty": "medium",
        "question_en": (
            "Reaching the place of meeting 20 minutes before 8:50 hrs, Sanjay "
            "found himself 30 minutes earlier than the person who came 40 minutes "
            "late. What was the scheduled time of meeting?"
        ),
        "question_hi": (
            "8:50 बजे से 20 मिनट पहले मीटिंग स्थल पर पहुँचने पर संजय ने पाया "
            "कि वह 40 मिनट देरी से आने वाले व्यक्ति से 30 मिनट पहले पहुँच गया। "
            "मीटिंग का निर्धारित समय क्या था?"
        ),
        "option_a": "8:09",
        "option_b": "8:05",
        "option_c": "8:20",
        "option_d": "8:10",
        "correct_answer": "C",
    },
    # Q76
    {
        "question_number": 76,
        "difficulty": "medium",
        "question_en": (
            "A class starts at 10:00 am. and lasts till 1:27 pm. Four periods are "
            "held during this interval. After every period, 5 minutes rest is given "
            "to the students. The exact duration of each period is?"
        ),
        "question_hi": (
            "एक कक्षा सुबह 10:00 बजे शुरू होती है और दोपहर 1:27 बजे तक चलती है। "
            "इस अंतराल के दौरान चार पीरियड आयोजित किए जाते हैं। प्रत्येक पीरियड "
            "के बाद छात्रों को 5 मिनट का आराम दिया जाता है। प्रत्येक पीरियड की "
            "सही अवधि क्या है?"
        ),
        "option_a": "40 min.",
        "option_b": "48 min.",
        "option_c": "51 min.",
        "option_d": "53 min.",
        "correct_answer": "B",
    },
    # Q77
    {
        "question_number": 77,
        "difficulty": "hard",
        "question_en": (
            "A series of letters, digits and symbols is given below:\n"
            "L•4Pβ∅N7@906P•D*EHT↓M>3#\n"
            "If the digits/Number of the clock are replaced in such a way that "
            "∅ takes the place of 6, N takes the place of 7 and this arrangement "
            "goes on in the same way, then what comes in the place of 11?"
        ),
        "question_hi": (
            "नीचे अक्षरों, अंकों और प्रतीकों की एक श्रृंखला दी गई है:\n"
            "L•4Pβ∅N7@906P•D*EHT↓M>3#\n"
            "यदि घड़ी के डायल के अंक/संख्या को इस प्रकार प्रतिस्थापित किया जाए "
            "कि 6, 6 के स्थान पर आ जाए, N, 7 के स्थान पर आ जाए और यह व्यवस्था "
            "इसी प्रकार चलती रहे, तो 11 के स्थान पर क्या आएगा?"
        ),
        "option_a": "7",
        "option_b": "0",
        "option_c": "*",
        "option_d": "9",
        "correct_answer": "B",
    },
    # Q78
    {
        "question_number": 78,
        "difficulty": "medium",
        "question_en": (
            "The digits/Number from 1 to 24 to be represented by the dial of clock "
            "are replaced by letters of English alphabet. The replacement is started "
            "with letter C. Find the letter which represent 16 O'clock."
        ),
        "question_hi": (
            "घड़ी के डायल द्वारा दर्शाए जाने वाले 1 से 24 तक के अंक/संख्या को "
            "अंग्रेजी वर्णमाला के अक्षरों से बदल दिया जाता है। प्रतिस्थापन की "
            "शुरुआत अक्षर C से होती है। वह अक्षर ज्ञात कीजिए जो 16 बजे को दर्शाता है।"
        ),
        "option_a": "W",
        "option_b": "P",
        "option_c": "S",
        "option_d": "R",
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
