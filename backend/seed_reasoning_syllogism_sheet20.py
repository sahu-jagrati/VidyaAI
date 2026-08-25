"""
seed_reasoning_syllogism_sheet20.py  —  Reasoning → Syllogism  Q96–Q100
Q96   A  CGL_24Sep2024_Shift2            3-conclusion CUSTOM options
Q97   C  GD_Constable_24Feb2024_Shift2   standard 2-conclusion
Q98   D  GD_Constable_06March2024_Shift2 standard 2-conclusion
Q99   A  GD_Constable_06March2024_Shift3 standard 2-conclusion
Q100  B  CGL_25Sep2024_Shift1            3-conclusion CUSTOM options

Reasoning notes
───────────────
Q96  All Ne→Sq (A); Some Sq are Ci (I); No Ci is Ri (E).
     I:  No Sq is Ri (E-type) → Ferio gives only O: Some Sq are not Ri; E-type undeducible ✗
     II: No Ri is Ci → E-conv of "No Ci is Ri" ✓
     III:Some Sq are Ne → All Ne→Sq (A) → subalternation: Some Ne are Sq → I-conv: Some Sq are Ne ✓
     Only conclusions II and III follow.

Q97  All Cu→Be (A); Some Be are Ch (I); Some Ch are not Ta (O).
     I:  Some chairs are beds → I-conv of "Some Be are Ch": Some Ch are Be ✓
     II: Some chairs being curtains is possible →
         Assume Some Ch are Cu: those chairs become beds too (All Cu→Be), consistent with
         "Some Be are Ch"; no premise contradicts this assumption. ✓
     Both I and II follow.

Q98  Some L are G (I); All T→G (A).
     Middle = G: predicate in I-type (undistrib.) and predicate in A-type (undistrib.).
     Undistributed middle → no valid conclusion about L and T.
     I:  No T is L (E-type) → undistributed middle ✗
     II: No G is T (E-type) → "All T→G" gives "Some G are T" (subalternation+I-conv);
         "No G is T" directly contradicts this. ✗
     Neither conclusion follows.

Q99  No Po is Li (E); All Li→Cr (A); No Cr is Lo (E).
     I:  No Li is Lo → Celarent (M=Cr, S=Li, P=Lo):
         All Li→Cr (All S→M) + No Cr is Lo (No M is P) → No Li is Lo ✓
     II: No Po is Cr → No premise rules out non-lipstick creams being powders;
         can't derive E-type blocking Po∩Cr. ✗
     Only conclusion I follows.

Q100 Some Ve are Fr (I); Some Fr are Fl (I); All Fl→Ga (A).
     I:  Some Ga are Fr →
         Darii (M=Fl, S=Fr, P=Ga): All Fl→Ga + Some Fr are Fl → Some Fr are Ga
         → I-conv: Some Ga are Fr ✓
     II: Some Ve are Fl → middle Fr: Some Ve are Fr (I) + Some Fr are Fl (I) = I+I ✗
     III:Some Ve are Ga → even with "Some Fr are Ga" derived, Some Ve are Fr (I) + Some Fr
         are Ga (I) = I+I ✗
     Only conclusion I follows.
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

    # ── Q96 (CGL, 24 Sep 2024 Shift-2) — 3-conclusion CUSTOM ────────────────
    # All Ne→Sq (A); Some Sq are Ci (I); No Ci is Ri (E).
    # I:  Ferio gives O-type only (Some Sq are not Ri); E-type unreachable ✗
    # II: E-conv of No Ci is Ri → No Ri is Ci ✓
    # III:All Ne→Sq → subalternation → Some Ne are Sq → I-conv: Some Sq are Ne ✓
    # Only II and III follow → custom option A.
    {
        "question_number": 96,
        "difficulty": "hard",
        "source_pdf": "CGL_24Sep2024_Shift2",
        "question_en": (
            "In this question, three statements are given, followed by three conclusions "
            "numbered I, II and III. Assuming the statements to be true, even if they seem "
            "to be at variance with commonly known facts, decide which of the conclusions "
            "logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "All necklaces are squares.\n"
            "Some squares are circles.\n"
            "No circle is a ring.\n\n"
            "Conclusions:\n"
            "I.   No square is a ring.\n"
            "II.  No ring is a circle.\n"
            "III. Some squares are necklaces."
        ),
        "question_hi": (
            "इस प्रश्न में तीन कथन दिए गए हैं, जिनके बाद I, II और III क्रमांकित तीन "
            "निष्कर्ष दिए गए हैं। कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात "
            "तथ्यों से भिन्न प्रतीत होते हों, तय करें कि कौन-सा/से निष्कर्ष तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी हार वर्ग हैं।\n"
            "कुछ वर्ग वृत्त हैं।\n"
            "कोई भी वृत्त, वलय नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.   कोई भी वर्ग, वलय नहीं है।\n"
            "II.  कोई भी वलय, वृत्त नहीं है।\n"
            "III. कुछ वर्ग, हार हैं।"
        ),
        # Custom options in image order; correct answer = option 1 = "A"
        "option_a": "Only conclusions II and III follow. / केवल निष्कर्ष II और III अनुसरण करते हैं।",
        "option_b": "Only conclusion III follows. / केवल निष्कर्ष III अनुसरण करता है।",
        "option_c": "All the conclusions follow. / सभी निष्कर्ष अनुसरण करते हैं।",
        "option_d": "Only conclusions I and III follow. / केवल निष्कर्ष I और III अनुसरण करते हैं।",
        "correct_answer": "A",
    },

    # ── Q97 (GD Constable, 24 Feb 2024 Shift-2) ──────────────────────────────
    # All Cu→Be (A); Some Be are Ch (I); Some Ch are not Ta (O).
    # I:  Some Ch are Be → I-conv of "Some Be are Ch" ✓
    # II: Some chairs being curtains is possible → assume Some Ch are Cu;
    #     they become beds (All Cu→Be), consistent with Some Be are Ch; no contradiction ✓
    # Both conclusions I and II follow.
    {
        "question_number": 97,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_24Feb2024_Shift2",
        "question_en": (
            "Three statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow(s) from "
            "the statements.\n\n"
            "Statements:\n"
            "All curtains are beds.\n"
            "Some beds are chairs.\n"
            "Some chairs are not tables.\n\n"
            "Conclusions:\n"
            "I.  Some chairs are beds.\n"
            "II. Some chairs being curtains is possible."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद I और II से क्रमांकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत "
            "होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी पर्दे बिस्तर हैं।\n"
            "कुछ बिस्तर कुर्सियाँ हैं।\n"
            "कुछ कुर्सियाँ टेबल नहीं हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ कुर्सियाँ बिस्तर हैं।\n"
            "II. कुछ कुर्सियाँ पर्दे होना संभव है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
    },

    # ── Q98 (GD Constable, 06 March 2024 Shift-2) ─────────────────────────────
    # Some L are G (I); All T→G (A).
    # Middle = G: predicate in both I and A-type → undistributed middle. ✗
    # I:  No T is L (E) → undistributed middle; no valid chain ✗
    # II: No G is T (E) → "All T→G" gives "Some G are T" (subalternation+I-conv);
    #     "No G is T" contradicts this derived fact. ✗
    # Neither conclusion follows.
    {
        "question_number": 98,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_06March2024_Shift2",
        "question_en": (
            "In the following question, some statements are given followed by some conclusions. "
            "Taking the given statements to be true even if they seem to be at variance from "
            "commonly known facts, decide which conclusion(s) logically follow(s).\n\n"
            "Statements:\n"
            "Some L are G.\n"
            "All T are G.\n\n"
            "Conclusions:\n"
            "I.  No T is L.\n"
            "II. No G is T."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कुछ कथन और उसके बाद उन कथनों पर आधारित कुछ "
            "निष्कर्ष दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, भले ही वे "
            "सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों, तय करें कि कौन-सा/से "
            "निष्कर्ष तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ L, G हैं।\n"
            "सभी T, G हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कोई T, L नहीं है।\n"
            "II. कोई G, T नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q99 (GD Constable, 06 March 2024 Shift-3) ─────────────────────────────
    # No Po is Li (E); All Li→Cr (A); No Cr is Lo (E).
    # I:  No Li is Lo → Celarent (M=Cr, S=Li, P=Lo):
    #     All Li→Cr (All S→M) + No Cr is Lo (No M is P) → No Li is Lo ✓
    # II: No Po is Cr → No premise blocks non-lipstick creams from being powders;
    #     Po and Cr are not necessarily disjoint. ✗
    # Only conclusion I follows.
    {
        "question_number": 99,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_06March2024_Shift3",
        "question_en": (
            "Three Statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow(s) from "
            "the statements.\n\n"
            "Statement I:   No powder is a lipstick.\n"
            "Statement II:  All lipsticks are creams.\n"
            "Statement III: No cream is a lotion.\n\n"
            "Conclusion I:  No lipstick is a lotion.\n"
            "Conclusion II: No powder is a cream."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद I और II से क्रमांकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत "
            "होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से अनुसरण करता/"
            "करते हैं।\n\n"
            "कथन I:   कोई भी पाउडर, लिपस्टिक नहीं है।\n"
            "कथन II:  सभी लिपस्टिक, क्रीम हैं।\n"
            "कथन III: कोई भी क्रीम, लोशन नहीं है।\n\n"
            "निष्कर्ष I:  कोई भी लिपस्टिक, लोशन नहीं है।\n"
            "निष्कर्ष II: कोई भी पाउडर, क्रीम नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
    },

    # ── Q100 (CGL, 25 Sep 2024 Shift-1) — 3-conclusion CUSTOM ───────────────
    # Some Ve are Fr (I); Some Fr are Fl (I); All Fl→Ga (A).
    # I:  Some Ga are Fr →
    #     Darii (M=Fl, S=Fr, P=Ga): All Fl→Ga + Some Fr are Fl → Some Fr are Ga
    #     → I-conv: Some Ga are Fr ✓
    # II: Some Ve are Fl → middle Fr: I+I = undistributed middle ✗
    # III:Some Ve are Ga → chain to "Some Fr are Ga" via Darii, then
    #     Some Ve are Fr (I) + Some Fr are Ga (I): I+I ✗
    # Only conclusion I follows → custom option B.
    {
        "question_number": 100,
        "difficulty": "hard",
        "source_pdf": "CGL_25Sep2024_Shift1",
        "question_en": (
            "Read the given statements and conclusions carefully. Assuming that the information "
            "given in the statements is true, even if it appears to be at variance with commonly "
            "known facts, decide which of the given conclusions logically follow(s) from the "
            "statements.\n\n"
            "Statements:\n"
            "Some vegetables are fruits.\n"
            "Some fruits are flowers.\n"
            "All flowers are garlands.\n\n"
            "Conclusions:\n"
            "I.   Some garlands are fruits.\n"
            "II.  Some vegetables are flowers.\n"
            "III. Some vegetables are garlands."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों को ध्यानपूर्वक पढ़ें। यह मानते हुए कि कथनों में "
            "दी गई जानकारी सत्य है, भले ही वह सामान्य ज्ञात तथ्यों से भिन्न प्रतीत होती "
            "हो, यह तय करें कि दिए गए निष्कर्षों में से कौन-सा/से कथनों का तार्किक रूप "
            "से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ सब्जियाँ फल हैं।\n"
            "कुछ फल फूल हैं।\n"
            "सभी फूल माला हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कुछ मालाएँ फल हैं।\n"
            "II.  कुछ सब्जियाँ फूल हैं।\n"
            "III. कुछ सब्जियाँ माला हैं।"
        ),
        # Custom options in image order; correct answer = option 2 = "B"
        "option_a": "Only conclusions I and II follow. / केवल निष्कर्ष I और II अनुसरण करते हैं।",
        "option_b": "Only conclusion I follows. / केवल निष्कर्ष I अनुसरण करता है।",
        "option_c": "Only conclusions II and III follow. / केवल निष्कर्ष II और III अनुसरण करते हैं।",
        "option_d": "Only conclusions I and III follow. / केवल निष्कर्ष I और III अनुसरण करते हैं।",
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
