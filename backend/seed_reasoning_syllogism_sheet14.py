"""
seed_reasoning_syllogism_sheet14.py
=====================================
Seeds Reasoning → Syllogism  Q62–Q66 (Sheet 14).
Subject : Reasoning
Topic   : Syllogism

Q62 — 3-conclusion custom   (CGL 09 Sep 2024 Shift-2)
Q63 — standard 2-conclusion (CGL 09 Sep 2024 Shift-2)
Q64 — standard 2-conclusion (CGL 10 Sep 2024 Shift-1)
Q65 — 3-conclusion custom   (CGL 11 Sep 2024 Shift-1)
Q66 — standard 2-conclusion (CGL 11 Sep 2024 Shift-2)

Answer key:
  Q62  C   Q63  D   Q64  B   Q65  A   Q66  C

Reasoning notes
───────────────
Q62  All Fa→Br (A); Some Br are Ch (I); Some Ch are Pl (I).
     I:  Some Br are Fa → I-conversion of Stmt I (All Fa→Br → Some Fa are Br → Some Br are Fa) ✓
     II: Some Ch are Br → I-conversion of Stmt II (Some Br are Ch → Some Ch are Br) ✓
     III: No Ch is Pl → directly contradicts Stmt III (Some chairs ARE plastic) ✗
     Only conclusions I and II follow.

Q63  No Ri is Mo (E); Some Ri are An (I); Some Bi are Mo (I).
     I:  No An is Mo (E-type) →
         Ferio: No Ri is Mo (E) + Some An are Ri (I-conv of Some Ri are An) → Some An are not Mo (O).
         O-type cannot strengthen to E-type. "No animal is a mountain" does NOT follow. ✗
     II: No Ri is Bi (E-type) →
         Festino: No Ri is Mo → E-conv: No Mo is Ri; Some Bi are Mo + No Mo is Ri:
         Ferio → Some Bi are not Ri (O-type only). E-type "No Ri is Bi" does NOT follow. ✗
     Neither conclusion I nor II follows.

Q64  All Bo→Ca (A); All Ca→Pa (A); Some Ca are Ut (I).
     Barbara: All Bo→Ca + All Ca→Pa → All Bo→Pa.
     I:  No Ut is Bo (E-type) → no E-type premise connecting Ut and Bo; no valid derivation. ✗
     II: Some Pa are Ut →
         Darii (M=Ca, S=Ut, P=Pa): All Ca→Pa (A) + Some Ut are Ca (I-conv of Some Ca are Ut)
         → Some Ut are Pa (I) → I-conv: Some Pa are Ut ✓
     Only conclusion II follows.

Q65  All Bo→Ju (A); Some Bo are Fl (I); All Fl→Bi (A).
     I:  Some Bo are Bi →
         Darii: Some Bo are Fl (I) + All Fl→Bi (A) [M=Fl, S=Bo, P=Bi] → Some Bo are Bi ✓
     II: Some Ju are Bi →
         From I: Some Bo are Bi → I-conv: Some Bi are Bo.
         Darii: All Bo→Ju (A) + Some Bi are Bo (I) [M=Bo, S=Bi, P=Ju] → Some Bi are Ju → I-conv: Some Ju are Bi ✓
     III: Some Fl are Ju →
         I-conv of Stmt II: Some Bo are Fl → Some Fl are Bo.
         Darii: All Bo→Ju (A) + Some Fl are Bo (I) [M=Bo, S=Fl, P=Ju] → Some Fl are Ju ✓
     All conclusions I, II and III follow.

Q66  All Ap→Ma (A); All Ma→Le (A); All Le→Ki (A).
     I:  All Ap→Le → Barbara: All Ap→Ma + All Ma→Le → All Ap→Le ✓
     II: All Ma→Ki → Barbara: All Ma→Le + All Le→Ki → All Ma→Ki ✓
     Both conclusions I and II follow.
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

    # ── Q62 (CGL, 09 Sep 2024 Shift-2) ──────────────────────────────────────
    # All Fa→Br (A); Some Br are Ch (I); Some Ch are Pl (I).
    # I:  Some Br are Fa → I-conv of Stmt I ✓
    # II: Some Ch are Br → I-conv of Stmt II ✓
    # III: No Ch is Pl → contradicts Stmt III ✗
    # Custom options as per exam.
    {
        "question_number": 62,
        "difficulty": "medium",
        "source_pdf": "CGL_09Sep2024_Shift2",
        "question_en": (
            "In this question, three statements are given, followed by three conclusions "
            "numbered I, II and III. Assuming the statements to be true, even if they seem "
            "to be at variance with commonly known facts, decide which of the conclusions "
            "logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "All fans are brown.\n"
            "Some brown are chairs.\n"
            "Some chairs are plastic.\n\n"
            "Conclusions:\n"
            "I.   Some brown are fans.\n"
            "II.  Some chairs are brown.\n"
            "III. No chair is plastic."
        ),
        "question_hi": (
            "इस प्रश्न में तीन कथन दिए गए हैं, जिनके बाद तीन निष्कर्ष I, II और III "
            "दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, भले ही वे सामान्य ज्ञात "
            "तथ्यों से भिन्न प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष "
            "कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी पंखे भूरे हैं।\n"
            "कुछ भूरे कुर्सियाँ हैं।\n"
            "कुछ कुर्सियाँ प्लास्टिक हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कुछ भूरे पंखे हैं।\n"
            "II.  कुछ कुर्सियाँ भूरी हैं।\n"
            "III. कोई कुर्सी प्लास्टिक नहीं है।"
        ),
        "option_a": "Only conclusions II and III follow.",
        "option_b": "None of the conclusions follows.",
        "option_c": "Only conclusions I and II follow.",
        "option_d": "Only conclusion III follows.",
        "correct_answer": "C",
    },

    # ── Q63 (CGL, 09 Sep 2024 Shift-2) ──────────────────────────────────────
    # No Ri is Mo (E); Some Ri are An (I); Some Bi are Mo (I).
    # I:  No An is Mo (E-type) → Ferio gives only Some An are not Mo (O-type) ✗
    # II: No Ri is Bi (E-type) → Festino gives only Some Bi are not Ri (O-type) ✗
    # Neither conclusion I nor II follows.
    {
        "question_number": 63,
        "difficulty": "medium",
        "source_pdf": "CGL_09Sep2024_Shift2",
        "question_en": (
            "Read the given statements and conclusions carefully. You have to take the given "
            "statements to be true even if they seem to be at variance from commonly known "
            "facts. You have to decide which conclusion(s) logically follow(s) from the given "
            "statements.\n\n"
            "Statements:\n"
            "No river is a mountain.\n"
            "Some rivers are animals.\n"
            "Some birds are mountains.\n\n"
            "Conclusions:\n"
            "I.  No animal is a mountain.\n"
            "II. No river is a bird."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों का ध्यानपूर्वक अध्ययन करें। आपको दिए गए "
            "कथनों को सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों। आपको यह तय करना है कि कौन-सा/से निष्कर्ष कथनों का "
            "तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कोई नदी पहाड़ नहीं है।\n"
            "कुछ नदियाँ जानवर हैं।\n"
            "कुछ पक्षी पहाड़ हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कोई जानवर पहाड़ नहीं है।\n"
            "II. कोई नदी पक्षी नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q64 (CGL, 10 Sep 2024 Shift-1) ──────────────────────────────────────
    # All Bo→Ca (A); All Ca→Pa (A); Some Ca are Ut (I).
    # I:  No Ut is Bo (E-type) → no valid E-type derivation; no E-premise involving Ut ✗
    # II: Some Pa are Ut → Darii: Some Ut are Ca (I-conv) + All Ca→Pa → Some Ut are Pa → I-conv ✓
    # Only conclusion II follows.
    {
        "question_number": 64,
        "difficulty": "medium",
        "source_pdf": "CGL_10Sep2024_Shift1",
        "question_en": (
            "Read the given statements and conclusions carefully. Assuming that the information "
            "given in the statements is true, even if it appears to be at variance with commonly "
            "known facts, decide which of the given conclusions logically follow/s from the "
            "statements.\n\n"
            "Statements:\n"
            "All boxes are cartons.\n"
            "All cartons are papers.\n"
            "Some cartons are utensils.\n\n"
            "Conclusion (I):  No utensil is a box.\n"
            "Conclusion (II): Some papers are utensils."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों का ध्यानपूर्वक अध्ययन करें। यह मानते हुए कि "
            "कथनों में दी गई जानकारी सत्य है, भले ही वह सामान्य ज्ञात तथ्यों से भिन्न "
            "प्रतीत होती हो, यह तय करें कि दिए गए निष्कर्षों में से कौन-सा/से निष्कर्ष "
            "कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी बॉक्स, कार्टन हैं।\n"
            "सभी कार्टन, कागज हैं।\n"
            "कुछ कार्टन, बर्तन हैं।\n\n"
            "निष्कर्ष (I):  कोई भी बर्तन बॉक्स नहीं है।\n"
            "निष्कर्ष (II): कुछ कागज बर्तन हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q65 (CGL, 11 Sep 2024 Shift-1) ──────────────────────────────────────
    # All Bo→Ju (A); Some Bo are Fl (I); All Fl→Bi (A).
    # I:  Some Bo are Bi → Darii: Some Bo are Fl + All Fl→Bi ✓
    # II: Some Ju are Bi → derived Some Bo are Bi + All Bo→Ju → Darii → Some Bi are Ju → I-conv ✓
    # III: Some Fl are Ju → I-conv Some Fl are Bo + All Bo→Ju → Darii ✓
    # Custom options as per exam.
    {
        "question_number": 65,
        "difficulty": "medium",
        "source_pdf": "CGL_11Sep2024_Shift1",
        "question_en": (
            "Three statements are given, followed by three conclusions numbered I, II and III. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow/s from the "
            "statements.\n\n"
            "Statements:\n"
            "All bottles are jugs.\n"
            "Some bottles are flasks.\n"
            "All flasks are bins.\n\n"
            "Conclusions:\n"
            "I.   Some bottles are bins.\n"
            "II.  Some jugs are bins.\n"
            "III. Some flasks are jugs."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं, जिनके बाद तीन निष्कर्ष I, II और III क्रमांकित हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी बोतलें जग हैं।\n"
            "कुछ बोतलें फ्लास्क हैं।\n"
            "सभी फ्लास्क डिब्बे हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कुछ बोतलें डिब्बे हैं।\n"
            "II.  कुछ जग डिब्बे हैं।\n"
            "III. कुछ फ्लास्क जग हैं।"
        ),
        "option_a": "All conclusions I, II and III follow.",
        "option_b": "Either conclusion I or II follows.",
        "option_c": "Only conclusions I and III follow.",
        "option_d": "Only conclusions I and II follow.",
        "correct_answer": "A",
    },

    # ── Q66 (CGL, 11 Sep 2024 Shift-2) ──────────────────────────────────────
    # All Ap→Ma (A); All Ma→Le (A); All Le→Ki (A).
    # I:  All Ap→Le → Barbara: All Ap→Ma + All Ma→Le ✓
    # II: All Ma→Ki → Barbara: All Ma→Le + All Le→Ki ✓
    # Both conclusions I and II follow.
    {
        "question_number": 66,
        "difficulty": "easy",
        "source_pdf": "CGL_11Sep2024_Shift2",
        "question_en": (
            "Read the given statements and conclusions carefully. You have to take the given "
            "statements to be true even if they seem to be at variance from commonly known "
            "facts. You have to decide which conclusion(s) logically follow(s) from the given "
            "statements.\n\n"
            "Statements:\n"
            "All apples are mangoes.\n"
            "All mangoes are lemons.\n"
            "All lemons are kiwis.\n\n"
            "Conclusions:\n"
            "(I)  All apples are lemons.\n"
            "(II) All mangoes are kiwis."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों का ध्यानपूर्वक अध्ययन करें। आपको दिए गए "
            "कथनों को सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों। आपको यह तय करना है कि कौन-सा/से निष्कर्ष कथनों का "
            "तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी सेब आम हैं।\n"
            "सभी आम नींबू हैं।\n"
            "सभी नींबू कीवी हैं।\n\n"
            "निष्कर्ष:\n"
            "(I)  सभी सेब नींबू हैं।\n"
            "(II) सभी आम कीवी हैं।"
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
