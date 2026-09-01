"""
seed_reasoning_dice_sheet3.py
==============================
Seeds Reasoning → Dice  Q11–Q15.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q11 C  (B — Blue)
     Net layout:
       (1,1)=R  (1,2)=B
       (2,1)=G  (2,2)=Y  (2,3)=O
       (3,1)=W
     Fold with Y as front: G→left, O→right, B→top,
     R (above G) →back, W (below G) →bottom.
     Pairs: {Y,R}, {G,O}, {B,W}  →  opp(White) = Blue (B).
     [GPSC BDO Repeat Pre Screening 18-12-2021 Set 1]

Q12 C  (4)
     Two dice positions; adjacency of 3:
       3 adj 5, 6 (pos-1)  →  3 adj 1, 2 (pos-2)
       3 adj {5,6,1,2}  →  opp(3) = 4.
     [WBCS Prelims 2020]

Q13 B  (3)
     Three dice positions; adjacency of 4:
       4 adj 1, 2 (pos-1); 4 adj 5, 6 (pos-2); pos-3 confirms.
       4 adj {1,2,5,6}  →  opp(4) = 3.
     [WBCS Prelims 2019]

Q14 A  (Four dots / चार बिंदु)
     Four positions of solid (faces: ·, ··, ···, ····, ×, —).
     From positions (I)–(IV): single dot (·) adj ×, —, ··, ···
       →  opp(·) = ···· (four dots).
     [UPSC Prelims CSAT 2018]

Q15 D  (Line / रेखा)
     Same four positions as Q14.
     Two dots (··) adj ·, ×, ···, ····
       →  opp(··) = — (line).
     [UPSC Prelims CSAT 2018]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Dice"

QUESTIONS = [

    # ── Q11 [GPSC BDO Repeat Pre Screening 18-12-2021 Set 1] ─────────────────
    # Net: R B / G Y O / W  (W is below G, col-1 row-3).
    # Fold: Y=front, G=left, O=right, B=top, R=back, W=bottom.
    # opp(White/W) = Blue/B.
    {
        "question_number": 11,
        "difficulty": "medium",
        "source_pdf": "GPSC_BDO_Repeat_Pre_Screening_18_12_2021_Set1",
        "question_en": (
            "Six squares are coloured — front and back: red (R), blue (B), yellow (Y), "
            "green (G), white (W) and orange (O) — as shown in the figure given below. "
            "If they were folded to form a cube what would be the face opposite to white colour?\n"
            "[Net: Row-1: R B | Row-2: G Y O | Row-3 (col-1): W]"
        ),
        "question_hi": (
            "छह वर्ग रंगीन हैं — आगे और पीछे: लाल (R), नीला (B), पीला (Y), हरा (G), "
            "सफेद (W) और नारंगी (O) — जैसा कि नीचे दिए गए चित्र में दिखाया गया है। "
            "यदि इन्हें मोड़कर एक घन बनाया जाए तो सफेद रंग के विपरीत फलक क्या होगा?\n"
            "[जाल: पंक्ति-1: R B | पंक्ति-2: G Y O | पंक्ति-3 (कॉल-1): W]"
        ),
        "image_url": None,
        "option_a": "R",
        "option_b": "G",
        "option_c": "B",
        "option_d": "O",
        "correct_answer": "C",   # opp(White) = Blue
    },

    # ── Q12 [WBCS Prelims 2020] ───────────────────────────────────────────────
    # Two dice positions shown; find dots opposite to 3 dots.
    # 3 adj 5,6 (pos-1); 3 adj 1,2 (pos-2) → opp(3) = 4.
    {
        "question_number": 12,
        "difficulty": "medium",
        "source_pdf": "WBCS_Prelims_2020",
        "question_en": (
            "Two positions of a dice are shown. Find the number of dots on the face "
            "opposite the face bearing 3 dots."
        ),
        "question_hi": (
            "एक पासे की दो स्थितियाँ दिखाई गई हैं। 3 बिंदुओं वाले चेहरे के विपरीत "
            "चेहरे पर बिंदुओं की संख्या ज्ञात कीजिए।"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "2",
        "option_c": "4",
        "option_d": "5",
        "correct_answer": "C",   # opp(3) = 4
    },

    # ── Q13 [WBCS Prelims 2019] ───────────────────────────────────────────────
    # Three dice positions (1–6 dots); find dots opposite to 4 dots.
    # 4 adj 1,2 (pos-1); 4 adj 5,6 (pos-2) → opp(4) = 3.
    {
        "question_number": 13,
        "difficulty": "medium",
        "source_pdf": "WBCS_Prelims_2019",
        "question_en": (
            "Observe the dots on a dice (one to six dots) in the following figures. "
            "How many dots are contained on the face opposite to that containing four dots?"
        ),
        "question_hi": (
            "निम्नलिखित आकृतियों में एक पासे पर बिंदुओं (एक से छह बिंदु) को देखें। "
            "चार बिंदुओं वाले फलक के विपरीत फलक पर कितने बिंदु हैं?"
        ),
        "image_url": None,
        "option_a": "2",
        "option_b": "3",
        "option_c": "6",
        "option_d": "Cannot be determined / तय नहीं किया जा सकता",
        "correct_answer": "B",   # opp(4) = 3
    },

    # ── Q14 [UPSC Prelims CSAT 2018] ─────────────────────────────────────────
    # Four positions of a solid with faces: · ·· ··· ···· × —
    # single dot adj ×, —, ··, ··· across positions → opp(·) = ····.
    {
        "question_number": 14,
        "difficulty": "hard",
        "source_pdf": "UPSC_CSAT_2018",
        "question_en": (
            "The rotated positions of a single solid are shown below. The various faces "
            "of the solid are marked with different symbols like dots, a cross, and a line. "
            "Answer the three items that follow the given figures.\n"
            "What is the symbol on the face opposite to that containing a single dot?"
        ),
        "question_hi": (
            "एकल ठोस की घुमाई गई स्थिति नीचे दिखाई गई है। ठोस के विभिन्न चेहरों को "
            "बिंदु, एक क्रॉस और एक रेखा जैसे विभिन्न प्रतीकों से चिह्नित किया जाता है। "
            "दिए गए आंकड़ों का पालन करने वाले तीन प्रश्नों के उत्तर दीजिए।\n"
            "एक बिंदु वाले चेहरे के विपरीत चेहरे पर कौन सा प्रतीक है?"
        ),
        "image_url": None,
        "option_a": "Four dots / चार बिंदु",
        "option_b": "Three dots / तीन बिंदु",
        "option_c": "Two dots / दो बिंदु",
        "option_d": "Cross / क्रॉस",
        "correct_answer": "A",   # opp(single dot) = four dots
    },

    # ── Q15 [UPSC Prelims CSAT 2018] ─────────────────────────────────────────
    # Same four solid positions as Q14.
    # two dots adj ·, ×, ···, ···· → opp(··) = — (line).
    {
        "question_number": 15,
        "difficulty": "hard",
        "source_pdf": "UPSC_CSAT_2018",
        "question_en": (
            "The rotated positions of a single solid are shown below. The various faces "
            "of the solid are marked with different symbols like dots, a cross, and a line. "
            "Answer the three items that follow the given figures.\n"
            "What is the symbol on the face opposite to that containing two dots?"
        ),
        "question_hi": (
            "एकल ठोस की घुमाई गई स्थिति नीचे दिखाई गई है। ठोस के विभिन्न चेहरों को "
            "बिंदु, एक क्रॉस और एक रेखा जैसे विभिन्न प्रतीकों से चिह्नित किया जाता है। "
            "दिए गए आंकड़ों का पालन करने वाले तीन प्रश्नों के उत्तर दीजिए।\n"
            "दो बिंदुओं वाले फलक के विपरीत फलक पर कौन सा चिह्न है?"
        ),
        "image_url": None,
        "option_a": "Single dot / एकल बिंदु",
        "option_b": "Three dots / तीन बिंदु",
        "option_c": "Four dots / चार बिंदु",
        "option_d": "Line / रेखा",
        "correct_answer": "D",   # opp(two dots) = line
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
