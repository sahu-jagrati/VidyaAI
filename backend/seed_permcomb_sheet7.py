"""
seed_permcomb_sheet7.py
========================
Seeds questions 51–59 (Permutation & Combination) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Permutation & Combination
Run     : python seed_permcomb_sheet7.py

Answer key verification:
  Q51: n(n-1)=600 → n=25                                                        → A
  Q52: C(20,2)=190                                                               → B
  Q53: C(15,3)=455                                                               → B
  Q54: C(10,3)-C(4,3)=120-4=116                                                 → C
  Q55: 2 compulsory fixed; C(7,3)=35                                             → B
  Q56: C(7,5)×C(5,2)=21×10=210                                                  → A
  Q57: C(5,4)×C(12,7)=5×792=3960                                                → A
  Q58: 22-2-4=16 free; need 11-2=9 → C(16,9)=C(16,7)=16C7                     → B
  Q59: C(5,3)×C(2,1)×C(9,7)=10×2×36=720                                       → B
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_PermComb_Sheet7"
SUBJECT = "Quant"
TOPIC   = "Permutation & Combination"

QUESTIONS = [
    # Q51
    {
        "question_number": 51,
        "difficulty": "medium",
        "question_en": "On a new year day every student of a class sends a card to every other student. The postman delivers 600 cards. How many students are there in the class?",
        "question_hi": "नए साल के दिन कक्षा का प्रत्येक छात्र प्रत्येक दूसरे छात्र को एक कार्ड भेजता है। डाकिया 600 कार्ड वितरित करता है। कक्षा में कितने छात्र हैं?",
        "option_a": "25",
        "option_b": "20",
        "option_c": "30",
        "option_d": "60",
        "correct_answer": "A",
    },
    # Q52
    {
        "question_number": 52,
        "difficulty": "easy",
        "question_en": "How many chords can be drawn through 20 points on a circle?",
        "question_hi": "एक वृत पर 20 बिंदुओं से होकर कितनी जीवाएँ खींची जा सकती हैं?",
        "option_a": "10",
        "option_b": "190",
        "option_c": "20!",
        "option_d": "270",
        "correct_answer": "B",
    },
    # Q53
    {
        "question_number": 53,
        "difficulty": "easy",
        "question_en": "There are 15 points in a plane, no three of which are collinear. Find the number of triangles formed by joining them.",
        "question_hi": "एक समतल में 15 बिंदु हैं, जिनमें से कोई भी तीन संरेख नहीं हैं। इन्हें मिलाने से बनने वाले त्रिभुजों की संख्या ज्ञात कीजिए।",
        "option_a": "435",
        "option_b": "455",
        "option_c": "420",
        "option_d": "441",
        "correct_answer": "B",
    },
    # Q54
    {
        "question_number": 54,
        "difficulty": "medium",
        "question_en": "There are 10 points on a surface, 4 of them are collinear. How many triangles can be formed from these points?",
        "question_hi": "एक सतह पर 10 बिंदु हैं जिनमें से 4 रैखिक हैं। इन बिंदुओं से कितने त्रिभुज बनेंगे?",
        "option_a": "120",
        "option_b": "110",
        "option_c": "116",
        "option_d": "114",
        "correct_answer": "C",
    },
    # Q55
    {
        "question_number": 55,
        "difficulty": "medium",
        "question_en": "In how many ways can a student choose a programme of 5 courses if 9 courses are available and 2 specific courses are compulsory for every student?",
        "question_hi": "यदि 9 पाठ्यक्रम उपलब्ध हैं और प्रत्येक छात्र के लिए 2 विशिष्ट पाठ्यक्रम अनिवार्य हैं, तो एक छात्र कितने तरीकों से 5 पाठ्यक्रमों का कार्यक्रम चुन सकता है?",
        "option_a": "25",
        "option_b": "35",
        "option_c": "70",
        "option_d": "65",
        "correct_answer": "B",
    },
    # Q56
    {
        "question_number": 56,
        "difficulty": "medium",
        "question_en": "There are 7 men and 5 women. In how many ways can a group of 5 men and 2 women be formed?",
        "question_hi": "7 पुरुष और 5 महिलाएं हैं। इनमें 5 पुरुषों और 2 महिलाओं का एक समूह कितने तरीकों से बनाया जा सकता है?",
        "option_a": "210",
        "option_b": "45",
        "option_c": "126",
        "option_d": "90",
        "correct_answer": "A",
    },
    # Q57
    {
        "question_number": 57,
        "difficulty": "hard",
        "question_en": "In how many ways can one select a cricket team of 11 from 17 players in which only 5 persons can bowl, if each cricket team of 11 must include exactly 4 bowlers?",
        "question_hi": "17 खिलाड़ियों में से एक क्रिकेट टीम 11 का एक तरीकों से चुनी जा सकती है, जिसमें केवल 5 व्यक्ति गेंदबाजी कर सकते हैं, यदि 11 खिलाड़ियों की प्रत्येक क्रिकेट टीम में ठीक 4 गेंदबाज शामिल होने चाहिए?",
        "option_a": "3960",
        "option_b": "4040",
        "option_c": "5100",
        "option_d": "3850",
        "correct_answer": "A",
    },
    # Q58
    {
        "question_number": 58,
        "difficulty": "hard",
        "question_en": "The number of ways in which a team of 11 players can be selected from 22 players including 2 of them and excluding 4 of them.",
        "question_hi": "उन तरीकों की संख्या ज्ञात कीजिए जिनसे यारह खिलाड़ियों की एक टीम को 22 खिलाड़ियों की टीम से चुना जा सकता है, जिनमें से 2 को अवश्य शामिल किया जाता है और उनमें से 4 को कतई शामिल नहीं किया जाता है।",
        "option_a": "¹⁶C₆",
        "option_b": "¹⁶C₇",
        "option_c": "¹⁶C₈",
        "option_d": "²⁰C₇",
        "correct_answer": "B",
    },
    # Q59
    {
        "question_number": 59,
        "difficulty": "hard",
        "question_en": "In a touring cricket team there are 16 players in all including 5 bowlers and 2 wicket-keepers. How many teams of 11 players from these can be chosen so as to include three bowlers and one wicket-keeper?",
        "question_hi": "एक भ्रमणशील क्रिकेट टीम में 5 गेंदबाज और 2 विकेटकीपर सहित कुल 16 खिलाड़ी हैं। इनमें से 11 खिलाड़ियों की कितनी टीमें चुनी जा सकती हैं, ताकि तीन गेंदबाज और एक विकेटकीपर शामिल हो सकें?",
        "option_a": "650",
        "option_b": "720",
        "option_c": "750",
        "option_d": "640",
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
        print(f"\nDone — inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
