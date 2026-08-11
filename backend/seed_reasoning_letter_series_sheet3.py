"""
seed_reasoning_letter_series_sheet3.py
========================================
Seeds Letter Series Q8-Q14 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Letter Series
Run     : python seed_reasoning_letter_series_sheet3.py

Answer key (verified via Python pattern-repeat check):
  Q8   mnonopqopqrs______         increasing groups (3→4→5→6 letters)    → C  pqrstu
  Q9   b_ccacca_ba_bbc_bc_a       cyclic shift of 5-letter block bbcca    → A  baabc
  Q10  _op_mo_n__pnmop_           mopn x4                                 → A  mnpmon
  Q11  _tu_rt_s__usrtu_           rtus x4  [DUPLICATE of Sheet1 Q6]       → D  rsurts
  Q12  m_ommn_m_nommn_m           mnommnom x2                             → B  nomo
  Q13  _sr_tr_srs_r_srst_         tsrstr x3                               → D  tstttr
  Q14  gfe_ig_eii_fei_gf_ii       gfeii x4                                → A  ifgie

NOTE: Q11 is a duplicate of Q6 from Sheet1 (same series, different option order).
      It will be automatically skipped by the dedup check.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Letter_Series_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Letter Series"

QUESTIONS = [
    # ── Q8 ── consecutive groups 3→4→5→6 letters ─────────────────────────────────
    # mno | nopq | opqrs | pqrstu  → fill 6 blanks = pqrstu
    {
        "question_number": 8,
        "difficulty": "medium",
        "question_en": "Complete the letter series: m n o n o p q o p q r s _ _ _ _ _ _",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: m n o n o p q o p q r s _ _ _ _ _ _",
        "option_a": "mnopqr",
        "option_b": "opqrst",
        "option_c": "pqrstu",
        "option_d": "oqrstu",
        "correct_answer": "C",   # groups mno/nopq/opqrs/pqrstu
    },
    # ── Q9 ── cyclic shift of 5-letter block bbcca ───────────────────────────────
    # bbcca | ccaab | aabbc | bbcca → fills at blanks = b,a,a,b,c
    {
        "question_number": 9,
        "difficulty": "hard",
        "question_en": "Complete the letter series: b _ c c a c c a _ b a _ b b c _ b c _ a",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: b _ c c a c c a _ b a _ b b c _ b c _ a",
        "option_a": "baabc",
        "option_b": "abaaa",
        "option_c": "acbca",
        "option_d": "bacab",
        "correct_answer": "A",   # cyclic shift bbcca → ccaab → aabbc → bbcca
    },
    # ── Q10 ── mopn x4 ──────────────────────────────────────────────────────────
    {
        "question_number": 10,
        "difficulty": "medium",
        "question_en": "Complete the letter series: _ o p _ m o _ n _ _ p n m o p _",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: _ o p _ m o _ n _ _ p n m o p _",
        "option_a": "mnpmon",
        "option_b": "mpnmop",
        "option_c": "mnompn",
        "option_d": "mnpomn",
        "correct_answer": "A",   # mopn mopn mopn mopn → fills: m,n,p,m,o,n
    },
    # ── Q11 ── rtus x4  [DUPLICATE of Sheet1 Q6 — will be skipped] ──────────────
    {
        "question_number": 11,
        "difficulty": "medium",
        "question_en": "Complete the letter series: _ tu _ rt _ s _ _ us rtu _",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: _ tu _ rt _ s _ _ us rtu _",
        "option_a": "rtusru",
        "option_b": "rsurtr",
        "option_c": "rsutrr",
        "option_d": "rsurts",
        "correct_answer": "D",   # rtus x4 → fills: r,s,u,r,t,s  [already in DB as Sheet1 Q6]
    },
    # ── Q12 ── mnommnom x2 ──────────────────────────────────────────────────────
    {
        "question_number": 12,
        "difficulty": "medium",
        "question_en": "Complete the letter series: m _ o m m n _ m _ n o m m n _ m",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: m _ o m m n _ m _ n o m m n _ m",
        "option_a": "onmo",
        "option_b": "nomo",
        "option_c": "monm",
        "option_d": "nnmo",
        "correct_answer": "B",   # mnommnom x2 → fills: n,o,m,o
    },
    # ── Q13 ── tsrstr x3 ────────────────────────────────────────────────────────
    {
        "question_number": 13,
        "difficulty": "hard",
        "question_en": "Complete the letter series: _ s r _ t r _ s r s _ r _ s r s t _",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: _ s r _ t r _ s r s _ r _ s r s t _",
        "option_a": "ttssrr",
        "option_b": "tsrtsr",
        "option_c": "strtrs",
        "option_d": "tstttr",
        "correct_answer": "D",   # tsrstr x3 → fills: t,s,t,t,t,r
    },
    # ── Q14 ── gfeii x4 ─────────────────────────────────────────────────────────
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": "Complete the letter series: g f e _ i g _ e i i _ f e i _ g f _ i i",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: g f e _ i g _ e i i _ f e i _ g f _ i i",
        "option_a": "ifgie",
        "option_b": "igife",
        "option_c": "fgiie",
        "option_d": "egfii",
        "correct_answer": "A",   # gfeii x4 → fills: i,f,g,i,e
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
