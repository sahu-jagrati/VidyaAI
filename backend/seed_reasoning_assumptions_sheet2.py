"""
seed_reasoning_assumptions_sheet2.py
=========================================
Seeds Assumptions Q3-Q6 from Gagan Pratap Reasoning PDFs (Sheet 2).
Subject : Reasoning
Topic   : Assumptions
Run     : python seed_reasoning_assumptions_sheet2.py

Answer key (solutions verified):
  Q3   Statement: The employee's association urged its members to stay away from the
       annual function as many of their demands were not met by the management.
       I)  Majority of members may not attend the function → IMPLICIT
           (urging members to stay away assumes they will comply with the call)
       II) The management may cancel the annual function → NOT IMPLICIT
           (cancellation is a separate management decision, not implied by the
            association's boycott call)
       Answer: A  (Only I is implicit)

  Q4   Statement: The Sarpanch of the village called a meeting of all heads of
       families to discuss the problem of acute shortage of drinking water.
       I)  The Sarpanch had earlier called such meetings to discuss various problems
           → NOT IMPLICIT (past meetings are not assumed; this is a fresh situation)
       II) Most of the heads of families may attend the meeting called by Sarpanch
           → IMPLICIT (calling a meeting assumes people will attend; otherwise
           calling the meeting would be pointless)
       Answer: B  (Only II is implicit)

  Q5   Statement: The district authority has decided to set up wireless communication
       along the coastline in view of the cyclonic storm hitting the coast.
       I)  The telephone communication may be paralysed due to cyclonic storm → IMPLICIT
           (setting up wireless as an alternative assumes regular telephone may fail)
       II) The wireless communication systems may be able to withstand the impact of
           the cyclonic storm → IMPLICIT
           (setting up wireless assumes it will remain functional during the storm;
            otherwise there is no point in establishing it)
       Answer: C  (Both I & II are implicit)

  Q6   Statement: The Government of India has appointed a Joint Parliamentary Committee
       to investigate the recent market crash.
       I)  The members of the committee may possess requisite expertise to carry out
           the investigation → IMPLICIT
           (appointing a committee to investigate assumes it has the necessary expertise)
       II) The people responsible for the crash may destroy all their documents before
           the committee lay their hands on them → NOT IMPLICIT
           (possible concern, but the government would not appoint a committee on the
            assumption that evidence will be destroyed; this is speculative, not assumed)
       Answer: A  (Only I is implicit)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Assumptions_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Assumptions"

QUESTIONS = [
    # ── Q3 ── Only Assumption I implicit (employee association boycott) ────────
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: The employee's association urged its members to stay away from "
            "the annual function as many of their demands were not met by the "
            "management.\n\n"
            "Assumptions:\n"
            "I.  Majority of the members of the association may not attend the "
            "function.\n"
            "II. The management may cancel the annual function."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: कर्मचारी संघ ने अपने सदस्यों को वार्षिक कार्यक्रम से दूर रहने के "
            "लिए कहा है क्योंकि प्रबंधन ने उनकी कई मांगें नहीं मानी थीं।\n\n"
            "पूर्वानुमान:\n"
            "I.  हो सकता है संघ के अधिकांश सदस्य कार्यक्रम में भाग न लें।\n"
            "II. हो सकता है प्रबंधन वार्षिक कार्यक्रम को रद्द कर दे।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "A",
        # I: urging members to stay away assumes they will comply → IMPLICIT ✓
        # II: management cancelling the function is a separate, unrelated decision → NOT IMPLICIT ✗
    },
    # ── Q4 ── Only Assumption II implicit (Sarpanch meeting on water shortage) ─
    {
        "question_number": 4,
        "difficulty": "easy",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: The Sarpanch of the village called a meeting of all the heads "
            "of the families to discuss the problem of acute shortage of drinking water "
            "in the village.\n\n"
            "Assumptions:\n"
            "I.  The Sarpanch had earlier called such meetings to discuss various "
            "problems.\n"
            "II. Most of the heads of families may attend the meeting called by the "
            "Sarpanch."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: गांव में पीने की पानी की कमी की गंभीर समस्या पर चर्चा करने के लिए "
            "गांव के सरपंच ने सभी परिवारों के मुखिया की बैठक बुलाई।\n\n"
            "पूर्वानुमान:\n"
            "I.  विभिन्न समस्याओं के बारे में चर्चा करने के लिए सरपंच ने ऐसी बैठकें "
            "पहले भी बुलाई थीं।\n"
            "II. हो सकता है अधिकांश परिवारों के मुखिया सरपंच द्वारा बुलाई गई बैठक "
            "में भाग लें।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "B",
        # I: past meetings are not assumed — this is a specific new situation → NOT IMPLICIT ✗
        # II: calling a meeting assumes people will attend; pointless otherwise → IMPLICIT ✓
    },
    # ── Q5 ── Both assumptions implicit (wireless communication on coastline) ──
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: The district authority has decided to set up wireless "
            "communication along the coastline in view of the cyclonic storm hitting "
            "the coast.\n\n"
            "Assumptions:\n"
            "I.  The telephone communication may be paralysed due to cyclonic storm.\n"
            "II. The wireless communication systems may be able to withstand the "
            "impact of the cyclonic storm."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: चक्रवाती तूफानों से सागर तटों के प्रभावित होने को मद्देनजर रखते हुए "
            "जिला प्रशासन ने तटवर्ती क्षेत्रों में बेतार संचार प्रणाली की स्थापना का "
            "निर्णय लिया है।\n\n"
            "पूर्वानुमान:\n"
            "I.  चक्रवाती तूफानों के कारण दूरभाषीय सम्पर्क व्यवस्था भंग हो सकती है।\n"
            "II. बेतार संचार प्रणाली चक्रवाती तूफान के आघात को सहने में सक्षम हो "
            "सकती है।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "C",
        # I: setting up wireless as alternative assumes telephone will fail → IMPLICIT ✓
        # II: establishing wireless assumes it can withstand the storm; else pointless → IMPLICIT ✓
    },
    # ── Q6 ── Only Assumption I implicit (JPC to investigate market crash) ─────
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": (
            "In the question below is given a statement followed by two assumptions "
            "numbered I and II. Consider the statement and the following assumptions "
            "and decide which of the assumption(s) is/are implicit in the given "
            "statement.\n\n"
            "Statement: The Government of India has appointed a Joint Parliamentary "
            "Committee to investigate the recent market crash.\n\n"
            "Assumptions:\n"
            "I.  The members of the committee may possess requisite expertise to carry "
            "out the investigation.\n"
            "II. The people responsible for the crash may destroy all their documents "
            "before the committee lay their hands on them."
        ),
        "question_hi": (
            "नीचे दिए गए प्रश्न में एक कथन के बाद दो पूर्वानुमान I और II दिए गए हैं। "
            "कथन और निम्नलिखित पूर्वानुमानों पर विचार करें और निर्णय लें कि दिए गए "
            "कथन में कौन सा/से पूर्वानुमान अंतर्निहित है/हैं।\n\n"
            "कथन: हाल ही में स्टॉक एक्सचेंज मार्केट में आई जबरदस्त गिरावट की जांच के "
            "लिए भारत सरकार ने एक संयुक्त संसदीय समिति का गठन किया है।\n\n"
            "पूर्वानुमान:\n"
            "I.  समिति के सदस्यों में जांच करने की अपेक्षित विशेषज्ञता हो सकती है।\n"
            "II. इसके पूर्व समिति उन दस्तावेजों पर कब्जा करे, हो सकता है उक्त गिरावट "
            "के लिए जिम्मेदार लोग अपने सभी दस्तावेज को नष्ट कर सकते हैं।"
        ),
        "option_a": "Only I is implicit / केवल I अंतर्निहित है",
        "option_b": "Only II is implicit / केवल II अंतर्निहित है",
        "option_c": "Both I & II are implicit / I और II दोनों अंतर्निहित हैं",
        "option_d": "Neither I nor II is implicit / न तो I और न ही II अंतर्निहित है",
        "correct_answer": "A",
        # I: appointing a committee assumes it has expertise to do the job → IMPLICIT ✓
        # II: government wouldn't appoint a committee assuming evidence will be destroyed;
        #    this is speculative fear, not an underlying assumption → NOT IMPLICIT ✗
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
