"""
seed_reasoning_syllogism_sheet10.py
=====================================
Seeds Reasoning → Syllogism  Q37–Q42 (Sheet 10).
Subject : Reasoning
Topic   : Syllogism

All questions use standard 2-conclusion 4-option format.

Q37 [GD Constable 22 Feb 2024 Shift-4]  → B (Only II)
Q38 [GD Constable 24 Feb 2024 Shift-1]  → D (Both)
Q39 [GD Constable 24 Feb 2024 Shift-4]  → A (Neither)
Q40 [CHSL 03 July 2024 Shift-1]         → B (Only II)
Q41 [GD Constable 24 Feb 2024 Shift-3]  → A (Only I)
Q42 [GD Constable 26 Feb 2024 Shift-1]  → A (Only I)

Reasoning notes
───────────────
Q37  Some Eng are Doc (I); All Doc→Law (A); Some Law not Tea (O).
     Derived: Darii: Some Eng are Doc + All Doc→Law → Some Eng are Law.

     I:   Some lawyers are teachers (Some Law are Tea).
          Stmt III is O-type: "Some Law are not Tea" — O-type does NOT imply
          I-type; presence of non-teacher-lawyers says nothing about teacher-
          lawyers. No premise yields "Some Law are Tea." ✗

     II:  Some engineers are lawyers (Some Eng are Law).
          Darii: Some Eng are Doc (I) + All Doc→Law (A) → Some Eng are Law ✓

     Only conclusion II follows.

Q38  No A is B (E); Some B are P (I).

     I:   Some B are not A (Some B are not A).
          E-conversion of Stmt I: No A is B → No B is A.
          No B is A → subalternation: Some B are not A ✓

     II:  Some P are not A (Some P are not A).
          From E-conv: No B is A  ↔  B∩A = ∅.
          From Stmt II: B∩P ≠ ∅  (there exist x ∈ B∩P).
          For any such x: x ∈ B and B∩A = ∅, so x ∉ A.
          x ∈ P and x ∉ A  →  Some P are not A ✓
          (Equivalently, Ferio: Some B are P (I) + No B is A (E) →
          Some P are not A (O), re-labelling with minor=P, middle=B, major=A.)

     Both conclusions I and II follow.

Q39  No red is black (E); No rat is black (E).
     Re = red, Ra = rat, Bl = black.

     Two E-type premises sharing the same predicate (black). In syllogistic
     logic, two negative premises yield no valid conclusion. The relationship
     between reds and rats is completely unconstrained:

     Scenario 1: All reds are rats  — consistent.
     Scenario 2: No red is a rat    — consistent.
     Scenario 3: Some reds are rats — consistent.

     I:   Some rats are not red  → Cannot derive. ✗
     II:  Some red are not rats  → Cannot derive. ✗

     Neither conclusion follows.

Q40  All paints→houses (A); All houses→wood (A); Some streets are wood (I).
     Pa = paints, Ho = houses, Wo = wood, St = streets.

     Barbara chain: All Pa→Ho + All Ho→Wo → All Pa→Wo.

     I:   Some streets are houses (Some St are Ho).
          We know Some St are Wo. But Ho ⊆ Wo (not Wo ⊆ Ho); streets can be
          non-house wood (planks, flooring, etc.). ✗

     II:  All paints are wood (All Pa→Wo).
          Barbara: All Pa→Ho + All Ho→Wo → All Pa→Wo ✓

     Only conclusion II follows.

Q41  All bicycles→wheels (A); Some wheels are rubber (I); No rubber is plastic (E).
     Bi = bicycles, Wh = wheels, Ru = rubber, Pl = plastic.

     I:   Some wheels are bicycles (Some Wh are Bi).
          All Bi→Wh (A) → Subalternation: Some Bi are Wh →
          I-conversion: Some Wh are Bi ✓

     II:  Some wheels are plastics (Some Wh are Pl).
          Ferio: Some Wh are Ru (I) + No Ru is Pl (E) →
          Some Wh are NOT Pl (O-type).
          Conclusion II is the OPPOSITE of what is derivable. ✗

     Only conclusion I follows.

Q42  No S is T (E); Some U are S (I).
     S, T, U are abstract classes.

     I:   Some U are not T (Some U are not T).
          Ferio: Some U are S (I) + No S is T (E) →
          Some U are not T (O-type) ✓
          (Middle = S: undistributed as predicate of I, distributed as
          subject of E → valid.)

     II:  All T are U (All T→U).
          The only derived fact involving T is No T is S (E-conv of Stmt I)
          and Some U are S (Stmt II). These give no path to a universal
          affirmative All T→U. ✗

     Only conclusion I follows.
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

    # ── Q37 (GD Constable, 22 Feb 2024 Shift-4) ─────────────────────────────
    # Some Eng→Doc (I); All Doc→Law (A); Some Law not Tea (O).
    # I:  Some lawyers are teachers → O-type Stmt III gives no I-type conclusion ✗
    # II: Some engineers are lawyers → Darii (Some Eng are Doc + All Doc→Law) ✓
    {
        "question_number": 37,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_22Feb2024_Shift4",
        "question_en": (
            "Three Statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s) from the statements.\n\n"
            "Statement I:   Some engineers are doctors.\n"
            "Statement II:  All doctors are lawyers.\n"
            "Statement III: Some lawyers are not teachers.\n\n"
            "Conclusion I:  Some lawyers are teachers.\n"
            "Conclusion II: Some engineers are lawyers."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन I:   कुछ इंजीनियर डॉक्टर हैं।\n"
            "कथन II:  सभी डॉक्टर वकील हैं।\n"
            "कथन III: कुछ वकील शिक्षक नहीं हैं।\n\n"
            "निष्कर्ष I:  कुछ वकील शिक्षक हैं।\n"
            "निष्कर्ष II: कुछ इंजीनियर वकील हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q38 (GD Constable, 24 Feb 2024 Shift-1) ─────────────────────────────
    # No A is B (E); Some B are P (I).
    # I:  Some B are not A → E-conv: No B is A → subaltern: Some B are not A ✓
    # II: Some P are not A → B∩A = ∅; the B's that are P (Stmt II) cannot be A
    #     ∴ those P entities are not A → Ferio: Some P are not A ✓
    {
        "question_number": 38,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_24Feb2024_Shift1",
        "question_en": (
            "In the following question some statements are given and some conclusions "
            "based on those statements. You have to take the given statements to be true "
            "even if they seem to be at variance from commonly known facts. Read all the "
            "conclusions carefully and then decide which of the given conclusions "
            "logically follows from the given statements.\n\n"
            "Statements:\n"
            "I.  No A is B.\n"
            "II. Some B are P.\n\n"
            "Conclusions:\n"
            "I.  Some B are not A.\n"
            "II. Some P are not A."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कुछ कथन और उनके बाद उन कथनों पर आधारित कुछ "
            "निष्कर्ष दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, भले ही वे "
            "सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों, सभी निष्कर्षों को "
            "पढ़िए और तय कीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "I.  कोई A, B नहीं है।\n"
            "II. कुछ B, P हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ B, A नहीं हैं।\n"
            "II. कुछ P, A नहीं हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q39 (GD Constable, 24 Feb 2024 Shift-4) ─────────────────────────────
    # No red is black (E); No rat is black (E).
    # Two E-type premises with the same predicate (black) — two negative premises
    # yield no valid conclusion. The relationship between reds and rats is
    # completely unconstrained by the premises.
    # I:  Some rats are not red  ✗
    # II: Some red are not rats  ✗
    {
        "question_number": 39,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_24Feb2024_Shift4",
        "question_en": (
            "In the following question below are given some statements followed by "
            "some conclusions based on those statements. Taking the given statements "
            "to be true even if they seem to be at variance from commonly known facts. "
            "Read all the conclusions and then decide which of the given conclusion(s) "
            "logically follows the given statements.\n\n"
            "Statements:\n"
            "I.  No red is black.\n"
            "II. No rat is black.\n\n"
            "Conclusions:\n"
            "I.  Some rats are not red.\n"
            "II. Some red are not rats."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कुछ कथन और उनके बाद उन कथनों पर आधारित कुछ "
            "निष्कर्ष दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, सभी निष्कर्षों को "
            "पढ़िए और तय कीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "I.  कोई लाल, काला नहीं है।\n"
            "II. कोई चूहा, काला नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ चूहे, लाल नहीं हैं।\n"
            "II. कुछ लाल, चूहे नहीं हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q40 (CHSL, 03 July 2024 Shift-1) ────────────────────────────────────
    # All paints→houses (A); All houses→wood (A); Some streets are wood (I).
    # Barbara: All Pa→Ho + All Ho→Wo → All Pa→Wo.
    # I:  Some streets are houses → Some St are Wo but Ho ⊆ Wo (not Wo ⊆ Ho);
    #     streets can be non-house wood. ✗
    # II: All paints are wood → Barbara ✓
    {
        "question_number": 40,
        "difficulty": "medium",
        "source_pdf": "CHSL_03July2024_Shift1",
        "question_en": (
            "Three statements are followed by conclusions numbered I and II. "
            "You have to consider these statements to be true, even if they seem "
            "to be at variance with commonly known facts. Decide which of the given "
            "conclusions logically follow(s) from the given statements.\n\n"
            "Statements:\n"
            "All paints are houses.\n"
            "All houses are wood.\n"
            "Some streets are wood.\n\n"
            "Conclusion (I):  Some streets are houses.\n"
            "Conclusion (II): All paints are wood."
        ),
        "question_hi": (
            "तीन कथनों के बाद I और II अंकित निष्कर्ष दिए गए हैं। आपको इन कथनों को "
            "सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते "
            "हों। निर्णय लीजिए कि दिए गए निष्कर्षों में से कौन-सा/से कथनों का "
            "तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी पेंट घर हैं।\n"
            "सभी घर लकड़ी हैं।\n"
            "कुछ गलियाँ लकड़ी हैं।\n\n"
            "निष्कर्ष (I):  कुछ गलियाँ घर हैं।\n"
            "निष्कर्ष (II): सभी पेंट लकड़ी हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q41 (GD Constable, 24 Feb 2024 Shift-3) ─────────────────────────────
    # All Bi→Wh (A); Some Wh are Ru (I); No Ru is Pl (E).
    # I:  Some Wh are Bi → subaltern of All Bi→Wh → I-conv: Some Wh are Bi ✓
    # II: Some Wh are plastic → Ferio: Some Wh are Ru + No Ru is Pl
    #     → Some Wh are NOT Pl (O-type) — the opposite of Conclusion II ✗
    {
        "question_number": 41,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_24Feb2024_Shift3",
        "question_en": (
            "Three Statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s) from the statements.\n\n"
            "Statement I:   All bicycles are wheels.\n"
            "Statement II:  Some wheels are rubber.\n"
            "Statement III: No rubber is plastic.\n\n"
            "Conclusion I:  Some wheels are bicycles.\n"
            "Conclusion II: Some wheels are plastics."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन I:   सभी साइकिल पहिए हैं।\n"
            "कथन II:  कुछ पहिए रबड़ हैं।\n"
            "कथन III: कोई रबड़ प्लास्टिक नहीं है।\n\n"
            "निष्कर्ष I:  कुछ पहिए साइकिल हैं।\n"
            "निष्कर्ष II: कुछ पहिए प्लास्टिक हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
    },

    # ── Q42 (GD Constable, 26 Feb 2024 Shift-1) ─────────────────────────────
    # No S is T (E); Some U are S (I).
    # I:  Some U are not T → Ferio: Some U are S (I) + No S is T (E)
    #     Middle S: undistributed in I (predicate), distributed in E (subject).
    #     Valid Ferio → Some U are not T ✓
    # II: All T are U → no path from two premises that give only E and I about
    #     {T,S} and {U,S} to derive a universal affirmative about T and U. ✗
    {
        "question_number": 42,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_26Feb2024_Shift1",
        "question_en": (
            "In the following question below are given some statements followed by "
            "some conclusions based on those statements. Taking the given statements "
            "to be true even if they seem to be at variance from commonly known facts. "
            "Read all the conclusions and then decide which of the given conclusion(s) "
            "logically follows the given statements.\n\n"
            "Statements:\n"
            "I.  No S is T.\n"
            "II. Some U are S.\n\n"
            "Conclusions:\n"
            "I.  Some U are not T.\n"
            "II. All T are U."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कुछ कथन और उनके बाद उन कथनों पर आधारित कुछ "
            "निष्कर्ष दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, सभी निष्कर्षों को "
            "पढ़िए और तय कीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "I.  कोई S, T नहीं है।\n"
            "II. कुछ U, S हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ U, T नहीं हैं।\n"
            "II. सभी T, U हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
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
