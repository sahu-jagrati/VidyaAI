"""
seed_reasoning_assumptions_sheet5.py
=========================================
Seeds Assumptions Q16-Q20 from Gagan Pratap Reasoning PDFs (Sheet 5).
Subject : Reasoning
Topic   : Assumptions
Run     : python seed_reasoning_assumptions_sheet5.py

Answer key (solutions verified from image tick/cross markings):
  Q16  Statement: Akbar said to his queen, 'Birbal is the wisest man in my kingdom.'
       I)  Akbar is not as wise as Birbal → IMPLICIT (ticked ✓)
           (calling Birbal "the wisest man in the kingdom" implies Akbar himself is less
            wise; the superlative comparison encompasses everyone including the speaker)
       II) Akbar wants Birbal to become the next king → NOT IMPLICIT (crossed ✗)
           ("wisest man" ≠ "next king"; that inference is a huge logical leap not
            supported by the statement)
       Answer: A  (Only I is implicit)
       Source: ALP, 14 Aug 2018, (Shift-2)

  Q17  Statement: If you're a classical dancer we have an exciting job for you.
       I)  We need a classical dancer → IMPLICIT (ticked ✓)
           (the speaker is offering a job to classical dancers, which directly implies they
            have a vacancy / need for a classical dancer)
       II) You are a classical dancer → NOT IMPLICIT (crossed ✗)
           (the statement uses "If you're …" — a conditional; it does not assume the
            listener IS a dancer, only addresses one who might be)
       Answer: C  (Only I is implicit — note: Q17's option (c) says "Only I is implicit")
       Source: ALP, 13 Aug 2018, (Shift-3)

  Q18  Statement: This year in the budget section, there was no fund allotment for
       travel insurance.
       I)  Travel insurance requires funds → IMPLICIT (ticked ✓)
           (the statement discusses "fund allotment" for travel insurance — the very act of
            allotting funds assumes that travel insurance needs funds to function)
       II) There are many other areas that need more financial attention → IMPLICIT (ticked ✓)
           (budget decisions involve prioritisation; choosing NOT to allot funds to travel
            insurance implies the budget was directed to areas deemed more needy — this
            underlying rationale is implicit in the decision)
       Answer: C  (Both I & II are implicit)
       Source: ALP, 13 Aug 2018, (Shift-3)

  Q19  Statement: A flyover has been constructed with a whopping cost of 200 crores,
       yet people are not utilising the flyover much.
       I)  Construction of the flyover is useless → NOT IMPLICIT (crossed ✗)
           ("not utilising much" is an observation; the statement does not conclude the
            construction is "useless" — too strong a label for low usage)
       II) The time, money and energy spent on construction of the flyover was wasted
           → NOT IMPLICIT (crossed ✗)
           (again, low current usage does not mean the investment was "wasted"; the flyover
            may serve future needs or emergency purposes — this inference is extreme)
       Answer: D  (Neither I nor II is implicit)
       Source: ALP, 13 Aug 2018, (Shift-3)

  Q20  Statement: Today is Sunday.
       I)  Tomorrow is Monday → IMPLICIT (ticked ✓)
           (if today is Sunday, tomorrow being Monday is a logical / calendrical certainty;
            this is directly and necessarily implied by the statement)
       II) Today is a holiday → NOT IMPLICIT (crossed ✗)
           (Sunday is not universally a holiday — many people work on Sundays; the
            statement only states the day of the week, not whether it is a holiday)
       Answer: A  (Only I is implicit)
       Source: ALP, 10 Aug 2018, (Shift-2)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Assumptions_Sheet5"
SUBJECT = "Reasoning"
TOPIC   = "Assumptions"

QUESTIONS = [
    # ── Q16 ── Only Assumption I implicit (Akbar–Birbal wisest man) ──────────
    {
        "question_number": 16,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: Akbar said to his queen, 'Birbal is the wisest man in my "
            "kingdom.'\n\n"
            "Assumptions:\n"
            "I.  Akbar is not as wise as Birbal.\n"
            "II. Akbar wants Birbal to become the next king."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: अकबर ने अपनी रानी से कहा, 'बीरबल मेरे राज्य का सबसे बुद्धिमान "
            "व्यक्ति है।'\n\n"
            "पूर्वानुमान:\n"
            "I.  अकबर बीरबल जितना बुद्धिमान नहीं है।\n"
            "II. अकबर चाहता है कि बीरबल अगला राजा बने।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "A",
        # I: "wisest man in my kingdom" — the speaker is part of the kingdom, so Birbal
        #    is wiser than Akbar too → IMPLICIT ✓
        # II: wisest man ≠ next king; the inference about kingship is an unjustified leap
        #    → NOT IMPLICIT ✗
    },
    # ── Q17 ── Only Assumption I implicit (classical dancer job offer) ────────
    # NOTE: In the original PDF the option order for Q17 is non-standard:
    #   (a) Neither I nor II   (b) Only II   (c) Only I ← answer   (d) Both
    # We store options in the standard order below; correct_answer = C
    {
        "question_number": 17,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: If you're a classical dancer we have an exciting job for you.\n\n"
            "Assumptions:\n"
            "I.  We need a classical dancer.\n"
            "II. You are a classical dancer."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: यदि आप एक शास्त्रीय नृत्यांगना हैं तो हमारे पास आपके लिए एक "
            "रोमांचक काम है।\n\n"
            "पूर्वानुमान:\n"
            "I.  हमें एक शास्त्रीय नृत्यांगना की जरूरत है।\n"
            "II. आप शास्त्रीय नृत्यांगना हैं।"
        ),
        "option_a": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Only I is implicit / केवल I अंतर्निहित है",
        "option_d": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "correct_answer": "C",
        # I: offering a job to classical dancers implies a vacancy / need exists → IMPLICIT ✓
        # II: "If you're a dancer …" is a conditional — does NOT assume the listener IS a
        #    dancer; it only addresses the possibility → NOT IMPLICIT ✗
    },
    # ── Q18 ── Both assumptions implicit (no travel insurance budget allotment) ─
    # NOTE: In the original PDF Q18 options:
    #   (a) Only I   (b) Either I or II   (c) Both I & II ← answer   (d) Only II
    {
        "question_number": 18,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: This year in the budget section, there was no fund allotment "
            "for travel insurance.\n\n"
            "Assumptions:\n"
            "I.  Travel insurance requires funds.\n"
            "II. There are many other areas that need more financial attention."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: इस वर्ष बजट अनुभाग में यात्रा बीमा के लिए कोई निधि आवंटन नहीं "
            "किया गया।\n\n"
            "पूर्वानुमान:\n"
            "I.  यात्रा बीमा के लिए धन की आवश्यकता होती है।\n"
            "II. ऐसे कई अन्य क्षेत्र हैं जिन पर अधिक वित्तीय ध्यान देने की "
            "आवश्यकता है।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Either I or II is implicit / I या II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Only II is implicit / केवल II अंतर्निहित है",
        "correct_answer": "C",
        # I: discussing "no fund allotment" for travel insurance assumes it needs funds
        #    → IMPLICIT ✓
        # II: NOT allotting funds implies they were directed to more financially needy areas
        #    — the prioritisation is an underlying rationale → IMPLICIT ✓
    },
    # ── Q19 ── Neither assumption implicit (200-crore flyover under-utilised) ───
    {
        "question_number": 19,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: A flyover has been constructed with a whopping cost of 200 "
            "crores, yet people are not utilising the flyover much.\n\n"
            "Assumptions:\n"
            "I.  Construction of the flyover is useless.\n"
            "II. The time, money and energy spent on the construction of the flyover "
            "was wasted."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: 200 करोड़ रुपये की लागत से एक फ्लाईओवर का निर्माण किया गया है, "
            "फिर भी लोग फ्लाईओवर का अधिक उपयोग नहीं कर रहे हैं।\n\n"
            "पूर्वानुमान:\n"
            "I.  फ्लाईओवर का निर्माण व्यर्थ है।\n"
            "II. फ्लाईओवर के निर्माण पर खर्च किया गया समय, पैसा और ऊर्जा बर्बाद "
            "हो गई।"
        ),
        "option_a": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Only I is implicit / केवल I अंतर्निहित है",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "D",
        # I: "not utilising much" ≠ "useless"; the flyover may serve emergency/future
        #    needs — "useless" is too extreme a label → NOT IMPLICIT ✗
        # II: low current usage does not mean the investment was "wasted"; infrastructure
        #    value may materialise over time → NOT IMPLICIT ✗
    },
    # ── Q20 ── Only Assumption I implicit (Today is Sunday) ───────────────────
    {
        "question_number": 20,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: Today is Sunday.\n\n"
            "Assumptions:\n"
            "I.  Tomorrow is Monday.\n"
            "II. Today is a holiday."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: आज रविवार है।\n\n"
            "पूर्वानुमान:\n"
            "I.  कल सोमवार है।\n"
            "II. आज छुट्टी है।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "option_d": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "correct_answer": "A",
        # I: if today is Sunday, tomorrow is Monday — a calendrical certainty → IMPLICIT ✓
        # II: Sunday is not universally a holiday (many work on Sundays); the statement
        #    only states the day, not its work/holiday status → NOT IMPLICIT ✗
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
