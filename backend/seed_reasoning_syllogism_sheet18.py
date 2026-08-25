"""
seed_reasoning_syllogism_sheet18.py
=====================================
Seeds Reasoning → Syllogism  Q84–Q89 (Sheet 18).
Subject : Reasoning
Topic   : Syllogism

Q84 — standard 2-conclusion (CGL 18 Sep 2024 Shift-3)
Q85 — standard 2-conclusion (CGL 18 Sep 2024 Shift-3)
Q86 — standard 2-conclusion (CGL 19 Sep 2024 Shift-1)
Q87 — standard 2-conclusion (CGL 13 Sep 2024 Shift-2)
Q88 — standard 2-conclusion (CGL 13 Sep 2024 Shift-2)
Q89 — standard 2-conclusion (CGL 19 Sep 2024 Shift-2)

Answer key:
  Q84  D   Q85  B   Q86  C   Q87  D   Q88  D   Q89  D

Reasoning notes
───────────────
Q84  All Be→Sa (A); Some De are Sa (I); All Mo→Ro (A).
     I:  Some Be are De → middle Sa: predicate of A-type (undistrib.) AND predicate of I-type
         (undistrib.) → fallacy of undistributed middle ✗
     II: Some Sa are Ro → no premise connects Sa and Ro; All Mo→Ro has Mo→Ro,
         but no statement links Sa to Mo ✗
     Neither conclusion follows.

Q85  No Me is Ca (E); Some Ca are Ta (I); Some Ta are La (I).
     I:  Some Ca are La → I + I = no valid syllogistic conclusion ✗
     II: All tablets can never be medicines (impossibility) →
         Assume All Ta→Me:
         Darii (M=Ta, S=Ca, P=Me): All Ta→Me + Some Ca are Ta (I) → Some Ca are Me.
         But E-conv of No Me is Ca → No Ca is Me. Contradiction! → IMPOSSIBLE ✓
     Only conclusion II follows.

Q86  Some Ea are Sp (I); All Sp→Pa (A); No Pa is Pe (E).
     I:  Some Pa are Ea →
         Darii (M=Sp, S=Ea, P=Pa): All Sp→Pa + Some Ea are Sp → Some Ea are Pa → I-conv ✓
     II: No Pe is Sp →
         Celarent (M=Pa, S=Sp, P=Pe): No Pa is Pe (No M is P) + All Sp→Pa (All S→M)
         → No Sp is Pe → E-conv: No Pe is Sp ✓
     Both conclusions I and II follow.

Q87  Some To are Pl (I); Some Pl are Me (I); No Me is Ch (E).
     I:  Some Ch are Pl →
         Ferio (M=Me, S=Pl, P=Ch): No Me is Ch + Some Pl are Me → Some Pl are not Ch (O).
         Only O-type derived; I-type "Some Ch are Pl" does NOT follow ✗
     II: No toy can be a chemical (impossibility) →
         Assume Some To are Ch (even one toy is chemical). Those toys might not be plastic
         or metal → no contradiction with No Me is Ch. → NOT impossible ✗
         (Unlike Q85, Darii with Some To are Pl + Some Pl are Me gives I+I = no conclusion;
          no pathway creates a contradiction.)
     Neither conclusion follows.

Q88  All Fr→So (A); Some So are Ve (I); Some Ve are Gr (I).
     I:  All Ve→So (A-type) → I-conv of Some So are Ve gives Some Ve are So (I-type only);
         cannot derive A-type from I-type ✗
     II: Some So are Gr → middle Ve: Some So are Ve (I) + Some Ve are Gr (I) → I+I ✗
     Neither conclusion follows.

Q89  All Te→Da (A); All Da→En (A); Some En are Be (I).
     Barbara: All Te→Da + All Da→En → All Te→En.
     I:  All Te→Be (A-type) → All Te→En (A) + Some En are Be (I): middle En undistributed
         as predicate of A-type and subject of I-type → fallacy of undistributed middle ✗
     II: Some Da are Be → All Da→En (A, En as predicate, undistrib.) + Some En are Be (I,
         En as subject, undistrib.) → same fallacy; also need All En→Be for Darii ✗
     Neither conclusion follows.
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

    # ── Q84 (CGL, 18 Sep 2024 Shift-3) ──────────────────────────────────────
    # All Be→Sa (A); Some De are Sa (I); All Mo→Ro (A).
    # I:  Some Be are De → undistributed middle (Sa as predicate in both) ✗
    # II: Some Sa are Ro → no Sa-Mo or Sa-Ro connection ✗
    # Neither follows.
    {
        "question_number": 84,
        "difficulty": "medium",
        "source_pdf": "CGL_18Sep2024_Shift3",
        "question_en": (
            "Read the given statements and conclusions carefully. You have to take the given "
            "statements to be true even if they seem to be at variance from commonly known "
            "facts. You have to decide which conclusion/s logically follow/s from the given "
            "statements.\n\n"
            "Statements:\n"
            "All beaches are sand.\n"
            "Some deserts are sand.\n"
            "All mountains are rocky.\n\n"
            "Conclusions:\n"
            "I.  At least some beaches are desert.\n"
            "II. At least some sands are rocky."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों को ध्यान से पढ़ें। आपको दिए गए कथनों को सत्य "
            "मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों। "
            "आपको यह तय करना है कि दिए गए कथनों से कौन-सा/से निष्कर्ष तार्किक रूप "
            "से निकलता/निकलते है/हैं।\n\n"
            "कथन:\n"
            "सभी समुद्र तट रेत हैं।\n"
            "कुछ रेगिस्तान रेत हैं।\n"
            "सभी पहाड़ चट्टानी हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कम से कम कुछ समुद्र तट रेगिस्तान हैं।\n"
            "II. कम से कम कुछ रेत चट्टानी हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q85 (CGL, 18 Sep 2024 Shift-3) ──────────────────────────────────────
    # No Me is Ca (E); Some Ca are Ta (I); Some Ta are La (I).
    # I:  Some Ca are La → I+I = no valid conclusion ✗
    # II: All tablets can never be medicines →
    #     Assume All Ta→Me: Darii (Some Ca are Ta + All Ta→Me → Some Ca are Me).
    #     Contradicts No Ca is Me (E-conv of No Me is Ca) → IMPOSSIBLE ✓
    # Only conclusion II follows.
    {
        "question_number": 85,
        "difficulty": "hard",
        "source_pdf": "CGL_18Sep2024_Shift3",
        "question_en": (
            "In this question, three statements are given, followed by two conclusions "
            "numbered I and II. Assuming the statements to be true, even if they seem to "
            "be at variance with commonly known facts, decide which of the conclusion(s) "
            "logically follows/follow from the statements.\n\n"
            "Statements:\n"
            "No medicine is a capsule.\n"
            "Some capsules are tablets.\n"
            "Some tablets are laptops.\n\n"
            "Conclusions:\n"
            "I.  Some capsules are laptops.\n"
            "II. All tablets can never be medicines."
        ),
        "question_hi": (
            "इस प्रश्न में तीन कथन दिए गए हैं, जिनके बाद I और II से क्रमांकित दो निष्कर्ष "
            "दिए गए हैं। कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत होते हों, तय करें कि कौन-सा/से निष्कर्ष कथनों का तार्किक "
            "रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कोई दवा कैप्सूल नहीं है।\n"
            "कुछ कैप्सूल टेबलेट हैं।\n"
            "कुछ टेबलेट लैपटॉप हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ कैप्सूल लैपटॉप हैं।\n"
            "II. सभी टेबलेट, कभी भी दवाई नहीं हो सकती।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q86 (CGL, 19 Sep 2024 Shift-1) ──────────────────────────────────────
    # Some Ea are Sp (I); All Sp→Pa (A); No Pa is Pe (E).
    # I:  Some Pa are Ea →
    #     Darii (M=Sp, S=Ea, P=Pa): All Sp→Pa + Some Ea are Sp → Some Ea are Pa → I-conv ✓
    # II: No Pe is Sp →
    #     Celarent (M=Pa, S=Sp, P=Pe): No Pa is Pe + All Sp→Pa → No Sp is Pe → E-conv ✓
    # Both conclusions I and II follow.
    {
        "question_number": 86,
        "difficulty": "medium",
        "source_pdf": "CGL_19Sep2024_Shift1",
        "question_en": (
            "Read the given statements and conclusions carefully. You have to take the given "
            "statements to be true even if they seem to be at variance from commonly known "
            "facts. You have to decide which conclusion(s) logically follow(s) from the given "
            "statements.\n\n"
            "Statements:\n"
            "Some eagles are sparrows.\n"
            "All sparrows are parrots.\n"
            "No parrot is a penguin.\n\n"
            "Conclusions:\n"
            "I.  Some parrots are eagles.\n"
            "II. No penguin is a sparrow."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों का ध्यानपूर्वक अध्ययन करें। दिए गए कथनों को "
            "सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न प्रतीत होते हों। "
            "निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ चील गौरैया हैं।\n"
            "सभी गौरैया तोते हैं।\n"
            "कोई तोता पेंगुइन नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ तोते चील हैं।\n"
            "II. कोई पेंगुइन गौरैया नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
    },

    # ── Q87 (CGL, 13 Sep 2024 Shift-2) ──────────────────────────────────────
    # Some To are Pl (I); Some Pl are Me (I); No Me is Ch (E).
    # I:  Some Ch are Pl → Ferio only gives Some Pl are not Ch (O-type, not I-type) ✗
    # II: No toy can be a chemical (impossibility) →
    #     Assume Some To are Ch: the chemical toy might not be plastic or metal;
    #     no contradiction with No Me is Ch → NOT impossible ✗
    # Neither conclusion follows.
    {
        "question_number": 87,
        "difficulty": "hard",
        "source_pdf": "CGL_13Sep2024_Shift2",
        "question_en": (
            "Read the given statements and conclusions carefully. Assuming that the information "
            "given in the statements is true, even if it appears to be at variance with commonly "
            "known facts, decide which of the given conclusions logically follow/s from the "
            "statements.\n\n"
            "Statements:\n"
            "Some Toys are Plastic.\n"
            "Some Plastic are Metal.\n"
            "No Metal is Chemical.\n\n"
            "Conclusions:\n"
            "I.  Some Chemicals are Plastic.\n"
            "II. No Toy is a Chemical."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों का ध्यानपूर्वक अध्ययन करें। यह मानते हुए कि "
            "कथनों में दी गई जानकारी सत्य है, भले ही वह सामान्य ज्ञात तथ्यों से भिन्न "
            "प्रतीत होती हो, यह तय करें कि कौन-सा/से निष्कर्ष कथनों का तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ खिलौने प्लास्टिक हैं।\n"
            "कुछ प्लास्टिक धातु हैं।\n"
            "कोई धातु रसायन नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ रसायन प्लास्टिक हैं।\n"
            "II. कोई खिलौना रसायन नहीं हो सकता।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q88 (CGL, 13 Sep 2024 Shift-2) ──────────────────────────────────────
    # All Fr→So (A); Some So are Ve (I); Some Ve are Gr (I).
    # I:  All Ve→So (A-type) → I-conv of Some So are Ve gives only I-type; A-type unreachable ✗
    # II: Some So are Gr → middle Ve: Some So are Ve (I) + Some Ve are Gr (I) → I+I ✗
    # Neither conclusion follows.
    {
        "question_number": 88,
        "difficulty": "medium",
        "source_pdf": "CGL_13Sep2024_Shift2",
        "question_en": (
            "Read the given statements and conclusions carefully. Assuming that the information "
            "given in the statements is true, even if it appears to be at variance from commonly "
            "known facts, decide which of the given conclusions logically follow/s from the "
            "statements.\n\n"
            "Statements:\n"
            "All fruit are sour.\n"
            "Some sour are vegetables.\n"
            "Some vegetables are green.\n\n"
            "Conclusions:\n"
            "I.  All vegetables are sour.\n"
            "II. Some sour are green."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों का ध्यानपूर्वक अध्ययन करें। यह मानते हुए कि "
            "कथनों में दी गई जानकारी सत्य है, भले ही वह सामान्य ज्ञात तथ्यों से भिन्न "
            "प्रतीत होती हो, यह तय करें कि दिए गए निष्कर्षों में से कौन-सा/से कथनों का "
            "तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी फल खट्टे हैं।\n"
            "कुछ खट्टी सब्जियाँ हैं।\n"
            "कुछ सब्जियाँ हरी हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  सभी सब्जियाँ खट्टी हैं।\n"
            "II. कुछ खट्टे हरे हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q89 (CGL, 19 Sep 2024 Shift-2) ──────────────────────────────────────
    # All Te→Da (A); All Da→En (A); Some En are Be (I).
    # Barbara: All Te→Da + All Da→En → All Te→En.
    # I:  All Te→Be (A-type) → All Te→En (A) + Some En are Be (I):
    #     middle En undistributed in both (predicate of A, subject of I) → fallacy ✗
    # II: Some Da are Be → All Da→En (A, En undistrib.) + Some En are Be (I, En subject):
    #     same undistributed middle; no All En→Be (A) available for Darii ✗
    # Neither conclusion follows.
    {
        "question_number": 89,
        "difficulty": "medium",
        "source_pdf": "CGL_19Sep2024_Shift2",
        "question_en": (
            "In this question, three statements are given, followed by two conclusions "
            "numbered I and II. Assuming the statements to be true, even if they seem to "
            "be at variance with commonly known facts, decide which of the conclusion(s) "
            "logically follows/follow from the statements.\n\n"
            "Statements:\n"
            "All the teachers are dancers.\n"
            "All dancers are engineers.\n"
            "Some engineers are beautiful.\n\n"
            "Conclusions:\n"
            "I.  All teachers are beautiful.\n"
            "II. Some dancers are beautiful."
        ),
        "question_hi": (
            "इस प्रश्न में तीन कथन दिए गए हैं, जिनके बाद I और II से क्रमांकित दो निष्कर्ष "
            "दिए गए हैं। कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष कथनों का "
            "तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी शिक्षक नर्तक हैं।\n"
            "सभी नर्तक इंजीनियर हैं।\n"
            "कुछ इंजीनियर सुंदर हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  सभी शिक्षक सुंदर हैं।\n"
            "II. कुछ नर्तक सुंदर हैं।"
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
