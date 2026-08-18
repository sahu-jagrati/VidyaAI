"""
seed_reasoning_analytical_sheet2.py
=========================================
Seeds Analytical Reasoning Q4-Q6 from Gagan Pratap Reasoning PDFs (Sheet 2).
Subject : Reasoning
Topic   : Analytical Reasoning
Run     : python seed_reasoning_analytical_sheet2.py

Answer key (solutions verified):
  Q4  Statement: Municipal Commissioner told city 'A' people:
        "My first and foremost task is to beautify this city like Indore."
      I)  People of city 'A' are not aware of the present condition of the city.
          → Statement contains no information about citizens' awareness → FALSE
      II) The Commissioner has worked in Indore and has good experience in
          beautifying cities.
          → Using Indore as a benchmark does not mean the Commissioner worked
            there; it could merely be a well-known example → FALSE
      Answer: A  (Neither conclusion I nor conclusion II follows)

  Q5  Statement: In a one-day cricket match, total runs by a team = 200,
        of which 160 runs were made by spinners.
      I)  80% of the team consisted of spinners.
          → Runs scored ≠ proportion of players in the 11-member team → FALSE
      II) The opening batsmen were spinners.
          → Statement gives no information about batting order → FALSE
      Answer: D  (Neither I nor II follows the statement)

  Q6  Statement: Money is a huge motivator.
      I)  People get motivated ONLY when they expect to get money.
          → "only" is overly restrictive; money is "a" (one of many)
            motivator, not the sole motivator → FALSE
      II) There are some factors other than money which also motivate people.
          → "Money is A huge motivator" (use of the indefinite article "a")
            implies other motivators exist → TRUE
      Answer: A  (Only II follows)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Analytical_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Analytical Reasoning"

QUESTIONS = [
    # ── Q4 ── Neither conclusion follows ──────────────────────────────────────
    {
        "question_number": 4,
        "difficulty": "easy",
        "question_en": (
            "A Statement is given followed by two Conclusions. Consider the Statement "
            "and the Conclusions. Decide which of the given conclusions logically follows "
            "from the given statements.\n\n"
            "Statement: After joining, the Municipal Commissioner told the people of the "
            "city 'A' — 'My first and foremost task is to beautify this city like Indore.'\n\n"
            "Conclusion I: The people of the city 'A' are not aware of the present "
            "condition of the city.\n"
            "Conclusion II: The Commissioner has worked in Indore and has good experience "
            "in beautifying cities."
        ),
        "question_hi": (
            "एक कथन के बाद दो निष्कर्ष I और II दिए गए हैं। कथन और निष्कर्ष पर "
            "विचार कीजिए। तय कीजिए कि इनमें से कौन सा निष्कर्ष तार्किक रूप से दिए "
            "गए कथन से अनुसरण करता है।\n\n"
            "कथन: नगर निगम आयुक्त ने शहर 'A' के लोगों से कहा — 'मेरा पहला और सबसे "
            "महत्वपूर्ण काम इस शहर को इंदौर की तरह सुंदर बनाना है।'\n\n"
            "निष्कर्ष I: शहर 'A' के लोग शहर की वर्तमान स्थिति से अवगत नहीं हैं।\n"
            "निष्कर्ष II: आयुक्त ने इंदौर में काम किया है और शहरों को सुंदर बनाने "
            "में उनका अच्छा अनुभव है।"
        ),
        "option_a": "Neither conclusion I nor conclusion II follows / न तो निष्कर्ष I और न ही II अनुसरण करते हैं",
        "option_b": "Both of the conclusions follow / दोनों निष्कर्ष अनुसरण करते हैं",
        "option_c": "Only conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_d": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "correct_answer": "A",
        # I: statement has no info about citizens' awareness → FALSE
        # II: Indore as benchmark ≠ Commissioner worked there → FALSE
    },
    # ── Q5 ── Neither conclusion follows ──────────────────────────────────────
    {
        "question_number": 5,
        "difficulty": "easy",
        "question_en": (
            "Read the given statement and conclusion carefully. Decide which of the given "
            "conclusions logically follows from the given statement.\n\n"
            "Statement: In a one-day cricket match, the total runs made by a team were 200, "
            "of which 160 runs were made by spinners.\n\n"
            "Conclusion I: 80% of the team consisted of spinners.\n"
            "Conclusion II: The opening batsmen were spinners."
        ),
        "question_hi": (
            "दिए गए कथन और निष्कर्ष को ध्यान से पढ़िए। तय कीजिए कि दिए गए निष्कर्षों "
            "में से कौन सा कथन का तार्किक रूप से अनुसरण करता है।\n\n"
            "कथन: एक दिवसीय क्रिकेट मैच में एक टीम द्वारा बनाए गए कुल रन 200 थे, "
            "जिनमें से 160 रन स्पिनरों द्वारा बनाए गए।\n\n"
            "निष्कर्ष I: टीम में 80% स्पिनर थे।\n"
            "निष्कर्ष II: शुरुआती बल्लेबाज स्पिनर थे।"
        ),
        "option_a": "Only I follows the statement / केवल I कथन का अनुसरण करता है",
        "option_b": "Only II follows the statement / केवल II कथन का अनुसरण करता है",
        "option_c": "Both I and II follow the statement / I और II दोनों कथन का अनुसरण करते हैं",
        "option_d": "Neither I nor II follows the statement / न तो I और न ही II कथन का अनुसरण करता है",
        "correct_answer": "D",
        # I: runs scored by spinners (160/200 = 80%) ≠ % of spinners in 11-player team → FALSE
        # II: statement gives no information about batting order → FALSE
    },
    # ── Q6 ── Only conclusion II follows ──────────────────────────────────────
    {
        "question_number": 6,
        "difficulty": "easy",
        "question_en": (
            "Which option is/are to be followed?\n\n"
            "Statement: Money is a huge motivator.\n\n"
            "Conclusion I: People get motivated only when they expect to get some money "
            "for doing or behaving in a certain way.\n"
            "Conclusion II: There are some factors other than money which also motivate "
            "people."
        ),
        "question_hi": (
            "कौन सा विकल्प/विकल्प अपनाने वाले चाहिए?\n\n"
            "कथन: पैसा एक बहुत बड़ा प्रेरक है।\n\n"
            "निष्कर्ष I: लोग तभी प्रेरित होते हैं जब वे किसी तरीके से काम करने या "
            "व्यवहार करने के लिए कुछ पैसे मिलने की उम्मीद करते हैं।\n"
            "निष्कर्ष II: पैसे के अलावा कुछ अन्य कारण भी हैं जो लोगों को प्रेरित "
            "करते हैं।"
        ),
        "option_a": "Only II follow / केवल II अनुसरण करता है",
        "option_b": "Both I and II follow / I और II दोनों अनुसरण करते हैं",
        "option_c": "Neither I nor II follow / न तो I और न ही II अनुसरण करता है",
        "option_d": "Only I follow / केवल I अनुसरण करता है",
        "correct_answer": "A",
        # I: "ONLY" money — too restrictive; money is "a" motivator, not the sole one → FALSE
        # II: "a huge motivator" (use of "a") implies other motivators exist → TRUE
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
