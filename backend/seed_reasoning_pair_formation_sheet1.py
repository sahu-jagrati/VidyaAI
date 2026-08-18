"""
seed_reasoning_pair_formation_sheet1.py
=========================================
Seeds Pair Formation Q1-Q3 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Pair Formation
Run     : python seed_reasoning_pair_formation_sheet1.py

Rule: count letter-pairs (X, Y) where the number of letters between
them in the WORD equals the number between them in the ENGLISH ALPHABET.
"Both forward and backward" means the check is done both left→right and
right→left through the word; each unordered pair is counted once.

Answer key (verified via Python):
  Q1  HEADINGS   → 2 pairs: D-G (fwd), I-G (bwd)           → C  2
  Q2  DECATHLON  → 4 pairs: D-E(fwd), D-A(bwd), L-N(fwd),  → B  Four
                             N-O(bwd)
  Q3  WILHELMINE → Answer key says 1 (L-M only)             → B  One
      NOTE: algorithmically there are 2 valid pairs (L-M at
      positions 6&7 AND L-E at positions 3&10: 6 letters
      between in both word and alphabet). The source answer
      key appears to overlook the L(3)-E(10) pair. Seeded as
      given (B = One) to match the official answer key.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Pair_Formation_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Pair Formation"

QUESTIONS = [
    # ── Q1 ── HEADINGS: 2 valid pairs (D-G forward, I-G backward) ────────────────
    # HEADINGS: H(1)E(2)A(3)D(4)I(5)N(6)G(7)S(8)  (word positions)
    # Alphabet: H=8,E=5,A=1,D=4,I=9,N=14,G=7,S=19
    # D(pos4)-G(pos7): 2 between in word(I,N); D=4,G=7 → 2 between in alpha(E,F) ✓
    # I(pos5)-G(pos7): 1 between in word(N); I=9,G=7 → 1 between in alpha(H) ✓
    {
        "question_number": 1,
        "difficulty": "medium",
        "question_en": (
            "How many pairs of letters are there in the word 'HEADINGS', which has as many "
            "letters between them in the word (both forward and backward) as in the English "
            "alphabetical series (both forward and backward)?"
        ),
        "question_hi": (
            "शब्द 'HEADINGS' में अक्षरों के ऐसे कितने युग्म हैं, जिनके बीच शब्द "
            "(आगे और पीछे दोनों) में उतने ही अक्षर हैं, जितने कि अंग्रेजी वर्णमाला "
            "श्रृंखला (आगे और पीछे दोनों) में हैं?"
        ),
        "option_a": "3",
        "option_b": "0",
        "option_c": "2",
        "option_d": "1",
        "correct_answer": "C",   # 2 pairs: D-G (forward), I-G (backward)
    },
    # ── Q2 ── DECATHLON: 4 valid pairs ───────────────────────────────────────────
    # DECATHLON: D(1)E(2)C(3)A(4)T(5)H(6)L(7)O(8)N(9)  (word positions)
    # Alphabet: D=4,E=5,C=3,A=1,T=20,H=8,L=12,O=15,N=14
    # D(pos1)-E(pos2): 0 between in word; D=4,E=5 → 0 between in alpha ✓ (fwd)
    # L(pos7)-N(pos9): 1 between(O); L=12,N=14 → 1 between in alpha(M) ✓ (fwd)
    # O(pos8)-N(pos9): 0 between; O=15,N=14 → 0 between ✓ (bwd: N before O)
    # D(pos1)-A(pos4): 2 between(E,C); A=1,D=4 → 2 between(B,C) ✓ (bwd: A before D)
    {
        "question_number": 2,
        "difficulty": "medium",
        "question_en": (
            "How many pairs of letters are there in the word 'DECATHLON' which has as many "
            "letters between them in the word, in both the forward direction as well as "
            "backward direction, as in English alphabetical series?"
        ),
        "question_hi": (
            "शब्द 'DECATHLON' में अक्षरों के ऐसे कितने युग्म हैं, जिनके बीच आगे और "
            "पीछे दोनों दिशाओं में शब्दों के बीच उतने ही अक्षर हैं, जितने कि अंग्रेजी "
            "वर्णमाला में होते हैं?"
        ),
        "option_a": "Five/पाँच",
        "option_b": "Four/चार",
        "option_c": "Three/तीन",
        "option_d": "Two/दो",
        "correct_answer": "B",   # 4 pairs: D-E(fwd), L-N(fwd), N-O(bwd), A-D(bwd)
    },
    # ── Q3 ── WILHELMINE: answer key says 1 pair (L-M) ───────────────────────────
    # WILHELMINE: W(1)I(2)L(3)H(4)E(5)L(6)M(7)I(8)N(9)E(10)  (word positions)
    # Alphabet: W=23,I=9,L=12,H=8,E=5,M=13,N=14
    # L(pos6)-M(pos7): 0 between in word; L=12,M=13 → 0 between in alpha ✓ (fwd)
    # Note: L(pos3)-E(pos10) also yields 6 between in word and 6 in alpha — the
    #       source answer key does not count this pair; seeded as official answer.
    {
        "question_number": 3,
        "difficulty": "medium",
        "question_en": (
            "How many pairs of letters are there in the word 'WILHELMINE', each of which "
            "has as many letters between (in both forward and backward direction) them in "
            "the word as they have between them in the English alphabet?"
        ),
        "question_hi": (
            "'WILHELMINE' शब्द में कितने जोड़े हैं, जिनमें से प्रत्येक के बीच उतने ही "
            "अक्षर हैं (आगे और पीछे दोनों दिशाओं में) जितने उनके बीच अंग्रेजी वर्णमाला "
            "में हैं?"
        ),
        "option_a": "Two/दो",
        "option_b": "One/एक",
        "option_c": "Four/चार",
        "option_d": "None/कोई नहीं",
        "correct_answer": "B",   # Official answer: 1 pair (L-M at positions 6&7)
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
