"""
seed_reasoning_course_of_action_sheet2.py
==========================================
Seeds Course of Action Q5-Q7 from Gagan Pratap Reasoning PDFs (Sheet 2).
Subject : Reasoning
Topic   : Course of Action

Standard 4 options (same order for all Course of Action questions):
  (a) Only I follows.
  (b) Only II follows.
  (c) Both I and II follow.
  (d) Neither I nor II follows.

Answer key:
  Q5  B — Dress code violation:
           I  (rusticate from college) is disproportionately harsh for a dress
              code offence → does NOT follow ✗
           II (reprimand & warn first-time violators) is proportional and
              appropriate → follows ✓
           Only II follows.

  Q6  A — Railway track repair; all city operations suspended for whole Sunday:
           I  (public notification well in advance) is essential so passengers
              can reschedule → follows ✓
           II (stop long-distance trains outside city limits) is redundant
              because the railways have already decided to suspend ALL
              operations; that decision already implies no trains will enter ✗
           Only I follows.

  Q7  D — BPO employees quit to protest inhuman treatment by company:
           I  (govt orders BPO to close down) is too extreme; the remedy for
              mistreatment is investigation/penalisation, not closure → ✗
           II (BPO shifts operations to another place) does not address the
              root cause (inhuman treatment); location change ≠ behaviour
              change → ✗
           Neither I nor II follows.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Course_Of_Action_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Course of Action"

_OPT_A = "Only I follows. / केवल कार्यवाही I अनुसरण करती है।"
_OPT_B = "Only II follows. / केवल कार्यवाही II अनुसरण करती है।"
_OPT_C = "Both I and II follow. / I और II दोनों कार्यवाही अनुसरण करती हैं।"
_OPT_D = "Neither I nor II follows. / न तो I और न ही II कार्यवाही अनुसरण करती है।"

QUESTIONS = [
    # ── Q5 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": (
            "Statement: The local college principal has ordered that all the students "
            "must strictly adhere to the dress code stipulated by the college authority "
            "in the admission brochure.\n\n"
            "Courses of Action:\n"
            "I.  Those students who are found to violate the dress code should be "
            "rusticated from the college.\n"
            "II. Those students who are found to violate the dress code for the first "
            "time should be reprimanded & be warned against further violation."
        ),
        "question_hi": (
            "कथन: स्थानीय कॉलेज के प्राचार्य ने आदेश दिया है कि प्रवेश विवरणिका में "
            "कॉलेज प्राधिकरण द्वारा तय किए गए ड्रेस कोड का सभी छात्रों द्वारा सख्ती "
            "से पालन किया जाना चाहिए।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  ड्रेस कोड का उल्लंघन करने वाले छात्रों को कॉलेज से निकाल दिया जाना "
            "चाहिए।\n"
            "II. पहली बार ड्रेस कोड का उल्लंघन करने वाले छात्रों को डांटा जाना चाहिए "
            "और आगे उल्लंघन न करने की चेतावनी दी जानी चाहिए।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "B",
        # I: Rustication is far too severe for a dress code offence — disproportionate ✗
        # II: Reprimand + warning for first-time offence is proportional and standard
        #     disciplinary practice ✓
        # Only II follows.
    },
    # ── Q6 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": (
            "Statement: The railways have decided to repair the main track within the "
            "city on the following Sunday & have decided to suspend operations for "
            "the whole day.\n\n"
            "Courses of Action:\n"
            "I.  The railway authority should issue public notification well in advance "
            "to avoid inconvenience to the passengers.\n"
            "II. All the long-distance trains entering the city during the repair hours "
            "should be stopped outside the city limit."
        ),
        "question_hi": (
            "कथन: रेलवे ने अगले रविवार को शहर के भीतर मुख्य पटरी की मरम्मत करने का "
            "फैसला किया है और पूरा दिन रेलगाड़ियों के आवागमन को स्थगित करने का "
            "निर्णय लिया है।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  यात्रियों की असुविधा कम करने के लिए रेलवे प्राधिकरण को सार्वजनिक "
            "अधिसूचना समय रहते जारी करनी चाहिए।\n"
            "II. मरम्मत के समय के दौरान शहर में प्रवेश करने वाली लंबी दूरी की सभी "
            "रेलगाड़ियों को शहर की सीमा के बाहर ही रोक देना चाहिए।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # I: Advance public notification is essential — passengers need to reschedule ✓
        # II: Stopping trains outside city limits is redundant; the decision to suspend
        #     ALL operations for the whole day already covers this operationally ✗
        # Only I follows.
    },
    # ── Q7 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": (
            "Statement: Majority of city employees in the renowned BPO company have "
            "left their jobs to protest against inhuman treatment meted out to them "
            "by the company.\n\n"
            "Courses of Action:\n"
            "I.  The Government should immediately order the BPO company to close "
            "down its operation.\n"
            "II. The BPO company should shift its operations to some other place to "
            "continue its operations."
        ),
        "question_hi": (
            "कथन: एक प्रसिद्ध BPO कंपनी में कार्यरत शहर के कर्मचारियों ने कंपनी "
            "द्वारा किए गए अमानवीय व्यवहार के खिलाफ विरोध स्वरूप अपनी नौकरियां "
            "छोड़ दी हैं।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  सरकार को BPO कंपनी को अपने परिचालन बंद करने का आदेश तत्काल देना "
            "चाहिए।\n"
            "II. BPO कंपनी को उनके परिचालनों को जारी रखने के लिए तत्काल अपने "
            "परिचालनों को किसी दूसरी जगह ले जाना चाहिए।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "D",
        # I: Ordering immediate closure is too extreme and unilateral; the correct
        #    response is to investigate and penalise the mistreatment, not shut
        #    down the company — other employees and stakeholders are affected ✗
        # II: Shifting operations to another location does nothing to address the
        #    root cause (inhuman treatment of employees); employees quit because of
        #    HOW they were treated, not WHERE ✗
        # Neither I nor II follows.
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
