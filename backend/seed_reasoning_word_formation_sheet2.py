"""
seed_reasoning_word_formation_sheet2.py
========================================
Seeds Word Formation questions Q7-Q14 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Word Formation
Run     : python seed_reasoning_word_formation_sheet2.py

Answer key (verified via letter-frequency Counter check):
  Q7  MULTIPLICATION  → APPLICATION needs P×2 (only P×1 available)          → C
  Q8  UNCONTAMINATED  → CONTROL needs R (not in source)                      → D
  Q9  EVOLUTION       → VALE needs A (not in source)                         → B
  Q10 PRAGMATIC       → NOTE: 3 options (GUITAR/AGMARK/GAME) cannot be formed;
                        only MAGIC can → question asks "which CAN be formed"  → D
  Q11 RESOLUTION      → MOTION needs M (not in source)                       → C
  Q12 MULTIPLICATION  → MUTUAL needs U×2 (only U×1 available)               → D
  Q13 PUNCTUATION     → POUND needs D (not in source)                        → C
  Q14 IMMEDIATELY     → CAN be formed: LIMITED (L,I×2,M,T,E,D all available) → B
  Q15 QUINTESSENCE    → CAN be formed: QUITE (Q,U,I,T,E all available)        → C
  Q16 ENVIRONMENT     → CAN be formed: EMINENT (E×2,M,I,N×2,T all available)  → C

NOTE: Question text puts source word first so both MULTIPLICATION questions
      (Q7 and Q12) have different 80-char fingerprints (options diverge at ~pos 65).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Word_Formation_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Word Formation"

QUESTIONS = [
    # ── Q7 ────────────────────────────────────────────────────────────────────
    {
        "question_number": 7,
        "difficulty": "easy",
        "question_en": (
            "From 'MULTIPLICATION', which word CANNOT be formed using its letters? "
            "LIMITATION / ACTION / APPLICATION / TIPICAL"
        ),
        "question_hi": (
            "'MULTIPLICATION' शब्द के अक्षरों का प्रयोग करके कौन सा शब्द नहीं बनाया जा सकता? "
            "LIMITATION / ACTION / APPLICATION / TIPICAL"
        ),
        "option_a": "LIMITATION",
        "option_b": "ACTION",
        "option_c": "APPLICATION",
        "option_d": "TIPICAL",
        "correct_answer": "C",
    },
    # ── Q8 ────────────────────────────────────────────────────────────────────
    {
        "question_number": 8,
        "difficulty": "easy",
        "question_en": (
            "From 'UNCONTAMINATED', which word CANNOT be formed using its letters? "
            "CONTAIN / NATION / MENTION / CONTROL"
        ),
        "question_hi": (
            "'UNCONTAMINATED' शब्द के अक्षरों का प्रयोग करके कौन सा शब्द नहीं बनाया जा सकता? "
            "CONTAIN / NATION / MENTION / CONTROL"
        ),
        "option_a": "CONTAIN",
        "option_b": "NATION",
        "option_c": "MENTION",
        "option_d": "CONTROL",
        "correct_answer": "D",
    },
    # ── Q9 ────────────────────────────────────────────────────────────────────
    {
        "question_number": 9,
        "difficulty": "easy",
        "question_en": (
            "From 'EVOLUTION', which word CANNOT be formed using its letters? "
            "VOLT / VALE / TOOL / LOOT"
        ),
        "question_hi": (
            "'EVOLUTION' शब्द के अक्षरों का प्रयोग करके कौन सा शब्द नहीं बनाया जा सकता? "
            "VOLT / VALE / TOOL / LOOT"
        ),
        "option_a": "VOLT",
        "option_b": "VALE",
        "option_c": "TOOL",
        "option_d": "LOOT",
        "correct_answer": "B",
    },
    # ── Q10 ── (question asks CAN be formed — only MAGIC qualifies) ───────────
    {
        "question_number": 10,
        "difficulty": "medium",
        "question_en": (
            "From 'PRAGMATIC', which word CAN be formed using its letters? "
            "GUITAR / AGMARK / GAME / MAGIC"
        ),
        "question_hi": (
            "'PRAGMATIC' शब्द के अक्षरों का प्रयोग करके कौन सा शब्द बनाया जा सकता है? "
            "GUITAR / AGMARK / GAME / MAGIC"
        ),
        "option_a": "GUITAR",
        "option_b": "AGMARK",
        "option_c": "GAME",
        "option_d": "MAGIC",
        "correct_answer": "D",
    },
    # ── Q11 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 11,
        "difficulty": "easy",
        "question_en": (
            "From 'RESOLUTION', which word CANNOT be formed using its letters? "
            "SOLUTION / RESULT / MOTION / LOTION"
        ),
        "question_hi": (
            "'RESOLUTION' शब्द के अक्षरों का प्रयोग करके कौन सा शब्द नहीं बनाया जा सकता? "
            "SOLUTION / RESULT / MOTION / LOTION"
        ),
        "option_a": "SOLUTION",
        "option_b": "RESULT",
        "option_c": "MOTION",
        "option_d": "LOTION",
        "correct_answer": "C",
    },
    # ── Q12 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 12,
        "difficulty": "medium",
        "question_en": (
            "From 'MULTIPLICATION', which word CANNOT be formed using its letters? "
            "LIMITATION / LIPTON / TIPICAL / MUTUAL"
        ),
        "question_hi": (
            "'MULTIPLICATION' शब्द के अक्षरों का प्रयोग करके कौन सा शब्द नहीं बनाया जा सकता? "
            "LIMITATION / LIPTON / TIPICAL / MUTUAL"
        ),
        "option_a": "LIMITATION",
        "option_b": "LIPTON",
        "option_c": "TIPICAL",
        "option_d": "MUTUAL",
        "correct_answer": "D",
    },
    # ── Q13 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 13,
        "difficulty": "easy",
        "question_en": (
            "From 'PUNCTUATION', which word CANNOT be formed using its letters? "
            "AUCTION / NATION / POUND / ACTION"
        ),
        "question_hi": (
            "'PUNCTUATION' शब्द के अक्षरों का प्रयोग करके कौन सा शब्द नहीं बनाया जा सकता? "
            "AUCTION / NATION / POUND / ACTION"
        ),
        "option_a": "AUCTION",
        "option_b": "NATION",
        "option_c": "POUND",
        "option_d": "ACTION",
        "correct_answer": "C",
    },
    # ── Q14 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": (
            "From 'IMMEDIATELY', which word CAN be formed using its letters? "
            "DIALECT / LIMITED / DIAMETER / DICTATE"
        ),
        "question_hi": (
            "'IMMEDIATELY' शब्द के अक्षरों का प्रयोग करके कौन सा शब्द बनाया जा सकता है? "
            "DIALECT / LIMITED / DIAMETER / DICTATE"
        ),
        "option_a": "DIALECT",
        "option_b": "LIMITED",
        "option_c": "DIAMETER",
        "option_d": "DICTATE",
        "correct_answer": "B",
    },
    # ── Q15 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 15,
        "difficulty": "medium",
        "question_en": (
            "From 'QUINTESSENCE', which word CAN be formed using its letters? "
            "SCOT / QUOTE / QUITE / ESTEEM"
        ),
        "question_hi": (
            "'QUINTESSENCE' शब्द के अक्षरों का प्रयोग करके कौन सा शब्द बनाया जा सकता है? "
            "SCOT / QUOTE / QUITE / ESTEEM"
        ),
        "option_a": "SCOT",
        "option_b": "QUOTE",
        "option_c": "QUITE",
        "option_d": "ESTEEM",
        "correct_answer": "C",
    },
    # ── Q16 ───────────────────────────────────────────────────────────────────
    {
        "question_number": 16,
        "difficulty": "medium",
        "question_en": (
            "From 'ENVIRONMENT', which word CAN be formed using its letters? "
            "MOVEMENT / ENTERTAIN / EMINENT / ENTRANCE"
        ),
        "question_hi": (
            "'ENVIRONMENT' शब्द के अक्षरों का प्रयोग करके कौन सा शब्द बनाया जा सकता है? "
            "MOVEMENT / ENTERTAIN / EMINENT / ENTRANCE"
        ),
        "option_a": "MOVEMENT",
        "option_b": "ENTERTAIN",
        "option_c": "EMINENT",
        "option_d": "ENTRANCE",
        "correct_answer": "C",
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
