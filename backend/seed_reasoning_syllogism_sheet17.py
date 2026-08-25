"""
seed_reasoning_syllogism_sheet17.py
=====================================
Seeds Reasoning → Syllogism  Q79–Q83 (Sheet 17).
Subject : Reasoning
Topic   : Syllogism

Q79 — standard 2-conclusion (CPO 29 June 2024 Shift-3)
Q80 — standard 2-conclusion (CPO 29 June 2024 Shift-3)
Q81 — 3-conclusion custom   (CGL 12 Sep 2024 Shift-1)
Q82 — 3-conclusion custom   (CGL 12 Sep 2024 Shift-2)
Q83 — 3-conclusion custom   (CGL 18 Sep 2024 Shift-1)

Answer key:
  Q79  B   Q80  B   Q81  C   Q82  D   Q83  B

Reasoning notes
───────────────
Q79  All Pl→Fi (A); Some Fi are Le (I).
     I:  Some Pl are Le → middle Fi: All Pl→Fi (Fi undistrib. as predicate, A-type) +
         Some Fi are Le (Fi undistrib. as subject, I-type) → fallacy of undistributed middle ✗
     II: Some Fi are Pl → subalternation of All Pl→Fi: Some Pl are Fi → I-conv: Some Fi are Pl ✓
     Only conclusion II follows.

Q80  All Lu→Ca (A); All Ca→Sc (A).
     Barbara: All Lu→Ca + All Ca→Sc → All Lu→Sc.
     I:  Some Ca are not Sc (O-type) → directly contradicts All Ca→Sc (A-type) ✗
     II: Some Sc are Ca → subalternation of All Ca→Sc: Some Ca are Sc → I-conv: Some Sc are Ca ✓
     Only conclusion II follows.

Q81  All Pa→Di (A); Some Di are Bo (I); All Bo→No (A).
     Darii (M=Bo, S=Di, P=No): All Bo→No + Some Di are Bo → Some Di are No.
     I:  No Pa is No (E-type) → no E-premise involving Pa and No; no valid chain ✗
     II: All diaries being notebooks is a possibility →
         Assume All Di→No: no contradiction with any premise (All Pa→Di → All Pa→No,
         consistent). But the exam treats this standard possibility claim as not separately
         actionable given only Some Di are No is established ✗ (exam answer)
     III: Some Di are No → Darii: Some Di are Bo (I) + All Bo→No (A) → Some Di are No ✓
     Only conclusion III follows.

Q82  All Ca→Po (A); Some Po are Bo (I); All Bo→No (A).
     I:  Some Po are No →
         Darii (M=Bo, S=Po, P=No): All Bo→No + Some Po are Bo → Some Po are No ✓
     II: No Ca is Bo (E-type) →
         Middle Po: All Ca→Po (Po undistrib. as predicate) + Some Po are Bo (Po undistrib.
         as subject) → fallacy of undistributed middle ✗
     III: All Ca→No (A-type) →
         All Ca→Po + Some Po are Bo + All Bo→No: only get Some Po are No (I via Darii),
         not All Po→No (A-type); Barbara chain incomplete ✗
     Only conclusion I follows.

Q83  Some Pi are Or (I); All Or→Ba (A); All Ba→Pl (A).
     Barbara: All Or→Ba + All Ba→Pl → All Or→Pl.
     Darii step 1: Some Pi are Or (I) + All Or→Ba (A) → Some Pi are Ba.
     Darii step 2: Some Pi are Ba (I) + All Ba→Pl (A) → Some Pi are Pl.
     I:  Some Pi are Pl → chain of Darii (step 1 + step 2) ✓
     II: All Or→Pl → Barbara: All Or→Ba + All Ba→Pl ✓
     III: No Pi is Ba (E-type) → contradicts derived "Some Pi are Ba" ✗
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

    # ── Q79 (CPO, 29 June 2024 Shift-3) ─────────────────────────────────────
    # All Pl→Fi (A); Some Fi are Le (I).
    # I:  Some Pl are Le → undistributed middle (Fi in both premises) ✗
    # II: Some Fi are Pl → subalternation + I-conv of All Pl→Fi ✓
    # Only conclusion II follows.
    {
        "question_number": 79,
        "difficulty": "medium",
        "source_pdf": "CPO_29June2024_Shift3",
        "question_en": (
            "Two statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide whether the conclusion(s) follow/s the given "
            "statements.\n\n"
            "Statements:\n"
            "All plastics are fibres.\n"
            "Some fibres are leathers.\n\n"
            "Conclusions:\n"
            "I.  Some plastics are leathers.\n"
            "II. Some fibres are plastics."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं जिनके बाद दो निष्कर्ष I और II दिए गए हैं। कथनों को सत्य "
            "मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों, "
            "निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी प्लास्टिक फाइबर हैं।\n"
            "कुछ फाइबर चमड़े हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ प्लास्टिक चमड़े हैं।\n"
            "II. कुछ फाइबर प्लास्टिक हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q80 (CPO, 29 June 2024 Shift-3) ─────────────────────────────────────
    # All Lu→Ca (A); All Ca→Sc (A). Barbara: All Lu→Sc.
    # I:  Some Ca are not Sc (O-type) → contradicts All Ca→Sc (A-type) ✗
    # II: Some Sc are Ca → subalternation of All Ca→Sc → I-conv ✓
    # Only conclusion II follows.
    {
        "question_number": 80,
        "difficulty": "medium",
        "source_pdf": "CPO_29June2024_Shift3",
        "question_en": (
            "Two statements are given, followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow(s) from "
            "the statements.\n\n"
            "Statements:\n"
            "All ludos are caroms.\n"
            "All caroms are scrabbles.\n\n"
            "Conclusions:\n"
            "I.  Some caroms are not scrabbles.\n"
            "II. Some scrabbles are caroms."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं, जिनके बाद दो निष्कर्ष I और II दिए गए हैं। कथनों को सत्य "
            "मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों, "
            "निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी लूडो कैरम हैं।\n"
            "सभी कैरम स्क्रैबल हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ कैरम स्क्रैबल नहीं हैं।\n"
            "II. कुछ स्क्रैबल कैरम हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q81 (CGL, 12 Sep 2024 Shift-1) ──────────────────────────────────────
    # All Pa→Di (A); Some Di are Bo (I); All Bo→No (A).
    # I:  No Pa is No (E-type) → no E-premise or valid chain ✗
    # II: All diaries being notebooks is a possibility → not accepted by exam ✗
    # III: Some Di are No → Darii: Some Di are Bo + All Bo→No ✓
    # Only conclusion III follows.
    {
        "question_number": 81,
        "difficulty": "medium",
        "source_pdf": "CGL_12Sep2024_Shift1",
        "question_en": (
            "Three statements are given, followed by three conclusions numbered I, II and III. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow/s from "
            "the statements.\n\n"
            "Statements:\n"
            "All pages are diaries.\n"
            "Some diaries are books.\n"
            "All books are notebooks.\n\n"
            "Conclusions:\n"
            "I.   No page is a notebook.\n"
            "II.  All diaries being notebooks is a possibility.\n"
            "III. Some diaries are notebooks."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं, जिनके बाद तीन निष्कर्ष I, II और III क्रमांकित हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी पृष्ठ डायरी हैं।\n"
            "कुछ डायरियाँ किताबें हैं।\n"
            "सभी किताबें नोटबुक हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कोई भी पृष्ठ नोटबुक नहीं है।\n"
            "II.  सभी डायरियों का नोटबुक होना एक संभावना है।\n"
            "III. कुछ डायरियाँ नोटबुक हैं।"
        ),
        "option_a": "Both conclusions I and II follow.",
        "option_b": "Only conclusions I and III follow.",
        "option_c": "Only conclusion III follows.",
        "option_d": "Only conclusion II follows.",
        "correct_answer": "C",
    },

    # ── Q82 (CGL, 12 Sep 2024 Shift-2) ──────────────────────────────────────
    # All Ca→Po (A); Some Po are Bo (I); All Bo→No (A).
    # I:  Some Po are No → Darii: Some Po are Bo + All Bo→No → Some Po are No ✓
    # II: No Ca is Bo (E-type) → middle Po undistributed in both premises → fallacy ✗
    # III: All Ca→No (A-type) → Barbara chain incomplete (only Some Po are No, not All Po→No) ✗
    # Only conclusion I follows.
    {
        "question_number": 82,
        "difficulty": "medium",
        "source_pdf": "CGL_12Sep2024_Shift2",
        "question_en": (
            "Three statements are given followed by three conclusions numbered I, II and III. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow/s from "
            "the statements.\n\n"
            "Statements:\n"
            "All cards are postcards.\n"
            "Some postcards are books.\n"
            "All books are novels.\n\n"
            "Conclusions:\n"
            "I.   Some postcards are novels.\n"
            "II.  No card is a book.\n"
            "III. All cards are novels."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद तीन निष्कर्ष I, II और III क्रमांकित हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी कार्ड पोस्टकार्ड हैं।\n"
            "कुछ पोस्टकार्ड किताबें हैं।\n"
            "सभी किताबें उपन्यास हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कुछ पोस्टकार्ड उपन्यास हैं।\n"
            "II.  कोई कार्ड किताब नहीं है।\n"
            "III. सभी कार्ड उपन्यास हैं।"
        ),
        "option_a": "Only conclusions II and III follow.",
        "option_b": "Only conclusion III follows.",
        "option_c": "Only conclusions I and II follow.",
        "option_d": "Only conclusion I follows.",
        "correct_answer": "D",
    },

    # ── Q83 (CGL, 18 Sep 2024 Shift-1) ──────────────────────────────────────
    # Some Pi are Or (I); All Or→Ba (A); All Ba→Pl (A).
    # Barbara: All Or→Ba + All Ba→Pl → All Or→Pl.
    # Darii (step 1): Some Pi are Or + All Or→Ba → Some Pi are Ba.
    # Darii (step 2): Some Pi are Ba + All Ba→Pl → Some Pi are Pl.
    # I:  Some Pi are Pl → chain of Darii (steps 1+2) ✓
    # II: All Or→Pl → Barbara: All Or→Ba + All Ba→Pl ✓
    # III: No Pi is Ba → contradicts derived "Some Pi are Ba" ✗
    # Both conclusions I and II follow.
    {
        "question_number": 83,
        "difficulty": "medium",
        "source_pdf": "CGL_18Sep2024_Shift1",
        "question_en": (
            "Three statements are given, followed by three conclusions numbered I, II and III. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow/s from "
            "the statements.\n\n"
            "Statements:\n"
            "Some pineapples are oranges.\n"
            "All oranges are bananas.\n"
            "All bananas are plums.\n\n"
            "Conclusions:\n"
            "I.   Some pineapples are plums.\n"
            "II.  All oranges are plums.\n"
            "III. No pineapple is a banana."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं, जिनके बाद तीन निष्कर्ष I, II और III क्रमांकित हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ अनानास संतरे हैं।\n"
            "सभी संतरे केले हैं।\n"
            "सभी केले बेर हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कुछ अनानास बेर हैं।\n"
            "II.  सभी संतरे बेर हैं।\n"
            "III. कोई अनानास केला नहीं है।"
        ),
        "option_a": "Only conclusions I and III follow.",
        "option_b": "Both conclusions I and II follow.",
        "option_c": "Only conclusion III follows.",
        "option_d": "Only conclusions II and III follow.",
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
