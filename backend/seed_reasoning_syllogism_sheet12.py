"""
seed_reasoning_syllogism_sheet12.py
=====================================
Seeds Reasoning → Syllogism  Q50–Q55 (Sheet 12).
Subject : Reasoning
Topic   : Syllogism

Q50 [CHSL 08 July 2024 Shift-1]  3-concl custom   → D (Both I and III)
Q51 [CHSL 04 July 2024 Shift-2]  standard 2-concl  → D (Neither)
Q52 [CHSL 08 July 2024 Shift-2]  standard 2-concl  → D (Neither)
Q53 [CHSL 04 July 2024 Shift-3]  standard 2-concl  → A (Only I)
Q54 [CHSL 08 July 2024 Shift-3]  standard 2-concl  → D (Neither)
Q55 [CHSL 08 July 2024 Shift-4]  standard 2-concl  → A (Only I)

Reasoning notes
───────────────
Q50  No Cu is Si (E); All Go→Cu (A); All Al→Go (A).
     Cu=copper, Si=silver, Go=gold, Al=aluminium.

     Barbara:   All Al→Go + All Go→Cu → All Al→Cu.

     Camestres (Fig 2): All P→M + No S is M → No S is P.
     For "No Go is Si":  P=Go, M=Cu, S=Si.
       All Go→Cu (✓) + No Si is Cu (E-conv of Stmt I: No Cu is Si → No Si is Cu) ✓
       → No Si is Go → E-conv: No Go is Si.
     For "No Al is Si":  P=Al, M=Cu, S=Si.
       All Al→Cu (Barbara, ✓) + No Si is Cu (✓) → No Si is Al → No Al is Si.

     I:   No Al is Si → Camestres chain above ✓
     II:  Some Go is Si → contradicts derived "No Go is Si" ✗
     III: All Al is Cu → Barbara ✓

     Both conclusions I and III follow.

Q51  All Sp→Wi (A); Some Wi are Ea (I); Some Fi are Ea (I).
     Sp=space, Wi=wind, Ea=earth, Fi=fire.

     I:   All Ea→Sp (All earth is space).
          All Sp→Wi says Sp ⊆ Wi. "Some Wi are Ea" means some wind entities are
          earth — but those earth entities need not be in the Sp subset of Wi.
          "All Ea→Sp" is NOT derivable. ✗

     II:  Some Wi are Fi (Some wind is fire).
          Some Wi are Ea (I) + Some Fi are Ea (I): Middle=Ea. I+I → no valid
          syllogistic conclusion (two particular premises). ✗

     Neither conclusion follows.

Q52  Some Ro are Fl (I); All Bu→Ro (A); All Li→Fl (A).
     Ro=roses, Fl=flowers, Bu=buds, Li=lilies.

     I:   Some Bu are Li (Some buds are lilies).
          No premise connects buds to lilies. The path Bu→Ro→?→Li requires a
          link from Ro to Li, but there is none given. ✗

     II:  Some Fl are Bu (Some flowers are buds).
          Attempt: All Bu→Ro + Some Ro are Fl.
          Middle=Ro: undistributed as predicate of A and as subject of I.
          Fallacy of undistributed middle → no valid conclusion. ✗

     Neither conclusion follows.

Q53  No Pi is Cu (E); All Cu→Sh (A); No Sh is Bl (E).
     Pi=pillow, Cu=cushion, Sh=sheet, Bl=blanket.

     I:   No Cu is Bl (No cushion is a blanket).
          Set argument: Cu ⊆ Sh (All Cu→Sh) and Sh ∩ Bl = ∅ (No Sh is Bl)
          → Cu ∩ Bl = ∅ → No Cu is Bl.
          Camestres (Fig 2): All Cu→Sh (All P→M) + No Bl is Sh (No S is M,
          E-conv of Stmt III) → No Bl is Cu → E-conv: No Cu is Bl ✓

     II:  Some Pi are Sh (Some pillows are sheets).
          No Pi is Cu (E): pillows and cushions are disjoint.
          All Cu→Sh (A): cushions are sheets.
          No premise links pillows directly to sheets; the cushions-in-sheets
          chain gives no information about non-cushion pillows. ✗

     Only conclusion I follows.

Q54  Some Ri are Hu (I); All St→Ri (A); Some Gr are Hu (I).
     Ri=rivers, Hu=huts, St=streams, Gr=grass.

     I:   All St→Hu (All streams are huts).
          Attempt: All St→Ri + Some Ri are Hu.
          Darii needs A-type major premise (All M→P); here Ri→Hu is only I-type.
          Cannot upgrade partial "Some Ri are Hu" to derive "All St→Hu." ✗

     II:  Some Gr are Ri (Some grass are rivers).
          Some Gr are Hu (I) + Some Ri are Hu (I): Middle=Hu. I+I → no valid
          syllogistic conclusion. ✗

     Neither conclusion follows.

Q55  All Sh→Ti (A); Some Ti are Pa (I); All Pa→Bu (A).
     Sh=shoes, Ti=ties, Pa=pants, Bu=buttons.

     Darii: Some Ti are Pa (I) + All Pa→Bu (A) → Some Ti are Bu.
            I-conv: Some Bu are Ti.

     I:   Some Bu are Ti (Some buttons are ties).
          Derived directly by Darii + I-conversion above ✓

     II:  No Ti are Bu (No tie is a button).
          Directly contradicted by derived "Some Ti are Bu." ✗

     Only conclusion I follows.
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

    # ── Q50 (CHSL, 08 July 2024 Shift-1) — 3-conclusion custom ──────────────
    # No Cu is Si (E); All Go→Cu (A); All Al→Go (A).
    # Barbara:  All Al→Go + All Go→Cu → All Al→Cu.
    # Camestres: All Go→Cu + No Si is Cu → No Si is Go → No Go is Si.
    # Camestres: All Al→Cu + No Si is Cu → No Si is Al → No Al is Si.
    #
    # I:   No Al is Si  → Camestres ✓
    # II:  Some Go is Si → contradicts "No Go is Si" ✗
    # III: All Al is Cu  → Barbara ✓
    #
    # Both I and III follow → option D.
    {
        "question_number": 50,
        "difficulty": "hard",
        "source_pdf": "CHSL_08July2024_Shift1",
        "question_en": (
            "Q:50 Directions: In this question, three statements are given, followed by "
            "conclusions numbered I, II and III. Assuming the statements to be true, "
            "even if they seem to be at variance with commonly known facts, decide "
            "which of the conclusion(s) logically follows/follow from the statements.\n\n"
            "Statements:\n"
            "No copper is silver.\n"
            "All gold is copper.\n"
            "All aluminium is gold.\n\n"
            "Conclusions:\n"
            "I.   No aluminium is silver.\n"
            "II.  Some gold is silver.\n"
            "III. All aluminium is copper."
        ),
        "question_hi": (
            "इस प्रश्न में तीन कथन दिए गए हैं, जिनके बाद I, II और III अंकित निष्कर्ष "
            "दिए गए हैं। कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों "
            "से भिन्न प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का "
            "तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कोई भी तांबा चांदी नहीं है।\n"
            "सभी सोना तांबा है।\n"
            "सभी एल्युमीनियम सोना है।\n\n"
            "निष्कर्ष:\n"
            "I.   कोई भी एल्युमीनियम चांदी नहीं है।\n"
            "II.  कुछ सोना चांदी है।\n"
            "III. सभी एल्युमीनियम तांबा है।"
        ),
        "option_a": "Both conclusions I and II follow. / दोनों निष्कर्ष I और II अनुसरण करते हैं।",
        "option_b": "Only conclusion II follows. / केवल निष्कर्ष II अनुसरण करता है।",
        "option_c": "Only conclusion I follows. / केवल निष्कर्ष I अनुसरण करता है।",
        "option_d": "Both conclusions I and III follow. / दोनों निष्कर्ष I और III अनुसरण करते हैं।",
        "correct_answer": "D",
    },

    # ── Q51 (CHSL, 04 July 2024 Shift-2) — standard 2-conclusion ─────────────
    # All Sp→Wi (A); Some Wi are Ea (I); Some Fi are Ea (I).
    # I:  All Ea→Sp → A-type reverse of All Sp→Wi; invalid ✗
    # II: Some Wi are Fi → I+I (middle Ea) → no valid conclusion ✗
    {
        "question_number": 51,
        "difficulty": "medium",
        "source_pdf": "CHSL_04July2024_Shift2",
        "question_en": (
            "Three statements are followed by conclusions numbered I, II. You have to "
            "consider these statements to be true, even if they seem to be at variance "
            "with commonly known facts. Decide which of the given conclusions logically "
            "follow/s from the given statement.\n\n"
            "Statements:\n"
            "All space is wind.\n"
            "Some wind is earth.\n"
            "Some fire is earth.\n\n"
            "Conclusion (I):  All earth is space.\n"
            "Conclusion (II): Some wind is fire."
        ),
        "question_hi": (
            "तीन कथनों के बाद I और II अंकित निष्कर्ष दिए गए हैं। आपको इन कथनों को "
            "सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते "
            "हों। निर्णय लीजिए कि दिए गए निष्कर्षों में से कौन-सा/से कथनों का "
            "तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी अंतरिक्ष, वायु हैं।\n"
            "कुछ वायु, पृथ्वी हैं।\n"
            "कुछ अग्नि, पृथ्वी हैं।\n\n"
            "निष्कर्ष (I):  सभी पृथ्वी, अंतरिक्ष हैं।\n"
            "निष्कर्ष (II): कुछ वायु, अग्नि हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q52 (CHSL, 08 July 2024 Shift-2) — standard 2-conclusion ─────────────
    # Some Ro are Fl (I); All Bu→Ro (A); All Li→Fl (A).
    # I:  Some Bu are Li → no premise links buds to lilies ✗
    # II: Some Fl are Bu → All Bu→Ro + Some Ro are Fl: Ro undistributed in
    #     both (A-predicate & I-subject) → fallacy of undistributed middle ✗
    {
        "question_number": 52,
        "difficulty": "medium",
        "source_pdf": "CHSL_08July2024_Shift2",
        "question_en": (
            "Three statements are followed by conclusions numbered I, II. You have to "
            "consider these statements to be true, even if they seem to be at variance "
            "with commonly known facts. Decide which of the given conclusions logically "
            "follow/s from the given statement.\n\n"
            "Statements:\n"
            "Some roses are flowers.\n"
            "All buds are roses.\n"
            "All lilies are flowers.\n\n"
            "Conclusion (I):  Some buds are lilies.\n"
            "Conclusion (II): Some flowers are buds."
        ),
        "question_hi": (
            "तीन कथनों के बाद I और II अंकित निष्कर्ष दिए गए हैं। आपको इन कथनों को "
            "सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते "
            "हों। निर्णय लीजिए कि दिए गए निष्कर्षों में से कौन-सा/से कथनों का "
            "तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ गुलाब फूल हैं।\n"
            "सभी कलियाँ गुलाब हैं।\n"
            "सभी लिली फूल हैं।\n\n"
            "निष्कर्ष (I):  कुछ कलियाँ लिली हैं।\n"
            "निष्कर्ष (II): कुछ फूल कलियाँ हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q53 (CHSL, 04 July 2024 Shift-3) — standard 2-conclusion ─────────────
    # No Pi is Cu (E); All Cu→Sh (A); No Sh is Bl (E).
    # I:  No Cu is Bl → Camestres: All Cu→Sh + No Bl is Sh → No Bl is Cu
    #     → E-conv: No Cu is Bl ✓
    # II: Some Pi are Sh → no premise links pillows to sheets ✗
    {
        "question_number": 53,
        "difficulty": "medium",
        "source_pdf": "CHSL_04July2024_Shift3",
        "question_en": (
            "Read the given statements and conclusions carefully. Assuming that the "
            "information given in the statements is true, even if it appears to be "
            "at variance with commonly known facts, decide which of the given "
            "conclusions logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "No pillow is a cushion.\n"
            "All cushions are sheets.\n"
            "No sheet is a blanket.\n\n"
            "Conclusions:\n"
            "(I)  No cushion is a blanket.\n"
            "(II) Some pillows are sheets."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों को ध्यानपूर्वक पढ़िए। यह मानते हुए कि "
            "कथनों में दी गई जानकारी सत्य है, भले ही वह सामान्यतः ज्ञात तथ्यों "
            "से भिन्न प्रतीत होती हो, निर्णय लीजिए कि दिए गए निष्कर्षों में से "
            "कौन-सा/से कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कोई भी तकिया कुशन नहीं है।\n"
            "सभी कुशन चादर हैं।\n"
            "कोई भी चादर कम्बल नहीं है।\n\n"
            "निष्कर्ष:\n"
            "(I)  कोई भी कुशन कम्बल नहीं है।\n"
            "(II) कुछ तकिए चादर हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
    },

    # ── Q54 (CHSL, 08 July 2024 Shift-3) — standard 2-conclusion ─────────────
    # Some Ri are Hu (I); All St→Ri (A); Some Gr are Hu (I).
    # Ri=rivers, Hu=huts, St=streams, Gr=grass.
    # I:  All St→Hu → Darii needs A-type major (All Ri→Hu); only I-type given ✗
    # II: Some Gr are Ri → I+I (middle Hu) → no valid conclusion ✗
    {
        "question_number": 54,
        "difficulty": "medium",
        "source_pdf": "CHSL_08July2024_Shift3",
        "question_en": (
            "Directions: Three statements are followed by conclusions numbered I, II. "
            "You have to consider these statements to be true, even if they seem to "
            "be at variance with commonly known facts. Decide which of the given "
            "conclusions logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "Some rivers are huts.\n"
            "All streams are rivers.\n"
            "Some grass are huts.\n\n"
            "Conclusions:\n"
            "(I)  All streams are huts.\n"
            "(II) Some grass are rivers."
        ),
        "question_hi": (
            "निर्देश: तीन कथनों के बाद I और II अंकित निष्कर्ष दिए गए हैं। आपको इन "
            "कथनों को सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों। निर्णय लीजिए कि दिए गए निष्कर्षों में से कौन-सा/से "
            "कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ नदियाँ घाट हैं।\n"
            "सभी धाराएँ नदियाँ हैं।\n"
            "कुछ घास घाट हैं।\n\n"
            "निष्कर्ष:\n"
            "(I)  सभी धाराएँ घाट हैं।\n"
            "(II) कुछ घास नदियाँ हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q55 (CHSL, 08 July 2024 Shift-4) — standard 2-conclusion ─────────────
    # All Sh→Ti (A); Some Ti are Pa (I); All Pa→Bu (A).
    # Sh=shoes, Ti=ties, Pa=pants, Bu=buttons.
    #
    # Darii: Some Ti are Pa (I) + All Pa→Bu (A) → Some Ti are Bu.
    #        I-conv: Some Bu are Ti.
    #
    # I:  Some Bu are Ti (Some buttons are ties)
    #     Derived directly by Darii + I-conversion ✓
    #
    # II: No Ti are Bu (No tie is a button)
    #     Directly contradicted by derived "Some Ti are Bu." ✗
    {
        "question_number": 55,
        "difficulty": "medium",
        "source_pdf": "CHSL_08July2024_Shift4",
        "question_en": (
            "Three statements are followed by conclusions numbered I, II. You have to "
            "consider these statements to be true, even if they seem to be at variance "
            "with commonly known facts. Decide which of the given conclusions logically "
            "follow/s from the given statement.\n\n"
            "Statements:\n"
            "All shoes are ties.\n"
            "Some ties are pants.\n"
            "All pants are buttons.\n\n"
            "Conclusion I:  Some buttons are ties.\n"
            "Conclusion II: No tie is a button."
        ),
        "question_hi": (
            "तीन कथनों के बाद I और II अंकित निष्कर्ष दिए गए हैं। आपको इन कथनों को "
            "सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते "
            "हों। निर्णय लीजिए कि दिए गए निष्कर्षों में से कौन-सा/से कथनों का "
            "तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी जूते टाई हैं।\n"
            "कुछ टाई पैंट हैं।\n"
            "सभी पैंट बटन हैं।\n\n"
            "निष्कर्ष I:  कुछ बटन टाई हैं।\n"
            "निष्कर्ष II: कोई टाई बटन नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
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
