"""
seed_reasoning_syllogism_sheet4.py
====================================
Seeds Reasoning → Syllogism  Q12–Q16 (Sheet 4).
Subject : Reasoning
Topic   : Syllogism

Q12 — 3-conclusion custom 4-opt (GD Constable 20 Feb 2024 Shift-4)
Q13 — standard 2-conclusion 4-opt (CHSL 02 July 2024 Shift-4)
Q14 — standard 2-conclusion 4-opt (CPO 27 June 2024 Shift-3)
Q15 — standard 2-conclusion 4-opt (CPO 27 June 2024 Shift-2)
Q16 — standard 2-conclusion 4-opt (CPO 27 June 2024 Shift-2)

Answer key:
  Q12  B   Q13  D   Q14  B   Q15  D   Q16  C

Reasoning notes
───────────────
Q12  Some namkeen are pizza (I); No pizza is biscuit (E).
     I:  No biscuit is namkeen
         We know no pizza-biscuit exists, but non-pizza namkeen could be
         biscuits. Universal negative impossible to derive. ✗
     II: No biscuit is pizza → E-conversion of Stmt II ✓
     III:Some pizza are not biscuit → No P is B → All P ⊆ non-B →
         Some P are not B (sub-altern of E to O) ✓
     Both II and III follow (option B).

Q13  All fire→water (A); Some water are earth (I); No earth is air (E).
     I:  Some fire is earth
         A + I with W as middle: W is predicate in "All F is W" (undistributed)
         and subject in "Some W are E" (undistributed) → Fallacy of
         undistributed middle → no valid conclusion. ✗
     II: Some fire is air
         No valid chain from fire to air via the given premises. ✗
     Neither I nor II follows.

Q14  All wings→whites (A); No whites are wands (E).
     I:  Some wings are wands
         All W→Wh + No Wh is Wa → Celarent: No W is Wa.
         "Some wings are wands" contradicts this. ✗
     II: No wand is a white → E-conversion of Stmt II ✓
     Only II follows.

Q15  All tablets→medicines (A); Some medicines are ointments (I).
     Middle term M: undistributed in A-predicate and I-subject.
     Fallacy of undistributed middle → no valid conclusion possible.
     I:  Some tablets are ointments ✗
     II: All ointments are medicines → cannot upgrade I-type to A-type. ✗
     Neither I nor II follows.

Q16  All pineapples→papayas (A); All papayas→pears (A).
     Barbara (A+A→A): All pineapples→pears.
     I:  All pineapples are pears ✓
     II: Some pears are pineapples
         All Pi→Pe → Subalternation: Some Pi are Pe → I-conversion: Some Pe are Pi ✓
     Both I and II follow.
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

    # ── Q12 (GD Constable, 20 Feb 2024 Shift-4) ─────────────────────────────
    # 3-conclusion question with custom option set.
    # Some namkeen are pizza (I); No pizza is biscuit (E).
    # I:  No biscuit is namkeen    → ✗ (non-pizza namkeen could be biscuits)
    # II: No biscuit is pizza      → ✓ (E-conv of Stmt II)
    # III:Some pizza are not biscuit → ✓ (O sub-altern of E: No P is B → Some P are not B)
    # Both II and III follow → option B.
    {
        "question_number": 12,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_20Feb2024_Shift4",
        "question_en": (
            "In the following question below are given some statements followed by some "
            "conclusions based on those statements. Taking the given statements to be "
            "true even if they seem to be at variance from commonly known facts. Read "
            "all the conclusions and then decide which of the given conclusion(s) "
            "logically follows the given statements.\n\n"
            "Statements:\n"
            "I.  Some namkeen are pizza.\n"
            "II. No pizza is biscuit.\n\n"
            "Conclusions:\n"
            "I.   No biscuit is namkeen.\n"
            "II.  No biscuit is pizza.\n"
            "III. Some pizza are not biscuit."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कुछ कथन और उनके बाद उन कथनों पर आधारित कुछ "
            "निष्कर्ष दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, भले ही वे "
            "सामान्य ज्ञात तथ्यों से भिन्न प्रतीत होते हों, सभी निष्कर्षों को "
            "पढ़िए और फिर तय कीजिए कि दिए गए निष्कर्षों में से कौन-सा/से दिए गए "
            "कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "I.  कुछ नमकीन पिज़्ज़ा हैं।\n"
            "II. कोई पिज़्ज़ा बिस्किट नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.   कोई बिस्किट नमकीन नहीं है।\n"
            "II.  कोई बिस्किट पिज़्ज़ा नहीं है।\n"
            "III. कुछ पिज़्ज़ा बिस्किट नहीं हैं।"
        ),
        "option_a": "Both conclusions I and III follow. / निष्कर्ष I और III दोनों अनुसरण करते हैं।",
        "option_b": "Both conclusions II and III follow. / निष्कर्ष II और III दोनों अनुसरण करते हैं।",
        "option_c": "Only conclusion III follows. / केवल निष्कर्ष III अनुसरण करता है।",
        "option_d": "All conclusions follow. / सभी निष्कर्ष अनुसरण करते हैं।",
        "correct_answer": "B",
    },

    # ── Q13 (CHSL, 02 July 2024 Shift-4) ────────────────────────────────────
    # All fire→water (A); Some water are earth (I); No earth is air (E).
    # I:  Some fire is earth  → A+I, middle W undistributed → no valid conclusion ✗
    # II: Some fire is air    → no valid chain F→Air ✗
    {
        "question_number": 13,
        "difficulty": "medium",
        "source_pdf": "CHSL_02July2024_Shift4",
        "question_en": (
            "Three statements are followed by conclusions numbered I and II. "
            "You have to consider these statements to be true, even if they seem "
            "to be at variance with commonly known facts. Decide which of the "
            "given conclusions logically follow/s from the given statement.\n\n"
            "Statements:\n"
            "All fire is water.\n"
            "Some water is earth.\n"
            "No earth is air.\n\n"
            "Conclusions:\n"
            "(I):  Some fire is earth.\n"
            "(II): Some fire is air."
        ),
        "question_hi": (
            "तीन कथनों के बाद I और II अंकित निष्कर्ष दिए गए हैं। आपको इन "
            "कथनों को सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों। निर्णय लीजिए कि दिए गए निष्कर्षों में से कौन-सा/से "
            "कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी आग, पानी हैं।\n"
            "कुछ पानी, मिट्टी हैं।\n"
            "कोई मिट्टी, वायु नहीं है।\n\n"
            "निष्कर्ष:\n"
            "(I):  कुछ आग, मिट्टी हैं।\n"
            "(II): कुछ आग, वायु हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q14 (CPO, 27 June 2024 Shift-3) ─────────────────────────────────────
    # All wings→whites (A); No whites are wands (E).
    # I:  Some wings are wands → Celarent gives No wings are wands; "Some" impossible ✗
    # II: No wand is a white   → E-conversion of Stmt II ✓
    {
        "question_number": 14,
        "difficulty": "easy",
        "source_pdf": "CPO_27June2024_Shift3",
        "question_en": (
            "Two statements are given, followed by two conclusions I and II. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s).\n\n"
            "Statements:\n"
            "All wings are whites.\n"
            "No whites are wands.\n\n"
            "Conclusions:\n"
            "I.  Some wings are wands.\n"
            "II. No wand is a white."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं, जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी पंख सफेद हैं।\n"
            "कोई सफेद छड़ी नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ पंख छड़ी हैं।\n"
            "II. कोई छड़ी सफेद नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q15 (CPO, 27 June 2024 Shift-2) ─────────────────────────────────────
    # All tablets→medicines (A); Some medicines are ointments (I).
    # Middle term M: undistributed as predicate (A) AND as subject (I).
    # Fallacy of undistributed middle → no valid conclusion.
    # I:  Some tablets are ointments → ✗
    # II: All ointments are medicines → cannot upgrade I-type to A-type ✗
    {
        "question_number": 15,
        "difficulty": "medium",
        "source_pdf": "CPO_27June2024_Shift2",
        "question_en": (
            "Two statements are given, followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s).\n\n"
            "Statements:\n"
            "All tablets are medicines.\n"
            "Some medicines are ointments.\n\n"
            "Conclusions:\n"
            "I.  Some tablets are ointments.\n"
            "II. All ointments are medicines."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं, जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी गोलियाँ दवाइयाँ हैं।\n"
            "कुछ दवाइयाँ मलहम हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ गोलियाँ मलहम हैं।\n"
            "II. सभी मलहम दवाइयाँ हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q16 (CPO, 27 June 2024 Shift-2) ─────────────────────────────────────
    # All pineapples→papayas (A); All papayas→pears (A).
    # I:  All pineapples are pears → Barbara (A+A→A) ✓
    # II: Some pears are pineapples
    #     All Pi→Pe → Subalternation → Some Pi are Pe → I-conversion: Some Pe are Pi ✓
    {
        "question_number": 16,
        "difficulty": "easy",
        "source_pdf": "CPO_27June2024_Shift2",
        "question_en": (
            "Three statements are given, followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s).\n\n"
            "Statements:\n"
            "All pineapples are papayas.\n"
            "All papayas are pears.\n\n"
            "Conclusions:\n"
            "I.  All pineapples are pears.\n"
            "II. Some pears are pineapples."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं, जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी अनानास पपीते हैं।\n"
            "सभी पपीते नाशपाती हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  सभी अनानास नाशपाती हैं।\n"
            "II. कुछ नाशपाती अनानास हैं।"
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
