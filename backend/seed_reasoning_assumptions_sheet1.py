"""
seed_reasoning_assumptions_sheet1.py
=========================================
Seeds Assumptions Q1-Q2 from Gagan Pratap Reasoning PDFs (Sheet 1).
Subject : Reasoning
Topic   : Assumptions
Run     : python seed_reasoning_assumptions_sheet1.py

NOTE: "Assumptions" is a new topic — added to frontend TopicWise.jsx alongside
this seed. The topic covers questions where you decide which implicit assumptions
underlie a given statement.

Answer key (solutions verified):
  Q1   Statement: The municipal corporation has announced 50% reduction in water
       supply till monsoon arrives in the city.
       I)  People may protest against the unilateral decision of the municipal
           corporation → NOT IMPLICIT
           (protest is a possible reaction but the corporation made the decision
            without assuming public approval; protest is speculative, not assumed)
       II) Municipal corporation may reduce its taxes from the residents as it
           failed to provide adequate water → NOT IMPLICIT
           (tax reduction is not implied by reducing water supply; these are
            independent administrative actions)
       Answer: D  (Neither I nor II is implicit)

  Q2   Statement: Many people were caught by the railway police while they were
       trying to cross the railway tracks & imposed heavy penalty before releasing them.
       I)  People may refrain from crossing railway tracks in future → IMPLICIT
           (imposing a penalty assumes it will deter future violations — that is the
            very purpose of a penalty)
       II) People may continue crossing railway tracks & pay heavy penalty → NOT IMPLICIT
           (assuming the penalty will fail to deter contradicts the purpose of imposing
            the penalty in the first place)
       Answer: A  (Only I is implicit)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Assumptions_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Assumptions"

QUESTIONS = [
    # ── Q1 ── Neither assumption implicit (50% water supply reduction) ─────────
    {
        "question_number": 1,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: The municipal corporation has announced 50% reduction in water "
            "supply till monsoon arrives in the city.\n\n"
            "Assumptions:\n"
            "I.  People may protest against the unilateral decision of the municipal "
            "corporation.\n"
            "II. Municipal corporation may reduce its taxes from the residents as it "
            "failed to provide adequate water."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: नगर निगम ने मानसून के आने तक शहर में जल आपूर्ति में 50% कमी करने "
            "की घोषणा की है।\n\n"
            "पूर्वानुमान:\n"
            "I.  हो सकता है लोग नगर निगम के एकपक्षीय निर्णय का विरोध करेंगे।\n"
            "II. हो सकता है नगर निगम निवासियों के कर को कम कर दे क्योंकि यह पर्याप्त "
            "जल उपलब्ध कराने में असफल रहा है।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "D",
        # I: protest is speculative — the corporation made its decision without assuming
        #    public approval or reaction → NOT IMPLICIT ✗
        # II: tax reduction is a separate administrative action, not implied by cutting
        #    water supply → NOT IMPLICIT ✗
    },
    # ── Q2 ── Only Assumption I implicit (railway track crossing penalty) ──────
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: Many people were caught by the railway police while they were "
            "trying to cross the railway tracks & imposed heavy penalty before "
            "releasing them.\n\n"
            "Assumptions:\n"
            "I.  People may refrain from crossing railway tracks in future.\n"
            "II. People may continue crossing railway tracks & pay heavy penalty."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: रेल पटरियों को पार करने की कोशिश कर रहे कई लोगों को रेलवे पुलिस ने "
            "पकड़ लिया और छोड़ने से पहले उन पर भारी जुर्माना लगाया।\n\n"
            "पूर्वानुमान:\n"
            "I.  हो सकता है भविष्य में लोग रेल पटरियों पर न चढ़ें।\n"
            "II. हो सकता है लोग पटरियाँ पार करते रहें तथा भारी जुर्माना भरते रहें।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "A",
        # I: imposing a penalty assumes it will deter future violations — that is the
        #    very purpose of a penalty → IMPLICIT ✓
        # II: assuming penalty will fail to deter contradicts the purpose of imposing it
        #    → NOT IMPLICIT ✗
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
