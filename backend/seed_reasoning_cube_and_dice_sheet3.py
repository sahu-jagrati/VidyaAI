"""
seed_reasoning_cube_and_dice_sheet3.py
=======================================
Seeds Reasoning → Cube and Dice  Q13–Q20 (DSSSB exam papers source).

question_numbers 13–20.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q13 B  (Only III)
     — Paper-folding net with symbols D,M,Z,#,@,$. Only cube III is
       consistent with all opposite-pair constraints derived from the net.
       [DSSSB DOE PRT - 07 March 2022 - Shift 2]

Q14 C  (27)
     — 5×5×5 = 125 cubes. All 6 faces are painted (2 black + 2 blue + 2 yellow).
       Interior (unpainted) cubes = (5−2)³ = 3³ = 27.
       [DSSSB PRT (Assistant Teacher Primary) - 25 March 2022 - Shift 1]

Q15 D  (8)
     — 4 cm cube divided by 2 cm cuts: 4÷2 = 2 per edge → 2³ = 8 small cubes.
       [DSSSB DOE PRT - 07 March 2022 - Shift]

Q16 D  (4)
     — Three dice positions; opposite of 6:
       Die-i: 6 adj 3,1  → opp(6)≠3,≠1
       Die-ii: 6 adj 2,? → opp(6)≠2
       → opp(6)=4. Options are {1,2,3,4}; answer=4.
       [DSSSB TGT SST (Female) - 09 Oct 2021 - Shift 2]

Q17 A  (2)
     — Two dice; opposite of 6:
       Die-i: 2 adj 1     → opp(2)≠1
       Die-ii: 4 adj 1,6  → opp(4)≠1,≠6; 6 adj 4,1 → opp(6)≠4,≠1
       Pairs resolved: {1,3},{4,?},{6,2}  → opp(6)=2.
       [DSSSB PGT Political Science (Male) - 04 July 2021]

Q18 C  (VI)
     — Three dice with Roman numerals I–VI; opposite of III:
       Die-I: IV,VI,V all visible  → mutually adjacent; opp(IV/V/VI) ∈ {I,II,III}
       Die-II: V adj II, V adj VI  → opp(V)≠II,≠VI → opp(V)∈{I,III}
       Die-II third face: II adj VI → opp(II)≠VI → opp(II)=IV.
       Remaining pairs: {V,I} and {III,VI}  → opp(III)=VI.
       [DSSSB TGT Hindi (Female) - 05 Sep 2021 - Shift 1]

Q19 A  (#)
     — Three dice with symbols #,@,$,%,!,⚫; opposite of @:
       From three positions, @ is adjacent to $,%,! and one other symbol;
       the only non-adjacent symbol = #  → opp(@)=#.
       [DSSSB TGT Maths (Male) - 02 Sep 2021 - Shift 2]

Q20 B  (6)
     — Three dice; opposite of 1:
       Die-1 (3,5,1): 1 adj 3,5  → opp(1)≠3,≠5
       Die-2 (6,5,4): 5 adj 6,4  → opp(5)≠6,≠4; combined opp(5)≠3,≠6,≠4 → opp(5)=1? No.
       Correct chain: Die-2 shows 6 adj 5, 6 adj 4 → opp(6)≠5,≠4.
       Die-3 (2,4): 2 adj 4 → opp(2)≠4.
       Pairs: opp(6)≠5,≠4 and opp(1)≠3,≠5 → opp(1)=2 or 6.
       Die-2 third visible face =4: 4 adj 5, 4 adj 6 → opp(4)≠5,≠6 → opp(4)∈{1,2,3}.
       opp(2)≠4 (die-3) → if opp(4)=2 then opp(2)=4 contradiction → opp(4)=1 or 3.
       If opp(4)=1: then opp(1)=4 — but 4 not in options {3,6,2,4}... wait 4 IS option D.
       Test opp(1)=6: pairs {1,6},{2,5},{3,4}. opp(4)=3 ✓(≠5,≠6 ✓).
         Die-1(3,5,1): 3 adj 5 ✓, 3 adj 1 ✓, 5 adj 1 ✓.
         Die-2(6,5,4): 6 adj 5 ✓, 6 adj 4 ✓, 5 adj 4 ✓.
         Die-3(2,4): 2 adj 4 ✓. All consistent → opp(1)=6.
       [DSSSB PGT Commerce (Male) - 28 June 2021 - Shift 1]
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

    # ── Q13 [DSSSB DOE PRT - 07 March 2022 - Shift 2] ───────────────────────
    # Paper/net with symbols D,M,Z,#,@,$ folded into a cube.
    # Which of the four assembled cubes (I–IV) can be formed?
    # Only cube III is consistent with the net's opposite-pair constraints.
    {
        "question_number": 13,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "When the given paper is folded, which of the following cubes can be formed?"
            "\n[Net shows six faces with symbols: D, M, Z, #, @, $]"
        ),
        "question_hi": (
            "दिए गए कागज को मोड़ने पर, निम्नलिखित में से कौन सा घन बनाया जा सकता है?"
            "\n[खुले घन में छह फलकों पर D, M, Z, #, @, $ प्रतीक हैं]"
        ),
        "image_url": None,
        "option_a": "II and III / II तथा III",
        "option_b": "Only III / केवल III",
        "option_c": "I, II and III / I, II तथा III",
        "option_d": "I and II / I तथा II",
        "correct_answer": "B",   # Only cube III can be made from the given net
    },

    # ── Q14 [DSSSB PRT - 25 March 2022 - Shift 1] ───────────────────────────
    # Solid cube split into 5×5×5=125 cubes; all 6 faces painted (2 black, 2 blue, 2 yellow).
    # Interior (no-face-painted) cubes = (5−2)³ = 27.
    {
        "question_number": 14,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "Two adjacent faces of a solid cube are painted with black colour. "
            "The faces opposite to the black faces are painted with blue colour "
            "while the remaining faces are painted with yellow colour. After "
            "painting, this cube has been divided into 125 equal cubes. "
            "How many cubes have no faces painted?"
        ),
        "question_hi": (
            "एक ठोस घन के दो आसन्न फलकों को काले रंग से रंगा गया है। काले "
            "फलकों के विपरीत फलकों को नीले रंग से रंगा गया है जबकि शेष "
            "फलकों को पीले रंग से रंगा गया है। रंगने के बाद, इस घन को 125 "
            "बराबर घनों में विभाजित किया गया है। कितने घनों का कोई फलक "
            "रंगे नहीं हैं?"
        ),
        "image_url": None,
        "option_a": "8",
        "option_b": "35",
        "option_c": "27",
        "option_d": "24",
        "correct_answer": "C",   # (5−2)³ = 3³ = 27 interior cubes have no faces painted
    },

    # ── Q15 [DSSSB DOE PRT - 07 March 2022 - Shift] ─────────────────────────
    # 4 cm cube painted green, then divided into 2 cm cubes.
    # Per edge: 4÷2=2 → total 2³=8 small cubes.
    {
        "question_number": 15,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            "A cube of side 4 cm is painted green on all its faces and then divided "
            "into smaller cubes with every 2 cm sides. How many small cubes are obtained?"
        ),
        "question_hi": (
            "4 सेमी भुजा वाले एक घन को सभी फलकों पर हरे रंग से रंगा गया है "
            "तथा फिर प्रत्येक 2 सेमी भुजा वाले छोटे घनों में विभाजित किया "
            "गया है। कितने छोटे घन प्राप्त होते हैं?"
        ),
        "image_url": None,
        "option_a": "4",
        "option_b": "64",
        "option_c": "27",
        "option_d": "8",
        "correct_answer": "D",   # 4 cm ÷ 2 cm = 2 per edge → 2³ = 8 small cubes
    },

    # ── Q16 [DSSSB TGT SST (Female) - 09 Oct 2021 - Shift 2] ────────────────
    # Three dice positions; if 6 is on bottom, what number is on top (opp of 6)?
    # Die-i: 6 adj 3,1; die-ii: 6 adj 2,? → opp(6)=4 (the only unchosen number).
    {
        "question_number": 16,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "Three positions of a dice are given below. If '6' is on the bottom "
            "face, then what can come on the top face?"
        ),
        "question_hi": (
            "नीचे एक पासे की तीन स्थितियाँ दी गई हैं। यदि नीचे वाले फलक पर "
            "'6' है, तो ऊपर वाले फलक पर क्या आएगा?"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "2",
        "option_c": "3",
        "option_d": "4",
        "correct_answer": "D",   # opp(6) = 4
    },

    # ── Q17 [DSSSB PGT Political Science (Male) - 04 July 2021] ─────────────
    # Dice with faces 1–6; two positions shown. Which number is opposite to 6?
    # Die-ii: 6 adj 4,1 → opp(6)≠4,≠1. Pairs resolved → opp(6)=2.
    {
        "question_number": 17,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "In the following question, a die has six faces 1, 2, 3, 4, 5 and 6. "
            "Two positions of the same cube are given. Which number is opposite to number 6?"
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में, एक पासे के छह फलक 1, 2, 3, 4, 5 और 6 हैं। "
            "एक ही पासे की दो स्थितियाँ दी गई हैं। कौन सी संख्या संख्या 6 के "
            "विपरीत है?"
        ),
        "image_url": None,
        "option_a": "2",
        "option_b": "5",
        "option_c": "3",
        "option_d": "6",
        "correct_answer": "A",   # opp(6) = 2
    },

    # ── Q18 [DSSSB TGT Hindi (Female) - 05 Sep 2021 - Shift 1] ──────────────
    # Three different positions of same dice with Roman numerals I–VI.
    # Die-I: IV,VI,V visible → mutually adjacent; opp of each ∈ {I,II,III}.
    # Die-II: V adj II, II adj VI → opp(II)=IV; remaining pairs {V,I},{III,VI}.
    # → opp(III) = VI.
    {
        "question_number": 18,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Three different positions of the same dice are given below. "
            "Find the symbol opposite of (III)."
        ),
        "question_hi": (
            "नीचे एक ही पासे की तीन अलग-अलग स्थितियाँ दी गई हैं। (III) के "
            "विपरीत चिह्न ज्ञात कीजिए।"
        ),
        "image_url": None,
        "option_a": "IV",
        "option_b": "V",
        "option_c": "VI",
        "option_d": "I",
        "correct_answer": "C",   # opp(III) = VI
    },

    # ── Q19 [DSSSB TGT Maths (Male) - 02 Sep 2021 - Shift 2] ────────────────
    # Three different positions of same dice with symbols #,@,$,%,!,⚫.
    # From positions: @ is adjacent to $,%,! and ⚫; only # is not adjacent → opp(@)=#.
    {
        "question_number": 19,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "Three different positions of the same dice are given below. "
            "Which symbol is on the face opposite to the face showing '@'?"
        ),
        "question_hi": (
            "एक ही पासे की तीन अलग-अलग स्थितियाँ नीचे दी गई हैं। '@' दर्शाने "
            "वाले फलक के विपरीत फलक पर कौन सा चिह्न है?"
        ),
        "image_url": None,
        "option_a": "#",
        "option_b": "%",
        "option_c": "!",
        "option_d": "$",
        "correct_answer": "A",   # # is opposite to @
    },

    # ── Q20 [DSSSB PGT Commerce (Male) - 28 June 2021 - Shift 1] ────────────
    # Three dice positions; what number is opposite to 1?
    # Die-1(3,5,1): 1 adj 3,5 → opp(1)≠3,≠5.
    # Die-2(6,5,4): 5 adj 6,4 → opp(5)≠6,≠4; 6 adj 5,4 → opp(6)≠5,≠4.
    # Die-3(2,4): 2 adj 4 → opp(2)≠4.
    # Pairs {1,6},{2,5},{3,4}: all constraints satisfied → opp(1)=6.
    {
        "question_number": 20,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Three different positions of the same dice are shown. "
            "What will be the number on the face opposite to the side having '1'?"
        ),
        "question_hi": (
            "एक ही पासे की तीन अलग-अलग स्थितियाँ दर्शाई गई हैं। "
            "'1' वाले पक्ष के विपरीत फलक पर कौन सी संख्या होगी?"
        ),
        "image_url": None,
        "option_a": "3",
        "option_b": "6",
        "option_c": "2",
        "option_d": "4",
        "correct_answer": "B",   # opp(1) = 6; pairs: {1,6},{2,5},{3,4}
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
