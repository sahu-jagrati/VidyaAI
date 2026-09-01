"""
update_dice_q3_q4.py
====================
Replaces the wrong Q3 and Q4 in topic 'Dice' with the correct questions
from the GPSC JSO Pre Screening exams shown in the image.

Run from backend/ directory:
    python update_dice_q3_q4.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Dice"

UPDATES = {
    3: {
        "source_pdf":    "GPSC_JSO_Pre_Screening_29_01_2022",
        "difficulty":    "medium",
        "question_en": (
            "A dice is rolled twice and the two positions are shown in the figure below. "
            "What is the number of dots at the bottom face when the dice is in position (i)?"
        ),
        "question_hi": (
            "एक पासे को दो बार घुमाया जाता है और दोनों स्थितियों को नीचे दिए गए "
            "चित्र में दिखाया गया है। जब पासा स्थिति (i) में हो तो निचली सतह पर "
            "बिंदुओं की संख्या क्या है?"
        ),
        "option_a":      "1",
        "option_b":      "5",
        "option_c":      "6",
        "option_d":      "Cannot be determined / तय नहीं किया जा सकता",
        "correct_answer":"C",   # top of pos(i)=1 → bottom=6
        "image_url":     None,  # user will upload dice positions image
    },
    4: {
        "source_pdf":    "GPSC_JSO_Pre_Screening_19_11_2022",
        "difficulty":    "hard",
        "question_en": (
            "Choose the box that is similar to the box formed from the given sheet of paper (X). "
            "Which of the following boxes can be formed?"
        ),
        "question_hi": (
            "वह बॉक्स चुनें जो कागज की दी गई शीट (X) से बने बॉक्स के समान है। "
            "निम्नलिखित में से कौन सा/से बॉक्स बनाया/बनाए जा सकता/सकते है/हैं?"
        ),
        "option_a":      "1 and 2 only / केवल 1 और 2",
        "option_b":      "1 and 3 only / केवल 1 और 3",
        "option_c":      "3 and 4 only / केवल 3 और 4",
        "option_d":      "1, 2, 3 and 4 / 1, 2, 3 और 4",
        "correct_answer":"C",   # only boxes 3 and 4 consistent with net X
        "image_url":     None,  # user will upload net + cubes image
    },
}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    updated = 0
    try:
        for qnum, data in UPDATES.items():
            row = (
                db.query(Question)
                .filter(
                    Question.subject         == SUBJECT,
                    Question.topic           == TOPIC,
                    Question.question_number == qnum,
                )
                .first()
            )
            if row is None:
                print(f"  NOT FOUND Q{qnum}")
                continue
            for field, val in data.items():
                setattr(row, field, val)
            updated += 1
            print(f"  UPDATED Q{qnum} (id={row.id}) — {data['source_pdf']}")

        db.commit()
        print(f"\nDone — updated: {updated}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
