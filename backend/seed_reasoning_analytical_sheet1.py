"""
seed_reasoning_analytical_sheet1.py
=========================================
Seeds Analytical Reasoning Q1-Q3 from Gagan Pratap Reasoning PDFs (Sheet 1).
Subject : Reasoning
Topic   : Analytical Reasoning
Run     : python seed_reasoning_analytical_sheet1.py

Question types:
  Q1  — Statement + 2 conclusions (can conclusions be logically derived?)
  Q2  — Main statement + 4 labelled sub-statements; pick ordered pair(s) where
         first logically implies second and both are consistent with the main statement
  Q3  — Set of conditional premises; which listed conclusions follow via valid logic?

Answer key (solutions verified):
  Q1  Statement: India is the world's largest producer of milk.
      I) India is the world's largest exporter of milk.
         → Being largest producer ≠ largest exporter (domestic consumption may absorb output)
         → FALSE
      II) India does not import milk.
         → Production capacity does not logically rule out importing milk
         → FALSE
      Answer: D  (Neither conclusion I nor conclusion II follows)

  Q2  Main Statement: Pradeep becomes either a Director or a Producer.  (D ∨ P)
      P = Pradeep is a Director.
      Q = Pradeep is a Producer.
      R = Pradeep is NOT a Director.  (¬D)
      S = Pradeep is NOT a Producer.  (¬P)

      SP: S(¬P) → P(D).  From D∨P, if ¬P then D must hold → valid ✓
      RQ: R(¬D) → Q(P).  From D∨P, if ¬D then P must hold → valid ✓
      Answer: C  (Both SP and RQ)

  Q3  Given premises:
        (1) P → (Q ∧ S)
        (2) (R ∧ S) → ¬T

      Conclusion I: "If T is true, then at least one of P and R must be false."
        Proof (contrapositive): Assume P∧R.
          From (1): S is true.   From (2): R∧S → ¬T, so T is false.
          Contrapositive: T → ¬(P∧R) → ¬P ∨ ¬R  → valid ✓

      Conclusion II: "If Q is true, then P is true."
        Premise (1) gives P → Q, not Q → P.
        This is the fallacy of affirming the consequent → invalid ✗

      Answer: A  (I only)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Analytical_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Analytical Reasoning"

QUESTIONS = [
    # ── Q1 ── Statement → two conclusions; neither follows ────────────────────
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": (
            "A Statement is given followed by two Conclusions numbered I and II. "
            "Consider the Statement and the Conclusions.\n\n"
            "Statement: India is the world's largest producer of milk.\n\n"
            "Conclusion I: India is the world's largest exporter of milk.\n"
            "Conclusion II: India does not import milk.\n\n"
            "Which one of the following is correct?"
        ),
        "question_hi": (
            "एक कथन के बाद दो निष्कर्ष I और II दिए गए हैं। कथन और निष्कर्ष पर "
            "विचार कीजिए।\n\n"
            "कथन: भारत विश्व का सबसे बड़ा दूध उत्पादक है।\n\n"
            "निष्कर्ष I: भारत विश्व का सबसे बड़ा दूध निर्यातक है।\n"
            "निष्कर्ष II: भारत दूध का आयात नहीं करता है।\n\n"
            "निम्नलिखित में से कौन सा सही है?"
        ),
        "option_a": "Only conclusion I follows / केवल निष्कर्ष I अनुसरण करता है",
        "option_b": "Only conclusion II follows / केवल निष्कर्ष II अनुसरण करता है",
        "option_c": "Both conclusion I and conclusion II follow / निष्कर्ष I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither conclusion I nor conclusion II follows / न तो निष्कर्ष I और न ही II अनुसरण करता है",
        "correct_answer": "D",
        # I: largest producer ≠ largest exporter (domestic demand absorbs output) → FALSE
        # II: production volume does not rule out imports → FALSE
    },
    # ── Q2 ── Ordered-pair implication; both SP and RQ valid ──────────────────
    {
        "question_number": 2,
        "difficulty": "medium",
        "question_en": (
            "A Main Statement is followed by four Statements labelled P, Q, R and S. "
            "Choose the ordered pair of the Statements where the first Statement implies "
            "the second, and the two Statements are logically consistent with the Main Statement.\n\n"
            "Main Statement: Pradeep becomes either a Director or a Producer.\n\n"
            "Statement P: Pradeep is a Director.\n"
            "Statement Q: Pradeep is a Producer.\n"
            "Statement R: Pradeep is not a Director.\n"
            "Statement S: Pradeep is not a Producer.\n\n"
            "Select the correct answer."
        ),
        "question_hi": (
            "एक मुख्य कथन के बाद P, Q, R और S से अंकित चार कथन दिए गए हैं। "
            "कथनों के क्रमित जोड़े चुनिए जहाँ पहला कथन दूसरे कथन को दर्शाता है "
            "और दोनों कथन तार्किक रूप से मुख्य कथन के अनुरूप हैं।\n\n"
            "मुख्य कथन: प्रदीप या तो निदेशक या तो निर्माता बन जाता है।\n\n"
            "कथन P: प्रदीप एक निदेशक है।\n"
            "कथन Q: प्रदीप एक निर्माता है।\n"
            "कथन R: प्रदीप एक निदेशक नहीं है।\n"
            "कथन S: प्रदीप एक निर्माता नहीं है।\n\n"
            "सही उत्तर चुनिए।"
        ),
        "option_a": "SP only / केवल SP",
        "option_b": "RQ only / केवल RQ",
        "option_c": "Both SP and RQ / SP और RQ दोनों",
        "option_d": "Neither SP nor RQ / न तो SP और न ही RQ",
        "correct_answer": "C",
        # D∨P (Director or Producer).
        # SP: S(¬P) → P(D): if not-Producer, must be Director → valid ✓
        # RQ: R(¬D) → Q(P): if not-Director, must be Producer → valid ✓
    },
    # ── Q3 ── Conditional logic premises; only conclusion I follows ────────────
    {
        "question_number": 3,
        "difficulty": "hard",
        "question_en": (
            "Let P, Q, R, S and T be five statements such that:\n"
            "I.  If P is true, then both Q and S are true.\n"
            "II. If R and S are true, then T is false.\n\n"
            "Which of the following can be concluded?\n\n"
            "I.  If T is true, then at least one of P and R must be false.\n"
            "II. If Q is true, then P is true.\n\n"
            "Select the correct answer."
        ),
        "question_hi": (
            "मान लीजिए कि P, Q, R, S और T पाँच कथन हैं, जैसे:\n"
            "I.  यदि P सत्य है, तो Q और S दोनों सत्य हैं।\n"
            "II. यदि R और S सत्य हैं, तो T असत्य है।\n\n"
            "निम्न में से कौन सा निष्कर्ष निकाला जा सकता है?\n\n"
            "I.  यदि T सत्य है, तो P और R में से कम से कम एक असत्य होना चाहिए।\n"
            "II. यदि Q सत्य है, तो P सत्य है।\n\n"
            "नीचे दिए गए कूट का उपयोग करके सही उत्तर चुनिए।"
        ),
        "option_a": "I only / केवल I",
        "option_b": "II only / केवल II",
        "option_c": "Both I and II / I और II दोनों",
        "option_d": "Neither I nor II / न तो I और न ही II",
        "correct_answer": "A",
        # Premise 1: P → (Q∧S). Premise 2: (R∧S) → ¬T.
        # Conclusion I: T → (¬P ∨ ¬R).
        #   Proof: assume P∧R → from P: S is true → R∧S → T is false.
        #   Contrapositive: T → ¬(P∧R) = ¬P∨¬R  → VALID ✓
        # Conclusion II: Q → P.
        #   Premise 1 gives P→Q (P sufficient for Q); Q→P would be converse (not guaranteed)
        #   Fallacy of affirming the consequent → INVALID ✗
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
