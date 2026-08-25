"""
seed_reasoning_syllogism_sheet3.py
====================================
Seeds Reasoning → Syllogism  Q8–Q11 (Sheet 3).
Subject : Reasoning
Topic   : Syllogism

NOTE: Q8 previously seeded incorrectly (kites/tables/clocks reconstruction).
This script REPLACES Q8 with the correct GD Constable question and inserts Q9–Q11.

All use standard 2-conclusion 4-option format:
  A = Only conclusion I follows.
  B = Only conclusion II follows.
  C = Both conclusions I and II follow.
  D = Neither conclusion I nor II follows.

Sources (all GD Constable, 29 Feb 2024):
  Q8  Shift-1   Q9  Shift-4   Q10  Shift-2   Q11  Shift-3

Answer key:
  Q8  A   Q9  A   Q10  B   Q11  D

Reasoning notes
───────────────
Q8  No bridge is a mountain (E); Some mountains are monuments (I);
    All monuments are harbors (A).
    I:  Some harbors are mountains
        Some M are Mo + All Mo→H → Some M are H; I-conv: Some H are M ✓
    II: No bridge is a monument
        No B is M + Some M are Mo → can't extend the negation:
        monuments that are not mountains might be bridges. ✗

Q9  Some A are B (I); Some B are K (I); All K are J (A).
    I:  Some B are J
        Some B are K + All K→J → Some B are J (I+A→I) ✓
    II: Some A are J
        Some A are B + Some B are K → I+I = no valid conclusion.
        A↛K, so A↛J. ✗

Q10 No M are N (E); Some O are N (I).
    I:  All O are M
        O that are N cannot be M (No M is N). At least some O are
        non-M, so "All O are M" is impossible. ✗
    II: No N is M
        E-conversion of Stmt I: No M is N → No N is M ✓

Q11 All mathematicians→logical thinkers (A);
    Some logical thinkers are scientists (I);
    Some scientists are fools (I).
    I:  Some scientists are not fools
        "Some S are F" ≠ "Some S are not F"; all could be fools. ✗
    II: Some logical thinkers are not scientists
        "Some L are S" ≠ "Some L are not S"; all L could be S. ✗
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Syllogism"

_A = "Only conclusion I follows. / केवल निष्कर्ष I अनुसरण करता है।"
_B = "Only conclusion II follows. / केवल निष्कर्ष II अनुसरण करता है।"
_C = "Both conclusions I and II follow. / दोनों निष्कर्ष I और II अनुसरण करते हैं।"
_D = "Neither conclusion I nor II follows. / न तो निष्कर्ष I और न ही II अनुसरण करता है।"

QUESTIONS = [

    # ── Q8 (GD Constable, 29 Feb 2024 Shift-1) ──────────────────────────────
    # [REPLACEMENT] Previously stored kites/tables/clocks is incorrect.
    # No bridge is a mountain; Some mountains are monuments; All monuments are harbors.
    # I:  Some harbors are mountains  ✓ (Some M→Mo→H; I-conv: Some H are M)
    # II: No bridge is a monument     ✗ (No B is M can't extend to No B is Mo;
    #     non-mountain monuments could be bridges)
    {
        "question_number": 8,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_29Feb2024_Shift1",
        "question_en": (
            "Three Statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s) from the statements.\n\n"
            "Statement I:   No bridge is a mountain.\n"
            "Statement II:  Some mountains are monuments.\n"
            "Statement III: All monuments are harbors.\n\n"
            "Conclusion I:  Some harbors are mountains.\n"
            "Conclusion II: No bridge is a monument."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन I:   कोई पुल पहाड़ नहीं है।\n"
            "कथन II:  कुछ पहाड़ स्मारक हैं।\n"
            "कथन III: सभी स्मारक बंदरगाह हैं।\n\n"
            "निष्कर्ष I:  कुछ बंदरगाह पहाड़ हैं।\n"
            "निष्कर्ष II: कोई पुल स्मारक नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
    },

    # ── Q9 (GD Constable, 29 Feb 2024 Shift-4) ──────────────────────────────
    # Some A are B; Some B are K; All K are J.
    # I:  Some B are J  → Some B are K + All K→J → Some B are J (I+A→I) ✓
    # II: Some A are J  → Some A are B + Some B are K = I+I (no valid conclusion) ✗
    {
        "question_number": 9,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_29Feb2024_Shift4",
        "question_en": (
            "Three Statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s) from the statements.\n\n"
            "Statement I:   Some A are B.\n"
            "Statement II:  Some B are K.\n"
            "Statement III: All K are J.\n\n"
            "Conclusion I:  Some B are J.\n"
            "Conclusion II: Some A are J."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन I:   कुछ A, B हैं।\n"
            "कथन II:  कुछ B, K हैं।\n"
            "कथन III: सभी K, J हैं।\n\n"
            "निष्कर्ष I:  कुछ B, J हैं।\n"
            "निष्कर्ष II: कुछ A, J हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
    },

    # ── Q10 (GD Constable, 29 Feb 2024 Shift-2) ─────────────────────────────
    # No M are N; Some O are N.
    # I:  All O are M  → O that are N must be non-M (No M is N); impossible. ✗
    # II: No N is M    → E-conversion of Stmt I directly ✓
    {
        "question_number": 10,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_29Feb2024_Shift2",
        "question_en": (
            "In the following question below are given some statements followed by "
            "some conclusions based on those statements. Taking the given statements "
            "to be true even if they seem to be at variance from commonly known facts. "
            "Read all the conclusions and then decide which of the given conclusion(s) "
            "logically follows the given statements.\n\n"
            "Statements:\n"
            "No M are N.\n"
            "Some O are N.\n\n"
            "Conclusions:\n"
            "I.  All O are M.\n"
            "II. No N is M."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कुछ कथन और उनके बाद उन कथनों पर आधारित कुछ "
            "निष्कर्ष दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, भले ही वे "
            "सामान्य ज्ञात तथ्यों से भिन्न प्रतीत होते हों, सभी निष्कर्षों को "
            "पढ़िए और फिर तय कीजिए कि दिए गए निष्कर्षों में से कौन-सा/से दिए गए "
            "कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "I.  कोई M, N नहीं है।\n"
            "II. कुछ O, N हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  सभी O, M हैं।\n"
            "II. कोई N, M नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q11 (GD Constable, 29 Feb 2024 Shift-3) ─────────────────────────────
    # All mathematicians→logical thinkers; Some logical thinkers are scientists;
    # Some scientists are fools.
    # I:  Some scientists are not fools
    #     "Some S are F" does not imply "Some S are not F" (all could be fools) ✗
    # II: Some logical thinkers are not scientists
    #     "Some L are S" does not imply "Some L are not S" (all L could be S) ✗
    {
        "question_number": 11,
        "difficulty": "hard",
        "source_pdf": "GD_Constable_29Feb2024_Shift3",
        "question_en": (
            "Three Statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s) from the statements.\n\n"
            "Statement I:   All mathematicians are logical thinkers.\n"
            "Statement II:  Some logical thinkers are scientists.\n"
            "Statement III: Some scientists are fools.\n\n"
            "Conclusion I:  Some scientists are not fools.\n"
            "Conclusion II: Some logical thinkers are not scientists."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन I:   सभी गणितज्ञ तार्किक विचारक हैं।\n"
            "कथन II:  कुछ तार्किक विचारक वैज्ञानिक हैं।\n"
            "कथन III: कुछ वैज्ञानिक मूर्ख हैं।\n\n"
            "निष्कर्ष I:  कुछ वैज्ञानिक मूर्ख नहीं हैं।\n"
            "निष्कर्ष II: कुछ तार्किक विचारक वैज्ञानिक नहीं हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = replaced = skipped = 0
    try:
        existing = {
            row[0]: row[1]
            for row in db.query(Question.question_number, Question.id)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        for d in QUESTIONS:
            qn = d["question_number"]
            if qn in existing:
                # Delete the old record and re-insert (used for Q8 replacement)
                old = db.query(Question).filter(Question.id == existing[qn]).one()
                db.delete(old)
                db.flush()
                db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
                db.flush()
                print(f"  REPLACE Q{qn}  (old record deleted, new inserted)")
                replaced += 1
            else:
                db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
                inserted += 1
                print(f"  INSERT  Q{qn}")

        db.commit()
        print(f"\nDone -- inserted: {inserted}, replaced: {replaced}, skipped: {skipped}")

    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
