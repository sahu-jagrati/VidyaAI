"""
seed_discount_sheet1.py
========================
Seeds questions 1–6 (Discount) from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Discount
Run     : python seed_discount_sheet1.py

Answer key verification:
  Q1: 2/5×MP=3/4×SP→SP/MP=8/15; discount%=7/15×100=46.66%                   → A
  Q2: 26% of 2050=533 (SSC CGL Mains 2024)                                    → A
  Q3: (21600-19872)/21600×100=1728/21600=8% (SSC CPO 2023)                   → A
  Q4: MP=7710+1285=8995; 1285/8995=1/7=14.28%=14 2/7%                        → B
  Q5: 12.5% discount→SP=7MP/8→MP:SP=8:7                                      → D
  Q6: SP=CP=0.55MP; markup=0.45/0.55×100=81.81%                              → A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Discount_Sheet1"
SUBJECT = "Quant"
TOPIC   = "Discount"

QUESTIONS = [
    # Q1
    {
        "question_number": 1,
        "difficulty": "medium",
        "question_en": "2/5 of marked price is equal to 3/4 of selling price. What is the discount percent?",
        "question_hi": "अंकित मूल्य का 2/5 विक्रय मूल्य के 3/4 के बराबर है। छूट का प्रतिशत क्या है?",
        "option_a": "46.66%",
        "option_b": "25%",
        "option_c": "50%",
        "option_d": "66.67%",
        "correct_answer": "A",
    },
    # Q2 — SSC CGL Mains 2024
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": "On Republic Day, a retail store offers a 26% discount on total purchase. If Manish buys items worth Rs 2,050, how much money (in Rs) will he save through the scheme? (SSC CGL Mains 2024)",
        "question_hi": "गणतंत्र दिवस के अवसर पर एक खुदरा स्टोर एक स्कीम देता है, जहाँ ग्राहक अपनी कुल खरीद पर 26% की छूट का लाभ उठा सकते हैं। यदि मनीष Rs 2,050 की वस्तुएँ खरीदता है, तो वह स्कीम के द्वारा कितनी राशि बचायेगा? (SSC CGL Mains 2024)",
        "option_a": "533",
        "option_b": "544",
        "option_c": "522",
        "option_d": "511",
        "correct_answer": "A",
    },
    # Q3 — SSC CPO 2023
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": "The marked price of a refrigerator is Rs 21600. It is sold at Rs 19872 after allowing a certain discount. Find the discount percentage? (SSC CPO 2023)",
        "question_hi": "एक रेफ्रिजरेटर का अंकित मूल्य Rs 21600 रुपये है। एक निश्चित छूट देने के बाद इसे 19872 रुपये में बेचा जाता है। छूट प्रतिशत ज्ञात कीजिये?",
        "option_a": "8%",
        "option_b": "15%",
        "option_c": "12%",
        "option_d": "5%",
        "correct_answer": "A",
    },
    # Q4
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": "A person purchased a saree for Rs 7710 after availing a net discount of Rs 1285. The percentage of discount the saree shop offers is?",
        "question_hi": "एक व्यक्ति ने Rs 1285 की निवल छूट मिलने पर साड़ी Rs 7710 में खरीदी। साड़ी दुकानदार ने साड़ी पर कितने प्रतिशत छूट दी?",
        "option_a": "14 2/7% (first type)",
        "option_b": "14 2/7%",
        "option_c": "14 2/5% (first type)",
        "option_d": "14 2/5%",
        "correct_answer": "B",
    },
    # Q5
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": "A shopkeeper marks an article at such a price that after giving a discount of 12½% on the marked price, he still earns a profit of 15%. What is the ratio of the marked price to the selling price of the article?",
        "question_hi": "एक दुकानदार एक वस्तु की कीमत इस प्रकार अंकित करता है कि अंकित मूल्य पर 12½% की छूट देने के बाद भी उसे 15% का लाभ होता है। अंकित मूल्य का विक्रय मूल्य से अनुपात ज्ञात कीजिए।",
        "option_a": "7:9",
        "option_b": "6:5",
        "option_c": "6:1",
        "option_d": "8:7",
        "correct_answer": "D",
    },
    # Q6
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": "A shopkeeper offers a discount of 45% on the MRP of his goods and thus ends up selling at CP. What was % markup?",
        "question_hi": "एक दुकानदार अंकित मूल्य पर 45% की छूट देता है और इस प्रकार वह क्रय मूल्य पर वस्तु को बेचता है। ज्ञात कीजिए उसने कितने % अधिक मूल्य अंकित किया था।",
        "option_a": "81.81%",
        "option_b": "80%",
        "option_c": "77.77%",
        "option_d": "90.9%",
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
        print(f"\nDone — inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
