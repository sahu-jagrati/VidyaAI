"""
seed_reasoning_coding_decoding_sheet4.py
====================================
Seeds questions 28-36 (Coding-Decoding) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Coding-Decoding
Run     : python seed_reasoning_coding_decoding_sheet4.py

Answer key verification:
  Q28: reverse-alpha positions *2; M(14)+A(26)+P(11)=51*2=102✓; R(9)+O(12)+T(7)=28*2=56✓;
       SEC: S(8)+E(22)+C(24)=54*2=108                                               -> A
  Q29: alternating -1/-4; TASK: T-1=S,A-4=W(wrap),S-1=R,K-4=G -> SWRG              -> A
  Q30: alternating +2/-2; STAR: S+2=U,T-2=R,A+2=C,R-2=P -> URCP                   -> A
  Q31: sum of reverse-alpha positions; MATCH: M(14)+A(26)+T(7)+C(24)+H(19)=90       -> D
  Q32: position-2 concatenated; ROUND: R(16)+O(13)+U(19)+N(12)+D(2)=161319122       -> C
  Q33: unique code for unique word; 'music'='rj'                                     -> B
  Q34: sum_of_positions - num_letters; CAMEL=(3+1+13+5+12)-5=29                     -> B
  Q35: alternating -3/-4; TEAM: T-3=Q,E-4=A,A-3=X(wrap),M-4=I -> QAXI              -> A
  Q36: alternating +3/-4; VOTE: V+3=Y,O-4=K,T+3=W,E-4=A -> YKWA                   -> D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Coding_Decoding_Sheet4"
SUBJECT = "Reasoning"
TOPIC   = "Coding-Decoding"

QUESTIONS = [
    # Q28
    {
        "question_number": 28,
        "difficulty": "medium",
        "question_en": (
            "In a code language, 'MAP' is written as '102' and 'ROT' is written as "
            "'56'. How will 'SEC' be written in that language?"
        ),
        "question_hi": (
            "एक निश्चित कूट भाषा में, 'MAP' को '102' और 'ROT' को '56' के रूप में "
            "लिखा जाता है। उसी कूट भाषा में 'SEC' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "108",
        "option_b": "112",
        "option_c": "98",
        "option_d": "84",
        "correct_answer": "A",
    },
    # Q29
    {
        "question_number": 29,
        "difficulty": "medium",
        "question_en": (
            "In a code language, 'ROAD' is written as 'QKZZ' and 'BAND' is written "
            "as 'AWMZ'. How will 'TASK' be written in that code language?"
        ),
        "question_hi": (
            "एक कूट भाषा में, 'ROAD' को 'QKZZ' और 'BAND' को 'AWMZ' के रूप में "
            "लिखा जाता है। उसी कूट भाषा में 'TASK' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "SWRG",
        "option_b": "RSWG",
        "option_c": "SRGW",
        "option_d": "GRSW",
        "correct_answer": "A",
    },
    # Q30
    {
        "question_number": 30,
        "difficulty": "medium",
        "question_en": (
            "In a code language, 'COOL' is written as 'EMQJ' and 'CARD' is written "
            "as 'EYTB'. How will 'STAR' be written in that language?"
        ),
        "question_hi": (
            "एक कूट भाषा में, 'COOL' को 'EMQJ' और 'CARD' को 'EYTB' के रूप में "
            "लिखा जाता है। उस भाषा में 'STAR' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "URCP",
        "option_b": "UCPR",
        "option_c": "PCUR",
        "option_d": "URPC",
        "correct_answer": "A",
    },
    # Q31
    {
        "question_number": 31,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'HELLO' is coded as 83 and 'SHELL' is coded "
            "as 79. How will 'MATCH' be coded in the same language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'HELLO' को 83 और 'SHELL' को 79 के रूप में "
            "कूटबद्ध किया जाता है। उसी भाषा में 'MATCH' को कैसे कूटबद्ध किया जाएगा?"
        ),
        "option_a": "87",
        "option_b": "96",
        "option_c": "92",
        "option_d": "90",
        "correct_answer": "D",
    },
    # Q32
    {
        "question_number": 32,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'WHILE' is written as '2167103' and 'DEPTH' "
            "is written as '2314186'. How will 'ROUND' be written in that language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'WHILE' को '2167103' और 'DEPTH' को '2314186' "
            "के रूप में लिखा जाता है। उस भाषा में 'ROUND' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "15112021",
        "option_b": "171520145",
        "option_c": "161319122",
        "option_d": "181521154",
        "correct_answer": "C",
    },
    # Q33
    {
        "question_number": 33,
        "difficulty": "easy",
        "question_en": (
            "In a certain code language, 'join the class' is written as 'yq pt dm' "
            "and 'the music class' is written as 'rj yq dm'. How is 'music' written "
            "in the given language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'join the class' को 'yq pt dm' और 'the music "
            "class' को 'rj yq dm' के रूप में लिखा जाता है। दी गई भाषा में 'music' "
            "को कैसे लिखा जाएगा?"
        ),
        "option_a": "yg",
        "option_b": "rj",
        "option_c": "dm",
        "option_d": "pt",
        "correct_answer": "B",
    },
    # Q34
    {
        "question_number": 34,
        "difficulty": "medium",
        "question_en": (
            "In a code language, 'PIG' is coded as 29 and 'COW' is coded as 38. "
            "How will 'CAMEL' be coded in the same language?"
        ),
        "question_hi": (
            "एक कूट भाषा में, 'PIG' को 29 तथा 'COW' को 38 लिखा जाता है। उसी भाषा "
            "में 'CAMEL' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "27",
        "option_b": "29",
        "option_c": "22",
        "option_d": "34",
        "correct_answer": "B",
    },
    # Q35
    {
        "question_number": 35,
        "difficulty": "medium",
        "question_en": (
            "In a code language, 'LAND' is written as 'IWKZ' and 'GOLD' is written "
            "as 'DKIZ'. How will 'TEAM' be written in that language?"
        ),
        "question_hi": (
            "एक कूट भाषा में, 'LAND' को 'IWKZ' और 'GOLD' को 'DKIZ' के रूप में "
            "लिखा जाता है। उस भाषा में 'TEAM' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "QAXI",
        "option_b": "XJQB",
        "option_c": "QXJB",
        "option_d": "JXQB",
        "correct_answer": "A",
    },
    # Q36
    {
        "question_number": 36,
        "difficulty": "medium",
        "question_en": (
            "In a code language, 'CUTE' is written as 'FQWA' and 'BLUE' is written "
            "as 'EHXA'. How will 'VOTE' be written in that language?"
        ),
        "question_hi": (
            "एक कूट भाषा में, 'CUTE' को 'FQWA' और 'BLUE' को 'EHXA' के रूप में "
            "लिखा जाता है। उस भाषा में 'VOTE' को किस प्रकार लिखा जाएगा?"
        ),
        "option_a": "AYWK",
        "option_b": "YWAK",
        "option_c": "YKAW",
        "option_d": "YKWA",
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
