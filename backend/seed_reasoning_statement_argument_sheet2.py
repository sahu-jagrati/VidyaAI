"""
seed_reasoning_statement_argument_sheet2.py
============================================
Seeds Statement-Argument Q5–Q9 from Gagan Pratap Reasoning PDFs (Sheet 2).
Subject : Reasoning
Topic   : Statement Argument

Fixed 4-option format (same options every question):
  (A) Only argument I is strong.
  (B) Only argument II is strong.
  (C) Both I & II are strong.
  (D) Neither I nor II is strong.

Answer key:
  Q5  D — Surrogate tobacco ads: ban or not?
           I:  "Only way" to prevent tobacco use → WEAK
               (taxation, health warnings, education are proven alternatives)
           II: Companies spend a lot on ads, so shouldn't ban → WEAK
               (profit motive / commercial investment ≠ valid policy reason)
           Neither I nor II is strong.

  Q6  B — Extend reservation to private sector?
           I:  Private sector management won't agree → WEAK
               (resistance from those subject to a regulation is never a valid
               objection; govts regulate private sectors routinely)
           II: Will significantly improve economic conditions of weaker sections → STRONG
               (direct, concrete societal benefit — the whole purpose of reservation)
           Only Argument II is strong.

  Q7  A — Legislation to ensure children maintain aging parents?
           I:  Growing abuse & neglect of aged parents is a serious and expanding
               social problem → STRONG (concrete, growing harm that directly
               justifies the proposed law)
           II: Implementation cost will be too much → WEAK
               (vague; cost alone cannot override a socially vital legislative need;
               laws protecting elderly are considered essential)
           Only Argument I is strong.

  Q8  B — Divert space research funds to address needs of the poor?
           I:  Our space budget is lower than other countries so we can't compete,
               better redirect it → WEAK
               (flawed logic: lower budget ≠ futile research; competition is not
               the only measure of value; conclusion doesn't follow from premise)
           II: Communication satellites enable telemedicine → rural people get
               access to best professional advice → STRONG
               (space research itself directly benefits poor/rural populations;
               this directly counters the statement)
           Only Argument II is strong.

  Q9  A — Merge loss-making Govt. airlines into a single entity?
           I:  Merger pools resources → expanded services → more competitive with
               private & foreign airlines → STRONG
               (directly addresses the problem; logical chain of practical benefit)
           II: Merger will result in loss of jobs → WEAK
               (continued heavy losses risk full closure, which would cause far more
               job losses; temporary restructuring concern is outweighed by the
               long-term viability argument)
           Only Argument I is strong.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Statement_Argument_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Statement Argument"

# Standard fixed options — identical for every Statement-Argument question.
_OPT_A = "Only argument I is strong. / केवल तर्क I ठोस है।"
_OPT_B = "Only argument II is strong. / केवल तर्क II ठोस है।"
_OPT_C = "Both I & II are strong. / तर्क I और II दोनों ठोस हैं।"
_OPT_D = "Neither I nor II is strong. / न तो तर्क I और न ही तर्क II ठोस है।"

QUESTIONS = [
    # ── Q5 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 5,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should all the surrogate advertisements released by "
            "companies manufacturing tobacco products be banned?\n\n"
            "Arguments:\n"
            "I.  Yes, this is the only way to prevent the use of tobacco products "
            "by people.\n"
            "II. No, these companies spend a lot of money for preparing these "
            "advertisements and hence they should not be banned."
        ),
        "question_hi": (
            "कथन: क्या तम्बाकू बनाने वाली कंपनियों द्वारा प्रतिनिधित्व प्रचार "
            "पर रोक लगानी चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, यही एकमात्र तरीका है, लोगों को तम्बाकू प्रयोग से रोकने "
            "के लिए।\n"
            "II. नहीं, ये कंपनियाँ इन प्रचारों को तैयार करने में काफी खर्च करती "
            "हैं इसलिए इन पर रोक नहीं लगानी चाहिए।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "D",
        # I:  "ONLY way" → too absolute; taxation, labelling, awareness campaigns,
        #     outright bans are proven alternatives to surrogate-ad bans → WEAK ✗
        # II: Commercial investment in ads is not a valid reason to allow advertising
        #     of harmful products → profit motive ≠ policy justification → WEAK ✗
    },
    # ── Q6 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 6,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should the reservation of jobs for weaker sections of the "
            "society be extended to the private sectors also?\n\n"
            "Arguments:\n"
            "I.  No, the management of the private sector undertakings would not "
            "agree to such compulsions.\n"
            "II. Yes, this will significantly improve the economic conditions of the "
            "weaker sections of the society."
        ),
        "question_hi": (
            "कथन: क्या निजी क्षेत्रों में भी कमजोर वर्गों के लिए आरक्षण को "
            "बढ़ाया दिया जाना चाहिए?\n\n"
            "तर्क:\n"
            "I.  नहीं, निजी क्षेत्र का प्रबंधन इस प्रश्न पर तैयार नहीं होगा।\n"
            "II. हाँ, यह कमजोर वर्गों की आर्थिक स्थिति में काफी हद तक सुधार "
            "लायेगा।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "B",
        # I:  Resistance of those subject to a regulation is never a valid objection;
        #     governments routinely regulate private sectors → WEAK ✗
        # II: Direct, concrete socio-economic benefit to disadvantaged groups;
        #     directly relevant to the policy's stated goal → STRONG ✓
    },
    # ── Q7 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 7,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should there be a legislation to ensure that children provide "
            "maintenance to their aging parents?\n\n"
            "Arguments:\n"
            "I.  Yes, the magnitude of the problem of abuse and neglect of aged "
            "parents by their immediate family is growing.\n"
            "II. No, the cost of implementing this legislation will be too much."
        ),
        "question_hi": (
            "कथन: क्या यह सुनिश्चित करने के लिए कानून होना चाहिए कि बच्चे बूढ़े "
            "माता-पिता को गुजारा भत्ता दें?\n\n"
            "तर्क:\n"
            "I.  हाँ, बूढ़े माता-पिता को उनके नजदीकी परिवार द्वारा उपेक्षा और "
            "दुर्व्यवहार की समस्या की परिमाण बढ़ रही है।\n"
            "II. नहीं, इस कानून को क्रियान्वित करने की लागत बहुत अधिक होगी।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # I:  Growing, documented social problem (elder abuse/neglect) directly
        #     justifies the proposed law; concrete and escalating harm → STRONG ✓
        # II: "Cost will be too much" is vague and relative; cost alone cannot
        #     override a socially vital legislation protecting the elderly → WEAK ✗
    },
    # ── Q8 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 8,
        "difficulty": "medium",
        "question_en": (
            "Statement: Should the funding for National Space Research programmes be "
            "diverted to addressing the needs of the poor?\n\n"
            "Arguments:\n"
            "I.  Yes, our budget for space research is lower than that of other "
            "countries. So we cannot compete with them and hence it can be put to "
            "better use in schemes to benefit the poor.\n"
            "II. No, communication satellites help to provide services like "
            "telemedicine. So people in rural areas can get access to the best "
            "professional advice."
        ),
        "question_hi": (
            "कथन: क्या राष्ट्रीय अंतरिक्ष अनुसंधान कार्यक्रमों के लिए दी जा रही "
            "निधि को गरीबों की जरूरतों को पूरा करने के लिए खर्च कर देना चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, हमारा अंतरिक्ष अनुसंधान का बजट अन्य देशों के बजट से कम "
            "होता है। इसलिए, हम उनसे प्रतिस्पर्धा नहीं कर सकते और उसे गरीबों में "
            "लाभ वाली योजनाओं के बेहतर काम पर लगाया जा सकता है।\n"
            "II. नहीं, संचार उपग्रह टेलीमेडिसिन जैसी सेवाएं देने में मदद करते "
            "हैं। इसलिए ग्रामीण इलाकों के लोगों को बेहतरीन पेशेवर सलाह मिल "
            "सकती है।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "B",
        # I:  Flawed reasoning — lower budget ≠ futile research; competition is not
        #     the sole measure of space programme value; conclusion does not follow
        #     logically from the premise → WEAK ✗
        # II: Communication satellites directly enable telemedicine, giving rural
        #     poor access to professional healthcare — space research itself benefits
        #     the poor; strong, concrete counter-argument → STRONG ✓
    },
    # ── Q9 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 9,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should loss incurring Govt. airlines be merged into a "
            "single entity?\n\n"
            "Arguments:\n"
            "I.  Yes, the merger will pool their resources allowing them to expand "
            "their services and be more competitive with private and foreign airlines.\n"
            "II. No, the merger will result in loss of jobs."
        ),
        "question_hi": (
            "कथन: क्या घाटा देने वाली सरकारी एयरलाइनों का विलय करके उन्हें एक "
            "इकाई बना देना चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, विलय से उनके संसाधन इकट्ठे हो जायेंगे और उनकी सेवाएं बढ़ "
            "सकेंगी और वे निजी और फिर विदेशी एयरलाइनों से प्रतिस्पर्धी काम कर "
            "सकेंगी।\n"
            "II. नहीं, विलय से नौकरियाँ जाएंगी।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # I:  Pooled resources → expanded services → competitiveness against private
        #     & foreign airlines; directly addresses the loss-making problem with a
        #     clear, logical benefit chain → STRONG ✓
        # II: "Merger will result in loss of jobs" is a general restructuring concern;
        #     NOT merging risks full closure of loss-making airlines (far more job
        #     losses); temporary redundancy concern is outweighed by long-term
        #     viability → WEAK ✗
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
