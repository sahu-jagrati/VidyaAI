"""
seed_reasoning_analytical_sheet6.py
=========================================
Seeds Analytical Reasoning Q21-Q26 from Gagan Pratap Reasoning PDFs (Sheet 6).
Subject : Reasoning
Topic   : Analytical Reasoning
Run     : python seed_reasoning_analytical_sheet6.py

NOTE:
  Q22 shares its statement with Q18 ("bear your travel expenses" letter) —
   they come from different practice sets in the PDF, same statement, same answer.

Answer key (solutions verified):
  Q21  Statement: Postal rates have been increased to meet the deficit.
       I)  The present rates are very low → NOT IMPLICIT
           (raising rates to cover a deficit does not imply current rates are
            low in absolute terms — they may be reasonable but insufficient)
       II) If rates are not increased, the deficit cannot be met → IMPLICIT
           (choosing to raise rates specifically to address the deficit assumes
            this is the necessary method to cover it)
       Answer: B  (Only assumption II is implicit)

  Q22  Statement: Letter to exam candidates — "You have to bear your expenses on travel etc."
       (Same statement as Q18 — different practice set)
       I)  If not clarified, candidates may claim reimbursement → IMPLICIT
       II) Many organisations reimburse travel expenses for exam candidates → IMPLICIT
       Answer: D  (Both I and II are implicit)

  Q23  Statement: Pure ghee is good for health.
       I)  All healthy people take ghee → NOT IMPLICIT
           (extreme generalisation; "good for health" does not mean every healthy
            person consumes ghee)
       II) Sweets with pure ghee are good for health → NOT IMPLICIT
           (ghee alone being healthy does not make ghee-containing sweets healthy overall —
            sugar and other ingredients can negate the benefit)
       Answer: D  (Neither assumption is implicit)

  Q24  Statement: A notice reads "Please do not photocopy this book without my permission."
       I)  It is possible to photocopy the book → IMPLICIT
           (prohibiting an action assumes the action is physically possible)
       II) This warning implicates punishment for people violating it → NOT IMPLICIT
           (the notice is a request/prohibition, not an explicit declaration of legal
            penalty or punishment)
       Answer: A  (Only assumption I is implicit)

  Q25  Statement: Book reading must be encouraged at a young age as it provides
       comprehensive and detailed information about a given issue.
       I)  Books are the best resource for complete knowledge and learning → NOT IMPLICIT
           (extrapolating to "the best resource" goes beyond the statement's scope)
       II) Reading helps to improve focus and analytical thinking → IMPLICIT
           (the statement highlights comprehensive/detailed information which directly
            supports cognitive development: focus and analytical thinking)
       Answer: B  (Only assumption II is strong/implicit)

  Q26  Argument: Hindi ought to be the official language of India. There is no reason
       for the government to spend money printing documents in different languages
       just to cater to people who cannot read/write Hindi. The government has better
       ways to spend taxpayers' money. People across India should read/write Hindi or
       learn it at the earliest.
       Question: Which of the following, if true, weakens the speaker's argument most?
       Answer: C  (People who are multilingual usually pay maximum taxes)
       Reasoning: The speaker argues government should not "waste" taxpayers' money
       serving non-Hindi speakers. If multilingual people (who speak other languages too)
       pay the most taxes, then government expenditure to serve them in their languages
       is entirely justified by their own tax contributions — directly undermining the
       "wasteful spending on non-Hindi speakers" premise.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Analytical_Sheet6"
SUBJECT = "Reasoning"
TOPIC   = "Analytical Reasoning"

QUESTIONS = [
    # ── Q21 ── Only Assumption II implicit (postal rates and deficit) ─────────
    {
        "question_number": 21,
        "difficulty": "easy",
        "question_en": (
            "Study the following questions carefully and choose the right answer.\n\n"
            "Statement: Postal rates have been increased to meet the deficit.\n\n"
            "Assumptions:\n"
            "I.  The present rates are very low.\n"
            "II. If the rates are not increased, the deficit cannot be met."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों का सावधानीपूर्वक अध्ययन करें और सही उत्तर चुनें।\n\n"
            "कथन: घाटे को पूरा करने के लिए डाक दरों में वृद्धि की गई है।\n\n"
            "अनुमान:\n"
            "I.  वर्तमान दरें बहुत कम हैं।\n"
            "II. यदि दरें नहीं बढ़ाई जाती हैं, तो घाटे को पूरा नहीं किया जा सकता।"
        ),
        "option_a": "If only assumption I is implicit / यदि केवल अनुमान I अंतर्निहित है",
        "option_b": "If only assumption II is implicit / यदि केवल अनुमान II अंतर्निहित है",
        "option_c": "If either I or II is implicit / यदि I या II में से कोई एक अंतर्निहित है",
        "option_d": "If neither I nor II is implicit / यदि न तो I और न ही II अंतर्निहित है",
        "correct_answer": "B",
        # I: raising rates ≠ current rates are low in absolute terms → NOT IMPLICIT ✗
        # II: increasing rates specifically to meet deficit → rates are the necessary fix → IMPLICIT ✓
    },
    # ── Q22 ── Both assumptions implicit (travel expenses letter, same as Q18) ─
    {
        "question_number": 22,
        "difficulty": "medium",
        "question_en": (
            "Study the following questions carefully and choose the right answer.\n\n"
            "Statement: A sentence in the letter to the candidates called for written "
            "examinations — 'You have to bear your expenses on travel etc.'\n\n"
            "Assumptions:\n"
            "I.  If not clarified, all the candidates may claim reimbursement of "
            "expenses.\n"
            "II. Many organisations reimburse expenses on travel to candidates called "
            "for written examinations."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों का सावधानीपूर्वक अध्ययन करें और सही उत्तर चुनें।\n\n"
            "कथन: लिखित परीक्षाओं के लिए बुलाए गए अभ्यर्थियों को पत्र में एक वाक्य "
            "— 'आपको यात्रा आदि पर होने वाले खर्च स्वयं वहन करने होंगे।'\n\n"
            "अनुमान:\n"
            "I.  यदि स्पष्ट नहीं किया गया, तो सभी अभ्यर्थी खर्च की प्रतिपूर्ति का "
            "दावा कर सकते हैं।\n"
            "II. कई संगठन लिखित परीक्षाओं के लिए बुलाए गए अभ्यर्थियों की यात्रा पर "
            "खर्च की प्रतिपूर्ति करते हैं।"
        ),
        "option_a": "If only assumption I is implicit / यदि केवल अनुमान I अंतर्निहित है",
        "option_b": "If only assumption II is implicit / यदि केवल अनुमान II अंतर्निहित है",
        "option_c": "If either I or II is implicit / यदि I या II में से कोई एक अंतर्निहित है",
        "option_d": "If both I and II are implicit / यदि I और II दोनों अंतर्निहित हैं",
        "correct_answer": "D",
        # Same reasoning as Q18: clarification was needed because...
        # I: candidates might expect reimbursement → IMPLICIT ✓
        # II: many orgs do reimburse → that expectation is reasonable → IMPLICIT ✓
    },
    # ── Q23 ── Neither assumption implicit (pure ghee and health) ────────────
    {
        "question_number": 23,
        "difficulty": "medium",
        "question_en": (
            "In each of the questions below is a given statement followed by two "
            "arguments/assumptions numbered I and II. Consider the arguments/assumptions "
            "and decide which is correct.\n\n"
            "Statement: Pure ghee is good for health.\n\n"
            "Assumptions:\n"
            "I.  All healthy people take ghee.\n"
            "II. Sweets with pure ghee are good for health."
        ),
        "question_hi": (
            "नीचे दिए गए प्रत्येक प्रश्न में एक कथन के बाद दो तर्क/धारणाएँ I और II "
            "दी गई हैं। तर्क/धारणाओं पर विचार कीजिए और निर्णय लीजिए कि कौन सी सही है।\n\n"
            "कथन: शुद्ध घी स्वास्थ्य के लिए अच्छा है।\n\n"
            "धारणाएँ:\n"
            "I.  सभी स्वस्थ लोग घी लेते हैं।\n"
            "II. शुद्ध घी वाली मिठाइयाँ स्वास्थ्य के लिए अच्छी होती हैं।"
        ),
        "option_a": "Both of the assumptions are implicit / दोनों धारणाएँ अंतर्निहित हैं",
        "option_b": "If only assumption II is implicit / यदि केवल धारणा II अंतर्निहित है",
        "option_c": "If only assumption I is implicit / यदि केवल धारणा I अंतर्निहित है",
        "option_d": "Neither assumption I nor II is implicit / न तो धारणा I और न ही II अंतर्निहित है",
        "correct_answer": "D",
        # I: "all healthy people take ghee" — extreme generalisation, not supported → NOT IMPLICIT ✗
        # II: ghee alone being healthy ≠ ghee-containing sweets (with sugar etc.) are healthy → NOT IMPLICIT ✗
    },
    # ── Q24 ── Only Assumption I implicit (photocopy notice) ──────────────────
    {
        "question_number": 24,
        "difficulty": "easy",
        "question_en": (
            "Study the following questions carefully and choose the right answer.\n\n"
            "Statement: A notice reads 'Please do not photocopy this book without my "
            "permission'.\n\n"
            "Assumptions:\n"
            "I.  It is possible to photocopy the book.\n"
            "II. This warning implicates punishment for people violating it."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों का सावधानीपूर्वक अध्ययन करें और सही उत्तर चुनें।\n\n"
            "कथन: एक नोटिस में लिखा है 'कृपया मेरी अनुमति के बिना इस पुस्तक की "
            "फोटोकॉपी न करें।'\n\n"
            "अनुमान:\n"
            "I.  पुस्तक की फोटोकॉपी करना संभव है।\n"
            "II. यह चेतावनी इसका उल्लंघन करने वाले लोगों के लिए दंड का प्रावधान "
            "करती है।"
        ),
        "option_a": "If only assumption I is implicit / यदि केवल अनुमान I अंतर्निहित है",
        "option_b": "If only assumption II is implicit / यदि केवल अनुमान II अंतर्निहित है",
        "option_c": "Both assumptions are implicit / दोनों अनुमान अंतर्निहित हैं",
        "option_d": "Neither assumption I nor II is implicit / न तो अनुमान I और न ही II अंतर्निहित है",
        "correct_answer": "A",
        # I: prohibiting an action assumes it is physically possible to perform → IMPLICIT ✓
        # II: notice is a polite request/prohibition, NOT an explicit declaration of punishment → NOT IMPLICIT ✗
    },
    # ── Q25 ── Only Assumption II strong (book reading at young age) ──────────
    {
        "question_number": 25,
        "difficulty": "medium",
        "question_en": (
            "In each of the questions below is a given statement followed by two "
            "arguments/assumptions numbered I and II. Consider the arguments/assumptions "
            "and decide which is correct.\n\n"
            "Statement: Book reading must be encouraged at a young age as it provides "
            "comprehensive and detailed information about a given issue.\n\n"
            "Assumptions:\n"
            "I.  Books are the best resource for complete knowledge and learning.\n"
            "II. Reading helps to improve focus and analytical thinking."
        ),
        "question_hi": (
            "नीचे दिए गए प्रत्येक प्रश्न में एक कथन के बाद दो तर्क/धारणाएँ I और II "
            "दी गई हैं। तर्क/धारणाओं पर विचार कीजिए और निर्णय लीजिए कि कौन सी सही है।\n\n"
            "कथन: कम उम्र में पुस्तक पढ़ना चाहिए क्योंकि यह किसी दिए गए मुद्दे के "
            "बारे में व्यापक और विस्तृत जानकारी प्रदान करता है।\n\n"
            "धारणाएँ:\n"
            "I.  पुस्तकें संपूर्ण ज्ञान और सीखने के लिए सबसे अच्छा स्रोत हैं।\n"
            "II. पढ़ना फोकस और विश्लेषणात्मक चिंतन को बेहतर बनाने में मदद करता है।"
        ),
        "option_a": "Only Assumption I is strong / केवल पूर्वधारणा I मजबूत है",
        "option_b": "Only Assumption II is strong / केवल पूर्वधारणा II मजबूत है",
        "option_c": "Both assumptions are strong / दोनों पूर्वधारणाएं मजबूत हैं",
        "option_d": "Neither assumption I nor II is strong / न तो पूर्वधारणा I और न ही II मजबूत है",
        "correct_answer": "B",
        # I: "best resource" is an extreme claim beyond the statement's scope → NOT strong ✗
        # II: comprehensive & detailed info → directly implies improved focus/analytical thinking → STRONG ✓
    },
    # ── Q26 ── Weaken the argument (Hindi as official language) ──────────────
    {
        "question_number": 26,
        "difficulty": "hard",
        "question_en": (
            "Hindi ought to be the official language of India. There is no reason of "
            "the government to spend money printing documents in different languages, "
            "just to cater to people who cannot read/write Hindi. The government has "
            "better ways to spend tax payers' money. People across India should "
            "read/write Hindi or learn it at the earliest.\n\n"
            "In the following, if true, which of the following weakens the speaker's "
            "argument the most?"
        ),
        "question_hi": (
            "हिंदी को भारत की आधिकारिक भाषा होनी चाहिए। सरकार को अलग-अलग भाषाओं में "
            "पैसे खर्च करने की कोई जरूरत नहीं है, सिर्फ उन लोगों की जरूरतें पूरी करने "
            "के लिए जो हिंदी पढ़ / लिख नहीं सकते। सरकार के पास करदाताओं के पैसे खर्च "
            "करने के बेहतर तरीके हैं। पूरे भारत में लोगों को हिंदी पढ़/लिखनी चाहिए "
            "या जल्द से जल्द इसे सीखना चाहिए।\n\n"
            "निम्नलिखित में से कौन सा तर्क, यदि सत्य है, तो वक्ता के तर्क को सबसे "
            "अधिक कमजोर करता है?"
        ),
        "option_a": "The government currently translates official documents into more official languages than government employees can read or write / सरकार वर्तमान में उससे अधिक भाषाओं में सरकारी दस्तावेजों का अनुवाद करती है जितनी सरकारी कर्मचारी पढ़ या लिख सकते हैं",
        "option_b": "Hindi is the most difficult language in the world / हिंदी दुनिया की सबसे कठिन भाषा है",
        "option_c": "People who are multilingual usually pay maximum taxes / बहुभाषी लोग आमतौर पर अधिकतम कर देते हैं",
        "option_d": "Most people who travel across India learn Hindi within five years / भारत में पाँच वर्षों के भीतर यात्रा करने वाले अधिकांश लोग हिंदी सीख लेते हैं",
        "correct_answer": "C",
        # Speaker's premise: spending money on non-Hindi documents "wastes" taxpayers' money.
        # C: multilingual (non-Hindi-only) people pay the most taxes → government is obligated
        #    to serve these top taxpayers in their languages → directly undermines the premise ✓
        # A: about translation volume vs employee literacy — tangential, not a direct weakener ✗
        # B: Hindi being difficult actually weakens the "everyone should learn Hindi" claim
        #    but does not directly attack the taxpayer-money premise ✗ (weaker than C)
        # D: supports the "learn Hindi" idea → actually strengthens the argument ✗
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
