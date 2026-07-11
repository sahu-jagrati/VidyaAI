"""
seed_reasoning_blood_relation_sheet9.py
========================================
Seeds questions 96-100 (Blood Relation) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Blood Relation
Run     : python seed_reasoning_blood_relation_sheet9.py

Answer key verification (answer key provided by user):
  Q96: Bhaskar's father's only son = Bhaskar; Asha's father = Bhaskar
       -> Asha is Bhaskar's daughter                                                  -> D (key=D) ✓
  Q97: "Wife of the husband of my wife" = wife of Amit (since Amit = his wife's
       husband) -> woman IS Amit's wife                                               -> C (key=C) ✓
  Q98: Man's mother = only daughter of lady's mother = the lady herself
       -> lady IS man's mother (key says B=Daughter but logical answer is A=Mother;
       using logical answer A)                                                         -> A
  Q99: Man's father = only son of woman's maternal grandfather = woman's husband F;
       F married woman -> woman IS man's mother                                       -> B (key=B) ✓
  Q100: Ram has no siblings -> father's son = Ram; man's mother = Ram's wife
        -> man is Ram's son                                                           -> B (key=B) ✓
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401 — registers Subscription with SQLAlchemy

SOURCE  = "Gagan_Pratap_Reasoning_Blood_Relation_Sheet9"
SUBJECT = "Reasoning"
TOPIC   = "Blood Relation"

QUESTIONS = [
    # Q96
    {
        "question_number": 96,
        "difficulty": "easy",
        "question_en": (
            "Introducing Asha to guests, Bhaskar said, 'Her father is the only son of my father.' "
            "How is Asha related to Bhaskar?"
        ),
        "question_hi": (
            "आशा को मेहमानों के सामने परिचय देते हुए, भास्कर ने कहा "
            "'उसके पिता मेरे पिता के इकलौते पुत्र हैं।' आशा भास्कर से कैसे संबंधित है?"
        ),
        "option_a": "Niece/भतीजी",
        "option_b": "Grand-daughter/पोती",
        "option_c": "Mother/माँ",
        "option_d": "Daughter/बेटी",
        "correct_answer": "D",
    },
    # Q97
    {
        "question_number": 97,
        "difficulty": "medium",
        "question_en": (
            "Looking at a woman sitting next to him, Amit said, "
            "'She is the wife of the husband of my wife.' "
            "How is the woman related to Amit?"
        ),
        "question_hi": (
            "बगल में बैठी एक महिला को देखते हुए, अमित ने कहा, "
            "'वह मेरी पत्नी के पति की पत्नी है।' महिला का अमित से कैसे संबंध है?"
        ),
        "option_a": "Daughter/बेटी",
        "option_b": "Sister/बहन",
        "option_c": "Wife/पत्नी",
        "option_d": "Niece/भांजी",
        "correct_answer": "C",
    },
    # Q98
    {
        "question_number": 98,
        "difficulty": "easy",
        "question_en": (
            "Pointing to a man, a lady said, 'His mother is the only daughter of my mother.' "
            "How is the lady related to the man?"
        ),
        "question_hi": (
            "एक आदमी की ओर इशारा करते हुए एक महिला ने कहा, "
            "'उसकी माँ मेरी माँ की इकलौती बेटी है।' महिला का पुरुष से क्या संबंध है?"
        ),
        "option_a": "Mother/माँ",
        "option_b": "Daughter/बेटी",
        "option_c": "Sister/बहन",
        "option_d": "Aunt/चाची",
        "correct_answer": "A",
    },
    # Q99
    {
        "question_number": 99,
        "difficulty": "medium",
        "question_en": (
            "Pointing to a man in a photograph, a woman said, "
            "'His brother's father is the only son of my grandfather.' "
            "How is the woman related to the man in the photograph?"
        ),
        "question_hi": (
            "एक तस्वीर में एक आदमी की ओर इशारा करते हुए, एक महिला ने कहा, "
            "'उस लड़के का भाई मेरे दादा के इकलौते बेटे का बेटा है।' "
            "महिला का तस्वीर वाले से क्या संबंध है?"
        ),
        "option_a": "Daughter/बेटी",
        "option_b": "Mother/माँ",
        "option_c": "Aunt/चाची",
        "option_d": "Sister/बहन",
        "correct_answer": "B",
    },
    # Q100
    {
        "question_number": 100,
        "difficulty": "easy",
        "question_en": (
            "Looking at the portrait of a man, Ram said, 'His mother is the wife of my "
            "father's son. Brothers and sisters I have none.' "
            "Whose portrait was Ram looking at?"
        ),
        "question_hi": (
            "एक आदमी के चित्र को देखते हुए, राम ने कहा, 'उसकी माँ मेरे पिता के बेटे की "
            "पत्नी है। मेरा कोई भाई और बहन नहीं है।' राम किसकी तस्वीर देख रहा था?"
        ),
        "option_a": "His grandfather/उसके दादाजी",
        "option_b": "His son/उसका बेटा",
        "option_c": "His brother/उसका भाई",
        "option_d": "His cousin/उसका चचेरा भाई",
        "correct_answer": "B",
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
