"""
seed_reasoning_alphabet_sheet3_fix.py
=========================================
Inserts Q20, Q21, Q23, Q24 that were skipped by fingerprint collision.

Root cause: multiple ordering questions share identical first-80-char preamble
("Select the option that indicates the correct arrangement of the given words in t")
so they collide with Q1/Q5 already in DB.

Fix: restructure question_en to START with the word list, making first-80-chars unique.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Alphabet_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Alphabet"

QUESTIONS = [
    # ── Q20 ── word list first → unique fingerprint ───────────────────────────
    {
        "question_number": 20,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Kibble 2.Kennel 3.Kettle 4.Kicker 5.Kernel — "
            "Select the option that indicates the correct arrangement of the given words "
            "in the order in which they appear in an English dictionary. "
            "[CPO-28 Jun 2024 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Kibble 2.Kennel 3.Kettle 4.Kicker 5.Kernel — "
            "उस विकल्प का चयन करें जो दिए गए शब्दों की अंग्रेजी शब्दकोश में उनके क्रम में "
            "सही व्यवस्था को इंगित करता है।"
        ),
        "option_a": "5, 2, 3, 1, 4",
        "option_b": "2, 5, 3, 1, 4",
        "option_c": "5, 3, 2, 1, 4",
        "option_d": "2, 3, 5, 4, 1",
        "correct_answer": "B",
        # Ken-n(Kennel2) < Ker(Kernel5) < Ket(Kettle3) < Kib(Kibble1) < Kic(Kicker4) → 2,5,3,1,4
    },
    # ── Q21 ── word list first → unique fingerprint ───────────────────────────
    {
        "question_number": 21,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Infant 2.Indolent 3.Inert 4.Infamous 5.Inefficient 6.Ineffable — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CPO-28 Jun 2024 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Infant 2.Indolent 3.Inert 4.Infamous 5.Inefficient 6.Ineffable — "
            "उस विकल्प का चयन करें जो दिए गए शब्दों के सही उस क्रम को दर्शाता है "
            "जैसा कि वे अंग्रेजी शब्दकोश में दिखाई देंगे।"
        ),
        "option_a": "2, 6, 5, 3, 4, 1",
        "option_b": "5, 4, 3, 2, 1, 6",
        "option_c": "5, 3, 4, 6, 2, 1",
        "option_d": "2, 5, 6, 1, 4, 3",
        "correct_answer": "A",
        # Ind(2) < Ine-f-f-a(6) < Ine-f-f-i(5) < Ine-r(3) < Inf-a-m(4) < Inf-a-n(1) → 2,6,5,3,4,1
    },
    # ── Q23 ── word list first → unique fingerprint ───────────────────────────
    {
        "question_number": 23,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Incest 2.Inception 3.Incense 4.Incapacity 5.Incentive — "
            "Select the option that indicates the correct arrangement of the given words "
            "in the order in which they appear in an English dictionary. "
            "[CPO-28 Jun 2024 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Incest 2.Inception 3.Incense 4.Incapacity 5.Incentive — "
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों की सही उस क्रम में व्यवस्था को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "5, 3, 2, 1, 4",
        "option_b": "4, 3, 5, 2, 1",
        "option_c": "5, 4, 3, 2, 1",
        "option_d": "4, 5, 3, 2, 1",
        "correct_answer": "D",
        # Inca(4) < Ince-n-t(5) < Ince-n-s(3) < Incep(2) < Inces(1) per official CPO key → 4,5,3,2,1
    },
    # ── Q24 ── word list first → unique fingerprint ───────────────────────────
    {
        "question_number": 24,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Dinnerware 2.Dingiest 3.Dinosaurs 4.Dinucleotide 5.Dinkier 6.Dingling — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CPO-28 Jun 2024 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Dinnerware 2.Dingiest 3.Dinosaurs 4.Dinucleotide 5.Dinkier 6.Dingling — "
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों के उस क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देंगे।"
        ),
        "option_a": "5, 2, 3, 6, 1, 4",
        "option_b": "2, 6, 3, 5, 1, 4",
        "option_c": "5, 2, 6, 3, 1, 4",
        "option_d": "2, 6, 5, 1, 3, 4",
        "correct_answer": "D",
        # Ding-i(2)<Ding-l(6)<Dink(5)<Dinn(1)<Dino(3)<Dinu(4) → 2,6,5,1,3,4
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
                print(f"  SKIP  Q{d['question_number']}: question_number already in DB")
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
