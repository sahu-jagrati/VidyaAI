"""
seed_reasoning_dice_sheet9.py
==============================
Seeds Reasoning → Dice  Q41–Q50.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q41 D  (+)
     Symbols on dice: •, +, △, □, *, [6th face].
     From pos II & III (pivot = •):
       Strip II: • — □ — *
       Strip III: • — + — △
     Middle-face pairs: □ and + are opposite → opp(□) = +.

Q42 D  (6)
     Two positions of a number dice.
     From spine analysis: 2/3 ↔ 1/4, opp(5) = 6.

Q43 C  (3)
     Two positions: Pos I {6,1,2}, Pos II {2,3,...}.
     Spine: 6/2 ↔ 1/4, then 1 ↔ 3 → opp(1) = 3.

Q44 B  (3)
     Two positions of a dice with triangles on faces (1–6 triangles).
     Spine: 1 < 3-5-4 / 3-6-2 → opp(1) = 3.
     When 1 triangle is at bottom → 3 triangles at top.

Q45 C  (Box c)
     Net with faces 1,2 | 3 | 4 | 5,6 (cross shape).
     Opposite pairs: {1,6}, {2,4}, {3,5}.
     Rotation method:
       (a): 1,2,3 anticlockwise in answer but clockwise in net → INVALID.
       (b): 4,6,5 anticlockwise in answer → INVALID.
       (c): 3,6,4 clockwise in both net and answer → VALID ✓.
       (d): 3,4,1 anticlockwise in answer → INVALID.

Q46 B  (4)
     Three positions; find opp(6).
     From I & III: 1 < 3-2-6 / 3-5-4 → endpoint pair: opp(6) = 4.

Q47 C  (4)
     Multiple positions; find bottom when top = 5.
     From I & II: 6 < 3-4-2 / 3-5-1 → middle-face pair: opp(5) = 4.
     Top = 5 → bottom = 4.

Q48 A  (1)
     Two positions; find opp(4).
     Spine: 5 < 3-4-6 / 3-1-2 → middle-face pair: opp(4) = 1.

Q49 C  (5)
     Three positions; find opp(3).
     From II & III: 3 < 5-4-6 / 5-1-2 → opp(3) = 5.

Q50 C  (5)
     Three positions; find opp(2).
     From I & III: 1 < 3-2-6 / 3-5-4 → middle-face pair: opp(2) = 5.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Dice"

QUESTIONS = [

    # ── Q41 ──────────────────────────────────────────────────────────────────
    # Dice with symbols; find face opposite to □ in figure (III).
    # Spine from pos II & III: opp(□) = +.
    {
        "question_number": 41,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the given figure (III), which of the following will be the face "
            "opposite to the face showing □ (square)?\n"
            "[Dice faces carry symbols: •, +, △, □, * and one more. "
            "Three positions (I, II, III) are shown.]"
        ),
        "question_hi": (
            "(iii) में दिए गए (□) के विपरीत होगा?\n"
            "[पासे के फलकों पर चिह्न: •, +, △, □, * और एक अन्य चिह्न। "
            "तीन स्थितियाँ (I, II, III) दिखाई गई हैं।]"
        ),
        "image_url": None,
        "option_a": "* (star/asterisk)",
        "option_b": "△ (triangle / त्रिभुज)",
        "option_c": "• (dot / बिंदु)",
        "option_d": "+ (plus / प्लस)",
        "correct_answer": "D",   # opp(□) = +
    },

    # ── Q42 ──────────────────────────────────────────────────────────────────
    # Two dice positions; find opp(5).
    # Spine: 2/3 ↔ 1/4, opp(5) = 6.
    {
        "question_number": 42,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "From the following two different appearances of dice, find out the "
            "number which is opposite to '5'."
        ),
        "question_hi": (
            "निम्नलिखित पासे के दो अलग-अलग चित्रों में से संख्या का पता लगाएं "
            "जो '5' के विपरीत है।"
        ),
        "image_url": None,
        "option_a": "2",
        "option_b": "3",
        "option_c": "4",
        "option_d": "6",
        "correct_answer": "D",   # opp(5) = 6
    },

    # ── Q43 ──────────────────────────────────────────────────────────────────
    # Two cube positions; find opp(1).
    # Pos I: {6,1,2} | Pos II: {2,3,...}. opp(1) = 3.
    {
        "question_number": 43,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Two positions of a cube are given. Based on them find out which number "
            "is found opposite number 1 in the given cube?"
        ),
        "question_hi": (
            "एक घन के दो चित्र दिए गए हैं। उनके आधार पर पता लगाइए कि दिए गए "
            "घन में संख्या 1 के विपरीत कौन सी संख्या पाई जाती है?"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "2",
        "option_c": "3",
        "option_d": "4",
        "correct_answer": "C",   # opp(1) = 3
    },

    # ── Q44 ──────────────────────────────────────────────────────────────────
    # Two positions of a dice with triangles (1–6) per face.
    # Spine: 1 < 3-5-4 / 3-6-2 → opp(1) = 3.
    # When 1 triangle at bottom → 3 triangles at top.
    {
        "question_number": 44,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Two positions of a cubical block are given below, each face having a "
            "number of small triangles. In another position of the cube, if there is "
            "one triangle at the bottom, how many triangles will be there on the top face?"
        ),
        "question_hi": (
            "एक घन के दो चित्र नीचे दिए गए हैं, जिनमें प्रत्येक में कई छोटे त्रिकोण हैं। "
            "घन की एक और स्थिति में, यदि नीचे की सतह पर एक त्रिकोण है, "
            "तो ऊपरी सतह पर कितने त्रिकोण होंगे?"
        ),
        "image_url": None,
        "option_a": "4",
        "option_b": "3",
        "option_c": "2",
        "option_d": "5",
        "correct_answer": "B",   # opp(1) = 3 → top = 3 triangles
    },

    # ── Q45 ──────────────────────────────────────────────────────────────────
    # Net folding question; cross-shaped net with faces 1,2,3,4,5,6.
    # Pairs: {1,6}, {2,4}, {3,5}. Rotation confirms option (c).
    {
        "question_number": 45,
        "difficulty": "hard",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Choose from the four answer figures, the figure that will be formed "
            "when the question figure is folded into a box?\n"
            "[Net layout: 1,2 in top row | 3 alone | 4 alone | 5,6 in bottom row. "
            "Opposite pairs: {1,6}, {2,4}, {3,5}]"
        ),
        "question_hi": (
            "चार विकल्पों में से वह आकृति चुनें जो तब बनेगी जब प्रश्न आकृति को "
            "एक बॉक्स में बदल दिया जाता है?\n"
            "[जाल: शीर्ष पंक्ति 1,2 | अकेला 3 | अकेला 4 | निचली पंक्ति 5,6। "
            "विपरीत जोड़े: {1,6}, {2,4}, {3,5}]"
        ),
        "image_url": None,
        "option_a": "Box (a) / डिब्बा (a)",
        "option_b": "Box (b) / डिब्बा (b)",
        "option_c": "Box (c) / डिब्बा (c)",
        "option_d": "Box (d) / डिब्बा (d)",
        "correct_answer": "C",   # rotation confirms (c) → 3,6,4 clockwise ✓
    },

    # ── Q46 ──────────────────────────────────────────────────────────────────
    # Three dice positions; find opp(6).
    # From I & III: spine gives endpoint pair opp(6) = 4.
    {
        "question_number": 46,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Three positions of a dice are given below. Identify the number on the "
            "face opposite to 6."
        ),
        "question_hi": (
            "एक पासे की तीन चित्र नीचे दिए गए हैं। 6 के विपरीत सतह पर संख्या को पहचानें।"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "4",
        "option_c": "5",
        "option_d": "6",
        "correct_answer": "B",   # opp(6) = 4
    },

    # ── Q47 ──────────────────────────────────────────────────────────────────
    # Multiple dice positions; find bottom when top = 5.
    # Spine: 6 < 3-4-2 / 3-5-1 → opp(5) = 4. Top = 5 → bottom = 4.
    {
        "question_number": 47,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Position of Dices is given below: Identify the number when top is 5, "
            "what will be at bottom?"
        ),
        "question_hi": (
            "एक पासे की स्थितियाँ नीचे दी गई हैं: संख्या की पहचान करें जब शीर्ष 5 "
            "है तो नीचे क्या होगा?"
        ),
        "image_url": None,
        "option_a": "6",
        "option_b": "3",
        "option_c": "4",
        "option_d": "2",
        "correct_answer": "C",   # opp(5) = 4
    },

    # ── Q48 ──────────────────────────────────────────────────────────────────
    # Two dice positions; find opp(4).
    # Spine: 5 < 3-4-6 / 3-1-2 → middle-face pair: opp(4) = 1.
    {
        "question_number": 48,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which number appears on the face opposite to the face with number 4?"
        ),
        "question_hi": (
            "संख्या 4 के विपरीत सतह में कौन सी संख्या दिखाई देती है?"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "2",
        "option_c": "3",
        "option_d": "5",
        "correct_answer": "A",   # opp(4) = 1
    },

    # ── Q49 ──────────────────────────────────────────────────────────────────
    # Three positions; find opp(3).
    # From II & III: 3 < 5-4-6 / 5-1-2 → opp(3) = 5.
    {
        "question_number": 49,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Study the following figures and find out the number opposite to 3."
        ),
        "question_hi": (
            "निम्नलिखित चित्रों का अध्ययन करें और 3 के विपरीत संख्या का पता लगाएं।"
        ),
        "image_url": None,
        "option_a": "6",
        "option_b": "4",
        "option_c": "5",
        "option_d": "2",
        "correct_answer": "C",   # opp(3) = 5
    },

    # ── Q50 ──────────────────────────────────────────────────────────────────
    # Three positions; find opp(2).
    # From I & III: 1 < 3-2-6 / 3-5-4 → middle-face pair: opp(2) = 5.
    {
        "question_number": 50,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Study the following figures and find out the number opposite to 2."
        ),
        "question_hi": (
            "निम्नलिखित चित्रों का अध्ययन करें और 2 के विपरीत संख्या का पता लगाएं।"
        ),
        "image_url": None,
        "option_a": "1",
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
