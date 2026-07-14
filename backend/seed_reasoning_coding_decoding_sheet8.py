"""
seed_reasoning_coding_decoding_sheet8.py
====================================
Seeds questions 63-71 (Coding-Decoding) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Coding-Decoding
Run     : python seed_reasoning_coding_decoding_sheet8.py

Answer key verification:
  Q63: sum of letter positions; ZERO(64)✓;FIVE(42)✓; ELEVEN=5+12+5+22+5+14=63    -> B
  Q64: alternating +3/+8 mod26; QUIRKY->TCLZNG✓;MUZHIK->PCCPLS✓;
       FROWZY: F+3=I,R+8=Z,O+3=R,W+8=E,Z+3=C,Y+8=G -> IZRECG                     -> B
  Q65: SET: ARCHED{5,2,6,7,4,9}∩CHASED{4,3,2,5,7,6}={5,2,6,7,4}; R=9              -> A
  Q66: SET: MOST{3,4,7,2}∩STOW{2,6,3,4}={3,4,2}; M=7                               -> D
  Q67: code=25-position; FOX->SJA✓;CRIPPLE->VGPIIMT✓;
       MOVEMENT: M=12=L,O=10=J,V=3=C,E=20=T,M=12=L,E=20=T,N=11=K,T=5=E -> LJCTLTKE -> D
  Q68: sum_of_positions+num_letters; TARNISH(89+7=96)✓;CORRECT(82+7=89)✓;
       GENERAL: 7+5+14+5+18+1+12=62+7=69                                           -> A
  Q69: common word=common code; 'you'='sq'                                          -> D
  Q70: each letter +7; GKLI: G+7=N,K+7=R,L+7=S,I+7=P -> NRSP                     -> B
  Q71: pos1-2: code=29-pos; pos3-5: code=30-pos;
       BRING: B->A(29-2=27->1),R->K(29-18=11),I->U(30-9=21),
       N->P(30-14=16),G->W(30-7=23) -> AKUPW                                       -> D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Coding_Decoding_Sheet8"
SUBJECT = "Reasoning"
TOPIC   = "Coding-Decoding"

QUESTIONS = [
    # Q63
    {
        "question_number": 63,
        "difficulty": "easy",
        "question_en": (
            "In a certain code language, ZERO is coded as 64 and FIVE is coded as "
            "42. How will ELEVEN be coded in that language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, ZERO को 64 और FIVE को 42 के रूप में कूटबद्ध "
            "किया जाता है। उस भाषा में ELEVEN को कैसे कूटबद्ध किया जाएगा?"
        ),
        "option_a": "64",
        "option_b": "63",
        "option_c": "62",
        "option_d": "61",
        "correct_answer": "B",
    },
    # Q64
    {
        "question_number": 64,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'QUIRKY' is coded as 'TCLZNG' and 'MUZHIK' "
            "is coded as 'PCCPLS'. What is the code for 'FROWZY' in the given code "
            "language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'QUIRKY' को 'TCLZNG' और 'MUZHIK' को 'PCCPLS' "
            "के रूप में कूटबद्ध किया जाता है। दी गई कूट भाषा में 'FROWZY' के लिए "
            "कूट क्या है?"
        ),
        "option_a": "IZKECG",
        "option_b": "IZRECG",
        "option_c": "IZREDG",
        "option_d": "IZRECF",
        "correct_answer": "B",
    },
    # Q65
    {
        "question_number": 65,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'ARCHED' is coded as '526749' and 'CHASED' "
            "is coded as '432576'. What is the code for 'R' in the given code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'ARCHED' को '526749' और 'CHASED' को '432576' "
            "के रूप में कूटबद्ध किया जाता है। दी गई कूट भाषा में 'R' के लिए कूट क्या है?"
        ),
        "option_a": "9",
        "option_b": "7",
        "option_c": "3",
        "option_d": "5",
        "correct_answer": "A",
    },
    # Q66
    {
        "question_number": 66,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'MOST' is coded as '3472' and 'STOW' is "
            "coded as '2634'. What is the code for 'M' in the given code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'MOST' को '3472' और 'STOW' को '2634' के रूप "
            "में कूटबद्ध किया जाता है। दी गई कूट भाषा में 'M' के लिए कूट क्या है?"
        ),
        "option_a": "3",
        "option_b": "4",
        "option_c": "2",
        "option_d": "7",
        "correct_answer": "D",
    },
    # Q67
    {
        "question_number": 67,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'FOX' is coded as 'SJA' and 'CRIPPLE' is "
            "coded as 'VGPIIMT'. How will 'MOVEMENT' be coded in that language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'FOX' को 'SJA' और 'CRIPPLE' को 'VGPIIMT' "
            "के रूप में कूटबद्ध किया जाता है। उस भाषा में 'MOVEMENT' को किस प्रकार "
            "कूटबद्ध किया जाएगा?"
        ),
        "option_a": "LJCSLTKE",
        "option_b": "LJCTLTKF",
        "option_c": "LJCTLTJE",
        "option_d": "LJCTLTKE",
        "correct_answer": "D",
    },
    # Q68
    {
        "question_number": 68,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'TARNISH' is coded as '96' and 'CORRECT' "
            "is coded as '89'. How is 'GENERAL' coded in the given language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'TARNISH' को '96' और 'CORRECT' को '89' के "
            "रूप में कूटबद्ध किया जाता है। दी गई भाषा में 'GENERAL' को कैसे "
            "कूटबद्ध किया जाएगा?"
        ),
        "option_a": "69",
        "option_b": "96",
        "option_c": "71",
        "option_d": "67",
        "correct_answer": "A",
    },
    # Q69
    {
        "question_number": 69,
        "difficulty": "easy",
        "question_en": (
            "In a certain code language, 'can you speak' is written as 'pr lt sq' "
            "and 'you work hard' is written as 'sq wp mq'. How is 'you' written "
            "in the given language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, 'can you speak' को 'pr lt sq' और 'you work "
            "hard' को 'sq wp mq' के रूप में लिखा जाता है। उस भाषा में 'you' को "
            "किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "pr",
        "option_b": "wp",
        "option_c": "mq",
        "option_d": "sq",
        "correct_answer": "D",
    },
    # Q70
    {
        "question_number": 70,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, BFGD is written as IMNK and PTUR is "
            "written as WABY. How will GKLI be written in that language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, BFGD को IMNK और PTUR को WABY के रूप में "
            "लिखा जाता है। उसी भाषा में GKLI को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "NRSO",
        "option_b": "NRSP",
        "option_c": "MRSO",
        "option_d": "MRSP",
        "correct_answer": "B",
    },
    # Q71
    {
        "question_number": 71,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'TOWER' is written as 'INGYL' and 'SIGHT' "
            "is written as 'JTWVJ'. How will 'BRING' be written in that language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'TOWER' को 'INGYL' और 'SIGHT' को 'JTWVJ' "
            "के रूप में लिखा जाता है। उस भाषा में 'BRING' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "LWYDB",
        "option_b": "ACTBE",
        "option_c": "KRPJS",
        "option_d": "AKUPW",
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
