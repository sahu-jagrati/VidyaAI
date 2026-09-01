"""
seed_reasoning_non_verbal_sheet3.py
========================================
Seeds Reasoning → Non-Verbal  Q10–Q13.

Q10  = Mirror image (mirror at AB, right-side vertical)
Q11  = Paper folding & cutting (fold → cut → unfold)
Q12  = Paper folding & punching (fold → punch → unfold)
Q13  = Paper folding & punching (different fold)

NOTE: image_url = None; upload images to Supabase and run
      update_non_verbal_image_urls_batch3.py.

Bucket  : question_image_Non_Verbal
Pattern : non_verbal_{N}.png

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q10 A  Mirror at AB (right-side vertical; A=top, B=bottom).
     Original: compass/flower design with arrows in 4 cardinal directions.
     Left-right reflection → option (a) shows the correct mirror image. → A.

Q11 B  Paper folded twice (into quarters) then a diagonal/corner cut is made.
     Unfolding reveals the cut pattern in all 4 quadrants → 4 diamond shapes.
     Option (b) shows this symmetrical diamond pattern. → B.

Q12 C  Paper folded into quarters then punched at 2 positions.
     Each punch × 4 (two-fold symmetry) → 8 holes arranged symmetrically
     when fully unfolded. Option (c) shows the correct pattern. → C.

Q13 B  Paper folded with a different fold pattern, then punched.
     Unfolding reveals a specific symmetric hole arrangement.
     Option (b) shows the correct unfolded pattern. → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Non-Verbal"

QUESTIONS = [

    # ── Q10 ──────────────────────────────────────────────────────────────────
    # Compass/flower figure. Mirror at AB (right-side vertical; A=top).
    # Left-right flip: answer option (a).
    {
        "question_number": 10,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the answer figures is exactly the mirror image of the "
            "question figure, when the mirror is held on the line AB?"
        ),
        "question_hi": (
            "जब दर्पण को रेखा AB पर रखा जाता है, तो कौन सी उत्तर आकृति "
            "वास्तव में प्रश्न आकृति की दर्पण छवि है?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "A",
        # Right-side vertical mirror (AB) flips the compass/flower figure left-right;
        # option (a) shows the correct mirror image.
    },

    # ── Q11 ──────────────────────────────────────────────────────────────────
    # Paper fold + cut. Folded twice → diagonal cut in corner.
    # Unfolding: 4 symmetric diamond shapes appear.
    {
        "question_number": 11,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following questions, a piece of paper is folded and cut as "
            "shown below. From the given answer figures indicate how it will "
            "appear when opened."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों में, कागज के एक टुकड़े को नीचे दिखाए "
            "अनुसार मोड़ा और काटा गया है। दिए गए उत्तर आंकड़ों से पता "
            "चलता है कि खोलने पर यह कैसा दिखाई देगा।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Paper folded twice → diagonal/corner cut → 4 symmetric diamond shapes
        # appear when fully unfolded; option (b) shows this pattern.
    },

    # ── Q12 ──────────────────────────────────────────────────────────────────
    # Paper fold + punch. Folded into quarters → 2 holes punched.
    # Unfolding: 8 holes in symmetric pattern.
    {
        "question_number": 12,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "A piece of paper is folded and punched as shown in the figure "
            "below. How will it appear when unfolded?"
        ),
        "question_hi": (
            "कागज के एक टुकड़े को मोड़कर छेद किया जाता है जैसा कि नीचे "
            "दिए गए चित्र में दिखाया गया है। खुलने पर यह कैसा दिखाई देगा?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "C",
        # Paper folded into quarters → 2 circular punches → 8 holes arranged
        # symmetrically when unfolded; option (c) shows the correct pattern.
    },

    # ── Q13 ──────────────────────────────────────────────────────────────────
    # Paper fold + punch (different fold pattern). Holes appear symmetrically.
    {
        "question_number": 13,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "A piece of paper is folded and punched as shown below. From the "
            "given responses, indicate how it will appear when opened."
        ),
        "question_hi": (
            "कागज के एक टुकड़े को नीचे दिखाए अनुसार मोड़कर छेद किया जाता "
            "है। दिए गए उत्तरों से बताएं कि खोलने पर यह कैसा दिखाई देगा।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Different fold + punch pattern → specific symmetric hole arrangement;
        # option (b) shows the correct unfolded result.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Non-Verbal Q10–Q13 into '{TOPIC}' / '{SUBJECT}'")

        for d in QUESTIONS:
            qn = d["question_number"]
            exists = (
                db.query(Question)
                .filter(
                    Question.subject == SUBJECT,
                    Question.topic == TOPIC,
                    Question.question_number == qn,
                )
                .first()
            )
            if exists:
                print(f"  SKIP  Q{qn}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
            inserted += 1
            print(f"  INSERT Q{qn}")

        db.commit()
        print(f"\nDone — inserted: {inserted}, skipped: {skipped}")
        if inserted:
            print(
                "\n  Upload non_verbal_10.png … non_verbal_13.png to Supabase bucket "
                "'question_image_Non_Verbal', then run:\n"
                "  python update_non_verbal_image_urls_batch3.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
