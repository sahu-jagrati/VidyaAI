"""
seed_reasoning_analytical_sheet8.py
====================================
Seeds Statement Assumption & Conclusion Q52–Q62 (Sheet 8).
Subject : Reasoning
Topic   : Statement Assumption and Conclusion

Option-format guide
───────────────────
5-opt (5th injected by frontend) — REQUIRES option_c starts "Both I & II follow" (ampersand):
  used for Q24-Q51 (previously seeded, NOT in this script).

4-opt standard, NO injection  — option_c = "Both I and II follow." (uses "and", not "&"):
  Q52, Q54, Q58, Q59, Q60, Q61, Q62

Special 4-opt: "Either I or II" is stored explicitly as option_b (no "Both" option):
  Q53  →  A=Only I, B=Either I or II, C=Only II, D=Neither I nor II

3-conclusion 4-opt (option_c = "Only III follows." → no injection):
  Q55  (option_d = "All three follow.")
  Q56  (option_d = "None of them follows.")
  Q57  (option_d = "None of them follows.")

Answer key:
  Q52 B   Q53 C   Q54 A   Q55 B   Q56 D   Q57 C
  Q58 A   Q59 A   Q60 C   Q61 A   Q62 B
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Statement Assumption and Conclusion"

# ── shared option strings ──────────────────────────────────────────────────

# 4-opt standard (no injection) — uses "and" NOT "&"
_A  = "Only I follows. / केवल I अनुसरण करता है।"
_B  = "Only II follows. / केवल II अनुसरण करता है।"
_C4 = "Both I and II follow. / I और II दोनों अनुसरण करते हैं।"
_D  = "Neither I nor II follows. / न तो I और न ही II अनुसरण करता है।"

# 3-conclusion shared options
_C3  = "Only III follows. / केवल III अनुसरण करता है।"
_D3A = "All three follow. / सभी तीनों अनुसरण करते हैं।"
_D3N = "None of them follows. / इनमें से कोई भी अनुसरण नहीं करता।"

QUESTIONS = [

    # ── Q52 ──────────────────────────────────────────────────────────────────
    # Source: NTPC CBT-2, 2021 | Format: 4-opt, no injection
    # Statement: Adversity is the best teacher.
    # I. Poor people are learned.            → ✗ (adversity ≠ poverty; "learned" too strong)
    # II. Adversity provides opp. to learn.  → ✓ (best teacher = provides learning opportunities)
    # Answer: B
    {
        "question_number": 52,
        "difficulty": "medium",
        "source_pdf": "NTPC_CBT2_2021",
        "question_en": (
            "Statement: Adversity is the best teacher.\n\n"
            "Conclusions:\n"
            "I.  Poor people are learned.\n"
            "II. Adversity provides opportunities to learn."
        ),
        "question_hi": (
            "कथन: विपत्ति सबसे अच्छी शिक्षक होती है।\n\n"
            "निष्कर्ष:\n"
            "I.  निर्धन लोग शिक्षित होते हैं।\n"
            "II. विपत्ति सीखने का अवसर प्रदान करती है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C4,
        "option_d": _D,
        "correct_answer": "B",
    },

    # ── Q53 ──────────────────────────────────────────────────────────────────
    # Source: NTPC CBT-2, 2021 | Format: special 4-opt (option_b = "Either I or II")
    # Statement: Adversity makes the man wise.
    # I. The poor are wise.               → ✗ (poverty ≠ adversity; too broad a generalization)
    # II. Men learn from bitter experience. → ✓ (adversity = bitter experience → learn → wise)
    # Answer: C  (option_c = "Only II follows.")
    {
        "question_number": 53,
        "difficulty": "medium",
        "source_pdf": "NTPC_CBT2_2021",
        "question_en": (
            "Statement: Adversity makes the man wise.\n\n"
            "Conclusions:\n"
            "I.  The poor are wise.\n"
            "II. Men learn from bitter experience."
        ),
        "question_hi": (
            "कथन: प्रतिकूलता मनुष्य को बुद्धिमान बनाती है।\n\n"
            "निष्कर्ष:\n"
            "I.  गरीब लोग समझदार होते हैं।\n"
            "II. व्यक्ति कड़वे अनुभवों से सीखता है।"
        ),
        "option_a": "Only I follows. / केवल I अनुसरण करता है।",
        "option_b": "Either I or II follows. / या तो I या II अनुसरण करता है।",
        "option_c": "Only II follows. / केवल II अनुसरण करता है।",
        "option_d": "Neither I nor II follows. / न तो I और न ही II अनुसरण करता है।",
        "correct_answer": "C",
    },

    # ── Q54 ──────────────────────────────────────────────────────────────────
    # Source: NTPC CBT-2, 2021 | Format: 4-opt, no injection
    # Statement: All drugs have side effects. There is always a built-in risk.
    # I. No medicine is without risk of side effects. → ✓ (direct restatement)
    # II. Drugs make things worse than disease itself. → ✗ (side effects ≠ worse than disease)
    # Answer: A
    {
        "question_number": 54,
        "difficulty": "medium",
        "source_pdf": "NTPC_CBT2_2021",
        "question_en": (
            "Statement: All drugs have side effects. So, there is always a built-in risk "
            "while taking medicines.\n\n"
            "Conclusions:\n"
            "I.  No medicine is without the risk of side effects.\n"
            "II. Drugs make things worse than the disease itself."
        ),
        "question_hi": (
            "कथन: सभी दवाओं के दुष्प्रभाव होते हैं। इसलिए, दवाएँ लेते समय हमेशा "
            "एक अंतर्निहित जोखिम होता है।\n\n"
            "निष्कर्ष:\n"
            "I.  कोई भी दवा दुष्प्रभाव के जोखिम के बिना नहीं है।\n"
            "II. दवाएँ बीमारी से भी बुरी स्थिति उत्पन्न कर देती हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C4,
        "option_d": _D,
        "correct_answer": "A",
    },

    # ── Q55 ──────────────────────────────────────────────────────────────────
    # Source: UP Constable, 27 Jan 2019 Shift-1 | Format: 3-conclusion 4-opt
    # Statements:
    #   I.  Many business offices are in buildings of 3–8 floors.
    #   II. >3 floors → has a lift.
    #   III. All floors may be reached by lifts.
    # Conclusions:
    #   I.  Only floors above 3rd have lifts.     → ✗ (lift serves ALL floors in the building)
    #   II. 7th floors have lifts.                → ✓ (7 > 3 → building has lift; all floors reachable)
    #   III. All business offices accessible by lift → ✗ (3-floor buildings lack lift; 3 is NOT > 3)
    # Answer: B
    {
        "question_number": 55,
        "difficulty": "medium",
        "source_pdf": "UP_Constable_27Jan2019_Shift1",
        "question_en": (
            "Statements:\n"
            "I.  Many business offices are located in buildings having 3 to 8 floors.\n"
            "II. If a building has more than 3 floors, it has a lift.\n"
            "III. All floors may be reached by lifts.\n\n"
            "Conclusions:\n"
            "I.  Only floors above the 3rd floor have lifts.\n"
            "II. 7th floors have lifts.\n"
            "III. All business offices can be accessed by lift."
        ),
        "question_hi": (
            "कथन:\n"
            "I.  कई व्यावसायिक कार्यालय 3 से 8 मंजिल वाली इमारतों में स्थित हैं।\n"
            "II. यदि किसी इमारत में 3 मंजिल से अधिक हों, तो उसमें एक लिफ्ट है।\n"
            "III. सभी मंजिलों पर लिफ्ट द्वारा पहुँचा जा सकता है।\n\n"
            "निष्कर्ष:\n"
            "I.  केवल तीसरी मंजिल के ऊपर की मंजिलों पर लिफ्ट है।\n"
            "II. 7वीं मंजिल पर लिफ्ट है।\n"
            "III. सभी व्यावसायिक कार्यालयों तक लिफ्ट द्वारा पहुँचा जा सकता है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C3,
        "option_d": _D3A,
        "correct_answer": "B",
    },

    # ── Q56 ──────────────────────────────────────────────────────────────────
    # Source: UP Constable, 28 Jan 2019 Shift-2 | Format: 3-conclusion 4-opt
    # Statement: Every man should carry an ID card with blood group, address, phone.
    # I. Blood CANNOT be replaced unless group is on card. → ✗ (too absolute; doctors can test)
    # II. People may forget their phone number.            → ✗ (not implied by statement)
    # III. Police need this info if injury is fatal.       → ✗ (statement is general emergency, not specifically police/fatal)
    # Answer: D
    {
        "question_number": 56,
        "difficulty": "medium",
        "source_pdf": "UP_Constable_28Jan2019_Shift2",
        "question_en": (
            "Statement: Every man should have his identity card with him. That card "
            "should mention his blood group, complete address, and telephone number "
            "for contact in case of emergencies.\n\n"
            "Conclusions:\n"
            "I.  Blood CANNOT be replaced unless its group is mentioned in the card.\n"
            "II. People may forget their own phone number under certain circumstances.\n"
            "III. The police need this information if the injury is fatal."
        ),
        "question_hi": (
            "कथन: प्रत्येक व्यक्ति के पास उसका पहचान पत्र होना चाहिए। उस कार्ड में "
            "आपात स्थिति में संपर्क के लिए रक्त समूह, पूरा पता और फोन नंबर का उल्लेख "
            "होना चाहिए।\n\n"
            "निष्कर्ष:\n"
            "I.  जब तक कार्ड में रक्त समूह का उल्लेख नहीं होगा, रक्त नहीं दिया जा सकता।\n"
            "II. कुछ परिस्थितियों में लोग अपना फोन नंबर भूल सकते हैं।\n"
            "III. यदि चोट घातक हो तो पुलिस को इस जानकारी की आवश्यकता होगी।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C3,
        "option_d": _D3N,
        "correct_answer": "D",
    },

    # ── Q57 ──────────────────────────────────────────────────────────────────
    # Source: UP Constable, 28 Jan 2019 Shift-1 | Format: 3-conclusion 4-opt
    # Statements:
    #   I.  All students in a class are bright.
    #   II. X is NOT bright.
    # Conclusions:
    #   I.  Some students are NOT bright.    → ✗ (contradicts "ALL students bright")
    #   II. X must work hard.                → ✗ (not derivable from premises)
    #   III. X is NOT a student of that class. → ✓ (contrapositive: all students→bright; X not bright ∴ X not student)
    # Answer: C
    {
        "question_number": 57,
        "difficulty": "medium",
        "source_pdf": "UP_Constable_28Jan2019_Shift1",
        "question_en": (
            "Statements:\n"
            "I.  All the students in a class are bright.\n"
            "II. X is NOT bright.\n\n"
            "Conclusions:\n"
            "I.  Some students are NOT bright.\n"
            "II. X must work hard.\n"
            "III. X is NOT a student of that class."
        ),
        "question_hi": (
            "कथन:\n"
            "I.  कक्षा के सभी छात्र प्रतिभाशाली हैं।\n"
            "II. X प्रतिभाशाली नहीं है।\n\n"
            "निष्कर्ष:\n"
            "I.  कुछ छात्र प्रतिभाशाली नहीं हैं।\n"
            "II. X को कड़ी मेहनत करनी चाहिए।\n"
            "III. X उस कक्षा का छात्र नहीं है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C3,
        "option_d": _D3N,
        "correct_answer": "C",
    },

    # ── Q58 ──────────────────────────────────────────────────────────────────
    # Source: ALP, 14 Aug 2018 Shift-2 | Format: 4-opt, no injection
    # Statement: Many people living in villages relocate to cities for a better future.
    # I. Govt officers should have compulsory rural posting. → ✓ (directly addresses rural exodus root cause)
    # II. More transport between cities and villages.        → ✗ (transport ≠ cause of PERMANENT relocation for "better future")
    # Answer: A
    {
        "question_number": 58,
        "difficulty": "medium",
        "source_pdf": "ALP_14Aug2018_Shift2",
        "question_en": (
            "Statement: Many people living in villages relocate to cities for a better future.\n\n"
            "Conclusions:\n"
            "I.  Government officers should have compulsory rural posting.\n"
            "II. More transport facilities should be provided between cities and villages."
        ),
        "question_hi": (
            "कथन: बेहतर भविष्य के लिए गाँवों में रहने वाले बहुत से लोग शहरों में "
            "स्थानांतरित हो जाते हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  सरकारी अधिकारियों की अनिवार्य ग्रामीण पोस्टिंग होनी चाहिए।\n"
            "II. शहरों और गाँवों के बीच अधिक परिवहन सुविधाएँ बढ़ानी चाहिए।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C4,
        "option_d": _D,
        "correct_answer": "A",
    },

    # ── Q59 ──────────────────────────────────────────────────────────────────
    # Source: CHSL Tier-II, 10 Jan 2024 Shift-1 | Format: 4-opt, no injection
    # Statement: All mammals are warm-blooded animals.
    # I. Dogs are warm-blooded animals.          → ✓ (dogs are mammals + all mammals → warm-blooded)
    # II. All warm-blooded creatures are mammals. → ✗ (invalid converse; birds are warm-blooded but not mammals)
    # Answer: A
    {
        "question_number": 59,
        "difficulty": "medium",
        "source_pdf": "CHSL_TierII_10Jan2024_Shift1",
        "question_en": (
            "Statement: All mammals are warm-blooded animals.\n\n"
            "Inferences:\n"
            "I.  Dogs are warm-blooded animals.\n"
            "II. All warm-blooded creatures are mammals."
        ),
        "question_hi": (
            "कथन: सभी स्तनधारी जीव गर्म रक्त वाले जानवर हैं।\n\n"
            "अनुमान:\n"
            "I.  कुत्ते गर्म रक्त वाले जानवर हैं।\n"
            "II. सभी गर्म रक्त वाले प्राणी स्तनधारी हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C4,
        "option_d": _D,
        "correct_answer": "A",
    },

    # ── Q60 ──────────────────────────────────────────────────────────────────
    # Source: CGL Tier-II, 26 Oct 2023 Shift-1 | Format: 4-opt, no injection
    # Statement: Fuel prices in India are inflating day by day with no upper limit.
    # I. Govts have not cut taxes on fuel.      → ✓ (uncontrolled rise implies no govt tax cut intervention)
    # II. International market influencing prices. → ✓ (India imports crude; established fact)
    # Answer: C
    {
        "question_number": 60,
        "difficulty": "medium",
        "source_pdf": "CGL_TierII_26Oct2023_Shift1",
        "question_en": (
            "Statement: Fuel prices in India are inflating day by day, and there is no "
            "upper limit in its price increase.\n\n"
            "Inferences:\n"
            "I.  Central and State governments have not cut down their respective taxes on fuel.\n"
            "II. International market is influencing the rising fuel prices."
        ),
        "question_hi": (
            "कथन: भारत में ईंधन की कीमतें प्रतिदिन बढ़ रही हैं और इसकी कीमत वृद्धि में "
            "कोई ऊपरी सीमा नहीं है।\n\n"
            "अनुमान:\n"
            "I.  केंद्र और राज्य सरकारों ने ईंधन पर अपने-अपने करों में कटौती नहीं की है।\n"
            "II. अंतर्राष्ट्रीय बाजार बढ़ती ईंधन कीमतों को प्रभावित कर रहा है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C4,
        "option_d": _D,
        "correct_answer": "C",
    },

    # ── Q61 ──────────────────────────────────────────────────────────────────
    # Source: CHSL Tier-II, 02 Nov 2023 Shift-1 | Format: 4-opt, no injection
    # Statement: Suresh started practising critical reasoning after hearing about
    #            Ramesh's incredible result in the competitive exam.
    # I. Ramesh scored most marks in critical reasoning.   → ✓ (Suresh chose CR specifically → implies Ramesh excelled in CR)
    # II. Most exam questions are critical reasoning.      → ✗ (no info on question distribution)
    # Answer: A
    {
        "question_number": 61,
        "difficulty": "medium",
        "source_pdf": "CHSL_TierII_02Nov2023_Shift1",
        "question_en": (
            "Statement: Suresh has started practising critical reasoning after hearing about "
            "Ramesh's incredible result in the competitive exam.\n\n"
            "Inferences:\n"
            "I.  Ramesh has scored most of the marks in critical reasoning.\n"
            "II. Most of the questions in the exam constitute critical reasoning."
        ),
        "question_hi": (
            "कथन: सुरेश ने प्रतियोगी परीक्षा में रमेश के अविश्वसनीय परिणाम के बारे में "
            "सुनने के बाद क्रिटिकल रीज़निंग का अभ्यास करना शुरू किया।\n\n"
            "अनुमान:\n"
            "I.  रमेश ने क्रिटिकल रीज़निंग में अधिकांश अंक प्राप्त किए हैं।\n"
            "II. परीक्षा के अधिकांश प्रश्न क्रिटिकल रीज़निंग पर आधारित हैं।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C4,
        "option_d": _D,
        "correct_answer": "A",
    },

    # ── Q62 ──────────────────────────────────────────────────────────────────
    # Source: CHSL Tier-II, 02 Nov 2023 Shift-1 | Format: 4-opt, no injection
    # Statement: Eligibility = 80%+ in 10th board; students who appeared for 10th
    #            this year may also apply.
    # I. No 11th standard students can apply.         → ✗ (11th graders with 80%+ in 10th CAN apply)
    # II. 10th appearing students get admission only if ≥80%. → ✓ (80% threshold applies to them too)
    # Answer: B
    {
        "question_number": 62,
        "difficulty": "medium",
        "source_pdf": "CHSL_TierII_02Nov2023_Shift1",
        "question_en": (
            "Statement: The eligibility for admission to the course is a minimum of 80% marks "
            "in the 10th standard board exams. However, students who have appeared for the "
            "10th standard board exams this year can also apply.\n\n"
            "Conclusions:\n"
            "I.  No 11th standard students can apply for the course.\n"
            "II. Students who have appeared for the 10th standard exams will get admission "
            "only if they score 80% or more."
        ),
        "question_hi": (
            "कथन: पाठ्यक्रम में प्रवेश के लिए पात्रता 10वीं कक्षा की बोर्ड परीक्षाओं में "
            "न्यूनतम 80% अंक है। हालाँकि, जो छात्र इस वर्ष 10वीं कक्षा की बोर्ड परीक्षाओं "
            "में सम्मिलित हुए हैं, वे भी आवेदन कर सकते हैं।\n\n"
            "निष्कर्ष:\n"
            "I.  कोई भी 11वीं कक्षा का छात्र इस पाठ्यक्रम के लिए आवेदन नहीं कर सकता।\n"
            "II. जो छात्र 10वीं कक्षा की परीक्षाओं में सम्मिलित हुए हैं, उन्हें प्रवेश तभी "
            "मिलेगा जब वे 80% या उससे अधिक अंक प्राप्त करें।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C4,
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
