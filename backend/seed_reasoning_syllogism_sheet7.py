"""
seed_reasoning_syllogism_sheet7.py
====================================
Seeds Reasoning → Syllogism  Q24–Q26 (Sheet 7).
Subject : Reasoning
Topic   : Syllogism

Q24 — standard 2-conclusion 4-opt (CPO 28 June 2024 Shift-2)
Q25 — standard 2-conclusion 4-opt (CHSL 01 July 2024 Shift-3)
Q26 — standard 2-conclusion 4-opt (CHSL 01 July 2024 Shift-4)

Answer key:
  Q24  C   Q25  C   Q26  D

Reasoning notes
───────────────
Q24  All pebbles→shells (A); No shell is a stone (E).
     Pe = pebbles, Sh = shells, St = stones.

     Conclusion I:  Some pebbles are shells (Some Pe are Sh).
         Subalternation of Stmt I: All Pe→Sh → Some Pe are Sh ✓
         (A-type gives I-type by subalternation)

     Conclusion II: No shells are stones (No Sh is St).
         Identical to Stmt II ("No shell is a stone") — direct restatement ✓

     Both I and II follow.
     (Tests whether students recognise subalternation and premise-restatement
     as valid conclusions — a classic trap in competitive-exam syllogism.)

Q25  Some handles are bars (I); All bars→rods (A); No rod is a stick (E).
     H = handles, Ba = bars, Ro = rods, St = sticks.

     Conclusion I:  Some handles are rods (Some H are Ro).
         Darii: Some H are Ba (I) + All Ba→Ro (A) → Some H are Ro ✓

     Conclusion II: No bar is a stick (No Ba is St).
         Celarent: All Ba→Ro (A) + No Ro is St (E) → No Ba is St ✓
         (All bars are rods; no rod is a stick; therefore no bar is a stick.)

     Both I and II follow.

Q26  All watches→dials (A); All dials→phones (A); Some phones are mobiles (I).
     W = watches, D = dials, Ph = phones, Mo = mobiles.

     Barbara chain: All W→D + All D→Ph → All W→Ph.

     Conclusion I:  No watch is a phone (No W is Ph).
         Barbara gives All W→Ph; "No W is Ph" directly contradicts this. ✗

     Conclusion II: Some dials are mobiles (Some D are Mo).
         All D→Ph (A) + Some Ph are Mo (I):
         Middle term Ph — undistributed as predicate in A ("All D is Ph") and
         as subject in I ("Some Ph are Mo"). Fallacy of undistributed middle
         → no valid conclusion about D and Mo. ✗
         (Mobile-phones may be the non-dial portion of phones; D and Mo
         need not overlap.)

     Neither I nor II follows.
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

    # ── Q24 (CPO, 28 June 2024 Shift-2) ─────────────────────────────────────
    # All pebbles→shells; No shell is a stone.
    # I:  Some pebbles are shells → Subalternation of Stmt I ✓
    # II: No shells are stones    → Restatement of Stmt II ✓
    {
        "question_number": 24,
        "difficulty": "easy",
        "source_pdf": "CPO_28June2024_Shift2",
        "question_en": (
            "Two statements are given, followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s) from the statements.\n\n"
            "Statements:\n"
            "All pebbles are shells.\n"
            "No shell is a stone.\n\n"
            "Conclusions:\n"
            "I.  Some pebbles are shells.\n"
            "II. No shells are stones."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं, जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी कंकड़ शैल हैं।\n"
            "कोई शैल पत्थर नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ कंकड़ शैल हैं।\n"
            "II. कोई शैल पत्थर नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
    },

    # ── Q25 (CHSL, 01 July 2024 Shift-3) ────────────────────────────────────
    # Some handles are bars (I); All bars→rods (A); No rod is a stick (E).
    # I:  Some handles are rods → Darii (I+A) ✓
    # II: No bar is a stick     → Celarent (A+E) ✓
    {
        "question_number": 25,
        "difficulty": "medium",
        "source_pdf": "CHSL_01July2024_Shift3",
        "question_en": (
            "Read the given statements and conclusions carefully. Assuming that the "
            "information given in the statements is true, even if it appears to be "
            "at variance with commonly known facts, decide which of the given "
            "conclusions logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "Some handles are bars.\n"
            "All bars are rods.\n"
            "No rod is a stick.\n\n"
            "Conclusions:\n"
            "(I)  Some handles are rods.\n"
            "(II) No bar is a stick."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों को ध्यानपूर्वक पढ़िए। यह मानते हुए कि "
            "कथनों में दी गई जानकारी सत्य है, भले ही वह सामान्यतः ज्ञात तथ्यों "
            "से भिन्न प्रतीत होती हो, निर्णय लीजिए कि दिए गए निष्कर्षों में से "
            "कौन-सा/से कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ हैंडल बार हैं।\n"
            "सभी बार रॉड हैं।\n"
            "कोई रॉड स्टिक नहीं है।\n\n"
            "निष्कर्ष:\n"
            "(I)  कुछ हैंडल रॉड हैं।\n"
            "(II) कोई बार स्टिक नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
    },

    # ── Q26 (CHSL, 01 July 2024 Shift-4) ────────────────────────────────────
    # All watches→dials (A); All dials→phones (A); Some phones are mobiles (I).
    # Barbara chain: All W→D + All D→Ph → All W→Ph.
    # I:  No watch is a phone   → contradicts Barbara chain (All W→Ph). ✗
    # II: Some dials are mobiles → A+I, Ph undistributed in both premises
    #     (predicate of A, subject of I) → fallacy of undistributed middle. ✗
    {
        "question_number": 26,
        "difficulty": "hard",
        "source_pdf": "CHSL_01July2024_Shift4",
        "question_en": (
            "Read the given statements and conclusions carefully. Assuming that the "
            "information given in the statements is true, even if it appears to be "
            "at variance with commonly known facts, decide which of the given "
            "conclusions logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "All watches are dials.\n"
            "All dials are phones.\n"
            "Some phones are mobiles.\n\n"
            "Conclusions:\n"
            "(I)  No watch is a phone.\n"
            "(II) Some dials are mobiles."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों को ध्यानपूर्वक पढ़िए। यह मानते हुए कि "
            "कथनों में दी गई जानकारी सत्य है, भले ही वह सामान्यतः ज्ञात तथ्यों "
            "से भिन्न प्रतीत होती हो, निर्णय लीजिए कि दिए गए निष्कर्षों में से "
            "कौन-सा/से कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी घड़ियाँ डायल हैं।\n"
            "सभी डायल फोन हैं।\n"
            "कुछ फोन मोबाइल हैं।\n\n"
            "निष्कर्ष:\n"
            "(I)  कोई घड़ी फोन नहीं है।\n"
            "(II) कुछ डायल मोबाइल हैं।"
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
