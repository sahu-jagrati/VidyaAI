"""
seed_reasoning_blood_relation_sheet7.py
========================================
Seeds questions 79-86 (Blood Relation) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Blood Relation
Run     : python seed_reasoning_blood_relation_sheet7.py

Answer key verification:
  Q79: A's wife's only son = A's own son; girl = wife of A's son -> daughter-in-law -> B
  Q80: Ram=Preeti's brother; Neeta=Ram's sister -> Preeti & Neeta are sisters;
       Arun (Preeti's son) & Reema (Neeta's daughter) -> cousins (ममेरे भाई)       -> C
  Q81: Star A is father of Star B's son -> they share a child -> husband & wife      -> C
  Q82: Vijay's mother's only daughter = Vijay's sister; Ananda's mother = Vijay's
       sister -> Ananda is Vijay's nephew (भांजा)                                    -> C
  Q83: Man's wife = only daughter of woman's mother = the woman herself
       -> the woman IS the man's wife                                                 -> B
  Q84: Kala's brother's only sister = Kala herself; Mala = daughter of Kala         -> B
  Q85: No siblings -> father's son = person himself; man's father = person
       -> photo is of person's son                                                    -> A
  Q86: Her father = only son of Mathew's mother = Mathew himself
       -> photo is of Mathew's daughter                                               -> C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401 — registers Subscription with SQLAlchemy

SOURCE  = "Gagan_Pratap_Reasoning_Blood_Relation_Sheet7"
SUBJECT = "Reasoning"
TOPIC   = "Blood Relation"

QUESTIONS = [
    # Q79
    {
        "question_number": 79,
        "difficulty": "easy",
        "question_en": (
            "Pointing to a girl, A said 'She is the wife of the only son of my wife.' "
            "How is the girl related to A?"
        ),
        "question_hi": (
            "एक लड़की की ओर इशारा करते हुए A ने कहा 'वह मेरी पत्नी के इकलौते बेटे की पत्नी है।' "
            "वह लड़की A से कैसे संबंधित है?"
        ),
        "option_a": "Mother/माँ",
        "option_b": "Daughter-in-law/पुत्रवधू",
        "option_c": "Granddaughter/पोती",
        "option_d": "Wife/पत्नी",
        "correct_answer": "B",
    },
    # Q80
    {
        "question_number": 80,
        "difficulty": "medium",
        "question_en": (
            "Preeti has a son named Arun. Ram is Preeti's brother. Neeta too has a daughter "
            "named Reema. Neeta is Ram's sister. What is Arun's relationship to Reema?"
        ),
        "question_hi": (
            "प्रीति का एक बेटा है, जिसका नाम अरुण है। राम प्रीति का भाई है। नीता की एक बेटी भी "
            "है जिसका नाम रीमा है। नीता राम की बहन है। अरुण का रीमा से क्या रिश्ता है?"
        ),
        "option_a": "Brother/भाई",
        "option_b": "Nephew/भांजा",
        "option_c": "Cousin/ममेरे भाई",
        "option_d": "Uncle/चाचा",
        "correct_answer": "C",
    },
    # Q81
    {
        "question_number": 81,
        "difficulty": "medium",
        "question_en": (
            "There are 2 film stars. One is the father of the other's son. "
            "What is the relationship of the two with each other?"
        ),
        "question_hi": (
            "2 फिल्मी सितारे हैं। इनमें एक दूसरे के बेटे का पिता है। "
            "दोनों का आपस में क्या रिश्ता है?"
        ),
        "option_a": "Grandfather and Grandson/दादा और पोता",
        "option_b": "Grandfather and son/दादा और बेटा",
        "option_c": "Husband and wife/पति और पत्नी",
        "option_d": "Father and Son/पिता और बेटा",
        "correct_answer": "C",
    },
    # Q82
    {
        "question_number": 82,
        "difficulty": "easy",
        "question_en": (
            "Vijay says 'Ananda's mother is the only daughter of my mother.' "
            "How is Ananda related to Vijay?"
        ),
        "question_hi": (
            "विजय कहता है कि 'आनंद की माँ मेरी माँ की इकलौती बेटी है।' "
            "आनंद विजय से कैसे संबंधित है?"
        ),
        "option_a": "Brother/भाई",
        "option_b": "Father/पिता",
        "option_c": "Nephew/भांजा",
        "option_d": "Grand Father/नाना",
        "correct_answer": "C",
    },
    # Q83
    {
        "question_number": 83,
        "difficulty": "easy",
        "question_en": (
            "Introducing a man, a woman said, 'His wife is the only daughter of my mother.' "
            "How is the woman related to the man?"
        ),
        "question_hi": (
            "एक आदमी का परिचय कराते हुए एक महिला ने कहा, 'उसकी पत्नी मेरी माँ की इकलौती बेटी है।' "
            "महिला का आदमी से क्या संबंध है?"
        ),
        "option_a": "Sister-in-law/नंद/भाभी",
        "option_b": "Wife/पत्नी",
        "option_c": "Aunt/चाची",
        "option_d": "Mother-in-law/सास",
        "correct_answer": "B",
    },
    # Q84
    {
        "question_number": 84,
        "difficulty": "medium",
        "question_en": (
            "Pointing to Mala, Kala said, 'She is my brother's only sister's daughter.' "
            "How is Mala related to Kala?"
        ),
        "question_hi": (
            "माला की ओर इशारा करते हुए काला ने कहा, 'वह मेरे भाई की इकलौती बहन की बेटी है।' "
            "माला का काला से क्या संबंध है?"
        ),
        "option_a": "Mother/माँ",
        "option_b": "Daughter/बेटी",
        "option_c": "Aunt/चाची",
        "option_d": "Niece/भतीजी",
        "correct_answer": "B",
    },
    # Q85
    {
        "question_number": 85,
        "difficulty": "medium",
        "question_en": (
            "Looking at a photograph a person said 'I have no brother or sister but that "
            "man's father is my father's son.' Whose photograph was the person looking at?"
        ),
        "question_hi": (
            "एक तस्वीर पर नज़र डालते हुए एक व्यक्ति ने कहा 'मेरा कोई भाई और बहन नहीं है "
            "लेकिन उस आदमी का पिता मेरे पिता का बेटा है।' वह व्यक्ति किसकी तस्वीर देख रहा था?"
        ),
        "option_a": "His son's/उसके बेटे की",
        "option_b": "His nephew/उसके भांजे",
        "option_c": "His father's/उसके पिता",
        "option_d": "His own/स्वयं की",
        "correct_answer": "A",
    },
    # Q86
    {
        "question_number": 86,
        "difficulty": "easy",
        "question_en": (
            "Mathew told his friend Sham, pointing to a photograph, "
            "'Her father is the only son of my mother.' The photograph is of whom?"
        ),
        "question_hi": (
            "मैथ्यू ने अपने दोस्त श्याम को एक तस्वीर की ओर इशारा करते हुए कहा, "
            "'उसके पिता मेरी माँ के इकलौते बेटे हैं।' वह तस्वीर किसकी है?"
        ),
        "option_a": "Mathew's niece/मैथ्यू की भतीजी",
        "option_b": "Mathew's mother/मैथ्यू की माँ",
        "option_c": "Mathew's daughter/मैथ्यू की बेटी",
        "option_d": "Mathew's sister/मैथ्यू की बहन",
        "correct_answer": "C",
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
