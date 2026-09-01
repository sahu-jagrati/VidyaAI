"""
seed_reasoning_dice_sheet1.py
==============================
Seeds Reasoning → Dice  Q1–Q4.

Topic: Dice  (NEW — created implicitly by first insert)
Subject: Reasoning

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q1  A  (Only I)
     7 × 5 × 3 cuboid; each pair of opposite faces painted red/green/blue.
     Cut into 1 cm cubes.
     Statement I  → interior = (7-2)(5-2)(3-2) = 5×3×1 = 15  ✓ TRUE
     Statement II → edge cubes touching blue AND green (not red):
       4 vertical edges, each contributes only z=2 (z=1,3 are red corners)
       → 4 cubes, NOT 6  ✗ FALSE
     Only Statement I is correct.
     [UPSC Prelims CSAT 2023]

Q2  A  (8)
     64 smaller cubes → edge = 4 (4³=64).
     Completely interior cubes (never visible) = (4-2)³ = 2³ = 8.
     [RPSC RAS Prelims 2023]

Q3  C  (6)
     Dice rolled twice; two positions shown.
     From visible adjacency in both positions, pairs derived:
     1 adj 2,3,4,5 → opp(1)=6; combined with position (ii) confirms opp(top)=6.
     Bottom of position (i) = 6.
     [KGPSC JSO Pre Screening 29-01-2022]

Q4  C  (3 and 4 only)
     Net (X) folded; opposite pairs derived from net layout.
     Cubes 3 and 4 show only face combinations consistent with those pairs.
     Cubes 1 and 2 show at least one opposite-pair on adjacent faces → invalid.
     [KGPSC JSO Pre Screening 19-11-2022]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Dice"
SOURCE  = "KGPSC_JSO_UPSC_RPSC_Mixed"

QUESTIONS = [

    # ── Q1 [UPSC Prelims CSAT 2023] ──────────────────────────────────────────
    # 7×5×3 cuboid painted red(7×5), green(5×3), blue(7×3); cut into 1cm cubes.
    # I: 15 interior cubes (no paint)  →  TRUE
    # II: 6 cubes with exactly blue+green → FALSE (only 4 such cubes)
    {
        "question_number": 1,
        "difficulty": "hard",
        "source_pdf": "UPSC_CSAT_2023",
        "question_en": (
            "A cuboid of dimensions 7 cm × 5 cm × 3 cm is painted red, green and blue "
            "colour on each pair of opposite faces of dimensions 7 cm × 5 cm, 5 cm × 3 cm, "
            "7 cm × 3 cm respectively. The cuboid is then cut into various cubes each of "
            "side length 1 cm. Which of the following statements is/are correct?\n"
            "I.  There are exactly 15 small cubes with no paint on any face.\n"
            "II. There are exactly 6 small cubes with exactly two faces, one painted with "
            "blue and the other with green."
        ),
        "question_hi": (
            "7 सेमी × 5 सेमी × 3 सेमी आयाम वाले घनाभ को क्रमशः 7 सेमी × 5 सेमी, "
            "5 सेमी × 3 सेमी, 7 सेमी × 3 सेमी आयाम वाले प्रत्येक जोड़े के विपरीत "
            "फलकों पर लाल, हरे और नीले रंग से रंगा गया है। फिर घनाभ को काटा जाता "
            "है और विभिन्न घनों में अलग किया जाता है जिनकी प्रत्येक भुजा की लंबाई "
            "1 सेमी होती है। निम्नलिखित में से कौन सा/से कथन सही है/हैं?\n"
            "I.  बिल्कुल 15 छोटे घन हैं जिनके किसी भी फलक पर कोई रंग नहीं है।\n"
            "II. बिल्कुल 6 छोटे घन हैं जिनमें बिल्कुल दो फलक हैं, एक नीले रंग से "
            "और दूसरा हरे रंग से रंगा हुआ है।"
        ),
        "image_url": None,
        "option_a": "Only I / केवल I",
        "option_b": "Only II / केवल II",
        "option_c": "Both I and II / I और II दोनों",
        "option_d": "Neither I nor II / न तो I और न ही II",
        "correct_answer": "A",   # Only I is correct (II gives 4, not 6)
    },

    # ── Q2 [RPSC RAS Prelims 2023] ────────────────────────────────────────────
    # Solid cube formed from 64 smaller cubes. How many smaller cubes are never visible?
    # 64 = 4³ → edge = 4; interior = (4-2)³ = 8.
    {
        "question_number": 2,
        "difficulty": "easy",
        "source_pdf": "RPSC_RAS_Prelims_2023",
        "question_en": (
            "A solid cube has been formed with 64 smaller cubes. How many smaller cubes "
            "will not be visible in any condition?"
        ),
        "question_hi": (
            "64 छोटे घनों से एक ठोस घन बनाया गया है। कितने छोटे घन किसी भी "
            "स्थिति में दिखाई नहीं देंगे?"
        ),
        "image_url": None,
        "option_a": "8",
        "option_b": "6",
        "option_c": "4",
        "option_d": "2",
        "correct_answer": "A",   # (4-2)³ = 8 interior cubes
    },

    # ── Q3 [KGPSC JSO Pre Screening 29-01-2022] ───────────────────────────────
    # Dice rolled twice; two positions shown. Find dots at bottom of position (i).
    # From the two positions, adjacency analysis: opp pair {1,6} derived;
    # top face of position (i) = 1 → bottom = 6.
    {
        "question_number": 3,
        "difficulty": "medium",
        "source_pdf": "KGPSC_JSO_Pre_Screening_29_01_2022",
        "question_en": (
            "A dice is rolled twice and the two positions are shown in the figure below. "
            "What is the number of dots at the bottom face when the dice is in position (i)?"
        ),
        "question_hi": (
            "एक पासे को दो बार घुमाया जाता है और दोनों स्थितियों को नीचे दिए गए "
            "चित्र में दिखाया गया है। जब पासा स्थिति (i) में हो तो निचली सतह पर "
            "बिंदुओं की संख्या क्या है?"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "5",
        "option_c": "6",
        "option_d": "Cannot be determined / तय नहीं किया जा सकता",
        "correct_answer": "C",   # bottom of position (i) = 6
    },

    # ── Q4 [KGPSC JSO Pre Screening 19-11-2022] ───────────────────────────────
    # Net (X) with symbols: choose which assembled boxes can be formed.
    # Opposite pairs from net layout confirmed for cubes 3 and 4 only.
    {
        "question_number": 4,
        "difficulty": "hard",
        "source_pdf": "KGPSC_JSO_Pre_Screening_19_11_2022",
        "question_en": (
            "Choose the box that is similar to the box formed from the given sheet of "
            "paper (X). Which of the following boxes can be formed?"
        ),
        "question_hi": (
            "वह बॉक्स चुनें जो कागज की दी गई शीट (X) से बने बॉक्स के समान है। "
            "निम्नलिखित में से कौन सा/से बॉक्स बनाया/बनाए जा सकता/सकते है/हैं?"
        ),
        "image_url": None,
        "option_a": "1 and 2 only / केवल 1 और 2",
        "option_b": "1 and 3 only / केवल 1 और 3",
        "option_c": "3 and 4 only / केवल 3 और 4",
        "option_d": "1, 2, 3 and 4 / 1, 2, 3 और 4",
        "correct_answer": "C",   # Only boxes 3 and 4 can be formed from net X
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
