"""
seed_reasoning_course_of_action_sheet1.py
==========================================
Seeds Course of Action Q1-Q4 from Gagan Pratap Reasoning PDFs (Sheet 1).
Subject : Reasoning
Topic   : Course of Action

Format:
  - Each question has a Statement/कथन describing a situation/problem.
  - Two Courses of Action (I and II) are proposed.
  - Standard 4 options (always same order, no 5th option):
      (a) Only I follows.
      (b) Only II follows.
      (c) Both I and II follow.
      (d) Neither I nor II follows.
  - No CE_OPTION_E injection needed — frontend handles as standard 4-option question.

Answer key:
  Q1  C — Respiratory diseases in coastal town:
           I  (send health team) is an immediate relief measure ✓
           II (special ward + medication) is a proper treatment measure ✓
           Both follow.

  Q2  C — Drop in telephone connections from public sector company:
           I  (committee to find reasons) addresses the root cause ✓
           II (new schemes with value-added services) addresses the demand ✓
           Both follow.

  Q3  C — Speeding truck seriously injures people sleeping on roadside:
           I  (ban sleeping on roadsides) is a preventive administrative action ✓
           II (nab & try the truck driver) is the clear legal action ✓
           Both follow.

  Q4  A — Unprecedented increase in school admission applicants:
           I  (objective admission criteria) directly solves the problem ✓
           II (open another school) is too drastic/infeasible for one admission year ✗
           Only I follows.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Course_Of_Action_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Course of Action"

# Standard 4 options shared by all Course of Action questions (always same order).
_OPT_A = "Only I follows. / केवल कार्यवाही I अनुसरण करती है।"
_OPT_B = "Only II follows. / केवल कार्यवाही II अनुसरण करती है।"
_OPT_C = "Both I and II follow. / I और II दोनों कार्यवाही अनुसरण करती हैं।"
_OPT_D = "Neither I nor II follows. / न तो I और न ही II कार्यवाही अनुसरण करती है।"

QUESTIONS = [
    # ── Q1 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 1,
        "difficulty": "easy",
        "question_en": (
            "Statement: Many people in the coastal town have been suffering from "
            "respiratory diseases during past few months.\n\n"
            "Courses of Action:\n"
            "I.  The government should immediately send a team of health professionals "
            "to provide medical care to the affected people.\n"
            "II. The people suffering from such diseases should be kept in a special "
            "ward & put through proper medication."
        ),
        "question_hi": (
            "कथन: पिछले कुछ महीनों के दौरान तटीय शहर के बहुत से लोग श्वास संबंधी "
            "रोगों से पीड़ित हैं।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  प्रभावित लोगों को चिकित्सा सुविधा उपलब्ध कराने के लिए सरकार को "
            "तत्काल स्वास्थ्य पेशेवरों का एक दल भेजना चाहिए।\n"
            "II. ऐसे रोगों से पीड़ित लोगों को एक विशेष वार्ड में रखा जाना चाहिए और "
            "उनका उचित उपचार किया जाना चाहिए।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "C",
        # I: Immediate medical team = urgent relief ✓
        # II: Special ward + proper medication = proper treatment ✓
        # Both are logical and complementary → Both I and II follow.
    },
    # ── Q2 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 2,
        "difficulty": "medium",
        "question_en": (
            "Statement: There has been a substantial drop in the number of people "
            "opting for new telephone connection from the public sector telephone "
            "company in the recent months.\n\n"
            "Courses of Action:\n"
            "I.  The public sector telephone company should immediately set up a "
            "committee to identify the reasons for the drop.\n"
            "II. The public sector telephone company should offer new schemes with "
            "value added services to woo the new clients."
        ),
        "question_hi": (
            "कथन: हाल के महीनों में सरकारी क्षेत्र की टेलीफोन कंपनी से नया टेलीफोन "
            "कनेक्शन लेने के इच्छुक लोगों की संख्या में भारी गिरावट आई है।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  सरकारी क्षेत्र की टेलीफोन कंपनी को तुरंत इस गिरावट के कारणों का "
            "पता लगाने के लिए तत्काल एक समिति स्थापित करनी चाहिए।\n"
            "II. नए ग्राहकों को आकर्षित करने के लिए सरकारी क्षेत्र की टेलीफोन कंपनी "
            "को वेल्यू एडेड सेवाओं के साथ नई योजनाएं पेश करनी चाहिए।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "C",
        # I: Committee to find root cause = logical diagnostic step ✓
        # II: New schemes with value-added services = proactive demand-recovery step ✓
        # Both are valid and address the problem from different angles → Both follow.
    },
    # ── Q3 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": (
            "Statement: A speeding truck has seriously injured many persons sleeping "
            "on the roadside early in the morning.\n\n"
            "Courses of Action:\n"
            "I.  The local administration should immediately put a complete ban on "
            "people sleeping on the roadsides.\n"
            "II. The driver of the speeding truck should be nabbed & tried for the "
            "crime he committed."
        ),
        "question_hi": (
            "कथन: तेज गति से आते हुए एक ट्रक ने अलसुबह सड़क के किनारे सोए हुए बहुत "
            "से लोगों को गंभीर चोट पहुंचाई है।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  स्थानीय प्रशासन के द्वारा सड़क के किनारे सोने पर तत्काल प्रतिबंध "
            "लगाया जाना चाहिए।\n"
            "II. तेज गति से चलने वाले ट्रक के चालक को पकड़कर उस पर किए गए अपराध हेतु "
            "न्यायिक कार्यवाही की जानी चाहिए।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "C",
        # I: Ban sleeping on roadsides = preventive administrative measure ✓
        # II: Nab & legally try the driver = immediate legal accountability ✓
        # Both are logical and implementable → Both I and II follow.
    },
    # ── Q4 ────────────────────────────────────────────────────────────────────────────
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": (
            "Statement: There has been an unprecedented increase in the number of "
            "students applying for admission to first standard in a local school "
            "making it difficult for the school authority to convince the parents "
            "of rejected applicants.\n\n"
            "Courses of Action:\n"
            "I.  The school authority should immediately put in place an objective "
            "criteria for admitting students to select the required number.\n"
            "II. The school authority should open another school in the area to "
            "accommodate the remaining students."
        ),
        "question_hi": (
            "कथन: एक स्थानीय स्कूल में पहली कक्षा में प्रवेश के लिए आवेदन करने वाले "
            "छात्रों की संख्या में अभूतपूर्व वृद्धि हुई है जिनमें से जिन बच्चों को "
            "अस्वीकार किया गया है उनके माता-पिता को यह विश्वास दिलाने में स्कूल "
            "प्राधिकरणों को काफी मुश्किलें हुई हैं।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  स्कूल प्राधिकरणों को आवश्यक संख्या के चयन हेतु छात्रों के प्रवेश के "
            "लिए तत्काल समुचित, वस्तुनिष्ठ मापदंड स्थापित करने चाहिए।\n"
            "II. शेष विद्यार्थियों के समायोजन के लिए स्कूल प्राधिकरणों को उस क्षेत्र "
            "में दूसरा स्कूल खोलना चाहिए।"
        ),
        "option_a": _OPT_A,
        "option_b": _OPT_B,
        "option_c": _OPT_C,
        "option_d": _OPT_D,
        "correct_answer": "A",
        # I: Objective admission criteria = directly addresses the dispute fairly ✓
        # II: Open another school = too drastic/impractical for a single admission
        #     surge; not within the school authority's usual capacity ✗
        # Only I follows.
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
