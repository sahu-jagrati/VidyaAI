"""
seed_reasoning_coding_decoding_sheet9.py
====================================
Seeds questions 72-80 (Coding-Decoding) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Coding-Decoding
Run     : python seed_reasoning_coding_decoding_sheet9.py

Answer key verification:
  Q72: alternating +2/-3; PLAY->RICV✓; TREE->VOGB✓;
       BOOK: B+2=D,O-3=L,O+2=Q,K-3=H -> DLQH                                      -> C
  Q73: pos1+4,pos2↔pos5 swap,pos3+3,pos4-3,pos6-4; PUBLIC->TIEIUY✓;SERVER->WEUSEN✓;
       DIRECT: D+4=H,I↔C swap,R+3=U,E-3=B,T-4=P -> HCUBIP                         -> A
  Q74: FRISK->THLIQ✓; MOADS->QODQB✓; WAGER -> CYJPC                               -> C
  Q75: code=(letter_position+3) concatenated; CBVQ->652520✓;FRJT->9211323✓;
       EHLP: E(8),H(11),L(15),P(19) -> 8111519                                     -> D
  Q76: all letters +1; PENDANT->QFOEBOU✓; LAWFUL->MBXGVM✓;
       IMPOSE: I->J,M->N,P->Q,O->P,S->T,E->F -> JNQPTF                             -> A
  Q77: MANAGE->HJDQDP✓; LITTLE->HOWWLO✓;
       POLICY -> BFLORS                                                              -> D
  Q78: consonants*2, vowels*1 concatenated; CHECK->6165622✓;SURGE->382136145✓;
       PRIEST: P(32)R(36)I(9)E(5)S(38)T(40) -> 3236953840                          -> A
  Q79: sum of reverse-alphabet positions (A=26,Z=1); PDU->40✓;HXO->34✓;
       BMW: B(25)+M(14)+W(4)=43                                                     -> C
  Q80: SET: ZEAL{9,4,7,6}∩LAME{8,6,9,4}={9,4,6}={L,A,E}; M=8                     -> B
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Coding_Decoding_Sheet9"
SUBJECT = "Reasoning"
TOPIC   = "Coding-Decoding"

QUESTIONS = [
    # Q72
    {
        "question_number": 72,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'PLAY' is coded as 'RICV' and 'TREE' is "
            "coded as 'VOGB'. What is the code for 'BOOK' in the given code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'PLAY' को 'RICV' और 'TREE' को 'VOGB' के रूप "
            "में कूटबद्ध किया जाता है। दी गई कूट भाषा में 'BOOK' के लिए कूट क्या है?"
        ),
        "option_a": "DLPH",
        "option_b": "DMQH",
        "option_c": "DLQH",
        "option_d": "ELQH",
        "correct_answer": "C",
    },
    # Q73
    {
        "question_number": 73,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'PUBLIC' is coded as 'TIEIUY' and 'SERVER' "
            "is coded as 'WEUSEN'. What is the code for 'DIRECT' in the given code "
            "language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'PUBLIC' को 'TIEIUY' और 'SERVER' को 'WEUSEN' "
            "के रूप में कूटबद्ध किया जाता है। दी गई कूट भाषा में 'DIRECT' के लिए "
            "कूट क्या है?"
        ),
        "option_a": "HCUBIP",
        "option_b": "HDUBJP",
        "option_c": "GCUBIP",
        "option_d": "HCVBIP",
        "correct_answer": "A",
    },
    # Q74
    {
        "question_number": 74,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'FRISK' is coded as 'THLIQ' and 'MOADS' is "
            "coded as 'QODQB'. What is the code for 'WAGER' in the given code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'FRISK' को 'THLIQ' और 'MOADS' को 'QODQB' के "
            "रूप में कूटबद्ध किया जाता है। दी गई कूट भाषा में 'WAGER' के लिए कूट "
            "क्या है?"
        ),
        "option_a": "AYJPC",
        "option_b": "BZJPC",
        "option_c": "CYJPC",
        "option_d": "CUJPG",
        "correct_answer": "C",
    },
    # Q75
    {
        "question_number": 75,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'CBVQ' is coded as '652520' and 'FRJT' is "
            "coded as '9211323'. What is the code for 'EHLP' in the given code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'CBVQ' को '652520' और 'FRJT' को '9211323' के "
            "रूप में कूटबद्ध किया जाता है। दी गई कूट भाषा में 'EHLP' के लिए कूट "
            "क्या है?"
        ),
        "option_a": "7101418",
        "option_b": "9131721",
        "option_c": "6101418",
        "option_d": "8111519",
        "correct_answer": "D",
    },
    # Q76
    {
        "question_number": 76,
        "difficulty": "easy",
        "question_en": (
            "In a certain code language, 'PENDANT' is coded as 'QFOEBOU' and 'LAWFUL' "
            "is coded as 'MBXGVM'. What is the code for 'IMPOSE' in the given code "
            "language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'PENDANT' को 'QFOEBOU' और 'LAWFUL' को 'MBXGVM' "
            "के रूप में कूटबद्ध किया जाता है। दी गई कूट भाषा में 'IMPOSE' के लिए "
            "कूट क्या है?"
        ),
        "option_a": "JNQPTF",
        "option_b": "JMQPTF",
        "option_c": "JNRPTF",
        "option_d": "KNQPTF",
        "correct_answer": "A",
    },
    # Q77
    {
        "question_number": 77,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'MANAGE' is coded as 'HJDQDP' and 'LITTLE' "
            "is coded as 'HOWWLO'. What is the code for 'POLICY' in the given code "
            "language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'MANAGE' को 'HJDQDP' और 'LITTLE' को 'HOWWLO' "
            "के रूप में कूटबद्ध किया जाता है। दी गई कूट भाषा में 'POLICY' के लिए "
            "कूट क्या है?"
        ),
        "option_a": "ELORBS",
        "option_b": "SROLFB",
        "option_c": "BFLOSR",
        "option_d": "BFLORS",
        "correct_answer": "D",
    },
    # Q78
    {
        "question_number": 78,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'CHECK' is coded as '6165622' and 'SURGE' "
            "is coded as '382136145'. What is the code for 'PRIEST' in the given code "
            "language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'CHECK' को '6165622' और 'SURGE' को '382136145' "
            "के रूप में कूटबद्ध किया जाता है। दी गई कूट भाषा में 'PRIEST' के लिए "
            "कूट क्या है?"
        ),
        "option_a": "3236953840",
        "option_b": "3234953840",
        "option_c": "3236953841",
        "option_d": "3237953840",
        "correct_answer": "A",
    },
    # Q79
    {
        "question_number": 79,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'PDU' is coded as '40' and 'HXO' is coded "
            "as '34'. What is the code for 'BMW' in the given code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'PDU' को '40' और 'HXO' को '34' के रूप में "
            "कूटबद्ध किया जाता है। दी गई कूट भाषा में 'BMW' के लिए कूट क्या है?"
        ),
        "option_a": "38",
        "option_b": "41",
        "option_c": "43",
        "option_d": "45",
        "correct_answer": "C",
    },
    # Q80
    {
        "question_number": 80,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'ZEAL' is coded as '9476' and 'LAME' is "
            "coded as '8694'. What is the code for 'M' in the given code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'ZEAL' को '9476' और 'LAME' को '8694' के रूप "
            "में कूटबद्ध किया जाता है। दी गई कूट भाषा में 'M' के लिए कूट क्या है?"
        ),
        "option_a": "6",
        "option_b": "8",
        "option_c": "9",
        "option_d": "4",
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
