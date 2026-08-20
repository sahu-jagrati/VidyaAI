"""
seed_reasoning_course_of_action_sheet5.py
==========================================
Seeds Course of Action Q15-Q18 from Gagan Pratap Reasoning PDFs (Sheet 5).
Subject : Reasoning
Topic   : Course of Action

Q15  — Standard 5-option format (options (a)-(d) in DB; option (e) injected by frontend
        when option_c starts with "Either I or II"):
          (a) Only I follows.
          (b) Only II follows.
          (c) Either I or II follows.
          (d) Neither I nor II follows.
          (e) Both I and II follow.  ← COA_5OPT_E injected by frontend

Q16  — Custom 4-option CHSL format (shuffled order; all option text stored in DB)
        Source: CHSL Tier-II, 10 Jan 2024 (Shift-1)

Q17  — Custom 4-option CHSL format (shuffled order; all option text stored in DB)
        Source: CHSL Tier-II, 07 March 2023 (Shift-1)

Q18  — Custom 4-option CGL format (shuffled order; all option text stored in DB)
        Source: CGL Tier-II, 03 March 2023 (Shift-1)

Answer key:
  Q15  A — CBI receives bribe complaint against officer:
            I  (catch red-handed → strict action) = proper CBI procedure ✓
            II (wait for more complaints) = delays action while corruption
               continues ✗
            Only I follows.

  Q16  C — Voltage fluctuation damaged A's electrical appliances:
            I  (consult electrician + install surge-protection device)
               = addresses both immediate protection and future prevention ✓
            II (replace ALL appliances) = too extreme; new appliances will
               also be damaged if the voltage issue isn't fixed ✗
            Only I follows. [option (c) in shuffled set]

  Q17  D — Serious mistakes found in technical section of company:
            I  (appoint efficient technical team to check errors)
               = directly addresses the technical mistakes ✓
            II (issue reason-explanation notice to employees in irregularities)
               = appropriate accountability measure ✓
            Both I and II follow. [option (d) in shuffled set]

  Q18  D — Large migration of villagers to cities due to repeated crop failure:
            I  (provide alternate income in villages) = fixes root cause,
               keeps villagers in villages ✓
            II (give migrated villagers access to all housing in urban areas)
               = facilitates further migration rather than solving the root
               problem of crop failure / financial distress ✗
            Only I follows. [option (d) in shuffled set]
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Course_Of_Action_Sheet5"
SUBJECT = "Reasoning"
TOPIC   = "Course of Action"

QUESTIONS = [
    # ── Q15 — 5-option standard format ────────────────────────────────────────────────
    # option_e "Both I and II follow" is injected by frontend when option_c starts
    # with "Either I or II". Do NOT embed it in the question body.
    {
        "question_number": 15,
        "difficulty": "medium",
        "question_en": (
            "Statement: The Central Bureau of Investigation receives the complaint of "
            "an officer taking bribe to do the duty he is supposed to.\n\n"
            "Courses of Action:\n"
            "I.  CBI should try to catch the officer red-handed and then take a strict "
            "action against him.\n"
            "II. CBI should wait for some more complaints about the officer to be sure "
            "about the matter."
        ),
        "question_hi": (
            "कथन: केंद्रीय जांच ब्यूरो को एक अधिकारी द्वारा अपनी ड्यूटी निभाने के "
            "लिए रिश्वत लेने की शिकायत प्राप्त होती है।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  CBI को अधिकारी को रंगे हाथों पकड़ने की कोशिश करनी चाहिए और फिर "
            "उसके खिलाफ कड़ी कार्रवाई करनी चाहिए।\n"
            "II. CBI को इस मामले में सुनिश्चित होने के लिए अधिकारी के बारे में कुछ "
            "और शिकायतों का इंतजार करना चाहिए।"
        ),
        # 5-option format: option_c = "Either I or II follows" signals frontend injection
        "option_a": "Only I follows. / केवल कार्यवाही I अनुसरण करती है।",
        "option_b": "Only II follows. / केवल कार्यवाही II अनुसरण करती है।",
        "option_c": "Either I or II follows. / या तो I या II कार्यवाही अनुसरण करती है।",
        "option_d": "Neither I nor II follows. / न तो I और न ही II कार्यवाही अनुसरण करती है।",
        # option_e injected by frontend as COA_5OPT_E = "Both I and II follow."
        "correct_answer": "A",
        # I: Red-handed catch + strict action is the standard CBI investigative
        #    procedure once a complaint is received ✓
        # II: Waiting for more complaints delays justice and lets the officer
        #    continue taking bribes with impunity ✗
        # Only I follows.
    },
    # ── Q16 — Custom shuffled 4-option (CHSL Tier-II, 10 Jan 2024, Shift-1) ──────────
    {
        "question_number": 16,
        "difficulty": "medium",
        "question_en": (
            "Statement: Voltage fluctuation in A's home has damaged many of his new "
            "electrical appliances.\n\n"
            "Courses of Action:\n"
            "I.  A should consult an electrician and install a device to safeguard "
            "appliances against fluctuations in voltage.\n"
            "II. A should replace all the appliances."
        ),
        "question_hi": (
            "कथन: A के घर में वोल्टेज में उतार-चढ़ाव के कारण उसके कई नए विद्युत "
            "उपकरण क्षतिग्रस्त हो गए हैं।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  A को एक इलेक्ट्रीशियन से परामर्श करना चाहिए और वोल्टेज में "
            "उतार-चढ़ाव के विरुद्ध उपकरणों की सुरक्षा के लिए एक उपकरण स्थापित "
            "करना चाहिए।\n"
            "II. A को सभी उपकरणों को बदलना चाहिए।"
        ),
        # Shuffled options (a)=Both, (b)=Only II, (c)=Only I ← correct, (d)=Neither
        "option_a": "Both I & II follow. / I और II दोनों कार्यवाही अनुसरण करती हैं।",
        "option_b": "Only II follows. / केवल कार्यवाही II अनुसरण करती है।",
        "option_c": "Only I follows. / केवल कार्यवाही I अनुसरण करती है।",
        "option_d": "Neither I nor II follows. / न तो I और न ही II कार्यवाही अनुसरण करती है।",
        "correct_answer": "C",
        # I: Consult electrician + install surge protector = targeted, practical fix ✓
        # II: Replace ALL appliances = extreme; new appliances will also be damaged
        #     if the voltage issue isn't resolved first ✗
        # Only I follows → (c) in this shuffled set.
    },
    # ── Q17 — Custom shuffled 4-option (CHSL Tier-II, 07 March 2023, Shift-1) ────────
    {
        "question_number": 17,
        "difficulty": "easy",
        "question_en": (
            "Statement: Some serious mistakes were found in the technical section of "
            "the company.\n\n"
            "Courses of Action:\n"
            "I.  An efficient technical team should be appointed to check the "
            "technical errors.\n"
            "II. A reason explanation notice should be issued to all the employees "
            "involved in the irregularities."
        ),
        "question_hi": (
            "कथन: कंपनी के तकनीकी अनुभाग में कुछ गंभीर गलतियाँ पाई गईं।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  तकनीकी त्रुटियों की जांच के लिए एक कुशल तकनीकी टीम नियुक्त की "
            "जानी चाहिए।\n"
            "II. अनियमितताओं में शामिल सभी कर्मचारियों को कारण स्पष्टीकरण नोटिस "
            "जारी किया जाना चाहिए।"
        ),
        # Shuffled options (a)=Neither, (b)=Only I, (c)=Only II, (d)=Both ← correct
        "option_a": "Neither I nor II follows. / न तो I और न ही II कार्यवाही अनुसरण करती है।",
        "option_b": "Only I follows. / केवल कार्यवाही I अनुसरण करती है।",
        "option_c": "Only II follows. / केवल कार्यवाही II अनुसरण करती है।",
        "option_d": "Both I & II follow. / I और II दोनों कार्यवाही अनुसरण करती हैं।",
        "correct_answer": "D",
        # I: Appoint technical team to identify and fix errors = direct corrective action ✓
        # II: Explanation notice to involved employees = accountability and due process ✓
        # Both I and II follow → (d) in this shuffled set.
    },
    # ── Q18 — Custom shuffled 4-option (CGL Tier-II, 03 March 2023, Shift-1) ─────────
    {
        "question_number": 18,
        "difficulty": "hard",
        "question_en": (
            "Statement: There is a large increase in migration of villagers to urban "
            "areas as repeated crop failure has put them into financial problems.\n\n"
            "Courses of Action:\n"
            "I.  The villagers should be provided with an alternate source of income "
            "in their villages which will make them stay there only.\n"
            "II. To ensure their survival, the migrated villagers should be given "
            "access to all housing options in urban areas."
        ),
        "question_hi": (
            "कथन: ग्रामीणों के शहरी क्षेत्रों की ओर प्रवास में बड़ी वृद्धि हुई है, "
            "क्योंकि बार-बार फसल की विफलता ने उन्हें वित्तीय समस्याओं में डाल "
            "दिया है।\n\n"
            "कार्यवाहियाँ:\n"
            "I.  ग्रामीणों को उनके गांवों में आय का एक वैकल्पिक स्रोत प्रदान "
            "किया जाना चाहिए जिससे वे वहीं रहें।\n"
            "II. अपने अस्तित्व को सुनिश्चित करने के लिए, प्रवासित ग्रामीणों को "
            "शहरी क्षेत्रों में सभी आवास विकल्पों तक पहुंच प्रदान की जानी चाहिए।"
        ),
        # Shuffled options (a)=Only II, (b)=Both, (c)=Neither, (d)=Only I ← correct
        "option_a": "Only II follows. / केवल कार्यवाही II अनुसरण करती है।",
        "option_b": "Both I and II follow. / I और II दोनों कार्यवाही अनुसरण करती हैं।",
        "option_c": "Neither I nor II follows. / न तो I और न ही II कार्यवाही अनुसरण करती है।",
        "option_d": "Only I follows. / केवल कार्यवाही I अनुसरण करती है।",
        "correct_answer": "D",
        # I: Alternate income source in villages = addresses root cause (crop failure
        #    financial distress) and prevents further migration ✓
        # II: Housing access in urban areas = facilitates/encourages migration rather
        #    than solving the underlying problem; doesn't help those still in villages ✗
        # Only I follows → (d) in this shuffled set.
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
