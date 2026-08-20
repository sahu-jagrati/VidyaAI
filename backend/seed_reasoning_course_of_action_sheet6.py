"""
seed_reasoning_course_of_action_sheet6.py
==========================================
Seeds Course of Action Q19-Q22 from Gagan Pratap Reasoning PDFs (Sheet 6).
Subject : Reasoning
Topic   : Course of Action

All four questions use custom option texts stored directly in DB columns
(shuffled exam sets or unique NTPC situational-judgment format).
No frontend option-injection needed.

Answer key:
  Q19  A — Large number of city people diagnosed with Malaria:
            I  (municipal authorities carry out extensive fumigation) = eliminates
               mosquitoes at the source ✓
            II (advise people to avoid mosquito bites) = personal protection ✓
            Both I and II follow. [option (a) in shuffled set]
            Source: CGL Tier-II, 02 March 2023 (Shift-1)

  Q20  C — Traffic congestion significantly increased during peak hours:
            I  (improve public transport infrastructure & services) = addresses
               root cause by providing viable alternatives to private vehicles ✓
            II (impose hefty fines on individual drivers during peak hours) =
               punitive; penalises people who have no alternative when public
               transport is inadequate ✗
            Only I follows. [option (c) in shuffled set]
            Source: CHSL Tier-II, 26 June 2023 (Shift-1)

  Q21  D — Research shows outdoor play improves kids' health; kids have no
            time to play outdoors. Parents should …:
            (a) Encourage indoor games → goes against outdoor-play finding ✗
            (b) Not send kids to school → extreme and counterproductive ✗
            (c) Make playing outdoors compulsory → plausible but prescriptive ✗
            (d) Re-schedule office hours to get more time to play with kids →
                enables and models outdoor play; practical parental action ✓
            Source: NTPC CBT-2, 2021

  Q22  D — First-time offence: accountant J misappropriated ₹1200;
            manager may dismiss, impose large fine, or give written warning:
            (a) Terminate J → too extreme for a first offence ✗
            (b) Fine of ₹5 → disproportionately trivial for ₹1200 offence ✗
            (c) Congratulate J → rewards misconduct ✗
            (d) Call J and warn him → proportionate, corrective first response ✓
            Source: NTPC CBT-2, 2021
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Course_Of_Action_Sheet6"
SUBJECT = "Reasoning"
TOPIC   = "Course of Action"

QUESTIONS = [
    # ── Q19 — Custom shuffled 4-option (CGL Tier-II, 02 March 2023, Shift-1) ─────────
    {
        "question_number": 19,
        "difficulty": "easy",
        "question_en": (
            "Statement: A large number of the people of the city are diagnosed to be "
            "suffering from Malaria disease.\n\n"
            "Courses of Action:\n"
            "I.  The city municipal authorities should take immediate steps to carry "
            "out extensive fumigation in the city.\n"
            "II. The people in the area should be advised to take steps to avoid "
            "mosquito bites."
        ),
        "question_hi": (
            "कथन: शहर में बड़ी संख्या में लोग मलेरिया रोग से पीड़ित पाए गए।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  शहर के नगरपालिका अधिकारियों को शहर में व्यापक धूमन करने के लिए "
            "तत्काल कदम उठाने चाहिए।\n"
            "II. क्षेत्र के लोगों को मच्छरों के काटने से बचने के लिए कदम उठाने "
            "की सलाह दी जानी चाहिए।"
        ),
        # Shuffled options (a)=Both ← correct, (b)=Only II, (c)=Only I, (d)=Neither
        "option_a": "Both I & II follow. / I और II दोनों कार्यवाही अनुसरण करती हैं।",
        "option_b": "Only II follows. / केवल कार्यवाही II अनुसरण करती है।",
        "option_c": "Only I follows. / केवल कार्यवाही I अनुसरण करती है।",
        "option_d": "Neither I nor II follows. / न तो I और न ही II कार्यवाही अनुसरण करती है।",
        "correct_answer": "A",
        # I: Municipal fumigation = immediate source elimination of mosquitoes ✓
        # II: Public advice to avoid bites = personal-protection layer ✓
        # Both are complementary (environmental + individual) → Both I & II follow → (a).
    },
    # ── Q20 — Custom shuffled 4-option (CHSL Tier-II, 26 June 2023, Shift-1) ─────────
    {
        "question_number": 20,
        "difficulty": "medium",
        "question_en": (
            "Statement: The traffic congestion in the city has significantly increased "
            "during peak hours.\n\n"
            "Courses of Action:\n"
            "I.  Improve public transportation infrastructure and services to provide "
            "viable alternatives to private vehicles.\n"
            "II. Impose hefty fines on individual drivers during peak hours."
        ),
        "question_hi": (
            "कथन: चरम घंटों के दौरान शहर में यातायात की भीड़ काफी बढ़ जाती है।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  निजी वाहनों को व्यवहार्य विकल्प प्रदान करने के लिए सार्वजनिक "
            "परिवहन अवसंरचना और सेवाओं में सुधार करें।\n"
            "II. चरम घंटों के दौरान व्यक्तिगत वाहन चालकों पर भारी जुर्माना लगाएं।"
        ),
        # Shuffled options (a)=Both, (b)=Neither, (c)=Only I ← correct, (d)=Only II
        "option_a": "Both I & II follow. / I और II दोनों कार्यवाही अनुसरण करती हैं।",
        "option_b": "Neither I nor II follows. / न तो I और न ही II कार्यवाही अनुसरण करती है।",
        "option_c": "Only I follows. / केवल कार्यवाही I अनुसरण करती है।",
        "option_d": "Only II follows. / केवल कार्यवाही II अनुसरण करती है।",
        "correct_answer": "C",
        # I: Improving public transport addresses root cause by reducing dependence
        #    on private vehicles; people need a viable alternative first ✓
        # II: Hefty fines punish drivers who often have no choice when public
        #    transport is inadequate; punitive without solving systemic issue ✗
        # Only I follows → (c) in this shuffled set.
    },
    # ── Q21 — NTPC CBT-2, 2021 situational-judgment format ───────────────────────────
    {
        "question_number": 21,
        "difficulty": "medium",
        "question_en": (
            "Based on the scenario given, choose the decision from the options which "
            "would be most suitable.\n\n"
            "Research shows that playing outdoors improves the overall health of kids. "
            "Nowadays kids do not find time to play outdoors.\n\n"
            "Parents should ..........."
        ),
        "question_hi": (
            "दिए गए परिदृश्य के आधार पर, विकल्पों में से वह निर्णय चुनें जो "
            "सबसे उपयुक्त होगा।\n\n"
            "शोध से पता चलता है कि बाहर खेलने से बच्चों के समग्र स्वास्थ्य में "
            "सुधार होता है। आजकल बच्चों के पास बाहर खेलने का समय नहीं है।\n\n"
            "माता-पिता को करना चाहिए ................."
        ),
        "option_a": "Encourage indoor games. / घर के अंदर के खेलों को प्रोत्साहित करें।",
        "option_b": "Not send the kids to school. / बच्चों को स्कूल न भेजें।",
        "option_c": "Make playing outdoors compulsory. / बच्चों के बाहर खेलना अनिवार्य कर दें।",
        "option_d": (
            "Re-schedule their office hours so they get more time to play with "
            "the kids. / "
            "आपने कार्यालय समय को फिर से पुनर्निधारित करें ताकि उन्हें बच्चों के "
            "साथ खेलने के लिए अधिक समय मिल सके।"
        ),
        "correct_answer": "D",
        # (a) Indoor games → contradicts the outdoor-play finding ✗
        # (b) No school → extreme, harmful ✗
        # (c) Compulsory outdoor play → overly rigid prescription ✗
        # (d) Re-schedule office hours → parents free up time to accompany and
        #     enable kids' outdoor play; practical parental action ✓
    },
    # ── Q22 — NTPC CBT-2, 2021 situational-judgment format ───────────────────────────
    {
        "question_number": 22,
        "difficulty": "medium",
        "question_en": (
            "Based on the scenario given, choose the decision from the options which "
            "would be most suitable.\n\n"
            "For a first-time offence by an employee at the factory, the manager can "
            "either dismiss the employee, impose a large fine or give a written "
            "warning. J, the accountant misappropriated an amount of Rs 1200. This "
            "was J's first Offence. What should his manager do?"
        ),
        "question_hi": (
            "दिए गए परिदृश्य के आधार पर, विकल्पों में से वह निर्णय चुनें जो "
            "सबसे उपयुक्त होगा।\n\n"
            "फैक्टी में किसी कर्मचारी द्वारा पहली बार अपराध करने पर, प्रबंधक "
            "या तो कर्मचारी को बर्खास्त कर सकता है, बड़ा जुर्माना लगा सकता है "
            "या लिखित चेतावनी दे सकता है। J, अकाउंटेंट ने 1200 रुपये की राशि "
            "का गबन किया। यह J का पहला अपराध था। उसके प्रबंधक को क्या करना चाहिए।"
        ),
        "option_a": "Terminate J from his job. / J को नौकरी से बर्खास्त कर दिया जाये।",
        "option_b": "Impose a fine of Rs 5 on J. / J पर 5 रुपए का जुर्माना लगाया जाये।",
        "option_c": (
            "Call for a meeting and congratulate his behavior. / "
            "एक बैठक बुलाई जाये और उसके व्यवहार की सराहना की जाये।"
        ),
        "option_d": "Call J over the phone and warn him. / J को फोन करके चेतावनी दी जाये।",
        "correct_answer": "D",
        # (a) Terminate → too extreme for a FIRST offence ✗
        # (b) Fine of ₹5 → disproportionately trivial for ₹1200 misappropriation ✗
        # (c) Congratulate → rewards misconduct ✗
        # (d) Phone warning → proportionate, corrective first-time response; closest
        #     to "written warning" intent available in the options ✓
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
