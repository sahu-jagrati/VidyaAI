"""
seed_reasoning_cube_and_dice_sheet2.py
=======================================
Seeds Reasoning → Cube and Dice  Q9–Q12 (DSSSB exam papers source).

question_numbers 9–12 (continuing from sheet1 which covered Q1–Q8).

Answer key
──────────────────────────────────────────────────────────────────────
Q9  B (3)    — Three dot-dice positions; opposite of 6 = 3.
               Adjacent to 6 in the three positions: {1, 2, 4, 5}
               → only 3 is never adjacent → opp(6) = 3.
               [DSSSB PRT (Assistant Teacher Primary) - 26 March 2022 - Shift 2]

Q10 B        — Dice with 1–6; three positions shown.
               From positions: die-1 shows 5,2,4 visible → 5 adj 2,4.
                               die-2 shows 2,6,4 visible → 6 adj 2,4 → 6 NOT opp 4.
                               die-3 shows 4,1,6 visible → 4 adj 1,6 → 4 NOT opp 6.
               Derived pairs: opp(4)=3, opp(5)=6, opp(1)=2.
               Statement I  "4 & 6 opposite" → FALSE (opp(4)=3).
               Statement II "1 & 5 opposite" → FALSE (opp(1)=2, opp(5)=6).
               Answer: Neither I nor II.
               [DSSSB PRT (Assistant Teacher Primary) - 24 March 2022 - Shift 3]

Q11 A (□)   — Symbol dice (three positions); opposite of triangle △ = small square □.
               From three positions the triangle's four adjacent symbols are identified;
               the remaining symbol (small square) is opposite.
               [DSSSB PRT (Assistant Teacher Primary) - 27 March 2022 - Shift 1]

Q12 B        — Cube net has symbols: ×, ★, △, ○, □, and ✦ (6 faces).
               From net layout: opp(×)=○, opp(★)=□, opp(△)=✦.
               Option 2 cube shows △ and □ on visible faces with ○ on top — consistent
               with all opposite-pair constraints → answer B.
               [DSSSB PRT (Assistant Teacher Primary) - 26 March 2022 - Shift 2]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Cube and Dice"
SOURCE  = "DSSSB_Cube_and_Dice"

QUESTIONS = [

    # ── Q9 [DSSSB PRT - 26 March 2022 - Shift 2] ─────────────────────────────
    # Three positions of same dot-dice; which number is opposite to 6?
    # Adjacent to 6 across positions: 1, 2, 4, 5 → only 3 never adjacent → opp(6)=3.
    {
        "question_number": 9,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "Three positions of the same dice are shown below. Find the number of "
            "dots that lies opposite to the face with 6 dots."
        ),
        "question_hi": (
            "एक ही पासे की तीन स्थितियाँ नीचे दिखाई गई हैं। 6 बिंदुओं वाले "
            "फलक के विपरीत फलक पर स्थित बिंदुओं की संख्या ज्ञात कीजिए।"
        ),
        "image_url": None,
        "option_a": "2",
        "option_b": "3",
        "option_c": "1",
        "option_d": "5",
        "correct_answer": "B",   # 3 is opposite to 6
    },

    # ── Q10 [DSSSB PRT - 24 March 2022 - Shift 3] ────────────────────────────
    # Dice numbered 1–6; three positions shown. Which statements are correct?
    # I. 4 and 6 are on opposite faces.  II. 1 and 5 are on opposite faces.
    # Derived: opp(4)=3, opp(5)=6, opp(1)=2 → Both statements FALSE.
    {
        "question_number": 10,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "A dice has six numbers marked 1, 2, 3, 4, 5 and 6 on its faces. "
            "Three positions of dice are shown below.\n"
            "Which of the following statements is correct?\n"
            "I.  4 and 6 are on opposite faces.\n"
            "II. 1 and 5 are on opposite faces."
        ),
        "question_hi": (
            "एक पासे के फलकों पर 1, 2, 3, 4, 5 और 6 से अंकित छह संख्याएं हैं। "
            "नीचे पासे की तीन स्थितियाँ दर्शाई गई हैं।\n"
            "निम्नलिखित में से कौन सा कथन सही है?\n"
            "I.  4 और 6 विपरीत फलकों पर हैं।\n"
            "II. 1 और 5 विपरीत फलकों पर हैं।"
        ),
        "image_url": None,
        "option_a": "Only II / केवल II",
        "option_b": "Neither I nor II / न तो I और न ही II",
        "option_c": "Only I / केवल I",
        "option_d": "Both I and II / I और II दोनों",
        "correct_answer": "B",   # Neither statement is correct
    },

    # ── Q11 [DSSSB PRT - 27 March 2022 - Shift 1] ────────────────────────────
    # Three positions of symbol dice; which symbol is opposite triangle (△)?
    # From three positions, △ is adjacent to: ○, □(large), ✦, and one more.
    # The remaining symbol small □ is opposite.
    {
        "question_number": 11,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "Given below are three positions of the same dice. Which of the symbols "
            "in the options appears opposite the face having a triangle?"
        ),
        "question_hi": (
            "नीचे एक ही पासे की तीन स्थितियाँ दी गई हैं। विकल्पों में से कौन सा "
            "प्रतीक त्रिभुज वाले फलक के विपरीत दिखाई देता है?"
        ),
        "image_url": None,
        "option_a": "□ (Small rectangle / छोटा आयत)",
        "option_b": "○ (Small circle / छोटा वृत्त)",
        "option_c": "○ (Large circle / बड़ा वृत्त)",
        "option_d": "□ (Large rectangle / बड़ा आयत)",
        "correct_answer": "A",   # Small square/rectangle is opposite to triangle
    },

    # ── Q12 [DSSSB PRT - 26 March 2022 - Shift 2] ────────────────────────────
    # Unfolded cube (net) with symbols ×, ★, △, ○, □, ✦.
    # Which assembled cube can be made from this net?
    # Opposite pairs from net: ×↔○, ★↔□, △↔✦.
    # Option 2: shows △, □, ○ on visible faces — no opposite pair on same cube face → valid.
    {
        "question_number": 12,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Which of the following cubes in the answer figure can be made based on "
            "the unfolded cube (net) shown in the question figure?\n"
            "[Net shows six symbols: ×, ★, △, ○, □, and ✦]"
        ),
        "question_hi": (
            "उत्तर आकृति में निम्नलिखित में से कौन सा घन प्रश्न आकृति में खुले "
            "घन के आधार पर बनाया जा सकता है?\n"
            "[खुले घन में छह प्रतीक हैं: ×, ★, △, ○, □ और ✦]"
        ),
        "image_url": None,
        "option_a": "Cube 1 (★, △ visible / ★, △ दृश्यमान)",
        "option_b": "Cube 2 (△, □, ○ visible / △, □, ○ दृश्यमान)",
        "option_c": "Cube 3 (□, × visible / □, × दृश्यमान)",
        "option_d": "Cube 4 (○, ★ visible / ○, ★ दृश्यमान)",
        "correct_answer": "B",   # Cube 2 is consistent with the net's opposite-pair constraints
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
            if row[0] is not None
        }
        print(f"Topic '{TOPIC}' — existing question_numbers: {len(existing_qnums)}")

        for d in QUESTIONS:
            qn = d["question_number"]
            if qn in existing_qnums:
                print(f"  SKIP  Q{qn}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
            inserted += 1
            print(f"  INSERT Q{qn}")

        db.commit()
        print(f"\nDone — inserted: {inserted}, skipped: {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
