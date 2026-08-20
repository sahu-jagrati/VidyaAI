"""
seed_reasoning_data_sufficiency_sheet1.py
==========================================
Seeds Data Sufficiency Q1-Q2 from Gagan Pratap Reasoning PDFs (Sheet 1).
Subject : Reasoning
Topic   : Data Sufficiency

Fixed 5-option format (always the same options in the same order):
  (A) Only Statement I is sufficient to answer.
  (B) Only Statement II is sufficient to answer.
  (C) Either Statement I or Statement II is sufficient to answer.
  (D) Neither Statement I nor Statement II is sufficient to answer.
  (E) Both Statement I and Statement II are sufficient to answer.

Options (A)-(D) are stored in DB columns; option (E) is injected by the
frontend via DS_OPTION_E constant for every Data Sufficiency question
(TopicWise.jsx / DailyChallenge.jsx detect topic === "Data Sufficiency").

Answer key:
  Q1  A — How many chocolates does Seetha have?
           Statement I : Abi=10, Geetha=5, Swetha=7, Seetha=9 (fully determined) ✓
           Statement II: Swetha > Geetha but < 10 — no exact values, Seetha
                         relation unknown → cannot determine ✗
           Only Statement I is sufficient.

  Q2  D — On which day does Arun take his leave?
           Statement I : Arun does not take leave on Wednesday → 6 days still
                         possible → insufficient ✗
           Statement II: Arun took leave either on Monday or Thursday → 2 days,
                         cannot pin down exactly ✗
           Both together: Statement I does not eliminate Monday or Thursday, so
                          still 2 possibilities → insufficient ✗
           Neither Statement I nor Statement II is sufficient.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Data_Sufficiency_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Data Sufficiency"

# Standard fixed options (A)-(D) — same for every Data Sufficiency question.
# Option (E) "Both Statement I and Statement II are sufficient to answer." is
# injected by the frontend (DS_OPTION_E constant); do NOT store in DB.
_OPT_A = (
    "Only Statement I is sufficient to answer. / "
    "केवल कथन I उत्तर देने के लिए पर्याप्त है।"
)
_OPT_B = (
    "Only Statement II is sufficient to answer. / "
    "केवल कथन II उत्तर देने के लिए पर्याप्त है।"
)
_OPT_C = (
    "Either Statement I or Statement II is sufficient to answer. / "
    "या तो कथन I या कथन II उत्तर देने के लिए पर्याप्त है।"
)
_OPT_D = (
    "Neither Statement I nor Statement II is sufficient to answer. / "
    "न तो कथन I न ही कथन II उत्तर देने के लिए पर्याप्त है।"
)

QUESTIONS = [
    # ── Q1 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 1,
        "difficulty": "medium",
        "question_en": (
            "Question: How many chocolates does Seetha have?\n\n"
            "Statement I:  Abi has 10 chocolates which is five more than Geetha. "
            "Seetha has 2 chocolates more than Swetha, who has 2 more than Geetha.\n"
            "Statement II: Swetha has more chocolates than Geetha but less than Abi, "
            "who has 10 chocolates."
        ),
        "question_hi": (
            "प्रश्न: सीता के पास कितनी चॉकलेट हैं?\n\n"
            "कथन I:  अबी के पास 10 चॉकलेट हैं जो गीता से पांच अधिक हैं। सीता के "
            "पास स्वेता से 2 चॉकलेट अधिक हैं, जिसके पास गीता से 2 अधिक हैं।\n"
            "कथन II: स्वेता के पास गीता से अधिक चॉकलेट हैं लेकिन अबी से कम है, "
            "जिसके पास 10 चॉकलेट हैं।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # Statement I alone: Abi=10, Geetha=10-5=5, Swetha=5+2=7, Seetha=7+2=9 ✓
        # Statement II alone: Geetha < Swetha < 10, but no exact value given;
        #   Seetha's relation to any person unknown → cannot determine Seetha ✗
        # Only Statement I is sufficient.
    },
    # ── Q2 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 2,
        "difficulty": "medium",
        "question_en": (
            "Question: On which day does Arun take his leave?\n\n"
            "Statement I:  Arun does not take his leave on Wednesday.\n"
            "Statement II: Arun took his leave either on Monday or on Thursday."
        ),
        "question_hi": (
            "प्रश्न: अरुण किस दिन छुट्टी लेता है?\n\n"
            "कथन I:  अरुण बुधवार को छुट्टी नहीं लेता है।\n"
            "कथन II: अरुण ने या तो सोमवार या गुरुवार को छुट्टी ली।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "D",
        # Statement I alone: "Not Wednesday" → 6 remaining days possible → ✗
        # Statement II alone: Monday OR Thursday → 2 options, undetermined → ✗
        # Both together: Statement I doesn't eliminate Monday or Thursday; still
        #   {Monday, Thursday} as possibilities → cannot determine specific day → ✗
        # Neither Statement I nor Statement II is sufficient.
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
