"""
seed_reasoning_statement_argument_sheet3.py
============================================
Seeds Statement-Argument Q10–Q15 from Gagan Pratap Reasoning PDFs (Sheet 3).
Subject : Reasoning
Topic   : Statement Argument

Three option formats used across these questions:

1. STANDARD 4-option (Q10, Q11, Q13):
   (A) Only argument I is strong.
   (B) Only argument II is strong.
   (C) Both I & II are strong.
   (D) Neither I nor II is strong.

2. CUSTOM 4-option (Q12 — 4 arguments, "logical" wording):
   (A) Only argument I is logical.
   (B) Either II or III argument is logical.
   (C) Only argument IV is logical.
   (D) Only argument IV is not logical.

3. EXTENDED 5-option (Q14, Q15 — option C = "Either I or II is strong"):
   DB stores (A)-(D); frontend injects (E) = SA_5OPT_E when
   option_c starts with "Either I or II".
   (A) Only argument I is strong.
   (B) Only argument II is strong.
   (C) Either I or II is strong.      ← stored in DB
   (D) Neither I nor II is strong.
   (E) Both I and II are strong.      ← injected by frontend

Answer key:
  Q10  C — Admission to professional courses on pure merit?
            I:  Merit ensures only capable students enter → professionals complete
                courses successfully → quality improves. STRONG ✓
            II: Excludes large numbers of socially/economically backward students
                from professional education. STRONG ✓
            Both I & II are strong.

  Q11  B — Merge all private sector banks with public sector banks?
            I:  Private banks are profit-making so shouldn't be merged → WEAK
                (profitability ≠ exemption from regulation)
            II: Will safeguard customers' hard-earned money → STRONG
                (public sector backing secures depositors' interests) ✓
            Only Argument II is strong.

  Q12  C — Abolish common entrance exams for professional subjects?
            (4-argument, "logical" option format)
            I:   Saves money → WEAK (cost-saving alone cannot justify abolition of
                 a socially important selection mechanism)
            II:  Specialty scorers don't do well in entrance test → WEAK
                 (entrance tests assess different aptitude; discrepancy is expected)
            III: Rural candidates don't do well → WEAK
                 (rural educational disadvantage is not solved by abolishing exams)
            IV:  Marks from different boards are not uniform and comparable → STRONG
                 (directly justifies the need for a standardised common entrance exam
                 to level the playing field across diverse boards) ✓
            Only Argument IV is logical → (C).

  Q13  D — Remove songs from Indian films?
            I:  Hollywood movies are hits without songs → WEAK
                (irrelevant cross-cultural comparison; Indian film tradition differs)
            II: Songs help increase the length of the film → WEAK
                (longer film ≠ better film; "increases length" is not a merit)
            Neither I nor II is strong.

  Q14  B — Prestigious people who commit crime unknowingly: special treatment?
            (5-option format; option E injected by frontend as SA_5OPT_E)
            I:  Prestigious people don't commit crime intentionally → WEAK
                (intent is already considered by law; "prestigious" status is not
                a special legal privilege; common people also commit accidental crimes)
            II: Everyone is equal before the law → STRONG
                (fundamental rule-of-law principle; directly and validly opposes
                status-based differential treatment) ✓
            Only Argument II is strong.

  Q15  E — Abolish all annual exams up to Standard V?
            (5-option format; option E = SA_5OPT_E "Both I and II are strong")
            I:  Young students should not be burdened with exams that hamper
                natural growth → STRONG (valid child-development argument; up to
                Standard V = approximately ages 5–10, a formative period) ✓
            II: Without exams students won't study seriously; automatic promotion
                will affect them in future → STRONG (valid academic-preparedness
                argument; lack of evaluation can reduce motivation and readiness) ✓
            Both I & II are strong → (E) injected by frontend.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Statement_Argument_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Statement Argument"

# ── Option sets ───────────────────────────────────────────────────────────────
# Standard 4-option (Q10, Q11, Q13)
_STD_A = "Only argument I is strong. / केवल तर्क I ठोस है।"
_STD_B = "Only argument II is strong. / केवल तर्क II ठोस है।"
_STD_C = "Both I & II are strong. / तर्क I और II दोनों ठोस हैं।"
_STD_D = "Neither I nor II is strong. / न तो तर्क I और न ही तर्क II ठोस है।"

# Extended 5-option (Q14, Q15) — option E injected by frontend when
# option_c starts with "Either I or II".
_EXT_A = "Only argument I is strong. / केवल तर्क I मजबूत है।"
_EXT_B = "Only argument II is strong. / केवल तर्क II मजबूत है।"
_EXT_C = "Either I or II is strong. / या तो I या II मजबूत है।"
_EXT_D = "Neither I nor II is strong. / न तो I और न ही II मजबूत है।"
# _EXT_E "Both I and II are strong." injected by frontend as SA_5OPT_E.

QUESTIONS = [
    # ── Q10 — Standard 4-option ───────────────────────────────────────────────
    {
        "question_number": 10,
        "difficulty": "medium",
        "question_en": (
            "Statement: Should the admission to professional courses in India be "
            "given only on merit without any concession to any particular group "
            "of students?\n\n"
            "Arguments:\n"
            "I.  Yes, this will improve the quality of the professionals as they "
            "will be able to complete the courses successfully.\n"
            "II. No, this will keep large number of socially and economically "
            "backward students out of the reach of the professional courses."
        ),
        "question_hi": (
            "कथन: क्या भारत में प्रोफेशनल कोर्सों में प्रवेश विद्यार्थियों के "
            "किसी विशेष समूह को कोई रियायत दिए बिना सिर्फ मैरिट पर दिया जाना "
            "चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ, इससे छात्रों की गुणवत्ता में सुधार आएगा, क्योंकि ये "
            "कोर्सों को सफलतापूर्वक पूरा कर सकेंगे।\n"
            "II. नहीं, इससे सामाजिक और आर्थिक रूप से पिछड़े हुए अधिकांश "
            "विद्यार्थी प्रोफेशनल कोर्सों से वंचित हो जाएंगे।"
        ),
        "option_a": _STD_A,
        "option_b": _STD_B,
        "option_c": _STD_C,
        "option_d": _STD_D,
        "correct_answer": "C",
        # I:  Merit-based selection → qualified students → better completion rates
        #     → higher professional quality. STRONG ✓
        # II: Removing concessions → excludes socially/economically backward
        #     students → concrete educational inequality. STRONG ✓
    },
    # ── Q11 — Standard 4-option ───────────────────────────────────────────────
    {
        "question_number": 11,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should all the private sector banks be immediately merged "
            "with the public sector banks?\n\n"
            "Arguments:\n"
            "I.  No, the private sector banks are profit making entities and hence "
            "they should not be merged.\n"
            "II. Yes, this will safeguard the hard earned money of the customers "
            "and their interests will be secured."
        ),
        "question_hi": (
            "कथन: क्या निजी क्षेत्र के सभी बैंकों का तत्काल सार्वजनिक क्षेत्र "
            "के बैंकों में विलय कर दिया जाना चाहिए?\n\n"
            "तर्क:\n"
            "I.  नहीं, निजी क्षेत्र के बैंक लाभ कमाने वाली संस्थाएं हैं इसलिए "
            "उनका विलय नहीं किया जाना चाहिए।\n"
            "II. हाँ, इससे ग्राहकों को मेहनत से कमाया हुआ धन सुरक्षित हो जाएगा "
            "और उनके हित सुरक्षित रहेंगे।"
        ),
        "option_a": _STD_A,
        "option_b": _STD_B,
        "option_c": _STD_C,
        "option_d": _STD_D,
        "correct_answer": "B",
        # I:  "Profit-making entities should not be merged" → being profitable
        #     does not exempt a company from regulation or merger → WEAK ✗
        # II: Public sector backing would secure depositors' hard-earned money;
        #     directly relevant customer-protection benefit → STRONG ✓
    },
    # ── Q12 — Custom 4-option (4 arguments, "logical" wording) ────────────────
    {
        "question_number": 12,
        "difficulty": "hard",
        "question_en": (
            "Statement: Should the common entrance examinations for admission to "
            "professional subjects be abolished?\n\n"
            "Arguments:\n"
            "I.   Yes, this will save a lot of money.\n"
            "II.  Yes, many candidates who scored well in the specialty test do "
            "not do that well in the entrance test.\n"
            "III. Yes, rural candidates do not do well in common entrance tests.\n"
            "IV.  No, marks obtained in the specialty examination of different "
            "Boards and Universities are not uniform and comparable."
        ),
        "question_hi": (
            "कथन: क्या व्यावसायिक विषयों में भर्ती के लिए सामान्य प्रवेश "
            "परीक्षाएं समाप्त कर दी जानी चाहिए?\n\n"
            "तर्क:\n"
            "I.   हाँ, इससे बहुत धन की बचत होगी।\n"
            "II.  हाँ, अनेक प्रत्याशी जिन्होंने विशेषक परीक्षा में अच्छे अंक "
            "प्राप्त किए थे, प्रवेश परीक्षा में उतना अच्छा नहीं कर पाते।\n"
            "III. हाँ, ग्रामीण प्रत्याशी सामान्य प्रवेश परीक्षाओं में अच्छा "
            "नहीं कर पाते।\n"
            "IV.  नहीं, विभिन्न बोर्डों और विश्वविद्यालयों की विशेषक परीक्षा "
            "में प्राप्त अंक एक समान और तुलनीय नहीं होते।"
        ),
        # Custom options matching the original exam format (4 arguments, logical)
        "option_a": "Only argument I is logical. / केवल तर्क I युक्ति-युक्त है।",
        "option_b": (
            "Either II or III argument is logical. / "
            "तर्क II या III में से कोई भी एक युक्ति-युक्त है।"
        ),
        "option_c": "Only argument IV is logical. / केवल तर्क IV युक्ति-युक्त है।",
        "option_d": (
            "Only argument IV is not logical. / "
            "केवल तर्क IV युक्ति-युक्त नहीं है।"
        ),
        "correct_answer": "C",
        # I:   Saves money → cost saving alone does not justify abolition → WEAK ✗
        # II:  Specialty scorers not doing well in entrance → expected; entrance
        #      tests assess different aptitude than specialty exams → WEAK ✗
        # III: Rural candidates underperform → rural inequality ≠ reason to abolish
        #      entrance exams (better addressed by rural education or reservations)
        #      → WEAK ✗
        # IV:  Different board marks are not uniform/comparable → this is the core
        #      justification FOR having a common entrance exam as a standardised
        #      level-playing-field measure → STRONG ✓ → (C) Only IV is logical.
    },
    # ── Q13 — Standard 4-option ───────────────────────────────────────────────
    {
        "question_number": 13,
        "difficulty": "easy",
        "question_en": (
            "Statement: Should songs be removed from Indian films?\n\n"
            "Arguments:\n"
            "I.  Yes, Hollywood movies are hits without having any songs.\n"
            "II. No, songs help in increasing the length of the film."
        ),
        "question_hi": (
            "कथन: क्या भारतीय फिल्मों से गानों को हटाया जाना चाहिए।\n\n"
            "तर्क:\n"
            "I.  हाँ, हॉलीवुड की फिल्में बिना गाने के होने के बावजूद हिट होती "
            "हैं।\n"
            "II. नहीं, गाने फिल्म की लंबाई बढ़ाने में मदद करते हैं।"
        ),
        "option_a": _STD_A,
        "option_b": _STD_B,
        "option_c": _STD_C,
        "option_d": _STD_D,
        "correct_answer": "D",
        # I:  Irrelevant cross-cultural comparison; Hollywood and Indian films
        #     have fundamentally different cultural traditions → WEAK ✗
        # II: "Increases the length of the film" is not a merit; longer ≠ better;
        #     trivial and irrelevant reason to retain songs → WEAK ✗
    },
    # ── Q14 — Extended 5-option (option E injected by frontend) ───────────────
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": (
            "Statement: Should the prestigious people who have committed crime "
            "unknowingly be met with special treatment?\n\n"
            "Arguments:\n"
            "I.  Yes. The prestigious people do not commit crime intentionally.\n"
            "II. No, it is our policy that everybody is equal before the law."
        ),
        "question_hi": (
            "कथन: क्या अनजाने में अपराध करने वाले प्रतिष्ठित लोगों को एक "
            "विशेष प्रकार की सजा दी जानी चाहिए?\n\n"
            "तर्क:\n"
            "I.  हाँ। प्रतिष्ठित लोग जानबूझकर अपराध नहीं करते हैं।\n"
            "II. नहीं यह हमारी नीति है कि हर कोई कानून के समक्ष समान है।"
        ),
        # Extended 5-option format — frontend injects option E (SA_5OPT_E) because
        # option_c starts with "Either I or II".
        "option_a": _EXT_A,
        "option_b": _EXT_B,
        "option_c": _EXT_C,
        "option_d": _EXT_D,
        "correct_answer": "B",
        # I:  "Prestigious people don't commit crime intentionally" → intent is
        #     already considered by the existing legal framework; claiming prestige
        #     earns special status is not a valid argument → WEAK ✗
        # II: Equality before the law is a fundamental rule-of-law principle;
        #     status-based differential treatment directly undermines it → STRONG ✓
    },
    # ── Q15 — Extended 5-option (option E injected by frontend) ───────────────
    {
        "question_number": 15,
        "difficulty": "medium",
        "question_en": (
            "Statement: Should all the annual examinations up to Standard V "
            "be abolished?\n\n"
            "Arguments:\n"
            "I.  Yes. The young students should not be burdened with such "
            "examinations which hampers their natural growth.\n"
            "II. No. The students will not study seriously as they will get "
            "automatic promotion to the next class and this will affect them "
            "in future."
        ),
        "question_hi": (
            "कथन: क्या कक्षा V तक की सभी वार्षिक परीक्षाएं समाप्त कर दी जाए?\n\n"
            "तर्क:\n"
            "I.  हाँ। युवा छात्रों पर ऐसी परीक्षाओं का बोझ नहीं डाला जाना "
            "चाहिए जो उनके प्राकृतिक विकास को बाधित करती हैं।\n"
            "II. नहीं। छात्र गंभीरता से अध्ययन नहीं करेंगे क्योंकि उन्हें "
            "अगली कक्षा में स्वतः पदोन्नति मिलेगी और यह भविष्य में उन्हें "
            "प्रभावित करेगा।"
        ),
        # Extended 5-option format — frontend injects option E (SA_5OPT_E).
        "option_a": _EXT_A,
        "option_b": _EXT_B,
        "option_c": _EXT_C,
        "option_d": _EXT_D,
        "correct_answer": "E",
        # I:  Children up to Std V (ages 5–10) are in a formative developmental
        #     stage; exam pressure at this age can genuinely hamper natural growth
        #     and creativity → STRONG ✓
        # II: Without formal assessment, students may lack motivation to study
        #     seriously; automatic promotion without evaluation can create
        #     unprepared students in higher grades → STRONG ✓
        # Both I & II are strong → option (E) injected by frontend = SA_5OPT_E.
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
