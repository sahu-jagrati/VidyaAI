"""
seed_reasoning_blood_relation_sheet8.py
========================================
Seeds questions 87-95 (Blood Relation) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Blood Relation
Run     : python seed_reasoning_blood_relation_sheet8.py

Answer key verification:
  Q87: Raghu & Babu = twins; Reema = their sister; Rajesh = Lakshmi's husband
       = Reema's father; Rajan = Reema's husband -> Rajesh is Rajan's father-in-law -> A
  Q88: Sheela = Ram's wife; Ram = Ravi's brother; Shanthi = Ravi & Ram's mother
       -> Sheela is Shanthi's daughter-in-law                                        -> B
  Q89: Kala = Dilip's wife; Rohit = Kala's brother -> Dilip is Rohit's जीजा
       (brother-in-law / sister's husband)                                            -> B
  Q90: Govind = Ravi's brother; Prabhu = Govind's brother -> Prabhu also = Ravi's
       brother; Kusuma = Ravi's wife -> Prabhu is Kusuma's देवर (brother-in-law)    -> C
  Q91: My father's only son = Gopal himself; Govind's father = Gopal
       -> Gopal is Govind's father                                                    -> D
  Q92: Rajiv = Arun's brother; Arun = Sonia's son -> Rajiv also = Sonia's son;
       Sonia = Sunil's sister -> Rajiv is Sunil's nephew (भांजा)                    -> D
  Q93: Sunil = Kesav's son; Maruti = Simran's son; Simran = Kesav's sister
       -> Sunil & Maruti are cousins (ममेरे भाई)                                    -> B
  Q94: Z = W's son; W = V's wife -> V = Z's father; Y = Z's wife
       -> V is Y's father-in-law (ससुर)                                              -> C
  Q95: C = A's father's भांजा (paternal aunt's son); D = A's only चाचा's child;
       C's parent and D's parent are siblings -> C and D are cousins (चचेरे)        -> A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401 — registers Subscription with SQLAlchemy

SOURCE  = "Gagan_Pratap_Reasoning_Blood_Relation_Sheet8"
SUBJECT = "Reasoning"
TOPIC   = "Blood Relation"

QUESTIONS = [
    # Q87
    {
        "question_number": 87,
        "difficulty": "medium",
        "question_en": (
            "Raghu and Babu are twins. Babu's sister is Reema. Reema's husband is Rajan. "
            "Raghu's mother is Lakshmi. Lakshmi's husband is Rajesh. "
            "How is Rajesh related to Rajan?"
        ),
        "question_hi": (
            "राघु और बाबू जुड़वाँ हैं। बाबू की बहन रीमा है। रीमा का पति राजन है। "
            "राघु की माँ लक्ष्मी है। लक्ष्मी के पति राजेश हैं। राजेश का राजन से क्या संबंध है?"
        ),
        "option_a": "Father-in-law/ससुर",
        "option_b": "Cousin/चचेरे भाई",
        "option_c": "Son-in-law/दामाद",
        "option_d": "Uncle/चाचा",
        "correct_answer": "A",
    },
    # Q88
    {
        "question_number": 88,
        "difficulty": "medium",
        "question_en": (
            "Sheela is Ravi's sister-in-law. Ram is Ravi's brother. Ram's wife is Sheela. "
            "Deepa is Ravi's sister. Deepa's mother is Shanthi. "
            "How is Sheela related to Shanthi?"
        ),
        "question_hi": (
            "शीला रवि की भाभी है। राम रवि के भाई हैं। राम की पत्नी शीला है। "
            "दीपा रवि की बहन है। दीपा की माँ शांति है। शीला का शांति से क्या संबंध है?"
        ),
        "option_a": "Mother-in-law/सास",
        "option_b": "Daughter-in-law/पुत्रवधू",
        "option_c": "Granddaughter/पोती",
        "option_d": "Daughter/बेटी",
        "correct_answer": "B",
    },
    # Q89
    {
        "question_number": 89,
        "difficulty": "easy",
        "question_en": (
            "Tarun is the father of Rohit. Rohit is the brother of Kala. "
            "Kala is the wife of Dilip. How is Dilip related to Rohit?"
        ),
        "question_hi": (
            "तरुण रोहित के पिता हैं। रोहित कला का भाई है। काला दिलीप की पत्नी है। "
            "दिलीप, रोहित से कैसे संबंधित है?"
        ),
        "option_a": "Brother/भाई",
        "option_b": "Brother-in-law/जीजा",
        "option_c": "Son/बेटा",
        "option_d": "Uncle/चाचा",
        "correct_answer": "B",
    },
    # Q90
    {
        "question_number": 90,
        "difficulty": "easy",
        "question_en": (
            "Kusuma is the wife of Ravi. Govind and Prabhu are brothers. "
            "Govind is the brother of Ravi. How is Prabhu related to Kusuma?"
        ),
        "question_hi": (
            "कुसुमा रवि की पत्नी है। गोविंद और प्रभु भाई हैं। गोविंद रवि का भाई है। "
            "प्रभु कुसुमा के कैसे हैं?"
        ),
        "option_a": "Cousin/चचेरा भाई",
        "option_b": "Brother/भाई",
        "option_c": "Brother-in-law/देवर",
        "option_d": "Uncle/चाचा",
        "correct_answer": "C",
    },
    # Q91
    {
        "question_number": 91,
        "difficulty": "easy",
        "question_en": (
            "Gopal said, pointing to Govind, 'His father is my father's only son.' "
            "How is Gopal related to Govind?"
        ),
        "question_hi": (
            "गोपाल ने गोविंद की ओर इशारा करते हुए कहा 'उसके पिता मेरे पिता के इकलौते पुत्र हैं।' "
            "गोपाल का गोविंद से कैसे संबंध है?"
        ),
        "option_a": "Grandfather/नाना",
        "option_b": "Grandson/पोता",
        "option_c": "Son/बेटा",
        "option_d": "Father/पिता",
        "correct_answer": "D",
    },
    # Q92
    {
        "question_number": 92,
        "difficulty": "medium",
        "question_en": (
            "Rajiv is the brother of Arun. Sonia is the sister of Sunil. "
            "Arun is the son of Sonia. How is Rajiv related to Sunil?"
        ),
        "question_hi": (
            "राजीव अरुण का भाई है। सोनिया सुनील की बहन है। अरुण सोनिया का बेटा है। "
            "राजीव का सुनील से क्या संबंध है?"
        ),
        "option_a": "Son/बेटा",
        "option_b": "Brother/भाई",
        "option_c": "Father/पिता",
        "option_d": "Nephew/भांजा",
        "correct_answer": "D",
    },
    # Q93
    {
        "question_number": 93,
        "difficulty": "medium",
        "question_en": (
            "Sunil is the son of Kesav. Simran, Kesav's sister, has a son Maruti "
            "and daughter Sita. Prem is the maternal uncle of Maruti. "
            "How is Sunil related to Maruti?"
        ),
        "question_hi": (
            "सुनील केसव का बेटा है। केसव की बहन सिमरन का एक बेटा मारुती और बेटी सीता है। "
            "प्रेम मारुती का मामा है। सुनील का मारुती से क्या संबंध है?"
        ),
        "option_a": "Nephew/भतीजा",
        "option_b": "Cousin/ममेरे भाई",
        "option_c": "Uncle/चाचा",
        "option_d": "Brother/भाई",
        "correct_answer": "B",
    },
    # Q94
    {
        "question_number": 94,
        "difficulty": "medium",
        "question_en": (
            "X is Y's brother. Y is Z's wife. Z is W's son. W is the wife of V. "
            "What is the relation of V with Y?"
        ),
        "question_hi": (
            "X, Y का भाई है। Y, Z की पत्नी है। Z, W का बेटा है। W, V की पत्नी है। "
            "V का Y से क्या संबंध है?"
        ),
        "option_a": "Grandfather/नाना",
        "option_b": "Husband/पति",
        "option_c": "Father-in-law/ससुर",
        "option_d": "Father/पिता",
        "correct_answer": "C",
    },
    # Q95
    {
        "question_number": 95,
        "difficulty": "hard",
        "question_en": (
            "A said to B, 'C is my father's nephew. D is my only uncle's child, "
            "but C is not my brother.' What is the relation of D with C?"
        ),
        "question_hi": (
            "A ने B से कहा, 'C मेरे पिता का भांजा है। D, मेरे इकलौते चाचा का बच्चा है, "
            "लेकिन C मेरा भाई नहीं है।' D, C से कैसे संबंधित है?"
        ),
        "option_a": "Cousin/चचेरा",
        "option_b": "Sister/बहन",
        "option_c": "Mother/माता",
        "option_d": "Niece/भतीजी",
        "correct_answer": "A",
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
