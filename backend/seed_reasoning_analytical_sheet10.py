"""
seed_reasoning_analytical_sheet10.py
=========================================
Seeds Analytical Reasoning Q45-Q50 from Gagan Pratap Reasoning PDFs (Sheet 10).
Subject : Reasoning
Topic   : Analytical Reasoning
Run     : python seed_reasoning_analytical_sheet10.py

NOTE:
  Q46 shares its statement with Q39 (imported fruits); different practice set.
  Q47 shares its statement with Q36 (Municipal Corporation strike); different practice set.
  Q49-Q50 are situation/scenario type (workplace judgment questions).

Answer key (solutions verified):
  Q45  Statement: Cinema halls incurring heavy losses; people prefer TV at home.
       I)  Demolish cinema halls and construct residential buildings → DOES NOT FOLLOW
           (demolition is an extreme, irreversible action not proportional to the problem)
       II) Convert cinema halls into shopping malls → DOES NOT FOLLOW
           (irrelevant / extreme; does not address the actual problem of declining viewership)
       Answer: D  (Neither I nor II follows)

  Q46  Statement: Availability of imported fruits increased; demand for indigenous
       fruits decreased. (Same statement as Q39 — different practice set)
       I)  Impose heavy import duty even if fruits are not of good quality → DOES NOT FOLLOW
           (protecting poor-quality goods at consumers' expense is unjustifiable)
       II) Fruit vendors should stop selling imported fruits → DOES NOT FOLLOW
           (forcibly restricting legal trade is an improper administrative action)
       Answer: D  (Neither I nor II follows)

  Q47  Statement: Municipal Corporation employees' union decided indefinite strike
       over management's refusal to grant bonus. (Same as Q36 — different practice set)
       I)  Government should immediately pay ex-gratia grant for bonus → DOES NOT FOLLOW
           (financial concession without negotiation sets a bad precedent)
       II) Striking employees should be persuaded to defer the strike notice → FOLLOWS
           (dialogue and persuasion are the appropriate administrative response)
       Answer: B  (Only II follows)

  Q48  Statement: If retired Professors of same Institutes are invited to deliberate
       on restructuring, their contribution may be beneficial to the Institute.
       I)  Management may seek opinion of employees before calling retired professors
           → DOES NOT FOLLOW (employees' permission is not a stated prerequisite)
       II) Management should involve experienced people for systematic restructuring
           → FOLLOWS (directly aligns with using expert/retired experience)
       Answer: B  (Only II follows)

  Q49  Scenario: Your sub-ordinate has done good work on her own, worthy of
       publication in a prestigious journal. What do you do?
       Answer: D  (Encourage the sub-ordinate to publish the paper on her own)
       Reasoning: The work is hers; the ethical action is to support her independent
       publication without appropriating credit.

  Q50  Scenario: You are asked to prepare a report but do not have time. What do you do?
       Answer: C  (Explain to your superior that you will take help of your sub-ordinate
       and submit the report with both your name and the sub-ordinate's name)
       Reasoning: Transparent delegation with shared credit is the ethical and
       professional approach; neither stealing credit nor refusing outright is acceptable.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Analytical_Sheet10"
SUBJECT = "Reasoning"
TOPIC   = "Analytical Reasoning"

QUESTIONS = [
    # ── Q45 ── Neither CoA follows (cinema halls and TV preference) ───────────
    {
        "question_number": 45,
        "difficulty": "easy",
        "question_en": (
            "Study the following questions carefully and choose the right answer.\n\n"
            "Statement: The cinema halls are incurring heavy losses these days as "
            "people prefer to watch movies in home on TV than to visit cinema halls.\n\n"
            "Courses of Action:\n"
            "I.  The cinema halls should be demolished and residential multi-story "
            "buildings should be constructed there.\n"
            "II. The cinema halls should be converted into shopping malls."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों का सावधानीपूर्वक अध्ययन करें और सही उत्तर चुनें।\n\n"
            "कथन: आजकल सिनेमा हॉल भारी नुकसान में चल रहे हैं क्योंकि लोग सिनेमा हॉल "
            "में जाने की बजाय घर पर टीवी पर फिल्में देखना पसंद करते हैं।\n\n"
            "कार्रवाई के तरीके:\n"
            "I.  सिनेमा हॉल को ध्वस्त कर दिया जाना चाहिए और वहाँ आवासीय बहुमंजिला "
            "इमारतों का निर्माण किया जाना चाहिए।\n"
            "II. सिनेमा हॉल को शॉपिंग मॉल में बदल दिया जाना चाहिए।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Either I or II follows / I या II अनुसरण करता है",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "D",
        # I: demolition is an extreme, irreversible response not warranted by declining viewership → ✗
        # II: converting to shopping malls doesn't address the root cause of cinema's losses → ✗
    },
    # ── Q46 ── Neither CoA follows (imported fruits; same statement as Q39) ───
    {
        "question_number": 46,
        "difficulty": "medium",
        "question_en": (
            "Study the following questions carefully and choose the right answer.\n\n"
            "Statement: The availability of imported fruits has increased in the "
            "indigenous market and so the demand for indigenous fruits has been "
            "decreased.\n\n"
            "Courses of Action:\n"
            "I.  To help the indigenous producers of fruits, the Government should "
            "impose high import duty on these fruits, even if these are not of good "
            "quality.\n"
            "II. The fruit vendors should stop selling imported fruits so that the "
            "demand for indigenous fruits would be increased."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों का सावधानीपूर्वक अध्ययन करें और सही उत्तर चुनें।\n\n"
            "कथन: स्थानीय बाजार में आयातित फलों की उपलब्धता बढ़ गई है और इसलिए "
            "स्वदेशी फलों की माँग कम हो गई है।\n\n"
            "कार्रवाई के तरीके:\n"
            "I.  स्वदेशी फल उत्पादकों की मदद के लिए सरकार को इन फलों पर भारी "
            "आयात शुल्क लगाना चाहिए, भले ही ये अच्छी गुणवत्ता के न हों।\n"
            "II. फल विक्रेताओं को आयातित फलों की बिक्री बंद कर देनी चाहिए ताकि "
            "स्वदेशी फलों की माँग बढ़े।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Either I or II follows / I या II अनुसरण करता है",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "D",
        # I: taxing poor-quality imports forces consumers to accept inferior goods → ✗
        # II: forcibly banning legal trade is an improper administrative action → ✗
    },
    # ── Q47 ── Only CoA II follows (Municipal Corp strike; same as Q36) ───────
    {
        "question_number": 47,
        "difficulty": "easy",
        "question_en": (
            "Study the following questions carefully and choose the right answer.\n\n"
            "Statement: The employees union of the Municipal Corporation has decided "
            "to strike work for an indefinite period in protest against the "
            "management's refusal to grant bonus.\n\n"
            "Courses of Action:\n"
            "I.  The government should immediately pay ex-gratia grant to the "
            "Municipal Corporation to grant bonus to its employees.\n"
            "II. The striking employees should be persuaded to defer the strike notice."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों का सावधानीपूर्वक अध्ययन करें और सही उत्तर चुनें।\n\n"
            "कथन: नगर निगम के कर्मचारियों की यूनियन ने बोनस देने से प्रबंधन के इनकार "
            "के विरोध में अनिश्चित काल के लिए हड़ताल करने का फैसला किया है।\n\n"
            "कार्रवाई के तरीके:\n"
            "I.  सरकार को अपने कर्मचारियों को बोनस देने के लिए तुरंत नगर निगम को "
            "अनुग्रह अनुदान देना चाहिए।\n"
            "II. हड़ताली कर्मचारियों को हड़ताल नोटिस स्थगित करने के लिए राजी किया "
            "जाना चाहिए।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Either I or II follows / I या II अनुसरण करता है",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "B",
        # I: paying immediately under pressure sets bad precedent and bypasses negotiation → ✗
        # II: persuading workers to defer keeps dialogue open — proper administrative response → ✓
    },
    # ── Q48 ── Only CoA II follows (retired professors and restructuring) ──────
    {
        "question_number": 48,
        "difficulty": "medium",
        "question_en": (
            "Study the following questions carefully and choose the right answer.\n\n"
            "Statement: If the retired Professors of the same Institutes are also "
            "invited to deliberate on the restructuring of the organization, their "
            "contribution may be beneficial to the Institute.\n\n"
            "Courses of Action:\n"
            "I.  Management may seek the opinion of the employees before calling "
            "retired professors.\n"
            "II. Management should involve experienced people for the systematic "
            "restructuring of the organization."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों का सावधानीपूर्वक अध्ययन करें और सही उत्तर चुनें।\n\n"
            "कथन: यदि उसी संस्थान के सेवानिवृत्त प्रोफेसरों को भी संगठन के पुनर्गठन "
            "पर विचार-विमर्श करने के लिए आमंत्रित किया जाता है, तो उनका योगदान "
            "संस्थान के लिए लाभकारी हो सकता है।\n\n"
            "कार्रवाई के तरीके:\n"
            "I.  प्रबंधन सेवानिवृत्त प्रोफेसरों को बुलाने से पहले कर्मचारियों की "
            "राय ले सकता है।\n"
            "II. प्रबंधन को संगठन के व्यवस्थित पुनर्गठन के लिए अनुभवी लोगों को "
            "शामिल करना चाहिए।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Either I or II follows / I या II अनुसरण करता है",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "B",
        # I: employees' permission/opinion is not a stated prerequisite → irrelevant → ✗
        # II: involving experienced people directly follows from the statement's logic → ✓
    },
    # ── Q49 ── Workplace scenario: sub-ordinate's publishable research ────────
    {
        "question_number": 49,
        "difficulty": "easy",
        "question_en": (
            "You are working in a research lab. One of your sub-ordinates has done "
            "some good work on her own and the work is worthy of publication in a "
            "prestigious journal. What do you do?"
        ),
        "question_hi": (
            "आप एक शोध प्रयोगशाला में काम कर रहे हैं। आपके किसी अधीनस्थ ने अपने दम "
            "पर अच्छा काम किया है और वह काम एक प्रतिष्ठित पत्रिका में प्रकाशन के "
            "योग्य है। आप क्या करते हैं?"
        ),
        "option_a": "Take all the data and publish it in your name / सारा डेटा ले लें और इसे अपने नाम से प्रकाशित करें",
        "option_b": "Ask the sub-ordinate to add your name as one of the authors / अधीनस्थ से लेखकों में से एक के रूप में अपना नाम जोड़ने के लिए कहें",
        "option_c": "Tell your sub-ordinate that unless you are made co-author you will not allow her to publish the paper / अपने अधीनस्थ को बताएं कि जब तक आपको सह-लेखक नहीं बनाया जाता, आप उसे पेपर प्रकाशित करने की अनुमति नहीं देंगे",
        "option_d": "Encourage the sub-ordinate to publish the paper on her own / अधीनस्थ को पेपर स्वयं प्रकाशित करने के लिए प्रोत्साहित करें",
        "correct_answer": "D",
        # The work is solely hers; the ethical action is to support her independent
        # publication without appropriating any credit → D is the only ethical choice ✓
        # (a)(b)(c) all involve claiming unearned credit or coercion → ✗
    },
    # ── Q50 ── Workplace scenario: report due, no time ────────────────────────
    {
        "question_number": 50,
        "difficulty": "easy",
        "question_en": (
            "You are asked to prepare a report on some issue. You do not have the "
            "time to prepare the report. What do you do?"
        ),
        "question_hi": (
            "आपको किसी मुद्दे पर एक रिपोर्ट तैयार करने के लिए कहा जाता है। आपके "
            "पास रिपोर्ट तैयार करने का समय नहीं है। आप क्या करते हैं?"
        ),
        "option_a": "Ask the sub-ordinate to prepare the report, put your name, and submit it / अधीनस्थ को रिपोर्ट तैयार करने, उस पर अपना नाम डालने और जमा करने के लिए कहें",
        "option_b": "Refuse to prepare the report / रिपोर्ट तैयार करने से इनकार करें",
        "option_c": "Explain to your superior that you will take the help of your sub-ordinate and submit the report with your name as well as that of your sub-ordinate / अपने वरिष्ठ को बताएं कि आप अधीनस्थ की मदद लेंगे और रिपोर्ट अपने नाम के साथ-साथ अधीनस्थ के नाम से भी जमा करेंगे",
        "option_d": "Prepare a report by putting together some material even if they are irrelevant / कुछ सामग्रियों को एक साथ रखकर रिपोर्ट तैयार करें भले ही वे अप्रासंगिक हों",
        "correct_answer": "C",
        # (a): taking sub-ordinate's work under your name alone is unethical → ✗
        # (b): simply refusing is irresponsible → ✗
        # (c): transparent delegation + shared credit = ethical and professional → ✓
        # (d): submitting irrelevant material is dishonest → ✗
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
