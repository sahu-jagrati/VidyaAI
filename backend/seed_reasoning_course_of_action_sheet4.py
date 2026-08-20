"""
seed_reasoning_course_of_action_sheet4.py
==========================================
Seeds Course of Action Q12-Q14 from Gagan Pratap Reasoning PDFs (Sheet 4).
Subject : Reasoning
Topic   : Course of Action

Standard 4 options (same order):
  (a) Only I follows.
  (b) Only II follows.
  (c) Both I and II follow.
  (d) Neither I nor II follows.

Answer key:
  Q12  C — 30 people die in building collapse; locals agitated:
            I  (govt announces immediate compensation for affected families)
               = urgent humanitarian relief ✓
            II (stringent action against builders who compromise on material
               quality) = accountability + prevention of future collapses ✓
            Both I and II follow.

  Q13  C — More students pass X class but can't get into college of their choice:
            I  (govt permits colleges to increase seats) = directly reduces the
               supply–demand gap ✓
            II (counsel children & parents to be flexible on college choice)
               = manages expectations, reduces frustration ✓
            Both I and II follow.

  Q14  C — Monsoon onset causes epidemic surge; hospitals overwhelmed:
            I  (educate public on minimum required hygiene) = preventive action
               targeting the root cause of epidemics ✓
            II (equip hospitals with medicines and facilities) = curative
               support for the already increased patient load ✓
            Both I and II follow.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Course_Of_Action_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Course of Action"

_OPT_A = "Only I follows. / केवल कार्यवाही I अनुसरण करती है।"
_OPT_B = "Only II follows. / केवल कार्यवाही II अनुसरण करती है।"
_OPT_C = "Both I and II follow. / I और II दोनों कार्यवाही अनुसरण करती हैं।"
_OPT_D = "Neither I nor II follows. / न तो I और न ही II कार्यवाही अनुसरण करती है।"

QUESTIONS = [
    # ── Q12 ───────────────────────────────────────────────────────────────────────────
    {
        "question_number": 12,
        "difficulty": "easy",
        "question_en": (
            "Statement: People in the locality were agitated as more than 30 people "
            "died in a building collapse.\n\n"
            "Courses of Action:\n"
            "I.  Government should immediately announce compensations for the "
            "affected families.\n"
            "II. Authorities should take a stringent action against builders tending "
            "to compromise over the quality of material used."
        ),
        "question_hi": (
            "कथन: एक मकान के ढहने पर तीस लोगों की मृत्यु हो गई। इससे इस इलाके "
            "के लोग उत्तेजित हो गए।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  सरकार को प्रभावित परिवारों के लिए तुरंत मुआवजे की घोषणा करनी "
            "चाहिए।\n"
            "II. प्रयुक्त सामग्री में समझौता करने वाले बिल्डरों के विरुद्ध सरकार "
            "को कड़ी कार्यवाही करनी चाहिए।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "C",
        # I: Immediate compensation addresses the urgent humanitarian need of
        #    bereaved families and helps calm the agitated locality ✓
        # II: Action against builders who cut corners on material quality prevents
        #    future collapses and provides accountability ✓
        # Both are appropriate and complementary → Both I and II follow.
    },
    # ── Q13 ───────────────────────────────────────────────────────────────────────────
    {
        "question_number": 13,
        "difficulty": "medium",
        "question_en": (
            "Statement: More number of students passing Xᵗʰ class examination has "
            "resulted into frustration among children for not getting admissions in "
            "Colleges of their choice.\n\n"
            "Courses of Action:\n"
            "I.  Govt. should permit the colleges to increase the number of seats.\n"
            "II. Children and their parents should be counseled for being flexible "
            "on the choice of college."
        ),
        "question_hi": (
            "कथन: अधिक संख्या में विद्यार्थियों द्वारा दसवीं की परीक्षा पास करने के "
            "परिणामस्वरूप बच्चे निराश हो गए हैं क्योंकि उन्हें अपनी पसंद के "
            "कॉलेजों में प्रवेश नहीं मिल पाया है।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  सरकार को कॉलेजों की सीटों की संख्या बढ़ाने की अनुमति देनी "
            "चाहिए।\n"
            "II. बच्चों और उनके माता-पिता को कॉलेज की पसंदगी में लचीला होने की "
            "सलाह दी जानी चाहिए।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "C",
        # I: Permitting colleges to increase seats directly reduces the supply–demand
        #    gap — more seats = more students get into desired colleges ✓
        # II: Counseling students and parents to be flexible reduces frustration and
        #    opens up alternatives — practical demand-side management ✓
        # Both are valid and complementary → Both I and II follow.
    },
    # ── Q14 ───────────────────────────────────────────────────────────────────────────
    {
        "question_number": 14,
        "difficulty": "easy",
        "question_en": (
            "Statement: With the onset of monsoon all the hospitals are getting "
            "increased number of patients due to various epidemics.\n\n"
            "Courses of Action:\n"
            "I.  Civil authorities should educate the public the need for observing "
            "minimum required hygiene.\n"
            "II. Civic authorities should make arrangements to equip the hospitals "
            "with required medicines and other facilities."
        ),
        "question_hi": (
            "कथन: मानसून के प्रारंभ के साथ विभिन्न महामारियों के कारण सभी "
            "अस्पतालों में अधिक संख्या में रोगी आने लगे हैं।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  नागरिक प्राधिकरण को लोगों को न्यूनतम स्वच्छता के अनुपालन की "
            "जरूरत के विषय में शिक्षित करना चाहिए।\n"
            "II. नागरिक प्राधिकरण को अस्पतालों को आवश्यक दवाइयां और अन्य "
            "सुविधाओं की व्यवस्था करनी चाहिए।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "C",
        # I: Educating people about hygiene is preventive — targets the root cause
        #    of monsoon epidemics and reduces future cases ✓
        # II: Equipping hospitals with medicines and facilities is curative —
        #    handles the already increased patient load effectively ✓
        # Both are complementary (preventive + curative) → Both I and II follow.
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
