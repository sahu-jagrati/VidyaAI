"""
seed_reasoning_jumbling_sheet1.py
====================================
Seeds Jumbled-Word questions Q17-Q26 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Jumbling
Run     : python seed_reasoning_jumbling_sheet1.py

Two question sub-types:
  Type 1 (Q17-Q23): Letters are numbered; find the correct positional order.
  Type 2 (Q24-Q26): Letters assigned number codes; find permutation that forms a word.

Answer key (verified via Python positional decode):
  Q17  C(1)I(2)O(3)C(4)D(5)L(6)Y(7)P(8)E(9)N(10)E(11)A(12)  → B (ENCYCLOPEDIA)
  Q18  N(1)D(2)I(3)O(4)I(5)T(6)C(7)A(8)R(9)                  → C (INDICATOR)
  Q19  A(1)O(2)U(3)T(4)Q(5)I(6)E(7)N(8)                       → C (EQUATION)
  Q20  N(1)T(2)I(3)V(4)A(5)A(6)I(7)R(8)O(9)                  → C (VARIATION)
  Q21  E(1)R(2)R(3)A(4)T(5)N(6)S(7)G(8)                       → B (STRANGER)
  Q22  O(1)R(2)S(3)P(4)N(5)I(6)                               → B (PRISON)
  Q23  S(1)A(2)B(3)I(4)T(5)S(6)L(7)H(8)                      → C (STABLISH)
  Q24  E=1,N=2,T=3,S=4,T=5,D=6,U=7                            → B (STUDENT)
  Q25  L=1,P=2,C=3,E=4,I=5,N=6                                 → B (PENCIL)
  Q26  E=1,Z=2,L=3,P=4,U=5,Z=6                                 → D (PUZZLE)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Jumbling_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Jumbling"

QUESTIONS = [
    # ── Q17 ── ENCYCLOPEDIA ──────────────────────────────────────────────────────
    {
        "question_number": 17,
        "difficulty": "medium",
        "question_en": (
            "Letters numbered: C(1) I(2) O(3) C(4) D(5) L(6) Y(7) P(8) E(9) N(10) E(11) A(12). "
            "Select order to form a meaningful word."
        ),
        "question_hi": (
            "अक्षरों को संख्याबद्ध किया गया है: C(1) I(2) O(3) C(4) D(5) L(6) Y(7) P(8) E(9) N(10) E(11) A(12). "
            "एक सार्थक शब्द बनाने के लिए सही क्रम चुनिए।"
        ),
        "option_a": "9,12,11,1,6,7,8,10,3,5,2,4",
        "option_b": "11,10,1,7,4,6,3,8,9,5,2,12",
        "option_c": "11,10,1,3,7,4,6,8,9,2,5,12",
        "option_d": "10,1,5,2,8,9,7,3,4,12,11,6",
        "correct_answer": "B",   # → ENCYCLOPEDIA
    },
    # ── Q18 ── INDICATOR ─────────────────────────────────────────────────────────
    {
        "question_number": 18,
        "difficulty": "easy",
        "question_en": (
            "Letters numbered: N(1) D(2) I(3) O(4) I(5) T(6) C(7) A(8) R(9). "
            "Select order to form a meaningful word."
        ),
        "question_hi": (
            "अक्षरों को संख्याबद्ध किया गया है: N(1) D(2) I(3) O(4) I(5) T(6) C(7) A(8) R(9). "
            "एक सार्थक शब्द बनाने के लिए सही क्रम चुनिए।"
        ),
        "option_a": "5,2,1,9,8,4,3,7,6",
        "option_b": "4,9,1,3,2,8,6,7,5",
        "option_c": "5,1,2,3,7,8,6,4,9",
        "option_d": "2,5,1,8,7,3,4,6,9",
        "correct_answer": "C",   # → INDICATOR
    },
    # ── Q19 ── EQUATION ──────────────────────────────────────────────────────────
    {
        "question_number": 19,
        "difficulty": "easy",
        "question_en": (
            "Letters numbered: A(1) O(2) U(3) T(4) Q(5) I(6) E(7) N(8). "
            "Select order to form a meaningful word."
        ),
        "question_hi": (
            "अक्षरों को संख्याबद्ध किया गया है: A(1) O(2) U(3) T(4) Q(5) I(6) E(7) N(8). "
            "एक सार्थक शब्द बनाने के लिए सही क्रम चुनिए।"
        ),
        "option_a": "7,3,5,1,6,2,8,4",
        "option_b": "3,7,5,8,1,2,4,6",
        "option_c": "7,5,3,1,4,6,2,8",
        "option_d": "5,1,3,4,2,7,6,8",
        "correct_answer": "C",   # → EQUATION
    },
    # ── Q20 ── VARIATION ─────────────────────────────────────────────────────────
    {
        "question_number": 20,
        "difficulty": "easy",
        "question_en": (
            "Letters numbered: N(1) T(2) I(3) V(4) A(5) A(6) I(7) R(8) O(9). "
            "Select order to form a meaningful word."
        ),
        "question_hi": (
            "अक्षरों को संख्याबद्ध किया गया है: N(1) T(2) I(3) V(4) A(5) A(6) I(7) R(8) O(9). "
            "एक सार्थक शब्द बनाने के लिए सही क्रम चुनिए।"
        ),
        "option_a": "5,4,3,9,1,7,6,2,8",
        "option_b": "4,8,5,6,2,7,9,3,1",
        "option_c": "4,5,8,7,6,2,3,9,1",
        "option_d": "6,4,2,8,7,3,1,5,9",
        "correct_answer": "C",   # → VARIATION
    },
    # ── Q21 ── STRANGER ──────────────────────────────────────────────────────────
    {
        "question_number": 21,
        "difficulty": "easy",
        "question_en": (
            "Letters numbered: E(1) R(2) R(3) A(4) T(5) N(6) S(7) G(8). "
            "Select order to form a meaningful word."
        ),
        "question_hi": (
            "अक्षरों को संख्याबद्ध किया गया है: E(1) R(2) R(3) A(4) T(5) N(6) S(7) G(8). "
            "एक सार्थक शब्द बनाने के लिए सही क्रम चुनिए।"
        ),
        "option_a": "5,7,4,3,8,6,2,1",
        "option_b": "7,5,3,4,6,8,1,2",
        "option_c": "5,3,4,7,1,6,2,8",
        "option_d": "7,3,5,4,6,8,2,1",
        "correct_answer": "B",   # → STRANGER
    },
    # ── Q22 ── PRISON ────────────────────────────────────────────────────────────
    {
        "question_number": 22,
        "difficulty": "easy",
        "question_en": (
            "Letters numbered: O(1) R(2) S(3) P(4) N(5) I(6). "
            "Select order to form a meaningful word."
        ),
        "question_hi": (
            "अक्षरों को संख्याबद्ध किया गया है: O(1) R(2) S(3) P(4) N(5) I(6). "
            "एक सार्थक शब्द बनाने के लिए सही क्रम चुनिए।"
        ),
        "option_a": "1,4,6,5,2,3",
        "option_b": "4,2,6,3,1,5",
        "option_c": "4,6,2,1,3,5",
        "option_d": "5,2,4,3,6,1",
        "correct_answer": "B",   # → PRISON
    },
    # ── Q23 ── STABLISH ──────────────────────────────────────────────────────────
    {
        "question_number": 23,
        "difficulty": "medium",
        "question_en": (
            "Letters numbered: S(1) A(2) B(3) I(4) T(5) S(6) L(7) H(8). "
            "Select order to form a meaningful word."
        ),
        "question_hi": (
            "अक्षरों को संख्याबद्ध किया गया है: S(1) A(2) B(3) I(4) T(5) S(6) L(7) H(8). "
            "एक सार्थक शब्द बनाने के लिए सही क्रम चुनिए।"
        ),
        "option_a": "8,2,6,3,1,4,7,5",
        "option_b": "2,8,6,1,3,4,5,7",
        "option_c": "6,5,2,3,7,4,1,8",
        "option_d": "6,8,2,3,4,5,7,1",
        "correct_answer": "C",   # → STABLISH (archaic: establish)
    },
    # ── Q24 ── STUDENT ── (letter code type) ─────────────────────────────────────
    # E=1,N=2,T=3,S=4,T=5,D=6,U=7  (T appears twice with codes 3 and 5)
    {
        "question_number": 24,
        "difficulty": "easy",
        "question_en": (
            "Letter codes: E=1, N=2, T=3, S=4, T=5, D=6, U=7. "
            "Which number permutation forms a meaningful word?"
        ),
        "question_hi": (
            "अक्षर कूट: E=1, N=2, T=3, S=4, T=5, D=6, U=7. "
            "कौन सा संख्या क्रम एक सार्थक शब्द बनाता है?"
        ),
        "option_a": "2,1,4,6,3,5,7",
        "option_b": "4,3,7,6,1,2,5",
        "option_c": "4,3,7,1,6,5,2",
        "option_d": "2,1,4,3,6,7,5",
        "correct_answer": "B",   # → S,T,U,D,E,N,T = STUDENT
    },
    # ── Q25 ── PENCIL ── (letter code type) ──────────────────────────────────────
    # L=1,P=2,C=3,E=4,I=5,N=6  (all unique)
    {
        "question_number": 25,
        "difficulty": "easy",
        "question_en": (
            "Letter codes: L=1, P=2, C=3, E=4, I=5, N=6. "
            "Which number combination forms a meaningful word?"
        ),
        "question_hi": (
            "अक्षर कूट: L=1, P=2, C=3, E=4, I=5, N=6. "
            "कौन सा संख्या संयोजन एक सार्थक शब्द बनाता है?"
        ),
        "option_a": "6,5,3,4,1,2",
        "option_b": "2,4,6,3,5,1",
        "option_c": "3,4,1,5,2,6",
        "option_d": "2,4,6,3,1,5",
        "correct_answer": "B",   # → P,E,N,C,I,L = PENCIL
    },
    # ── Q26 ── PUZZLE ── (letter code type) ──────────────────────────────────────
    # E=1,Z=2,L=3,P=4,U=5,Z=6  (Z appears twice with codes 2 and 6)
    {
        "question_number": 26,
        "difficulty": "medium",
        "question_en": (
            "Letter codes: E=1, Z=2, L=3, P=4, U=5, Z=6. "
            "Which number permutation forms a meaningful word?"
        ),
        "question_hi": (
            "अक्षर कूट: E=1, Z=2, L=3, P=4, U=5, Z=6. "
            "कौन सा संख्या क्रम एक सार्थक शब्द बनाता है?"
        ),
        "option_a": "1,5,3,4,2,6",
        "option_b": "6,1,4,3,5,2",
        "option_c": "4,5,1,6,2,3",
        "option_d": "4,5,6,2,3,1",
        "correct_answer": "D",   # → P,U,Z,Z,L,E = PUZZLE
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
