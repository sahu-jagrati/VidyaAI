"""
seed_reasoning_coding_decoding_sheet5.py
====================================
Seeds questions 37-45 (Coding-Decoding) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Coding-Decoding
Run     : python seed_reasoning_coding_decoding_sheet5.py

Answer key verification:
  Q37: reverse word then shift -1,-2,-3,-4; FIND->DNIF->C,L,F,B=CLFB✓;
       WILL->LLIW->K,J,F,S=KJFS                                                    -> D
  Q38: each letter +1,+2,+3,+4; LUDO: L+1=M,U+2=W,D+3=G,O+4=S -> MWGS            -> C
  Q39: alternating +4/-4; STEM: S+4=W,T-4=P,E+4=I,M-4=I -> WPII                   -> D
  Q40: reverse word then alternating -1/0; ALLIES->SEILLA->REHLKA✓;
       BALLET->TELLAB->S,E,K,L,Z,B=SEKLZB                                          -> A
  Q41: adjacent pairs swapped; SHILLONG:(SH)(IL)(LO)(NG)->(HS)(LI)(OL)(GN)=HSLIOLGN -> C
  Q42: alternating +4/+2; TOWN: T+4=X,O+2=Q,W+4=A(wrap),N+2=P -> XQAP            -> A
  Q43: sum of reverse-alphabet positions; GOD: G=20,O=12,D=23 -> 55                -> A
  Q44: sum_of_positions*2; PEON: P(16)+E(5)+O(15)+N(14)=50; 50*2=100              -> C
  Q45: sum of letter positions; LAW: L(12)+A(1)+W(23)=36                            -> C
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Coding_Decoding_Sheet5"
SUBJECT = "Reasoning"
TOPIC   = "Coding-Decoding"

QUESTIONS = [
    # Q37
    {
        "question_number": 37,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'FIND' is written as 'CLFB' and 'HOW' is "
            "written as 'VME'. How will 'WILL' be written in that language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'FIND' को 'CLFB' और 'HOW' को 'VME' के रूप "
            "में लिखा जाता है। उस भाषा में 'WILL' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "KSFJ",
        "option_b": "SJFK",
        "option_c": "SFJK",
        "option_d": "KJFS",
        "correct_answer": "D",
    },
    # Q38
    {
        "question_number": 38,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'DICE' is written as 'EKFI' and 'PLAN' is "
            "written as 'QNDR'. How will 'LUDO' be written in that language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'DICE' को 'EKFI' और 'PLAN' को 'QNDR' के रूप "
            "में लिखा जाता है। उस भाषा में 'LUDO' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "NXES",
        "option_b": "NWES",
        "option_c": "MWGS",
        "option_d": "MXES",
        "correct_answer": "C",
    },
    # Q39
    {
        "question_number": 39,
        "difficulty": "medium",
        "question_en": (
            "In a code language, 'RACE' is written as 'VWGA' and 'BANK' is written "
            "as 'FWRG'. How will 'STEM' be written in that language?"
        ),
        "question_hi": (
            "एक कूट भाषा में, 'RACE' को 'VWGA' और 'BANK' को 'FWRG' के रूप में "
            "लिखा जाता है। उस भाषा में 'STEM' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "IIWP",
        "option_b": "WIPI",
        "option_c": "WIIP",
        "option_d": "WPII",
        "correct_answer": "D",
    },
    # Q40
    {
        "question_number": 40,
        "difficulty": "hard",
        "question_en": (
            "In a code language, 'ALLIES' is coded as 'REHLKA'. What is the code "
            "for 'BALLET' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'ALLIES' को 'REHLKA' के रूप में कूटबद्ध "
            "किया जाता है। उस कूट भाषा में 'BALLET' के लिए कूट क्या है?"
        ),
        "option_a": "SEKLZB",
        "option_b": "SDKLZB",
        "option_c": "SEKLZC",
        "option_d": "STKZLB",
        "correct_answer": "A",
    },
    # Q41
    {
        "question_number": 41,
        "difficulty": "medium",
        "question_en": (
            "In certain code languages, if AMRITSAR is coded as MAIRSTRA and "
            "DURGAPUR is coded as UDGRPARU, then what will SHILLONG be coded as?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, यदि AMRITSAR को MAIRSTRA और DURGAPUR को "
            "UDGRPARU के रूप में कूटबद्ध किया जाता है, तो SHILLONG को किस प्रकार "
            "कूटबद्ध किया जाएगा?"
        ),
        "option_a": "GNLIOLSH",
        "option_b": "NGLOILSH",
        "option_c": "HSLIOLGN",
        "option_d": "HSLOILGN",
        "correct_answer": "C",
    },
    # Q42
    {
        "question_number": 42,
        "difficulty": "medium",
        "question_en": (
            "In a code language, 'GAME' is written as 'KCQG' and 'FARM' is written "
            "as 'JCVO'. How will 'TOWN' be written in that code language?"
        ),
        "question_hi": (
            "एक कूट भाषा में, 'GAME' को 'KCQG' और 'FARM' को 'JCVO' के रूप में "
            "लिखा जाता है। उसी कूट भाषा में 'TOWN' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "XQAP",
        "option_b": "PAXQ",
        "option_c": "XAPQ",
        "option_d": "AXQP",
        "correct_answer": "A",
    },
    # Q43
    {
        "question_number": 43,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'FLY' is written as '38' and 'NUT' is "
            "written as '26'. How will 'GOD' be written in that language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, 'FLY' को '38' और 'NUT' को '26' के रूप में "
            "लिखा जाता है। उसी कूट भाषा में 'GOD' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "55",
        "option_b": "34",
        "option_c": "28",
        "option_d": "46",
        "correct_answer": "A",
    },
    # Q44
    {
        "question_number": 44,
        "difficulty": "medium",
        "question_en": (
            "In a code language, 'PEN' is coded as '70' and 'NEST' is coded as "
            "'116'. How will 'PEON' be coded in the same language?"
        ),
        "question_hi": (
            "एक कूट भाषा में, 'PEN' को '70' और 'NEST' को '116' के रूप में कूटबद्ध "
            "किया जाता है। उसी भाषा में 'PEON' को कैसे कूटबद्ध किया जाएगा?"
        ),
        "option_a": "162",
        "option_b": "46",
        "option_c": "100",
        "option_d": "99",
        "correct_answer": "C",
    },
    # Q45
    {
        "question_number": 45,
        "difficulty": "easy",
        "question_en": (
            "In a certain code language, 'JAM' is written as '24' and 'GEL' is "
            "written as '24'. How will 'LAW' be written in that language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, 'JAM' को '24' और 'GEL' को '24' के रूप में "
            "लिखा जाता है। उसी कूट भाषा में 'LAW' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "32",
        "option_b": "24",
        "option_c": "36",
        "option_d": "48",
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
