"""
seed_reasoning_coding_decoding_sheet7.py
====================================
Seeds questions 55-62 (Coding-Decoding) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Coding-Decoding
Run     : python seed_reasoning_coding_decoding_sheet7.py

Answer key verification:
  Q55: alternating -3/+1; A-3=X(wrap)✓,C+1=D✓,I-3=F✓,D+1=E✓; HAND->EBKE✓;
       ZEST: Z-3=W,E+1=F,S-3=P,T+1=U -> WFPU                                      -> B
  Q56: +1 all letters, middle letter +3; KIOSK✓;FLAME✓;
       ENJOY: E+1=F,N+1=O,J+3=M,O+1=P,Y+1=Z -> FOMPZ                              -> B
  Q57: common word = common code; 'are' = 'mz'                                      -> A
  Q58: CERTAIN{9,6,4,3,8,2,1}; UNCERTAIN has extra digit 7 not in CERTAIN -> U=7  -> A
  Q59: common word = common code; 'this' = 'Ka'                                     -> C
  Q60: common word = common code; 'someone' = 'Te'                                  -> B
  Q61: alternating 0/+1; HUMAN->HVMBN✓;BEING->BFIOG✓;
       NURSE: N,V,R,T,E -> NVRTE                                                    -> A
  Q62: swap positions 1↔3 and 4↔6; ADVICE->VDAECI✓;BELONG->LEBGNO✓;
       BETTER(B,E,T,T,E,R)->T,E,B,R,E,T=TEBRET                                    -> C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Coding_Decoding_Sheet7"
SUBJECT = "Reasoning"
TOPIC   = "Coding-Decoding"

QUESTIONS = [
    # Q55
    {
        "question_number": 55,
        "difficulty": "medium",
        "question_en": (
            "In a code language, 'ACID' is written as 'XDFE' and 'HAND' is written "
            "as 'EBKE'. How will 'ZEST' be written in that language?"
        ),
        "question_hi": (
            "एक कूट भाषा में, 'ACID' को 'XDFE' और 'HAND' को 'EBKE' के रूप में "
            "लिखा जाता है। उस भाषा में 'ZEST' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "PUWF",
        "option_b": "WFPU",
        "option_c": "WPUF",
        "option_d": "UWPF",
        "correct_answer": "B",
    },
    # Q56
    {
        "question_number": 56,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'KIOSK' is coded as 'LJRTL' and 'FLAME' "
            "is coded as 'GMDNF'. What is the code for 'ENJOY' in the given code "
            "language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'KIOSK' को 'LJRTL' और 'FLAME' को 'GMDNF' "
            "के रूप में कूटबद्ध किया जाता है। दी गई कूट भाषा में 'ENJOY' का कूट "
            "क्या है?"
        ),
        "option_a": "EMOQY",
        "option_b": "FOMPZ",
        "option_c": "ENOQZ",
        "option_d": "GNMRY",
        "correct_answer": "B",
    },
    # Q57
    {
        "question_number": 57,
        "difficulty": "easy",
        "question_en": (
            "In a certain code language, 'messages are encrypted' is written as "
            "'tg gc mz' and 'are you coming' is written as 'ze fp mz'. How is "
            "'are' written in the given language?"
        ),
        "question_hi": (
            "किसी निश्चित कूट भाषा में, 'messages are encrypted' को 'tg gc mz' "
            "और 'are you coming' को 'ze fp mz' के रूप में लिखा जाता है। दी गई "
            "भाषा में 'are' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "mz",
        "option_b": "fp",
        "option_c": "ze",
        "option_d": "gc",
        "correct_answer": "A",
    },
    # Q58
    {
        "question_number": 58,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'CERTAIN' is coded as '9643821' and "
            "'UNCERTAIN' is coded as '964382117'. What is the code for 'U' in "
            "that language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, 'CERTAIN' को '9643821' और 'UNCERTAIN' को "
            "'964382117' के रूप में कूटबद्ध किया गया है। उस कूट भाषा में 'U' "
            "के लिए कूट क्या है?"
        ),
        "option_a": "7",
        "option_b": "1",
        "option_c": "6",
        "option_d": "4",
        "correct_answer": "A",
    },
    # Q59
    {
        "question_number": 59,
        "difficulty": "easy",
        "question_en": (
            "In a certain language, 'this is music' is written as 'Ta Bu Ka Bi' "
            "and 'who touched this' is written as 'Pi Ka Bi'. How is 'this' written "
            "in the given language?"
        ),
        "question_hi": (
            "किसी निश्चित कूट भाषा में, 'this is music' को 'Ta Bu Ka' और 'who "
            "touched this' को 'Pi Ka Bi' के रूप में लिखा जाता है। दी गई भाषा में "
            "'this' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "Bi",
        "option_b": "Bu",
        "option_c": "Ka",
        "option_d": "Ta",
        "correct_answer": "C",
    },
    # Q60
    {
        "question_number": 60,
        "difficulty": "easy",
        "question_en": (
            "In a certain language, 'make someone happy' is written as 'Ab Te Dp' "
            "and 'someone robbed him' is written as 'Te Ko Vi'. How is 'someone' "
            "written in the given language?"
        ),
        "question_hi": (
            "किसी निश्चित कूट भाषा में, 'make someone happy' को 'Ab Te Dp' और "
            "'someone robbed him' को 'Te Ko Vi' के रूप में लिखा जाता है। दी गई "
            "कूट भाषा में 'someone' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "Vi",
        "option_b": "Te",
        "option_c": "Ab",
        "option_d": "Ko",
        "correct_answer": "B",
    },
    # Q61
    {
        "question_number": 61,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'HUMAN' is written as 'HVMBN' and 'BEING' "
            "is written as 'BFIOG'. How will 'NURSE' be written in that language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'HUMAN' को 'HVMBN' और 'BEING' को 'BFIOG' "
            "के रूप में लिखा जाता है। उस भाषा में 'NURSE' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "NVRTE",
        "option_b": "NRVTE",
        "option_c": "NURTE",
        "option_d": "NVRET",
        "correct_answer": "A",
    },
    # Q62
    {
        "question_number": 62,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, ADVICE is written as VDAECI and BELONG is "
            "written as LEBGNO. How will BETTER be written in the same language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, ADVICE को VDAECI और BELONG को LEBGNO के "
            "रूप में लिखा जाता है। उसी भाषा में BETTER को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "RETTEB",
        "option_b": "CFUUFS",
        "option_c": "TEBRET",
        "option_d": "YVGGVI",
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
