"""
seed_reasoning_assumptions_sheet3.py
=========================================
Seeds Assumptions Q7-Q10 from Gagan Pratap Reasoning PDFs (Sheet 3).
Subject : Reasoning
Topic   : Assumptions
Run     : python seed_reasoning_assumptions_sheet3.py

Answer key (solutions verified):
  Q7   Statement: Because of the large number of potholes in road X, reaching
       airport in time has become difficult.
       I)  Reaching airport in time may not be always necessary → NOT IMPLICIT
           (contradicts the statement's expressed concern about reaching in time)
       II) There is no other convenient road to the airport → IMPLICIT
           (if another convenient road existed, potholes in road X would not make
            reaching the airport difficult — the statement implies X is the only route)
       Answer: B  (Only II is implicit)

  Q8   Statement: Why don't you go to the court if the employer does not pay you
       the Provident Fund contribution?
       I)  Courts can intervene in matters of dispute between employer and employees
           → IMPLICIT (suggesting court implies courts can handle such disputes)
       II) It is obligatory for the employer to pay the Provident Fund contribution
           → IMPLICIT (going to court for non-payment assumes it is legally mandatory;
            otherwise there would be no legal basis for the case)
       Answer: C  (Both I & II are implicit)

  Q9   Statement: Weapon inspectors of country 'X' could not detect the presence of
       chemical weapons in the custody of country 'Y'.
       I)  Country 'X' allowed the weapon inspectors of country 'Y' to inspect weapons
           → NOT IMPLICIT (the statement says X's inspectors went to Y, not Y's
           inspectors to X — this assumption reverses the direction)
       II) Presence of chemical weapons cannot be detected → NOT IMPLICIT
           (the statement says X's inspectors failed to detect, not that detection is
            fundamentally impossible — it is a specific failure, not a general rule)
       Answer: D  (Neither I nor II is implicit)

  Q10  Statement: It is desirable for the child to enter school at the age of 5.
       I)  At that age the child reaches the appropriate level of development and is
           ready to learn → IMPLICIT
           (recommending age 5 as desirable assumes children are developmentally
            ready to learn at that age)
       II) Schools do not admit children after the age of 6 years → NOT IMPLICIT
           (this is an external factual claim not implied by the statement; the
            statement says "desirable", not "last chance" or "mandatory")
       Answer: A  (Only I is implicit)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Assumptions_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Assumptions"

QUESTIONS = [
    # ── Q7 ── Only Assumption II implicit (potholes on road X to airport) ─────
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: Because of the large number of potholes in the road X, "
            "reaching airport in time has become difficult.\n\n"
            "Assumptions:\n"
            "I.  Reaching airport in time may not be always necessary.\n"
            "II. There is no other convenient road to the airport."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: मार्ग 'X' में अधिक संख्या में गढ्ढे होने के कारण निर्धारित समय पर "
            "हवाई अड्डा पहुँचना मुश्किल हो गया है।\n\n"
            "पूर्वानुमान:\n"
            "I.  निर्धारित समय पर हवाई अड्डा पहुँचना हमेशा जरूरी नहीं होता है।\n"
            "II. हवाई अड्डे तक और दूसरा कोई आसान/सुविधाजनक मार्ग नहीं है।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "B",
        # I: directly contradicts the statement's expressed concern about reaching in time → NOT IMPLICIT ✗
        # II: if an alternate route existed, potholes in X would not be the problem →
        #    difficulty implies X is the only/main route to the airport → IMPLICIT ✓
    },
    # ── Q8 ── Both assumptions implicit (Provident Fund and court) ────────────
    {
        "question_number": 8,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: Why don't you go to the court if the employer does not pay "
            "you the Provident Fund contribution?\n\n"
            "Assumptions:\n"
            "I.  Courts can intervene in matters of dispute between employer and "
            "employees.\n"
            "II. It is obligatory for the employer to pay the Provident Fund "
            "contribution to the employees."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: यदि नियोक्ता आपको भविष्य निधि के अंशदान का भुगतान नहीं करता है, "
            "तब आप न्यायालय के पास क्यों नहीं जाते?\n\n"
            "पूर्वानुमान:\n"
            "I.  नियोक्ता और कर्मचारियों में यदि विवाद हो, तब न्यायालय हस्तक्षेप "
            "करते हैं।\n"
            "II. नियोक्ता के लिए कर्मचारियों को भविष्य निधि के अंशदान का भुगतान "
            "करना अनिवार्य है।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "C",
        # I: advising someone to go to court assumes court can handle this dispute → IMPLICIT ✓
        # II: going to court for non-payment assumes the employer is legally obligated to
        #    pay; otherwise there is no legal basis for the case → IMPLICIT ✓
    },
    # ── Q9 ── Neither assumption implicit (chemical weapons inspection X→Y) ────
    {
        "question_number": 9,
        "difficulty": "hard",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: Weapon inspectors of country 'X' could not detect the presence "
            "of chemical weapons in the custody of country 'Y'.\n\n"
            "Assumptions:\n"
            "I.  Country 'X' allowed the weapon inspectors of country 'Y' to inspect "
            "weapons.\n"
            "II. Presence of chemical weapons cannot be detected."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: 'X' देश के शस्त्र निरीक्षक, 'Y' देश के सभी रासायनिक हथियारों की "
            "उपस्थिति का पता नहीं लगा पाये।\n\n"
            "पूर्वानुमान:\n"
            "I.  'X' देश ने 'Y' देश के हथियार निरीक्षकों को हथियारों के निरीक्षण की "
            "अनुमति दी।\n"
            "II. रासायनिक हथियारों की उपस्थिति का पता नहीं लगाया जा सकता।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "D",
        # I: reverses the direction — statement says X's inspectors went to Y, not Y's
        #    inspectors to X; this assumption is factually backwards → NOT IMPLICIT ✗
        # II: the statement says X's inspectors failed to detect, not that detection is
        #    fundamentally impossible — it is a specific failure → NOT IMPLICIT ✗
    },
    # ── Q10 ── Only Assumption I implicit (school entry age 5) ───────────────
    {
        "question_number": 10,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: It is desirable for the child to enter the school at the age "
            "of 5.\n\n"
            "Assumptions:\n"
            "I.  At that age the child reaches the appropriate level of development "
            "and is ready to learn.\n"
            "II. Schools do not admit children after the age of 6 years."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: बालक को 5 या उसके लगभग अवस्था पर विद्यालय में प्रवेश करना वांछनीय।\n\n"
            "पूर्वानुमान:\n"
            "I.  उस आयु अवस्था पर बालक विकास के उचित स्तर पर पहुँच जाता है और "
            "सीखने के लिए तत्पर होता है।\n"
            "II. विद्यालय 6 वर्ष की आयु के पश्चात् बच्चों को दाखिल नहीं करते।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "A",
        # I: recommending age 5 as desirable assumes children are developmentally ready
        #    to learn at that age → IMPLICIT ✓
        # II: external factual claim about school admission policy; not implied by
        #    "desirable" — the statement does not suggest it is the last chance → NOT IMPLICIT ✗
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
