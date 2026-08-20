"""
seed_reasoning_statement_assumption_sheet1.py
=============================================
Seeds Statement-Assumption Q1–Q5 from Gagan Pratap Reasoning PDFs (Sheet 1).
Subject : Reasoning
Topic   : Statement Assumption and Conclusion

Fixed 4-option format — same options for every question:
  (A) Only Assumption I is implicit.
  (B) Only Assumption II is implicit.
  (C) Both I & II are implicit.
  (D) Neither I nor II is implicit.

No 5th option injection needed.

Answer key:
  Q1  D — Municipal corporation announces 50% water supply cut till monsoon.
            Assumption I:   People may protest the unilateral decision → NOT implicit
                            (possible reaction, not embedded in the announcement)
            Assumption II:  Corp may reduce charges for failing to provide water
                            → NOT implicit (financial compensation is not assumed
                            anywhere in the announcement)
            Neither I nor II is implicit.

  Q2  A — Railway police imposed heavy penalty on people crossing tracks.
            Assumption I:   People may refrain from crossing tracks in future
                            → IMPLICIT ✓ (the whole purpose of imposing a penalty
                            is deterrence; the action assumes future compliance)
            Assumption II:  People may continue crossing and keep paying penalty
                            → NOT implicit (this contradicts the purpose of the
                            penalty; the authority acts assuming the opposite)
            Only Assumption I is implicit.

  Q3  A — Employee association urges members to boycott annual function because
           management did not meet their demands.
            Assumption I:   Majority of members may not attend the function
                            → IMPLICIT ✓ (urging a boycott assumes members will
                            follow the call; otherwise the urge would be pointless)
            Assumption II:  Management may cancel the annual function
                            → NOT implicit (boycott is meant to pressure management,
                            but management cancelling is not assumed by the action)
            Only Assumption I is implicit.

  Q4  B — Sarpanch calls a meeting of all family heads to discuss acute drinking
           water shortage in the village.
            Assumption I:   Sarpanch had earlier called such meetings for various
                            problems → NOT implicit (past history is not embedded
                            in the current statement)
            Assumption II:  Most heads of families may attend the meeting
                            → IMPLICIT ✓ (calling a meeting assumes people will
                            attend it; if no one came, the meeting would serve no
                            purpose)
            Only Assumption II is implicit.

  Q5  C — District authority decides to set up wireless communication along the
           coastline because of an approaching cyclonic storm.
            Assumption I:   Telephone communication may be paralysed due to the
                            cyclonic storm → IMPLICIT ✓ (the decision to deploy
                            WIRELESS specifically implies that normal/telephone
                            communication might fail during the storm)
            Assumption II:  Wireless communication systems can withstand the impact
                            of the cyclonic storm → IMPLICIT ✓ (the authority sets
                            up wireless assuming it will work where conventional
                            communication fails; if wireless also failed, the action
                            would be pointless)
            Both I & II are implicit.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Statement_Assumption_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Statement Assumption and Conclusion"

# Standard fixed options — same for every question.
_A = "Only Assumption I is implicit. / केवल पूर्वानुमान I अंतर्निहित है।"
_B = "Only Assumption II is implicit. / केवल पूर्वानुमान II अंतर्निहित है।"
_C = "Both I & II are implicit. / I और II दोनों अंतर्निहित हैं।"
_D = "Neither I nor II is implicit. / न तो I और न ही II अंतर्निहित है।"

QUESTIONS = [
    # ── Q1 ────────────────────────────────────────────────────────────────────
    {
        "question_number": 1,
        "difficulty": "medium",
        "question_en": (
            "Statement: The municipal corporation has announced 50% reduction in "
            "water supply till monsoon arrives in the city.\n\n"
            "Assumptions:\n"
            "I.  People may protest against the unilateral decision of the "
            "municipal corporation.\n"
            "II. Municipal corporation may reduce its expenses from the residents "
            "as it failed to provide adequate water."
        ),
        "question_hi": (
            "कथन: नगर निगम ने मानसून के आने तक शहर में जल आपूर्ति में 50% कमी "
            "करने की घोषणा की है।\n\n"
            "पूर्वानुमान:\n"
            "I.  हो सकता है लोग नगर निगम के एकपक्षीय निर्णय का विरोध करें।\n"
            "II. हो सकता है नगर निगम निवासियों के कर की राशि कम करे क्योंकि वह "
            "पर्याप्त जल उपलब्ध कराने में असफल रहा है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "D",
        # I:  Public protest is a possible reaction but is NOT assumed by the
        #     announcement; the corporation's statement doesn't imply it ✗
        # II: Reducing residents' taxes/charges is a separate possible action
        #     not embedded in the water supply announcement ✗
    },
    # ── Q2 ────────────────────────────────────────────────────────────────────
    {
        "question_number": 2,
        "difficulty": "easy",
        "question_en": (
            "Statement: Many people were caught by the railway police while they "
            "were trying to cross the railway tracks and imposed heavy penalty "
            "before releasing them.\n\n"
            "Assumptions:\n"
            "I.  People may refrain from crossing railway tracks in future.\n"
            "II. People may continue crossing railway tracks and pay heavy penalty."
        ),
        "question_hi": (
            "कथन: रेल पटरियों को पार करने की कोशिश कर रहे कई लोगों को पुलिस ने "
            "पकड़ा और छोड़ने से पहले उन पर भारी जुर्माना लगाया।\n\n"
            "पूर्वानुमान:\n"
            "I.  हो सकता है भविष्य में लोग रेल पटरियों पर न चढ़ें।\n"
            "II. हो सकता है लोग रेल पटरियों पर चलते रहें और भारी जुर्माना "
            "भरते रहें।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Imposing a penalty ASSUMES it will deter future violations; deterrence
        #     is the implicit purpose of the punishment ✓
        # II: Assuming violators will continue despite the penalty would make the
        #     penalty pointless; this contradicts the action taken ✗
    },
    # ── Q3 ────────────────────────────────────────────────────────────────────
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": (
            "Statement: The employee's association urged its members to stay away "
            "from the annual function as many of their demands were not met by the "
            "management.\n\n"
            "Assumptions:\n"
            "I.  Majority of the members of the association may not attend the "
            "function.\n"
            "II. The management may cancel the annual function."
        ),
        "question_hi": (
            "कथन: कर्मचारी संघ ने अपने सदस्यों को वार्षिक कार्यक्रम से दूर रहने "
            "के लिए कहा है क्योंकि उनकी कई माँगें प्रबंधन से पूरी नहीं थीं।\n\n"
            "पूर्वानुमान:\n"
            "I.  हो सकता है कि संघ के अधिकांश सदस्य कार्यक्रम में भाग न लें।\n"
            "II. हो सकता है प्रबंधन वार्षिक कार्यक्रम को रद्द कर दे।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "A",
        # I:  Urging a boycott assumes the members will follow the call; if they
        #     were expected to ignore it, the urge would be pointless ✓
        # II: Management cancelling the function is a possible outcome, not an
        #     assumption embedded in the association's appeal ✗
    },
    # ── Q4 ────────────────────────────────────────────────────────────────────
    {
        "question_number": 4,
        "difficulty": "easy",
        "question_en": (
            "Statement: The Sarpanch of the village called a meeting of all the "
            "heads of the families to discuss the problem of acute shortage of "
            "drinking water in the village.\n\n"
            "Assumptions:\n"
            "I.  The Sarpanch had earlier called such meetings to discuss various "
            "problems.\n"
            "II. Most of the heads of families may attend the meeting called by "
            "the Sarpanch."
        ),
        "question_hi": (
            "कथन: गाँव के सरपंच ने पीने के पानी की गंभीर समस्या पर चर्चा करने "
            "के लिए गाँव के सभी परिवारों के मुखिया की बैठक बुलाई।\n\n"
            "पूर्वानुमान:\n"
            "I.  विभिन्न समस्याओं के बारे में चर्चा करने के लिए सरपंच ने ऐसी "
            "बैठकें पहले भी बुलाई थीं।\n"
            "II. हो सकता है कि अधिकांश परिवारों के मुखिया सरपंच द्वारा बुलाई "
            "गई बैठक में भाग लें।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "B",
        # I:  Past meeting history is external information not embedded in the
        #     current statement; NOT implicit ✗
        # II: Calling a meeting assumes people will attend it; a meeting called
        #     with no expectation of attendance would serve no purpose ✓
    },
    # ── Q5 ────────────────────────────────────────────────────────────────────
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": (
            "Statement: The district authority has decided to set up wireless "
            "communication along the coastline in view of the cyclonic storm "
            "hitting the coast.\n\n"
            "Assumptions:\n"
            "I.  The telephone communication may be paralysed due to cyclonic "
            "storm.\n"
            "II. The wireless communication systems may be able to withstand the "
            "impact of the cyclonic storm."
        ),
        "question_hi": (
            "कथन: चक्रवाती तूफान के तटीय क्षेत्रों से टकराने की स्थिति में बेहतर "
            "संचार सुनिश्चित करने के लिए जिला प्रशासन ने तटीय क्षेत्रों में बेतार "
            "संचार प्रणाली का स्थापन का निर्णय लिया है।\n\n"
            "पूर्वानुमान:\n"
            "I.  चक्रवाती तूफान के कारण दूरभाष संचार व्यवस्था भंग हो सकती है।\n"
            "II. बेतार संचार प्रणाली चक्रवाती तूफान के आघात को सह सकती है।"
        ),
        "option_a": _A,
        "option_b": _B,
        "option_c": _C,
        "option_d": _D,
        "correct_answer": "C",
        # I:  Deploying WIRELESS communication specifically for a cyclonic storm
        #     scenario implies normal telephone communication is assumed to fail ✓
        # II: The authority sets up wireless communication assuming it will work
        #     where conventional systems fail; if wireless also failed, the action
        #     would have no purpose ✓
        # Both I & II are implicit.
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
