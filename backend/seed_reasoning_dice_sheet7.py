"""
seed_reasoning_dice_sheet7.py
==============================
Seeds Reasoning → Dice  Q27–Q36.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q27 D  (6)
     Four positions of a dice; find bottom of position III.
     From pos I & III (spine analysis): opp(3) = 6.
     In position III, face 3 is on top → bottom = 6.

Q28 B  (Box b)
     Standard dice: opposite faces always sum to 7 (1↔6, 2↔5, 3↔4).
     Only box (b) shows a face arrangement consistent with this rule.
     All others violate the standard pairing.

Q29 A  (Box a)
     Same standard dice rule (opp faces = 7).
     Only box (a) is consistent; boxes (b),(c),(d) each show
     a pair of opposite faces as adjacent.

Q30 C  (15)
     Standard dice: top + bottom = 7 for each die.
     4 dice tops = 13 (shown: 4, 3, 1, 5).
     Total bottoms = 7×4 − 13 = 28 − 13 = 15.
     Individual: 4→3, 3→4, 1→6, 5→2 (sum = 15).

Q31 A  (3)
     Two positions; find face opposite to 2 (two dots).
     Spine analysis (i) & (ii): 6 < 1-3-5 / 1-2-4 → opp(3) = 2.
     i.e. opp(2) = 3. When 2 at bottom → 3 at top.

Q32 C  (1)
     Two positions; find face opposite to 2.
     Spine analysis: 4 < 3-6-1 / 3-5-2 → opp(1) = 2.
     i.e. opp(2) = 1. When 2 at bottom → 1 at top.

Q33 B  (6)
     Two positions; find face opposite to 2.
     Spine analysis: 1 < 3-4-6 / 3-5-2 → opp(6) = 2.
     i.e. opp(2) = 6. When 2 at bottom → 6 at top.

Q34 C  (5)
     Two positions of a parallelepiped; find bottom when 3 is on top.
     Spine analysis: 4 < 2-1-5 / 2-6-3 → opp(5) = 3.
     i.e. opp(3) = 5. When 3 on top → 5 at bottom.

Q35 D  (5)
     Two positions of a block; find top when 6 is at bottom.
     Spine analysis: 5 < 6-2-1 / 6-4-3 → opp(5) = 6.
     i.e. opp(6) = 5. When 6 at bottom → 5 at top.

Q36 A  (a)
     Faces a, b, c, d written clockwise on the four side faces;
     e = top, f = bottom (given).
     In a clockwise ring a→b→c→d→a, opposite side pairs are:
       opp(a)=c  and  opp(b)=d.
     Also opp(e)=f (top↔bottom, given).
     When c is rotated to the top → a (opposite c) goes to the bottom.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Dice"

QUESTIONS = [

    # ── Q27 ──────────────────────────────────────────────────────────────────
    # Four positions of a dice; find bottom of position III.
    # From positions I & III: opp(3) = 6 → bottom in pos III = 6.
    {
        "question_number": 27,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Four positions of a dice are shown below. What number must be at the "
            "bottom face when the dice is in the position shown in figure (III)?"
        ),
        "question_hi": (
            "एक पासे की चार अलग-अलग स्थितियाँ नीचे दिखाई गई हैं। जब पासा चित्र (III) "
            "में दिखाई गई स्थिति में हो तो नीचे की सतह पर कौन-सी संख्या होगी?"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "2",
        "option_c": "4",
        "option_d": "6",
        "correct_answer": "D",   # opp(3) = 6; pos III has 3 on top → bottom = 6
    },

    # ── Q28 ──────────────────────────────────────────────────────────────────
    # Standard dice (opposite faces sum to 7); identify valid figure.
    # Only box (b) is consistent with 1↔6, 2↔5, 3↔4.
    {
        "question_number": 28,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "If the total number of dots on opposite faces of a cubical block is always 7, "
            "find the figure which is correct?"
        ),
        "question_hi": (
            "यदि किसी घन के विपरीत सतहों पर बिंदुओं की कुल संख्या हमेशा 7 होती है, "
            "तो कौन सी आकृति सही है?"
        ),
        "image_url": None,
        "option_a": "Box (a) / डिब्बा (a)",
        "option_b": "Box (b) / डिब्बा (b)",
        "option_c": "Box (c) / डिब्बा (c)",
        "option_d": "Box (d) / डिब्बा (d)",
        "correct_answer": "B",   # only (b) is a valid standard dice
    },

    # ── Q29 ──────────────────────────────────────────────────────────────────
    # Standard dice (opposite faces sum to 7); identify valid figure.
    # Only box (a) is consistent.
    {
        "question_number": 29,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Amongst the following figures, find the correct one, if it is known that "
            "the total number of dots on opposite faces of the cube is always 7?"
        ),
        "question_hi": (
            "निम्नलिखित आकृतियों में से सही आकृति ज्ञात कीजिए, यदि यह ज्ञात हो कि "
            "घन के विपरीत फलकों पर बिंदुओं की कुल संख्या हमेशा 7 होती है?"
        ),
        "image_url": None,
        "option_a": "Box (a) / डिब्बा (a)",
        "option_b": "Box (b) / डिब्बा (b)",
        "option_c": "Box (c) / डिब्बा (c)",
        "option_d": "Box (d) / डिब्बा (d)",
        "correct_answer": "A",   # only (a) is a valid standard dice
    },

    # ── Q30 ──────────────────────────────────────────────────────────────────
    # 4 standard dice; tops sum to 13; find total of bottom faces.
    # Top→Bottom: 4→3, 3→4, 1→6, 5→2. Total bottom = 3+4+6+2 = 15.
    # Shortcut: 7×4 − 13 = 15.
    {
        "question_number": 30,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Four standard dices are thrown on the ground. The total of numbers on the "
            "top faces of these four dice is 13 as the top faces showed 4, 3, 1 and 5 "
            "respectively. What is the total of the faces touching the ground?"
        ),
        "question_hi": (
            "चार मानक पासों को जमीन पर फेंका जाता है। इन चार पासों के ऊपरी सतहों पर "
            "कुल संख्या 13 है और ऊपरी सतहों पर क्रमशः 4, 3, 1 और 5 दिखाई देती है। "
            "जमीन को छूने वाली सतहों की कुल संख्याओं का योग क्या होगा?"
        ),
        "image_url": None,
        "option_a": "11",
        "option_b": "13",
        "option_c": "15",
        "option_d": "Cannot be determined / तय नहीं किया जा सकता",
        "correct_answer": "C",   # 7×4 − 13 = 15
    },

    # ── Q31 ──────────────────────────────────────────────────────────────────
    # Two dice positions; find top when 2 (two dots) is at bottom.
    # Spine: 6 < 1-3-5 / 1-2-4 → opp(2) = 3.
    {
        "question_number": 31,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Two positions of a dice are shown below. When there are two dots at the "
            "bottom, the number at the top will be?"
        ),
        "question_hi": (
            "एक पासे की दो स्थितियाँ नीचे दिखाई गई हैं। जब दो बिंदु सबसे नीचे होते "
            "हैं, तो ऊपरी सतह पर बिंदुओं की संख्या होगी?"
        ),
        "image_url": None,
        "option_a": "3",
        "option_b": "5",
        "option_c": "6",
        "option_d": "Cannot be determined / तय नहीं किया जा सकता",
        "correct_answer": "A",   # opp(2) = 3
    },

    # ── Q32 ──────────────────────────────────────────────────────────────────
    # Two dice positions; find top when 2 is at bottom.
    # Spine: 4 < 3-6-1 / 3-5-2 → opp(2) = 1.
    {
        "question_number": 32,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Two positions of a dice are shown below. When 2 is at the bottom, what "
            "number will be at the top?"
        ),
        "question_hi": (
            "एक पासे की दो नीचे-दिखाए गए चित्र हैं। जब 2 सबसे नीचे होती है, "
            "तो ऊपरी सतह पर कौन-सी संख्या होगी?"
        ),
        "image_url": None,
        "option_a": "6",
        "option_b": "3",
        "option_c": "1",
        "option_d": "5",
        "correct_answer": "C",   # opp(2) = 1
    },

    # ── Q33 ──────────────────────────────────────────────────────────────────
    # Two dice positions; find top when 2 is at bottom.
    # Spine: 1 < 3-4-6 / 3-5-2 → opp(2) = 6.
    {
        "question_number": 33,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Two positions of a dice are shown below. When 2 is at the bottom, which "
            "number will be at the top?"
        ),
        "question_hi": (
            "एक पासे की दो स्थितियाँ नीचे दिखाई गई हैं। जब 2 सबसे नीचे होता है, "
            "तो ऊपरी सतह पर कौन-सी संख्या होगी?"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "6",
        "option_c": "5",
        "option_d": "4",
        "correct_answer": "B",   # opp(2) = 6
    },

    # ── Q34 ──────────────────────────────────────────────────────────────────
    # Two positions of a parallelepiped; find bottom when 3 is on top.
    # Spine: 4 < 2-1-5 / 2-6-3 → opp(3) = 5.
    {
        "question_number": 34,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Two positions of a parallelopiped are shown below. When the number 3 will "
            "be on the top side, then which number will be at the bottom?"
        ),
        "question_hi": (
            "नीचे दिखाए गए पासे की दो स्थितियाँ हैं। यदि संख्या 3 सबसे ऊपर है, "
            "तो कौन-सी संख्या सबसे नीचे होगी?"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "4",
        "option_c": "5",
        "option_d": "6",
        "correct_answer": "C",   # opp(3) = 5
    },

    # ── Q35 ──────────────────────────────────────────────────────────────────
    # Two positions of a block; find top when 6 is at bottom.
    # Spine: 5 < 6-2-1 / 6-4-3 → opp(6) = 5.
    {
        "question_number": 35,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Two positions of a block are shown below. When six is at the bottom, "
            "what number will be at the top?"
        ),
        "question_hi": (
            "एक ब्लॉक के दो पदों को नीचे दिखाया गया है। जब छः सबसे नीचे होता है, "
            "तो ऊपरी सतह पर कौन-सी संख्या होगी?"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "2",
        "option_c": "4",
        "option_d": "5",
        "correct_answer": "D",   # opp(6) = 5
    },

    # ── Q36 ──────────────────────────────────────────────────────────────────
    # Letters a,b,c,d clockwise on side faces; e=top, f=bottom.
    # Clockwise ring a→b→c→d→a → opposite side pairs: opp(a)=c, opp(b)=d.
    # When c is rotated to top → a (opposite c) goes to bottom.
    {
        "question_number": 36,
        "difficulty": "hard",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In a dice, a, b, c and d are written on the adjacent faces in a clockwise "
            "order and e and f at the top and bottom. When c is at the top, what will "
            "be at the bottom?"
        ),
        "question_hi": (
            "एक पासे में a, b, c और d आसन्न सतहों पर एक दक्षिणावर्त क्रम में और ऊपर "
            "तथा नीचे e और f लिखे जाते हैं। जब c सबसे ऊपर है, तो सबसे नीचे क्या होगा?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "Data insufficient / डेटा अपर्याप्त",
        "correct_answer": "A",   # opp(a)=c in clockwise ring → when c on top, a at bottom
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
