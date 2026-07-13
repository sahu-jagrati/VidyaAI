"""
seed_reasoning_clock_sheet11.py
====================================
Seeds questions 87-95 (Clock) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Clock
Run     : python seed_reasoning_clock_sheet11.py

Answer key verification (confirmed against answer key in PDF):
  Q87: LCM(16,18)=144min=2h24min; 12:00+2:24=2:24PM                               -> C
  Q88: cumulative slow: 5+10+15+20+25+30=30min; clock shows 6:00-0:30=5:30AM      -> B
  Q89: loses 16min/day; 89 clock h → 90 true h → 5AM+90h=11PM                     -> C
  Q90: 6-7 coincide: t=30×12/11=360/11=32 8/11 min past 6                          -> A
  Q91: 5×40=200min=3h20min; latest start=10PM-3:20=6:40PM                          -> A
  Q92: excluded A,B,E,F,I,J,O,P,U,V; C=1..T=12; N:T=8:00 to 11:25=205min;
       4 breaks(7+9+11+13=40); 5P=165; P=33                                         -> B
  Q93: 7:30 minute@180°=West; 12=East; hour@225°→315°=NW                           -> C
  Q94: gains 2^(N-1) min at Nth hour; 2^6=64>60 at 7th hour                        -> C
  Q95: 50min ago=4:45; now=5:35; until 6:00=25min                                  -> C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Clock_Sheet11"
SUBJECT = "Reasoning"
TOPIC   = "Clock"

QUESTIONS = [
    # Q87
    {
        "question_number": 87,
        "difficulty": "medium",
        "question_en": (
            "In Ravi's clock shop, two clocks were brought for repairs. One clock "
            "has the cuckoo coming out every sixteen minutes, while the other one "
            "has the cuckoo coming out every eighteen minutes. Both cuckoos come "
            "out at 12.00 noon. When will they both come out together again?"
        ),
        "question_hi": (
            "रवि की घड़ी की दुकान में दो घड़ियाँ मरम्मत के लिए लाई गई थीं। एक "
            "घड़ी में हर सोलह मिनट पर कोयल निकलती है, जबकि दूसरी में हर अठारह "
            "मिनट पर कोयल निकलती है। दोनों कोयल दोपहर 12 बजे निकलती हैं। वे "
            "दोनों फिर कब एक साथ निकलेंगी?"
        ),
        "option_a": "2:06 PM",
        "option_b": "2:08 PM",
        "option_c": "2:24 PM",
        "option_d": "2:32 PM",
        "correct_answer": "C",
    },
    # Q88
    {
        "question_number": 88,
        "difficulty": "medium",
        "question_en": (
            "A clock goes slow from midnight by 5 mins at the end of the first "
            "hour, by 10 mins at the end of the second hour, by 15 mins at the "
            "end of the 3rd hour and so on. What will be the time by this clock "
            "after 6 hours?"
        ),
        "question_hi": (
            "एक घड़ी आधी रात से पहले घंटे के अंत में 5 मिनट धीमी हो जाती है, "
            "दूसरे घंटे के अंत में 10 मिनट धीमी हो जाती है, तीसरे घंटे के अंत में "
            "15 मिनट धीमी हो जाती है और इसी तरह आगे भी धीमी होती जाती है। "
            "6 घंटे बाद इस घड़ी में क्या समय होगा?"
        ),
        "option_a": "6:00 am",
        "option_b": "5:30 am",
        "option_c": "6:30 am",
        "option_d": "5:15 am",
        "correct_answer": "B",
    },
    # Q89
    {
        "question_number": 89,
        "difficulty": "medium",
        "question_en": (
            "A clock is set right at 5 a.m. The clock loses 16 minutes in "
            "24 hours. What will be the true time when the clock indicates "
            "10 p.m. on 4th day?"
        ),
        "question_hi": (
            "एक घड़ी को सुबह 5 बजे ठीक किया गया है। घड़ी 24 घंटे में 16 मिनट "
            "पीछे हो जाती है। चौथे दिन जब घड़ी रात के 10 बजे दिखाएगी तो "
            "सही समय क्या होगा?"
        ),
        "option_a": "12pm",
        "option_b": "1pm",
        "option_c": "11pm",
        "option_d": "2pm",
        "correct_answer": "C",
    },
    # Q90
    {
        "question_number": 90,
        "difficulty": "hard",
        "question_en": (
            "At what time are the hands of clocks together between 6 and 7?"
        ),
        "question_hi": (
            "किस समय घड़ी की सुइयाँ 6 और 7 के बीच एक साथ होंगी?"
        ),
        "option_a": "32⁸/₁₁ minutes past 6/6 बजकर 32⁸/₁₁ मिनट",
        "option_b": "34⁸/₁₁ minutes past 6/6 बजकर 34⁸/₁₁ मिनट",
        "option_c": "30⁸/₁₁ minutes past 6/6 बजकर 30⁸/₁₁ मिनट",
        "option_d": "32⁵/₇ minutes past 6/6 बजकर 32⁵/₇ मिनट",
        "correct_answer": "A",
    },
    # Q91
    {
        "question_number": 91,
        "difficulty": "easy",
        "question_en": (
            "Kamala would like to complete all her home-work before 10.00 p.m. "
            "in order to watch an important TV programme. She has 40 minutes "
            "assignment in each of her five prepared subjects. What is the latest "
            "time at which she can start and still complete her home-work in time "
            "for the programme?"
        ),
        "question_hi": (
            "कमला एक महत्वपूर्ण टीवी कार्यक्रम देखने के लिए रात 10 बजे से पहले "
            "अपना सारा गृहकार्य पूरा करना चाहती है। उसे अपने पाँच तैयार विषयों "
            "में से प्रत्येक में 40 मिनट असाइनमेंट मिला है। वह किस अंतिम समय पर "
            "अपना गृहकार्य शुरू कर सकती है और कार्यक्रम के समय में भी उसे पूरा "
            "कर सकती है?"
        ),
        "option_a": "6:40",
        "option_b": "6:50",
        "option_c": "7:00",
        "option_d": "5:40",
        "correct_answer": "A",
    },
    # Q92
    {
        "question_number": 92,
        "difficulty": "hard",
        "question_en": (
            "The digits/numbers from 1 to 12 of the clock dial are replaced by "
            "the letters of the English alphabet. The replacement starts with the "
            "letter 'C' but vowels and immediate next consonants of vowel are not "
            "included in the replacement. Classes in the school start at N:T and "
            "last till a time when the minute hand is at K and the hour hand "
            "between S and T, very slightly ahead of S. Five periods of equal "
            "duration are held during this interval. The break of 7 minutes is "
            "given after 1st period and duration of break increases by 2 minutes "
            "after each period. The exact duration of a period in minutes is:"
        ),
        "question_hi": (
            "घड़ी के डायल के 1 से 12 तक के अंक/संख्याओं को अंग्रेजी वर्णमाला के "
            "अक्षरों से बदल दिया जाता है। प्रतिस्थापन अक्षर 'C' से शुरू होता है, "
            "लेकिन स्वर और स्वर के तत्काल अगले व्यंजन प्रतिस्थापन में शामिल नहीं "
            "होते हैं। स्कूल में कक्षाएँ N:T से शुरू होती हैं और उस समय तक चलती "
            "हैं जब मिनट की सुई K पर होती है, और घंटे की सुई S और T के बीच होती "
            "है, जो S से बहुत थोड़ा आगे होती है। इस अंतराल के दौरान बराबर अवधि "
            "के पाँच पीरियड आयोजित किए जाते हैं। पहली अवधि के बाद छात्रों को "
            "7 मिनट का ब्रेक दिया जाता है और प्रत्येक अवधि के बाद ब्रेक की "
            "अवधि 2 मिनट बढ़ जाती है। मिनटों में एक अवधि की सटीक अवधि है:"
        ),
        "option_a": "32",
        "option_b": "33",
        "option_c": "34",
        "option_d": "35",
        "correct_answer": "B",
    },
    # Q93
    {
        "question_number": 93,
        "difficulty": "medium",
        "question_en": (
            "A watch reads 7.30. If the minute hand points West, then in which "
            "direction will the hour hand point?"
        ),
        "question_hi": (
            "एक घड़ी में 7.30 बजे हैं। यदि मिनट की सुई पश्चिम की ओर इशारा करती "
            "है, तो घंटे की सुई किस दिशा की ओर इशारा करेगी?"
        ),
        "option_a": "North/उत्तर",
        "option_b": "North East/उत्तर पूर्व",
        "option_c": "North West/उत्तर पश्चिम",
        "option_d": "South East/दक्षिण पूर्व",
        "correct_answer": "C",
    },
    # Q94
    {
        "question_number": 94,
        "difficulty": "hard",
        "question_en": (
            "A clock goes fast by one minute during the first hour, by two minutes "
            "at the end of the second hour, by 4 minutes at the end of 3rd hour, "
            "by eight minutes by the end of 4th hour and so on. At the end of "
            "which hour, will it be fast by just over sixty minutes?"
        ),
        "question_hi": (
            "एक घड़ी पहले घंटे में एक मिनट तेज चलती है, दूसरे घंटे के अंत में "
            "दो मिनट तेज चलती है, तीसरे घंटे के अंत में 4 मिनट तेज चलती है, "
            "चौथे घंटे के अंत में आठ मिनट तेज चलती है, और इसी तरह आगे भी चलती "
            "रहती है। किस घंटे के अंत में यह लगभग साठ मिनट तेज चलेगी?"
        ),
        "option_a": "Fifth/पाँचवाँ",
        "option_b": "Sixth/छठा",
        "option_c": "Seventh/सातवाँ",
        "option_d": "Eighth/आठवाँ",
        "correct_answer": "C",
    },
    # Q95
    {
        "question_number": 95,
        "difficulty": "easy",
        "question_en": (
            "If 50 minutes ago, it was 45 minutes past four O'clock, "
            "how many minutes is it until six O'clock?"
        ),
        "question_hi": (
            "यदि 50 मिनट पहले, चार बजे के 45 मिनट हुए थे, तो छह बजे तक "
            "कितने मिनट बाकी हैं?"
        ),
        "option_a": "45",
        "option_b": "15",
        "option_c": "25",
        "option_d": "35",
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
