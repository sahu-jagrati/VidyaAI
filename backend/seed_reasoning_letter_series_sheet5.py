"""
seed_reasoning_letter_series_sheet5.py
========================================
Seeds Letter Series Q23-Q30 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Letter Series
Run     : python seed_reasoning_letter_series_sheet5.py

Answer key (verified via Python pattern-repeat check):
  Q23  _bac_ac_acb__ba          cba x5                                → A  cbbac
  Q24  b_aacba_bca_cb_a_caa     alternating blocks bcaa/cbaa x5       → C  caaab
  Q25  ba_abab_b_ba_aba          baba x4                               → C  baab
  Q26  a_b_e_a_be_b_eb           aebeeb x2.5 (period 6: a,e,b,e,e,b)  → A  eebeea
  Q27  _ab_b_bc_ca_              rotating 3-letter blocks cab/abc/bca  → C  cacab
  Q28  b_ab_b_aab_b              blocks alternating aa/bb middles      → C  aabb
  Q29  ac_c_cb_acbcacbca_bc      acbc x5                               → B  bacc
  Q30  _bcab_cabc_abca_b         rotating 5-letter blocks abcab shift  → D  abca
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Letter_Series_Sheet5"
SUBJECT = "Reasoning"
TOPIC   = "Letter Series"

QUESTIONS = [
    # ── Q23 ── cba x5 ────────────────────────────────────────────────────────────
    # Full: c b a | c b a | c b a | c b a | c b a
    # Blanks at positions 1,5,8,12,13 → fills: c,b,b,a,c
    {
        "question_number": 23,
        "difficulty": "easy",
        "question_en": "Complete the letter series: _ b a c _ a c _ a c b _ _ b a",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: _ b a c _ a c _ a c b _ _ b a",
        "option_a": "cbbac",
        "option_b": "abbac",
        "option_c": "cabbc",
        "option_d": "accbb",
        "correct_answer": "A",   # cba x5 → fills: c,b,b,a,c
    },
    # ── Q24 ── alternating blocks bcaa / cbaa (5 blocks x 4 = 20 chars) ──────────
    # Block1: bcaa  Block2: cbaa  Block3: bcaa  Block4: cbaa  Block5: bcaa
    # Blanks at positions 2,8,12,15,17 → fills: c,a,a,a,b
    {
        "question_number": 24,
        "difficulty": "medium",
        "question_en": "Complete the letter series: b _ a a c b a _ b c a _ c b _ a _ c a a",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: b _ a a c b a _ b c a _ c b _ a _ c a a",
        "option_a": "cabab",
        "option_b": "babcb",
        "option_c": "caaab",
        "option_d": "cabac",
        "correct_answer": "C",   # alternating bcaa/cbaa → fills: c,a,a,a,b
    },
    # ── Q25 ── baba x4 ───────────────────────────────────────────────────────────
    # Full: b a b a | b a b a | b a b a | b a b a
    # Blanks at positions 3,8,10,13 → fills: b,a,a,b
    {
        "question_number": 25,
        "difficulty": "easy",
        "question_en": "Complete the letter series: b a _ a b a b _ b _ b a _ a b a",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: b a _ a b a b _ b _ b a _ a b a",
        "option_a": "abab",
        "option_b": "aabb",
        "option_c": "baab",
        "option_d": "bbaa",
        "correct_answer": "C",   # baba x4 → fills: b,a,a,b
    },
    # ── Q26 ── aebeeb x2.5 (period-6 block: a,e,b,e,e,b) ────────────────────────
    # Full: a e b e e b | a e b e e b | a e b
    # Blanks at positions 2,4,6,8,11,13 → fills: e,e,b,e,e,a
    {
        "question_number": 26,
        "difficulty": "medium",
        "question_en": "Complete the letter series: a _ b _ e _ a _ b e _ b _ e b",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: a _ b _ e _ a _ b e _ b _ e b",
        "option_a": "eebeea",
        "option_b": "eeaeeb",
        "option_c": "caeabe",
        "option_d": "aebeab",
        "correct_answer": "A",   # aebeeb x2.5 → fills: e,e,b,e,e,a
    },
    # ── Q27 ── rotating 3-letter blocks: cab → abc → bca → cab ──────────────────
    # Block1: cab  Block2: abc  Block3: bca  Block4: cab
    # Blanks at positions 1,4,6,9,12 → fills: c,a,c,a,b
    {
        "question_number": 27,
        "difficulty": "medium",
        "question_en": "Complete the letter series: _ a b _ b _ b c _ c a _",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: _ a b _ b _ b c _ c a _",
        "option_a": "accbb",
        "option_b": "abcca",
        "option_c": "cacab",
        "option_d": "abacb",
        "correct_answer": "C",   # rotating cab/abc/bca → fills: c,a,c,a,b
    },
    # ── Q28 ── alternating aa/bb middles: baab / aabb / abbb ─────────────────────
    # Blanks at positions 2,5,7,11 → fills: a,a,b,b
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": "Complete the letter series: b _ a b _ b _ a a b _ b",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: b _ a b _ b _ a a b _ b",
        "option_a": "abba",
        "option_b": "baaa",
        "option_c": "aabb",
        "option_d": "abbb",
        "correct_answer": "C",   # alternating aa/bb blocks → fills: a,a,b,b
    },
    # ── Q29 ── acbc x5 ───────────────────────────────────────────────────────────
    # Full: a c b c | a c b c | a c b c | a c b c | a c b c
    # Blanks at positions 3,5,8,18 → fills: b,a,c,c
    {
        "question_number": 29,
        "difficulty": "easy",
        "question_en": "Complete the letter series: a c _ c _ c b _ a c b c a c b c a _ b c",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: a c _ c _ c b _ a c b c a c b c a _ b c",
        "option_a": "abbb",
        "option_b": "bacc",
        "option_c": "babc",
        "option_d": "bbcc",
        "correct_answer": "B",   # acbc x5 → fills: b,a,c,c
    },
    # ── Q30 ── rotating 5-letter blocks: abcab → bcabc → cabca → abcab ──────────
    # Blanks at positions 1,6,11,16 → fills: a,b,c,a
    {
        "question_number": 30,
        "difficulty": "medium",
        "question_en": "Complete the letter series: _ b c a b _ c a b c _ a b c a _ b",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: _ b c a b _ c a b c _ a b c a _ b",
        "option_a": "aabc",
        "option_b": "bbca",
        "option_c": "abac",
        "option_d": "abca",
        "correct_answer": "D",   # rotating abcab/bcabc/cabca → fills: a,b,c,a
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
