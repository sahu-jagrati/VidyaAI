"""
seed_reasoning_syllogism_sheet1.py
====================================
Seeds Reasoning → Syllogism  Q1–Q3 (Sheet 1).
Subject : Reasoning
Topic   : Syllogism

Standard 4-option format for all questions:
  (A) Only conclusion I follows.
  (B) Only conclusion II follows.
  (C) Both conclusions I and II follow.
  (D) Neither conclusion I nor II follows.

Answer key:
  Q1  A  (CGL Tier II, 18 Jan 2025)
  Q2  D  (CGL Tier II, 20 Jan 2025)
  Q3  C  (GD Constable, 21 Feb 2024 Shift-4)

Reasoning notes
───────────────
Q1  All sheep→cows; Some cows→horses; All horses→jackals.
    I:  Some jackals are cows
        [Some cows are horses + All horses→jackals] → Some cows are jackals
        → by conversion: Some jackals are cows ✓
    II: Some horses are sheep
        [All sheep→cows] + [Some cows are horses] — the horses could be
        exactly those cows that are NOT sheep; we cannot conclude any
        horse is a sheep ✗

Q2  All dolls→robots; Some robots are toys; Some toys are cycles.
    I:  Some toys are dolls
        [All D→R] + [Some R are T] — those robot-toys need not be dolls ✗
    II: No cycle is a robot
        [Some R are T] + [Some T are C] — two I-type premises give no
        definite conclusion; some cycles may or may not be robots ✗

Q3  No mountains are deserts; Some deserts are sandy places;
    Some sandy places are mountains.
    I:  Some deserts are not mountains
        [No M is D] → No D is M → All deserts are non-mountains
        → Some deserts are not mountains ✓
    II: Some sandy places are mountains
        Directly stated as Statement III ✓
    Note: the Hindi rendering in the source image incorrectly includes
    "नहीं" in Statement III; the English ("are mountains") is correct
    and consistent with Conclusion II.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Syllogism"

# Standard 4-option set
_A = "Only conclusion I follows. / केवल निष्कर्ष I अनुसरण करता है।"
_B = "Only conclusion II follows. / केवल निष्कर्ष II अनुसरण करता है।"
_C = "Both conclusions I and II follow. / दोनों निष्कर्ष I और II अनुसरण करते हैं।"
_D = "Neither conclusion I nor II follows. / न तो निष्कर्ष I और न ही II अनुसरण करता है।"

QUESTIONS = [

    # ── Q1 (CGL Tier II, 18 Jan 2025) ────────────────────────────────────────
    # I:  Some jackals are cows  ✓  (Some cows→horses + All horses→jackals
    #     → Some cows are jackals → convert: Some jackals are cows)
    # II: Some horses are sheep  ✗  (horses may be the subset of cows
    #     that are NOT sheep; no valid link forces horse → sheep)
    {
        "question_number": 1,
        "difficulty": "medium",
        "source_pdf": "CGL_TierII_18Jan2025",
        "question_en": (
            "Statements:\n"
            "All sheep are cows.\n"
            "Some cows are horses.\n"
            "All horses are jackals.\n\n"
            "Conclusions:\n"
            "I.  Some jackals are cows.\n"
            "II. Some horses are sheep."
        ),
        "question_hi": (
            "कथन:\n"
            "सभी भेड़ें, गायें हैं।\n"
            "कुछ गायें, घोड़े हैं।\n"
            "सभी घोड़े, सियार हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ सियार, गायें हैं।\n"
            "II. कुछ घोड़े, भेड़ें हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
    },

    # ── Q2 (CGL Tier II, 20 Jan 2025) ────────────────────────────────────────
    # I:  Some toys are dolls  ✗  (All D→R and Some R are T — the toys
    #     that are robots need not be dolls; no definite conclusion)
    # II: No cycle is a robot  ✗  (two particular premises; cannot draw
    #     a universal negative; cycles and robots may overlap)
    {
        "question_number": 2,
        "difficulty": "medium",
        "source_pdf": "CGL_TierII_20Jan2025",
        "question_en": (
            "Statements:\n"
            "All dolls are robots.\n"
            "Some robots are toys.\n"
            "Some toys are cycles.\n\n"
            "Conclusions:\n"
            "I.  Some toys are dolls.\n"
            "II. No cycle is a robot."
        ),
        "question_hi": (
            "कथन:\n"
            "सभी गुड़िया, रोबोट हैं।\n"
            "कुछ रोबोट, खिलौने हैं।\n"
            "कुछ खिलौने, साइकिल हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ खिलौने, गुड़िया हैं।\n"
            "II. कोई साइकिल, रोबोट नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q3 (GD Constable, 21 Feb 2024 Shift-4) ───────────────────────────────
    # Stmts: No M is D; Some D are SP; Some SP are M.
    # I:  Some deserts are not mountains  ✓
    #     (No M is D → No D is M → All D are non-M → Some D are not M)
    # II: Some sandy places are mountains  ✓
    #     (directly stated as Statement III)
    {
        "question_number": 3,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_21Feb2024_Shift4",
        "question_en": (
            "Three Statements are given followed by two conclusions numbered "
            "I and II. Assuming the statements to be true, decide which of the "
            "conclusions logically follow(s).\n\n"
            "Statement I:   No mountains is deserts.\n"
            "Statement II:  Some deserts are sandy places.\n"
            "Statement III: Some sandy places are mountains.\n\n"
            "Conclusion I:  Some deserts are not mountains.\n"
            "Conclusion II: Some sandy places are mountains."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का "
            "तार्किक रूप से अनुसरण करता है/करते हैं।\n\n"
            "कथन I:   कोई भी पर्वत रेगिस्तान नहीं है।\n"
            "कथन II:  कुछ रेगिस्तान रेतीले स्थान हैं।\n"
            "कथन III: कुछ रेतीले स्थान पर्वत हैं।\n\n"
            "निष्कर्ष I:  कुछ रेगिस्तान पर्वत नहीं हैं।\n"
            "निष्कर्ष II: कुछ रेतीले स्थान पर्वत हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
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
        }

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
        print(f"\nDone -- inserted: {inserted}, skipped: {skipped}")

    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
