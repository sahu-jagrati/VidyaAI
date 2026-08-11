"""
seed_reasoning_letter_series_sheet2.py
========================================
Seeds Letter Series Q1-Q7 (Set 2) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Letter Series
Run     : python seed_reasoning_letter_series_sheet2.py

Answer key (verified via Python pattern-repeat check):
  Q1  _ aa _ ba _ bb _ ab _ aab    pattern baab x4     → C  bbaab
  Q2  _ stt _ tt _ tts _           pattern tst x4      → A  tsst
  Q3  qst _ qs _ rq _ tr _ str     pattern qstr x4     → B  rtsq
  Q4  a _ a _ bbaa _ bbba _ a      pattern aaabbb x2.5 → B  abaa
  Q5  l _ b _ ub _ ubt _ blu _ tub pattern lubtub x3   → B  utlub
  Q6  _ bcab _ cabc _ abca _ b     cyclic abcab shift   → D  abca
  Q7  _ ba _ bab _ bb _ b          increasing b's       → B  abbb
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Letter_Series_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Letter Series"

QUESTIONS = [
    # ── Q1 ── baab x4 ────────────────────────────────────────────────────────────
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": "Complete the letter series: _ aa _ ba _ bb _ ab _ aab",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: _ aa _ ba _ bb _ ab _ aab",
        "option_a": "babab",
        "option_b": "aaabb",
        "option_c": "bbaab",
        "option_d": "bbbaa",
        "correct_answer": "C",   # baab baab baab baab → fills: b,b,a,a,b
    },
    # ── Q2 ── tst x4 ─────────────────────────────────────────────────────────────
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": "Complete the letter series: _ stt _ tt _ tts _",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: _ stt _ tt _ tts _",
        "option_a": "tsst",
        "option_b": "sstt",
        "option_c": "ttst",
        "option_d": "tsts",
        "correct_answer": "A",   # tst tst tst tst → fills: t,s,s,t
    },
    # ── Q3 ── qstr x4 ────────────────────────────────────────────────────────────
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": "Complete the letter series: qst _ qs _ rq _ tr _ str",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: qst _ qs _ rq _ tr _ str",
        "option_a": "sqtr",
        "option_b": "rtsq",
        "option_c": "trqs",
        "option_d": "tsrq",
        "correct_answer": "B",   # qstr qstr qstr qstr → fills: r,t,s,q
    },
    # ── Q4 ── aaabbb x2 ──────────────────────────────────────────────────────────
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": "Complete the letter series: a _ a _ bbaa _ bbba _ a",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: a _ a _ bbaa _ bbba _ a",
        "option_a": "aabb",
        "option_b": "abaa",
        "option_c": "abab",
        "option_d": "aaab",
        "correct_answer": "B",   # aaabbb aaabbb aaa → fills: a,b,a,a
    },
    # ── Q5 ── lubtub x3 ──────────────────────────────────────────────────────────
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": "Complete the letter series: l _ b _ ub _ ubt _ blu _ tub",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: l _ b _ ub _ ubt _ blu _ tub",
        "option_a": "ubtlu",
        "option_b": "utlub",
        "option_c": "tulbu",
        "option_d": "butlu",
        "correct_answer": "B",   # lubtub lubtub lubtub → fills: u,t,l,u,b
    },
    # ── Q6 ── cyclic abcab shift ──────────────────────────────────────────────────
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": "Complete the letter series: _ bcab _ cabc _ abca _ b",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: _ bcab _ cabc _ abca _ b",
        "option_a": "aabc",
        "option_b": "bbca",
        "option_c": "abac",
        "option_d": "abca",
        "correct_answer": "D",   # abcab|bcabc|cabca|ab → fills: a,b,c,a
    },
    # ── Q7 ── increasing b's after a ─────────────────────────────────────────────
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": "Complete the letter series: _ ba _ bab _ bb _ b",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: _ ba _ bab _ bb _ b",
        "option_a": "baaa",
        "option_b": "abbb",
        "option_c": "babb",
        "option_d": "abab",
        "correct_answer": "B",   # ab|abb|abbb|abbbb → fills: a,b,b,b
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
