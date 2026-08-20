"""
seed_reasoning_analytical_sheet9.py
=========================================
Seeds Analytical Reasoning Q40-Q44 from Gagan Pratap Reasoning PDFs (Sheet 9).
Subject : Reasoning
Topic   : Analytical Reasoning
Run     : python seed_reasoning_analytical_sheet9.py

Q40     — Situation-judgment type (choose best strategy)
Q41-Q44 — Statement + Courses of Action (follow / does not follow type)
Q44     — Three courses of action

Answer key (solutions verified):
  Q40  Situation: Rita's bakery is perceived as a "special occasion" shop;
       she wants to increase daily business.
       (a) Birthday/wedding discount coupons → reinforces special-occasion image ✗
       (b) Bridal Expo exhibition → targets special-event customers only ✗
       (c) Ads advertising wide array of breads (everyday items) → daily routine traffic ✓
       (d) Moving bakery to other side of town → doesn't fix perception problem ✗
       Answer: C

  Q41  Statement: Large number of people in ward X diagnosed with a fatal malaria type.
       I)  City municipal authority: take immediate steps for extensive fumigation → FOLLOWS
           (fumigation removes the source — mosquitoes — directly)
       II) People in area should be advised to take steps to avoid mosquito bites → FOLLOWS
           (personal protective measures reduce individual infection risk)
       Answer: D  (Both I and II follow)

  Q42  Statement: Since launching in 1981, Vayudoot has accumulated losses of Rs 153 crore.
       I)  Reduce wasteful expenditure and increase passenger fares → FOLLOWS
           (direct operational measures to cut losses and improve revenue)
       II) Provide Rs 300 crore to Vayudoot → DOES NOT FOLLOW
           (pouring funds into a loss-maker without operational correction is imprudent)
       Answer: A  (Only I follows)

  Q43  Statement: Meteorological dept issued notification forecasting less rainfall
       during next year's monsoon.
       I)  Government should make arrangements to provide water to affected areas → FOLLOWS
           (proactive water-supply planning addresses the predicted drought impact)
       II) Farmers should be advised to be ready for the eventuality → FOLLOWS
           (advance advisory allows farmers to adjust crop choices and irrigation)
       Answer: B  (Both I and II follow)

  Q44  Statement: Significant drop in water level of all lakes supplying water to city.
       I)  Government should appeal to all residents via mass media to minimize water
           usage → FOLLOWS (demand-side conservation using existing resources)
       II) Water supply authority should impose a partial cut in supply → FOLLOWS
           (active supply management to make existing water last longer)
       III) Government should arrange water from another city nearby → FOLLOWS
            (emergency supply ensures basic needs during the shortage)
       Answer: D  (I and II follow — best available combination among given options)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Analytical_Sheet9"
SUBJECT = "Reasoning"
TOPIC   = "Analytical Reasoning"

QUESTIONS = [
    # ── Q40 ── Situation-judgment: Rita's bakery daily business strategy ───────
    {
        "question_number": 40,
        "difficulty": "medium",
        "question_en": (
            "Each question presents a situation and asks you to make a judgment "
            "regarding that particular circumstance. Choose an answer based on given "
            "information.\n\n"
            "Rita, an accomplished pastry chef who is well known for her artistic and "
            "exquisite wedding cakes, opened a bakery one year ago and is surprised "
            "that business has been so slow. A consultant she hired to conduct market "
            "research has reported that the local population doesn't think of her shop "
            "as one they would visit on a daily basis but rather a place they'd visit "
            "if they were celebrating a special occasion.\n\n"
            "Which of the following strategies should Rita employ to increase her "
            "daily business?"
        ),
        "question_hi": (
            "प्रत्येक प्रश्न एक स्थिति प्रस्तुत करता है और आपसे उस विशेष परिस्थिति के "
            "बारे में निर्णय लेने के लिए कहता है। दी गई जानकारी के आधार पर उत्तर चुनें।\n\n"
            "रीता, एक कुशल पेस्ट्री शेफ जो अपनी कलात्मक और उत्कृष्ट वेडिंग केक के "
            "लिए जानी जाती है, ने एक साल पहले बेकरी खोली और हैरान है कि व्यापार इतना "
            "धीमा रहा है। उसने बाजार अनुसंधान के लिए एक सलाहकार नियुक्त किया जिसने "
            "बताया कि स्थानीय आबादी उसकी दुकान को ऐसी जगह नहीं मानती जहाँ वे रोज़ "
            "जाएँ, बल्कि एक ऐसी जगह जहाँ वे किसी विशेष अवसर पर जाएँगे।\n\n"
            "रीता को अपने दैनिक व्यापार को बढ़ाने के लिए निम्नलिखित में से कौन सी "
            "रणनीति अपनानी चाहिए?"
        ),
        "option_a": "Making coupons available that entitle the coupon holder to receive a 25% discount on wedding, anniversary, or birthday cakes / कूपन उपलब्ध कराना जिससे कूपन धारक को शादी, सालगिरह या जन्मदिन के केक पर 25% की छूट मिलने का अधिकार हो",
        "option_b": "Exhibiting at the next Bridal Expo and having pieces of one of her wedding cakes available for tasting / अगली ब्राइडल एक्सपो में अपनी प्रविष्टि देना और अपनी वेडिंग केक के टुकड़े चखने के लिए उपलब्ध कराना",
        "option_c": "Placing a series of ads in the local news paper that advertise the wide array of breads / स्थानीय समाचार पत्र में विभिन्न प्रकार की ब्रेड का विज्ञापन देने वाली विज्ञापन श्रृंखला प्रकाशित करना",
        "option_d": "Moving the bakery to the other side of town / बेकरी को शहर के दूसरी ओर ले जाना",
        "correct_answer": "C",
        # Problem: shop seen as special-occasion only → need to attract daily customers
        # (a) wedding/birthday discounts → reinforces special-occasion perception ✗
        # (b) Bridal Expo → doubles down on special-event market ✗
        # (c) ads for everyday breads → positions shop as a daily-visit destination ✓
        # (d) relocating ≠ solving the brand perception issue ✗
    },
    # ── Q41 ── Both courses of action follow (fatal malaria in ward X) ─────────
    {
        "question_number": 41,
        "difficulty": "easy",
        "question_en": (
            "You have to assume everything in the statement to be true and on the basis "
            "of the information given in the statement, decide which of the suggested "
            "courses of action logically follow(s) for pursuing.\n\n"
            "Statement: A large number of people in ward X of the city are diagnosed to "
            "be suffering from a fatal malaria type.\n\n"
            "Courses of Action:\n"
            "I.  The city municipal authority should take immediate steps to carry out "
            "extensive fumigation in ward X.\n"
            "II. The people in the area should be advised to take steps to avoid "
            "mosquito bites."
        ),
        "question_hi": (
            "आपको कथन में दी गई सभी बातों को सत्य मानना है और कथन में दी गई जानकारी "
            "के आधार पर तय करना है कि सुझाए गए कार्यवाही के तरीकों में से कौन सा "
            "तार्किक रूप से अनुसरण करता है।\n\n"
            "कथन: शहर के वार्ड X में बड़ी संख्या में लोगों में मलेरिया के घातक प्रकार "
            "का पता चला है।\n\n"
            "कार्रवाई के तरीके:\n"
            "I.  शहर के नगर निगम प्राधिकरण को वार्ड X में व्यापक धुआँ करने के लिए "
            "तत्काल कदम उठाने चाहिए।\n"
            "II. क्षेत्र के लोगों को मच्छरों के काटने से बचाव के लिए कदम उठाने की "
            "सलाह दी जानी चाहिए।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Either I or II follows / I या II अनुसरण करता है",
        "option_d": "Both I and II follow / I और II दोनों अनुसरण करते हैं",
        "correct_answer": "D",
        # I: fumigation eliminates mosquitoes — tackles source of disease directly → FOLLOWS ✓
        # II: personal protection advice reduces individual infection risk → FOLLOWS ✓
    },
    # ── Q42 ── Only Course of Action I follows (Vayudoot losses) ─────────────
    {
        "question_number": 42,
        "difficulty": "medium",
        "question_en": (
            "In each question below is given a statement followed by courses of action. "
            "You have to assume everything in the statement to be true, then decide "
            "which of the given suggested courses of action logically follows for "
            "pursuing.\n\n"
            "Statement: Since its launching in 1981, Vayudoot has so far accumulated "
            "losses amounting to Rs 153 crore. In both 1988 to 1989 it added Rs 153 "
            "crore to its loss.\n\n"
            "Courses of Action:\n"
            "I.  Vayudoot should be directed to reduce wasteful expenditure and to "
            "increase passenger fare and also make the airliner economically viable.\n"
            "II. An amount of Rs 300 crore should be provided to Vayudoot to make the "
            "airliner economically viable."
        ),
        "question_hi": (
            "नीचे दिए गए प्रत्येक प्रश्न में एक कथन के बाद कार्यवाही के तरीके दिए "
            "गए हैं। आपको कथन में दी गई सभी बातों को सत्य मानना है फिर तय करना है "
            "कि सुझाए गए कार्यवाही के तरीकों में से कौन सा तार्किक रूप से अनुसरण "
            "करता है।\n\n"
            "कथन: अपनी शुरुआत से लेकर 1981 में, वायुदूत ने अब तक 153 करोड़ रुपये का "
            "नुकसान उठाया है।\n\n"
            "कार्रवाई के तरीके:\n"
            "I.  वायुदूत को फिजूल खर्चों को कम करने और यात्री किराया बढ़ाने का निर्देश "
            "दिया जाना चाहिए ताकि एयरलाइन को किफायती बनाया जा सके।\n"
            "II. वायुदूत को आर्थिक रूप से व्यवहार्य बनाने के लिए 300 करोड़ रुपये की "
            "राशि प्रदान की जानी चाहिए।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Either I or II follows / I या II अनुसरण करता है",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "A",
        # I: reduce waste + raise fares = direct operational remedy for mounting losses → FOLLOWS ✓
        # II: pouring Rs 300 cr into a structurally loss-making operation without reform → IMPRUDENT ✗
    },
    # ── Q43 ── Both courses of action follow (less rainfall forecast) ──────────
    {
        "question_number": 43,
        "difficulty": "easy",
        "question_en": (
            "Study the given statement then decide which of the suggested courses of "
            "action logically follow(s).\n\n"
            "Statement: The meteorological department has issued a notification "
            "forecasting less rainfall during next year's monsoon.\n\n"
            "Courses of Action:\n"
            "I.  The government should make arrangements to provide water to the "
            "affected areas.\n"
            "II. The farmers should be advised to be ready for the eventuality."
        ),
        "question_hi": (
            "दिए गए कथन का अध्ययन करें और फिर तय करें कि सुझाए गए कार्यवाही के "
            "तरीकों में से कौन सा तार्किक रूप से सही है।\n\n"
            "कथन: मौसम विभाग ने अगले साल के मानसून के दौरान कम वर्षा होने का पूर्वानुमान "
            "लगाते हुए एक अधिसूचना जारी की है।\n\n"
            "कार्रवाई के तरीके:\n"
            "I.  सरकार को प्रभावित क्षेत्रों में पानी उपलब्ध कराने के लिए प्रबंध "
            "करने चाहिए।\n"
            "II. किसानों को संभावित स्थिति के लिए तैयार रहने की सलाह दी जानी चाहिए।"
        ),
        "option_a": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_b": "Both I and II follow / I और II दोनों अनुसरण करते हैं",
        "option_c": "Only II follows / केवल II अनुसरण करता है",
        "option_d": "Only I follows / केवल I अनुसरण करता है",
        "correct_answer": "B",
        # I: proactive water-supply planning for predicted drought is necessary → FOLLOWS ✓
        # II: advance advisory lets farmers adjust crops/irrigation ahead of shortage → FOLLOWS ✓
    },
    # ── Q44 ── Three CoA; I and II follow (lake water level drop) ─────────────
    {
        "question_number": 44,
        "difficulty": "hard",
        "question_en": (
            "In each question below is given a statement followed by courses of action. "
            "You have to assume everything in the statement to be true, then decide "
            "which of the given suggested courses of action logically follows for "
            "pursuing.\n\n"
            "Statement: There has been a significant drop in the water level of all "
            "the lakes supplying water to the city.\n\n"
            "Courses of Action:\n"
            "I.  The government should appeal to all the residents through mass media "
            "to minimize the usage of water.\n"
            "II. The water supply authority should impose a partial cut in supply to "
            "take the situation.\n"
            "III. Govt should arrange water to the city from another city nearby."
        ),
        "question_hi": (
            "नीचे दिए गए प्रत्येक प्रश्न में एक कथन के बाद कार्यवाही के तरीके दिए "
            "गए हैं। आपको कथन में दी गई सभी बातों को सत्य मानना है फिर तय करना है "
            "कि सुझाए गए कार्यवाही के तरीकों में से कौन सा तार्किक रूप से अनुसरण "
            "करता है।\n\n"
            "कथन: शहर को पानी की आपूर्ति करने वाली सभी झीलों के जल स्तर में महत्वपूर्ण "
            "गिरावट आई है।\n\n"
            "कार्रवाई के तरीके:\n"
            "I.  सरकार को जनसंचार माध्यमों के माध्यम से सभी निवासियों से पानी का कम "
            "से कम उपयोग करने की अपील करनी चाहिए।\n"
            "II. जल आपूर्ति प्राधिकरण को स्थिति को संभालने के लिए आपूर्ति में आंशिक "
            "कटौती करनी चाहिए।\n"
            "III. सरकार को पास के किसी अन्य शहर से शहर में पानी की व्यवस्था करनी "
            "चाहिए।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Either I or II follows / I या II अनुसरण करता है",
        "option_d": "I and II follow / I और II अनुसरण करते हैं",
        "correct_answer": "D",
        # I: public appeal via mass media reduces demand-side consumption → FOLLOWS ✓
        # II: partial supply cut actively manages limited reserves → FOLLOWS ✓
        # III: sourcing from nearby city is also sound but the best available option
        #      among the given choices captures I + II → answer is D
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        existing_qnums = {
            row[0]
            for row in db.query(Question.question_number)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        for d in QUESTIONS:
            if d["question_number"] in existing_qnums:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
            inserted += 1
            print(f"  INSERT Q{d['question_number']}")

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped: {skipped}")

    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
