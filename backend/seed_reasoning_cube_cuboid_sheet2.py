"""
seed_reasoning_cube_cuboid_sheet2.py
=====================================
Seeds questions from Cube & Cuboid (Gagan Pratap Reasoning PDFs) - Sheet 2.
Subject : Reasoning
Topic   : Cube & Cuboid
Run     : python seed_reasoning_cube_cuboid_sheet2.py

Answer key verification:
  ImgQ1:  15cm->3cm; n=15/3=5; total=5^3=125                                    -> C
  ImgQ4:  12cm->2cm; n=12/2=6; total=6^3=216                                    -> A
  ImgQ5:  27 cubes->n=3; exactly 1 face=6*(3-2)^2=6                             -> B
  ImgQ6:  n=4 (side=1/4); exactly 1 face=6*(4-2)^2=24                           -> C
  ImgQ8:  125 cubes->n=5; exactly 2 faces=12*(5-2)=36                           -> C
  ImgQ12: 216 cubes->n=6; at-least-2 = corners+edges = 8+12*4=56                -> C
  ImgQ13: 343 cubes->n=7; at-least-1 = 343-(7-2)^3=343-125=218                  -> C
  ImgQ14: 216 cubes->n=6; at-most-2 = 216-8=208                                 -> C
  ImgQ15: 216 cubes->n=6; colored & at-most-2 = 6*16+12*4=96+48=144             -> D
  ImgQ16: 15cm->125 cubes; 125=5^3 -> side=15/5=3cm (SKIP-already in DB)        -> B
  ImgQ17: 125 cubes of 8cm^3 -> small side=2cm -> big=5*2=10cm (SKIP-in DB)     -> D
  ImgQ18: 125 cubes; 2 adj red,2 adj blue,2 adj green; red+green only edges
          = 3 edges * (5-2) = 9                                                  -> D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Cube_Cuboid_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"

QUESTIONS = [
    # ImgQ1 -> question_number=1
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": (
            "A 15 cm. colored cube is cut into 3 cm. Smaller cubes, what is the total "
            "number of cubes made?"
        ),
        "question_hi": (
            "एक 15 सेमी. के रंगे हुए घन को 3 सेमी. के छोटे-छोटे घनों में काटा जाता "
            "है, तब बनने वाले कुल छोटे घनों की संख्या बताइए?"
        ),
        "option_a": "64",
        "option_b": "216",
        "option_c": "125",
        "option_d": "27",
        "correct_answer": "C",
    },
    # ImgQ4 -> question_number=19 (Q4 slot taken by different question)
    {
        "question_number": 19,
        "difficulty": "easy",
        "question_en": (
            "A 12 cm. colored cube is cut into 2 cm. smaller cubes. What is the total "
            "number of cubes made?"
        ),
        "question_hi": (
            "एक 12 सेमी. के रंगे हुए घन को 2 सेमी. के छोटे-छोटे घनों में काटा जाता "
            "है, तब बनने वाले कुल छोटे घनों की संख्या कितनी होगी?"
        ),
        "option_a": "216",
        "option_b": "125",
        "option_c": "64",
        "option_d": "512",
        "correct_answer": "A",
    },
    # ImgQ5 -> question_number=20 (Q5 slot taken by different question)
    {
        "question_number": 20,
        "difficulty": "medium",
        "question_en": (
            "A bigger cube with all surfaces painted yellow is cut into 27 smaller cubes "
            "of equal size. How many smaller cubes are there which have only one surface "
            "painted?"
        ),
        "question_hi": (
            "सभी सतहों पर पीले रंग का एक घन 27 बराबर आकार के छोटे घनों में काटा जाता "
            "है। ऐसे कितने छोटे घन होंगे जिनकी केवल एक सतह रंगी हुई है?"
        ),
        "option_a": "1",
        "option_b": "6",
        "option_c": "8",
        "option_d": "12",
        "correct_answer": "B",
    },
    # ImgQ6 -> question_number=21 (Q6 slot taken by different question)
    {
        "question_number": 21,
        "difficulty": "medium",
        "question_en": (
            "All surfaces of a cube are colored. If a number of smaller cubes are taken "
            "out from it, each side 1/4 the size of the original cube's side, indicate "
            "the number of cubes with only one side painted."
        ),
        "question_hi": (
            "एक घन की सभी सतहें रंगी हुई हैं। यदि इसमें से कई छोटे घन निकाले जाते "
            "हैं, तो प्रत्येक पक्ष 1/4 मूल घन के पक्ष के आकार का होता है। केवल एक "
            "तरफ रंगे किये गये घनों की संख्या बताइए?"
        ),
        "option_a": "60",
        "option_b": "32",
        "option_c": "24",
        "option_d": "16",
        "correct_answer": "C",
    },
    # ImgQ8 -> question_number=8
    {
        "question_number": 8,
        "difficulty": "medium",
        "question_en": (
            "A cube of white material is painted black on all its surfaces. If it is cut "
            "into 125 smaller cubes of the same size, then how many cubes will have two "
            "sides painted black?"
        ),
        "question_hi": (
            "सफेद पदार्थ के एक घन की सभी सतहों को काला रंग किया जाता है। यदि इसको 125 "
            "बराबर छोटे घनों में काटा जाता है तो कितने छोटे घनों की दो सतह काले रंग "
            "से रंगी होंगी?"
        ),
        "option_a": "8",
        "option_b": "24",
        "option_c": "36",
        "option_d": "22",
        "correct_answer": "C",
    },
    # ImgQ12 -> question_number=22 (Q12 slot taken by different question)
    {
        "question_number": 22,
        "difficulty": "medium",
        "question_en": (
            "A colored cube is cut into 216 smaller cubes, then how many smaller cubes "
            "are there which have at least two surfaces painted?"
        ),
        "question_hi": (
            "एक रंगे हुए घन को 216 छोटे-छोटे घनों में काटा गया है, तब ऐसे घनों की "
            "संख्या कितनी होगी जिनकी कम से कम 2 सतह रंगी हुई है?"
        ),
        "option_a": "8",
        "option_b": "48",
        "option_c": "56",
        "option_d": "64",
        "correct_answer": "C",
    },
    # ImgQ13 -> question_number=13
    {
        "question_number": 13,
        "difficulty": "medium",
        "question_en": (
            "A colored cube is cut into 343 smaller cubes, then how many smaller cubes "
            "are there which have at least 1 surface painted?"
        ),
        "question_hi": (
            "एक रंगे हुए घन को 343 छोटे-छोटे घनों में काटा गया है, तब ऐसे घनों की "
            "संख्या कितनी होगी जिनकी कम से कम एक सतह रंगी हो?"
        ),
        "option_a": "150",
        "option_b": "60",
        "option_c": "218",
        "option_d": "216",
        "correct_answer": "C",
    },
    # ImgQ14 -> question_number=14
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": (
            "A coloured cube is cut into 216 smaller cubes, then how many smaller cubes "
            "are there which have atmost two surfaces painted?"
        ),
        "question_hi": (
            "एक रंगे हुए घन को 216 छोटे घनों में काटा जाता है, तब ऐसे कितने छोटे घन "
            "होंगे जिनकी अधिक से अधिक 2 सतह रंगी हो?"
        ),
        "option_a": "48",
        "option_b": "96",
        "option_c": "208",
        "option_d": "64",
        "correct_answer": "C",
    },
    # ImgQ15 -> question_number=15
    {
        "question_number": 15,
        "difficulty": "medium",
        "question_en": (
            "A colored cube is cut into 216 smaller cubes; then how many colored small "
            "cubes are there which have atmost two surfaces painted?"
        ),
        "question_hi": (
            "एक रंगे हुए घन को 216 कुल छोटे घनों में काटा जाता है; तब ऐसे कितने रंगे "
            "हुए छोटे घन होंगे जिनकी ज्यादा से ज्यादा 2 सतह रंगी हुई है?"
        ),
        "option_a": "48",
        "option_b": "64",
        "option_c": "96",
        "option_d": "144",
        "correct_answer": "D",
    },
    # ImgQ16 - already in DB, dedup will skip
    {
        "question_number": 16,
        "difficulty": "easy",
        "question_en": (
            "A 15 cm. colored cube is cut into 125 smaller cubes, then what is the "
            "length of the smaller cube?"
        ),
        "question_hi": (
            "एक 15 सेमी. लम्बाई के रंगीन घन को 125 छोटे-छोटे घनों में काटा जाता "
            "है तब छोटे घन की भुजा बताइए?"
        ),
        "option_a": "5cm",
        "option_b": "3cm",
        "option_c": "6cm",
        "option_d": "8cm",
        "correct_answer": "B",
    },
    # ImgQ17 - already in DB, dedup will skip
    {
        "question_number": 17,
        "difficulty": "easy",
        "question_en": (
            "A bigger colored cube is cut into 125 smaller cubes of 8 cm³, then "
            "what is the length of the bigger cube?"
        ),
        "question_hi": (
            "एक बड़े रंगे हुए घन को 125 छोटे-छोटे घनों में काटा गया है जिनमें प्रत्येक "
            "8 सेमी³ का है। तब बड़े घन की भुजा क्या होगी?"
        ),
        "option_a": "40cm",
        "option_b": "20cm",
        "option_c": "5cm",
        "option_d": "10cm",
        "correct_answer": "D",
    },
    # ImgQ18 -> question_number=18
    {
        "question_number": 18,
        "difficulty": "hard",
        "question_en": (
            "Two adjacent surfaces of a cube are painted red, two other adjacent surfaces "
            "are painted blue and two remaining adjacent surfaces are painted green. Now "
            "it is cut into 125 smaller cubes, then how many smaller cubes have only two "
            "surfaces painted with red and green color?"
        ),
        "question_hi": (
            "एक घन की दो निकटवर्ती सतहों को लाल रंग से, 2 अन्य निकटवर्ती सतहों को "
            "नीले रंग से और 2 बची हुई निकटवर्ती सतहों को हरे रंग से रंगा जाता है। "
            "अब इसे 125 छोटे-छोटे घनों में काटा जाए, तब ऐसे कितने छोटे घन होंगे "
            "जिनकी केवल 2 सतह लाल और हरे रंग से रंगी हों?"
        ),
        "option_a": "36",
        "option_b": "18",
        "option_c": "12",
        "option_d": "9",
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
