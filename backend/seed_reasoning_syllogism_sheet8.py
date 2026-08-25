"""
seed_reasoning_syllogism_sheet8.py
====================================
Seeds Reasoning → Syllogism  Q27–Q30 (Sheet 8).
Subject : Reasoning
Topic   : Syllogism

Q27 — standard 2-conclusion 4-opt (CHSL 02 July 2024 Shift-1)
Q28 — standard 2-conclusion 4-opt (CHSL 02 July 2024 Shift-3)
Q29 — standard 2-conclusion 4-opt (CHSL 02 July 2024 Shift-2)
Q30 — standard 2-conclusion 4-opt (GD Constable 21 Feb 2024 Shift-2)

Answer key:
  Q27  B   Q28  C   Q29  B   Q30  B

Reasoning notes
───────────────
Q27  All journals→books (A); Some books are fans (I); All fans→wood (A).
     J = journals, Bo = books, Fa = fans, W = wood.

     Conclusion I:  Some journals are wood (Some J are W).
         Chain attempt 1: All J→Bo (A) + Some Bo are Fa (I)
           Middle term Bo: undistributed as predicate (A) and as subject (I).
           Fallacy of undistributed middle → no "Some J are Fa." ✗
         Chain attempt 2: Some Bo are Fa + All Fa→W → Darii → Some Bo are W.
           Then All J→Bo + Some Bo are W: same fallacy (Bo undistributed in both).
           "Some J are W" still can't be derived. ✗

     Conclusion II: Some fans are books (Some Fa are Bo).
         I-conversion of Stmt II (Some Bo are Fa → Some Fa are Bo) ✓

     Only conclusion II follows.

Q28  Some bottles are pens (I); All pens→tables (A); All tables→glasses (A).
     Bo = bottles, Pe = pens, T = tables, G = glasses.

     Barbara chain: All Pe→T (A) + All T→G (A) → All Pe→G.

     Step 1: Some Bo are Pe (I) + All Pe→T (A): Darii → Some Bo are T.
     Step 2: Some Bo are T (I) + All T→G (A):  Darii → Some Bo are G.

     Conclusion I:  Some glasses are bottles (Some G are Bo).
         I-conversion of derived "Some Bo are G" ✓

     Conclusion II: Some pens are glasses (Some Pe are G).
         All Pe→G (Barbara, derived) → Subalternation → Some Pe are G ✓

     Both I and II follow.

Q29  All shirts→pants (A); Some dresses are pants (I); Some pants are ties (I).
     Sh = shirts, Pa = pants, Dr = dresses, Ti = ties.

     Conclusion I:  Some dresses are ties (Some Dr are Ti).
         Attempt: Some Dr are Pa (I) + Some Pa are Ti (I).
         Two particular (I-type) premises → no valid syllogistic conclusion. ✗

     Conclusion II: Some ties are pants (Some Ti are Pa).
         I-conversion of Stmt III (Some Pa are Ti → Some Ti are Pa) ✓

     Only conclusion II follows.

Q30  All L are V (A); No L is J (E).

     Conclusion I:  All V are L (All V → L).
         All L→V is A-type. A-type converts only to I-type by subalternation-
         then-conversion: All L→V → Some L are V → I-conv: Some V are L.
         "All V are L" (A-type) does NOT follow from "All L are V." ✗
         (Classic error: confusing "All A is B" with "All B is A.")

     Conclusion II: No J is L (No J is L).
         E-conversion of Stmt II: No L is J → No J is L ✓

     Only conclusion II follows.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Syllogism"

# Standard 2-conclusion options
_A = "Only conclusion I follows. / केवल निष्कर्ष I अनुसरण करता है।"
_B = "Only conclusion II follows. / केवल निष्कर्ष II अनुसरण करता है।"
_C = "Both conclusions I and II follow. / दोनों निष्कर्ष I और II अनुसरण करते हैं।"
_D = "Neither conclusion I nor II follows. / न तो निष्कर्ष I और न ही II अनुसरण करता है।"

QUESTIONS = [

    # ── Q27 (CHSL, 02 July 2024 Shift-1) ────────────────────────────────────
    # All journals→books; Some books are fans; All fans→wood.
    # I:  Some journals are wood → undistributed middle (Bo) in both chains ✗
    # II: Some fans are books   → I-conv of Stmt II ✓
    {
        "question_number": 27,
        "difficulty": "medium",
        "source_pdf": "CHSL_02July2024_Shift1",
        "question_en": (
            "Three statements are followed by conclusions I and II. You have to "
            "consider these statements to be true, even if they seem to be at "
            "variance with commonly known facts. Decide which of the given "
            "conclusions logically follow/s from the given statements.\n\n"
            "Statements:\n"
            "All journals are books.\n"
            "Some books are fans.\n"
            "All fans are wood.\n\n"
            "Conclusion (I):  Some journals are wood.\n"
            "Conclusion (II): Some fans are books."
        ),
        "question_hi": (
            "तीन कथनों के बाद निष्कर्ष I और II दिए गए हैं। आपको इन कथनों को सत्य "
            "मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों। "
            "निर्णय लीजिए कि दिए गए निष्कर्षों में से कौन-सा/से कथनों का तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी पत्रिकाएँ पुस्तकें हैं।\n"
            "कुछ पुस्तकें पंखे हैं।\n"
            "सभी पंखे लकड़ी हैं।\n\n"
            "निष्कर्ष (I):  कुछ पत्रिकाएँ लकड़ी हैं।\n"
            "निष्कर्ष (II): कुछ पंखे पुस्तकें हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q28 (CHSL, 02 July 2024 Shift-3) ────────────────────────────────────
    # Some bottles are pens (I); All pens→tables (A); All tables→glasses (A).
    # Barbara: All Pe→G (derived).
    # I:  Some glasses are bottles → derived Some Bo are G → I-conv: Some G are Bo ✓
    # II: Some pens are glasses   → subalternation of All Pe→G ✓
    {
        "question_number": 28,
        "difficulty": "medium",
        "source_pdf": "CHSL_02July2024_Shift3",
        "question_en": (
            "Three statements are followed by conclusions numbered I and II. "
            "You have to consider these statements to be true, even if they seem "
            "to be at variance with commonly known facts. Decide which of the given "
            "conclusions logically follow/s from the given statements.\n\n"
            "Statements:\n"
            "Some bottles are pens.\n"
            "All pens are tables.\n"
            "All tables are glasses.\n\n"
            "Conclusion (I):  Some glasses are bottles.\n"
            "Conclusion (II): Some pens are glasses."
        ),
        "question_hi": (
            "तीन कथनों के बाद I और II अंकित निष्कर्ष दिए गए हैं। आपको इन कथनों को "
            "सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते "
            "हों। निर्णय लीजिए कि दिए गए निष्कर्षों में से कौन-सा/से कथनों का "
            "तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ बोतल पेन हैं।\n"
            "सभी पेन टेबल हैं।\n"
            "सभी टेबल ग्लास हैं।\n\n"
            "निष्कर्ष (I):  कुछ ग्लास बोतल हैं।\n"
            "निष्कर्ष (II): कुछ पेन ग्लास हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
    },

    # ── Q29 (CHSL, 02 July 2024 Shift-2) ────────────────────────────────────
    # All shirts→pants (A); Some dresses are pants (I); Some pants are ties (I).
    # I:  Some dresses are ties → I+I = two particular premises, no conclusion ✗
    # II: Some ties are pants   → I-conv of Stmt III (Some Pa are Ti → Some Ti are Pa) ✓
    {
        "question_number": 29,
        "difficulty": "medium",
        "source_pdf": "CHSL_02July2024_Shift2",
        "question_en": (
            "Three statements are followed by conclusions numbered I and II. "
            "You have to consider these statements to be true, even if they seem "
            "to be at variance with commonly known facts. Decide which of the given "
            "conclusions logically follow/s from the given statements.\n\n"
            "Statements:\n"
            "All shirts are pants.\n"
            "Some dresses are pants.\n"
            "Some pants are ties.\n\n"
            "Conclusion (I):  Some dresses are ties.\n"
            "Conclusion (II): Some ties are pants."
        ),
        "question_hi": (
            "तीन कथनों के बाद I और II अंकित निष्कर्ष दिए गए हैं। आपको इन कथनों को "
            "सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते "
            "हों। निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी शर्ट, पैंट हैं।\n"
            "कुछ ड्रेस, पैंट हैं।\n"
            "कुछ पैंट, टाई हैं।\n\n"
            "निष्कर्ष (I):  कुछ ड्रेस, टाई हैं।\n"
            "निष्कर्ष (II): कुछ टाई, पैंट हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q30 (GD Constable, 21 Feb 2024 Shift-2) ──────────────────────────────
    # All L are V (A); No L is J (E).
    # I:  All V are L (All V → L)
    #     A-type "All L is V" converts only to I-type via subalternation then
    #     I-conversion: Some V are L — NOT "All V are L." ✗
    #     (Classic trap: "All A is B" ≠ "All B is A.")
    # II: No J is L
    #     E-conversion of Stmt II: No L is J → No J is L ✓
    {
        "question_number": 30,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_21Feb2024_Shift2",
        "question_en": (
            "In the following question below are given some statements followed by "
            "some conclusions based on those statements. Taking the given statements "
            "to be true even if they seem to be at variance from commonly known facts. "
            "Read all the conclusions and then decide which of the given conclusion(s) "
            "logically follows the given statements.\n\n"
            "Statements:\n"
            "I.  All L are V.\n"
            "II. No L is J.\n\n"
            "Conclusions:\n"
            "I.  All V are L.\n"
            "II. No J is L."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कुछ कथन और उनके बाद उन कथनों पर आधारित कुछ "
            "निष्कर्ष दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, भले ही वे "
            "सामान्य ज्ञात तथ्यों से भिन्न प्रतीत होते हों, सभी निष्कर्षों को "
            "पढ़िए और तय कीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "I.  सभी L, V हैं।\n"
            "II. कोई L, J नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  सभी V, L हैं।\n"
            "II. कोई J, L नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
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
