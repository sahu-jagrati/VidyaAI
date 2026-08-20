"""
seed_reasoning_assumptions_sheet6.py
=========================================
Seeds Assumptions Q21-Q30 from Gagan Pratap Reasoning PDFs (Sheet 6).
Subject : Reasoning
Topic   : Assumptions
Run     : python seed_reasoning_assumptions_sheet6.py

NOTE: Q21-Q27 are standard Assumptions questions (implicit/not implicit).
      Q28-Q30 are Conclusions questions placed in the same topic set;
      options use "follows / does not follow" language and the model stores
      4 options (option_e is omitted since correct answer is always within a-d).

Answer key (solutions verified from image tick/cross markings):
  Q21  Statement: The BEST bus travel company has decided to increase its fare by 10%.
       I)  Passengers may opt for other buses costing less → IMPLICIT ✓
           (fare hike implies the risk of passengers switching to cheaper alternatives
            is an accepted implicit concern)
       II) The demand for buses may remain unchanged even after the fare hike → IMPLICIT ✓
           (the company raises fares assuming overall travel demand won't collapse;
            if they expected zero demand, they wouldn't raise fares)
       Answer: A  (Both I & II are implicit)
       Source: ALP, 09 Aug 2018, (Shift-2)

  Q22  Statement: Public smoking is an offence under the law.
       Note: Assumptions here also function as concurrent conclusions.
       I)  Smoking is injurious to the health of the person who smokes → IMPLICIT ✓
           (the law against smoking rests on the premise that smoking is harmful to the
            smoker — a necessary background assumption of the legislation)
       II) Smoke is injurious even to others' health in public places → IMPLICIT ✓
           (the "public" nature of the offence implies the law specifically targets harm
            to others in public spaces — the direct basis for the prohibition)
       Answer: A  (Both I & II are implicit)
       Source: ALP, 09 Aug 2018, (Shift-2)

  Q23  Statement: Due to the water crisis in the city, the authority had asked all the
       citizens to reduce their water consumption by 25%.
       I)  Many citizens may reduce their water consumption → IMPLICIT ✓
           (the authority issues the advisory assuming citizens will comply with it;
            otherwise the advisory is pointless)
       II) Many activists may protest to this advisory by the authority → NOT IMPLICIT ✗
           (protest is a possible but speculative reaction; the advisory does not assume
            opposition — it assumes cooperation)
       Answer: B  (Only I is implicit)
       Source: ALP, 09 Aug 2018, (Shift-3)

  Q24  Statement: Shyam tells Gita, 'The way to reach Sri Lanka is through air and water.'
       I)  Gita likes to travel to Sri Lanka → NOT IMPLICIT ✗
           (Shyam is merely providing travel information; there is no basis to assume
            Gita wants to visit Sri Lanka)
       II) Shyam is fond of advising people → NOT IMPLICIT ✗
           (Shyam sharing travel route information ≠ having a general fondness for
            advising people; this is a sweeping personal trait inference)
       Answer: B  (Neither I nor II is implicit)
       Source: ALP, 09 Aug 2018, (Shift-3)

  Q25  Statement: All girls love reading novels.
       I)  Novels are the only reading materials → NOT IMPLICIT ✗
           ("only" is circled — loving novels does not imply novels are the ONLY reading
            material; the statement merely highlights a preference, not exclusivity)
       II) No girl loves to read other materials → NOT IMPLICIT ✗
           (same reasoning — preference for novels doesn't mean no other reading;
            "loves novels" and "reads other things" are not mutually exclusive)
       Answer: C  (Neither I nor II is implicit)
       Source: ALP, 09 Aug 2018, (Shift-3)

  Q26  Statement: The Supreme Court has decided that all rapists will be hanged till death.
       I)  Women will get protection → NOT IMPLICIT ✗
           ("protection" is too broad; the court's verdict is a legal punishment, not a
            blanket protective mechanism — an unjustified leap)
       II) The number of rape cases can be reduced → IMPLICIT ✓
           (the court imposing the death penalty for rape implicitly assumes this will
            serve as a deterrent, thereby reducing the number of such cases)
       Answer: A  (Only II is implicit — note: Q26's option (a) says "Only II is implicit")
       Source: ALP, 17 Aug 2018, (Shift-3)

  Q27  Statement: Honesty is the best policy.
       Note: "policy" in the statement is an English idiom meaning "practice/approach",
             not a literal government or organisational policy document.
       I)  Honest people are policy makers → NOT IMPLICIT ✗
           ("policy" in the idiom is not referring to formal policies or policy-makers;
            conflating the idiomatic "policy" with legislative/organisational policy)
       II) Each policy must contain honesty → NOT IMPLICIT ✗
           (same reason — "policy" here means "guiding principle/approach"; assuming it
            refers to formal policy documents is a misreading of the idiom)
       Answer: B  (Neither I nor II is implicit)
       Source: ALP, 09 Aug 2018, (Shift-1)

  Q28  [CONCLUSIONS TYPE] — two statements, draw conclusions.
       Statement 1: All the organised persons find time for rest.
       Statement 2: Sunita, in spite of her very busy schedule finds time for rest.
       I)  Sunita is an organised person → FOLLOWS ✓
           (finding rest time DESPITE a very busy schedule is the hallmark of an
            organised person who manages time efficiently — supported by context)
       II) Sunita is an industrious person → FOLLOWS ✓
           (having a "very busy schedule" directly implies she works hard → industrious)
       Answer: C  (Both I & II follow)

  Q29  [CONCLUSIONS TYPE]
       Statement: This book 'Z' is the only book which focuses its attention to the
       problem of poverty in India between 1950 & 1980.
       I)  There was no question of poverty before 1950 → DOES NOT FOLLOW ✗
           ("before 1950" goes beyond the scope of the statement; the statement only
            covers 1950–1980 and says nothing about the period before 1950)
       II) No other book deals with poverty in India from 1950 to 1980 → FOLLOWS ✓
           ("the only book" directly implies no other book covers this topic and period)
       Answer: B  (Only II follows)

  Q30  [CONCLUSIONS TYPE]
       Statement: The percentage of the national income shared by the top 10% of
       households in India is 35.
       I)  When an economy grows fast, concentration of wealth in certain pockets
           takes place → DOES NOT FOLLOW ✗
           (the statement gives a static statistic; it says nothing about the speed of
            economic growth or its causal relationship to wealth concentration)
       II) The national income is unevenly distributed in India → FOLLOWS ✓
           (top 10% holding 35% of national income directly shows unequal distribution)
       Answer: B  (Only II follows)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Assumptions_Sheet6"
SUBJECT = "Reasoning"
TOPIC   = "Assumptions"

QUESTIONS = [
    # ── Q21 ── Both assumptions implicit (BEST bus 10% fare hike) ─────────────
    # Original option order: (a) Both (b) Only II (c) Only I (d) Neither
    {
        "question_number": 21,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: The BEST bus travel company has decided to increase its fare "
            "by 10%.\n\n"
            "Assumptions:\n"
            "I.  Passengers may opt for other buses costing less than the BEST bus "
            "travel company.\n"
            "II. The demand for buses by passengers may remain unchanged even after "
            "the fare hike."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: BEST बस ट्रैवल कंपनी ने अपना किराया 10% बढ़ाने का फैसला किया है।\n\n"
            "पूर्वानुमान:\n"
            "I.  यात्री BEST बस ट्रैवल कंपनी से कम लागत वाली अन्य बसों का विकल्प चुन "
            "सकते हैं।\n"
            "II. किराया वृद्धि के बाद भी यात्रियों द्वारा बसों की मांग अपरिवर्तित रह "
            "सकती है।"
        ),
        "option_a": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Only I is implicit / केवल I अंतर्निहित है",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "A",
        # I: fare increase → passengers may switch to cheaper alternatives → IMPLICIT ✓
        # II: company raises fares assuming demand doesn't collapse → IMPLICIT ✓
    },
    # ── Q22 ── Both assumptions implicit (public smoking offence) ─────────────
    # Note: Assumptions here function concurrently as conclusions (Cum Conclusions).
    # Original option order: (a) Both (b) Neither (c) Only II (d) Only I
    {
        "question_number": 22,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: Public smoking is an offence under the law.\n\n"
            "Assumptions:\n"
            "I.  Smoking is injurious to the health of the person who smokes.\n"
            "II. Smoke is injurious even to others' health in public places."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: सार्वजनिक धूम्रपान कानून के तहत अपराध है।\n\n"
            "पूर्वानुमान:\n"
            "I.  धूम्रपान करने वाले व्यक्ति के स्वास्थ्य के लिए धूम्रपान हानिकारक "
            "होता है।\n"
            "II. सार्वजनिक स्थानों पर धूम्रपान दूसरों के स्वास्थ्य के लिए भी "
            "हानिकारक है।"
        ),
        "option_a": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_b": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "option_c": "Only II is implicit / केवल II अंतर्निहित है",
        "option_d": "Only I is implicit / केवल I अंतर्निहित है",
        "correct_answer": "A",
        # I: the law against smoking rests on the premise that smoking harms the smoker
        #    → an assumed underlying fact of the legislation → IMPLICIT ✓
        # II: "PUBLIC" smoking offence specifically targets harm to bystanders → IMPLICIT ✓
    },
    # ── Q23 ── Only Assumption I implicit (water crisis 25% reduction advisory) ─
    # Original option order: (a) Neither (b) Only I (c) Only II (d) Both
    {
        "question_number": 23,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: Due to the water crisis in the city, the authority had asked "
            "all the citizens to reduce their water consumption by 25%.\n\n"
            "Assumptions:\n"
            "I.  Many citizens may reduce their water consumption.\n"
            "II. Many activists may protest to this advisory by the authority."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: शहर में पानी के संकट के कारण, प्राधिकरण ने सभी नागरिकों को अपने पानी "
            "की खपत को 25% कम करने के लिए कहा था।\n\n"
            "पूर्वानुमान:\n"
            "I.  कई नागरिक अपनी पानी की खपत कम कर सकते हैं।\n"
            "II. प्राधिकरण की इस सलाह का कई कार्यकर्ता विरोध कर सकते हैं।"
        ),
        "option_a": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "option_b": "Only I is implicit / केवल I अंतर्निहित है",
        "option_c": "Only II is implicit / केवल II अंतर्निहित है",
        "option_d": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "correct_answer": "B",
        # I: issuing an advisory assumes citizens will comply → IMPLICIT ✓
        # II: activist protest is speculative, not an assumption behind the advisory → NOT IMPLICIT ✗
    },
    # ── Q24 ── Neither assumption implicit (Shyam tells Gita Sri Lanka route) ──
    # Original option order: (a) Both (b) Neither (c) Only II (d) Only I
    {
        "question_number": 24,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: Shyam tells Gita, 'The way to reach Sri Lanka is through air "
            "and water.'\n\n"
            "Assumptions:\n"
            "I.  Gita likes to travel to Sri Lanka.\n"
            "II. Shyam is fond of advising people."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: श्याम, गीता से कहता है, 'श्रीलंका पहुँचने का मार्ग वायु और जल से "
            "होकर है।'\n\n"
            "पूर्वानुमान:\n"
            "I.  गीता को श्रीलंका की यात्रा करना पसंद है।\n"
            "II. श्याम को लोगों को सलाह देने का शौक है।"
        ),
        "option_a": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_b": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "option_c": "Only II is implicit / केवल II अंतर्निहित है",
        "option_d": "Only I is implicit / केवल I अंतर्निहित है",
        "correct_answer": "B",
        # I: Shyam sharing travel route ≠ Gita wanting to visit Sri Lanka → NOT IMPLICIT ✗
        # II: providing one travel tip ≠ being generally fond of advising → NOT IMPLICIT ✗
    },
    # ── Q25 ── Neither assumption implicit (all girls love reading novels) ──────
    # Original option order: (a) Both (b) Only I (c) Neither (d) Only II
    {
        "question_number": 25,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: All girls love reading novels.\n\n"
            "Assumptions:\n"
            "I.  Novels are the only reading materials.\n"
            "II. No girl loves to read other materials."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: सभी लड़कियों को उपन्यास पढ़ना बहुत पसंद होता है।\n\n"
            "पूर्वानुमान:\n"
            "I.  उपन्यास ही एकमात्र पठन सामग्री है।\n"
            "II. कोई भी लड़की दूसरी सामग्री पढ़ना पसंद नहीं करती है।"
        ),
        "option_a": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_b": "Only I is implicit / केवल I अंतर्निहित है",
        "option_c": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "option_d": "Only II is implicit / केवल II अंतर्निहित है",
        "correct_answer": "C",
        # I: "only" circled — loving novels ≠ novels are the ONLY reading material → NOT IMPLICIT ✗
        # II: preference for novels ≠ not reading other things; not mutually exclusive → NOT IMPLICIT ✗
    },
    # ── Q26 ── Only Assumption II implicit (SC: all rapists hanged till death) ──
    # Original option order: (a) Only II (b) Neither (c) Both (d) Only I ← non-standard
    {
        "question_number": 26,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: The Supreme Court has decided that all rapists will be hanged "
            "till death.\n\n"
            "Assumptions:\n"
            "I.  Women will get protection.\n"
            "II. The number of rape cases can be reduced."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: सर्वोच्च न्यायालय ने निर्णय लिया है कि सभी बलात्कारियों को मृत्यु तक "
            "फाँसी दी जाएगी।\n\n"
            "पूर्वानुमान:\n"
            "I.  महिलाओं को सुरक्षा मिलेगी।\n"
            "II. बलात्कार के मामलों को कम किया जा सकता है।"
        ),
        "option_a": "Only II is implicit / केवल II अंतर्निहित है",
        "option_b": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Only I is implicit / केवल I अंतर्निहित है",
        "correct_answer": "A",
        # I: "protection" is too broad and general; the verdict is a specific punishment,
        #    not a blanket protection mechanism → NOT IMPLICIT ✗
        # II: imposing death penalty assumes it will deter, thereby reducing rape cases
        #    → the implicit logic behind the judgment → IMPLICIT ✓
    },
    # ── Q27 ── Neither assumption implicit ("Honesty is the best policy") ───────
    # Original option order: (a) Both (b) Neither (c) Only II (d) Only I
    {
        "question_number": 27,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: Honesty is the best policy.\n\n"
            "Assumptions:\n"
            "I.  Honest people are policy makers.\n"
            "II. Each policy must contain honesty."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: ईमानदारी सर्वोत्तम नीति है।\n\n"
            "पूर्वानुमान:\n"
            "I.  ईमानदार लोग नीति निर्माता हैं।\n"
            "II. प्रत्येक नीति में ईमानदारी होनी चाहिए।"
        ),
        "option_a": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_b": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "option_c": "Only II is implicit / केवल II अंतर्निहित है",
        "option_d": "Only I is implicit / केवल I अंतर्निहित है",
        "correct_answer": "B",
        # "policy" in "best policy" is an English idiom meaning "guiding principle/approach"
        # I: conflates idiomatic "policy" with formal government/organisational policy → NOT IMPLICIT ✗
        # II: same misreading — "each policy must contain honesty" is a literal/formal
        #    interpretation of an idiomatic phrase → NOT IMPLICIT ✗
    },
    # ── Q28 ── [CONCLUSIONS] Both conclusions follow (Sunita organised/industrious) ─
    # 5-option format; option_e ("Either I or II follows") dropped as answer is C.
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": (
            "In the question below are given two statements followed by two conclusions "
            "numbered I and II. You have to take the given statements to be true even "
            "if they seem to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "1. All the organised persons find time for rest.\n"
            "2. Sunita, in spite of her very busy schedule finds time for rest.\n\n"
            "Conclusions:\n"
            "I.  Sunita is an organised person.\n"
            "II. Sunita is an industrious person."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में दो कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथनों को सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हों, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से निष्कर्ष कथनों से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "1. सभी संगठित व्यक्ति विश्राम का समय पाते हैं।\n"
            "2. सुनीता, अपने बहुत व्यस्त कार्यक्रम के बावजूद विश्राम के लिए समय "
            "निकालती है।\n\n"
            "निष्कर्ष:\n"
            "I.  सुनीता एक संगठित व्यक्ति है।\n"
            "II. सुनीता एक मेहनती इंसान है।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "C",
        # I: finding rest despite a very busy schedule is the hallmark of an organised
        #    person (efficient time manager) → FOLLOWS ✓
        # II: having a "very busy schedule" directly implies she is hardworking / industrious
        #    → FOLLOWS ✓
    },
    # ── Q29 ── [CONCLUSIONS] Only II follows (book Z on poverty 1950–1980) ──────
    # 5-option format; option_e dropped as answer is B.
    {
        "question_number": 29,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: This book 'Z' is the only book which focuses its attention to "
            "the problem of poverty in India between 1950 & 1980.\n\n"
            "Conclusions:\n"
            "I.  There was no question of poverty before 1950.\n"
            "II. No other book deals with poverty in India from 1950 to 1980."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: यह पुस्तक 'Z' एकमात्र पुस्तक है जो 1950 और 1980 के बीच भारत में "
            "गरीबी की समस्या पर अपना ध्यान केंद्रित करती है।\n\n"
            "निष्कर्ष:\n"
            "I.  1950 से पहले गरीबी का कोई सवाल नहीं था।\n"
            "II. 1950 से 1980 के दौरान भारत में गरीबी से संबंधित कोई अन्य पुस्तक नहीं है।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "B",
        # I: "before 1950" is beyond the scope of the statement; the statement covers only
        #    1950–1980 and implies nothing about earlier periods → DOES NOT FOLLOW ✗
        # II: "the only book" directly and explicitly implies no other book covers this
        #    topic for this period → FOLLOWS ✓
    },
    # ── Q30 ── [CONCLUSIONS] Only II follows (top 10% hold 35% national income) ─
    # 5-option format; option_e dropped as answer is B.
    {
        "question_number": 30,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: The percentage of the national income shared by the top 10% of "
            "households in India is 35.\n\n"
            "Conclusions:\n"
            "I.  When an economy grows fast, concentration of wealth in certain pockets "
            "of population takes place.\n"
            "II. The national income is unevenly distributed in India."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: भारत में शीर्ष 10 प्रतिशत परिवारों द्वारा साझा राष्ट्रीय आय का "
            "प्रतिशत 35 है।\n\n"
            "निष्कर्ष:\n"
            "I.  जब कोई अर्थव्यवस्था तेजी से बढ़ती है, तो आबादी के कुछ हिस्सों में "
            "धन की एकाग्रता होती है।\n"
            "II. भारत में राष्ट्रीय आय असमान रूप से वितरित की जाती है।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "B",
        # I: the statement gives a static statistic; it says nothing about the rate of
        #    economic growth or its causal link to wealth concentration → DOES NOT FOLLOW ✗
        # II: top 10% of households holding 35% of national income directly proves unequal
        #    distribution → FOLLOWS ✓
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
