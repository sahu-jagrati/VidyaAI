"""
seed_reasoning_coding_decoding_sheet6.py
====================================
Seeds questions 46-54 (Coding-Decoding) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Coding-Decoding
Run     : python seed_reasoning_coding_decoding_sheet6.py

Answer key verification:
  Q46: reverse-alpha positions concatenated; C=24,I=18,T=7,Y=2->241872✓;
       GOLF: G=20,O=12,L=15,F=21 -> 20121521                                       -> B
  Q47: common word=common code; 'dinner'='rn'                                       -> B
  Q48: SET: BEAM{2,3,4,9}∩MEAN{4,3,2,7}={2,3,4}={M,E,A}; B=9,N=7                 -> B
  Q49: common word=common code; 'strong'='tk'                                       -> D
  Q50: position*3; MOHAN: M(13)=39,O(15)=45,H(8)=24,A(1)=3,N(14)=42              -> C
  Q51: alternating -1/+1; PIECE: P-1=O,I+1=J,E-1=D,C+1=D,E-1=D -> OJDDD          -> A
  Q52: num_letters^2; HEN(3^2=9)✓;AFTER(5^2=25)✓; SMALLEST(8^2=64)               -> B
  Q53: alternating -1/+1; WELL: W-1=V,E+1=F,L-1=K,L+1=M -> VFKM                  -> A
  Q54: reverse-alpha position*3; ZEBRA: Z(1*3=3),E(22*3=66),B(25*3=75),
       R(9*3=27),A(26*3=78) -> 3-66-75-27-78                                       -> A
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Coding_Decoding_Sheet6"
SUBJECT = "Reasoning"
TOPIC   = "Coding-Decoding"

QUESTIONS = [
    # Q46
    {
        "question_number": 46,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'CITY' is written as '241872' and 'DRUG' "
            "is written as '239620'. How will 'GOLF' be written in that language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, 'CITY' को '241872' और 'DRUG' को '239620' के "
            "रूप में लिखा जाता है। उसी कूट भाषा में 'GOLF' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "7121521",
        "option_b": "20121521",
        "option_c": "7151212",
        "option_d": "18151215",
        "correct_answer": "B",
    },
    # Q47
    {
        "question_number": 47,
        "difficulty": "easy",
        "question_en": (
            "In a certain code language, 'stay for dinner' is written as 'px rn tf' "
            "and 'dinner is ready' is written as 'sq mv rn'. How is 'dinner' written "
            "in the given code language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, 'stay for dinner' को 'px rn tf' और 'dinner is "
            "ready' को 'sq mv rn' के रूप में लिखा जाता है। दी गई कूट भाषा में "
            "'dinner' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "px",
        "option_b": "rn",
        "option_c": "tf",
        "option_d": "sq",
        "correct_answer": "B",
    },
    # Q48
    {
        "question_number": 48,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, BEAM is coded as 2349 and MEAN is coded as "
            "4327. What is the code for N in that language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, BEAM को 2349 और MEAN को 4327 के रूप में "
            "कूटबद्ध किया गया है। उस भाषा में N के लिए कूट क्या है?"
        ),
        "option_a": "3",
        "option_b": "7",
        "option_c": "4",
        "option_d": "2",
        "correct_answer": "B",
    },
    # Q49
    {
        "question_number": 49,
        "difficulty": "easy",
        "question_en": (
            "In a certain code language, 'strong and mighty' is written as 'ui yy tk' "
            "and 'soft yet strong' is written as 'hd tk bw'. How is 'strong' written "
            "in the given code language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, 'strong and mighty' को 'ui yy tk' और 'soft yet "
            "strong' को 'hd tk bw' के रूप में लिखा जाता है। दी गई भाषा में 'strong' "
            "को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "hd",
        "option_b": "bw",
        "option_c": "ui",
        "option_d": "tk",
        "correct_answer": "D",
    },
    # Q50
    {
        "question_number": 50,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'HEMANT' is coded as 24-15-39-3-42-60 and "
            "'VINAY' is coded as 66-27-42-3-75. How will 'MOHAN' be coded in the "
            "same language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'HEMANT' को 24-15-39-3-42-60 के रूप में और "
            "'VINAY' को 66-27-42-3-75 के रूप में कूटबद्ध किया जाता है। उसी भाषा में "
            "'MOHAN' को किस प्रकार कूटबद्ध किया जाएगा?"
        ),
        "option_a": "36-3-41-24-39",
        "option_b": "43-24-3-56-7",
        "option_c": "39-45-24-3-42",
        "option_d": "4-39-4-42-27",
        "correct_answer": "C",
    },
    # Q51
    {
        "question_number": 51,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'MARCH' is written as 'LBQDG' and 'TAXAS' "
            "is written as 'SBWBR'. How will 'PIECE' be written in the given language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'MARCH' को 'LBQDG' और 'TAXAS' को 'SBWBR' के "
            "रूप में लिखा जाता है। दी गई भाषा में 'PIECE' को कैसे लिखा जाएगा?"
        ),
        "option_a": "OJDDD",
        "option_b": "QHCED",
        "option_c": "OJDDF",
        "option_d": "OJDED",
        "correct_answer": "A",
    },
    # Q52
    {
        "question_number": 52,
        "difficulty": "easy",
        "question_en": (
            "In a certain code language, 'HEN' is coded as '9' and 'AFTER' is coded "
            "as '25'. How will 'SMALLEST' be coded in that language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, 'HEN' को '9' और 'AFTER' को '25' के रूप में "
            "कूटबद्ध किया जाता है। उस भाषा में 'SMALLEST' को किस प्रकार कूटबद्ध "
            "किया जाएगा?"
        ),
        "option_a": "31",
        "option_b": "64",
        "option_c": "81",
        "option_d": "56",
        "correct_answer": "B",
    },
    # Q53
    {
        "question_number": 53,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'BEAM' is written as 'AFZN' and 'BILL' is "
            "written as 'AJKM'. How will 'WELL' be written in that language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, 'BEAM' को 'AFZN' और 'BILL' को 'AJKM' के रूप "
            "में लिखा जाता है। उस भाषा में 'WELL' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "VFKM",
        "option_b": "MVKF",
        "option_c": "KMVF",
        "option_d": "VKMF",
        "correct_answer": "A",
    },
    # Q54
    {
        "question_number": 54,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'PANDA' is coded as 33-78-39-69-78 and "
            "'SNAKE' is coded as 24-39-78-48-66. How will 'ZEBRA' be coded in the "
            "same language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'PANDA' को 33-78-39-69-78 के रूप में और "
            "'SNAKE' को 24-39-78-48-66 के रूप में कूटबद्ध किया जाता है। उसी भाषा "
            "में 'ZEBRA' को किस प्रकार कूटबद्ध किया जाएगा?"
        ),
        "option_a": "3-66-75-27-78",
        "option_b": "6-46-63-38-78",
        "option_c": "7-46-65-13-78",
        "option_d": "5-66-71-29-78",
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
