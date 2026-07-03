"""
seed_discount_sheet2.py
========================
Seeds questions 1–7 (Discount — effective discount / free articles)
from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Discount
Run     : python seed_discount_sheet2.py

Answer key verification:
  Q1:  Customer pays 760 for 28.5kg; actual value=950; (950-760)/950×100=20%  → B
  Q2:  SP=73.6; pen=8.60; CP=65/1.17=55.56 (SSC MTS 2024)                    → C
  Q3:  Pay5 get7; discount=2/7×100=28.57%≈28.56% (SSC GD 2025)               → A
  Q4:  Pay5 get6; discount=1/6×100=16.67% (SSC CGL Mains 2024)                → D
  Q5:  Pay8 get11; discount=3/11×100=27.27% (MTS 2020)                        → C
  Q6:  x/(5+x)=3/8 → x=3                                                      → B
  Q7:  1-(0.82×0.78)=36.04% (SSC CGL 2022)                                   → A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Discount_Sheet2"
SUBJECT = "Quant"
TOPIC   = "Discount"

QUESTIONS = [
    # Q1
    {
        "question_number": 1,
        "difficulty": "hard",
        "question_en": "A trader sells 30 kg of sugar at Rs 1000. A customer asks 24% discount and trader agreed to it but instead of 1 kg he gives 5% less sugar. What is the effective discount that the customer gets?",
        "question_hi": "एक व्यापारी 30 किलो चीनी 1000 रु. में बेचता है। एक ग्राहक 24% का बट्टा चाहता है और व्यापारी सहमत हो जाता है लेकिन 1 किलो की जगह वह 5% कम चीनी देता है। व्यापारी को प्रभावी बट्टा क्या मिलता है?",
        "option_a": "25%",
        "option_b": "20%",
        "option_c": "15%",
        "option_d": "16.67%",
        "correct_answer": "B",
    },
    # Q2 — SSC MTS 2024
    {
        "question_number": 2,
        "difficulty": "hard",
        "question_en": "A shopkeeper sells a notebook that has a marked price of Rs 80 at a discount of 8% and gives a pen costing Rs 8.60 free with each notebook. Even then he makes a profit of 17%. Find the cost price of each notebook correct to two decimal places. (SSC MTS 2024)",
        "question_hi": "एक दुकानदार एक नोटबुक जिसका अंकित मूल्य Rs 80 है, 8% की छूट पर बेचता है और प्रत्येक नोटबुक के साथ Rs 8.60 मूल्य का एक पेन मुफ्त देता है। फिर भी उसे 17% का लाभ होता है। प्रत्येक नोट बुक का लागत मूल्य दशमलव के दो स्थानों तक सही ज्ञात कीजिए। (SSC MTS 2024)",
        "option_a": "Rs 49.75",
        "option_b": "Rs 45.35",
        "option_c": "Rs 55.56",
        "option_d": "Rs 51.32",
        "correct_answer": "C",
    },
    # Q3 — SSC GD 2025
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": "A store is running a 'Buy 5 Get 2 Free' promotion scheme. What is the net discount percentage? (SSC GD 2025)",
        "question_hi": "एक स्टोर '5 खरीदें 2 मुफ्त पाएं' प्रमोशन स्कीम चला रहा है। शुद्ध छूट प्रतिशत क्या है? (SSC GD 2025)",
        "option_a": "28.56%",
        "option_b": "22.5%",
        "option_c": "40%",
        "option_d": "33.33%",
        "correct_answer": "A",
    },
    # Q4 — SSC CGL Mains 2024
    {
        "question_number": 4,
        "difficulty": "easy",
        "question_en": "Murlidhar, the owner of a grocery store, offers a discount scheme 'buy 5 water bottles get 1 for free' to his customers. What is the effective percentage discount offered by Murlidhar (correct up to two decimal places)? (SSC CGL Mains 2024)",
        "question_hi": "एक किराने की दुकान के मालिक, मुरलीधर अपने ग्राहकों को छूट स्कीम '5 पानी की बोतलें खरीदें और 1 बोतल मुफ्त पाएं' उपलब्ध कराता है। मुरलीधर द्वारा दी गई प्रभावी प्रतिशत छूट (दो दशमलव स्थानों तक) कितनी है? (SSC CGL Mains 2024)",
        "option_a": "13.67%",
        "option_b": "20.00%",
        "option_c": "13.33%",
        "option_d": "16.67%",
        "correct_answer": "D",
    },
    # Q5 — MTS 2020
    {
        "question_number": 5,
        "difficulty": "easy",
        "question_en": "During festivals, a banner on a shop displays 'Pay for 8 and get 11'. The discount percentage offered is: (MTS 2020)",
        "question_hi": "त्योहारों के दौरान, किसी दुकान पर लगे बैनर पर लिखा था, '8 के लिए भुगतान करें और 11 पाएं।' छूट प्रतिशत क्या है? (MTS 2020)",
        "option_a": "33%",
        "option_b": "37.5%",
        "option_c": "27.27%",
        "option_d": "37.5% (variant)",
        "correct_answer": "C",
    },
    # Q6
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": "How many articles should be given free on 5 articles to provide 37.5% discount to customers?",
        "question_hi": "ग्राहकों को 37.5% छूट प्रदान करने के लिए 5 वस्तुओं पर कितनी वस्तुएँ मुफ्त में देनी चाहिए?",
        "option_a": "2",
        "option_b": "3",
        "option_c": "4",
        "option_d": "1",
        "correct_answer": "B",
    },
    # Q7 — SSC CGL 2022
    {
        "question_number": 7,
        "difficulty": "easy",
        "question_en": "Successive discounts of 18% and 22% are equal to a single discount of ______. (SSC CGL 2022)",
        "question_hi": "18% और 22% की क्रमिक छूट _______ की एक छूट के बराबर है। (SSC CGL 2022)",
        "option_a": "36.04%",
        "option_b": "35.04%",
        "option_c": "37.04%",
        "option_d": "34.04%",
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
