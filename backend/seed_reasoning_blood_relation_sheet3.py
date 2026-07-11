"""
seed_reasoning_blood_relation_sheet3.py
========================================
Seeds questions 19-27 (Blood Relation) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Blood Relation
Run     : python seed_reasoning_blood_relation_sheet3.py

Answer key verification:
  Q19: A&B siblings; F=A's son; F's child -> B is same generation as A (F's child's grandfather).
       B is at grandfather level relative to F's child                             -> D
  Q20: Woman's father's sister = man's Mousi -> man's mother is woman's father's
       sister -> woman's father = man's maternal uncle -> woman = man's maternal cousin -> C
  Q21: D=C's father; C=A&B's mother; E=B's son -> D is 3 generations above E
       -> D is E's great grandfather                                               -> C
  Q22: X&Y are A's children; A is X's father but Y is not A's son -> Y is A's daughter -> D
  Q23: A&B siblings; E=B's son -> A is E's uncle (father's/mother's brother)      -> C
  Q24: Man in photo is father of "only daughter of my mother" = Manisha herself
       -> he is Manisha's father -> Manisha is his daughter                        -> B
  Q25: F is C's niece; A is F's son; from F's perspective F calls C "aunt"        -> B
  Q26: B&A siblings; F=A's son -> B is F's aunt (sibling of F's father A)         -> A
  Q27: A=B's son; B&C are sisters; E=C&B's mother; D=E's son=B's brother
       -> D is A's maternal uncle (मामा)                                           -> A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401 — registers Subscription with SQLAlchemy

SOURCE  = "Gagan_Pratap_Reasoning_Blood_Relation_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Blood Relation"

QUESTIONS = [
    # Q19
    {
        "question_number": 19,
        "difficulty": "hard",
        "question_en": (
            "A is B's brother. C is A's mother. D is C's father. F is A's son. "
            "How is B related to F's child?"
        ),
        "question_hi": (
            "A, B का भाई है। C, A की माँ है। D, C का पिता है। F, A का पुत्र है। "
            "B, F के बच्चे से कैसे संबंधित है?"
        ),
        "option_a": "Aunt/चाची",
        "option_b": "Cousin/चचेरे भाई-बहन",
        "option_c": "Nephew/भतीजा",
        "option_d": "Grandfather/दादा",
        "correct_answer": "D",
    },
    # Q20
    {
        "question_number": 20,
        "difficulty": "hard",
        "question_en": (
            "A man introduced a woman and told, 'Her mother's husband's sister is my aunt (Mousi).' "
            "What is the relation of that woman with the man?"
        ),
        "question_hi": (
            "एक आदमी ने एक महिला का परिचय दिया और कहा, 'उसकी माँ की पति की बहन मेरी मौसी है।' "
            "उस महिला का आदमी से क्या संबंध है?"
        ),
        "option_a": "Sister/बहन",
        "option_b": "Mother/माता",
        "option_c": "Maternal Cousin/ममेरी बहन",
        "option_d": "Son/पुत्र",
        "correct_answer": "C",
    },
    # Q21
    {
        "question_number": 21,
        "difficulty": "medium",
        "question_en": (
            "A is B's brother. C is A's mother. D is C's father. E is B's son. "
            "How is D related to E?"
        ),
        "question_hi": (
            "A, B का भाई है। C, A की माँ है। D, C का पिता है। E, B का पुत्र है। "
            "D, E से कैसे संबंधित है?"
        ),
        "option_a": "Grandson/पोता",
        "option_b": "Great Grandson/परपोता",
        "option_c": "Great Grandfather/परनाना",
        "option_d": "Grandfather/दादा",
        "correct_answer": "C",
    },
    # Q22
    {
        "question_number": 22,
        "difficulty": "easy",
        "question_en": (
            "X and Y are the children of A. A is the father of X but Y is not his son. "
            "How is Y related to A?"
        ),
        "question_hi": (
            "X और Y, A के बच्चे हैं। A, X का पिता है लेकिन Y उसका बेटा नहीं है। "
            "Y, A से कैसे संबंधित है?"
        ),
        "option_a": "Sister/बहन",
        "option_b": "Brother/भाई",
        "option_c": "Son/बेटा",
        "option_d": "Daughter/बेटी",
        "correct_answer": "D",
    },
    # Q23
    {
        "question_number": 23,
        "difficulty": "easy",
        "question_en": (
            "A is B's brother. C is A's mother. D is C's father. E is B's son. "
            "How is E related to A?"
        ),
        "question_hi": (
            "A, B का भाई है। C, A की माँ है। D, C का पिता है। E, B का पुत्र है। "
            "E, A से कैसे संबंधित है?"
        ),
        "option_a": "Cousin/चचेरे भाई/बहन",
        "option_b": "Nephew/भतीजा",
        "option_c": "Uncle/चाचा",
        "option_d": "Grandson/पोता",
        "correct_answer": "C",
    },
    # Q24
    {
        "question_number": 24,
        "difficulty": "easy",
        "question_en": (
            "Pointing to a man in the photograph Manisha said, "
            "'He is the father of the only daughter of my mother.' "
            "How is Manisha related to that man?"
        ),
        "question_hi": (
            "तस्वीर में एक आदमी को और इशारा करते हुए मनीषा ने कहा, "
            "'वह मेरी माँ की इकलौती बेटी का पिता है।' मनीषा उस आदमी से कैसे संबंधित है?"
        ),
        "option_a": "Mother/माता",
        "option_b": "Daughter/बेटी",
        "option_c": "Aunt/चाची",
        "option_d": "Niece/भतीजी",
        "correct_answer": "B",
    },
    # Q25
    {
        "question_number": 25,
        "difficulty": "hard",
        "question_en": (
            "D is son of C and brother of E. F is niece of C. "
            "The father of B has two children, i.e., one son and one daughter. "
            "If A is son of F, then how is F related to C?"
        ),
        "question_hi": (
            "D, C का बेटा है और E का भाई है। F, C की भांजी है। "
            "B के पिता के दो बच्चे हैं अर्थात् एक बेटा और एक बेटी। "
            "यदि A, F का पुत्र है, तो F, C से कैसे संबंधित है?"
        ),
        "option_a": "Cousin/चचेरे भाई/बहन",
        "option_b": "Aunt (Paternal)/चाची",
        "option_c": "Sister-in-law/भाभी",
        "option_d": "Sister/बहन",
        "correct_answer": "B",
    },
    # Q26
    {
        "question_number": 26,
        "difficulty": "medium",
        "question_en": (
            "A is B's brother. C is A's mother. D is C's father. B is D's grand-daughter. "
            "How is B related to F who is A's son?"
        ),
        "question_hi": (
            "A, B का भाई है। C, A की माँ है। D, C का पिता है। B, D की पोती है। "
            "B, A के बेटे F से कैसे संबंधित है?"
        ),
        "option_a": "Aunt/चाची",
        "option_b": "Cousin/चचेरे भाई/बहन",
        "option_c": "Niece/भांजी",
        "option_d": "Grandaunt/दादी",
        "correct_answer": "A",
    },
    # Q27
    {
        "question_number": 27,
        "difficulty": "medium",
        "question_en": (
            "A is the son of B, while B and C are sisters to one another. "
            "E is the mother of C. If D is the son of E, "
            "which of the following statements is correct?"
        ),
        "question_hi": (
            "A, B का पुत्र है, जबकि B और C एक-दूसरे की बहन हैं। "
            "E, C की माँ है। यदि D, E का पुत्र है, "
            "तो निम्नलिखित में से कौन सा कथन सही है?"
        ),
        "option_a": "D is the maternal uncle of A/D, A का मामा है",
        "option_b": "E is the brother of B/E, B का भाई है",
        "option_c": "D is the cousin of A/D, A का चचेरा भाई/बहन है",
        "option_d": "B and D are brothers/B और D भाई हैं",
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
