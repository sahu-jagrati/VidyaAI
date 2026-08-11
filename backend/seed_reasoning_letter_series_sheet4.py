"""
seed_reasoning_letter_series_sheet4.py
========================================
Seeds Letter Series Q15-Q22 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Letter Series
Run     : python seed_reasoning_letter_series_sheet4.py

Answer key (verified via Python pattern-repeat check):
  Q15  a_ca_c_dc_d_ad_          adc x5                                → B  ddaacc
  Q16  p_rs_qr_pq_spq_s         pqrs x4                               → C  qpsrr
  Q17  bab_aba__a__baa           babaa x3                              → A  ababa
  Q18  b_cd_d_bcc_db_            cyclic-shift blocks (bbcdd/ddbcc/ccdb)→ B  bddcb
  Q19  _dbe_d_ea_bead_e_db_      cyclic adbe period, blocks of 5       → A  a,a,b,d,b,a,e
  Q20  ab_dda_ccd_bb_d_          abcd rotating right 1 each block      → A  cbaca
  Q21  mc_m_a_ca_ca_c_mc         mca x5+partial                        → A  acmmma
  Q22  a_baa_baa_ba              abba x3                               → B  bbb
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Letter_Series_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Letter Series"

QUESTIONS = [
    # ── Q15 ── adc x5 ────────────────────────────────────────────────────────────
    # Full: a d c | a d c | a d c | a d c | a d c
    # Blanks at positions 2,5,7,10,12,15 → fills: d,d,a,a,c,c
    {
        "question_number": 15,
        "difficulty": "easy",
        "question_en": "Complete the letter series: a _ c a _ c _ d c _ d _ a d _",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: a _ c a _ c _ d c _ d _ a d _",
        "option_a": "ddccaa",
        "option_b": "ddaacc",
        "option_c": "ccadad",
        "option_d": "adcadc",
        "correct_answer": "B",   # adc x5 → fills: d,d,a,a,c,c
    },
    # ── Q16 ── pqrs x4 ───────────────────────────────────────────────────────────
    # Full: p q r s | p q r s | p q r s | p q r s
    # Blanks at positions 2,5,8,11,15 → fills: q,p,s,r,r
    {
        "question_number": 16,
        "difficulty": "easy",
        "question_en": "Complete the letter series: p _ r s _ q r _ p q _ s p q _ s",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: p _ r s _ q r _ p q _ s p q _ s",
        "option_a": "pqsrr",
        "option_b": "qrrsp",
        "option_c": "qpsrr",
        "option_d": "prrsq",
        "correct_answer": "C",   # pqrs x4 → fills: q,p,s,r,r
    },
    # ── Q17 ── babaa x3 ──────────────────────────────────────────────────────────
    # Full: b a b a a | b a b a a | b a b a a
    # Blanks at positions 4,8,9,11,12 → fills: a,b,a,b,a
    {
        "question_number": 17,
        "difficulty": "easy",
        "question_en": "Complete the letter series: b a b _ a b a _ _ a _ _ b a a",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: b a b _ a b a _ _ a _ _ b a a",
        "option_a": "ababa",
        "option_b": "baaba",
        "option_c": "babab",
        "option_d": "aaabb",
        "correct_answer": "A",   # babaa x3 → fills: a,b,a,b,a
    },
    # ── Q18 ── cyclic-shift blocks (bbcdd → ddbcc → ccdb..) ──────────────────────
    # Block 1: bbcdd, Block 2: ddbcc, Block 3: ccdbbb
    # Blanks at positions 2,5,7,11,14 → fills: b,d,d,c,b
    {
        "question_number": 18,
        "difficulty": "medium",
        "question_en": "Complete the letter series: b _ c d _ d _ b c c _ d b _",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: b _ c d _ d _ b c c _ d b _",
        "option_a": "cbddb",
        "option_b": "bddcb",
        "option_c": "bddbc",
        "option_d": "cddbb",
        "correct_answer": "B",   # cyclic shift blocks → fills: b,d,d,c,b
    },
    # ── Q19 ── cyclic adbe (period 4), blocks of 5 shifted by 1 ──────────────────
    # Base cycle: a,d,b,e,a,d,b,e,...
    # Block1: adbe a  Block2: dbea d  Block3: bead b  Block4: eadb e
    # Series (20 chars): _dbe_d_ea_bead_e_db_
    # 7 blanks → fills: a,a,b,d,b,a,e
    {
        "question_number": 19,
        "difficulty": "hard",
        "question_en": "Complete the letter series: _ d b e _ d _ e a _ b e a d _ e _ d b _",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: _ d b e _ d _ e a _ b e a d _ e _ d b _",
        "option_a": "a, a, b, d, b, a, e",
        "option_b": "b, b, d, e, a, a, d",
        "option_c": "e, e, b, b, a, d, e",
        "option_d": "a, e, a, d, d, b, e",
        "correct_answer": "A",   # cyclic adbe → fills: a,a,b,d,b,a,e
    },
    # ── Q20 ── abcd rotating right by 1 each block ───────────────────────────────
    # Block1: abcd  Block2: dabc  Block3: cdab  Block4: bcda
    # Series (16 chars): ab_dda_ccd_bb_d_
    # 5 blanks → fills: c,b,a,c,a
    {
        "question_number": 20,
        "difficulty": "medium",
        "question_en": "Complete the letter series: a b _ d d a _ c c d _ b b _ d _",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: a b _ d d a _ c c d _ b b _ d _",
        "option_a": "cbaca",
        "option_b": "cbbed",
        "option_c": "ebeba",
        "option_d": "eeaae",
        "correct_answer": "A",   # abcd rotating blocks → fills: c,b,a,c,a
    },
    # ── Q21 ── mca repeating (5+ groups) ─────────────────────────────────────────
    # Pattern: m c a | m c a | m c a | m c a | m c a | m c
    # Series (17 chars): mc_m_a_ca_ca_c_mc
    # 6 blanks → fills: a,c,m,m,m,a
    {
        "question_number": 21,
        "difficulty": "easy",
        "question_en": "Complete the letter series: m c _ m _ a _ c a _ c a _ c _ m c",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: m c _ m _ a _ c a _ c a _ c _ m c",
        "option_a": "acmmma",
        "option_b": "camcam",
        "option_c": "aaacmm",
        "option_d": "acmmmc",
        "correct_answer": "A",   # mca x5+partial → fills: a,c,m,m,m,a
    },
    # ── Q22 ── abba x3 ───────────────────────────────────────────────────────────
    # Full: a b b a | a b b a | a b b a
    # Series (12 chars): a_baa_baa_ba
    # 3 blanks → fills: b,b,b
    {
        "question_number": 22,
        "difficulty": "easy",
        "question_en": "Complete the letter series: a _ b a a _ b a a _ b a",
        "question_hi": "अक्षर श्रृंखला पूर्ण कीजिए: a _ b a a _ b a a _ b a",
        "option_a": "bab",
        "option_b": "bbb",
        "option_c": "bba",
        "option_d": "aab",
        "correct_answer": "B",   # abba x3 → fills: b,b,b
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
