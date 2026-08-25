"""
seed_reasoning_syllogism_sheet11.py
=====================================
Seeds Reasoning → Syllogism  Q43–Q49 (Sheet 11).
Subject : Reasoning
Topic   : Syllogism

Q43 [GD Constable 26 Feb 2024 Shift-4]  standard 2-concl → D (Neither)
Q44 [GD Constable 26 Feb 2024 Shift-3]  standard 2-concl → D (Neither)
Q45 [CHSL 03 July 2024 Shift-2]         3-concl custom   → A (Both II & III)
Q46 [GD Constable 26 Feb 2024 Shift-2]  3-concl custom   → D (Only III)
Q47 [CHSL 03 July 2024 Shift-3]         3-concl custom   → A (Both I & II)
Q48 [CHSL 03 July 2024 Shift-4]         3-concl custom   → C (Both I & II)
Q49 [CHSL 04 July 2024 Shift-1]         standard 2-concl → A (Only I, possibility)

Reasoning notes
───────────────
Q43  All Re→Am (A); Some Am are Fr (I); Some Fr are Tu (I).

     I:   Some Am are not Re (O-type).
          All Re→Am says Re ⊆ Am. It does NOT imply "Some Am ⊄ Re."
          Indian-exam rule: "All A is B" never yields "Some B are not A." ✗

     II:  Some Tu are Am (I-type).
          Attempt: Some Am are Fr (I) + Some Fr are Tu (I) — I+I = two
          particular premises → no valid syllogistic conclusion. ✗

     Neither conclusion follows.

Q44  No La is W (E); No W is A (E); No A is F (E).
     La=land, W=water, A=air, F=forest.

     I:   No La is F.
          All three premises are E-type. Two (or more) consecutive negative
          premises → no valid syllogistic conclusion. ✗

     II:  Some A is W (Some air is water).
          E-conv of Stmt II: No W is A → No A is W.
          Conclusion II ("Some A is W") directly contradicts "No A is W." ✗

     Neither conclusion follows.

Q45  No P is Sc (E); All Sc→Er (A); All P→Ca (A).
     P=pen, Sc=scale, Er=eraser, Ca=calculator.

     E-conv of Stmt I: No Sc is P.

     I:   Some Er are Ca.
          Er comes from scales (All Sc→Er). Ca comes from pens (All P→Ca).
          Pens and scales are disjoint (Stmt I). No premise links Er to Ca. ✗

     II:  No P is Er (No pen is an eraser).
          Celarent (Fig 1): All M→P + No S is M → No S is P.
          M=Sc, P=Er, S=P(pen):
          All Sc→Er (✓) + No P is Sc (✓ from Stmt I) → No P is Er ✓

     III: No Sc is Ca (No scale is a calculator).
          Celarent (Fig 1): M=P(pen), P=Ca, S=Sc:
          All P→Ca (✓) + No Sc is P (✓ from E-conv Stmt I) → No Sc is Ca ✓

     Both conclusions II and III follow.

Q46  No La is Cu (E); Some Sp are La (I).
     La=land, Cu=cup, Sp=spoon.

     E-conv of Stmt I: No Cu is La.

     I:   All Cu are La (All Cu→La).
          "No Cu is La" directly contradicts "All Cu→La." ✗

     II:  All Cu are Sp (All Cu→Sp).
          No premise links cups to spoons. ✗

     III: Some La are Sp (Some La are Sp).
          I-conv of Stmt II: Some Sp are La → Some La are Sp ✓

     Only conclusion III follows.

Q47  All Ch→So (A); Some Ch are Be (I); No So is Ta (E).
     Ch=chairs, So=sofas, Be=beds, Ta=tables.

     Derived:
     — Darii:    Some Be are Ch (I-conv Stmt II) + All Ch→So → Some Be are So
                 → I-conv: Some So are Be.
     — E-conv(3): No So is Ta → No Ta is So.
     — Camestres (Fig 2): All P→M + No S is M → No S is P.
       P=Ch, M=So, S=Ta:
       All Ch→So (✓) + No Ta is So (✓) → No Ta is Ch.

     I:   Some So are Be (Some sofas are beds).
          Derived by Darii + I-conv above ✓

     II:  No Ta is Ch (No table is a chair).
          Derived by Camestres above ✓

     III: Some Ta are Be (Some tables are beds).
          Tables are neither sofas nor chairs (derived above). No premise
          links tables to beds. ✗

     Both conclusions I and II follow.

Q48  Some Ca are On (I); All On→Po (A); All Po→Ra (A).
     Ca=carrots, On=onions, Po=potatoes, Ra=radish.

     Barbara:     All On→Po + All Po→Ra → All On→Ra.
     Darii (1st): Some Ca are On + All On→Po → Some Ca are Po.
     Darii (2nd): Some Ca are Po + All Po→Ra → Some Ca are Ra.

     I:   Some Ca are Ra (Some carrots are radish).
          Double-Darii chain above ✓

     II:  All On→Ra (All onions are radish).
          Barbara chain above ✓

     III: No Ca is Po (No carrot is a potato).
          Contradicts derived "Some Ca are Po." ✗

     Both conclusions I and II follow.

Q49  All Ri→Ba (A); Some Ba are An (I); No An is Pe (E).
     Ri=rings, Ba=bangles, An=anklets, Pe=pendants.

     This is a POSSIBILITY-TYPE question.
     Derived: Ferio: Some Ba are An + No An is Pe → Some Ba are not Pe (O).

     I:   All rings being anklets is a possibility.
          Check: All Ri→An would require all rings (which are bangles by Stmt I)
          to also be anklets. Since some bangles ARE anklets (Stmt II), it is
          possible that the ring-bangles all fall in the anklet-bangle subset.
          No contradictions arise. ✓ (possibility holds)

     II:  All bangles can never be pendants.
          This claims: No Ba is Pe (necessarily).
          We only derived Some Ba are not Pe (O-type, from Ferio).
          Non-anklet bangles could still be pendants — nothing in the premises
          prevents it. "All bangles CAN NEVER be pendants" requires No Ba is Pe
          which is NOT derivable. ✗

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

    # ── Q43 (GD Constable, 26 Feb 2024 Shift-4) — standard 2-conclusion ──────
    # All Re→Am (A); Some Am are Fr (I); Some Fr are Tu (I).
    # I:  Some Am are not Re → A-type doesn't imply O-type of its converse ✗
    # II: Some Tu are Am     → I+I = no valid conclusion ✗
    {
        "question_number": 43,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_26Feb2024_Shift4",
        "question_en": (
            "Three Statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s) from the statements.\n\n"
            "Statement I:   All reptiles are amphibians.\n"
            "Statement II:  Some amphibians are frogs.\n"
            "Statement III: Some frogs are turtles.\n\n"
            "Conclusion I:  Some amphibians are not reptiles.\n"
            "Conclusion II: Some turtles are amphibians."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन I:   सभी सरीसृप उभयचर हैं।\n"
            "कथन II:  कुछ उभयचर मेंढक हैं।\n"
            "कथन III: कुछ मेंढक कछुए हैं।\n\n"
            "निष्कर्ष I:  कुछ उभयचर सरीसृप नहीं हैं।\n"
            "निष्कर्ष II: कुछ कछुए उभयचर हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q44 (GD Constable, 26 Feb 2024 Shift-3) — standard 2-conclusion ──────
    # No La is W (E); No W is A (E); No A is F (E).
    # I:  No La is F → E+E chain → no valid conclusion ✗
    # II: Some A is W → directly contradicts E-conv of Stmt II (No A is W) ✗
    {
        "question_number": 44,
        "difficulty": "medium",
        "source_pdf": "GD_Constable_26Feb2024_Shift3",
        "question_en": (
            "Three Statements are given followed by two conclusions numbered I and II. "
            "Assuming the statements to be true, even if they seem to be at variance "
            "with commonly known facts, decide which of the conclusions logically "
            "follow(s) from the statements.\n\n"
            "Statement I:   No land is water.\n"
            "Statement II:  No water is air.\n"
            "Statement III: No air is forest.\n\n"
            "Conclusion I:  No land is forest.\n"
            "Conclusion II: Some air is water."
        ),
        "question_hi": (
            "तीन कथन दिए गए हैं जिनके बाद I और II अंकित दो निष्कर्ष दिए गए हैं। "
            "कथनों को सत्य मानते हुए, भले ही वे सामान्यतः ज्ञात तथ्यों से भिन्न "
            "प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से "
            "अनुसरण करता/करते हैं।\n\n"
            "कथन I:   कोई भूमि जल नहीं है।\n"
            "कथन II:  कोई जल वायु नहीं है।\n"
            "कथन III: कोई वायु वन नहीं है।\n\n"
            "निष्कर्ष I:  कोई भूमि वन नहीं है।\n"
            "निष्कर्ष II: कुछ वायु जल है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
    },

    # ── Q45 (CHSL, 03 July 2024 Shift-2) — 3-conclusion custom ──────────────
    # No P is Sc (E); All Sc→Er (A); All P→Ca (A).
    # P=pen, Sc=scale, Er=eraser, Ca=calculator.
    # E-conv(Stmt I): No Sc is P.
    #
    # I:   Some Er are Ca → no premise links eraser to calculator ✗
    # II:  No P is Er    → Celarent(Sc,Er,P): All Sc→Er + No P is Sc → No P is Er ✓
    # III: No Sc is Ca   → Celarent(P,Ca,Sc): All P→Ca + No Sc is P → No Sc is Ca ✓
    #
    # Both II and III follow → option A.
    {
        "question_number": 45,
        "difficulty": "hard",
        "source_pdf": "CHSL_03July2024_Shift2",
        "question_en": (
            "In this question, three statements are given, followed by three conclusions "
            "numbered I, II and III. Assuming the statements to be true, even if they "
            "seem to be at variance with commonly known facts, decide which of the "
            "conclusion(s) logically follow/follows from the statements.\n\n"
            "Statements:\n"
            "No pen is a scale.\n"
            "All scales are erasers.\n"
            "All pens are calculators.\n\n"
            "Conclusions:\n"
            "I.   Some erasers are calculators.\n"
            "II.  No pen is an eraser.\n"
            "III. No scale is a calculator."
        ),
        "question_hi": (
            "इस प्रश्न में तीन कथन दिए गए हैं, जिनके बाद I, II और III अंकित तीन "
            "निष्कर्ष दिए गए हैं। कथनों को सत्य मानते हुए, भले ही वे सामान्यतः "
            "ज्ञात तथ्यों से भिन्न प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से "
            "निष्कर्ष कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कोई भी पेन स्केल नहीं है।\n"
            "सभी स्केल इरेज़र हैं।\n"
            "सभी पेन कैलकुलेटर हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कुछ इरेज़र कैलकुलेटर हैं।\n"
            "II.  कोई भी पेन इरेज़र नहीं है।\n"
            "III. कोई भी स्केल कैलकुलेटर नहीं है।"
        ),
        "option_a": "Both conclusions II and III follow. / दोनों निष्कर्ष II और III अनुसरण करते हैं।",
        "option_b": "Neither conclusion I nor II follows. / न तो निष्कर्ष I और न ही II अनुसरण करता है।",
        "option_c": "All conclusions I, II and III follow. / सभी निष्कर्ष I, II और III अनुसरण करते हैं।",
        "option_d": "Both conclusions I and II follow. / दोनों निष्कर्ष I और II अनुसरण करते हैं।",
        "correct_answer": "A",
    },

    # ── Q46 (GD Constable, 26 Feb 2024 Shift-2) — 3-conclusion custom ────────
    # No La is Cu (E); Some Sp are La (I).
    # La=land, Cu=cup, Sp=spoon.
    # E-conv(Stmt I): No Cu is La.
    #
    # I:   All Cu are La → contradicts "No Cu is La" ✗
    # II:  All Cu are Sp → no premise links cups to spoons ✗
    # III: Some La are Sp → I-conv of Stmt II (Some Sp are La → Some La are Sp) ✓
    #
    # Only conclusion III follows → option D.
    {
        "question_number": 46,
        "difficulty": "easy",
        "source_pdf": "GD_Constable_26Feb2024_Shift2",
        "question_en": (
            "In the following question below are given some statements followed by "
            "some conclusions based on those statements. Taking the given statements "
            "to be true even if they seem to be at variance from commonly known facts. "
            "Read all the conclusions and then decide which of the given conclusion(s) "
            "logically follows the given statements.\n\n"
            "Statements:\n"
            "I.  No land is cup.\n"
            "II. Some spoon are land.\n\n"
            "Conclusions:\n"
            "I.   All cup are land.\n"
            "II.  All cup are spoon.\n"
            "III. Some land are spoon."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में कुछ कथन और उनके बाद उन कथनों पर आधारित कुछ "
            "निष्कर्ष दिए गए हैं। दिए गए कथनों को सत्य मानते हुए, सभी निष्कर्षों को "
            "पढ़िए और तय कीजिए कि कौन-सा/से निष्कर्ष तार्किक रूप से अनुसरण "
            "करता/करते हैं।\n\n"
            "कथन:\n"
            "I.  कोई भूमि कप नहीं है।\n"
            "II. कुछ चम्मच भूमि हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   सभी कप भूमि हैं।\n"
            "II.  सभी कप चम्मच हैं।\n"
            "III. कुछ भूमि चम्मच हैं।"
        ),
        "option_a": "Only conclusion I follows. / केवल निष्कर्ष I अनुसरण करता है।",
        "option_b": "Neither conclusion follows. / कोई भी निष्कर्ष अनुसरण नहीं करता है।",
        "option_c": "Both conclusions I and III follow. / दोनों निष्कर्ष I और III अनुसरण करते हैं।",
        "option_d": "Only conclusion III follows. / केवल निष्कर्ष III अनुसरण करता है।",
        "correct_answer": "D",
    },

    # ── Q47 (CHSL, 03 July 2024 Shift-3) — 3-conclusion custom ──────────────
    # All Ch→So (A); Some Ch are Be (I); No So is Ta (E).
    # Ch=chairs, So=sofas, Be=beds, Ta=tables.
    #
    # Derivations:
    # Darii:     Some Be are Ch (I-conv Stmt II) + All Ch→So → Some Be are So
    #            → I-conv: Some So are Be.
    # E-conv(3): No So is Ta → No Ta is So.
    # Camestres(Fig 2): All Ch→So + No Ta is So → No Ta is Ch.
    #
    # I:   Some So are Be (Some sofas are beds) → Darii + I-conv ✓
    # II:  No Ta is Ch  (No table is a chair)   → Camestres ✓
    # III: Some Ta are Be (Some tables are beds) → no link between Ta and Be ✗
    #
    # Both I and II follow → option A.
    {
        "question_number": 47,
        "difficulty": "hard",
        "source_pdf": "CHSL_03July2024_Shift3",
        "question_en": (
            "In this question, three statements are given, followed by three conclusions "
            "numbered I, II and III. Assuming the statements to be true even if they "
            "seem to be at variance with commonly known facts, decide which of the "
            "conclusions logically follows/follow from the statements.\n\n"
            "Statements:\n"
            "All chairs are sofas.\n"
            "Some chairs are beds.\n"
            "No sofa is a table.\n\n"
            "Conclusions:\n"
            "I.   Some sofas are beds.\n"
            "II.  No table is a chair.\n"
            "III. Some tables are beds."
        ),
        "question_hi": (
            "इस प्रश्न में तीन कथन दिए गए हैं, जिनके बाद I, II और III अंकित तीन "
            "निष्कर्ष दिए गए हैं। कथनों को सत्य मानते हुए, भले ही वे सामान्यतः "
            "ज्ञात तथ्यों से भिन्न प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से "
            "निष्कर्ष कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी कुर्सियाँ सोफे हैं।\n"
            "कुछ कुर्सियाँ बिस्तर हैं।\n"
            "कोई भी सोफा मेज नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.   कुछ सोफे बिस्तर हैं।\n"
            "II.  कोई भी मेज कुर्सी नहीं है।\n"
            "III. कुछ मेज बिस्तर हैं।"
        ),
        "option_a": "Both conclusions I and II follow. / दोनों निष्कर्ष I और II अनुसरण करते हैं।",
        "option_b": "Only conclusion II follows. / केवल निष्कर्ष II अनुसरण करता है।",
        "option_c": "Only conclusion I follows. / केवल निष्कर्ष I अनुसरण करता है।",
        "option_d": "None of the conclusions follows. / कोई भी निष्कर्ष अनुसरण नहीं करता है।",
        "correct_answer": "A",
    },

    # ── Q48 (CHSL, 03 July 2024 Shift-4) — 3-conclusion custom ──────────────
    # Some Ca are On (I); All On→Po (A); All Po→Ra (A).
    # Ca=carrots, On=onions, Po=potatoes, Ra=radish.
    #
    # Barbara:     All On→Po + All Po→Ra → All On→Ra.
    # Darii (1st): Some Ca are On + All On→Po  → Some Ca are Po.
    # Darii (2nd): Some Ca are Po + All Po→Ra  → Some Ca are Ra.
    #
    # I:   Some Ca are Ra → double Darii ✓
    # II:  All On→Ra      → Barbara ✓
    # III: No Ca is Po    → contradicts derived Some Ca are Po ✗
    #
    # Both I and II follow → option C.
    {
        "question_number": 48,
        "difficulty": "medium",
        "source_pdf": "CHSL_03July2024_Shift4",
        "question_en": (
            "In this question some statements are given, followed by three conclusions "
            "numbered I, II and III. Assuming the statements to be true, even if they "
            "seem to be at variance with commonly known facts, decide which of the "
            "conclusion(s) logically follows/follow from the statements.\n\n"
            "Statements:\n"
            "Some carrots are onions.\n"
            "All onions are potatoes.\n"
            "All potatoes are radish.\n\n"
            "Conclusions:\n"
            "I.   Some carrots are radish.\n"
            "II.  All onions are radish.\n"
            "III. No carrot is a potato."
        ),
        "question_hi": (
            "इस प्रश्न में तीन कथन दिए गए हैं, जिनके बाद I, II और III अंकित तीन "
            "निष्कर्ष दिए गए हैं। कथनों को सत्य मानते हुए, भले ही वे सामान्यतः "
            "ज्ञात तथ्यों से भिन्न प्रतीत होते हों, निर्णय लीजिए कि कौन-सा/से "
            "निष्कर्ष कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "कुछ गाजर प्याज हैं।\n"
            "सभी प्याज आलू हैं।\n"
            "सभी आलू मूली हैं।\n\n"
            "निष्कर्ष:\n"
            "I.   कुछ गाजर मूली हैं।\n"
            "II.  सभी प्याज मूली हैं।\n"
            "III. कोई गाजर आलू नहीं है।"
        ),
        "option_a": "Only conclusion II follows. / केवल निष्कर्ष II अनुसरण करता है।",
        "option_b": "Only conclusion I follows. / केवल निष्कर्ष I अनुसरण करता है।",
        "option_c": "Both conclusions I and II follow. / दोनों निष्कर्ष I और II अनुसरण करते हैं।",
        "option_d": "Both conclusions I and III follow. / दोनों निष्कर्ष I और III अनुसरण करते हैं।",
        "correct_answer": "C",
    },

    # ── Q49 (CHSL, 04 July 2024 Shift-1) — standard 2-conclusion (possibility)
    # All Ri→Ba (A); Some Ba are An (I); No An is Pe (E).
    # Ri=rings, Ba=bangles, An=anklets, Pe=pendants.
    # Ferio: Some Ba are An + No An is Pe → Some Ba are not Pe (O).
    #
    # I:   All rings being anklets is a possibility.
    #      All Ri→An would mean all rings (which are bangles via Stmt I) are anklets.
    #      Some bangles ARE anklets (Stmt II), so ring-bangles being all anklets
    #      creates no contradiction. Possibility holds ✓
    #
    # II:  All bangles can never be pendants (= No Ba is Pe, necessarily).
    #      Only Some Ba are not Pe (O-type, from Ferio) is derivable. Non-anklet
    #      bangles could be pendants; "No Ba is Pe" is NOT established. ✗
    #
    # Only conclusion I follows.
    {
        "question_number": 49,
        "difficulty": "hard",
        "source_pdf": "CHSL_04July2024_Shift1",
        "question_en": (
            "Read the given statements and conclusions carefully. Assuming that the "
            "information given in the statements is true, even if it appears to be "
            "at variance with commonly known facts, decide which of the given "
            "conclusions logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "All rings are bangles.\n"
            "Some bangles are anklets.\n"
            "No anklet is a pendant.\n\n"
            "Conclusions:\n"
            "(I)  All rings being anklets is a possibility.\n"
            "(II) All bangles can never be pendants."
        ),
        "question_hi": (
            "दिए गए कथनों और निष्कर्षों को ध्यानपूर्वक पढ़िए। यह मानते हुए कि "
            "कथनों में दी गई जानकारी सत्य है, भले ही वह सामान्यतः ज्ञात तथ्यों "
            "से भिन्न प्रतीत होती हो, निर्णय लीजिए कि दिए गए निष्कर्षों में से "
            "कौन-सा/से कथनों का तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "सभी अंगूठियाँ चूड़ियाँ हैं।\n"
            "कुछ चूड़ियाँ पायल हैं।\n"
            "कोई भी पायल लॉकेट नहीं है।\n\n"
            "निष्कर्ष:\n"
            "(I)  कुछ अंगूठियों के पायल होने की संभावना है।\n"
            "(II) सभी चूड़ियाँ कभी भी लॉकेट नहीं हो सकती हैं।"
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
