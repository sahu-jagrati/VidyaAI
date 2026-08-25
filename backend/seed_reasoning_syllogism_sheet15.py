"""
seed_reasoning_syllogism_sheet15.py
=====================================
Seeds Reasoning → Syllogism  Q67–Q72 (Sheet 15).
Subject : Reasoning
Topic   : Syllogism

Q67 — 3-conclusion custom   (CGL 11 Sep 2024 Shift-2)
Q68 — standard 2-conclusion (CPO 29 June 2024 Shift-2)
Q69 — standard 2-conclusion (CPO 29 June 2024 Shift-1)
Q70 — standard 2-conclusion (CPO 29 June 2024 Shift-1)
Q71 — standard 2-conclusion (CPO 29 June 2024 Shift-2)
Q72 — standard 2-conclusion (CPO 29 June 2024 Shift-1)

Answer key:
  Q67  D   Q68  D   Q69  C   Q70  D   Q71  C   Q72  C

Reasoning notes
───────────────
Q67  All Pe→Pa (A); Some Pa are Pi (I); Some Pi are Bo (I).
     I:  Some Pi are Pe → need to go Pi→Pa→Pe; middle=Pa:
         Some Pa are Pi (I) + All Pe→Pa (subalternation gives Some Pa are Pe)
         → I+I = no valid conclusion. ✗
     II: Some Bo are Pa → middle=Pi: Some Pi are Bo (I) + Some Pa are Pi (I-conv)
         → I+I = no valid conclusion. ✗
     III: Some Pi are Bo → literal restatement of Stmt III ✓
     Option: "Either conclusion I or conclusion III follows" (III being the one that follows).

Q68  No Pl is Bo (E); All Pl→Tu (A).
     I:  No Tu is Pl (E-type) →
         E-conversion: No Tu is Pl ↔ No Pl is Tu. But All Pl→Tu contradicts No Pl is Tu.
         Conclusion I is IMPOSSIBLE (contradicted by premises). ✗
     II: Some Tu are Bo (I-type) →
         Only A and E premises; no I-type premise → cannot derive I-type conclusion. ✗
     Neither conclusion I nor II follows.

Q69  All Pa→Tr (A); Some Pa are Le (I).
     I:  Some Tr are Le →
         Darii (M=Pa, S=Le, P=Tr): All Pa→Tr (A) + Some Le are Pa (I-conv of Some Pa are Le)
         → Some Le are Tr (I) → I-conv: Some Tr are Le ✓
     II: Some Tr are Pa →
         Subalternation of All Pa→Tr: Some Pa are Tr → I-conv: Some Tr are Pa ✓
     Both conclusions I and II follow.

Q70  All Ne→Fi (A); Some Fi are Wi (I).
     I:  All networks can never be wires →
         Assume All Ne→Wi: Ne ⊆ Fi (from Stmt I) and Ne ⊆ Wi (assumed).
         No contradiction with "Some Fi are Wi." → NOT impossible ✗
     II: Some Ne are Wi →
         Middle term Fi: All Ne→Fi (A, Fi is predicate, undistributed) +
         Some Fi are Wi (I, Fi is subject). Undistributed middle (Fi) → fallacy ✗
         The wires could lie entirely in the non-network part of fibers.
     Neither conclusion I nor II follows.

Q71  Some Cl are Sa (I); All Sa→Si (A).
     I:  Some Cl are Si →
         Darii (M=Sa, S=Cl, P=Si): All Sa→Si (A) + Some Cl are Sa (I) → Some Cl are Si ✓
     II: Some Si are Sa →
         Subalternation of All Sa→Si: Some Sa are Si → I-conv: Some Si are Sa ✓
     Both conclusions I and II follow.

Q72  All No→Er (A); All Er→Pe (A).
     I:  All No→Pe → Barbara: All No→Er + All Er→Pe → All No→Pe ✓
     II: Some Pe are No →
         Derived All No→Pe: subalternation → Some No are Pe → I-conv: Some Pe are No ✓
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

    # ── Q67 (CGL, 11 Sep 2024 Shift-2) ──────────────────────────────────────
    # All Pe→Pa (A); Some Pa are Pi (I); Some Pi are Bo (I).
    # I:  Some Pi are Pe → I+I = no conclusion ✗
    # II: Some Bo are Pa → I+I = no conclusion ✗
    # III: Some Pi are Bo → direct restatement of Stmt III ✓
    # Custom options as per exam.
    {
        "question_number": 67,
        "difficulty": "medium",
        "source_pdf": "CGL_11Sep2024_Shift2",
        "question_en": (
            "Three statements are followed by three conclusions numbered I, II and III. "
            "You have to consider these statements to be true, even if they seem to be at "
            "variance with commonly known facts. Decide which of the given conclusions "
            "logically follow/s from the given statements.\n\n"
            "Statements:\n"
            "All pens are pages.\n"
            "Some pages are pins.\n"
            "Some pins are boards.\n\n"
            "Conclusions:\n"
            "I.   Some pins are pens.\n"
            "II.  Some boards are pages.\n"
            "III. Some pins are boards."
        ),
        "question_hi": (
            "तीन कथनों के बाद तीन निष्कर्ष I, II और III दिए गए हैं। आपको इन कथनों को "
            "सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों। "
            "निर्णय लीजिए कि दिए गए निष्कर्षों में से कौन-सा/से कथनों का तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी पेन पेज हैं।\n"
            "कुछ पेज पिन हैं।\n"
            "कुछ पिन बोर्ड हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कुछ पिन पेन हैं।\n"
            "II.  कुछ बोर्ड पेज हैं।\n"
            "III. कुछ पिन बोर्ड हैं।"
        ),
        "option_a": "Only conclusion I follows.",
        "option_b": "None of the conclusions follows.",
        "option_c": "Only conclusion II follows.",
        "option_d": "Either conclusion I or conclusion III follows.",
        "correct_answer": "D",
    },

    # ── Q68 (CPO, 29 June 2024 Shift-2) ─────────────────────────────────────
    # No Pl is Bo (E); All Pl→Tu (A).
    # I:  No Tu is Pl → E-conv: No Pl is Tu, contradicts All Pl→Tu ✗
    # II: Some Tu are Bo → no I-type premise; E+A cannot yield I-type ✗
    # Neither conclusion I nor II follows.
    {
        "question_number": 68,
        "difficulty": "medium",
        "source_pdf": "CPO_29June2024_Shift2",
        "question_en": (
            "Two statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow(s) from "
            "the statements.\n\n"
            "Statements:\n"
            "No plate is a bowl.\n"
            "All plates are tumblers.\n\n"
            "Conclusions:\n"
            "I.  No tumbler is a plate.\n"
            "II. Some tumblers are bowls."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं जिनके बाद दो निष्कर्ष I और II दिए गए हैं। कथनों को सत्य "
            "मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों, "
            "निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "कोई प्लेट कटोरा नहीं है।\n"
            "सभी प्लेट गिलास हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कोई गिलास प्लेट नहीं है।\n"
            "II. कुछ गिलास कटोरे हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q69 (CPO, 29 June 2024 Shift-1) ─────────────────────────────────────
    # All Pa→Tr (A); Some Pa are Le (I).
    # I:  Some Tr are Le → Darii: Some Le are Pa (I-conv) + All Pa→Tr → Some Le are Tr → I-conv ✓
    # II: Some Tr are Pa → subalternation of All Pa→Tr → I-conv ✓
    # Both conclusions I and II follow.
    {
        "question_number": 69,
        "difficulty": "easy",
        "source_pdf": "CPO_29June2024_Shift1",
        "question_en": (
            "Two statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow(s) from "
            "the statements.\n\n"
            "Statements:\n"
            "All papers are trees.\n"
            "Some papers are leaves.\n\n"
            "Conclusions:\n"
            "I.  Some trees are leaves.\n"
            "II. Some trees are papers."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं जिनके बाद दो निष्कर्ष I और II दिए गए हैं। कथनों को सत्य "
            "मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों, "
            "निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी कागज पेड़ हैं।\n"
            "कुछ कागज पत्ते हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ पेड़ पत्ते हैं।\n"
            "II. कुछ पेड़ कागज हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
    },

    # ── Q70 (CPO, 29 June 2024 Shift-1) ─────────────────────────────────────
    # All Ne→Fi (A); Some Fi are Wi (I).
    # I:  All networks can never be wires →
    #     Assume All Ne→Wi: Ne⊆Fi and Ne⊆Wi → no contradiction → NOT impossible ✗
    # II: Some Ne are Wi →
    #     Middle Fi undistributed in both premises (predicate in A, subject in I) → fallacy ✗
    # Neither conclusion I nor II follows.
    {
        "question_number": 70,
        "difficulty": "medium",
        "source_pdf": "CPO_29June2024_Shift1",
        "question_en": (
            "Two statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow(s) from "
            "the statements.\n\n"
            "Statements:\n"
            "1) All networks are fibers.\n"
            "2) Some fibers are wires.\n\n"
            "Conclusions:\n"
            "I.  All networks can never be wires.\n"
            "II. Some networks are wires."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं, जिनके बाद I और II क्रमांकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्य तथ्यों से भिन्न प्रतीत होते हों, "
            "तय करें कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "1) सभी नेटवर्क फाइबर हैं।\n"
            "2) कुछ फाइबर तार हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  सभी नेटवर्क कभी भी तार नहीं हो सकते।\n"
            "II. कुछ नेटवर्क तार हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q71 (CPO, 29 June 2024 Shift-2) ─────────────────────────────────────
    # Some Cl are Sa (I); All Sa→Si (A).
    # I:  Some Cl are Si → Darii (M=Sa, S=Cl, P=Si): All Sa→Si + Some Cl are Sa → Some Cl are Si ✓
    # II: Some Si are Sa → subalternation of All Sa→Si: Some Sa are Si → I-conv: Some Si are Sa ✓
    # Both conclusions I and II follow.
    {
        "question_number": 71,
        "difficulty": "easy",
        "source_pdf": "CPO_29June2024_Shift2",
        "question_en": (
            "Two statements are given, followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow/s from "
            "the statements.\n\n"
            "Statements:\n"
            "Some clothes are sarees.\n"
            "All sarees are silks.\n\n"
            "Conclusions:\n"
            "I.  Some clothes are silks.\n"
            "II. Some silks are sarees."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं, जिनके बाद दो निष्कर्ष I और II दिए गए हैं। कथनों को सत्य "
            "मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों, तय "
            "करें कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ कपड़े साड़ियाँ हैं।\n"
            "सभी साड़ियाँ रेशम हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ कपड़े रेशम हैं।\n"
            "II. कुछ रेशम साड़ियाँ हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
    },

    # ── Q72 (CPO, 29 June 2024 Shift-1) ─────────────────────────────────────
    # All No→Er (A); All Er→Pe (A).
    # I:  All No→Pe → Barbara: All No→Er + All Er→Pe → All No→Pe ✓
    # II: Some Pe are No → derived All No→Pe: subalternation → Some No are Pe → I-conv ✓
    # Both conclusions I and II follow.
    {
        "question_number": 72,
        "difficulty": "easy",
        "source_pdf": "CPO_29June2024_Shift1",
        "question_en": (
            "Two statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow/s from "
            "the statements.\n\n"
            "Statements:\n"
            "All notebooks are erasers.\n"
            "All erasers are pens.\n\n"
            "Conclusions:\n"
            "I.  All notebooks are pens.\n"
            "II. Some pens are notebooks."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं जिनके बाद दो निष्कर्ष I और II दिए गए हैं। कथनों को सत्य "
            "मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों, "
            "निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी नोटबुक, इरेज़र हैं।\n"
            "सभी इरेज़र, पेन हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  सभी नोटबुक, पेन हैं।\n"
            "II. कुछ पेन, नोटबुक हैं।"
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
