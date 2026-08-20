"""
seed_reasoning_course_of_action_sheet3.py
==========================================
Seeds Course of Action Q8-Q11 from Gagan Pratap Reasoning PDFs (Sheet 3).
Subject : Reasoning
Topic   : Course of Action

Standard 4 options (same order for all Course of Action questions):
  (a) Only I follows.
  (b) Only II follows.
  (c) Both I and II follow.
  (d) Neither I nor II follows.

Answer key:
  Q8  A — Organisation issues circular for 10 AM–5:30 PM attendance:
           I  (evolve mechanism to identify time-schedule violators) = logical
              first step to enforce the circular ✓
           II (summarily suspend violators) = too extreme; due process and
              progressive discipline required before suspension ✗
           Only I follows.

  Q9  D — Money has become more important than the game in Indian Cricket:
           I  (govt caps BCCI earnings) = government capping a sports body's
              income is impractical and doesn't fix the game's spirit ✗
           II (govt caps player earnings) = interference in contractual
              earnings; doesn't address the root cause of money culture ✗
           Neither I nor II follows.

  Q10 C — PDS food grains in some areas very poor, unfit for human consumption:
           I  (withdraw entire stock from distribution) = stops harmful grain
              from reaching more people immediately ✓
           II (advise people to return grain & get refund) = protects those
              who already received/bought the bad quality grain ✓
           Both I and II follow.

  Q11 B — People block highway protesting killing of 5 locals by speeding vehicle:
           I  (police fire teargas shells) = aggressive escalation against a
              grief-driven protest; disproportionate as a first response ✗
           II (police calm sentiments, assure action against culprit, deploy
              personnel) = measured, humane and effective response ✓
           Only II follows.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Course_Of_Action_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Course of Action"

_OPT_A = "Only I follows. / केवल कार्यवाही I अनुसरण करती है।"
_OPT_B = "Only II follows. / केवल कार्यवाही II अनुसरण करती है।"
_OPT_C = "Both I and II follow. / I और II दोनों कार्यवाही अनुसरण करती हैं।"
_OPT_D = "Neither I nor II follows. / न तो I और न ही II कार्यवाही अनुसरण करती है।"

QUESTIONS = [
    # ── Q8 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 8,
        "difficulty": "medium",
        "question_en": (
            "Statement: The management of the organisation has issued a circular to "
            "all its employees stating that each employee must report for duty at "
            "10:00 a.m. sharp & should remain in his/her workplace till 5:30 p.m. "
            "everyday.\n\n"
            "Courses of Action:\n"
            "I.  The management should evolve a mechanism to identify such employees "
            "who may not adhere to the time schedule.\n"
            "II. All such employees who are found to be failing to maintain time "
            "schedule should be summarily suspended."
        ),
        "question_hi": (
            "कथन: संस्था के प्रबंधन ने अपने सभी कर्मचारियों को यह बताते हुए परिपत्र "
            "जारी किया है कि प्रत्येक कर्मचारी को सुबह ठीक 10.00 बजे ड्यूटी पर रिपोर्ट "
            "करना चाहिए और शाम 5.30 तक अपने कार्यस्थल पर रहना चाहिए।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  समय सारणी का पालन न करने वाले कर्मचारियों की पहचान करने के लिए "
            "प्रबंधन को एक व्यवस्था विकसित करनी चाहिए।\n"
            "II. उन सभी कर्मचारियों को संक्षिप्त प्रक्रिया से निलंबित कर दिया जाना "
            "चाहिए जो समय सारणी का पालन करने में असफल रहें।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # I: Identification mechanism is the logical first enforcement step ✓
        # II: Summary suspension without prior warning / show-cause is too extreme
        #     and violates principles of natural justice ✗
        # Only I follows.
    },
    # ── Q9 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 9,
        "difficulty": "hard",
        "question_en": (
            "Statement: Money has become more important than the game itself in the "
            "case of Indian Cricket.\n\n"
            "Courses of Action:\n"
            "I.  Government should put a cap on the earnings of the Indian Cricket "
            "Board from different sources.\n"
            "II. Government should put a cap on the earnings of Indian Cricket players "
            "from different sources."
        ),
        "question_hi": (
            "कथन: भारतीय क्रिकेट के मामले में पैसा खेल से ज्यादा महत्वपूर्ण हो गया है।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  विभिन्न स्रोतों से भारतीय क्रिकेट बोर्ड की कमाई पर भारत सरकार को "
            "सीमा निर्धारित करनी चाहिए।\n"
            "II. विभिन्न स्रोतों से भारतीय खिलाड़ियों की कमाई पर भारत सरकार को सीमा "
            "निर्धारित करनी चाहिए।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "D",
        # I: Government capping a sports body's income from various sources is
        #    impractical and does not directly fix the cultural shift where money
        #    overshadows the game ✗
        # II: Capping individual players' earnings is interference in contractual
        #    matters; even if done, it doesn't restore the game's spirit ✗
        # Neither I nor II follows.
    },
    # ── Q10 ───────────────────────────────────────────────────────────────────────────
    {
        "question_number": 10,
        "difficulty": "easy",
        "question_en": (
            "Statement: The quality of food grains being distributed in some parts of "
            "the country through Public Distribution System is very poor & not fit for "
            "human consumption.\n\n"
            "Courses of Action:\n"
            "I.  The entire stock of food grains should be immediately withdrawn from "
            "the distribution system.\n"
            "II. People should be advised to return the food grains purchased from the "
            "system & take their money back."
        ),
        "question_hi": (
            "कथन: लोक वितरण प्रणाली द्वारा देश के कुछ हिस्सों में वितरण किए गए अनाज "
            "की गुणवत्ता बहुत खराब है और लोगों के उपभोग के लिए ठीक नहीं है।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  वितरण के लिए लिए गए सम्पूर्ण अन्न भंडार को तुरंत वापस ले लेना "
            "चाहिए।\n"
            "II. लोगों को सलाह देनी चाहिए कि वितरण द्वारा खरीदा गया अनाज वापस दे दें "
            "और अपना पैसा वापस ले लें।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "C",
        # I: Withdrawing entire stock from distribution halts further spread of
        #    unfit food grains — immediate and necessary preventive action ✓
        # II: Advising people to return purchased grain and get refunds protects
        #    those who already received the unsafe food ✓
        # Both are complementary and appropriate → Both I and II follow.
    },
    # ── Q11 ───────────────────────────────────────────────────────────────────────────
    {
        "question_number": 11,
        "difficulty": "medium",
        "question_en": (
            "Statement: A large number of people gathered on the highway blocking the "
            "traffic movement to protest the killing of five locals by a speeding "
            "vehicle.\n\n"
            "Courses of Action:\n"
            "I.  The police should fire teargas shells to disperse the crowd.\n"
            "II. The police authority should calm down the sentiment of the crowd "
            "assuring action against the culprit & deploy police personnel at the spot."
        ),
        "question_hi": (
            "कथन: तेज गति से आ रहे वाहन ने पांच व्यक्तियों को कुचल दिया जिसके कारण "
            "विरोध प्रदर्शन के लिए लोग हाईवे पर एकत्रित हो गए और यातायात के आवागमन "
            "पर रोक लगा दी।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  भीड़ को हटाने के लिए पुलिस को आंसू गैस का प्रयोग करना चाहिए।\n"
            "II. पुलिस अधिकारियों को चाहिए कि जन भावनाओं को शांत करें, अपराधियों के "
            "खिलाफ कार्यवाही का आश्वासन दें और उस स्थान पर पुलिस बल तैनात करें।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "B",
        # I: Firing teargas is an aggressive, disproportionate first response to
        #    people grieving the death of 5 locals — escalates rather than resolves ✗
        # II: Calming emotions, assuring justice, and deploying personnel is the
        #    correct measured and humane response to a grief-driven protest ✓
        # Only II follows.
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
