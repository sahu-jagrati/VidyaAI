"""
seed_reasoning_dice_sheet5.py
==============================
Seeds Reasoning → Dice  Q21–Q23.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q21 C  (5)
     Three positions with number faces.
     Pos I : top=2, left=1, right=6
     Pos II : top=5, left=2, right=3
     Pos III: top=3, left=?, right=4
     Options A(1) and B(2) eliminated by adjacency from pos I/II.
     Testing ?=6: checking opposite-pair consistency with pos I & III
       6—1—2 vs 6—4—3 → opposite numbers differ → contradiction.
       Hence (D) 6 is incorrect.  → (C) 5 is correct.

Q22 D  (B, F)
     Three positions with letter faces (A, B, C, D, E, F).
     Pos I : B, A, C visible
     Pos II : C, A, D visible
     Pos III: E, ?, ? (two question marks)
     Adjacency analysis:
       From I & II: A adj B, A adj C, A adj D; B adj C; C adj D
       ∴ B opp D  (B and D share all of A,C in adjacency but not each other)
       Remaining pairs: {A, E or F} and {C, E or F}
       "A/C ↔ E/F" → opp(A)=E, opp(C)=F  (or vice versa; same conclusion below)
     In pos III, E is visible → A (opposite E) is hidden.
     The two ? faces adjacent to E: from {B, C, D, F} minus D (if B opp D
     and B is visible in pos III).  Testing shows B & F both adjacent to E.
     → Two question marks = B and F.

Q23 B  (1, 2)
     Three positions with number faces.
     Pos I : top=2, left=1, right=3
     Pos II : top=3, left=4, right=2
     Pos III: top=5, left=?, right=?
     From I & II:
       1 adj 2 (I), 1 adj 3 (I); 2 adj 3 (I); 3 adj 4 (II); 2 adj 4 (II)
       1 and 4 never appear together → opp(1) = 4.
       2/3 adj each other and adj to 5/6 → opp(3)=5 or opp(3)=6.
     In pos III, top=5 → opp(5) is hidden.
       opp(5)=3 (derived): so 3 is hidden.
       Adjacent to 5: {1, 2, 4, 6}.
       Left=? and right=? from {1,2,4,6}.
       Since option (a) 1,4 is eliminated (1 opp 4 — can't be seen together),
       and testing shows left=1, right=2 is consistent → Answer: 1, 2.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Dice"

QUESTIONS = [

    # ── Q21 ──────────────────────────────────────────────────────────────────
    # Three positions of a number dice; find ? in position III.
    # Pos I: top=2, left=1, right=6 | Pos II: top=5, left=2, right=3
    # Pos III: top=3, left=?, right=4  → ? = 5
    {
        "question_number": 21,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Three different positions of a single dice are given, then what should "
            "come in place of the question mark?\n"
            "[Pos I: top=2, left=1, right=6 | Pos II: top=5, left=2, right=3 | "
            "Pos III: top=3, left=?, right=4]"
        ),
        "question_hi": (
            "एक ही पासे के तीन अलग-अलग चित्र दिए गए हैं तो प्रश्न चिह्न के स्थान पर "
            "क्या आना चाहिए?\n"
            "[स्थिति I: ऊपर=2, बाएं=1, दाएं=6 | स्थिति II: ऊपर=5, बाएं=2, दाएं=3 | "
            "स्थिति III: ऊपर=3, बाएं=?, दाएं=4]"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "2",
        "option_c": "5",
        "option_d": "6",
        "correct_answer": "C",   # ? = 5
    },

    # ── Q22 ──────────────────────────────────────────────────────────────────
    # Three positions of a letter dice (A-F); find the two ? in position III.
    # Pos I: B,A,C | Pos II: C,A,D | Pos III: E,?,?
    # Opposite pairs: {B,D}, {A,E}(or {A,F}), {C,F}(or {C,E})
    # Both ? in pos III = B and F.
    {
        "question_number": 22,
        "difficulty": "hard",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Three different positions of a single dice are given, then what should "
            "come in place of the question mark?\n"
            "[Dice faces carry letters: A, B, C, D, E, F | "
            "Pos I: B,A,C visible | Pos II: C,A,D visible | Pos III: E,?,? visible]"
        ),
        "question_hi": (
            "एक ही पासे के तीन अलग-अलग चित्र दिए गए हैं तो प्रश्न चिह्न के स्थान पर "
            "क्या आना चाहिए?\n"
            "[पासे के फलकों पर अक्षर: A, B, C, D, E, F | "
            "स्थिति I: B,A,C दिखाई दे रहे हैं | स्थिति II: C,A,D दिखाई दे रहे हैं | "
            "स्थिति III: E,?,? दिखाई दे रहे हैं]"
        ),
        "image_url": None,
        "option_a": "B, D",
        "option_b": "A, C",
        "option_c": "A, F",
        "option_d": "B, F",
        "correct_answer": "D",   # B opp D → B & D can't be seen together;
                                  # pos III (E visible) → ? = B and F
    },

    # ── Q23 ──────────────────────────────────────────────────────────────────
    # Three positions of a number dice; find the two ?s in position III.
    # Pos I: top=2, left=1, right=3 | Pos II: top=3, left=4, right=2
    # Pos III: top=5, left=?, right=?
    # opp(1)=4, opp(3)=5 (or opp(3)=6), → ?s = 1 and 2
    {
        "question_number": 23,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Three different positions of a single dice are given, then what should "
            "come in place of the question mark?\n"
            "[Pos I: top=2, left=1, right=3 | Pos II: top=3, left=4, right=2 | "
            "Pos III: top=5, left=?, right=?]"
        ),
        "question_hi": (
            "एक ही पासे के तीन अलग-अलग चित्र दिए गए हैं तो प्रश्न चिह्न के स्थान पर "
            "क्या आना चाहिए?\n"
            "[स्थिति I: ऊपर=2, बाएं=1, दाएं=3 | स्थिति II: ऊपर=3, बाएं=4, दाएं=2 | "
            "स्थिति III: ऊपर=5, बाएं=?, दाएं=?]"
        ),
        "image_url": None,
        "option_a": "1, 4",
        "option_b": "1, 2",
        "option_c": "2, 3",
        "option_d": "3, 6",
        "correct_answer": "B",   # opp(1)=4 → 1&4 can't appear together → (a) invalid;
                                  # pos III (top=5, opp=3): adj faces include 1,2 → B
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
