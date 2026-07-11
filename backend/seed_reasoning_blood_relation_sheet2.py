"""
seed_reasoning_blood_relation_sheet2.py
========================================
Seeds questions 9-18 (Blood Relation) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Blood Relation
Run     : python seed_reasoning_blood_relation_sheet2.py

Answer key verification:
  Q9:  F is A's brother; K is F's sister (=A's sister); G and C are A's children.
       Uncle of G = brother of A = F                                               -> D
  Q10: A&B brothers; C=A's father; D=C's sister; E=D's mother -> E is C's mother
       -> E is B's paternal grandmother (दादी)                                     -> C
  Q11: C=B's wife; E=C's son (B&C's son); A=B's brother; D=A's child
       -> E and D are cousins (children of brothers B & A)                         -> D
  Q12: O=P's husband; M=P's son -> M is O's son                                   -> A
  Q13: R=X&Y's father; S=T's brother; S=X's maternal uncle (S is brother of X's mother)
       -> T is S's sibling; T is X's mother = R's wife                             -> B
  Q14: A=father of B,D,E; C=B's daughter; E=A's son
       -> E is C's uncle; C is E's niece -> Niece and uncle                        -> C
  Q15: P=Q's husband; R=mother of S and Q -> R is Q's mother -> R is P's mother-in-law -> D
  Q16: X=Y's husband; W=X&Y's daughter; Z=W's husband; N=Z&W's daughter
       -> N is Y's granddaughter                                                    -> D
  Q17: B=paternal uncle of C; C=A's daughter -> B is brother of A's father
       Wait -- B is C's paternal uncle = brother of C's father = brother of A      -> A
  Q18: Shikha's mother's देवर (husband's brother) = Shikha's father's brother (चाचा)
       Girl = daughter of Shikha's paternal uncle -> Cousin (चचेरी बहन)           -> C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401 — needed for SQLAlchemy mapper

SOURCE  = "Gagan_Pratap_Reasoning_Blood_Relation_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Blood Relation"

QUESTIONS = [
    # Q9
    {
        "question_number": 9,
        "difficulty": "medium",
        "question_en": (
            "(I) F is the brother of A. "
            "(II) C is the daughter of A. "
            "(III) K is the sister of F. "
            "(IV) G is the brother of C. "
            "Who is the uncle of G?"
        ),
        "question_hi": (
            "(I) F, A का भाई है। "
            "(II) C, A की बेटी है। "
            "(III) K, F की बहन है। "
            "(IV) G, C का भाई है। "
            "G का चाचा कौन है?"
        ),
        "option_a": "A",
        "option_b": "C",
        "option_c": "K",
        "option_d": "F",
        "correct_answer": "D",
    },
    # Q10
    {
        "question_number": 10,
        "difficulty": "medium",
        "question_en": "A is B's brother. C is A's father. D is C's sister and E is D's mother. How is E related to B?",
        "question_hi": "A, B का भाई है। C, A का पिता है। D, C की बहन है और E, D की माँ है। B से E कैसे संबंधित है?",
        "option_a": "Granddaughter/पोती",
        "option_b": "Great-grandmother/परनानी",
        "option_c": "Grandmother/दादी",
        "option_d": "Daughter/बेटी",
        "correct_answer": "C",
    },
    # Q11
    {
        "question_number": 11,
        "difficulty": "easy",
        "question_en": "C is wife of B. E is the son of C. A is the brother of B and father of D. What is the relationship of E to D?",
        "question_hi": "C, B की पत्नी है। E, C का पुत्र है। A, B का भाई है और D का पिता है। E का D से क्या संबंध है?",
        "option_a": "Mother/माँ",
        "option_b": "Sister/बहन",
        "option_c": "Brother/भाई",
        "option_d": "Cousin/चचेरा भाई",
        "correct_answer": "D",
    },
    # Q12
    {
        "question_number": 12,
        "difficulty": "easy",
        "question_en": "M is the son of P. Q is the grand-daughter of O who is the husband of P. How is M related to O?",
        "question_hi": "M, P का पुत्र है। Q, O की पोती है, जो P का पति है। M, O से कैसे संबंधित है?",
        "option_a": "Son/पुत्र",
        "option_b": "Daughter/बेटी",
        "option_c": "Mother/माँ",
        "option_d": "Father/पिता",
        "correct_answer": "A",
    },
    # Q13
    {
        "question_number": 13,
        "difficulty": "medium",
        "question_en": "X and Y are brothers. R is the father of Y. S is the brother of T and maternal uncle of X. What is T to R?",
        "question_hi": "X और Y भाई हैं। R, Y का पिता है। S, T का भाई है और X का मामा है। T का R से क्या संबंध है?",
        "option_a": "Mother/माँ",
        "option_b": "Wife/पत्नी",
        "option_c": "Sister/बहन",
        "option_d": "Brother/भाई",
        "correct_answer": "B",
    },
    # Q14
    {
        "question_number": 14,
        "difficulty": "medium",
        "question_en": "A is the father of B. C is the daughter of B. D is the brother of B. E is the son of A. What is the relationship between C and E?",
        "question_hi": "A, B का पिता है। C, B की बेटी है। D, B का भाई है। E, A का पुत्र है। C और E के बीच क्या संबंध है?",
        "option_a": "Brother and sister/भाई और बहन",
        "option_b": "Cousins/चचेरे भाई-बहन",
        "option_c": "Niece and uncle/भांजी और चाचा",
        "option_d": "Uncle and aunt/चाचा और चाची",
        "correct_answer": "C",
    },
    # Q15
    {
        "question_number": 15,
        "difficulty": "easy",
        "question_en": "If P is the husband of Q and R is the mother of S and Q. What is R to P?",
        "question_hi": "यदि P, Q का पति है और R, S और Q की माँ है। R का P से क्या संबंध है?",
        "option_a": "Mother/माँ",
        "option_b": "Sister/बहन",
        "option_c": "Aunt/चाची",
        "option_d": "Mother-in-law/सास",
        "correct_answer": "D",
    },
    # Q16
    {
        "question_number": 16,
        "difficulty": "easy",
        "question_en": "X is the husband of Y. W is the daughter of X. Z is the husband of W. N is the daughter of Z. What is the relation of N to Y?",
        "question_hi": "X, Y का पति है। W, X की बेटी है। Z, W का पति है। N, Z की बेटी है। N का Y से क्या संबंध है?",
        "option_a": "Cousin/चचेरे भाई/बहन",
        "option_b": "Niece/भतीजी",
        "option_c": "Daughter/बेटी",
        "option_d": "Granddaughter/नातिन",
        "correct_answer": "D",
    },
    # Q17
    {
        "question_number": 17,
        "difficulty": "medium",
        "question_en": (
            "'A' reads a book and finds the name of the author familiar. "
            "The author 'B' is the paternal uncle of 'C'. "
            "'C' is the daughter of 'A'. How is 'B' related to 'A'?"
        ),
        "question_hi": (
            "'A' एक किताब पढ़ता है और लेखक के नाम से परिचित है। "
            "लेखक 'B', 'C' का पैतृक चाचा है। "
            "'C', 'A' की बेटी है। B, 'A' से कैसे संबंधित है?"
        ),
        "option_a": "Brother/भाई",
        "option_b": "Sister/बहन",
        "option_c": "Father/पिता",
        "option_d": "Uncle/चाचा",
        "correct_answer": "A",
    },
    # Q18
    {
        "question_number": 18,
        "difficulty": "medium",
        "question_en": (
            "Shikha told Aarushi, 'The girl I met yesterday at the beach was the youngest "
            "daughter of the brother-in-law of my mother.' How is the girl related to Shikha?"
        ),
        "question_hi": (
            "शिखा ने आरुषि को कहा, 'वह लड़की जिससे मैं कल मिली थी, "
            "मेरी माँ के देवर की सबसे छोटी बेटी है।' लड़की शिखा से कैसे संबंधित है?"
        ),
        "option_a": "Sister/बहन",
        "option_b": "Niece/भतीजी",
        "option_c": "Cousin/चचेरी बहन",
        "option_d": "Grand-daughter/पोती",
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
