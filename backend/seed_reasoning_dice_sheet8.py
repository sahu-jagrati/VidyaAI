"""
seed_reasoning_dice_sheet8.py
==============================
Seeds Reasoning → Dice  Q37–Q40.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q37 D  (I, II and III all correct)
     Four positions of a cube (faces numbered 1–6):
       Pos I : {6, 3, 2} visible
       Pos II : {4, 1, 2} visible
       Pos III: {4, 6, 5} visible
       Pos IV : {3, 1, 5} visible
     From fig II & III (common face = 4):
       4 adj {1,2,6,5} → opp(4) = 3
       Strip comparison: 1 and 6 on opposite sides of ring → opp(1) = 6
     ∴ Statement I (II & III → opp(6)=1) ✓
     ∴ Statement II (II & III → opp(4)=3) ✓
     From fig I & IV (common face = 3):
       3 adj {6,2,1,5} → opp(3) = 4
     ∴ Statement III (I & IV → opp(3)=4) ✓
     All three statements correct → D.

Q38 C  (3 is adjacent to 5)
     Condition: 1 adj 2, 4, and 6 (at least 3 of 1's adj faces).
     Remaining faces: {3, 5}. One is opp(1), the other is adj to 1.
     Case A — opp(1)=3: 3 adj {2,4,5,6} → 3 adj 5 ✓
     Case B — opp(1)=5: 5 adj {2,3,4,6} → 5 adj 3 ✓
     In both cases: 3 adj 5 (necessarily true).
     Options (a)/(b)/(d) are not necessarily true.

Q39 B  (2 is adjacent to 4 and 6)
     Given: opp(1)=5, opp(2)=3 → by elimination opp(4)=6.
     2 adj all faces except opp(2)=3 → 2 adj {1,4,5,6}.
     So 2 adj 4 ✓ and 2 adj 6 ✓ → option (B) necessarily true.
     (a) "4 adj 1,3 and 6": opp(4)=6 → 4 NOT adj 6 → FALSE.
     (c) "4 adj 5 and 6": opp(4)=6 → 4 NOT adj 6 → FALSE.
     (d) "6 adj 3 and 4": opp(4)=6 → 6 NOT adj 4 → FALSE.

Q40 A  (4 is adjacent to 6)
     Condition: 1 adj 2, 3, and 5 → opp(1) ∈ {4, 6}.
     Case A — opp(1)=4: 4 adj {2,3,5,6} → 4 adj 6 ✓
     Case B — opp(1)=6: 6 adj {2,3,4,5} → 6 adj 4 ✓
     In both cases: 4 adj 6 (necessarily true).
     (b) "5 opp 2": not determinable → NOT necessarily true.
     (c) "1 adj 6": false when opp(1)=6.
     (d) "1 adj 4": false when opp(1)=4.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Dice"

QUESTIONS = [

    # ── Q37 ──────────────────────────────────────────────────────────────────
    # Evaluate three sufficiency statements about opposite faces.
    # Pos I:{6,3,2} | Pos II:{4,1,2} | Pos III:{4,6,5} | Pos IV:{3,1,5}
    # Pairs: opp(1)=6, opp(2)=5, opp(3)=4.
    # All three statements are correct → D.
    {
        "question_number": 37,
        "difficulty": "hard",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Each of the six faces of a cube is numbered by one of the six digits from 1 to 6. "
            "This cube is shown in its four different positions in figures (I), (II), (III) and (IV).\n\n"
            "Consider the following statements:\n"
            "I.  Figures (II) and (III) are sufficient to know as to which face is opposite "
            "to the face numbered 6.\n"
            "II. Figures (II) and (III) are sufficient to know as to which face is opposite "
            "to the face numbered 4.\n"
            "III. Figures (I) and (IV) are sufficient to know as to which face is opposite "
            "to the face numbered 3.\n\n"
            "Which of the statements given above are correct?"
        ),
        "question_hi": (
            "एक घन के छः फलकों में से प्रत्येक को 1 से 6 तक के छः अंकों में से एक द्वारा "
            "क्रमांकित किया गया है। यह घन इसके चार अलग-अलग चित्रों (I), (II), (III) और (IV) "
            "में दिखाया गया है।\n\n"
            "निम्नलिखित कथनों पर विचार करें:\n"
            "I.  चित्र (II) और (III) यह जानने के लिए पर्याप्त हैं कि कौन सी सतह 6 के विपरीत है।\n"
            "II. चित्र (II) और (III) यह जानने के लिए पर्याप्त हैं कि कौन सी सतह 4 के विपरीत है।\n"
            "III. चित्र (I) और (IV) यह जानने के लिए पर्याप्त हैं कि कौन सी सतह 3 के विपरीत है।\n\n"
            "ऊपर दिए गए कौन से कथन सही हैं?"
        ),
        "image_url": None,
        "option_a": "I and III only / केवल I और III",
        "option_b": "I and II only / केवल I और II",
        "option_c": "II and III only / केवल II और III",
        "option_d": "I, II and III / I, II और III",
        "correct_answer": "D",   # all three statements are correct
    },

    # ── Q38 ──────────────────────────────────────────────────────────────────
    # Logic: if 1 adj {2,4,6}, which statement is necessarily true?
    # opp(1) ∈ {3,5} → in both cases 3 adj 5. Answer C.
    {
        "question_number": 38,
        "difficulty": "hard",
        "source_pdf": "Practice_Set",
        "question_en": (
            "The questions based on a dice numbered 1 to 6 in different ways as indicated:\n"
            "If 1 is adjacent to 2, 4 and 6, then which of the following statements "
            "is necessarily true?"
        ),
        "question_hi": (
            "प्रश्न एक पासा पर आधारित है जो 1 से 6 तक अलग-अलग तरीकों से इंगित किया गया है:\n"
            "यदि संख्या 1, 2, 4 और 6 से सटा हुआ है, तो निम्नलिखित में से कौन सा कथन सत्य है?"
        ),
        "image_url": None,
        "option_a": "2 is opposite to 6 / 2, 6 के विपरीत है",
        "option_b": "3 is adjacent to 1 / 1, 3 से सटा हुआ है",
        "option_c": "3 is adjacent to 5 / 3, 5 से सटा हुआ है",
        "option_d": "3 is opposite to 5 / 3, 5 के विपरीत है",
        "correct_answer": "C",   # 3 adj 5 in both cases (whether opp(1)=3 or opp(1)=5)
    },

    # ── Q39 ──────────────────────────────────────────────────────────────────
    # Logic: opp(1)=5, opp(2)=3 → opp(4)=6; 2 adj {1,4,5,6} → 2 adj 4 and 6.
    {
        "question_number": 39,
        "difficulty": "hard",
        "source_pdf": "Practice_Set",
        "question_en": (
            "The questions based on a dice numbered 1 to 6 in different ways as indicated:\n"
            "If 1 is opposite to 5 and 2 is opposite to 3, then?"
        ),
        "question_hi": (
            "प्रश्न एक पासा पर आधारित है जो 1 से 6 तक अलग-अलग तरीकों से इंगित किया गया है:\n"
            "यदि 1, 5 के विपरीत है और 2, 3 के विपरीत है, तो?"
        ),
        "image_url": None,
        "option_a": "4 is adjacent to 1, 3 and 6 / 4, 3 और 6 के समीप है",
        "option_b": "2 is adjacent to 4 and 6 / 2, 4 और 6 के समीप है",
        "option_c": "4 is adjacent to 5 and 6 / 4, 5 और 6 के समीप है",
        "option_d": "6 is adjacent to 3 and 4 / 6, 3 और 4 के समीप है",
        "correct_answer": "B",   # opp(4)=6 → 2 adj {1,4,5,6} → 2 adj 4 & 6
    },

    # ── Q40 ──────────────────────────────────────────────────────────────────
    # Logic: 1 adj {2,3,5} → opp(1) ∈ {4,6} → in both cases 4 adj 6.
    {
        "question_number": 40,
        "difficulty": "hard",
        "source_pdf": "Practice_Set",
        "question_en": (
            "The questions based on a dice numbered 1 to 6 in different ways as indicated:\n"
            "If 1 is adjacent to 2, 3 and 5, then which of the following statements "
            "is necessarily true?"
        ),
        "question_hi": (
            "प्रश्न एक पासा पर आधारित है जो 1 से 6 तक अलग-अलग तरीकों से इंगित किया गया है:\n"
            "यदि 1, 2, 3 और 5 के निकट है, तो निम्नलिखित में से कौन सा कथन सत्य है?"
        ),
        "image_url": None,
        "option_a": "4 is adjacent to 6 / 4, 6 के समीप है",
        "option_b": "5 is opposite to 2 / 5, 2 के विपरीत है",
        "option_c": "1 is adjacent to 6 / 1, 6 के समीप है",
        "option_d": "1 is adjacent to 4 / 1, 4 के समीप है",
        "correct_answer": "A",   # opp(1)=4 or opp(1)=6 → in both cases 4 adj 6
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
