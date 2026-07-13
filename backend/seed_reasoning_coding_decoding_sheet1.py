"""
seed_reasoning_coding_decoding_sheet1.py
====================================
Seeds questions 1-9 (Coding Decoding) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Coding Decoding
Run     : python seed_reasoning_coding_decoding_sheet1.py

Answer key verification:
  Q1:  SET approach: M=7(GAMES&FORUM), E=2(FORCE&GAMES), {F,O,R}={0,5,8}, C=3   -> B
  Q2:  FOX(3)->14=3^2+5; GOAT(4)->21=4^2+5; TOMMY(5)->5^2+5=30                  -> C
  Q3:  'I am'={it,sit}; boy=pit; girl=nit                                          -> B
  Q4:  {E,N,T}={*,7,9}; K=^; B=-(unique in BENT)                                  -> C
  Q5:  O=4(unique in IDOL); E=2(unique in IDLE); 2=E                               -> D
  Q6:  {R,S,T}={4,6,9}; U=2; O=8(unique in SORT)                                  -> B
  Q7:  QUITE sum=72; 72x3=216; PROVE sum=76; 76x3=228; EXIST sum=77; 77x3=231     -> C
  Q8:  A->X(-3),H->D(-4),E->B(-3),M->I(-4); alternating -3,-4;
       BETS: B->Y,E->A,T->Q,S->O=YAQO                                              -> D
  Q9:  distinct letters+4; SIXTEEN=6+4=10; NINE=3+4=7; EIGHT=5+4=9                -> B
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Coding_Decoding_Sheet1"
SUBJECT = "Reasoning"
TOPIC   = "Coding-Decoding"

QUESTIONS = [
    # Q1
    {
        "question_number": 1,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'FORCE' is coded as '83052', 'GAMES' is "
            "coded as 42761, 'FORUM' is coded as 08957. What is the code for 'C' "
            "in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'FORCE' को '83052' के रूप में कूटबद्ध किया "
            "जाता है, 'GAMES' को '42761' के रूप में कूटबद्ध किया जाता है, 'FORUM' "
            "को '08957' के रूप में कूटबद्ध किया जाता है। उस कूट भाषा में 'C' के "
            "लिए कूट क्या है?"
        ),
        "option_a": "8",
        "option_b": "3",
        "option_c": "4",
        "option_d": "5",
        "correct_answer": "B",
    },
    # Q2
    {
        "question_number": 2,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'FOX' is coded as '14' and 'GOAT' is "
            "coded as '21'. How will 'TOMMY' be coded in that language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, 'FOX' को '14' और 'GOAT' को '21' के रूप में "
            "कूटबद्ध किया जाता है। उसी कूट भाषा में 'TOMMY' को किस प्रकार कूटबद्ध "
            "किया जाएगा?"
        ),
        "option_a": "45",
        "option_b": "35",
        "option_c": "30",
        "option_d": "25",
        "correct_answer": "C",
    },
    # Q3
    {
        "question_number": 3,
        "difficulty": "easy",
        "question_en": (
            "In a certain code language, 'I am boy' is coded as 'it sit pit' and "
            "'I am girl' is coded as 'sit nit it'. What is the code for 'girl' in "
            "that language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, 'I am boy' को 'it sit pit' और 'I am girl' "
            "को 'sit nit it' के रूप में कूटबद्ध किया जाता है। उसी कूट भाषा में "
            "'girl' के लिए कूट क्या है?"
        ),
        "option_a": "it",
        "option_b": "nit",
        "option_c": "pit",
        "option_d": "sit",
        "correct_answer": "B",
    },
    # Q4
    {
        "question_number": 4,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'KENT' is coded as '9*^7' and 'BENT' is "
            "coded as '*-79'. What is the code for 'B' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'KENT' को '9*^7' के रूप में कूटबद्ध किया "
            "जाता है और 'BENT' को '*-79' के रूप में कूटबद्ध किया जाता है। उस कूट "
            "भाषा में 'B' के लिए कूट क्या है?"
        ),
        "option_a": "*",
        "option_b": "9",
        "option_c": "-",
        "option_d": "^",
        "correct_answer": "C",
    },
    # Q5
    {
        "question_number": 5,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, '4378' is coded as 'IDOL' and '7832' is "
            "coded as 'IDLE'. What is the code for '2' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, '4378' को 'IDOL' के रूप में कूटबद्ध किया "
            "जाता है और '7832' को 'IDLE' के रूप में कूटबद्ध किया जाता है। उस कूट "
            "भाषा में '2' के लिए कूट क्या है?"
        ),
        "option_a": "O",
        "option_b": "L",
        "option_c": "I",
        "option_d": "E",
        "correct_answer": "D",
    },
    # Q6
    {
        "question_number": 6,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'SORT' is coded as '4698' and 'RUST' is "
            "coded as '6429'. How is 'O' coded in the given language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, 'SORT' को '4698' के रूप में कूटबद्ध किया "
            "जाता है और 'RUST' को '6429' के रूप में कूटबद्ध किया जाता है। दी गई "
            "भाषा में 'O' को किस प्रकार कूटबद्ध किया जाएगा?"
        ),
        "option_a": "9",
        "option_b": "8",
        "option_c": "6",
        "option_d": "4",
        "correct_answer": "B",
    },
    # Q7
    {
        "question_number": 7,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'QUITE' is coded as '216', and 'PROVE' "
            "is coded as '228'. What is the code for 'EXIST' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'QUITE' को '216' के रूप में कूटबद्ध किया "
            "जाता है, और 'PROVE' को '228' के रूप में कूटबद्ध किया जाता है। उस कूट "
            "भाषा में 'EXIST' के लिए कूट क्या है?"
        ),
        "option_a": "258",
        "option_b": "252",
        "option_c": "231",
        "option_d": "256",
        "correct_answer": "C",
    },
    # Q8
    {
        "question_number": 8,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'AHEM' is coded as 'XDBI'. What is the "
            "code for 'BETS' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'AHEM' को 'XDBI' के रूप में कूटबद्ध किया "
            "जाता है। उस कूट भाषा में 'BETS' के लिए कूट क्या है?"
        ),
        "option_a": "YAPO",
        "option_b": "YBQP",
        "option_c": "YBQO",
        "option_d": "YAQO",
        "correct_answer": "D",
    },
    # Q9
    {
        "question_number": 9,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, if SIXTEEN is coded as '10', NINE is "
            "coded as '7', then what will 'EIGHT' be coded as?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, यदि SIXTEEN को '10' के रूप में कूटबद्ध किया "
            "जाता है, NINE को '7' के रूप में कूटबद्ध किया जाता है, तो 'Eight' को "
            "किस प्रकार कूटबद्ध किया जाएगा?"
        ),
        "option_a": "7",
        "option_b": "9",
        "option_c": "8",
        "option_d": "6",
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
