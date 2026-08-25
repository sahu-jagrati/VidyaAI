"""
seed_reasoning_syllogism_sheet19.py  —  Reasoning → Syllogism  Q90–Q95
Q90  A  CGL_19Sep2024_Shift3        standard 2-conclusion
Q91  B  GD_Constable_27Feb2024_Shift3  standard 2-conclusion
Q92  A  GD_Constable_27Feb2024_Shift4  standard 2-conclusion
Q93  A  GD_Constable_30March2024_Shift1  3-conclusion CUSTOM options
Q94  A  CGL_24Sep2024_Shift1        3-conclusion CUSTOM options
Q95  B  CGL_24Sep2024_Shift1        standard 2-conclusion

Reasoning notes
───────────────
Q90  Some Sh are Pa (I); All Pa→Ja (A); All Ja→Tr (A).
     I:  Darii (M=Pa): Some Sh are Ja → Darii (M=Ja): Some Sh are Tr → I-conv: Some Tr are Sh ✓
     II: All Ja→Sh (A-type) → can't derive A-type backward from I-chain ✗
     Only I follows.

Q91  Some Mo are Wa (I); No Wa is La (E).
     I:  No La is Mo (E-type) →
         Camestres needs All Mo→Wa (A); only Some Mo are Wa (I) available ✗
         Assume Some La are Mo: those laptop-mobiles need not be watches → no contradiction ✗
     II: Some La are not Wa (O-type) →
         E-conv: No La is Wa → subalternation: Some La are not Wa ✓
     Only II follows.

Q92  No G is M (E); Some A are M (I).
     I:  Some M are A → I-conv of "Some A are M" ✓
     II: Some M are G → E-conv of "No G is M" = "No M is G"; contradicted ✗
     Only I follows.

Q93  Some Tr are Fl (I); No Fl is Re (E).
     I:  All Tr are Re (A-type) → Ferio derives Some Tr are not Re (O), contradiction ✗
     II: All Re are Fl (A-type) → E-conv gives No Re is Fl, contradicts II ✗
     III:Some Tr are not Re (O-type) → Ferio: No Fl is Re + Some Tr are Fl → Some Tr are not Re ✓
     Only conclusion III follows.

Q94  All Sp→Fo (A); All Fo→Kn (A); No Kn is Spa (E).
     Barbara: All Sp→Fo + All Fo→Kn → All Sp→Kn.
     I:  Some Kn are Sp → All Sp→Kn → I-conv: Some Kn are Sp ✓
     II: No Fo is Spa → Celarent (M=Kn, S=Fo, P=Spa): All Fo→Kn + No Kn is Spa → No Fo is Spa ✓
     III:Some Sp are Spa → Celarent: All Sp→Kn + No Kn is Spa → No Sp is Spa; contradicts III ✗
     Only conclusions I and II follow.

Q95  Some Mi are De (I); No De is Pl (E); All Pl→Tr (A).
     I:  Some De are Tr → De disjoint from Pl (No De is Pl); Pl⊆Tr but De need not overlap Tr ✗
     II: Some Mi are not Pl → Ferio (M=De, S=Mi, P=Pl): No De is Pl + Some Mi are De
         → Some Mi are not Pl ✓
     Only II follows.
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

    # ── Q90 (CGL, 19 Sep 2024 Shift-3) ──────────────────────────────────────
    {
        "question_number": 90,
        "difficulty": "medium",
        "source_pdf": "CGL_19Sep2024_Shift3",
        "question_en": (
            "Read the given statements and conclusions carefully. Assuming the statements "
            "to be true even if they seem to be at variance with commonly known facts, "
            "decide which conclusion(s) logically follow(s).\n\n"
            "Statements:\n"
            "Some shirts are pants.\n"
            "All pants are jackets.\n"
            "All jackets are trousers.\n\n"
            "Conclusions:\n"
            "I.  Some trousers are shirts.\n"
            "II. All jackets are shirts."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों को ध्यानपूर्वक पढ़ें। कथनों को सत्य मानते हुए, "
            "भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत हों, तय करें कि कौन-सा/"
            "से निष्कर्ष तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ कमीजें पतलून हैं।\n"
            "सभी पतलून जैकेट हैं।\n"
            "सभी जैकेट ट्राउजर हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ ट्राउजर कमीजें हैं।\n"
            "II. सभी जैकेट कमीजें हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
    },

    # ── Q91 (GD Constable, 27 Feb 2024 Shift-3) ──────────────────────────────
    {
        "question_number": 91,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_27Feb2024_Shift3",
        "question_en": (
            "In the following question, some statements are given followed by some conclusions. "
            "Taking the given statements to be true even if they seem to be at variance from "
            "commonly known facts, decide which conclusion(s) logically follow(s).\n\n"
            "Statements:\n"
            "Some mobile is a watch.\n"
            "No watch is a laptop.\n\n"
            "Conclusions:\n"
            "I.  No laptop is mobile.\n"
            "II. Some laptops are not watches."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कुछ कथन और उसके बाद उन कथनों पर आधारित कुछ निष्कर्ष "
            "दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात "
            "तथ्यों से भिन्न प्रतीत होते हों, तय करें कि कौन-सा/से निष्कर्ष तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ मोबाइल घड़ी हैं।\n"
            "कोई घड़ी लैपटॉप नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  कोई लैपटॉप मोबाइल नहीं है।\n"
            "II. कुछ लैपटॉप घड़ी नहीं हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q92 (GD Constable, 27 Feb 2024 Shift-4) ──────────────────────────────
    {
        "question_number": 92,
        "difficulty": "easy",
        "source_pdf": "GD_Constable_27Feb2024_Shift4",
        "question_en": (
            "In the following question, some statements are given followed by some conclusions. "
            "Taking the given statements to be true even if they seem to be at variance from "
            "commonly known facts, decide which conclusion(s) logically follow(s).\n\n"
            "Statements:\n"
            "No G are M.\n"
            "Some A are M.\n\n"
            "Conclusions:\n"
            "I.  Some M are A.\n"
            "II. Some M are G."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कुछ कथन और उसके बाद उन कथनों पर आधारित कुछ निष्कर्ष "
            "दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात "
            "तथ्यों से भिन्न प्रतीत होते हों, तय करें कि कौन-सा/से निष्कर्ष तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कोई G, M नहीं हैं।\n"
            "कुछ A, M हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ M, A हैं।\n"
            "II. कुछ M, G हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
    },

    # ── Q93 (GD Constable, 30 Mar 2024 Shift-1) — 3-conclusion CUSTOM ────────
    # Ferio: No Fl is Re + Some Tr are Fl → Some Tr are not Re (III ✓).
    # I: A-type contradicted by O-type derivation. II: contradicts E-conv. III: ✓
    {
        "question_number": 93,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_30March2024_Shift1",
        "question_en": (
            "In the following question below are given some statements followed by some "
            "conclusions. Taking the given statements to be true even if they seem to be at "
            "variance from commonly known facts. Read all the conclusions and then decide "
            "which of the given conclusions logically follows the given statements.\n\n"
            "Statements:\n"
            "Some tree are flower.\n"
            "No flower is red.\n\n"
            "Conclusions:\n"
            "I.   All tree are red.\n"
            "II.  All red are flower.\n"
            "III. Some tree are not red."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कुछ कथन दिए गए हैं और उसके बाद उन कथनों पर "
            "आधारित कुछ निष्कर्ष दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, "
            "भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों। सभी निष्कर्षों "
            "को पढ़ें और फिर तय करें कि दिए गए निष्कर्षों में से कौन-सा दिए गए "
            "कथनों का तार्किक रूप से अनुसरण करता है।\n\n"
            "कथन:\n"
            "कुछ पेड़ फूल हैं।\n"
            "कोई फूल लाल नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.   सभी पेड़ लाल हैं।\n"
            "II.  सभी लाल फूल हैं।\n"
            "III. कुछ पेड़ लाल नहीं हैं।"
        ),
        # Custom options — answer is option 1 = "A"
        "option_a": "Only conclusion III follows. / केवल निष्कर्ष III अनुसरण करता है।",
        "option_b": "Both conclusions II and III follow. / दोनों निष्कर्ष II और III अनुसरण करते हैं।",
        "option_c": "Only conclusion II follows. / केवल निष्कर्ष II अनुसरण करता है।",
        "option_d": "All conclusions follow. / सभी निष्कर्ष अनुसरण करते हैं।",
        "correct_answer": "A",
    },

    # ── Q94 (CGL, 24 Sep 2024 Shift-1) — 3-conclusion CUSTOM ────────────────
    # Barbara: All Sp→Fo + All Fo→Kn → All Sp→Kn.
    # I: All Sp→Kn → I-conv ✓. II: Celarent ✓. III: contradicted by Celarent ✗.
    {
        "question_number": 94,
        "difficulty": "hard",
        "source_pdf": "CGL_24Sep2024_Shift1",
        "question_en": (
            "Three statements are given, followed by three conclusions numbered I, II and III. "
            "Assuming the statements to be true, even if they seem to be at variance with "
            "commonly known facts, decide which of the conclusions logically follow(s) from "
            "the statements.\n\n"
            "Statements:\n"
            "All spoons are forks.\n"
            "All forks are knives.\n"
            "No knife is a spatula.\n\n"
            "Conclusions:\n"
            "I.   Some knives are spoons.\n"
            "II.  No fork is a spatula.\n"
            "III. Some spoons are spatulas."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं, जिनके बाद I, II और III क्रमांकित तीन निष्कर्ष दिए गए "
            "हैं। कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, तय करें कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी चम्मच काँटे हैं।\n"
            "सभी काँटे चाकू हैं।\n"
            "कोई भी चाकू स्पेचुला नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.   कुछ चाकू चम्मच हैं।\n"
            "II.  कोई भी काँटा स्पेचुला नहीं है।\n"
            "III. कुछ चम्मच स्पेचुला हैं।"
        ),
        # Custom options — answer is option 1 = "A"
        "option_a": "Only conclusions I and II follow. / केवल निष्कर्ष I और II अनुसरण करते हैं।",
        "option_b": "Neither conclusion follows. / कोई भी निष्कर्ष अनुसरण नहीं करता।",
        "option_c": "Only conclusion III follows. / केवल निष्कर्ष III अनुसरण करता है।",
        "option_d": "Only conclusion I follows. / केवल निष्कर्ष I अनुसरण करता है।",
        "correct_answer": "A",
    },

    # ── Q95 (CGL, 24 Sep 2024 Shift-1) ──────────────────────────────────────
    # Some Mi are De (I); No De is Pl (E); All Pl→Tr (A).
    # I: Some De are Tr → De disjoint from Pl (No De is Pl); no chain to Tr ✗
    # II: Some Mi are not Pl → Ferio (M=De, S=Mi, P=Pl): No De is Pl + Some Mi are De
    #     → Some Mi are not Pl ✓
    # Only II follows.
    {
        "question_number": 95,
        "difficulty": "medium",
        "source_pdf": "CGL_24Sep2024_Shift1",
        "question_en": (
            "Read the given statements and conclusions carefully. Assuming that the information "
            "given in the statements is true, even if it appears to be at variance with commonly "
            "known facts, decide which of the given conclusions logically follow(s) from the "
            "statements.\n\n"
            "Statements:\n"
            "Some Mirrors are Decoratives.\n"
            "No Decorative is a Plant.\n"
            "All Plants are Trees.\n\n"
            "Conclusions:\n"
            "I.  Some Decoratives are Trees.\n"
            "II. Some Mirrors are not Plants."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों को ध्यानपूर्वक पढ़ें। यह मानते हुए कि कथनों में "
            "दी गई जानकारी सत्य है, भले ही वह सामान्य ज्ञात तथ्यों से भिन्न प्रतीत होती "
            "हो, यह तय करें कि दिए गए निष्कर्षों में से कौन-सा/से कथनों का तार्किक रूप "
            "से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ दर्पण सजावटी हैं।\n"
            "कोई भी सजावटी, पौधा नहीं है।\n"
            "सभी पौधे, पेड़ हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ सजावटी, पेड़ हैं।\n"
            "II. कुछ दर्पण, पौधे नहीं हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
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
