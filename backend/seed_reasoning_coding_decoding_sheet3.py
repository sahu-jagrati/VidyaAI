"""
seed_reasoning_coding_decoding_sheet3.py
====================================
Seeds questions 19-27 (Coding-Decoding) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Coding-Decoding
Run     : python seed_reasoning_coding_decoding_sheet3.py

Answer key verification:
  Q19: sum_of_positions+4; MATURE(78+4=82)✓; HIGHER(55+4=59)✓; ASIAN(44+4=48) -> D
  Q20: consonant->next_letter(O as 0), vowel->position; MOONLIGHT=N15150M9HIU -> B
  Q21: alternating -2/+1; SUGAR: S->Q,U->V,G->E,A->B,R->P = QVEBP               -> B
  Q22: product_of_positions×3; KCE=11×3×5×3=495                                  -> C
  Q23: map T=9,O=6,W=2,A=1,R=4,D=7,N=3,E=5; WARRANT=2144139                     -> C
  Q24: alternating -3/-4; LOGS: L->I,O->K,G->D,S->O = IKDO                       -> A
  Q25: SET: BROW{7,5,4,2}∩WORM{7,2,9,5}={7,5,2}={W,O,R}; B=4                   -> B
  Q26: alternating -1/-2; TEXT: T->S,E->C,X->W,T->R = SCWR                       -> B
  Q27: position×3; GAUTAM: G=21,A=3,U=63,T=60,A=3,M=39 = 21-3-63-60-3-39       -> C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Coding_Decoding_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Coding-Decoding"

QUESTIONS = [
    # Q19
    {
        "question_number": 19,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'MATURE' is coded as '82' and 'HIGHER' "
            "is coded as '59'. What is the code for 'ASIAN' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'MATURE' को '82' के रूप में और 'HIGHER' को "
            "'59' के रूप में कूटबद्ध किया जाता है। उस कूट भाषा में 'ASIAN' के लिए "
            "कूट क्या है?"
        ),
        "option_a": "44",
        "option_b": "42",
        "option_c": "46",
        "option_d": "48",
        "correct_answer": "D",
    },
    # Q20
    {
        "question_number": 20,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, if RAINBOW is coded as 'S190C15X' and "
            "SUNSHINE is coded as 'T210T1905', then what will MOONLIGHT be coded as?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, यदि RAINBOW को 'S190C15X' के रूप में और "
            "SUNSHINE को 'T210T1905' के रूप में कूटबद्ध किया जाता है, तो MOONLIGHT "
            "को किस प्रकार कूटबद्ध किया जाएगा?"
        ),
        "option_a": "N15150N9HIU",
        "option_b": "N15150M9HIU",
        "option_c": "N151509MHIU",
        "option_d": "N1515M9OHIU",
        "correct_answer": "B",
    },
    # Q21
    {
        "question_number": 21,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, if TEA is coded as RFY and COFFEE is coded "
            "as APDGCF, then what will SUGAR be coded as?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, यदि TEA को RFY और COFFEE को APDGCF के रूप में "
            "कूटबद्ध किया जाता है, तो SUGAR को किस प्रकार कूटबद्ध किया जाएगा?"
        ),
        "option_a": "TVHBS",
        "option_b": "QVEBP",
        "option_c": "QTEZP",
        "option_d": "QSEYP",
        "correct_answer": "B",
    },
    # Q22
    {
        "question_number": 22,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'TDG' is coded as '1680' and 'BHI' is coded "
            "as '432'. What is the code for 'KCE' in that code language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, 'TDG' को '1680' और 'BHI' को '432' के रूप में "
            "कूटबद्ध किया जाता है। उस कूट भाषा में 'KCE' के लिए कूट क्या है?"
        ),
        "option_a": "520",
        "option_b": "425",
        "option_c": "495",
        "option_d": "465",
        "correct_answer": "C",
    },
    # Q23
    {
        "question_number": 23,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'TOWARD' is coded as '962147' and 'WANTED' "
            "is coded as '213957'. What is the code for 'WARRANT' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'TOWARD' को '962147' और 'WANTED' को '213957' "
            "के रूप में कूटबद्ध किया जाता है। उस कूट भाषा में 'WARRANT' के लिए "
            "कूट क्या है?"
        ),
        "option_a": "2133129",
        "option_b": "2145129",
        "option_c": "2144139",
        "option_d": "2144129",
        "correct_answer": "C",
    },
    # Q24
    {
        "question_number": 24,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'LALP' is coded as 'IWIL'. What is the "
            "code for 'LOGS' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'LALP' को 'IWIL' के रूप में कूटबद्ध किया "
            "जाता है। उस कूट भाषा में 'LOGS' के लिए कूट क्या है?"
        ),
        "option_a": "IKDO",
        "option_b": "IKEO",
        "option_c": "IJDO",
        "option_d": "IKDP",
        "correct_answer": "A",
    },
    # Q25
    {
        "question_number": 25,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'BROW' is coded as '7542' and 'WORM' is "
            "coded as '7295'. What is the code for 'B' in the given code language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, 'BROW' को '7542' और 'WORM' को '7295' के रूप "
            "में कूटबद्ध किया जाता है। दी गई कूट भाषा में 'B' के लिए कूट क्या है?"
        ),
        "option_a": "7",
        "option_b": "4",
        "option_c": "9",
        "option_d": "2",
        "correct_answer": "B",
    },
    # Q26
    {
        "question_number": 26,
        "difficulty": "medium",
        "question_en": (
            "In a code language, 'HAND' is written as 'GYMB' and 'FOOD' is written "
            "as 'EMNB'. How will 'TEXT' be written in that language?"
        ),
        "question_hi": (
            "एक कूट भाषा में, 'HAND' को 'GYMB' के रूप में और 'FOOD' को 'EMNB' के "
            "रूप में लिखा जाता है। उस भाषा में 'TEXT' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "RWSC",
        "option_b": "SCWR",
        "option_c": "SCRW",
        "option_d": "SWRC",
        "correct_answer": "B",
    },
    # Q27
    {
        "question_number": 27,
        "difficulty": "medium",
        "question_en": (
            "In a code language, 'DINESH' is coded as 12-27-42-15-57-24 and 'VIRAT' "
            "is coded as 66-27-54-3-60. How will 'GAUTAM' be coded in the same language?"
        ),
        "question_hi": (
            "एक कूट भाषा में, 'DINESH' को 12-27-42-15-57-24 के रूप में और 'VIRAT' "
            "को 66-27-54-3-60 के रूप में कूटबद्ध किया जाता है। उसी भाषा में "
            "'GAUTAM' को कैसे कूटबद्ध किया जाएगा?"
        ),
        "option_a": "24-7-61-34-5-31",
        "option_b": "26-7-25-67-4-37",
        "option_c": "21-3-63-60-3-39",
        "option_d": "29-9-55-47-8-28",
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
