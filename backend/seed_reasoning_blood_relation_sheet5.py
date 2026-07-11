"""
seed_reasoning_blood_relation_sheet5.py
========================================
Seeds questions 49-58 (Blood Relation) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Blood Relation
Run     : python seed_reasoning_blood_relation_sheet5.py

Answer key verification:
  Q49: A=B's sister; G=B&D's daughter -> G is A's niece                           -> C
  Q50: Z=P's wife; P=A's son -> Z is A's daughter-in-law                          -> A
  Q51: M=P's son; O=P's husband; Q=O's granddaughter -> M is Q's father           -> A
  Q52: A=B's mother; C=A's son -> C and B are siblings; E=B's daughter
       -> E's uncle = B's sibling = C                                              -> A
  Q53: "Shyam's daughter's paternal grandmother" = Shyam's mother;
       "daughter-in-law's husband" = Shyam; Ram = Shyam's brother;
       bridegroom = Ram's son = Shyam's nephew                                     -> D
  Q54: P+Q=P is father of Q; Q*R=Q is brother of R; R-S=R is mother of S
       -> Q is R's brother; R is S's mother -> Q is S's maternal uncle (मामा)     -> B
  Q55: T=R's wife; S=R's son; S=L's husband -> L is T's daughter-in-law           -> C
  Q56: J3L=J is daughter of L; L9N=L is sister of N; N3O=N is daughter of O;
       O5K=O is father of K -> J(L's daughter) is K(O's son)'s niece              -> C
  Q57: +brother; -sister; *mother. P*O -> P is O's mother; O+S -> O is S's
       brother -> P is also S's mother; S*Q -> S is Q's mother -> P is Q's granny -> C
  Q58: A=B's father; B not son -> B is daughter; D=A's wife -> D is B's mother    -> C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Blood_Relation_Sheet5"
SUBJECT = "Reasoning"
TOPIC   = "Blood Relation"

QUESTIONS = [
    # Q49
    {
        "question_number": 49,
        "difficulty": "easy",
        "question_en": (
            "'A' is the sister of 'B' who is married to 'D'. "
            "'B' and 'D' have a daughter 'G'. How is 'G' related to 'A'?"
        ),
        "question_hi": (
            "'A', 'B' की बहन है जो D से विवाहित है। "
            "B और D की एक बेटी G है। G, A से कैसे संबंधित है?"
        ),
        "option_a": "Sister/बहन",
        "option_b": "Daughter/बेटी",
        "option_c": "Niece/भतीजी",
        "option_d": "Cousin/चचेरी भाई/बहन",
        "correct_answer": "C",
    },
    # Q50
    {
        "question_number": 50,
        "difficulty": "easy",
        "question_en": (
            "If M is the sister of Z, Z is the wife of P and P is the son of A, "
            "how is Z related to A?"
        ),
        "question_hi": (
            "यदि M, Z की बहन है, Z, P की पत्नी है और P, A का पुत्र है, "
            "तो Z, A से कैसे संबंधित है?"
        ),
        "option_a": "Daughter-in-law/पुत्रवधू",
        "option_b": "Daughter/बेटी",
        "option_c": "Wife/पत्नी",
        "option_d": "Mother/माँ",
        "correct_answer": "A",
    },
    # Q51
    {
        "question_number": 51,
        "difficulty": "medium",
        "question_en": (
            "M is son of P. Q is the grand-daughter of O who is the husband of P. "
            "How is M related to Q?"
        ),
        "question_hi": (
            "M, P का पुत्र है। Q, O की पोती है, जो P का पति है। "
            "M, Q से कैसे संबंधित है?"
        ),
        "option_a": "Father/पिता",
        "option_b": "Daughter/बेटी",
        "option_c": "Mother/माँ",
        "option_d": "Son/बेटा",
        "correct_answer": "A",
    },
    # Q52
    {
        "question_number": 52,
        "difficulty": "medium",
        "question_en": (
            "A is mother of B, C is son of A, D is brother of E, E is daughter of B. "
            "Who is the uncle of E?"
        ),
        "question_hi": (
            "A, B की माँ है, C, A का पुत्र है, D, E का भाई है, E, B की बेटी है। "
            "E का चाचा कौन है?"
        ),
        "option_a": "C",
        "option_b": "B",
        "option_c": "A",
        "option_d": "D",
        "correct_answer": "A",
    },
    # Q53
    {
        "question_number": 53,
        "difficulty": "hard",
        "question_en": (
            "Shyam went to attend the marriage of Ram's son. Ram is the brother of "
            "Shyam's daughter's paternal grandmother's daughter-in-law's husband. "
            "How is the bridegroom related to Shyam where Shyam is a male?"
        ),
        "question_hi": (
            "श्याम, राम के बेटे की शादी में गया। राम, श्याम की बेटी की दादी के "
            "पुत्रवधू के पति का भाई है। वर का श्याम से क्या संबंध है यदि श्याम एक पुरुष है?"
        ),
        "option_a": "Father/पिता",
        "option_b": "Brother/भाई",
        "option_c": "Uncle/चाचा",
        "option_d": "Nephew/भतीजा",
        "correct_answer": "D",
    },
    # Q54
    {
        "question_number": 54,
        "difficulty": "medium",
        "question_en": (
            "If 'A+B' means 'A is father of B', 'A-B' means 'A is mother of B', "
            "'A*B' means 'A is brother of B', and 'A%B' means 'A is sister of B', "
            "then how is Q related to S in 'P+Q*R-S'?"
        ),
        "question_hi": (
            "यदि 'A+B' का अर्थ 'A, B का पिता है', 'A-B' का अर्थ 'A, B की माँ है', "
            "'A*B' का अर्थ 'A, B का भाई है', और 'A%B' का अर्थ 'A, B की बहन है', "
            "तो 'P+Q*R-S' में Q, S से कैसे संबंधित है?"
        ),
        "option_a": "Husband/पति",
        "option_b": "Uncle/मामा",
        "option_c": "Brother/भाई",
        "option_d": "Father/पिता",
        "correct_answer": "B",
    },
    # Q55
    {
        "question_number": 55,
        "difficulty": "easy",
        "question_en": (
            "H is the brother of T who is the wife of R. S is the son of R and "
            "husband of L. How is L related to T?"
        ),
        "question_hi": (
            "H, T का भाई है, जो R की पत्नी है। S, R का पुत्र है और L का पति है। "
            "L, T से कैसे संबंधित है?"
        ),
        "option_a": "Wife/पत्नी",
        "option_b": "Son/बेटा",
        "option_c": "Daughter-in-law/पुत्रवधू",
        "option_d": "Husband/पति",
        "correct_answer": "C",
    },
    # Q56
    {
        "question_number": 56,
        "difficulty": "hard",
        "question_en": (
            "If 'P 3 Q' means 'P is daughter of Q', 'P 5 Q' means 'P is father of Q', "
            "'P 7 Q' means 'P is mother of Q', and 'P 9 Q' means 'P is sister of Q', "
            "then how is J related to K in J 3 L 9 N 3 O 5 K?"
        ),
        "question_hi": (
            "यदि 'P 3 Q' का अर्थ 'P, Q की पुत्री है', 'P 5 Q' का अर्थ 'P, Q का पिता है', "
            "'P 7 Q' का अर्थ 'P, Q की माँ है', और 'P 9 Q' का अर्थ 'P, Q की बहन है', "
            "तो J 3 L 9 N 3 O 5 K में J, K से कैसे संबंधित है?"
        ),
        "option_a": "Mother/माँ",
        "option_b": "Wife/पत्नी",
        "option_c": "Niece/भांजी",
        "option_d": "Daughter/बेटी",
        "correct_answer": "C",
    },
    # Q57
    {
        "question_number": 57,
        "difficulty": "hard",
        "question_en": (
            "If 'A+B' means 'A is brother of B', 'A-B' means 'A is sister of B', "
            "'A*B' means 'A is mother of B', then which of the following options "
            "signifies that P is grandmother of Q?"
        ),
        "question_hi": (
            "यदि 'A+B' का अर्थ 'A, B का भाई है', 'A-B' का अर्थ 'A, B की बहन है', "
            "'A*B' का अर्थ 'A, B की माँ है', तो निम्नलिखित में से कौन सा विकल्प "
            "दर्शाता है कि P, Q की दादी है?"
        ),
        "option_a": "R-P*O-S-Q",
        "option_b": "R-P+O*S+Q",
        "option_c": "R+P*O+S*Q",
        "option_d": "R-P*O*S+Q",
        "correct_answer": "C",
    },
    # Q58
    {
        "question_number": 58,
        "difficulty": "easy",
        "question_en": (
            "A is father of B, but B is not his son. D is wife of A. C is son of D. "
            "How is D related to B?"
        ),
        "question_hi": (
            "A, B का पिता है, लेकिन B उसका बेटा नहीं है। D, A की पत्नी है। C, D का पुत्र है। "
            "D, B से कैसे संबंधित है?"
        ),
        "option_a": "Daughter/बेटी",
        "option_b": "Brother/भाई",
        "option_c": "Mother/माँ",
        "option_d": "Cannot be determined/निर्धारित नहीं किया जा सकता",
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
