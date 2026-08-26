"""
seed_reasoning_cube_and_dice_sheet4.py
=======================================
Seeds Reasoning → Cube and Dice  Q21–Q25 (DSSSB exam papers source).

question_numbers 21–25.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q21 B  (6)
     — Three dice positions; opposite of face with 3 dots:
       Die-i: 3 adj 5,1  → opp(3)≠5,≠1
       Die-ii: 3 adj 2,4 → opp(3)≠2,≠4
       → only 6 remains → opp(3)=6.
       [DSSSB PGT English (Female) - 30 June 2021 - Shift 2]

Q22 A  (% and $)
     — Net layout: column spine %–#–$–@ (rows 1-4 in column 2);
       & is branch LEFT of %; ★ is branch RIGHT of $.
       Spine rule (A-B-C-D strip): opp(A)=C, opp(B)=D.
       → opp(%)=$, opp(#)=@, opp(&)=★.
       Option A "% and $" is the correct opposite pair.
       [DSSSB TGT Maths (Male) - 02 Sep 2021 - Shift 1]

Q23 B  (I and III)
     — Net with numbers on faces (T/L shape); opposite pairs derived.
       Cube I and Cube III are consistent with all constraints.
       Cubes II and IV show at least one contradictory adjacent-opposite pair.
       [DSSSB TGT SST (Female) - 09 Oct 2021 - Shift 2]

Q24 A  (Figure 1)
     — Cross-adjacent net: spine 1–2–4–5 (col 2, rows 1-4);
       branches: 3 (left of 4) and 6 (right of 4).
       Pairs: {1,4}, {2,5}, {3,6}.
       Figure 1 shows 1 on top and 4 on a side face (adjacent) →
       opp(1)=4 means they CANNOT appear adjacent → IMPOSSIBLE.
       [DSSSB PGT Chemistry (Female) - 18 July 2021 - Shift 1]

Q25 B  (Figure 2)
     — Net with symbols △,☆,○,◇,□,and another shape.
       Figure 2 is the only assembled cube whose visible-face combinations
       are consistent with the opposite-pair constraints from the net.
       [DSSSB TGT Hindi (Female) - 04 Sep 2021 - Shift 3]
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

    # ── Q21 [DSSSB PGT English (Female) - 30 June 2021 - Shift 2] ────────────
    # Three dice positions; how many dots opposite to face bearing 3 dots?
    # Die-i: 3 adj 5,1 → Die-ii: 3 adj 2,4 → opp(3)=6.
    {
        "question_number": 21,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "Three different positions of the same dice are given below. "
            "How many dots will be opposite to the face bearing 3 dots?"
        ),
        "question_hi": (
            "एक ही पासे की तीन अलग-अलग स्थितियाँ नीचे दी गई हैं। "
            "3 बिंदु वाले फलक के विपरीत फलक पर कितने बिंदु होंगे?"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "6",
        "option_c": "2",
        "option_d": "5",
        "correct_answer": "B",   # opp(3) = 6
    },

    # ── Q22 [DSSSB TGT Maths (Male) - 02 Sep 2021 - Shift 1] ────────────────
    # Sheet net with 6 symbols: &, %, #, $, ★, @.
    # Net: spine (col 2) = %–#–$–@; branch left of % = &; branch right of $ = ★.
    # Pairs: {%,$}, {#,@}, {&,★}.
    # Which pair of symbols will be on opposite sides?
    {
        "question_number": 22,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "A cube is made by folding the given sheet. In the cube so formed, "
            "which of the following pairs of symbols will be on opposite sides?\n"
            "[Net layout: spine (top→bottom) = %, #, $, @; "
            "branch left of % = &; branch right of $ = ★]"
        ),
        "question_hi": (
            "दी गई शीट को मोड़कर एक घन बनाया जाता है। इस प्रकार बने घन "
            "में निम्नलिखित में से प्रतीकों का कौन सा युग्म विपरीत भुजाओं पर "
            "होगा?\n"
            "[खुले घन में: ऊपर से नीचे %, #, $, @; & बाईं ओर % से; ★ दाईं ओर $ से]"
        ),
        "image_url": None,
        "option_a": "% and $ / % और $",
        "option_b": "# and ★ / # और ★",
        "option_c": "@ and % / @ और %",
        "option_d": "& and $ / & और $",
        "correct_answer": "A",   # % and $ are opposite (spine pair: %↔$)
    },

    # ── Q23 [DSSSB TGT SST (Female) - 09 Oct 2021 - Shift 2] ────────────────
    # Net with numbered faces; which of cubes I–IV can be made?
    # From net constraints, only cubes I and III satisfy all opposite-pair rules.
    {
        "question_number": 23,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "By folding the given paper, which of the following cube can be made?\n"
            "[Net shows numbered faces arranged in T/L shape with numbers 1–6]"
        ),
        "question_hi": (
            "दिए गए कागज को मोड़कर निम्नलिखित में से कौन सा घन बनाया जा सकता है?\n"
            "[दिए गए जाल में 1–6 अंकों वाले फलक T/L आकार में व्यवस्थित हैं]"
        ),
        "image_url": None,
        "option_a": "I, II, III and IV / I, II, III और IV",
        "option_b": "I and III / I और III",
        "option_c": "I, II and IV / I, II और IV",
        "option_d": "II and IV / II और IV",
        "correct_answer": "B",   # Only cubes I and III can be formed
    },

    # ── Q24 [DSSSB PGT Chemistry (Female) - 18 July 2021 - Shift 1] ──────────
    # Cross-shaped net with numbers 1–6.
    # Net: spine (col 2) = 1–2–4–5; branch left of 4 = 3; branch right of 4 = 6.
    # Opposite pairs: {1,4}, {2,5}, {3,6}.
    # Figure 1 shows 1 (top) adjacent to 4 (side) → opp(1)=4 → IMPOSSIBLE.
    {
        "question_number": 24,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Which of the following figures cannot be formed on folding "
            "the given cube in the question?\n"
            "[Net: cross shape with 1 at top, 2 below, 3-4-6 horizontal row, "
            "5 at bottom; opposite pairs: {1,4},{2,5},{3,6}]"
        ),
        "question_hi": (
            "प्रश्न में दिए गए घन को मोड़ने पर निम्नलिखित में से कौन सी आकृति "
            "नहीं बन सकती है?\n"
            "[जाल: 1 ऊपर, 2 नीचे, 3-4-6 क्षैतिज पंक्ति, 5 सबसे नीचे; "
            "विपरीत युग्म: {1,4},{2,5},{3,6}]"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "2",
        "option_c": "3",
        "option_d": "4",
        "correct_answer": "A",   # Figure 1 shows 1 adjacent to 4 — impossible (they are opposite)
    },

    # ── Q25 [DSSSB TGT Hindi (Female) - 04 Sep 2021 - Shift 3] ──────────────
    # Net with geometric symbols (△, ☆, ○, ◇, □, and another shape).
    # Which assembled cube figure CAN be formed from this net?
    # Figure 2 is the only one consistent with the net's opposite-pair constraints.
    {
        "question_number": 25,
        "difficulty": "hard",
        "source_pdf": SOURCE,
        "question_en": (
            "Which of the following figures can be formed by folding "
            "the given cube in the question?\n"
            "[Net shows geometric symbols: triangle △, star ☆, circle ○, "
            "diamond ◇, square □ and one more shape on six faces]"
        ),
        "question_hi": (
            "प्रश्न में दिए गए घन को मोड़कर निम्नलिखित में से कौन सी आकृति "
            "बनाई जा सकती है?\n"
            "[जाल में छह फलकों पर ज्यामितीय प्रतीक हैं: त्रिभुज △, तारा ☆, "
            "वृत्त ○, हीरा ◇, वर्ग □ और एक अन्य आकृति]"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "2",
        "option_c": "3",
        "option_d": "4",
        "correct_answer": "B",   # Figure 2 can be formed from the given net
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
