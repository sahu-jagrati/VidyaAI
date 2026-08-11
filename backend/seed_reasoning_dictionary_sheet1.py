"""
seed_reasoning_dictionary_sheet1.py
=====================================
Seeds Dictionary questions Q1-Q6 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Dictionary
Run     : python seed_reasoning_dictionary_sheet1.py

Answer key verification:
  Q1: Infatuation<Influence<Ingenious<Inhabit<Inherit  => 5,4,2,1,3 = 54213  -> B
  Q2: Decorate<Decrease<Deficiency<Democratic<Demonetization<Destroy
      => 6,5,2,1,4,3 = 652143                                                 -> A
  Q3: VERTEBENA<VERTEBRAL<VERTEX<VERTICAL<VERTICIL
      => 5,1,4,2,3 = 51423                                                    -> A
  Q4: Reverse of Q1 => 3,1,2,4,5 = 31245                                     -> B
  Q5: Unique<United<Uranium<Urvashi<Usha<Usmaan<Utensils  => 3rd = Uranium   -> A
  Q6: Gears<Goa<Gomti<Grapes<Great<Guava                  => 3rd = Gomti    -> B
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Dictionary_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Dictionary"

QUESTIONS = [
    # ── Q1 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": (
            "Arrange the following words as per order in the dictionary: "
            "(1) Inhabit  (2) Ingenious  (3) Inherit  (4) Influence  (5) Infatuation"
        ),
        "question_hi": (
            "अंग्रेजी शब्दकोश के क्रमानुसार निम्नलिखित शब्दों को व्यवस्थित करें: "
            "(1) Inhabit  (2) Ingenious  (3) Inherit  (4) Influence  (5) Infatuation"
        ),
        "option_a": "45312",
        "option_b": "54213",
        "option_c": "45213",
        "option_d": "54312",
        "correct_answer": "B",
    },
    # ── Q2 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 2,
        "difficulty": "medium",
        "question_en": (
            "Arrange the following words as per order in the dictionary: "
            "(1) Democratic  (2) Deficiency  (3) Destroy  (4) Demonetization  "
            "(5) Decrease  (6) Decorate"
        ),
        "question_hi": (
            "दिए गए शब्दों को अंग्रेजी वर्णमालानुसार व्यवस्थित करें: "
            "(1) Democratic  (2) Deficiency  (3) Destroy  (4) Demonetization  "
            "(5) Decrease  (6) Decorate"
        ),
        "option_a": "652143",
        "option_b": "562413",
        "option_c": "651234",
        "option_d": "561324",
        "correct_answer": "A",
    },
    # ── Q3 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 3,
        "difficulty": "medium",
        "question_en": (
            "Arrange the following words as per order in the dictionary: "
            "(1) VERTEBRAL  (2) VERTICAL  (3) VERTICIL  (4) VERTEX  (5) VERTEBENA"
        ),
        "question_hi": (
            "अंग्रेजी शब्दकोश के क्रमानुसार निम्नलिखित शब्दों को व्यवस्थित करें: "
            "(1) VERTEBRAL  (2) VERTICAL  (3) VERTICIL  (4) VERTEX  (5) VERTEBENA"
        ),
        "option_a": "51423",
        "option_b": "51432",
        "option_c": "54132",
        "option_d": "54123",
        "correct_answer": "A",
    },
    # ── Q4 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 4,
        "difficulty": "easy",
        "question_en": (
            "Arrange the following words as per the REVERSE order in the dictionary: "
            "(1) Inhabit  (2) Ingenious  (3) Inherit  (4) Influence  (5) Infatuation"
        ),
        "question_hi": (
            "दिए गए शब्दों को अंग्रेजी वर्णमालानुसार उनके विपरीत क्रम में व्यवस्थित करें: "
            "(1) Inhabit  (2) Ingenious  (3) Inherit  (4) Influence  (5) Infatuation"
        ),
        "option_a": "32415",
        "option_b": "31245",
        "option_c": "31254",
        "option_d": "32154",
        "correct_answer": "B",
    },
    # ── Q5 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": (
            "If the given words are arranged according to the English alphabetical order, "
            "then which of the following words will come at third place? "
            "(1) Uranium  (2) Urvashi  (3) Usmaan  (4) Usha  "
            "(5) Utensils  (6) United  (7) Unique"
        ),
        "question_hi": (
            "दिए गए शब्दों को अंग्रेजी वर्णमालानुसार व्यवस्थित किया जाए तो कौन "
            "तीसरे स्थान पर आयेगा? "
            "(1) Uranium  (2) Urvashi  (3) Usmaan  (4) Usha  "
            "(5) Utensils  (6) United  (7) Unique"
        ),
        "option_a": "Uranium",
        "option_b": "Urvashi",
        "option_c": "Usha",
        "option_d": "United",
        "correct_answer": "A",
    },
    # ── Q6 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": (
            "If the given words are arranged according to the English alphabetical order, "
            "then which of the following words will come at third place? "
            "(1) Great  (2) Goa  (3) Guava  (4) Grapes  (5) Gomti  (6) Gears"
        ),
        "question_hi": (
            "दिए गए शब्दों को अंग्रेजी वर्णमालानुसार व्यवस्थित किया जाए तो कौन "
            "तीसरे स्थान पर आयेगा? "
            "(1) Great  (2) Goa  (3) Guava  (4) Grapes  (5) Gomti  (6) Gears"
        ),
        "option_a": "Goa",
        "option_b": "Gomti",
        "option_c": "Great",
        "option_d": "Gears",
        "correct_answer": "B",
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
            fp = d["question_en"][:80]
            if fp in existing_short:
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
        print(f"\nDone -- inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
