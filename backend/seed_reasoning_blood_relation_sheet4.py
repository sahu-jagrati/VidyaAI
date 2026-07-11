"""
seed_reasoning_blood_relation_sheet4.py
========================================
Seeds questions 28-42 (Blood Relation) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Blood Relation
Run     : python seed_reasoning_blood_relation_sheet4.py

Answer key verification:
  Q28: A&B brothers; F=B's wife; E=F's daughter -> E is B's daughter -> A's niece     -> C
  Q29: M+F married; A&B sisters; A=F's sister -> B is F's sister -> M's sister-in-law -> B
  Q30: A&B siblings; C=A's father; D=C's sister; E=D's mother -> E is C's mother
       -> E is B's paternal grandmother -> B is E's granddaughter                      -> A
  Q31: Q=P's son; X=Q's daughter; R=X's Bua (Q's sister->P's daughter); L=R's son
       -> L is P's grandson                                                             -> A
  Q32: "father of my father's granddaughter" = X's grandfather's granddaughter
       (X's sister); Y married X's sister -> Y is X's brother-in-law                  -> A
  Q33: A=D's mother; G=A's husband -> G is D's father                                  -> D
  Q34: A&B brothers; C&D sisters; A's son is D's brother -> A is D's/C's father
       -> B is C's uncle                                                                -> C
  Q35: Z=K's son-in-law; E=K's only daughter; Z married E; G=E's brother
       -> G is K's son                                                                  -> D
  Q36: T(teacher)+S(doctor); P's son T; R&U=grandchildren; granddaughter is student   -> C
  Q37: C=B's father(male); A=female; E=C's brother(male); D=female; F=B's brother(male)
       -> Males: C,B,E,F = 4                                                           -> C
  Q38: A's mother = B's sister -> A is B's sibling's child -> A is B's niece          -> A
  Q39: A&B married; X&Y brothers; X=A's brother -> Y is A's sibling -> B's brother-in-law -> A
  Q40: P&Q brothers; Q has daughter M and son N -> P is N's uncle                     -> C
  Q41: Family: P(teacher)+S(salesman); Q(doctor)+R(lawyer); T=engineer; U=manager
       -> Married couples: P&S and Q&R                                                 -> B
  Q42: P is the Lady Teacher (married to Salesman S)                                   -> D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Blood_Relation_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Blood Relation"

_DIR41 = (
    "Read the information carefully and answer Q41-42: "
    "There is a family of six persons P, Q, R, S, T and U. "
    "They are Lawyer, Doctor, Teacher, Salesman, Engineer and Manager. "
    "There are two married couples in the family. "
    "S, the Salesman is married to the Lady Teacher. "
    "The Doctor is married to the Lawyer. "
    "U, the Manager, is the son of Q and brother of T. "
    "R, the Lawyer, is the daughter-in-law of P. "
    "T is the unmarried Engineer. P is the grandmother of U."
)
_DIR41_HI = (
    "प्रश्न 41-42 के लिए जानकारी: "
    "परिवार में 6 सदस्य P,Q,R,S,T,U हैं। वे वकील, डॉक्टर, शिक्षक, सेल्समैन, इंजीनियर और मैनेजर हैं। "
    "परिवार में दो विवाहित जोड़े हैं। "
    "S, सेल्समैन की शादी महिला टीचर से हुई है। डॉक्टर की शादी वकील से हुई है। "
    "U, मैनेजर, Q का पुत्र है और T का भाई है। "
    "R, वकील, P की पुत्रवधू है। T एक अविवाहित इंजीनियर है। P, U की दादी है।"
)

QUESTIONS = [
    # Q28
    {
        "question_number": 28,
        "difficulty": "easy",
        "question_en": "A and B are brothers. E is the daughter of F. F is the wife of B. What is the relation of E to A?",
        "question_hi": "A और B भाई हैं। E, F की बेटी है। F, B की पत्नी है। E का A से क्या संबंध है?",
        "option_a": "Sister/बहन",
        "option_b": "Daughter/बेटी",
        "option_c": "Niece/भतीजी",
        "option_d": "Sister-in-law/नंद/भाभी",
        "correct_answer": "C",
    },
    # Q29
    {
        "question_number": 29,
        "difficulty": "easy",
        "question_en": "M and F are a married couple. A and B are sisters. A is the sister of F. Who is B to M?",
        "question_hi": "M और F एक विवाहित जोड़े हैं। A और B बहनें हैं। A, F की बहन है। B का M से क्या संबंध है?",
        "option_a": "Sister/बहन",
        "option_b": "Sister-in-law/ननद/साली",
        "option_c": "Niece/भतीजी",
        "option_d": "Daughter/बेटी",
        "correct_answer": "B",
    },
    # Q30
    {
        "question_number": 30,
        "difficulty": "medium",
        "question_en": (
            "A and B are brother and sister respectively. C is A's father. "
            "D is C's sister and E is D's mother. How is B related to E?"
        ),
        "question_hi": (
            "A और B क्रमशः भाई और बहन हैं। C, A का पिता है। "
            "D, C की बहन है और E, D की माँ है। B, E से कैसे संबंधित है?"
        ),
        "option_a": "Grand-daughter/पोती",
        "option_b": "Great-grand-daughter/परपोती",
        "option_c": "Aunt/चाची",
        "option_d": "Daughter/बेटी",
        "correct_answer": "A",
    },
    # Q31
    {
        "question_number": 31,
        "difficulty": "medium",
        "question_en": (
            "Q is the son of P. X is the daughter of Q. R is the aunty (Bua) of X "
            "and L is the son of R. Then what is L to P?"
        ),
        "question_hi": (
            "Q, P का पुत्र है। X, Q की पुत्री है। R, X की बुआ है और L, R का पुत्र है। "
            "L का P से क्या संबंध है?"
        ),
        "option_a": "Grandson/नाती",
        "option_b": "Granddaughter/पोती",
        "option_c": "Daughter/बेटी",
        "option_d": "Nephew/भतीजा",
        "correct_answer": "A",
    },
    # Q32
    {
        "question_number": 32,
        "difficulty": "medium",
        "question_en": (
            "X introduces Y saying 'He is the husband of the grand-daughter of the father "
            "of my father.' How is Y related to X?"
        ),
        "question_hi": (
            "X, Y का परिचय देते हुए कहता है, 'वह मेरे पिता के पिता की पोती का पति है।' "
            "Y, X से किस प्रकार संबंधित है?"
        ),
        "option_a": "Brother-in-law/जीजा",
        "option_b": "Brother/भाई",
        "option_c": "Father/पिता",
        "option_d": "Grandfather/दादा",
        "correct_answer": "A",
    },
    # Q33
    {
        "question_number": 33,
        "difficulty": "medium",
        "question_en": (
            "A is the mother of D and sister of B. B has a daughter C who is married to F. "
            "G is the husband of A. How is G related to D?"
        ),
        "question_hi": (
            "A, D की माँ है और B की बहन है। B की एक बेटी C है, जो F से विवाहित है। "
            "G, A का पति है। G, D से कैसे संबंधित है?"
        ),
        "option_a": "Uncle/चाचा",
        "option_b": "Husband/पति",
        "option_c": "Son/बेटा",
        "option_d": "Father/पिता",
        "correct_answer": "D",
    },
    # Q34
    {
        "question_number": 34,
        "difficulty": "medium",
        "question_en": (
            "A and B are Brothers. C and D are sisters. A's son is D's brother. "
            "How is B related to C?"
        ),
        "question_hi": (
            "A और B भाई हैं। C और D बहनें हैं। A का पुत्र D का भाई है। "
            "B, C से कैसे संबंधित है?"
        ),
        "option_a": "Father/पिता",
        "option_b": "Brother/भाई",
        "option_c": "Uncle/चाचा",
        "option_d": "Son/बेटा",
        "correct_answer": "C",
    },
    # Q35
    {
        "question_number": 35,
        "difficulty": "medium",
        "question_en": (
            "Z is son-in-law of K and the brother-in-law of G who is the brother of E. "
            "E is the only daughter of K. How is G related to K?"
        ),
        "question_hi": (
            "Z, K का दामाद है और G का जीजा है जो E का भाई है। "
            "E, K की इकलौती पुत्री है। G, K से कैसे संबंधित है?"
        ),
        "option_a": "Brother/भाई",
        "option_b": "Grandfather/दादा",
        "option_c": "Father/पिता",
        "option_d": "Son/बेटा",
        "correct_answer": "D",
    },
    # Q36
    {
        "question_number": 36,
        "difficulty": "hard",
        "question_en": (
            "P,Q,R,S,T,U are 6 members of a family in which there are two married couples. "
            "T, a teacher is married to a doctor who is mother of R and U. "
            "Q, the lawyer is married to P. P has one son and one grandson. "
            "Of the two married ladies one is a housewife. "
            "There is also one student and one male engineer in the family. "
            "Which of the following is true about the grand-daughter of the family?"
        ),
        "question_hi": (
            "P,Q,R,S,T,U एक परिवार के 6 सदस्य हैं जिसमें दो विवाहित जोड़े हैं। "
            "T, शिक्षक की शादी डॉक्टर से होती है जो R और U की माँ है। "
            "Q, वकील की शादी P से होती है। P के एक बेटा और एक पोता है। "
            "दो विवाहित महिलाओं में से एक गृहिणी है। "
            "परिवार में एक छात्र और एक पुरुष इंजीनियर भी है। "
            "परिवार की पोती के बारे में निम्नलिखित में से कौन सा सच है?"
        ),
        "option_a": "She is a lawyer/वह एक वकील है",
        "option_b": "She is an engineer/वह एक इंजीनियर है",
        "option_c": "She is a student/वह एक छात्र है",
        "option_d": "She is a doctor/वह एक डॉक्टर है",
        "correct_answer": "C",
    },
    # Q37
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": (
            "Six members of a family namely A,B,C,D,E and F are travelling together. "
            "B is the son of C but C is not the mother of B. A and C are married couple. "
            "E is the brother of C. D is the daughter of A. F is the brother of B. "
            "How many male members are there in the family?"
        ),
        "question_hi": (
            "A,B,C,D,E और F एक परिवार के 6 सदस्य हैं। "
            "B, C का पुत्र है लेकिन C, B की माँ नहीं है। A और C विवाहित जोड़े हैं। "
            "E, C का भाई है। D, A की बेटी है। F, B का भाई है। "
            "परिवार में कितने पुरुष सदस्य हैं?"
        ),
        "option_a": "3",
        "option_b": "2",
        "option_c": "4",
        "option_d": "1",
        "correct_answer": "C",
    },
    # Q38
    {
        "question_number": 38,
        "difficulty": "medium",
        "question_en": (
            "A's mother is sister of B and has a daughter C. "
            "How can A be related to B from among the following?"
        ),
        "question_hi": (
            "A की माँ B की बहन है और उसकी एक बेटी C है। "
            "A निम्नलिखित में से B से किस प्रकार संबंधित हो सकता है?"
        ),
        "option_a": "Niece/भांजी",
        "option_b": "Uncle/चाचा",
        "option_c": "Daughter/बेटी",
        "option_d": "Father/पिता",
        "correct_answer": "A",
    },
    # Q39
    {
        "question_number": 39,
        "difficulty": "easy",
        "question_en": (
            "A and B are married couple. X and Y are brothers. X is the brother of A. "
            "How is Y related to B?"
        ),
        "question_hi": (
            "A और B विवाहित जोड़े हैं। X और Y भाई हैं। X, A का भाई है। "
            "Y, B से कैसे संबंधित है?"
        ),
        "option_a": "Brother-in-law/साला/देवर",
        "option_b": "Brother/भाई",
        "option_c": "Son-in-law/दामाद",
        "option_d": "Cousin/चचेरे भाई/बहन",
        "correct_answer": "A",
    },
    # Q40
    {
        "question_number": 40,
        "difficulty": "easy",
        "question_en": (
            "A man 'P' goes to a party hosted by his brother 'Q' who has a daughter M. "
            "M is dancing with her brother 'N'. How is 'P' related to 'N'?"
        ),
        "question_hi": (
            "एक आदमी 'P' अपने भाई 'Q' द्वारा होस्ट की गई पार्टी में जाता है, "
            "जिसकी एक बेटी M है। M अपने भाई 'N' के साथ नृत्य कर रही है। "
            "'P', 'N' से कैसे संबंधित है?"
        ),
        "option_a": "Nephew/भतीजा",
        "option_b": "Father/पिता",
        "option_c": "Uncle/चाचा",
        "option_d": "Cousin/चचेरे भाई/बहन",
        "correct_answer": "C",
    },
    # Q41
    {
        "question_number": 41,
        "difficulty": "hard",
        "question_en": _DIR41 + " | Which of the following is one of the married couples?",
        "question_hi": _DIR41_HI + " | निम्नलिखित में से कौन सा एक विवाहित जोड़ा है?",
        "option_a": "T and R/T और R",
        "option_b": "P and S/P और S",
        "option_c": "S and Q/S और Q",
        "option_d": "T and P/T और P",
        "correct_answer": "B",
    },
    # Q42
    {
        "question_number": 42,
        "difficulty": "hard",
        "question_en": _DIR41 + " | What is the profession of P?",
        "question_hi": _DIR41_HI + " | P का पेशा क्या है?",
        "option_a": "Lawyer/वकील",
        "option_b": "Engineer/इंजीनियर",
        "option_c": "Doctor/डॉक्टर",
        "option_d": "Teacher/टीचर",
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
