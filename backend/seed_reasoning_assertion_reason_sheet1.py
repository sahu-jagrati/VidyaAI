"""
seed_reasoning_assertion_reason_sheet1.py
==========================================
Seeds Assertion and Reason Q1-Q2 from Gagan Pratap Reasoning PDFs (Sheet 1).
Subject : Reasoning
Topic   : Assertion and Reason

5-OPTION FORMAT HANDLING
-------------------------
All Assertion-Reason questions have 5 standard options:
  (a) Both A & R are true & R is the correct explanation of A.
  (b) Both A & R are true but R is not the correct explanation of A.
  (c) A is true but R is false.
  (d) A is false but R is true.
  (e) Both A & R are false.

The Question model only stores option_a through option_d (4 columns).
Strategy:
  • Store options (a)-(d) uniformly in the 4 DB columns for every A&R question.
  • The 5th option "(e) Both A & R are false" is included in question_en/question_hi
    text so students can read it when taking the quiz.
  • correct_answer is stored as "E" when the answer is option (e); String(1) column
    accepts any single character, so "E" is valid.
  • Frontend can be updated later to always render option_e for the A&R topic.

Answer key:
  Q1 Answer: E — Both A & R are false.
     A: "We feel comfortable in hot and humid climate" → FALSE
        (we feel UNcomfortable because humid air prevents sweat from evaporating)
     R: "Sweat evaporates faster in humid climate" → FALSE
        (high humidity → air is already moisture-saturated → sweat evaporates
         SLOWER, not faster → the body cannot cool down → discomfort)
     Both A and R have X marks in the PDF. Since A itself is false, no further
     evaluation of whether R explains A is needed.

  Q2 Answer: A — Both A & R are true & R is the correct explanation of A.
     A: "Shimla is colder than Delhi" → TRUE (well-established fact)
     R: "Shimla is at a higher altitude as compared to Delhi" → TRUE
        (Shimla ~2200 m; Delhi ~216 m)
     Does R explain A?
       Higher altitude → lower atmospheric pressure → air is thinner and retains
       less heat → lower temperatures. This is the standard scientific explanation
       (environmental lapse rate). R directly and correctly explains A. → ✓
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Assertion_Reason_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Assertion and Reason"

# Standard A&R option texts (stored in option_a through option_d for every question).
# Option (e) is included in question_en/question_hi since no option_e column exists.
_OPT_A = "Both A & R are true & R is the correct explanation of A. / A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"
_OPT_B = "Both A & R are true but R is not the correct explanation of A. / A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।"
_OPT_C = "A is true but R is false. / A सत्य है लेकिन R असत्य है।"
_OPT_D = "A is false but R is true. / A असत्य है लेकिन R सत्य है।"
_OPT_E_TEXT = "(e) Both A & R are false. / A और R दोनों असत्य हैं।"  # shown in question body

QUESTIONS = [
    # ── Q1 ── A: comfortable in hot-humid climate (FALSE) | R: sweat evaporates faster
    #          in humid climate (FALSE)  →  E: Both A & R are false ──────────────────
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): We feel comfortable in hot and humid climate.\n"
            "Reason (R): Sweat evaporates faster in humid climate.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_TEXT}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): हम गर्म और आर्द्र जलवायु में सहज महसूस करते हैं।\n"
            "कारण (R): आर्द्र जलवायु में पसीना तेजी से वाष्पित होता है।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "E",
        # REASON: A is FALSE — we feel UNCOMFORTABLE in hot and humid climate because
        # sweat cannot evaporate efficiently; R is also FALSE — sweat evaporates SLOWER
        # in humid climate (air is already saturated with moisture, leaving little
        # capacity to absorb more water vapour; this is precisely why we feel
        # uncomfortable). Both statements are factually incorrect. → E
    },
    # ── Q2 ── A: Shimla colder than Delhi (TRUE) | R: Shimla at higher altitude (TRUE)
    #          R correctly explains A  →  A: Both true & R explains A ────────────────
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": (
            "In the following question, a statement of Assertion (A) is followed by a "
            "statement of Reason (R). Select the correct option.\n\n"
            "Assertion (A): Shimla is colder than Delhi.\n"
            "Reason (R): Shimla is at a higher altitude as compared to Delhi.\n\n"
            "Options:\n"
            "(a) Both A & R are true & R is the correct explanation of A.\n"
            "(b) Both A & R are true but R is not the correct explanation of A.\n"
            "(c) A is true but R is false.\n"
            "(d) A is false but R is true.\n"
            f"{_OPT_E_TEXT}"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में अभिकथन (A) के बाद कारण (R) का एक कथन दिया गया है। "
            "सही विकल्प चुनिए।\n\n"
            "अभिकथन (A): शिमला दिल्ली की तुलना में ठंडा है।\n"
            "कारण (R): दिल्ली की तुलना में शिमला अधिक ऊंचाई पर है।\n\n"
            "विकल्प:\n"
            "(a) A और R दोनों सत्य हैं और R, A की सही व्याख्या है।\n"
            "(b) A और R दोनों सत्य हैं, लेकिन R, A की सही व्याख्या नहीं है।\n"
            "(c) A सत्य है लेकिन R असत्य है।\n"
            "(d) A असत्य है लेकिन R सत्य है।\n"
            "(e) A और R दोनों असत्य हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # REASON: A is TRUE — Shimla (~2,200 m) is indeed colder than Delhi (~216 m).
        # R is TRUE — Shimla's altitude is much higher than Delhi's.
        # Does R explain A? YES — higher altitude → lower atmospheric pressure → thinner
        # air retains less heat → temperature drops with altitude (environmental lapse
        # rate ~6.5 °C per 1,000 m). R directly and correctly explains A. → (a)
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
