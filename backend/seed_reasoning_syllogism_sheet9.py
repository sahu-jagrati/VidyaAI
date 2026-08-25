"""
seed_reasoning_syllogism_sheet9.py
====================================
Seeds Reasoning → Syllogism  Q31–Q36 (Sheet 9).
Subject : Reasoning
Topic   : Syllogism

Q31 — 3-conclusion custom 4-opt (GD Constable 21 Feb 2024 Shift-3)
Q32 — standard 2-conclusion 4-opt (GD Constable 22 Feb 2024 Shift-2)
Q33 — standard 2-conclusion 4-opt (GD Constable 22 Feb 2024 Shift-1)
Q34 — 3-conclusion custom 4-opt (GD Constable 22 Feb 2024 Shift-3)
Q35 — standard 2-conclusion 4-opt (CGL 10 Sep 2024 Shift-2)
Q36 — 3-conclusion custom 4-opt (CGL 10 Sep 2024 Shift-2)

Answer key:
  Q31  A   Q32  A   Q33  B   Q34  D   Q35  C   Q36  D

Reasoning notes
───────────────
Q31  All W→C (A); Some P are W (I).
     W=W, C=C, P=P (abstract variables).

     I:   Some C are P
          Darii: Some P are W (I) + All W→C (A) → Some P are C.
          I-conversion: Some C are P ✓
     II:  No P is C
          Directly contradicted by derived "Some P are C". ✗
     III: Some C are W
          All W→C → Subalternation: Some W are C → I-conv: Some C are W ✓
     Both I and III follow.

Q32  All bicycles→wheels (A); Some bicycles are vehicles (I);
     Some vehicles are not tyres (O).
     Bi=bicycles, Wh=wheels, Ve=vehicles, Ty=tyres.

     Derived: Some Ve are Bi (I-conv of Stmt II) + All Bi→Wh (A)
              → Darii → Some Ve are Wh → I-conv: Some Wh are Ve.

     I:   Some wheels are vehicles (Some Wh are Ve) ✓ (derived above)
     II:  Some wheels are not vehicles (Some Wh are not Ve)
          Cannot be formally derived — no premise guarantees a wheel is
          definitely a non-vehicle. Stmt III relates vehicles to tyres only. ✗
     Only conclusion I follows.

Q33  All lands→vacant (A); No land is a girl (E).
     L=lands, V=vacant, G=girls.

     I:   All vacant are lands (All V→L)
          "All L is V" (A-type) converts only to I-type via subalternation:
          All L→V → Some L are V → I-conv: Some V are L.
          "All V are L" (A-type) does NOT follow. ✗
          (Classic trap: "All A is B" ≠ "All B is A".)
     II:  No girl is a land (No G is L)
          E-conversion of Stmt II: No L is G → No G is L ✓
     Only conclusion II follows.

Q34  Some tables are white (I); No road is white (E).
     T=tables, W=white, Rd=roads.

     I:   No white is a road (No W is Rd)
          E-conversion of Stmt II: No Rd is W → No W is Rd ✓
     II:  No road is a table (No Rd is T)
          Non-white tables could be roads — nothing in the premises rules
          this out. "Some T are W" is only partial (SOME, not all). ✗
     III: No road is white (No Rd is W)
          Direct restatement of Stmt II ✓
     Both I and III follow.

Q35  Some bags are purses (I); All purses→wallets (A); All wallets→sacks (A).
     Ba=bags, Pu=purses, Wa=wallets, Sa=sacks.

     Barbara: All Pu→Wa + All Wa→Sa → All Pu→Sa.
     Darii:   Some Ba are Pu (I) + All Pu→Wa (A) → Some Ba are Wa.
              I-conv: Some Wa are Ba.

     I:   All purses are sacks (All Pu→Sa) → Barbara ✓
     II:  Some wallets are bags (Some Wa are Ba) → Darii + I-conv ✓
     Both I and II follow.

Q36  No bench is a chair (E); All sofas→benches (A); All tables→sofas (A).
     Be=benches, Ch=chairs, So=sofas, Ta=tables.

     Barbara:  All Ta→So + All So→Be → All Ta→Be.
     Celarent: All So→Be + No Be is Ch → No So is Ch.
     Celarent: All Ta→Be + No Be is Ch → No Ta is Ch.

     I:   No table is a chair (No Ta is Ch) → Celarent ✓
     II:  Some sofas are chairs (Some So are Ch)
          Contradicted by derived "No So is Ch". ✗
     III: All tables are benches (All Ta→Be) → Barbara ✓
     Both I and III follow.
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

    # ── Q31 (GD Constable, 21 Feb 2024 Shift-3) — 3-conclusion custom ─────────
    # All W→C (A); Some P are W (I).
    # I: Some C are P  → Darii → Some P are C → I-conv: Some C are P ✓
    # II: No P is C    → contradicts derived Some P are C ✗
    # III: Some C are W → I-conv of subaltern of All W→C ✓
    # Both I and III follow → option A.
    {
        "question_number": 31,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_21Feb2024_Shift3",
        "question_en": (
            "In the following question below are given some statements followed by "
            "some conclusions based on those statements. Taking the given statements "
            "to be true even if they seem to be at variance from commonly known facts. "
            "Read all the conclusions and then decide which of the given conclusion(s) "
            "logically follows the given statements.\n\n"
            "Statements:\n"
            "I.  All W are C.\n"
            "II. Some P are W.\n\n"
            "Conclusions:\n"
            "I.   Some C are P.\n"
            "II.  No P is C.\n"
            "III. Some C are W."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कुछ कथन और उनके बाद उन कथनों पर आधारित कुछ "
            "निष्कर्ष दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, सभी निष्कर्षों को "
            "पढ़िए और तय कीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "I.  सभी W, C हैं।\n"
            "II. कुछ P, W हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कुछ C, P हैं।\n"
            "II.  कोई P, C नहीं है।\n"
            "III. कुछ C, W हैं।"
        ),
        "option_a": "Both conclusions I and III follow. / दोनों निष्कर्ष I और III अनुसरण करते हैं।",
        "option_b": "Both conclusions I and II follow. / दोनों निष्कर्ष I और II अनुसरण करते हैं।",
        "option_c": "All conclusions I, II and III follow. / सभी निष्कर्ष I, II और III अनुसरण करते हैं।",
        "option_d": "Only conclusion II follows. / केवल निष्कर्ष II अनुसरण करता है।",
        "correct_answer": "A",
    },

    # ── Q32 (GD Constable, 22 Feb 2024 Shift-2) — standard 2-conclusion ──────
    # All Bi→Wh; Some Bi are Ve; Some Ve are not Ty.
    # I:  Some Wh are Ve  → I-conv of Some Ve are Bi + All Bi→Wh (Darii) ✓
    # II: Some Wh not Ve  → no formal derivation; Stmt III unrelated to wheels ✗
    {
        "question_number": 32,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_22Feb2024_Shift2",
        "question_en": (
            "Three Statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s) from the statements.\n\n"
            "Statement I:   All bicycles are wheels.\n"
            "Statement II:  Some bicycles are vehicles.\n"
            "Statement III: Some vehicles are not tyres.\n\n"
            "Conclusion I:  Some wheels are vehicles.\n"
            "Conclusion II: Some wheels are not vehicles."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष अनुसरण करता/करते हैं।\n\n"
            "कथन I:   सभी साइकिलें पहिये हैं।\n"
            "कथन II:  कुछ साइकिलें वाहन हैं।\n"
            "कथन III: कुछ वाहन टायर नहीं हैं।\n\n"
            "निष्कर्ष I:  कुछ पहिये वाहन हैं।\n"
            "निष्कर्ष II: कुछ पहिये वाहन नहीं हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
    },

    # ── Q33 (GD Constable, 22 Feb 2024 Shift-1) — standard 2-conclusion ──────
    # All lands→vacant (A); No land is a girl (E).
    # I:  All vacant are lands → A converts only to I-type (not A-type). ✗
    # II: No girl is a land    → E-conversion of Stmt II ✓
    {
        "question_number": 33,
        "difficulty": "easy",
        "source_pdf": "GD_Constable_22Feb2024_Shift1",
        "question_en": (
            "In the following question below are given some statements followed by "
            "some conclusions based on those statements. Taking the given statements "
            "to be true even if they seem to be at variance from commonly known facts. "
            "Read all the conclusions and then decide which of the given conclusion(s) "
            "logically follows the given statements.\n\n"
            "Statements:\n"
            "I.  All lands are vacant.\n"
            "II. No land is a girl.\n\n"
            "Conclusions:\n"
            "I.  All vacant are lands.\n"
            "II. No girl is a land."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कुछ कथन और उनके बाद उन कथनों पर आधारित कुछ "
            "निष्कर्ष दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, सभी निष्कर्षों को "
            "पढ़िए और तय कीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "I.  सभी भूमि रिक्त हैं।\n"
            "II. कोई भूमि लड़की नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  सभी रिक्त, भूमि हैं।\n"
            "II. कोई लड़की, भूमि नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q34 (GD Constable, 22 Feb 2024 Shift-3) — 3-conclusion custom ─────────
    # Some tables are white (I); No road is white (E).
    # T=tables, W=white, Rd=roads.
    # I:   No white is a road → E-conv of Stmt II ✓
    # II:  No road is a table → non-white tables could be roads; not provable ✗
    # III: No road is white   → restatement of Stmt II ✓
    # Both I and III follow → option D.
    {
        "question_number": 34,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_22Feb2024_Shift3",
        "question_en": (
            "In the following question below are given some statements followed by "
            "some conclusions based on those statements. Taking the given statements "
            "to be true even if they seem to be at variance from commonly known facts. "
            "Read all the conclusions and then decide which of the given conclusion(s) "
            "logically follows the given statements.\n\n"
            "Statements:\n"
            "I.  Some tables are white.\n"
            "II. No road is white.\n\n"
            "Conclusions:\n"
            "I.   No white is a road.\n"
            "II.  No road is a table.\n"
            "III. No road is white."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कुछ कथन और उनके बाद उन कथनों पर आधारित कुछ "
            "निष्कर्ष दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, सभी निष्कर्षों को "
            "पढ़िए और तय कीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "I.  कुछ टेबल सफेद हैं।\n"
            "II. कोई सड़क सफेद नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.   कोई सफेद सड़क नहीं है।\n"
            "II.  कोई सड़क टेबल नहीं है।\n"
            "III. कोई सड़क सफेद नहीं है।"
        ),
        "option_a": "All conclusions follow. / सभी निष्कर्ष अनुसरण करते हैं।",
        "option_b": "Both conclusions II and III follow. / दोनों निष्कर्ष II और III अनुसरण करते हैं।",
        "option_c": "Both conclusions I and II follow. / दोनों निष्कर्ष I और II अनुसरण करते हैं।",
        "option_d": "Both conclusions I and III follow. / दोनों निष्कर्ष I और III अनुसरण करते हैं।",
        "correct_answer": "D",
    },

    # ── Q35 (CGL, 10 Sep 2024 Shift-2) — standard 2-conclusion ──────────────
    # Some bags→purses (I); All purses→wallets (A); All wallets→sacks (A).
    # I:  All purses are sacks → Barbara (All Pu→Wa + All Wa→Sa → All Pu→Sa) ✓
    # II: Some wallets are bags → Darii (Some Ba are Pu + All Pu→Wa → Some Ba are Wa)
    #     + I-conv → Some Wa are Ba ✓
    {
        "question_number": 35,
        "difficulty": "medium",
        "source_pdf": "CGL_10Sep2024_Shift2",
        "question_en": (
            "Read the given statements and conclusions carefully. Assuming that the "
            "information given in the statements is true, even if it appears to be "
            "at variance with commonly known facts, decide which of the given "
            "conclusions logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "Some bags are purses.\n"
            "All purses are wallets.\n"
            "All wallets are sacks.\n\n"
            "Conclusions:\n"
            "(I)  All purses are sacks.\n"
            "(II) Some wallets are bags."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों को ध्यानपूर्वक पढ़िए। यह मानते हुए कि "
            "कथनों में दी गई जानकारी सत्य है, भले ही वह सामान्यतः ज्ञात तथ्यों "
            "से भिन्न प्रतीत होती हो, निर्णय लीजिए कि कौन-सा/से निष्कर्ष "
            "कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ थैले पर्स हैं।\n"
            "सभी पर्स वॉलेट हैं।\n"
            "सभी वॉलेट बोरे हैं।\n\n"
            "निष्कर्ष:\n"
            "(I)  सभी पर्स बोरे हैं।\n"
            "(II) कुछ वॉलेट थैले हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
    },

    # ── Q36 (CGL, 10 Sep 2024 Shift-2) — 3-conclusion custom ─────────────────
    # No bench is chair (E); All sofas→benches (A); All tables→sofas (A).
    # Be=benches, Ch=chairs, So=sofas, Ta=tables.
    #
    # Barbara:  All Ta→So + All So→Be → All Ta→Be.
    # Celarent: All So→Be + No Be is Ch → No So is Ch.
    # Celarent: All Ta→Be + No Be is Ch → No Ta is Ch.
    #
    # I:   No table is a chair   → Celarent (double chain) ✓
    # II:  Some sofas are chairs → contradicts derived "No So is Ch" ✗
    # III: All tables are benches → Barbara ✓
    # Both I and III follow → option D.
    {
        "question_number": 36,
        "difficulty": "hard",
        "source_pdf": "CGL_10Sep2024_Shift2",
        "question_en": (
            "Three statements are given, followed by three conclusions numbered I, II, "
            "and III. Assuming the statements to be true, even if they seem to be at "
            "variance with commonly known facts, decide which of the conclusions "
            "logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "No bench is a chair.\n"
            "All sofas are benches.\n"
            "All tables are sofas.\n\n"
            "Conclusions:\n"
            "I.   No table is a chair.\n"
            "II.  Some sofas are chairs.\n"
            "III. All tables are benches."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं, जिनके बाद I, II और III अंकित तीन निष्कर्ष दिए गए "
            "हैं। कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कोई बेंच कुर्सी नहीं है।\n"
            "सभी सोफे बेंच हैं।\n"
            "सभी टेबल सोफे हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कोई टेबल कुर्सी नहीं है।\n"
            "II.  कुछ सोफे कुर्सी हैं।\n"
            "III. सभी टेबल बेंच हैं।"
        ),
        "option_a": "Only conclusion I follows. / केवल निष्कर्ष I अनुसरण करता है।",
        "option_b": "Both conclusions I and II follow. / दोनों निष्कर्ष I और II अनुसरण करते हैं।",
        "option_c": "Only conclusion II follows. / केवल निष्कर्ष II अनुसरण करता है।",
        "option_d": "Both conclusions I and III follow. / दोनों निष्कर्ष I और III अनुसरण करते हैं।",
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
