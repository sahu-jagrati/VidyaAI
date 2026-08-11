"""
seed_reasoning_letter_series_sheet1.py
========================================
Seeds Letter Series Q1-Q7 (Set 1) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Letter Series
Run     : python seed_reasoning_letter_series_sheet1.py

Fill-in-the-blank letter series — find the repeating pattern.

Answer key (verified via Python pattern-repeat check):
  Q1  a _ ba _ bb _ ab _ a       pattern abba x3     → B  baab
  Q2  _ ab _ b _ aba _ _ abab    pattern aabab x3    → D  a aa ba
  Q3  m _ nm _ n _ an _ a _ ma _ pattern man x5      → B  aammnn
  Q4  _ _ aab _ a _ a _ ba       pattern aba x4      → C  ababa
  Q5  r _ sr _ tsrrt _ rr _ sr   pattern rtsr x4     → C  trst
  Q6  _ tu _ rt _ s _ _ us rtu _ pattern rtus x4     → A  rsurts
  Q7  _ nmmn _ mmnn _ mnnm _     pattern nnmm x4     → A  nnmm
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Letter_Series_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Letter Series"

QUESTIONS = [
    # ── Q1 ── abba x3 ────────────────────────────────────────────────────────────
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": "Complete the letter series: a _ ba _ bb _ ab _ a",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: a _ ba _ bb _ ab _ a",
        "option_a": "aaba",
        "option_b": "baab",
        "option_c": "baaa",
        "option_d": "abab",
        "correct_answer": "B",   # abba abba abba → fills: b,a,a,b
    },
    # ── Q2 ── aabab x3 ───────────────────────────────────────────────────────────
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": "Complete the letter series: _ ab _ b _ aba _ _ abab",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: _ ab _ b _ aba _ _ abab",
        "option_a": "a bb aa",
        "option_b": "bb aa b",
        "option_c": "ab aa b",
        "option_d": "a aa ba",
        "correct_answer": "D",   # aabab aabab aabab → fills: a,a,a,b,a
    },
    # ── Q3 ── man x5 ─────────────────────────────────────────────────────────────
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": "Complete the letter series: m _ nm _ n _ an _ a _ ma _",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: m _ nm _ n _ an _ a _ ma _",
        "option_a": "amammn",
        "option_b": "aammnn",
        "option_c": "ammanm",
        "option_d": "aamnan",
        "correct_answer": "B",   # man man man man man → fills: a,a,m,m,n,n
    },
    # ── Q4 ── aba x4 ─────────────────────────────────────────────────────────────
    {
        "question_number": 4,
        "difficulty": "easy",
        "question_en": "Complete the letter series: _ _ aab _ a _ a _ ba",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: _ _ aab _ a _ a _ ba",
        "option_a": "bbaab",
        "option_b": "aaabb",
        "option_c": "ababa",
        "option_d": "babab",
        "correct_answer": "C",   # aba aba aba aba → fills: a,b,a,b,a
    },
    # ── Q5 ── rtsr x4 ────────────────────────────────────────────────────────────
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": "Complete the letter series: r _ sr _ tsrrt _ rr _ sr",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: r _ sr _ tsrrt _ rr _ sr",
        "option_a": "ttss",
        "option_b": "tsts",
        "option_c": "trst",
        "option_d": "sstt",
        "correct_answer": "C",   # rtsr rtsr rtsr rtsr → fills: t,r,s,t
    },
    # ── Q6 ── rtus x4 ────────────────────────────────────────────────────────────
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": "Complete the letter series: _ tu _ rt _ s _ _ us rtu _",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: _ tu _ rt _ s _ _ us rtu _",
        "option_a": "rsurts",
        "option_b": "rsurtr",
        "option_c": "rsutrr",
        "option_d": "rtusru",
        "correct_answer": "A",   # rtus rtus rtus rtus → fills: r,s,u,r,t,s
    },
    # ── Q7 ── nnmm x4 ────────────────────────────────────────────────────────────
    {
        "question_number": 7,
        "difficulty": "easy",
        "question_en": "Complete the letter series: _ nmmn _ mmnn _ mnnm _",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: _ nmmn _ mmnn _ mnnm _",
        "option_a": "n n m m",
        "option_b": "n m n m",
        "option_c": "m n n m",
        "option_d": "n m m n",
        "correct_answer": "A",   # nnmm nnmm nnmm nnmm → fills: n,n,m,m
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
