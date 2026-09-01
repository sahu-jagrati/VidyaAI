"""
seed_reasoning_dice_sheet6.py
==============================
Seeds Reasoning → Dice  Q24–Q26.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q24 A  (E, A)
     Three positions of a letter dice (A–F); find two ?s in pos III.
     Pos I : D, A, C visible
     Pos II: C, A, F visible
     Pos III: D, ?, ? visible
     From (I) & (II):
       A/C ↔ B/E  →  opp pairs among {A,B,C,E}
       D ↔ F      →  D and F are opposite
     In pos III, D is visible → F (opposite D) is hidden.
     ∴ F cannot be one of the two ?s → eliminates options (B),(C),(D).
     → Two ?s = E and A.   Answer: (A)

Q25 D  (Box d)
     Two positions of a number dice; identify the correct 3D representation.
     Pos I : 2, 1, 3 visible
     Pos II: 6, 1, 2 visible
     From (I) & (II):
       3 ↔ 6   (3 and 6 never appear together → opposite)
       1/2 ↔ 4/5
     Option (c) shows 3 and 6 adjacent → impossible (they are opposite).
     Option (d) is consistent with all derived pairs.   Answer: (D)

Q26 C  (5)
     Four positions of a number dice; find number opposite to face showing 2.
     Pos I : 6, 2, 4 visible
     Pos II: 2, 3, 4 visible
     Pos III: 3, 5, 4 visible
     Pos IV: 1, 3, 2 visible
     From (I) & (IV) — both contain face 2:
       Spine I : 2→6→4
       Spine IV: 2→3→1
       Testing opp(2)=5: 5 is absent from both positions → consistent.
     ∴  opp(2) = 5.   Answer: (C)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Dice"

QUESTIONS = [

    # ── Q24 ──────────────────────────────────────────────────────────────────
    # Three letter-dice positions; find the two ? faces in position III.
    # Pos I: D,A,C | Pos II: C,A,F | Pos III: D,?,?
    # D opp F → F can't appear in pos III (D is visible there).
    # → Two ?s = E and A.
    {
        "question_number": 24,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Three different positions of a single dice are given, then what should "
            "come in place of the question mark?\n"
            "[Dice faces carry letters: A, B, C, D, E, F | "
            "Pos I: D(top), A(left), C(right) | "
            "Pos II: C(top), A(left), F(right) | "
            "Pos III: D(top), ?(left), ?(right)]"
        ),
        "question_hi": (
            "एक ही पासे के तीन अलग-अलग चित्र दिए गए हैं तो प्रश्न चिह्न के स्थान पर "
            "क्या आना चाहिए?\n"
            "[पासे के फलकों पर अक्षर: A, B, C, D, E, F | "
            "स्थिति I: D(ऊपर), A(बाएं), C(दाएं) | "
            "स्थिति II: C(ऊपर), A(बाएं), F(दाएं) | "
            "स्थिति III: D(ऊपर), ?(बाएं), ?(दाएं)]"
        ),
        "image_url": None,
        "option_a": "E, A",
        "option_b": "F, C",
        "option_c": "E, F",
        "option_d": "B, F",
        "correct_answer": "A",   # D opp F → F hidden in pos III → ?s = E, A
    },

    # ── Q25 ──────────────────────────────────────────────────────────────────
    # Two positions of a number dice; find which answer cube is correct.
    # Pos I: 2,1,3 | Pos II: 6,1,2
    # Pairs: opp(3)=6, opp(1 or 2)=4 or 5
    # Option (c) shows 3 & 6 adjacent → impossible → INVALID.
    # Option (d) consistent with derived pairs → VALID.
    {
        "question_number": 25,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Two different positions of a single dice are given, then find the correct "
            "option which represents that dice given in question figure.\n"
            "[Pos I: top=2, left=1, right=3 | Pos II: top=6, left=1, right=2]"
        ),
        "question_hi": (
            "एक ही पासे के दो अलग-अलग चित्र दिए गए हैं, फिर सही विकल्प खोजें जो "
            "प्रश्न आकृति में दिए गए पासे को दर्शाए।\n"
            "[स्थिति I: ऊपर=2, बाएं=1, दाएं=3 | स्थिति II: ऊपर=6, बाएं=1, दाएं=2]"
        ),
        "image_url": None,
        "option_a": "Box (a) / डिब्बा (a)",
        "option_b": "Box (b) / डिब्बा (b)",
        "option_c": "Box (c) / डिब्बा (c)",
        "option_d": "Box (d) / डिब्बा (d)",
        "correct_answer": "D",   # opp(3)=6 → (c) invalid (shows 3&6 adj); (d) consistent
    },

    # ── Q26 ──────────────────────────────────────────────────────────────────
    # Four positions of a number dice; find number opposite to face showing 2.
    # Pos I: {6,2,4} | Pos II: {2,3,4} | Pos III: {3,5,4} | Pos IV: {1,3,2}
    # From pos I & IV (both show 2): opp(2)=5 (5 is absent from both).
    {
        "question_number": 26,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "A dice is thrown four times and its four different positions are shown below. "
            "Find the number on the face opposite the face showing 2.\n"
            "[Pos I: 6,2,4 | Pos II: 2,3,4 | Pos III: 3,5,4 | Pos IV: 1,3,2]"
        ),
        "question_hi": (
            "एक पासा चार बार फेंका जाता है और इसके चार अलग-अलग चित्र नीचे दिखाए गए हैं। "
            "तब 2 के विपरीत क्या होगा?\n"
            "[स्थिति I: 6,2,4 | स्थिति II: 2,3,4 | स्थिति III: 3,5,4 | स्थिति IV: 1,3,2]"
        ),
        "image_url": None,
        "option_a": "3",
        "option_b": "4",
        "option_c": "5",
        "option_d": "6",
        "correct_answer": "C",   # opp(2) = 5
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
