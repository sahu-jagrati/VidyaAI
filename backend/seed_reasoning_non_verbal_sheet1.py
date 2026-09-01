"""
seed_reasoning_non_verbal_sheet1.py
========================================
Seeds Reasoning → Non-Verbal  Q1–Q4.
All four questions are mirror-image (looking-glass) type.

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_non_verbal_image_urls_batch1.py.

Bucket  : question_image_Non_Verbal
Pattern : non_verbal_{N}.png

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q1  B  Mirror at PC (right-side vertical line).
     Original: clock face with arrow pointing NE (~2 o'clock).
     Left-right reflection → arrow moves to NW (~10 o'clock). → B.

Q2  D  Mirror at MN (right-side vertical line).
     Original: jug/mug facing left (handle on left).
     Left-right reflection → jug faces right (handle on right). → D.

Q3  B  Mirror held as shown (right-side vertical line at Y).
     Original: Hindi characters "ढ़ूक" type figure.
     Left-right reflection → characters appear correctly mirrored. → B.

Q4  B  Mirror at MN (left-side vertical; N at top, M at bottom).
     Original: tree/node diagram with branches.
     Left-right reflection → branches swap sides. → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Non-Verbal"

QUESTIONS = [

    # ── Q1 ───────────────────────────────────────────────────────────────────
    # Clock face; arrow at NE. Mirror at PC (right-side vertical).
    # Left-right reflection: NE arrow → NW. Answer option (b).
    {
        "question_number": 1,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the answer figures is exactly the mirror image of the "
            "given figure when the mirror is held at PC?"
        ),
        "question_hi": (
            "जब दर्पण को PC पर रखा जाता है तो कौन सी उत्तर आकृति दी गई "
            "आकृति की दर्पण छवि होती है?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Right-side vertical mirror flips figure left-right;
        # arrow at NE moves to NW position in option (b).
    },

    # ── Q2 ───────────────────────────────────────────────────────────────────
    # Jug/mug facing left. Mirror at MN (right-side vertical).
    # Left-right reflection: jug faces right. Answer option (d).
    {
        "question_number": 2,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the answer figures is exactly the mirror image of the "
            "given figure when the mirror is held at MN?"
        ),
        "question_hi": (
            "जब दर्पण को MN पर रखा जाता है तो कौन सी उत्तर आकृति दी गई "
            "आकृति की दर्पण छवि होती है?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "D",
        # Right-side vertical mirror flips figure left-right;
        # jug (handle left) → jug (handle right) in option (d).
    },

    # ── Q3 ───────────────────────────────────────────────────────────────────
    # Hindi characters figure. Mirror held as shown (right vertical at Y).
    # Left-right reflection of characters. Answer option (b).
    {
        "question_number": 3,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the answer figures is exactly the mirror image of the "
            "given figure when mirror is held as shown?"
        ),
        "question_hi": (
            "दिखाए गए अनुसार दर्पण को पकड़ने पर कौन सी उत्तर आकृति दी गई "
            "आकृति की बिलकुल दर्पण छवि होती है?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Right-side vertical mirror (at Y line) flips the Hindi
        # character figure horizontally; option (b) shows correct reflection.
    },

    # ── Q4 ───────────────────────────────────────────────────────────────────
    # Tree/node diagram. Mirror at MN (left-side vertical; N=top, M=bottom).
    # Left-right reflection: branches swap sides. Answer option (b).
    {
        "question_number": 4,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "If a mirror is placed on the line MN, then which of the answer "
            "figures is the correct image of the given question figure?"
        ),
        "question_hi": (
            "यदि एक दर्पण को रेखा MN पर रखा जाए, तो कौन सी उत्तर आकृति "
            "दी गई प्रश्न आकृति की सही छवि है?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Left-side vertical mirror (MN) flips tree/node diagram left-right;
        # branches and nodes appear on swapped sides in option (b).
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Non-Verbal Q1–Q4 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload non_verbal_1.png … non_verbal_4.png to Supabase bucket "
                "'question_image_Non_Verbal', then run:\n"
                "  python update_non_verbal_image_urls_batch1.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
