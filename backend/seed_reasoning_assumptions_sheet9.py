"""
seed_reasoning_assumptions_sheet9.py
=========================================
Seeds Assumptions Q51-Q60 from Gagan Pratap Reasoning PDFs (Sheet 9).
Subject : Reasoning
Topic   : Assumptions
Run     : python seed_reasoning_assumptions_sheet9.py

NOTE: All Q51-Q60 are CONCLUSIONS type questions ("follows / does not follow").
      Original PDF option orders are preserved so that correct_answer letter
      matches the PDF.  Several questions use "Either I or II follows" as a
      standard fifth possibility (stored in option_b or option_d as it appears).

Answer key (solutions verified from image tick/cross markings):
  Q51  Rahul reads 20 pages a day.
       I)  Rahul is poor in reading → ✗ (quantity of reading ≠ quality/ability)
       II) Rahul must be having exams → ✗ (reading 20 pages/day ≠ exam context)
       Answer: B  (Neither I nor II follows)
       [non-std: (a)=OnlyI  (b)=Neither  (c)=OnlyII  (d)=Both]
       Source: UPSI, 13 Nov 2021 (Shift-2)

  Q52  It rains every Monday. It rains today.
       I)  It must be a rainy season → ✗ (raining on Mondays + today ≠ rainy season)
       II) Today is Monday → ✗ (affirming-the-consequent: other days may also rain;
           "every Monday it rains" does not mean "if it rains, it is Monday")
       Answer: B  (Neither I nor II follows)
       [non-std: (a)=OnlyII  (b)=Neither  (c)=EitherIorII  (d)=OnlyI]
       Source: UPSI, 25 Nov 2021 (Shift-3)

  Q53  Girls native to Seoul will definitely get married at the age of 23.
       Beni is a 24-year-old girl.
       I)  Except for Seoul girls, girls in other cities marry BEFORE 23 → ?
       II) Except for Seoul girls, girls in other cities marry AFTER 23 → ?
       The statement sets Seoul at 23; girls in other cities must be either before OR
       after 23 — one must be true but the statement doesn't say which.
       Answer: C  (Either I or II follows)
       [non-std: (a)=OnlyII  (b)=Neither  (c)=EitherIorII  (d)=OnlyI]
       Source: UPSI, 27 Nov 2021 (Shift-2)

  Q54  Shyam is one of the students who are EXPECTED to get placed in ABC India Pvt Ltd.
       I)  Shyam WILL get placed → "Expected" ≠ certain; placement may or may not happen
       II) Shyam will NOT get placed → Equally possible given uncertainty
       One of I or II will ultimately be true; neither can be definitively concluded now.
       Answer: D  (Either I or II follows)
       [non-std: (a)=OnlyII  (b)=Neither  (c)=OnlyI  (d)=EitherIorII]
       Source: UPSI, 20 Nov 2021 (Shift-2)

  Q55  In modern days, a man influences his destiny by the choices he makes unlike in
       the past days.
       I)  Earlier there were less options available to choose from → ✓
           ("unlike in the past" implies the past was different — fewer choices available
            meant people couldn't influence their destiny through choice the same way)
       II) In the past, there was no desire to influence the destiny → ✗
           (the statement implies past methods were different, not that there was NO
            desire; "couldn't" ≠ "didn't want to" — too strong a claim)
       Answer: C  (Only I follows)
       [non-std: (a)=Neither  (b)=OnlyII  (c)=OnlyI  (d)=Both]
       Source: NTPC CBT-2, 2021

  Q56  There is no such thing as a free lunch.
       I)  Things that are free, always have a hidden cost → ✓
           ("no free lunch" directly means nothing is truly free — hidden costs exist)
       II) It is impossible to get some things for nothing → ✓
           (same idiomatic meaning: you can't get something without giving something;
            perfectly aligns with "no free lunch")
       Answer: C  (Both I & II follow)
       [non-std: (a)=OnlyII  (b)=OnlyI  (c)=Both  (d)=Neither]
       Source: NTPC CBT-2, 2021

  Q57  A. People who exercise regularly are health conscious.
       B. Meena in spite of her busy schedule, exercises every day.
       I)  Meena is health-conscious → ✓
           (A: regular exercisers = health conscious; B: Meena exercises every day
            → valid syllogism → Meena is health conscious)
       II) Meena's family has inculcated the importance of exercise from her childhood
           → ✗ (statements say nothing about Meena's family or childhood; speculative)
       Answer: D  (Only I follows)
       [non-std: (a)=Both  (b)=Neither  (c)=OnlyII  (d)=OnlyI]
       Source: NTPC CBT-2, 2021

  Q58  I. Use of electronic book reading has increased considerably during recent times.
       II. Printed books are costly.
       Conclusions:
       I)  Nobody reads books nowadays → ✗
           ("increased" use of e-books ≠ nobody reads books; books are still read)
       II) Electronic book reading is gaining popularity → ✓
           (has "increased considerably" = is gaining popularity; directly follows)
       Answer: B  (Only II follows)
       [non-std: (a)=Neither  (b)=OnlyII  (c)=OnlyI  (d)=Both]
       Source: NTPC CBT-2, 2021

  Q59  Adversity is the best teacher.
       I)  Poor people are learned → ✗
           (poor ≠ people who face adversity; and even if adversity → wisdom, the
            chain "poor → adversity → learned" involves too many unsupported links)
       II) Adversity provides opportunities to learn → ✓
           (best teacher = teaches well = provides learning opportunities; direct
            paraphrase of the statement's meaning)
       Answer: A  (Only II follows)
       [non-std: (a)=OnlyII  (b)=Neither  (c)=OnlyI  (d)=Both]
       Source: NTPC CBT-2, 2021

  Q60  Adversity makes the man wise.
       I)  The poor are wise → ✗  (crossed in PDF)
           (poverty ≠ adversity, and even adversity → wise doesn't mean all who face
            adversity are "the poor"; cannot map "adversity" to "poor people" → ✗)
       II) Men learn from bitter experience → ✓
           (adversity = bitter experience; "makes wise" = learn from it; direct and
            valid paraphrase)
       Answer: C  (Only II follows)
       [non-std: (a)=OnlyI  (b)=EitherIorII  (c)=OnlyII  (d)=Neither]
       Source: NTPC CBT-2, 2021
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Assumptions_Sheet9"
SUBJECT = "Reasoning"
TOPIC   = "Assumptions"

QUESTIONS = [
    # ── Q51 ── [CONCLUSIONS] Neither follows (Rahul reads 20 pages/day) ─────────
    # Non-standard option order: (a)=OnlyI  (b)=Neither  (c)=OnlyII  (d)=Both
    {
        "question_number": 51,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: Rahul reads 20 pages a day.\n\n"
            "Conclusions:\n"
            "I.  Rahul is poor in reading.\n"
            "II. Rahul must be having exams."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: राहुल एक दिन में 20 पेज पढ़ते हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  राहुल पढ़ने में कमजोर है।\n"
            "II. राहुल की परीक्षा हो रही होगी।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_c": "Only II follows / केवल II अनुसरण करता है",
        "option_d": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "correct_answer": "B",
        # I: reading 20 pages/day says nothing about reading ability → ✗
        # II: reading habitually ≠ exam context; no link to exams → ✗
    },
    # ── Q52 ── [CONCLUSIONS] Neither follows (rains every Monday, rains today) ───
    # Non-standard: (a)=OnlyII  (b)=Neither  (c)=EitherIorII  (d)=OnlyI
    {
        "question_number": 52,
        "difficulty": "medium",
        "question_en": (
            "In the question below are given two statements followed by two conclusions "
            "numbered I and II. You have to take the given statements to be true even "
            "if they seem to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "1. It rains every Monday.\n"
            "2. It rains today.\n\n"
            "Conclusions:\n"
            "I.  It must be a rainy season.\n"
            "II. Today is Monday."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में दो कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथनों को सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हों, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से निष्कर्ष कथनों से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "1. हर सोमवार को वर्षा होती है।\n"
            "2. आज वर्षा हो रही है।\n\n"
            "निष्कर्ष:\n"
            "I.  यह वर्षा का मौसम होना चाहिए।\n"
            "II. आज सोमवार है।"
        ),
        "option_a": "Only II follows / केवल II अनुसरण करता है",
        "option_b": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_c": "Either I or II follows / या तो I या II अनुसरण करता है",
        "option_d": "Only I follows / केवल I अनुसरण करता है",
        "correct_answer": "B",
        # I: raining on Mondays + raining today ≠ rainy season → ✗
        # II: affirming the consequent — other days may also have rain; "every Monday
        #    rains" ≠ "if it rains, it is Monday" → ✗
    },
    # ── Q53 ── [CONCLUSIONS] Either I or II follows (Seoul girls marry at 23) ────
    # Non-standard: (a)=OnlyII  (b)=Neither  (c)=EitherIorII  (d)=OnlyI
    {
        "question_number": 53,
        "difficulty": "hard",
        "question_en": (
            "In the question below are given two statements followed by two conclusions "
            "numbered I and II. You have to take the given statements to be true even "
            "if they seem to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "1. Girls native to Seoul will definitely get married at the age of 23.\n"
            "2. Beni is a 24-year-old girl.\n\n"
            "Conclusions:\n"
            "I.  Except for Seoul girls, girls in other cities marry before 23.\n"
            "II. Except for Seoul girls, girls in other cities marry after 23."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में दो कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथनों को सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हों, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से निष्कर्ष कथनों से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "1. सियोल की मूल निवासी लड़कियों की शादी निश्चित रूप से 23 वर्ष की आयु में "
            "हो जाएगी।\n"
            "2. बेनी 24 वर्ष की लड़की है।\n\n"
            "निष्कर्ष:\n"
            "I.  सियोल की लड़कियों को छोड़कर, अन्य शहरों की लड़कियों की शादी 23 वर्ष "
            "से पहले हो जाती है।\n"
            "II. सियोल को छोड़कर अन्य शहरों में लड़कियों की शादी 23 वर्ष के बाद होती है।"
        ),
        "option_a": "Only II follows / केवल II अनुसरण करता है",
        "option_b": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_c": "Either I or II follows / या तो I या II अनुसरण करता है",
        "option_d": "Only I follows / केवल I अनुसरण करता है",
        "correct_answer": "C",
        # Seoul girls marry AT 23; girls from other cities either marry before 23 or
        # after 23 — one of these must be true, but the statement doesn't specify which.
        # I and II are mutually exclusive opposites; exactly one is true → Either I or II
    },
    # ── Q54 ── [CONCLUSIONS] Either I or II follows (Shyam expected to get placed) ─
    # Non-standard: (a)=OnlyII  (b)=Neither  (c)=OnlyI  (d)=EitherIorII
    {
        "question_number": 54,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: Shyam is one of the students who are expected to get placed "
            "in ABC India Pvt Ltd.\n\n"
            "Conclusions:\n"
            "I.  Shyam will get placed in ABC India Pvt Ltd.\n"
            "II. Shyam will not get placed in ABC India Pvt Ltd."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: श्याम उन छात्रों में से एक हैं जिन्हें एबीसी इंडिया प्राइवेट लिमिटेड "
            "में नौकरी मिलने की उम्मीद है।\n\n"
            "निष्कर्ष:\n"
            "I.  श्याम को एबीसी इंडिया प्राइवेट लिमिटेड में नौकरी मिल जाएगी।\n"
            "II. श्याम को एबीसी इंडिया प्राइवेट लिमिटेड में नौकरी नहीं मिलेगी।"
        ),
        "option_a": "Only II follows / केवल II अनुसरण करता है",
        "option_b": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_c": "Only I follows / केवल I अनुसरण करता है",
        "option_d": "Either I or II follows / या तो I या II अनुसरण करता है",
        "correct_answer": "D",
        # "Expected" ≠ certain; placement may or may not happen.
        # I and II are mutually exclusive and exhaustive — one will ultimately be true.
        # We cannot say which now, so: Either I or II follows.
    },
    # ── Q55 ── [CONCLUSIONS] Only I follows (modern choices influence destiny) ────
    # Non-standard: (a)=Neither  (b)=OnlyII  (c)=OnlyI  (d)=Both
    {
        "question_number": 55,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: In modern days, a man influences his destiny by the choices he "
            "makes unlike in the past days.\n\n"
            "Conclusions:\n"
            "I.  Earlier there were less options available to choose from.\n"
            "II. In the past, there was no desire to influence the destiny."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: पिछले दिनों के विपरीत, आधुनिक दिनों में, एक आदमी अपने भाग्य को अपने "
            "द्वारा चुने गए विकल्पों से प्रभावित करता है।\n\n"
            "निष्कर्ष:\n"
            "I.  पहले चुनने के लिए कम विकल्प उपलब्ध थे।\n"
            "II. अतीत में, भाग्य को प्रभावित करने की कोई इच्छा नहीं थी।"
        ),
        "option_a": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Only I follows / केवल I अनुसरण करता है",
        "option_d": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "correct_answer": "C",
        # I: "unlike in the past" implies fewer choices were available before → ✓
        # II: "no desire" is too strong; past people may have desired but couldn't act;
        #    inability ≠ no desire → ✗
    },
    # ── Q56 ── [CONCLUSIONS] Both follow ("no free lunch") ───────────────────────
    # Non-standard: (a)=OnlyII  (b)=OnlyI  (c)=Both  (d)=Neither
    {
        "question_number": 56,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: There is no such thing as a free lunch.\n\n"
            "Conclusions:\n"
            "I.  Things that are free, always have a hidden cost.\n"
            "II. It is impossible to get some things for nothing."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: मुफ्त लंच जैसी कोई चीज नहीं होती है।\n\n"
            "निष्कर्ष:\n"
            "I.  चीजें जो मुफ्त हैं, हमेशा एक छिपी हुई लागत होती है।\n"
            "II. कुछ चीजें बिना कुछ लिए प्राप्त करना असंभव है।"
        ),
        "option_a": "Only II follows / केवल II अनुसरण करता है",
        "option_b": "Only I follows / केवल I अनुसरण करता है",
        "option_c": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "C",
        # I: "no free lunch" = nothing is truly free → hidden costs always exist → ✓
        # II: can't get something for nothing = direct restatement of the idiom → ✓
    },
    # ── Q57 ── [CONCLUSIONS] Only I follows (Meena exercises / health conscious) ──
    # Non-standard: (a)=Both  (b)=Neither  (c)=OnlyII  (d)=OnlyI
    {
        "question_number": 57,
        "difficulty": "medium",
        "question_en": (
            "In the question below are given two statements followed by two conclusions "
            "numbered I and II. You have to take the given statements to be true even "
            "if they seem to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "A. People who exercise regularly are health conscious.\n"
            "B. Meena in spite of her busy schedule, exercises every day.\n\n"
            "Conclusions:\n"
            "I.  Meena is health-conscious.\n"
            "II. Meena's family has inculcated the importance of exercise right from "
            "her childhood."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में दो कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथनों को सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हों, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से निष्कर्ष कथनों से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "A. जो लोग नियमित रूप से व्यायाम करते हैं वे स्वास्थ्य के प्रति जागरूक "
            "होते हैं।\n"
            "B. मीना अपने व्यस्त कार्यक्रम के बावजूद हर दिन व्यायाम करती है।\n\n"
            "निष्कर्ष:\n"
            "I.  मीना स्वास्थ्य के प्रति जागरूक है।\n"
            "II. मीना के परिवार ने बचपन से ही व्यायाम के महत्व को समझा है।"
        ),
        "option_a": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "option_b": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_c": "Only II follows / केवल II अनुसरण करता है",
        "option_d": "Only I follows / केवल I अनुसरण करता है",
        "correct_answer": "D",
        # I: A→ regular exercisers = health conscious; B→ Meena exercises every day
        #    → valid syllogism → Meena is health conscious → ✓
        # II: statements mention nothing about Meena's family or childhood → speculative → ✗
    },
    # ── Q58 ── [CONCLUSIONS] Only II follows (e-book use increased / printed costly) ─
    # Non-standard: (a)=Neither  (b)=OnlyII  (c)=OnlyI  (d)=Both
    {
        "question_number": 58,
        "difficulty": "medium",
        "question_en": (
            "In the question below are given two statements followed by two conclusions "
            "numbered I and II. You have to take the given statements to be true even "
            "if they seem to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statements.\n\n"
            "Statements:\n"
            "I.  Use of electronic book reading has increased considerably during "
            "recent times.\n"
            "II. Printed books are costly.\n\n"
            "Conclusions:\n"
            "I.  Nobody reads books nowadays.\n"
            "II. Electronic book reading is gaining popularity."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में दो कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथनों को सत्य मानना है, भले ही वे सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हों, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से निष्कर्ष कथनों से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन:\n"
            "I.  हाल के दिनों में इलेक्ट्रॉनिक रूप से पुस्तक पढ़ने का उपयोग काफी "
            "बढ़ गया है।\n"
            "II. छपी हुई पुस्तकें महंगी होती हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  आजकल कोई भी पुस्तकें नहीं पढ़ता है।\n"
            "II. इलेक्ट्रॉनिक रूप से पुस्तक पढ़ना लोकप्रिय हो रहा है।"
        ),
        "option_a": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_b": "Only II follows / केवल II अनुसरण करता है",
        "option_c": "Only I follows / केवल I अनुसरण करता है",
        "option_d": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "correct_answer": "B",
        # I: "increased" e-book use ≠ "nobody reads books"; books are still being read
        #    (just more electronic) → ✗
        # II: "increased considerably" = gaining popularity; direct paraphrase → ✓
    },
    # ── Q59 ── [CONCLUSIONS] Only II follows (adversity is the best teacher) ─────
    # Non-standard: (a)=OnlyII  (b)=Neither  (c)=OnlyI  (d)=Both
    {
        "question_number": 59,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: Adversity is the best teacher.\n\n"
            "Conclusions:\n"
            "I.  Poor people are learned.\n"
            "II. Adversity provides opportunities to learn."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: विपत्ति सबसे अच्छी शिक्षक होती है।\n\n"
            "निष्कर्ष:\n"
            "I.  गरीब लोग शिक्षित होते हैं।\n"
            "II. विपत्ति सीखने का अवसर प्रदान करती है।"
        ),
        "option_a": "Only II follows / केवल II अनुसरण करता है",
        "option_b": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "option_c": "Only I follows / केवल I अनुसरण करता है",
        "option_d": "Both I & II follow / I और II दोनों अनुसरण करते हैं",
        "correct_answer": "A",
        # I: poverty ≠ adversity; and adversity → wise ≠ "poor people are learned";
        #    the chain poor→adversity→learned involves too many unsupported steps → ✗
        # II: "best teacher" = teaches well = provides opportunities to learn;
        #    direct and valid restatement of the statement → ✓
    },
    # ── Q60 ── [CONCLUSIONS] Only II follows (adversity makes the man wise) ──────
    # Non-standard: (a)=OnlyI  (b)=EitherIorII  (c)=OnlyII  (d)=Neither
    {
        "question_number": 60,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two conclusions "
            "numbered I and II. You have to take the given statement to be true even "
            "if it seems to be at variance with commonly known facts and then decide "
            "which of the given conclusions logically follow(s) from the statement.\n\n"
            "Statement: Adversity makes the man wise.\n\n"
            "Conclusions:\n"
            "I.  The poor are wise.\n"
            "II. Men learn from bitter experience."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन और उसके बाद दो निष्कर्ष I और II दिए गए हैं। "
            "आपको दिए गए कथन को सत्य मानना है, भले ही वह सामान्यतः ज्ञात तथ्यों से "
            "भिन्न प्रतीत हो, और फिर निर्णय करना है कि दिए गए निष्कर्षों में से कौन "
            "सा/से कथन से तार्किक रूप से अनुसरण करता/करते हैं।\n\n"
            "कथन: प्रतिकूलता मनुष्य को बुद्धिमान बनाती है।\n\n"
            "निष्कर्ष:\n"
            "I.  गरीब समझदार होते हैं।\n"
            "II. व्यक्ति बुरे अनुभवों से सीखता है।"
        ),
        "option_a": "Only I follows / केवल I अनुसरण करता है",
        "option_b": "Either I or II follows / या तो I या II अनुसरण करता है",
        "option_c": "Only II follows / केवल II अनुसरण करता है",
        "option_d": "Neither I nor II follows / न तो I और न ही II अनुसरण करता है",
        "correct_answer": "C",
        # I: crossed in PDF — poverty ≠ adversity; "poor are wise" cannot be mapped
        #    from "adversity makes wise" → ✗
        # II: adversity = bitter experience; makes wise = learn from it → "men learn
        #    from bitter experience" is a valid direct paraphrase → ✓
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
