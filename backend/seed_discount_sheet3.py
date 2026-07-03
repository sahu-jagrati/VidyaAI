"""
seed_discount_sheet3.py
========================
Seeds questions 8–13 (Discount — successive discounts)
from Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Discount
Run     : python seed_discount_sheet3.py

Answer key verification:
  Q8:  1-(0.65×0.88)=1-0.572=42.8%                                            → A
  Q9:  1-(0.75)³=1-0.421875=57.81% (SSC CGL 2023 PRE)                        → D
  Q10: MP=24000; scheme=18000; SP=0.9×18000=16200; discount=7800/24000=32.5%  → C
  Q11: 1-(0.85×0.80×0.76)=48.32% (DP Constable 2023)                         → B
  Q12: 1-(0.96×0.95×0.86)=21.57% (Group D 29/08/2022 Afternoon)              → C
  Q13: 1-(0.88×0.80×0.76×0.68)=63.62% (SSC Selection Post Phase-XII)         → D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_Discount_Sheet3"
SUBJECT = "Quant"
TOPIC   = "Discount"

QUESTIONS = [
    # Q8
    {
        "question_number": 8,
        "difficulty": "easy",
        "question_en": "A man gets a discount 35% and then 12% on his food bill. How much equivalent single discount does he get?",
        "question_hi": "एक व्यक्ति अपने भोजन के बिल पर 35% और फिर 12% की छूट प्राप्त करता है। इसे कितने के समतुल्य एकल छूट प्राप्त हुई?",
        "option_a": "42.8%",
        "option_b": "42.6%",
        "option_c": "41.9%",
        "option_d": "44.7%",
        "correct_answer": "A",
    },
    # Q9 — SSC CGL 2023 PRE
    {
        "question_number": 9,
        "difficulty": "easy",
        "question_en": "Three successive discounts of 25% each on the marked price of an item are together equivalent to a single discount (correct up to 2 decimal places) of: (SSC CGL 2023 PRE)",
        "question_hi": "किसी वस्तु के अंकित मूल्य पर 25% प्रत्येक की तीन क्रमिक छूट, कितनी एकल छूट (2 दशमलव स्थानों तक सही) के बराबर होगी? (SSC CGL 2023 PRE)",
        "option_a": "62.35%",
        "option_b": "60.00%",
        "option_c": "56.45%",
        "option_d": "57.81%",
        "correct_answer": "D",
    },
    # Q10
    {
        "question_number": 10,
        "difficulty": "hard",
        "question_en": "A wholesaler's MP = Rs 300/item. Buy 3 Get 1 free scheme applies, plus 10% extra discount on purchases > Rs 10,000. Ramesh's scheme-price payable = Rs 18,000. What was the effective percentage discount offered to Ramesh?",
        "question_hi": "एक थोक व्यापारी द्वारा बेची जा रही प्रत्येक वस्तु का अंकित मूल्य Rs 300 था। थोक व्यापारी एक स्टॉक-क्लीयरेंस सेल की पेशकश कर रहा था जिसमें प्रत्येक तीन वस्तुएँ खरीदने पर एक वस्तु मुफ्त दी जा रही थी। इसके अलावा, Rs 10,000 से अधिक की खरीदारी करने वाले किसी भी व्यक्ति को 3 खरीदो, 1 मुफ्त पाओ योजना के देय पर 10% की छूट दी जा रही थी। रमेश ने खरीदारी की जिसके लिए यह देय राशि Rs 18,000 थी। इस लेन-देन के दौरान रमेश को कितनी प्रभावी छूट दी गई?",
        "option_a": "32%",
        "option_b": "31.5%",
        "option_c": "32.5%",
        "option_d": "32.75%",
        "correct_answer": "C",
    },
    # Q11 — DP Constable 2023
    {
        "question_number": 11,
        "difficulty": "easy",
        "question_en": "What will be the equivalent single discount for successive discounts of 15%, 20% and 24%? (DP Constable 2023)",
        "question_hi": "15%, 20% और 24% की क्रमिक छूटों के लिए समतुल्य एकल छूट कितनी होगी? (DP Constable 2023)",
        "option_a": "46.56%",
        "option_b": "48.32%",
        "option_c": "46.52%",
        "option_d": "44.25%",
        "correct_answer": "B",
    },
    # Q12 — Group D 29/08/2022 Afternoon
    {
        "question_number": 12,
        "difficulty": "easy",
        "question_en": "Three successive discounts of 4%, 5% and 14% are equal to a single discount of ___ (round off to two decimal places). (Group D 29/08/2022 Afternoon)",
        "question_hi": "4%, 5% और 14% की तीन क्रमिक छूट ___ की एकल छूट के बराबर (दशमलव के दो स्थानों तक सही) हैं। (Group D 29/08/2022 Afternoon)",
        "option_a": "22.57%",
        "option_b": "20.57%",
        "option_c": "21.57%",
        "option_d": "23.57%",
        "correct_answer": "C",
    },
    # Q13 — SSC Selection Post Phase-XII
    {
        "question_number": 13,
        "difficulty": "medium",
        "question_en": "Find a single discount equivalent to the successive discount of 12%, 20%, 24% and 32%. (Correct to two places of decimals.) (SSC Selection Post Phase-XII)",
        "question_hi": "12%, 20%, 24% और 32% की क्रमिक छूट के बराबर एक छूट ज्ञात कीजिए। (दशमलव के दो स्थानों तक सही) (SSC Selection Post Phase-XII)",
        "option_a": "73.71%",
        "option_b": "43.41%",
        "option_c": "53.51%",
        "option_d": "63.62%",
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
        print(f"\nDone — inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
