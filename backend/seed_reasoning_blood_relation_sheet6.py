"""
seed_reasoning_blood_relation_sheet6.py
========================================
Seeds questions 73-78 (Blood Relation) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Blood Relation
Run     : python seed_reasoning_blood_relation_sheet6.py

Answer key verification:
  Q73: M+N = M is husband of N; N-P = N is sister of P; P×Q = P is daughter of Q
       -> Q is parent of P and N; M married N -> M is Q's son-in-law (दामाद)         -> C
  Q74: Man's nephew's maternal grandmother = lady; man's only brother is father
       of nephew -> lady is mother of nephew's mother = brother's wife's mother
       -> lady is mother-in-law of man's brother                                      -> B
  Q75: Parvathi -> Kalyani married Gopal -> Lakshmi -> Ashok + sibling -> Sita
       Sita is 3 generations below Gopal -> Sita is Gopal's great-granddaughter       -> C
  Q76: Seema = daughter-in-law of Sudhir; Seema = sister-in-law of Ramesh;
       Mohan = Sudhir's son & only brother of Ramesh -> Seema is Mohan's wife         -> D
  Q77: Lady L; L's father's only son = L's brother B; B's wife = Meera's mother-in-law
       -> Meera's husband = B's son = L's nephew                                      -> A
  Q78: Rohit = Rani's brother's son = Ram's son; Ram's wife = Suresh's sister
       -> Rohit is son of Suresh's sister -> Rohit is Suresh's nephew (भांजा)        -> D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401 — registers Subscription with SQLAlchemy

SOURCE  = "Gagan_Pratap_Reasoning_Blood_Relation_Sheet6"
SUBJECT = "Reasoning"
TOPIC   = "Blood Relation"

QUESTIONS = [
    # Q73
    {
        "question_number": 73,
        "difficulty": "medium",
        "question_en": (
            "If 'B×C' means 'B is the daughter of C', 'B+C' means 'B is the husband of C' "
            "and 'B–C' means 'B is the sister of C', then what does 'M+N–P×Q' mean?"
        ),
        "question_hi": (
            "यदि 'B×C' का अर्थ 'B, C की बेटी है', 'B+C' का अर्थ 'B, C का पति है' "
            "और 'B–C' का अर्थ 'B, C की बहन है', तो 'M+N–P×Q' का क्या अर्थ है?"
        ),
        "option_a": "M is the brother-in-law of Q/M, Q का साला/देवर है।",
        "option_b": "M is the uncle of Q/M, Q का चाचा है।",
        "option_c": "M is the son-in-law of Q/M, Q का दामाद है।",
        "option_d": "Q is the mother-in-law of M/Q, M की सास है।",
        "correct_answer": "C",
    },
    # Q74
    {
        "question_number": 74,
        "difficulty": "hard",
        "question_en": (
            "A man pointing to a photograph says, 'The lady in the photograph is my nephew's "
            "maternal grandmother.' How is the lady related to the man's one and only brother "
            "who is father of man's nephew?"
        ),
        "question_hi": (
            "एक आदमी ने एक फोटो की ओर इशारा करते हुए कहा, 'बस महिला मेरे भांजे की नानी है।' "
            "महिला का आदमी के एकलौते भाई से क्या रिश्ता है जो आदमी के भांजे का पिता है?"
        ),
        "option_a": "Nephew/भांजा",
        "option_b": "Mother-in-law/सास",
        "option_c": "Son/बेटा",
        "option_d": "Father/पिता",
        "correct_answer": "B",
    },
    # Q75
    {
        "question_number": 75,
        "difficulty": "hard",
        "question_en": (
            "Sita is the niece of Ashok. Ashok's mother is Lakshmi. Kalyani is Lakshmi's mother. "
            "Kalyani's husband is Gopal. Parvathi is the mother-in-law of Gopal. "
            "How is Sita related to Gopal?"
        ),
        "question_hi": (
            "सीता अशोक की भांजी है। अशोक की माँ लक्ष्मी है। कल्याणी लक्ष्मी की माँ है। "
            "कल्याणी का पति गोपाल है। पार्वती गोपाल की सास है। सीता का गोपाल से संबंध है?"
        ),
        "option_a": "Great grandson's daughter/परपोते की बेटी",
        "option_b": "Gopal is Sita's father/गोपाल सीता का पिता है",
        "option_c": "Sita is Gopal's great granddaughter/सीता गोपाल की परपोती है",
        "option_d": "Grand niece/पोती",
        "correct_answer": "C",
    },
    # Q76
    {
        "question_number": 76,
        "difficulty": "medium",
        "question_en": (
            "Seema is the daughter-in-law of Sudhir and sister-in-law of Ramesh. "
            "Mohan is the son of Sudhir and only brother of Ramesh. "
            "Find the relation between Seema and Mohan."
        ),
        "question_hi": (
            "सीमा सुधीर की बहू और रमेश की भाभी है। मोहन सुधीर का बेटा है और रमेश का एकलौता भाई है। "
            "सीमा और मोहन के बीच का रिश्ता बताइए।"
        ),
        "option_a": "Sister-in-law/नंद/भाभी",
        "option_b": "Aunt/चाची",
        "option_c": "Cousin/ममेरी भाई/बहन",
        "option_d": "Wife/पत्नी",
        "correct_answer": "D",
    },
    # Q77
    {
        "question_number": 77,
        "difficulty": "medium",
        "question_en": (
            "Pointing to a lady in a photograph, Meera said, 'her father's only son's wife "
            "is my mother-in-law.' How is Meera's husband related to that lady in the photo?"
        ),
        "question_hi": (
            "एक तस्वीर में एक महिला की ओर इशारा करते हुए, मीरा ने कहा, "
            "'उसके पिता के एकमात्र बेटे की पत्नी मेरी माँ है।' मीरा के पति का उस महिला से क्या संबंध है?"
        ),
        "option_a": "Nephew/भांजा",
        "option_b": "Uncle/चाचा",
        "option_c": "Son/बेटा",
        "option_d": "Father/पिता",
        "correct_answer": "A",
    },
    # Q78
    {
        "question_number": 78,
        "difficulty": "hard",
        "question_en": (
            "Suresh's sister is the wife of Ram. Ram is Rani's brother. Ram's father is Madhur. "
            "Sheetal is Ram's grandmother. Reena is Sheetal's daughter-in-law. "
            "Rohit is Rani's brother's son. Who is Rohit to Suresh?"
        ),
        "question_hi": (
            "सुरेश की बहन राम की पत्नी है। राम, रानी का भाई है। राम का पिता मधुर है। "
            "शीतल राम की दादी है। रीना शीतल की पुत्रवधू है। रोहित रानी के भाई का बेटा है। "
            "रोहित सुरेश से किस प्रकार संबंधित है?"
        ),
        "option_a": "Brother-in-law/बहनाई/जीजा",
        "option_b": "Son/बेटा",
        "option_c": "Brother/भाई",
        "option_d": "Nephew/भांजा",
        "correct_answer": "D",
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        existing_short = {
            row[0][:80]
            for row in db.query(Question.question_en)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        for d in QUESTIONS:
            if d["question_en"][:80] in existing_short:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue

            db.add(Question(
                subject    = SUBJECT,
                topic      = TOPIC,
                source_pdf = SOURCE,
                **d,
            ))
            inserted += 1

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
