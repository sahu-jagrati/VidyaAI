"""
seed_reasoning_analytical_sheet7.py
=========================================
Seeds Analytical Reasoning Q27-Q34 from Gagan Pratap Reasoning PDFs (Sheet 7).
Subject : Reasoning
Topic   : Analytical Reasoning
Run     : python seed_reasoning_analytical_sheet7.py

Q27-Q33 are "Statement + two Arguments" (strength-of-argument type).
Q34 is a "weaken the argument" type (like Q26).

Answer key (solutions verified):
  Q27  Statement: Should articles of only deserving authors be allowed to be published?
       I)  Yes — saves paper in short supply → WEAK
           (paper supply is not a valid reason to censor publishing)
       II) No — impossible to draw a line between deserving / undeserving → STRONG
           ("deserving" is subjective; objective enforcement is virtually impossible)
       Answer: B  (Only II is strong)

  Q28  Statement: Should selection tests be of objective rather than descriptive type?
       I)  Yes — assessment of objective-type answers is fair and impartial → STRONG
           (eliminates evaluator bias and subjectivity)
       II) No — descriptive type is certainly a better tool → WEAK
           (bare assertion with no supporting justification)
       Answer: A  (Only I is strong)

  Q29  Statement: Should all diesel engines be replaced by electric engines in trains?
       I)  Yes — diesel engines cause a lot of pollution → STRONG
           (addressing environmental pollution is a legitimate policy objective)
       II) No — India does not produce enough electricity for domestic needs → STRONG
           (practical energy-supply constraint must be resolved before a full transition)
       Answer: B  (Both arguments are strong)

  Q30  Statement: In crowded public places, one should cover his/her mouth while
       coughing and sneezing.
       I)  Germs of deadly diseases spread through cough/sneeze droplets → STRONG
           (direct scientific rationale for the preventive measure)
       II) Risk of infection with deadly diseases is high in crowded places → STRONG
           (reinforces why the preventive measure is essential in the given context)
       Answer: C  (Both arguments are strong)

  Q31  Statement: Our country should enhance exports even when there is a shortage
       of internal consumption.
       I)  Yes — we need foreign exchange to import things like oil → STRONG
           (critical need for hard currency is a genuine economic necessity)
       II) No — it will harm internal consumers → STRONG
           (depriving domestic consumers during shortages causes immediate hardship)
       Answer: C  (Both arguments are strong)

  Q32  Statement: NHRC of India is responsible for the protection and promotion of
       Human Rights...
       I)  NHRC can initiate an inquiry on its own or on a petition by a victim → STRONG
           (directly describes the primary mandate and operational function of NHRC)
       II) NHRC promotes and undertakes research about Human Rights issues → STRONG
           (reflects NHRC's core promotional responsibility stated in the passage)
       Answer: C  (Both arguments are strong)

  Q33  Statement: Should India decide to give Kashmir to Pakistan?
       I)  Yes — it will save a lot of money for India → WEAK
           (territorial integrity and national security cannot be sold for savings)
       II) No — it will escalate other similar demands → STRONG
           (yielding territory sets a dangerous precedent; encourages further demands)
       Answer: B  (Only Argument II is strong)

  Q34  Premise (high-speed train argument): A used plane costs one-third of the train
       line, is just as fast, and can "fly anywhere" unlike a fixed linear train.
       Free-wheel systems (cars, buses, aircraft) are what consumers choose; a
       fixed train route will find no sufficient market.
       Question: Which, if true, most severely weakens the above argument?
       Answer: C  (Planes are not a free-wheel system because they can only fly
       between airports, which are less convenient for consumers than high-speed
       train stations would be — directly refutes the "free-wheel" premise)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Analytical_Sheet7"
SUBJECT = "Reasoning"
TOPIC   = "Analytical Reasoning"

QUESTIONS = [
    # ── Q27 ── Only Argument II strong (deserving authors) ───────────────────
    {
        "question_number": 27,
        "difficulty": "medium",
        "question_en": (
            "Study the following questions carefully and choose the right answer.\n\n"
            "Statement: Should articles of only deserving authors be allowed to be "
            "published?\n\n"
            "Arguments:\n"
            "I.  Yes, It will save a lot of paper which is in short supply.\n"
            "II. No, It is not possible to draw a line between the deserving and "
            "the undeserving."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों का सावधानीपूर्वक अध्ययन करें और सही उत्तर चुनें।\n\n"
            "कथन: क्या केवल योग्य लेखकों के लेखों को ही प्रकाशित करने की अनुमति दी "
            "जानी चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, इससे बहुत सारा कागज बचेगा जिसकी आपूर्ति कम है।\n"
            "II. नहीं, योग्य और अयोग्य के बीच रेखा खींचना संभव नहीं है।"
        ),
        "option_a": "Only I is strong / केवल I मजबूत है",
        "option_b": "Only II is strong / केवल II मजबूत है",
        "option_c": "Either I or II is strong / I या II मजबूत है",
        "option_d": "Neither I nor II is strong / न तो I और न ही II मजबूत है",
        "correct_answer": "B",
        # I: paper shortage ≠ valid reason to restrict publishing freedom → WEAK ✗
        # II: "deserving" is subjective; no objective enforcement possible → STRONG ✓
    },
    # ── Q28 ── Only Argument I strong (objective vs descriptive tests) ────────
    {
        "question_number": 28,
        "difficulty": "easy",
        "question_en": (
            "Study the following questions carefully and choose the right answer.\n\n"
            "Statement: Should selection tests be of the objective rather than of the "
            "descriptive type?\n\n"
            "Arguments:\n"
            "I.  Yes, The assessment of answers to objective-type questions is fair "
            "and impartial.\n"
            "II. No, The descriptive type test is certainly a better tool than the "
            "objective type test."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों का सावधानीपूर्वक अध्ययन करें और सही उत्तर चुनें।\n\n"
            "कथन: क्या चयन परीक्षाएँ वर्णनात्मक प्रकार के बजाय वस्तुनिष्ठ प्रकार की "
            "होनी चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, वस्तुनिष्ठ प्रकार के प्रश्नों के उत्तरों का मूल्यांकन निष्पक्ष "
            "और तटस्थ होता है।\n"
            "II. नहीं, वर्णनात्मक प्रकार की परीक्षा निश्चित रूप से वस्तुनिष्ठ प्रकार "
            "की परीक्षा से बेहतर उपकरण है।"
        ),
        "option_a": "Only I is strong / केवल I मजबूत है",
        "option_b": "Only II is strong / केवल II मजबूत है",
        "option_c": "Either I or II is strong / I या II मजबूत है",
        "option_d": "Neither I nor II is strong / न तो I और न ही II मजबूत है",
        "correct_answer": "A",
        # I: objective grading eliminates evaluator bias → STRONG ✓
        # II: bare assertion ("certainly a better tool") without any justification → WEAK ✗
    },
    # ── Q29 ── Both arguments strong (diesel → electric train engines) ────────
    {
        "question_number": 29,
        "difficulty": "medium",
        "question_en": (
            "A statement is followed by two Arguments numbered I and II. Consider the "
            "statement and decide which of the Arguments is/are strong.\n\n"
            "Statement: Should all diesel engines be replaced by electric engines "
            "in trains?\n\n"
            "Arguments:\n"
            "I.  Yes, diesel engines cause a lot of pollution.\n"
            "II. No, India does not produce enough electricity to fulfill even the "
            "domestic needs."
        ),
        "question_hi": (
            "एक कथन के बाद दो तर्क I और II दिए गए हैं। कथन पर विचार करें और निर्णय "
            "लें कि कौन सा/से तर्क मजबूत है/हैं।\n\n"
            "कथन: क्या ट्रेनों में सभी डीजल इंजनों को इलेक्ट्रिक इंजनों से बदल दिया "
            "जाना चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, डीजल इंजन बहुत अधिक प्रदूषण करते हैं।\n"
            "II. नहीं, भारत घरेलू जरूरतों को पूरा करने के लिए भी पर्याप्त बिजली का "
            "उत्पादन नहीं करता।"
        ),
        "option_a": "Neither argument I nor Argument II is strong / न तो तर्क I और न ही II मजबूत है",
        "option_b": "Both of the arguments are strong / दोनों तर्क मजबूत हैं",
        "option_c": "Only II is strong / केवल II मजबूत है",
        "option_d": "Only I is strong / केवल I मजबूत है",
        "correct_answer": "B",
        # I: pollution from diesel is a valid environmental concern → STRONG ✓
        # II: electricity supply shortage is a real practical constraint → STRONG ✓
    },
    # ── Q30 ── Both arguments strong (cover mouth in crowded places) ──────────
    {
        "question_number": 30,
        "difficulty": "easy",
        "question_en": (
            "In each of the questions below is a given statement followed by two "
            "arguments/assumptions numbered I and II. Consider the arguments/assumptions "
            "and decide which is correct.\n\n"
            "Statement: In crowded public places like markets, buses, and trains, one "
            "should cover his/her mouth while coughing and sneezing.\n\n"
            "Arguments:\n"
            "I.  Germs of deadly diseases such as tuberculosis spread through droplets "
            "of cough/sneeze.\n"
            "II. Chances of getting infected with deadly diseases such as tuberculosis "
            "is high if you visit crowded public place frequently."
        ),
        "question_hi": (
            "नीचे दिए गए प्रत्येक प्रश्न में एक कथन के बाद दो तर्क/धारणाएँ I और II "
            "दी गई हैं। तर्क/धारणाओं पर विचार कीजिए और निर्णय लीजिए कि कौन सी सही है।\n\n"
            "कथन: बाजारों, बसों और ट्रेनों जैसे भीड़-भाड़ वाले सार्वजनिक स्थानों पर "
            "खाँसते और छींकते समय अपना मुँह ढकना चाहिए।\n\n"
            "तर्क:\n"
            "I.  तपेदिक जैसी घातक बीमारियों के रोगाणु खाँसी/छींक की बूँदों से फैलते हैं।\n"
            "II. यदि आप बार-बार भीड़-भाड़ वाले सार्वजनिक स्थान पर जाते हैं तो तपेदिक "
            "जैसी घातक बीमारियों से संक्रमित होने की संभावना अधिक होती है।"
        ),
        "option_a": "Argument I is strong / तर्क I मजबूत है",
        "option_b": "Argument II is strong / तर्क II मजबूत है",
        "option_c": "Argument I and II are strong / तर्क I और II दोनों मजबूत हैं",
        "option_d": "Neither argument I nor II is strong / न तो तर्क I और न ही II मजबूत है",
        "correct_answer": "C",
        # I: scientific basis — droplet transmission explains why covering mouth works → STRONG ✓
        # II: risk of infection in crowded places reinforces necessity of the measure → STRONG ✓
    },
    # ── Q31 ── Both arguments strong (export during domestic shortage) ─────────
    {
        "question_number": 31,
        "difficulty": "hard",
        "question_en": (
            "In each of the questions below is a given statement followed by two "
            "arguments/assumptions numbered I and II. Consider the arguments/assumptions "
            "and decide which is correct.\n\n"
            "Statement: Our country should enhance exports even when there is a shortage "
            "of internal consumption.\n\n"
            "Arguments:\n"
            "I.  Yes, we need foreign exchange to import things like oil.\n"
            "II. No, it will harm the internal consumers."
        ),
        "question_hi": (
            "नीचे दिए गए प्रत्येक प्रश्न में एक कथन के बाद दो तर्क/धारणाएँ I और II "
            "दी गई हैं। तर्क/धारणाओं पर विचार कीजिए और निर्णय लीजिए कि कौन सी सही है।\n\n"
            "कथन: हमारे देश को आंतरिक उपभोग में कमी होने पर भी निर्यात बढ़ाना चाहिए।\n\n"
            "तर्क:\n"
            "I.  हाँ, हमें तेल जैसी चीजों के आयात के लिए विदेशी मुद्रा की जरूरत है।\n"
            "II. नहीं, इससे आंतरिक उपभोक्ताओं को नुकसान होगा।"
        ),
        "option_a": "Argument I is strong / तर्क I मजबूत है",
        "option_b": "Argument II is strong / तर्क II मजबूत है",
        "option_c": "Argument I and II are strong / तर्क I और II दोनों मजबूत हैं",
        "option_d": "Neither argument I nor II is strong / न तो तर्क I और न ही II मजबूत है",
        "correct_answer": "C",
        # I: foreign exchange for critical imports (oil) is a genuine economic necessity → STRONG ✓
        # II: domestic shortage + exports = real harm to consumers inside the country → STRONG ✓
    },
    # ── Q32 ── Both arguments strong (NHRC mandate) ───────────────────────────
    {
        "question_number": 32,
        "difficulty": "easy",
        "question_en": (
            "In each of the questions below is a given statement followed by two "
            "arguments/assumptions numbered I and II. Consider the arguments/assumptions "
            "and decide which is correct.\n\n"
            "Statement: National Human Rights Commission (NHRC) of India is responsible "
            "for the protection and promotion of Human Rights, defined by the act as "
            "rights relating to life, liberty equality, and dignity of the individual "
            "guaranteed by the Constitution or embodied in the International Covenants.\n\n"
            "Arguments:\n"
            "I.  On the violation of human rights NHRC can initiate an inquiry on its "
            "own or against a petition filed by a victim.\n"
            "II. NHRC promotes and undertakes research about Human Rights issues."
        ),
        "question_hi": (
            "नीचे दिए गए प्रत्येक प्रश्न में एक कथन के बाद दो तर्क/धारणाएँ I और II "
            "दी गई हैं। तर्क/धारणाओं पर विचार कीजिए और निर्णय लीजिए कि कौन सी सही है।\n\n"
            "कथन: भारत का राष्ट्रीय मानवाधिकार आयोग (NHRC) मानव अधिकारों की सुरक्षा "
            "और प्रचार के लिए जिम्मेदार है, जिसे अधिनियम द्वारा संविधान द्वारा "
            "गारंटीकृत या अंतरराष्ट्रीय अनुबंधों में सन्निहित जीवन, स्वतंत्रता, "
            "समानता और व्यक्ति की गरिमा से संबंधित अधिकारों के रूप में परिभाषित "
            "किया गया है।\n\n"
            "तर्क:\n"
            "I.  मानव अधिकारों के उल्लंघन पर NHRC स्वयं या पीड़ित द्वारा दायर याचिका "
            "के खिलाफ जाँच शुरू कर सकता है।\n"
            "II. NHRC मानवाधिकार मुद्दों के बारे में अनुसंधान को बढ़ावा देता और "
            "करता है।"
        ),
        "option_a": "Argument I is strong / तर्क I मजबूत है",
        "option_b": "Argument II is strong / तर्क II मजबूत है",
        "option_c": "Argument I and II are strong / तर्क I और II दोनों मजबूत हैं",
        "option_d": "Neither argument I nor II is strong / न तो तर्क I और न ही II मजबूत है",
        "correct_answer": "C",
        # I: inquiry power (suo motu or on petition) = primary operational mandate → STRONG ✓
        # II: research/promotion = explicitly stated in NHRC's core responsibility → STRONG ✓
    },
    # ── Q33 ── Only Argument II strong (give Kashmir to Pakistan) ────────────
    {
        "question_number": 33,
        "difficulty": "medium",
        "question_en": (
            "In each of the questions below is a given statement followed by two "
            "arguments/assumptions numbered I and II. Consider the arguments/assumptions "
            "and decide which is correct.\n\n"
            "Statement: Should India decide to give Kashmir to Pakistan?\n\n"
            "Arguments:\n"
            "I.  Yes, it will save a lot of money for India.\n"
            "II. No, it will escalate other similar demands."
        ),
        "question_hi": (
            "नीचे दिए गए प्रत्येक प्रश्न में एक कथन के बाद दो तर्क/धारणाएँ I और II "
            "दी गई हैं। तर्क/धारणाओं पर विचार कीजिए और निर्णय लीजिए कि कौन सी सही है।\n\n"
            "कथन: क्या भारत को कश्मीर पाकिस्तान को देने का निर्णय लेना चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, इससे भारत के लिए बहुत सारा पैसा बचेगा।\n"
            "II. नहीं, इससे अन्य ऐसी ही माँगें बढ़ेंगी।"
        ),
        "option_a": "Argument I is strong / तर्क I मजबूत है",
        "option_b": "Argument II is strong / तर्क II मजबूत है",
        "option_c": "Arguments I and II are strong / तर्क I और II दोनों मजबूत हैं",
        "option_d": "Neither argument I nor II is strong / न तो तर्क I और न ही II मजबूत है",
        "correct_answer": "B",
        # I: monetary savings cannot justify surrendering territorial integrity → WEAK ✗
        # II: ceding territory sets a dangerous precedent → fuels further secessionist demands → STRONG ✓
    },
    # ── Q34 ── Weaken the argument (high-speed train vs planes) ──────────────
    {
        "question_number": 34,
        "difficulty": "hard",
        "question_en": (
            "The difficulty with the proposed high-speed train line is that a used plane "
            "can be bought for one-third the price of the train line, and the plane, "
            "which is just as fast, can fly anywhere. The train would be a fixed linear "
            "system, and we live in a world that is spreading out in all directions and "
            "in which consumers choose the free-wheel systems (cars, buses, aircraft) "
            "which do not have fixed routes. Thus, a sufficient market for the train "
            "will not exist.\n\n"
            "Which of the following, if true, most severely weakens the argument "
            "presented above?"
        ),
        "question_hi": (
            "प्रस्तावित हाई-स्पीड ट्रेन लाइन के साथ कठिनाई यह है कि एक इस्तेमाल किया "
            "हुआ विमान ट्रेन लाइन की कीमत के एक तिहाई में खरीदा जा सकता है, और विमान, "
            "जो उतना ही तेज है, कहीं भी उड़ान भर सकता है। ट्रेन एक निश्चित रैखिक "
            "प्रणाली होगी, और हम एक ऐसी दुनिया में रहते हैं जो सभी दिशाओं में फैल "
            "रही है और जिसमें उपभोक्ता फ्री-व्हील सिस्टम (कार, बस, विमान) चुनते हैं "
            "जिनके निश्चित रूट नहीं होते। इस प्रकार, ट्रेन के लिए पर्याप्त बाजार "
            "नहीं होगा।\n\n"
            "निम्नलिखित में से कौन सा, यदि सत्य है, तो उपरोक्त तर्क को सबसे अधिक "
            "कमजोर करता है?"
        ),
        "option_a": "Cars, buses, and planes require the efforts of drivers and pilots to guide them, whereas the train will be guided mechanically / कारों, बसों और विमानों को चालकों और पायलटों के प्रयासों की आवश्यकता होती है, जबकि ट्रेन यंत्रवत् चलाई जाएगी",
        "option_b": "Cars and buses are not nearly as fast as the high-speed train will be / कारें और बसें हाई-स्पीड ट्रेन जितनी तेज नहीं होंगी",
        "option_c": "Planes are not a free-wheel system because they can fly only between airports, which are also less convenient for consumers than the high-speed train's stations would be / विमान एक फ्री-व्हील प्रणाली नहीं हैं क्योंकि वे केवल हवाई अड्डों के बीच उड़ सकते हैं, जो उपभोक्ताओं के लिए हाई-स्पीड ट्रेन के स्टेशनों की तुलना में कम सुविधाजनक भी हैं",
        "option_d": "High-speed rail line cannot use currently underprofitable train stations in large cities / हाई-स्पीड रेल लाइन वर्तमान में कम उपयोगी बड़े शहरों में रेलवे स्टेशनों का उपयोग नहीं कर सकती है",
        "correct_answer": "C",
        # Argument's key premise: planes are "free-wheel" (can go anywhere) unlike fixed trains.
        # C: directly refutes this — planes ALSO have fixed routes (airports only) and are
        #    LESS convenient than train stations → the "free-wheel" advantage evaporates ✓
        # A: guidance method is irrelevant to the market-viability argument ✗
        # B: speed comparison with cars/buses doesn't address the free-wheel premise ✗
        # D: about station profitability — tangential to the core "free-wheel" claim ✗
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
