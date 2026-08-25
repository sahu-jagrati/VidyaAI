"""
seed_reasoning_syllogism_sheet16.py
=====================================
Seeds Reasoning → Syllogism  Q73–Q78 (Sheet 16).
Subject : Reasoning
Topic   : Syllogism

Q73 — 2-conclusion custom   (CPO 28 June 2024 Shift-3)  — complementary pair
Q74 — standard 2-conclusion (CPO 28 June 2024 Shift-3)
Q75 — standard 2-conclusion (CPO 28 June 2024 Shift-3)
Q76 — 3-conclusion custom   (CGL 12 Sep 2024 Shift-3)   — complementary pair
Q77 — 3-conclusion custom   (CGL 11 Sep 2024 Shift-3)
Q78 — 3-conclusion custom   (CPO 29 June 2024 Shift-3)

Answer key:
  Q73  D   Q74  D   Q75  D   Q76  B   Q77  C   Q78  C

Reasoning notes
───────────────
Q73  All Ca→Pl (A); Some Pl are Wo (I).
     I:  Some Ca are Wo → middle Pl: All Ca→Pl (A, Pl undistrib. as predicate) +
         Some Pl are Wo (I, Pl subject undistrib.) → fallacy of undistributed middle ✗
     II: No Ca is Wo (E-type) → no E-type or chain derivable ✗
     I and II are complementary (I-type vs E-type, same S=Ca, P=Wo):
     one of them MUST be true → "Either I or II follows."

Q74  Some Sn are Me (I); All Ju→Sn (A).
     I:  All juices can never be meals →
         Assume All Ju→Me: All Ju→Sn (A) and All Ju→Me (assumed); Some Sn are Me.
         No contradiction. → NOT impossible ✗
     II: All Me→Sn (A-type) → can't derive A-type from I-type alone ✗
     Neither conclusion I nor II follows.

Q75  Some St are Ri (I); Some Ri are Oc (I).
     I:  Some St are Oc → I+I = no valid conclusion ✗
     II: All Ri→Oc (A-type) → can't derive A-type from I-type ✗
     Neither conclusion I nor II follows.

Q76  No Lo is Da (E); All Lo→Tu (A); All Tu→Su (A).
     Barbara: All Lo→Tu + All Tu→Su → All Lo→Su.
     I:  All Da→Tu (A-type) → no premise connects Da to Tu; "No Lo is Da" only
         tells us lotuses are not daisies, not anything about daisies and tulips. ✗
     II: Some Su are Da → premises give no information about Su-Da overlap. ✗
     III: No Su is Da → premises give no information that ALL sunflowers avoid daisies. ✗
     II and III are complementary (I-type vs E-type, same S=Su, P=Da):
     one of them MUST be true → "Either conclusion II or III follows."

Q77  Some Ra are Mo (I); No Mo is Ro (E); Some Ra are Ki (I).
     Ferio (M=Mo, S=Ra, P=Ro): No Mo is Ro (E) + Some Ra are Mo (I)
         → Some Ra are not Ro (O).  [This O-type is derivable but is NOT listed.]
     I:  No Ro is Ki (E-type) → no path connecting Ro and Ki ✗
     II: Some Ra are Ro (I-type) → Ferio gives O-type (some Ra are NOT Ro); positive I-type ✗
     III: No Ki is Mo (E-type) → middle Ra: I+I = no conclusion ✗
     None of the conclusions follows.

Q78  All Sc→Pr (A); Some Sc are Co (I).
     I:  Some Pr are Co →
         Darii (M=Sc, S=Co, P=Pr): All Sc→Pr (A) + Some Co are Sc (I-conv of Some Sc are Co)
         → Some Co are Pr (I) → I-conv: Some Pr are Co ✓
     II: No Co is Pr (E-type) →
         Contradicts derived "Some Co are Pr" (from I). ✗
     III: Some Pr are Sc →
         Subalternation of All Sc→Pr: Some Sc are Pr → I-conv: Some Pr are Sc ✓
     Only conclusions I and III follow.
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

    # ── Q73 (CPO, 28 June 2024 Shift-3) ─────────────────────────────────────
    # All Ca→Pl (A); Some Pl are Wo (I).
    # I:  Some Ca are Wo → undistributed middle (Pl) ✗
    # II: No Ca is Wo (E-type) → no E-type premise/chain ✗
    # I and II are complementary (I-type vs E-type, S=Ca, P=Wo)
    # → "Either conclusion I or II follows."
    # Custom options (exam's option 4 is "Either I or II").
    {
        "question_number": 73,
        "difficulty": "medium",
        "source_pdf": "CPO_28June2024_Shift3",
        "question_en": (
            "Two statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow(s) from "
            "the statements.\n\n"
            "Statements:\n"
            "All cards are plastics.\n"
            "Some plastics are woods.\n\n"
            "Conclusions:\n"
            "I.  Some cards are woods.\n"
            "II. No card is a wood."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं जिनके बाद दो निष्कर्ष I और II दिए गए हैं। कथनों को सत्य "
            "मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों, "
            "निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी कार्ड प्लास्टिक हैं।\n"
            "कुछ प्लास्टिक लकड़ी हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ कार्ड लकड़ी हैं।\n"
            "II. कोई भी कार्ड लकड़ी नहीं है।"
        ),
        "option_a": "Only conclusion II follows.",
        "option_b": "Neither conclusion I nor II follows.",
        "option_c": "Only conclusion I follows.",
        "option_d": "Either conclusion I or II follows.",
        "correct_answer": "D",
    },

    # ── Q74 (CPO, 28 June 2024 Shift-3) ─────────────────────────────────────
    # Some Sn are Me (I); All Ju→Sn (A).
    # I:  All juices can never be meals → no contradiction if All Ju→Me → NOT impossible ✗
    # II: All Me→Sn (A-type) → can't derive A from I ✗
    # Neither follows.
    {
        "question_number": 74,
        "difficulty": "medium",
        "source_pdf": "CPO_28June2024_Shift3",
        "question_en": (
            "Two statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow(s) from "
            "the statements.\n\n"
            "Statements:\n"
            "1) Some snacks are meals.\n"
            "2) All juices are snacks.\n\n"
            "Conclusions:\n"
            "I.  All juices can never be meals.\n"
            "II. All meals are snacks."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं जिनके बाद दो निष्कर्ष I और II दिए गए हैं। कथनों को सत्य "
            "मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों, "
            "निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "1) कुछ स्नैक्स भोजन हैं।\n"
            "2) सभी जूस स्नैक्स हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  सभी जूस कभी भी भोजन नहीं हो सकते।\n"
            "II. सभी भोजन स्नैक्स हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q75 (CPO, 28 June 2024 Shift-3) ─────────────────────────────────────
    # Some St are Ri (I); Some Ri are Oc (I).
    # I:  Some St are Oc → I+I = no valid conclusion ✗
    # II: All Ri→Oc (A-type) → can't derive A from I ✗
    # Neither follows.
    {
        "question_number": 75,
        "difficulty": "easy",
        "source_pdf": "CPO_28June2024_Shift3",
        "question_en": (
            "Two statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow(s) from "
            "the statements.\n\n"
            "Statements:\n"
            "Some streams are rivers.\n"
            "Some rivers are oceans.\n\n"
            "Conclusions:\n"
            "I.  Some streams are oceans.\n"
            "II. All rivers are oceans."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं जिनके बाद दो निष्कर्ष I और II दिए गए हैं। कथनों को सत्य "
            "मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों, "
            "निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ धाराएँ नदियाँ हैं।\n"
            "कुछ नदियाँ महासागर हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ धाराएँ महासागर हैं।\n"
            "II. सभी नदियाँ महासागर हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q76 (CGL, 12 Sep 2024 Shift-3) ──────────────────────────────────────
    # No Lo is Da (E); All Lo→Tu (A); All Tu→Su (A). Barbara: All Lo→Su.
    # I:  All Da→Tu → no Da-Tu connection in premises ✗
    # II: Some Su are Da → Su-Da relationship unknown ✗
    # III: No Su is Da → Su-Da relationship unknown ✗
    # II and III are complementary (I-type vs E-type, S=Su, P=Da)
    # → "Either conclusion II or III follows."
    {
        "question_number": 76,
        "difficulty": "hard",
        "source_pdf": "CGL_12Sep2024_Shift3",
        "question_en": (
            "Three statements are given, followed by three conclusions numbered I, II and III. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow/s from "
            "the statements.\n\n"
            "Statements:\n"
            "No lotus is a daisy.\n"
            "All lotuses are tulips.\n"
            "All tulips are sunflowers.\n\n"
            "Conclusions:\n"
            "I.   All daisies are tulips.\n"
            "II.  Some sunflowers are daisies.\n"
            "III. No sunflower is a daisy."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं, जिनके बाद तीन निष्कर्ष I, II और III क्रमांकित हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कोई कमल डेज़ी नहीं है।\n"
            "सभी कमल ट्यूलिप हैं।\n"
            "सभी ट्यूलिप सूरजमुखी हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   सभी डेज़ी ट्यूलिप हैं।\n"
            "II.  कुछ सूरजमुखी डेज़ी हैं।\n"
            "III. कोई भी सूरजमुखी डेज़ी नहीं है।"
        ),
        "option_a": "Only conclusions I and II follow.",
        "option_b": "Either conclusion II or III follows.",
        "option_c": "Only conclusion I follows.",
        "option_d": "Only conclusion III follows.",
        "correct_answer": "B",
    },

    # ── Q77 (CGL, 11 Sep 2024 Shift-3) ──────────────────────────────────────
    # Some Ra are Mo (I); No Mo is Ro (E); Some Ra are Ki (I).
    # Derivable: Some Ra are not Ro (O) via Ferio — but this is NOT a listed conclusion.
    # I:  No Ro is Ki (E-type) → no Ro-Ki connection ✗
    # II: Some Ra are Ro (I-type, positive) → Ferio only gives O-type; I-type ✗
    # III: No Ki is Mo (E-type) → middle Ra: I+I = no conclusion ✗
    # None of the conclusions follows.
    {
        "question_number": 77,
        "difficulty": "medium",
        "source_pdf": "CGL_11Sep2024_Shift3",
        "question_en": (
            "Three statements are given, followed by three conclusions numbered I, II and III. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow/s from "
            "the statements.\n\n"
            "Statements:\n"
            "Some rats are mouse.\n"
            "No mouse is a rodent.\n"
            "Some rats are kittens.\n\n"
            "Conclusions:\n"
            "I.   No rodent is a kitten.\n"
            "II.  Some rats are rodents.\n"
            "III. No kitten is a mouse."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं, जिनके बाद तीन निष्कर्ष I, II और III क्रमांकित हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ रेट माउस हैं।\n"
            "कोई माउस रोडेंट नहीं है।\n"
            "कुछ रेट किटेन हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कोई रोडेंट किटेन नहीं है।\n"
            "II.  कुछ रेट रोडेंट हैं।\n"
            "III. कोई किटेन माउस नहीं है।"
        ),
        "option_a": "Only conclusion III follows.",
        "option_b": "Only conclusion II follows.",
        "option_c": "Neither conclusion follows.",
        "option_d": "Only conclusion I follows.",
        "correct_answer": "C",
    },

    # ── Q78 (CPO, 29 June 2024 Shift-3) ─────────────────────────────────────
    # All Sc→Pr (A); Some Sc are Co (I).
    # I:  Some Pr are Co →
    #     Darii (M=Sc, S=Co, P=Pr): All Sc→Pr + Some Co are Sc (I-conv) → Some Co are Pr → I-conv ✓
    # II: No Co is Pr (E-type) → contradicts derived "Some Co are Pr" ✗
    # III: Some Pr are Sc →
    #     Subalternation of All Sc→Pr: Some Sc are Pr → I-conv: Some Pr are Sc ✓
    # Only conclusions I and III follow.
    {
        "question_number": 78,
        "difficulty": "medium",
        "source_pdf": "CPO_29June2024_Shift3",
        "question_en": (
            "Two statements are given, followed by three conclusions numbered I, II and III. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow/s from "
            "the statements.\n\n"
            "Statements:\n"
            "All scanners are printers.\n"
            "Some scanners are copiers.\n\n"
            "Conclusions:\n"
            "I.   Some printers are copiers.\n"
            "II.  No copier is a printer.\n"
            "III. Some printers are scanners."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं, जिनके बाद तीन निष्कर्ष I, II और III दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी स्कैनर प्रिंटर हैं।\n"
            "कुछ स्कैनर कॉपियर हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कुछ प्रिंटर कॉपियर हैं।\n"
            "II.  कोई कॉपियर प्रिंटर नहीं है।\n"
            "III. कुछ प्रिंटर स्कैनर हैं।"
        ),
        "option_a": "All of the conclusions follow.",
        "option_b": "Only conclusions I and II follow.",
        "option_c": "Only conclusions I and III follow.",
        "option_d": "Only conclusions II and III follow.",
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
