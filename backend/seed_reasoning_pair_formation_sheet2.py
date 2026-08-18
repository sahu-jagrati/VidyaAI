"""
seed_reasoning_pair_formation_sheet2.py
=========================================
Updates Q14 (already in DB) and seeds Q15-Q21.
Subject : Reasoning
Topic   : Pair Formation
Run     : python seed_reasoning_pair_formation_sheet2.py

Answer key:
  Q14  5321648 ascending sort         only 8 stays at pos 7          → B  One
  Q15  MEDITATION (1 less than alpha) official: 3 pairs (M-T,E-N,I-O) → A  3
       NOTE: 6 pairs found algorithmically; answer key lists only 3.
  Q16  DIPLOMAT (2 less than alpha)   2 pairs (L-O, O-T)             → A  2
  Q17  MEDITATION (2 more than alpha) 1 pair (E-I); T-T excluded     → A  1
  Q18  DIPLOMAT (1 more than alpha)   3 pairs (P-O,P-T,L-M)          → B  3
  Q19  SPIRITUAL rearranged→SIIUPLRAT 5 pairs                         → C  5
  Q20  5834619 digit pairs (asc)      4 pairs                         → D  4
  Q21  21467589 digit pairs (asc)     7 pairs                         → D  7
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Pair_Formation_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Pair Formation"

# ── Q14 is already in DB with no answer — update it, don't re-insert ────────
Q14_UPDATE = {
    "question_hi": (
        'संख्या 5321648 में ऐसे कितने अंक हैं, जो संख्या में आरंभ से उतने ही दूर हैं '
        'जितना कि अंकों को आरोही क्रम में व्यवस्थित करने पर रहते हैं?'
    ),
    "option_a": "None/कोई नहीं",
    "option_b": "One/एक",
    "option_c": "Two/दो",
    "option_d": "Three/तीन",
    "correct_answer": "B",   # only 8 stays at position 7 after ascending sort
}

# ── New questions Q15-Q21 ────────────────────────────────────────────────────
NEW_QUESTIONS = [
    # ── Q15 ── MEDITATION: 1 less than alphabet between ──────────────────────
    # N_word = N_alpha - 1; official answer 3 pairs: M-T(5=6-1), E-N(7=8-1), I-O(4=5-1)
    # NOTE: 6 pairs valid algorithmically; answer key lists only 3
    {
        "question_number": 15,
        "difficulty": "medium",
        "question_en": (
            "How many pairs of letters are there in the word 'MEDITATION' which have "
            "1 less than the number of letters between them as in the English alphabetical order?"
        ),
        "question_hi": (
            "शब्द 'MEDITATION' में ऐसे कितने अक्षर युग्म हैं जिनके बीच में "
            "अंग्रेजी वर्णमाला क्रम से एक कम अक्षर आते हैं?"
        ),
        "option_a": "3",
        "option_b": "4",
        "option_c": "2",
        "option_d": "5",
        "correct_answer": "A",   # official: 3 pairs (M-T, E-N, I-O)
    },
    # ── Q16 ── DIPLOMAT: 2 less than alphabet between ─────────────────────────
    # N_word = N_alpha - 2; 2 pairs: L-O(0=2-2), O-T(2=4-2)
    {
        "question_number": 16,
        "difficulty": "medium",
        "question_en": (
            "How many pairs of letters are there in the word 'DIPLOMAT' which have "
            "2 less than the number of letters between them as in the English alphabetical order?"
        ),
        "question_hi": (
            "शब्द 'DIPLOMAT' में ऐसे कितने अक्षर युग्म हैं जिनके बीच में "
            "अंग्रेजी वर्णमाला क्रम से दो कम अक्षर आते हैं?"
        ),
        "option_a": "2",
        "option_b": "1",
        "option_c": "3",
        "option_d": "4",
        "correct_answer": "A",   # 2 pairs: L-O(pos4,5), O-T(pos5,8)
    },
    # ── Q17 ── MEDITATION: 2 more than alphabet between ──────────────────────
    # N_word = N_alpha + 2; 1 pair: E-I(5=3+2) [T-T excluded as same letter]
    {
        "question_number": 17,
        "difficulty": "medium",
        "question_en": (
            "How many pairs of letters are there in the word 'MEDITATION' which have "
            "2 more than the number of letters between them as in the English alphabetical order?"
        ),
        "question_hi": (
            "शब्द 'MEDITATION' में ऐसे कितने अक्षर युग्म हैं जिनके बीच में "
            "अंग्रेजी वर्णमाला क्रम से 2 ज्यादा अक्षर आते हैं?"
        ),
        "option_a": "1",
        "option_b": "2",
        "option_c": "3",
        "option_d": "4",
        "correct_answer": "A",   # 1 pair: E(pos2)-I(pos8) word=5, alpha=3
    },
    # ── Q18 ── DIPLOMAT: 1 more than alphabet between ─────────────────────────
    # N_word = N_alpha + 1; 3 pairs: P-O(1=0+1), P-T(4=3+1), L-M(1=0+1)
    {
        "question_number": 18,
        "difficulty": "medium",
        "question_en": (
            "How many pairs of letters are there in the word 'DIPLOMAT' which have "
            "1 more than the number of letters between them as in the English alphabetical order?"
        ),
        "question_hi": (
            "शब्द 'DIPLOMAT' में ऐसे कितने अक्षर युग्म हैं जिनके बीच में "
            "अंग्रेजी वर्णमाला क्रम से एक ज्यादा अक्षर आते हैं?"
        ),
        "option_a": "4",
        "option_b": "3",
        "option_c": "1",
        "option_d": "2",
        "correct_answer": "B",   # 3 pairs: P-O(pos3,5), P-T(pos3,8), L-M(pos4,6)
    },
    # ── Q19 ── SPIRITUAL rearranged → SIIUPLRAT ───────────────────────────────
    # Swaps: 2↔5 (P↔I), 4↔7 (R↔U), 6↔9 (T↔L) → New word: SIIUPLRAT
    # 5 pairs: I(3)-L(6), U(4)-R(7), P(5)-R(7), P(5)-T(9), R(7)-T(9)
    {
        "question_number": 19,
        "difficulty": "hard",
        "question_en": (
            "If in the word 'SPIRITUAL', position of second and fifth letter is interchanged, "
            "similarly position of fourth and sixth letter is interchanged with seventh and ninth "
            "letters respectively, then how many pair of letters in the new word have as many "
            "letters between them (either forward or backward) as they have in the English alphabet series?"
        ),
        "question_hi": (
            "यदि शब्द 'SPIRITUAL' में दूसरे और पाँचवें अक्षर का स्थान आपस में बदल दिया "
            "जाता है, इसी प्रकार चौथे और छठे अक्षर का स्थान क्रमशः सातवें और नौवें अक्षर "
            "से बदल दिया जाता है, तो नए शब्द में अक्षरों की कितनी जोड़ियों के बीच उतने ही "
            "अक्षर हैं (या तो आगे या पीछे) जितने कि अंग्रेजी वर्णमाला श्रृंखला में हैं?"
        ),
        "option_a": "6",
        "option_b": "4",
        "option_c": "5",
        "option_d": "3",
        "correct_answer": "C",   # 5 pairs in new word SIIUPLRAT
    },
    # ── Q20 ── 5834619: digit pairs with same distance in orig & ascending ────
    # Orig: 5(1)8(2)3(3)4(4)6(5)1(6)9(7)  Asc: 1(1)3(2)4(3)5(4)6(5)8(6)9(7)
    # 4 pairs: (5,3)d=2, (3,4)d=1, (4,1)d=2, (6,9)d=2
    {
        "question_number": 20,
        "difficulty": "hard",
        "question_en": (
            "How many pairs of digits in number '5834619' are such, which contain the same "
            "number of digits between them, as they have between them when the digits are "
            "arranged in the ascending order?"
        ),
        "question_hi": (
            "'5834619' में ऐसे कितने अंकों के युग्म हैं, जिनके बीच में उतने ही "
            "अंक आते हैं, जितने इन्हें आरोही क्रम में व्यवस्थित करने पर हों?"
        ),
        "option_a": "1",
        "option_b": "2",
        "option_c": "3",
        "option_d": "4",
        "correct_answer": "D",   # 4 pairs: (5,3)d=2, (3,4)d=1, (4,1)d=2, (6,9)d=2
    },
    # ── Q21 ── 21467589: digit pairs with same distance in orig & ascending ───
    # Orig: 2(1)1(2)4(3)6(4)7(5)5(6)8(7)9(8)  Asc: 1(1)2(2)4(3)5(4)6(5)7(6)8(7)9(8)
    # 7 pairs: (2,1)d=1, (2,6)d=3, (2,7)d=4, (4,8)d=4, (4,9)d=5, (6,7)d=1, (8,9)d=1
    {
        "question_number": 21,
        "difficulty": "hard",
        "question_en": (
            "How many pairs of digits in number '21467589' are such, which contain the same "
            "number of digits between them, as they have between them when the digits are "
            "arranged in the ascending order?"
        ),
        "question_hi": (
            "'21467589' में ऐसे कितने अंकों के युग्म हैं, जिनके बीच में उतने ही "
            "अंक आते हैं, जितने इन्हें आरोही क्रम में व्यवस्थित करने पर हों?"
        ),
        "option_a": "6",
        "option_b": "10",
        "option_c": "8",
        "option_d": "7",
        "correct_answer": "D",   # 7 pairs verified
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = updated = 0
    try:
        # ── Update Q14 ───────────────────────────────────────────────────────
        q14 = db.query(Question).filter(
            Question.topic == TOPIC,
            Question.subject == SUBJECT,
            Question.question_number == 14,
        ).first()
        if q14 and q14.correct_answer is None:
            for field, value in Q14_UPDATE.items():
                setattr(q14, field, value)
            print("  Updated Q14: correct_answer=B (One)")
            updated += 1
        elif q14:
            print(f"  Q14 already answered ({q14.correct_answer}), skipping update")
        else:
            print("  Q14 not found in DB")

        # ── Insert Q15-Q21 ───────────────────────────────────────────────────
        existing_short = {
            row[0][:80]
            for row in db.query(Question.question_en)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        for d in NEW_QUESTIONS:
            fp = d["question_en"][:80]
            if fp in existing_short:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
            inserted += 1

        db.commit()
        print(f"\nDone -- updated: {updated}, inserted: {inserted}, skipped: {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
