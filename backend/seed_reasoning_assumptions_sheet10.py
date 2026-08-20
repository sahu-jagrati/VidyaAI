"""
seed_reasoning_assumptions_sheet10.py
=========================================
Seeds Assumptions Q61-Q70 from Gagan Pratap Reasoning PDFs (Sheet 10).
Subject : Reasoning
Topic   : Assumptions
Run     : python seed_reasoning_assumptions_sheet10.py

NOTE: All Q61-Q70 are CONCLUSIONS type questions.
      Q64 has identical content to Q39 (same statement/conclusions from a
      different exam — UP Constable vs NTPC — both included in the PDF).
      Q65, Q67, Q69 have THREE conclusions; their option_a-d cover all four
      PDF answer options (Only I / Only II / Only III / special last option).

Answer key (solutions verified from image tick/cross markings):
  Q61  All drugs have side effects; always a built-in risk taking medicines.
       I)  No medicine is without risk of side effects → ✓ (direct paraphrase)
       II) Drugs make things worse than the disease itself → ✗ (too extreme;
           side effects ≠ necessarily worse than the disease)
       Answer: A  (Only I follows)  [standard option order]
       Source: NTPC CBT-2, 2021

  Q62  Nowadays, life has become very difficult without a mobile phone.
       I)  Total number of mobile subscribers is increasing → ✓
           (difficult without mobile → people get mobiles → subscriber count grows)
       II) Mobile has become an integral part of life → ✓
           ("life very difficult without mobile" = mobile is integral to life)
       Answer: C  (Both I & II follow)  [standard option order]
       Source: NTPC CBT-2, 2021

  Q63  A good voice is a natural gift but one has to keep practicing to improve
       and excel in the field of music.
       I)  Natural gifts need nurturing and care → ✓
           (keeping practicing to improve a gift = the gift needs nurturing)
       II) By continuous practice, one can GET a natural gift → ✗
           (practice IMPROVES a gift you already have; it cannot GIVE you the gift;
            "karke" is crossed in PDF — this is explicitly marked wrong)
       Answer: C  (Only I follows)
       [non-std: (a)=EitherIorII  (b)=Neither  (c)=OnlyI  (d)=OnlyII]
       Source: NTPC CBT-2, 2021

  Q64  No country is absolutely self-dependent these days.
       [Content identical to Q39 from NTPC CBT-2; this instance from UP Constable,
        27 Jan 2019 (Shift-1) — included separately in the practice PDF.]
       I)  It is impossible to grow and produce all that a country needs → ✓
       II) Countrymen in general have become lazy → ✗ (no link between economic
           interdependence and laziness; marked with X in PDF)
       Answer: A  (Only I follows)  [standard option order]
       Source: UP Constable, 27 Jan 2019 (Shift-1)

  Q65  THREE STATEMENTS → THREE CONCLUSIONS.
       Statements:
       I.  Many business offices are in buildings having 3 to 8 floors.
       II. If a building has more than 3 floors, it has a lift.
       Conclusions:
       I.  Only floors above the 3rd floor have lifts → ✗
           (a lift in a >3-floor building serves ALL floors, not just above 3rd)
       II. 7th floors have lifts → ✗
           (too specific; not all office buildings have 7 floors)
       III.All floors may be reached by lifts → ✓
           (in buildings with >3 floors — which house most offices — all floors
            can be reached by the lift; "may" makes it conditional/possible)
       Answer: C  (Only III follows)
       [options: (a)=OnlyI  (b)=OnlyII  (c)=OnlyIII  (d)=AllThree]
       Source: UP Constable, 27 Jan 2019 (Shift-1)

  Q66  ABC Co. slogan: 'Go ahead; purchase it if the price and quality are your
       considerations'.
       I)  The price of the product must be HIGH → ✗
           ("price" is a consideration but the slogan doesn't say the price is HIGH;
            "price" circled in PDF — this word makes conclusion I unjustified)
       II) The product must be of good quality → ✓
           (targeting quality-conscious buyers implies the product has good quality;
            "good quality" is circled in PDF as the correctly followed conclusion)
       Answer: B  (Only II follows)  [standard option order]
       Source: UP Constable, 28 Jan 2019 (Shift-2)

  Q67  THREE CONCLUSIONS: Every man should carry identity card with blood group,
       complete address, and telephone number for emergencies.
       I)  Blood CANNOT be transfused until group is mentioned in card → ✗
           (statement says card SHOULD have blood group; doesn't say blood can't be
            transfused without it — too extreme a medical conclusion)
       II) No one should forget phone number under any circumstances → ✗
           (card has phone number for emergencies; this doesn't mean people can't
            forget their own number — entirely different issue)
       III)The police need this information if the injury is fatal → ✓
           (card has emergency contact info; "in case of emergencies" implies police
            or emergency services need it for fatal injury situations)
       Answer: C  (Only III follows)
       [options: (a)=OnlyI  (b)=OnlyII  (c)=OnlyIII  (d)=NoneFollows]
       Source: UP Constable, 28 Jan 2019 (Shift-2)

  Q68  Domestic demand has been increasing faster than the production of wheat.
       I)  Domestic demand must be reduced → ✓
           (demand growing faster than production → supply-demand gap → reducing
            demand is a direct implied course of action)
       II) We should export wheat → ✗
           ("export" circled in PDF — exporting wheat when domestic demand already
            exceeds production would worsen the shortage; counterproductive)
       Answer: A  (Only I follows)  [standard option order]
       Source: UP Constable, 28 Jan 2019 (Shift-1)

  Q69  THREE CONCLUSIONS: All students in a class are bright. X is NOT bright.
       I)  Some students are NOT bright → ✗
           (contradicts statement I which says ALL students are bright)
       II) X must work hard → ✗
           (no logical link between X not being bright and X needing to work hard;
            marked with X in PDF)
       III)X is NOT a student of that class → ✓
           (modus tollens: All students → bright; X → NOT bright;
            therefore X → NOT a student of that class — valid deduction)
       Answer: C  (Only III follows)
       [options: (a)=OnlyI  (b)=OnlyII  (c)=OnlyIII  (d)=NoneFollows]
       Source: UP Constable, 28 Jan 2019 (Shift-1)

  Q70  Many people living in villages relocate to cities for a better future.
       I)  Government officers should have compulsory rural posting → ✓
           (people leave villages because rural areas lack opportunities; compulsory
            rural posting would bring government services/development to villages,
            directly addressing the root cause of migration)
       II) Increase more transport facilities between cities and villages → ✗
           (better transport helps commuting but doesn't address the "better future"
            reason for migration; doesn't directly tackle why people leave villages)
       Answer: B  (Only I follows)
       [non-std: (a)=Both  (b)=OnlyI  (c)=Neither  (d)=OnlyII]
       Source: ALP, 14 Aug 2018 (Shift-2)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Assumptions_Sheet10"
SUBJECT = "Reasoning"
TOPIC   = "Assumptions"

QUESTIONS = [
    # ── Q61 ── [CONCLUSIONS] Only I follows (drugs / side effects / built-in risk) ─
    # Standard option order.
    {
        "question_number": 61,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: All drugs have side effects. So, there is always a built-in "
            "risk while taking medicines.\n\n"
            "Conclusions:\n"
            "I.  No medicine is without the risk of side effects.\n"
            "II. Drugs make things worse than the disease itself."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: सभी दवाओं के दुष्प्रभाव होते हैं। इसलिए, दवाइयाँ लेते समय हमेशा एक "
            "अंतर्निहित जोखिम होता है।\n\n"
            "निष्कर्ष:\n"
            "I.  कोई भी दवा दुष्प्रभाव के जोखिम के बिना नहीं है।\n"
            "II. दवाइयाँ चीजों को बीमारी से भी बदतर बना देती हैं।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_d": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "correct_answer": "A",
        # I: "all drugs have side effects" = "no medicine is without risk of side effects"
        #    — direct logical paraphrase → ✓
        # II: side effects exist ≠ drugs make things worse than the disease; too extreme → ✗
    },
    # ── Q62 ── [CONCLUSIONS] Both follow (life difficult without mobile) ──────────
    # Standard option order.
    {
        "question_number": 62,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: Nowadays, life has become very difficult without a mobile "
            "phone.\n\n"
            "Conclusions:\n"
            "I.  The total number of mobile subscribers is increasing.\n"
            "II. Mobile has become an integral part of life."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: आजकल, मोबाइल फोन के बिना जीवन बहुत मुश्किल हो गया है।\n\n"
            "निष्कर्ष:\n"
            "I.  कुल मोबाइल ग्राहकों की संख्या बढ़ रही है।\n"
            "II. मोबाइल जीवन का अभिन्न अंग बन गया है।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Only II follows / केवल II अनुसरण करता है",
        "correct_answer": "C",
        # I: difficult without mobile → people get mobiles to overcome difficulty →
        #    total subscriber count increases → ✓
        # II: "life very difficult without mobile" = mobile is integral/indispensable
        #    to life → direct and natural conclusion → ✓
    },
    # ── Q63 ── [CONCLUSIONS] Only I follows (good voice / natural gift / practice) ─
    # Non-standard option order: (a)=EitherIorII (b)=Neither (c)=OnlyI (d)=OnlyII
    {
        "question_number": 63,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: A good voice is a natural gift but one has to keep practicing "
            "to improve and excel in the field of music.\n\n"
            "Conclusions:\n"
            "I.  Natural gifts need nurturing and care.\n"
            "II. By continuous practice, one can get a natural gift."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: अच्छी आवाज एक प्राकृतिक उपहार है, लेकिन किसी भी व्यक्ति को संगीत के "
            "क्षेत्र में सुधार तथा उत्कृष्टता लाने के लिए अभ्यास करना पड़ता है।\n\n"
            "निष्कर्ष:\n"
            "I.  प्राकृतिक उपहारों को पोषण और देखभाल की आवश्यकता होती है।\n"
            "II. निरंतर अभ्यास करके कोई भी व्यक्ति प्राकृतिक उपहार प्राप्त कर सकता है।"
        ),
        "option_a": "Either I or II follows / या तो I या II अनुसरण करता है",
        "option_b": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_c": "Only I follows / केवल I अनुसरण करता है",
        "option_d": "Only II follows / केवल II अनुसरण करता है",
        "correct_answer": "C",
        # I: keeping practicing to IMPROVE a natural gift = the gift needs nurturing
        #    and care to develop → ✓
        # II: practice improves an existing gift; it cannot GIVE you a natural gift that
        #    you don't have → explicitly crossed in PDF → ✗
    },
    # ── Q64 ── [CONCLUSIONS] Only I follows (no country self-dependent — dup Q39) ─
    # Duplicate statement/conclusions from Q39 (NTPC CBT-2) appearing in this set
    # from UP Constable, 27 Jan 2019 (Shift-1). Standard option order.
    {
        "question_number": 64,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: No country is absolutely self-dependent these days.\n\n"
            "Conclusions:\n"
            "I.  It is impossible to grow and produce all that a country needs.\n"
            "II. Countrymen in general have become lazy."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: आजकल कोई भी देश पूर्णतः आत्मनिर्भर नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  किसी देश की जरूरत की सभी चीजें उगाना और उत्पादन करना असंभव है।\n"
            "II. आम तौर पर देशवासी आलसी हो गए हैं।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "A",
        # I: no self-dependent country → countries can't produce all they need → ✓
        # II: economic interdependence ≠ laziness; X-marked in PDF → ✗
    },
    # ── Q65 ── [CONCLUSIONS] Only III follows — 3 statements, 3 conclusions ───────
    # Four answer options covering I / II / III / All.
    {
        "question_number": 65,
        "difficulty": "hard",
        "question_en": (
            "In the question below are given three statements followed by three "
            "conclusions numbered I, II, and III. You have to take the given "
            "statements to be true even if they seem to be at variance with commonly "
            "known facts and then decide which of the given conclusions logically "
            "follow(s) from the statements.\n\n"
            "Statements:\n"
            "I.  Many business offices are located in buildings having 3 to 8 floors.\n"
            "II. If a building has more than 3 floors, it has a lift.\n\n"
            "Conclusions:\n"
            "I.  Only floors above the 3rd floor have lifts.\n"
            "II. 7th floors have lifts.\n"
            "III.All floors may be reached by lifts."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में तीन कथन और उसके बाद तीन निष्कर्ष I, II और III "
            "दिए गए हैं। आपको दिए गए कथनों को सत्य मानना है, भले ही वे सामान्यतः "
            "ज्ञात तथ्यों से भिन्न प्रतीत हों, और फिर निर्णय करना है कि दिए गए "
            "निष्कर्षों में से कौन सा/से कथनों से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "I.  कई व्यावसायिक कार्यालय 3 से 8 मंजिलों वाली इमारतों में स्थित हैं।\n"
            "II. यदि किसी इमारत में 3 मंजिल से अधिक है, तो उसमें एक लिफ्ट है।\n\n"
            "निष्कर्ष:\n"
            "I.  केवल तीसरी मंजिल से ऊपर की मंजिलों पर लिफ्ट हैं।\n"
            "II. 7वीं मंजिल पर लिफ्ट है।\n"
            "III.सभी मंजिलों तक लिफ्टों द्वारा पहुँचा जा सकता है।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Only III follows / केवल III अनुसरण करता है",
        "option_d": "All three follow / सभी तीन अनुसरण करते हैं",
        "correct_answer": "C",
        # I: a lift in a >3-floor building serves ALL floors (1st, 2nd, 3rd too), not
        #    "ONLY floors above 3rd"; the statement is about the BUILDING having a lift,
        #    not about which specific floors have lift access → ✗
        # II: too specific; "7th floors" applies only to buildings with 7+ floors; not
        #    all office buildings in the 3-8 range have 7 floors → ✗
        # III: in buildings with >3 floors (which house most business offices), a lift
        #    exists → all floors of those buildings "may be reached by lifts"; "may"
        #    makes this appropriately conditional → ✓
    },
    # ── Q66 ── [CONCLUSIONS] Only II follows (ABC Co. slogan — price and quality) ─
    # Standard option order.
    {
        "question_number": 66,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: Company ABC has marketed the product with the following slogan: "
            "'Go ahead; purchase it if the price and quality are your considerations'.\n\n"
            "Conclusions:\n"
            "I.  The price of the product must be high.\n"
            "II. The product must be of good quality."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: कंपनी ABC ने निम्नलिखित नारे के साथ उत्पाद का विपणन किया है: 'आगे "
            "बढ़ें; अगर कीमत और गुणवत्ता आपके लिए मायने रखती है तो इसे खरीदें'।\n\n"
            "निष्कर्ष:\n"
            "I.  उत्पाद की कीमत अधिक होनी चाहिए।\n"
            "II. उत्पाद अच्छी गुणवत्ता का होना चाहिए।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "B",
        # I: "price is a consideration" ≠ "price must be HIGH"; the slogan targets
        #    price-conscious buyers but doesn't say the price is high → ✗
        # II: slogan targets quality-conscious buyers → company implies the product HAS
        #    good quality (otherwise why appeal to quality-conscious buyers?) → ✓
    },
    # ── Q67 ── [CONCLUSIONS] Only III follows — 2 statements, 3 conclusions ────────
    # Four answer options: Only I / Only II / Only III / None.
    {
        "question_number": 67,
        "difficulty": "hard",
        "question_en": (
            "In the question below are given two statements followed by three "
            "conclusions numbered I, II, and III. You have to take the given "
            "statements to be true even if they seem to be at variance with commonly "
            "known facts and then decide which of the given conclusions logically "
            "follow(s) from the statements.\n\n"
            "Statements:\n"
            "I.  Every man should have his identity card with him.\n"
            "II. That card should mention his blood group, complete address, and "
            "telephone number for contact, in case of emergencies.\n\n"
            "Conclusions:\n"
            "I.  Blood CANNOT be transfused until its group is mentioned in the card.\n"
            "II. No one is supposed to forget his phone number under any circumstances.\n"
            "III.The police need this information if the injury is fatal."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में दो कथन और उसके बाद तीन निष्कर्ष I, II और III "
            "दिए गए हैं। आपको दिए गए कथनों को सत्य मानना है, भले ही वे सामान्यतः "
            "ज्ञात तथ्यों से भिन्न प्रतीत हों, और फिर निर्णय करना है कि दिए गए "
            "निष्कर्षों में से कौन सा/से कथनों से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "I.  हर आदमी के पास अपना पहचान पत्र होना चाहिए।\n"
            "II. उस कार्ड को आपात स्थिति के मामले में अपने रक्त समूह, पूर्ण पते और "
            "संपर्क के लिए टेलीफोन नंबर का उल्लेख करना चाहिए।\n\n"
            "निष्कर्ष:\n"
            "I.  जब तक कार्ड में उसके समूह का उल्लेख नहीं किया जाता तब तक रक्त नहीं "
            "चढ़ाया जा सकता।\n"
            "II. किसी को भी किसी भी परिस्थिति में अपने फोन नंबर को नहीं भूलना चाहिए।\n"
            "III.यदि चोट घातक है तो पुलिस को इस जानकारी की आवश्यकता है।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Only III follows / केवल III अनुसरण करता है",
        "option_d": "None of them follows / कोई भी अनुसरण नहीं करता है",
        "correct_answer": "C",
        # I: statement says card SHOULD have blood group; doesn't say blood CAN'T be
        #    transfused without the card — too extreme a medical conclusion → ✗
        # II: card has phone number for emergencies ≠ people can't forget their own
        #    number; carrying a card vs. remembering a number are different → ✗
        # III: card has emergency info (blood group, address, phone) for use in
        #    emergencies → police/emergency services need this if injury is fatal → ✓
    },
    # ── Q68 ── [CONCLUSIONS] Only I follows (domestic demand > wheat production) ───
    # Standard option order.
    {
        "question_number": 68,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: Domestic demand has been increasing faster than the production "
            "of wheat.\n\n"
            "Conclusions:\n"
            "I.  Domestic demand must be reduced.\n"
            "II. We should export wheat."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: गेहूं के उत्पादन की तुलना में घरेलू मांग तेजी से बढ़ रही है।\n\n"
            "निष्कर्ष:\n"
            "I.  घरेलू मांग कम होनी चाहिए।\n"
            "II. हमें गेहूं का निर्यात करना चाहिए।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "A",
        # I: demand increasing faster than production → growing supply-demand gap →
        #    reducing demand is a direct implied course of action → ✓
        # II: "export" is circled in PDF — when domestic demand already exceeds
        #    production, exporting wheat would worsen the shortage; counterproductive → ✗
    },
    # ── Q69 ── [CONCLUSIONS] Only III follows — 2 statements, 3 conclusions ────────
    # Four answer options: Only I / Only II / Only III / None.
    {
        "question_number": 69,
        "difficulty": "medium",
        "question_en": (
            "In the question below are given two statements followed by three "
            "conclusions numbered I, II, and III. You have to take the given "
            "statements to be true even if they seem to be at variance with commonly "
            "known facts and then decide which of the given conclusions logically "
            "follow(s) from the statements.\n\n"
            "Statements:\n"
            "I.  All the students in a class are bright.\n"
            "II. X is NOT bright.\n\n"
            "Conclusions:\n"
            "I.  Some students are NOT bright.\n"
            "II. X must work hard.\n"
            "III.X is NOT a student of that class."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में दो कथन और उसके बाद तीन निष्कर्ष I, II और III "
            "दिए गए हैं। आपको दिए गए कथनों को सत्य मानना है, भले ही वे सामान्यतः "
            "ज्ञात तथ्यों से भिन्न प्रतीत हों, और फिर निर्णय करना है कि दिए गए "
            "निष्कर्षों में से कौन सा/से कथनों से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "I.  एक कक्षा के सभी छात्र प्रतिभाशाली हैं।\n"
            "II. X प्रतिभाशाली नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ छात्र प्रतिभाशाली नहीं हैं।\n"
            "II. X को कड़ी मेहनत करनी चाहिए।\n"
            "III.X उस कक्षा का छात्र नहीं है।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Only III follows / केवल III अनुसरण करता है",
        "option_d": "None of them follows / कोई भी अनुसरण नहीं करता है",
        "correct_answer": "C",
        # I: directly contradicts statement I ("ALL students are bright" → none is not
        #    bright) → ✗
        # II: no logical connection between X not being bright and X needing to work
        #    hard; marked X in PDF → ✗
        # III: modus tollens — All students → bright; X → NOT bright;
        #    therefore X → NOT a student of that class → valid deduction → ✓
    },
    # ── Q70 ── [CONCLUSIONS] Only I follows (village to city migration) ───────────
    # Non-standard option order: (a)=Both (b)=OnlyI (c)=Neither (d)=OnlyII
    {
        "question_number": 70,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: Many people living in villages relocate to cities for a better "
            "future.\n\n"
            "Conclusions:\n"
            "I.  Government officers should have compulsory rural posting.\n"
            "II. Increase more transport facilities between cities and villages."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: गांवों में रहने वाले बहुत से लोग बेहतर भविष्य के लिए शहरों में "
            "स्थानांतरित हो जाते हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  सरकारी अधिकारियों की अनिवार्य ग्रामीण पोस्टिंग होनी चाहिए।\n"
            "II. शहरों और गांवों के बीच अधिक परिवहन सुविधाएं बढ़ानी चाहिए।"
        ),
        "option_a": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_b": "Only I follows / केवल I अनुसरण करता है",
        "option_c": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_d": "Only II follows / केवल II अनुसरण करता है",
        "correct_answer": "B",
        # I: people leave villages for "better future" → villages lack opportunities;
        #    compulsory rural posting of govt officers would bring services/development
        #    to rural areas, directly addressing the root cause of migration → ✓
        # II: better transport helps commuting but doesn't address "better future" in
        #    villages — the core reason for migration; doesn't tackle rural development
        #    → ✗
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
            if d["question_number"] in existing_qnums:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
            inserted += 1
            print(f"  INSERT Q{d['question_number']}")

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
