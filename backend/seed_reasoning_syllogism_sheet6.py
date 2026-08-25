"""
seed_reasoning_syllogism_sheet6.py
====================================
Seeds Reasoning → Syllogism  Q20–Q23 (Sheet 6).
Subject : Reasoning
Topic   : Syllogism

Q20 — standard 2-conclusion 4-opt (CPO 28 June 2024 Shift-1)
Q21 — standard 2-conclusion 4-opt (CHSL 01 July 2024 Shift-1)
Q22 — standard 2-conclusion 4-opt (CPO 28 June 2024 Shift-2)
Q23 — 3-conclusion custom 4-opt  (CHSL 01 July 2024 Shift-2)

Answer key:
  Q20  C   Q21  B   Q22  B   Q23  B

Reasoning notes
───────────────
Q20  All roads→routes (A); All routes→bridges (A).
     Ro = roads, Ru = routes, Br = bridges.
     Barbara chain: All Ro→Ru + All Ru→Br → All Ro→Br.

     Conclusion I:  Some routes are roads (Some Ru are Ro).
         All Ro→Ru → Subalternation: Some Ro are Ru → I-conv: Some Ru are Ro ✓

     Conclusion II: All roads are bridges (All Ro→Br).
         Barbara (A+A→A): All Ro→Ru + All Ru→Br → All Ro→Br ✓

     Both I and II follow.

Q21  Some keys are chains (I); All chains→locks (A); No lock is rock (E).
     K = keys, Ch = chains, L = locks, R = rocks.

     Derived: Some K are Ch + All Ch→L → Darii → Some K are L.

     Conclusion I:  No rock is a key (No R is K).
         No L is R → No R is L (E-conv). Some K are L (derived). The K that
         are locks are definitely not rocks, but non-lock keys might be rocks.
         "Some K are not R" (O-type) follows, NOT the universal "No R is K". ✗

     Conclusion II: At least some keys are locks (Some K are L).
         Darii: Some K are Ch (I) + All Ch→L (A) → Some K are L ✓

     Only conclusion II follows.

Q22  All trains→buses (A); Some buses are cars (I).
     T = trains, Bu = buses, Ca = cars.

     Conclusion I:  All cars are buses (All Ca→Bu).
         Stmt II gives Some Bu are Ca → I-conv: Some Ca are Bu.
         Cannot upgrade I-type to A-type (needs All Ca are Bu not given). ✗

     Conclusion II: Some buses are trains (Some Bu are T).
         All T→Bu → Subalternation: Some T are Bu → I-conv: Some Bu are T ✓

     Only conclusion II follows.

Q23  All rings→earrings (A); Some rings are chains (I); All chains→bangles (A).
     R = rings, E = earrings, Ch = chains, Ba = bangles.

     Conclusion I:  Some rings are bangles (Some R are Ba).
         Some R are Ch (I) + All Ch→Ba (A) → Darii → Some R are Ba ✓

     Conclusion II: Some earrings are bangles (Some E are Ba).
         The ring-chains derived above are also earrings (via All R→E) AND bangles
         (via All Ch→Ba). Let X = ring-chains. X ⊆ R ⊆ E, X ⊆ Ch ⊆ Ba.
         Hence X ⊆ E ∩ Ba → Some E are Ba ✓

     Conclusion III: Some chains are earrings (Some Ch are E).
         Some R are Ch → I-conv: Some Ch are R.
         Some Ch are R (I) + All R→E (A) → Darii → Some Ch are E ✓

     All three conclusions follow.
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

    # ── Q20 (CPO, 28 June 2024 Shift-1) ─────────────────────────────────────
    # All roads→routes; All routes→bridges.
    # I:  Some routes are roads  → I-conv of subaltern of Stmt I ✓
    # II: All roads are bridges  → Barbara (A+A→A) ✓
    {
        "question_number": 20,
        "difficulty": "easy",
        "source_pdf": "CPO_28June2024_Shift1",
        "question_en": (
            "Two statements are given, followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s).\n\n"
            "Statements:\n"
            "All roads are routes.\n"
            "All routes are bridges.\n\n"
            "Conclusions:\n"
            "I.  Some routes are roads.\n"
            "II. All roads are bridges."
        ),
        "question_hi": (
            "दो कथन दिए गए हैं, जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी सड़कें मार्ग हैं।\n"
            "सभी मार्ग पुल हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ मार्ग सड़कें हैं।\n"
            "II. सभी सड़कें पुल हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
    },

    # ── Q21 (CHSL, 01 July 2024 Shift-1) ────────────────────────────────────
    # Some keys are chains (I); All chains→locks (A); No lock is rock (E).
    # I:  No rock is a key  → only "Some K not R" derivable (O), not universal E. ✗
    # II: At least some keys are locks → Darii: Some K are Ch + All Ch→L → Some K are L ✓
    {
        "question_number": 21,
        "difficulty": "medium",
        "source_pdf": "CHSL_01July2024_Shift1",
        "question_en": (
            "Read the given statements and conclusions carefully. Assuming that the "
            "information given in the statements is true, even if it appears to be "
            "at variance with commonly known facts, decide which of the given "
            "conclusions logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "Some keys are chains.\n"
            "All chains are locks.\n"
            "No lock is a rock.\n\n"
            "Conclusions:\n"
            "(I)  No rock is a key.\n"
            "(II) At least some keys are locks."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों को ध्यानपूर्वक पढ़िए। यह मानते हुए कि "
            "कथनों में दी गई जानकारी सत्य है, भले ही वह सामान्यतः ज्ञात तथ्यों "
            "से भिन्न प्रतीत होती हो, निर्णय लीजिए कि दिए गए निष्कर्षों में से "
            "कौन-सा/से कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ चाबियाँ जंजीर हैं।\n"
            "सभी जंजीर ताले हैं।\n"
            "कोई ताला चट्टान नहीं है।\n\n"
            "निष्कर्ष:\n"
            "(I)  कोई चट्टान चाबी नहीं है।\n"
            "(II) कम से कम कुछ चाबी ताले हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q22 (CPO, 28 June 2024 Shift-2) ─────────────────────────────────────
    # All trains→buses (A); Some buses are cars (I).
    # I:  All cars are buses → I-conv gives only "Some Ca are Bu"; can't upgrade to A. ✗
    # II: Some buses are trains → I-conv of subaltern of Stmt I: All T→Bu → Some Bu are T ✓
    {
        "question_number": 22,
        "difficulty": "easy",
        "source_pdf": "CPO_28June2024_Shift2",
        "question_en": (
            "Given below are two statements and two conclusions. Take the statements "
            "to be true even if they are at variance with commonly known facts, and "
            "decide whether the conclusion(s) follow(s) the given statements.\n\n"
            "Statements:\n"
            "All trains are buses.\n"
            "Some buses are cars.\n\n"
            "Conclusions:\n"
            "I.  All cars are buses.\n"
            "II. Some buses are trains."
        ),
        "question_hi": (
            "नीचे दो कथन और दो निष्कर्ष दिए गए हैं। कथनों को सत्य मानें, "
            "भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न हों, और निर्णय करें कि "
            "कौन-सा/से निष्कर्ष दिए गए कथनों का अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी रेलगाड़ियाँ बसें हैं।\n"
            "कुछ बसें कारें हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  सभी कारें बसें हैं।\n"
            "II. कुछ बसें रेलगाड़ियाँ हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q23 (CHSL, 01 July 2024 Shift-2) — 3-conclusion custom options ───────
    # All rings→earrings (A); Some rings are chains (I); All chains→bangles (A).
    # R = rings, E = earrings, Ch = chains, Ba = bangles.
    #
    # I:  Some rings are bangles
    #     Some R are Ch (I) + All Ch→Ba (A) → Darii → Some R are Ba ✓
    # II: Some earrings are bangles
    #     Ring-chains (X ⊆ R ∩ Ch) are earrings (All R→E) and bangles (All Ch→Ba).
    #     X ⊆ E ∩ Ba → Some E are Ba ✓
    # III:Some chains are earrings
    #     Some R are Ch → I-conv: Some Ch are R.
    #     Some Ch are R (I) + All R→E (A) → Darii → Some Ch are E ✓
    #
    # All three conclusions follow.
    {
        "question_number": 23,
        "difficulty": "hard",
        "source_pdf": "CHSL_01July2024_Shift2",
        "question_en": (
            "In this question, three statements are given, followed by three "
            "conclusions numbered I, II and III. Assuming the statements to be true, "
            "even if they seem to be at variance with commonly known facts, decide "
            "which of the conclusion(s) logically follow/from the statements.\n\n"
            "Statements:\n"
            "All rings are earrings.\n"
            "Some rings are chains.\n"
            "All chains are bangles.\n\n"
            "Conclusions:\n"
            "I.   Some rings are bangles.\n"
            "II.  Some earrings are bangles.\n"
            "III. Some chains are earrings."
        ),
        "question_hi": (
            "इस प्रश्न में तीन कथन दिए गए हैं, जिनके बाद I, II और III अंकित तीन "
            "निष्कर्ष दिए गए हैं। कथनों को सत्य मानते हुए, भले ही वे सामान्यतः "
            "ज्ञात तथ्यों से भिन्न प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से "
            "निष्कर्ष कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी रिंग इयरिंग हैं।\n"
            "कुछ रिंग चेन हैं।\n"
            "सभी चेन कंगन हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कुछ रिंग कंगन हैं।\n"
            "II.  कुछ इयरिंग कंगन हैं।\n"
            "III. कुछ चेन इयरिंग हैं।"
        ),
        "option_a": "Neither conclusion I, II and III follow. / कोई भी निष्कर्ष I, II और III अनुसरण नहीं करता है।",
        "option_b": "All conclusions I, II, and III follow. / सभी निष्कर्ष I, II, और III अनुसरण करते हैं।",
        "option_c": "Both conclusions I and III follow. / दोनों निष्कर्ष I और III अनुसरण करते हैं।",
        "option_d": "Both conclusions I and II follow. / दोनों निष्कर्ष I और II अनुसरण करते हैं।",
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
