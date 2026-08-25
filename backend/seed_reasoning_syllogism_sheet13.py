"""
seed_reasoning_syllogism_sheet13.py
=====================================
Seeds Reasoning → Syllogism  Q56–Q61 (Sheet 13).
Subject : Reasoning
Topic   : Syllogism

Q56 — standard 2-conclusion (CHSL 09 July 2024 Shift-1)
Q57 — standard 2-conclusion (CHSL 09 July 2024 Shift-2)
Q58 — standard 2-conclusion (CHSL 09 July 2024 Shift-3)
Q59 — 3-conclusion custom   (GD Constable 27 Feb 2024 Shift-1)
Q60 — 3-conclusion custom   (CGL 09 Sep 2024 Shift-1)
Q61 — 3-conclusion custom   (CGL 09 Sep 2024 Shift-1)

Answer key:
  Q56  B   Q57  B   Q58  C   Q59  D   Q60  A   Q61  D

Reasoning notes
───────────────
Q56  All Pa→Ch (A); Some Ch are No (I); Some No are Fi (I).
     I:  Some Ch are Fi → requires Some Ch are No + Some No are Fi → I+I = no valid conclusion ✗
     II: Some paper being notebooks is a possibility → Pa⊆Ch, some Ch are No → no contradiction ✓
     Only conclusion II follows.

Q57  All Dr→Cl (A); Some Cl are Ta (I); Some Ta are St (I).
     I:  All St→Dr → no valid derivation (would need All St→Cl first, then converse of All Dr→Cl,
         but All-type doesn't reverse) ✗
     II: Some Ta are Cl → I-conversion of Stmt II (Some Cl are Ta → Some Ta are Cl) ✓
     Only conclusion II follows.

Q58  No Cl is Mo (E); All Mo→Ri (A); All Ri→Oc (A).
     Barbara: All Mo→Ri + All Ri→Oc → All Mo→Oc.
     I:  All rivers can never be clouds →
         Assume All Ri→Cl: Barbara: All Mo→Ri + All Ri→Cl → All Mo→Cl, contradicts No Cl is Mo → IMPOSSIBLE ✓
     II: All Mo→Oc → derived via Barbara ✓
     Both conclusions I and II follow.

Q59  All Re→Gr (A); Some Pi are Gr (I).
     I:  Some Pi are not Re → middle term Gr: undistributed as predicate (A) and predicate (I) → fallacy ✗
     II: All Gr→Re → invalid A-type converse of All Re→Gr (A→I only) ✗
     III: Some Pi are Gr → direct restatement of Stmt II ✓
     Only conclusion III follows.

Q60  No Ca is Pa (E); All Ca→En (A); Some En are Ba (I).
     I:  All envelopes can never be parcels →
         Assume All En→Pa: Barbara: All Ca→En + All En→Pa → All Ca→Pa, contradicts No Ca is Pa → IMPOSSIBLE ✓
     II: No Ca is Ba → All Ca→En + Some En are Ba: middle En undistributed in both premises → fallacy ✗
     III: All Ba→Ca → no valid derivation ✗
     Only conclusion I follows.

Q61  Some Te are Dr (I); Some Dr are St (I); All St→Ri (A).
     I:  All tears can never be rivers →
         Assume All Te→Ri: no contradiction with any premise (Te and Ri unrelated in premises) → NOT impossible ✗
     II: Some Dr are Ri → Darii: Some Dr are St (I) + All St→Ri (A) → Some Dr are Ri ✓
     III: All drops being rivers is a possibility →
         Some Dr are St and All St→Ri; no premise contradicts All Dr→Ri → possible ✓
     Both conclusions II and III follow.
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

    # ── Q56 (CHSL, 09 July 2024 Shift-1) ────────────────────────────────────
    # All Pa→Ch (A); Some Ch are No (I); Some No are Fi (I).
    # I:  Some Ch are Fi → I+I = no valid conclusion ✗
    # II: Some paper being notebooks is a possibility → no contradiction ✓
    {
        "question_number": 56,
        "difficulty": "medium",
        "source_pdf": "CHSL_09July2024_Shift1",
        "question_en": (
            "Three statements are followed by conclusions I and II. You have to "
            "consider these statements to be true, even if they seem to be at "
            "variance with commonly known facts. Decide which of the given "
            "conclusions logically follow/s from the given statements.\n\n"
            "Statements:\n"
            "All papers are charts.\n"
            "Some charts are notebooks.\n"
            "Some notebooks are files.\n\n"
            "Conclusion (I):  Some charts are files.\n"
            "Conclusion (II): Some papers being notebooks is a possibility."
        ),
        "question_hi": (
            "तीन कथनों के बाद निष्कर्ष I और II दिए गए हैं। आपको इन कथनों को सत्य "
            "मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों। "
            "निर्णय लीजिए कि दिए गए निष्कर्षों में से कौन-सा/से कथनों का तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी कागज़ चार्ट हैं।\n"
            "कुछ चार्ट नोटबुक हैं।\n"
            "कुछ नोटबुक फ़ाइलें हैं।\n\n"
            "निष्कर्ष (I):  कुछ चार्ट फ़ाइलें हैं।\n"
            "निष्कर्ष (II): कुछ कागज़ों का नोटबुक होना एक संभावना है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q57 (CHSL, 09 July 2024 Shift-2) ────────────────────────────────────
    # All Dr→Cl (A); Some Cl are Ta (I); Some Ta are St (I).
    # I:  All St→Dr → no valid derivation ✗
    # II: Some Ta are Cl → I-conv of Stmt II (Some Cl are Ta → Some Ta are Cl) ✓
    {
        "question_number": 57,
        "difficulty": "medium",
        "source_pdf": "CHSL_09July2024_Shift2",
        "question_en": (
            "Three statements are followed by conclusions I and II. You have to "
            "consider these statements to be true, even if they seem to be at "
            "variance with commonly known facts. Decide which of the given "
            "conclusions logically follow/s from the given statements.\n\n"
            "Statements:\n"
            "All drums are claps.\n"
            "Some claps are taps.\n"
            "Some taps are stamps.\n\n"
            "Conclusion (I):  All stamps are drums.\n"
            "Conclusion (II): Some taps are claps."
        ),
        "question_hi": (
            "तीन कथनों के बाद निष्कर्ष I और II दिए गए हैं। आपको इन कथनों को सत्य "
            "मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों। "
            "निर्णय लीजिए कि दिए गए निष्कर्षों में से कौन-सा/से कथनों का तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी ड्रम ताली हैं।\n"
            "कुछ तालियाँ थपथपाहट हैं।\n"
            "कुछ थपथपाहट स्टाम्प हैं।\n\n"
            "निष्कर्ष (I):  सभी स्टाम्प ड्रम हैं।\n"
            "निष्कर्ष (II): कुछ थपथपाहट तालियाँ हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q58 (CHSL, 09 July 2024 Shift-3) ────────────────────────────────────
    # No Cl is Mo (E); All Mo→Ri (A); All Ri→Oc (A).
    # I:  All rivers can never be clouds →
    #     Assume All Ri→Cl: Barbara → All Mo→Cl, contradicts No Cl is Mo → IMPOSSIBLE ✓
    # II: All Mo→Oc → Barbara: All Mo→Ri + All Ri→Oc ✓
    {
        "question_number": 58,
        "difficulty": "medium",
        "source_pdf": "CHSL_09July2024_Shift3",
        "question_en": (
            "Three statements are followed by conclusions I and II. You have to "
            "consider these statements to be true, even if they seem to be at "
            "variance with commonly known facts. Decide which of the given "
            "conclusions logically follow/s from the given statements.\n\n"
            "Statements:\n"
            "No cloud is a mountain.\n"
            "All mountains are rivers.\n"
            "All rivers are oceans.\n\n"
            "Conclusion (I):  All rivers can never be clouds.\n"
            "Conclusion (II): All mountains are oceans."
        ),
        "question_hi": (
            "तीन कथनों के बाद निष्कर्ष I और II दिए गए हैं। आपको इन कथनों को सत्य "
            "मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों। "
            "निर्णय लीजिए कि दिए गए निष्कर्षों में से कौन-सा/से कथनों का तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कोई बादल पहाड़ नहीं है।\n"
            "सभी पहाड़ नदियाँ हैं।\n"
            "सभी नदियाँ महासागर हैं।\n\n"
            "निष्कर्ष (I):  सभी नदियाँ कभी बादल नहीं हो सकतीं।\n"
            "निष्कर्ष (II): सभी पहाड़ महासागर हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
    },

    # ── Q59 (GD Constable, 27 Feb 2024 Shift-1) ──────────────────────────────
    # All Re→Gr (A); Some Pi are Gr (I).
    # I:  Some Pi are not Re → middle Gr undistributed in both → fallacy ✗
    # II: All Gr→Re → invalid A-type converse of All Re→Gr ✗
    # III: Some Pi are Gr → direct restatement of Stmt II ✓
    # Custom options as per exam.
    {
        "question_number": 59,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_27Feb2024_Shift1",
        "question_en": (
            "In the following question below are given some statements followed by "
            "some conclusions based on those statements. Taking the given statements "
            "to be true even if they seem to be at variance from commonly known facts. "
            "Read all the conclusions and then decide which of the given conclusion(s) "
            "logically follows the given statements.\n\n"
            "Statements:\n"
            "All rectangles are green.\n"
            "Some pink are green.\n\n"
            "Conclusions:\n"
            "I.   Some pink are not rectangles.\n"
            "II.  All green are rectangles.\n"
            "III. Some pink are green."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कुछ कथन और उनके बाद उन कथनों पर आधारित कुछ "
            "निष्कर्ष दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, भले ही वे "
            "सामान्य ज्ञात तथ्यों से भिन्न प्रतीत होते हों, सभी निष्कर्षों को "
            "पढ़िए और तय कीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी आयत हरे हैं।\n"
            "कुछ गुलाबी हरे हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कुछ गुलाबी आयत नहीं हैं।\n"
            "II.  सभी हरे आयत हैं।\n"
            "III. कुछ गुलाबी हरे हैं।"
        ),
        "option_a": "Both conclusions I and II follow.",
        "option_b": "All conclusions I, II and III follow.",
        "option_c": "Neither conclusion follows.",
        "option_d": "Only conclusion III follows.",
        "correct_answer": "D",
    },

    # ── Q60 (CGL, 09 Sep 2024 Shift-1) ──────────────────────────────────────
    # No Ca is Pa (E); All Ca→En (A); Some En are Ba (I).
    # I:  All envelopes can never be parcels →
    #     Assume All En→Pa: Barbara: All Ca→En + All En→Pa → All Ca→Pa,
    #     contradicts No Ca is Pa → IMPOSSIBLE ✓
    # II: No Ca is Ba → middle En undistributed in both premises → fallacy ✗
    # III: All Ba→Ca → no valid derivation ✗
    # Custom options as per exam.
    {
        "question_number": 60,
        "difficulty": "hard",
        "source_pdf": "CGL_09Sep2024_Shift1",
        "question_en": (
            "Three statements are given followed by three conclusions numbered I, II "
            "and III. Assuming the statements to be true, even if they seem to be at "
            "variance with commonly known facts, decide which of the conclusions "
            "logically follow/s from the statements.\n\n"
            "Statements:\n"
            "No carton is a parcel.\n"
            "All cartons are envelopes.\n"
            "Some envelopes are bags.\n\n"
            "Conclusions:\n"
            "I.   All envelopes can never be parcels.\n"
            "II.  No carton is a bag.\n"
            "III. All bags are cartons."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद तीन निष्कर्ष I, II और III क्रमांकित हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कोई कार्टन पार्सल नहीं है।\n"
            "सभी कार्टन लिफ़ाफ़े हैं।\n"
            "कुछ लिफ़ाफ़े थैले हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   सभी लिफ़ाफ़े कभी पार्सल नहीं हो सकते।\n"
            "II.  कोई कार्टन थैला नहीं है।\n"
            "III. सभी थैले कार्टन हैं।"
        ),
        "option_a": "Only conclusion I follows.",
        "option_b": "Conclusions II and III follow.",
        "option_c": "Only conclusion II follows.",
        "option_d": "Only conclusions I and III follow.",
        "correct_answer": "A",
    },

    # ── Q61 (CGL, 09 Sep 2024 Shift-1) ──────────────────────────────────────
    # Some Te are Dr (I); Some Dr are St (I); All St→Ri (A).
    # I:  All tears can never be rivers →
    #     Assume All Te→Ri: no contradiction with any premise → NOT impossible ✗
    # II: Some Dr are Ri → Darii: Some Dr are St (I) + All St→Ri (A) → Some Dr are Ri ✓
    # III: All drops being rivers is a possibility →
    #      Some Dr are St and All St→Ri; no premise forbids All Dr→Ri → possible ✓
    # Custom options as per exam.
    {
        "question_number": 61,
        "difficulty": "hard",
        "source_pdf": "CGL_09Sep2024_Shift1",
        "question_en": (
            "Three statements are given followed by three conclusions numbered I, II "
            "and III. Assuming the statements to be true, even if they seem to be at "
            "variance with commonly known facts, decide which of the conclusions "
            "logically follow/s from the statements.\n\n"
            "Statements:\n"
            "Some tears are drops.\n"
            "Some drops are stones.\n"
            "All stones are rivers.\n\n"
            "Conclusions:\n"
            "I.   All tears can never be rivers.\n"
            "II.  Some drops are rivers.\n"
            "III. All drops being rivers is a possibility."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद तीन निष्कर्ष I, II और III क्रमांकित हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ आँसू बूँदें हैं।\n"
            "कुछ बूँदें पत्थर हैं।\n"
            "सभी पत्थर नदियाँ हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   सभी आँसू कभी नदियाँ नहीं हो सकते।\n"
            "II.  कुछ बूँदें नदियाँ हैं।\n"
            "III. सभी बूँदों का नदियाँ होना एक संभावना है।"
        ),
        "option_a": "Both conclusions I and II follow.",
        "option_b": "Only conclusion I follows.",
        "option_c": "Only conclusion III follows.",
        "option_d": "Both conclusions II and III follow.",
        "correct_answer": "D",
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
