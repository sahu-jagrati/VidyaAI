"""
seed_reasoning_syllogism_sheet5.py
====================================
Seeds Reasoning → Syllogism  Q17–Q19 (Sheet 5).
Subject : Reasoning
Topic   : Syllogism

Q17 — standard 2-conclusion 4-opt (GD Constable 20 Feb 2024 Shift-3)
Q18 — standard 2-conclusion 4-opt (CPO 28 June 2024 Shift-1)
Q19 — 3-conclusion custom 4-opt  (CPO 28 June 2024 Shift-1)

Answer key:
  Q17  D   Q18  D   Q19  B

Reasoning notes
───────────────
Q17  All pens→stationery (A); Some stationery are rubbers (I);
     All markers→pens (A).
     Derived: All M→P→S (All markers are stationery items).

     Conclusion I:  Some stationery items are not rubbers.
         "Some S are R" (I-type) does NOT imply "Some S are not R" (O-type).
         We cannot prove any stationery item MUST be a non-rubber from these
         premises. Fallacy: treating partial I-type as implying exclusion. ✗

     Conclusion II: Some markers are not stationery items.
         Directly contradicted by All M→P→S (all markers ARE stationery). ✗

     Neither I nor II follows.

Q18  All games→tournaments (A); Some tournaments are matches (I).
     G = games, T = tournaments, M = matches.

     Conclusion I:  All games are matches (All G→M).
         Requires All T→M (Barbara). Only Some T are M (I-type) given. ✗

     Conclusion II: No game is a tournament.
         Directly contradicts Stmt I (All G→T). ✗

     Neither I nor II follows.

Q19  All blues→reds (A); All greens→blues (A).
     B = blues, R = reds, G = greens.
     Chain: All G→B→R (Barbara — All greens are reds).

     Conclusion I:  No red is a blue.
         All B→R → I-conv: Some R are B → "No R is B" contradicts this. ✗

     Conclusion II: No blue is a green.
         All G→B → I-conv: Some B are G → "No B is G" contradicts this. ✗

     Conclusion III: No green is a red.
         All G→B→R means ALL greens ARE reds → direct contradiction. ✗

     None of the conclusions follow.
     (Classic trap: "All A is B" does NOT yield "No B is A".)
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

    # ── Q17 (GD Constable, 20 Feb 2024 Shift-3) ─────────────────────────────
    # All pens→stationery; Some stationery are rubbers; All markers→pens.
    # I:  Some stationery are not rubbers → I-type "Some S are R" can't prove O-type. ✗
    # II: Some markers are not stationery → contradicts All M→P→S. ✗
    {
        "question_number": 17,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_20Feb2024_Shift3",
        "question_en": (
            "Three statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s) from the statements.\n\n"
            "Statement I:   All pens are stationery items.\n"
            "Statement II:  Some stationery items are rubbers.\n"
            "Statement III: All markers are pens.\n\n"
            "Conclusion I:  Some stationery items are not rubbers.\n"
            "Conclusion II: Some markers are not stationery items."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन I:   सभी पेन स्टेशनरी आइटम हैं।\n"
            "कथन II:  कुछ स्टेशनरी आइटम रबर हैं।\n"
            "कथन III: सभी मार्कर पेन हैं।\n\n"
            "निष्कर्ष I:  कुछ स्टेशनरी आइटम रबर नहीं हैं।\n"
            "निष्कर्ष II: कुछ मार्कर स्टेशनरी आइटम नहीं हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q18 (CPO, 28 June 2024 Shift-1) ─────────────────────────────────────
    # All games→tournaments; Some tournaments are matches.
    # I:  All games are matches → needs All T→M; only Some T are M given. ✗
    # II: No game is a tournament → contradicts Stmt I directly. ✗
    {
        "question_number": 18,
        "difficulty": "easy",
        "source_pdf": "CPO_28June2024_Shift1",
        "question_en": (
            "Two statements are given, followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s).\n\n"
            "Statements:\n"
            "All games are tournaments.\n"
            "Some tournaments are matches.\n\n"
            "Conclusions:\n"
            "I.  All games are matches.\n"
            "II. No game is a tournament."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं, जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी खेल टूर्नामेंट हैं।\n"
            "कुछ टूर्नामेंट मैच हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  सभी खेल मैच हैं।\n"
            "II. कोई भी खेल टूर्नामेंट नहीं हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q19 (CPO, 28 June 2024 Shift-1) — 3-conclusion custom options ────────
    # All blues→reds (A); All greens→blues (A).
    # Chain: All G→B→R via Barbara.
    # I:  No red is a blue  → All B→R gives Some R are B (I-conv); "No R is B" false. ✗
    # II: No blue is a green → All G→B gives Some B are G (I-conv); "No B is G" false. ✗
    # III:No green is a red  → All G→R (Barbara); "No G is R" direct contradiction. ✗
    # None of the conclusions follow.
    {
        "question_number": 19,
        "difficulty": "medium",
        "source_pdf": "CPO_28June2024_Shift1",
        "question_en": (
            "Two Statements are given followed by Three conclusions numbered I, II and III. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s) from the statements.\n\n"
            "Statements:\n"
            "All blues are reds.\n"
            "All greens are blues.\n\n"
            "Conclusions:\n"
            "I.   No red is a blue.\n"
            "II.  No blue is a green.\n"
            "III. No green is a red."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं जिनके बाद I, II और III अंकित तीन निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी नीला लाल हैं।\n"
            "सभी हरा नीला हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कोई लाल नीला नहीं है।\n"
            "II.  कोई नीला हरा नहीं है।\n"
            "III. कोई हरा लाल नहीं है।"
        ),
        "option_a": "Both conclusions I and III follow. / दोनों निष्कर्ष I और III अनुसरण करते हैं।",
        "option_b": "None of the conclusions follow. / कोई भी निष्कर्ष अनुसरण नहीं करता है।",
        "option_c": "Both conclusions I and II follow. / दोनों निष्कर्ष I और II अनुसरण करते हैं।",
        "option_d": "Both conclusions II and III follow. / दोनों निष्कर्ष II और III अनुसरण करते हैं।",
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
