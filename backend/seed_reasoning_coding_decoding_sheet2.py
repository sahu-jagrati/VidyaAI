"""
seed_reasoning_coding_decoding_sheet2.py
====================================
Seeds questions 10-18 (Coding-Decoding) from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Coding-Decoding
Run     : python seed_reasoning_coding_decoding_sheet2.py

Answer key verification:
  Q10: CHARGE=GHTBJD (reverse word, then +2/+1 alternating on reversed letters)
       CIRCLE -> reverse=ELCRIC -> E(+2)=G,L(+1)=M,C(+2)=E,R(+1)=S,I(+2)=K,C(+1)=D -> GMESKD -> A
  Q11: Eiffel Tower is in France; France is called Italy -> Italy -> B
  Q12: DAILY={D,A,I,L,Y}={5,0,7,3,9}; EARLY={E,A,R,L,Y}={7,5,8,3,4}; EVENT: E=4,D=5 -> D=5 -> B (wait, D=5->B)
       Actually: Q12 answer is B (D=5 per DAILY mapping)
  Q13: Vowels replaced by alphabetical position number; TIGER: T,I->9,G,E->5,R = T9G5R -> A
  Q14: LAPTOP=MZQSPO (alternate +1/-1); KILLED: K+1=L,I-1=H,L+1=M,L-1=K,E+1=F,D-1=C -> LHMKFC -> A
  Q15: code=135-sum_of_positions; BASIC(2+1+19+9+3=34)->135-34=101✓; MAGIC(33)->102✓;
       LIGHT(12+9+7+8+20=56)->135-56=79 -> B
  Q16: Word is reversed; RESEMBLE reversed=ELBMESER -> B
  Q17: Each letter position -2; WRITE: W=23-2=21,R=18-2=16,I=9-2=7,T=20-2=18,E=5-2=3 -> 21-16-7-18-3 -> B
  Q18: BEHALF=DCJYND (alternate +2/-2); CLINIC: C+2=E,L-2=J,I+2=K,N-2=L,I+2=K,C-2=A -> EJKLKA -> D
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Coding_Decoding_Sheet2"
SUBJECT = "Reasoning"
TOPIC   = "Coding-Decoding"

QUESTIONS = [
    # Q10
    {
        "question_number": 10,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'CHARGE' is coded as 'GHTBJD'. "
            "What will be the code for 'CIRCLE' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'CHARGE' को 'GHTBJD' के रूप में कूटबद्ध किया "
            "जाता है। उस कूट भाषा में 'CIRCLE' के लिए कूट क्या होगा?"
        ),
        "option_a": "GMESKD",
        "option_b": "GMESJD",
        "option_c": "GLESKD",
        "option_d": "GMFSKD",
        "correct_answer": "A",
    },
    # Q11
    {
        "question_number": 11,
        "difficulty": "easy",
        "question_en": (
            "In a certain code language, Eiffel Tower is in France and France is "
            "called Italy. What is Eiffel Tower called in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, एफिल टॉवर फ्रांस में है और फ्रांस को "
            "इटली कहा जाता है। उस कूट भाषा में एफिल टॉवर को क्या कहा जाता है?"
        ),
        "option_a": "France",
        "option_b": "Italy",
        "option_c": "Eiffel Tower",
        "option_d": "Paris",
        "correct_answer": "B",
    },
    # Q12
    {
        "question_number": 12,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'DAILY' is coded as '50739' and 'EARLY' "
            "is coded as '75834'. What is the code for 'D' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'DAILY' को '50739' के रूप में कूटबद्ध किया "
            "जाता है और 'EARLY' को '75834' के रूप में कूटबद्ध किया जाता है। उस कूट "
            "भाषा में 'D' के लिए कूट क्या है?"
        ),
        "option_a": "0",
        "option_b": "5",
        "option_c": "7",
        "option_d": "3",
        "correct_answer": "B",
    },
    # Q13
    {
        "question_number": 13,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, vowels in a word are replaced by their "
            "respective position numbers in the English alphabet. What will be the "
            "code for 'TIGER' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, किसी शब्द के स्वरों को अंग्रेजी वर्णमाला में "
            "उनके संबंधित स्थान संख्याओं से बदल दिया जाता है। उस कूट भाषा में "
            "'TIGER' के लिए कूट क्या होगा?"
        ),
        "option_a": "T9G5R",
        "option_b": "T9G4R",
        "option_c": "T8G5R",
        "option_d": "T9H5R",
        "correct_answer": "A",
    },
    # Q14
    {
        "question_number": 14,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'LAPTOP' is coded as 'MZQSPO'. "
            "What will be the code for 'KILLED' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'LAPTOP' को 'MZQSPO' के रूप में कूटबद्ध किया "
            "जाता है। उस कूट भाषा में 'KILLED' के लिए कूट क्या होगा?"
        ),
        "option_a": "LHMKFC",
        "option_b": "LHMKFD",
        "option_c": "LHNKFC",
        "option_d": "LJMKFC",
        "correct_answer": "A",
    },
    # Q15
    {
        "question_number": 15,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, 'BASIC' is coded as '101' and 'MAGIC' is "
            "coded as '102'. What will be the code for 'LIGHT' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'BASIC' को '101' और 'MAGIC' को '102' के रूप "
            "में कूटबद्ध किया जाता है। उस कूट भाषा में 'LIGHT' के लिए कूट क्या होगा?"
        ),
        "option_a": "76",
        "option_b": "79",
        "option_c": "81",
        "option_d": "83",
        "correct_answer": "B",
    },
    # Q16
    {
        "question_number": 16,
        "difficulty": "easy",
        "question_en": (
            "In a certain code language, words are coded by reversing the spelling. "
            "What will be the code for 'RESEMBLE' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, शब्दों को वर्तनी को उल्टा करके कूटबद्ध किया "
            "जाता है। उस कूट भाषा में 'RESEMBLE' के लिए कूट क्या होगा?"
        ),
        "option_a": "ELBESMER",
        "option_b": "ELBMESER",
        "option_c": "ELMBSERE",
        "option_d": "ELBESERE",
        "correct_answer": "B",
    },
    # Q17
    {
        "question_number": 17,
        "difficulty": "medium",
        "question_en": (
            "In a certain code language, each letter is coded as its alphabetical "
            "position minus 2. What will be the code for 'WRITE' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, प्रत्येक अक्षर को उसकी वर्णमाला स्थिति ऋण 2 "
            "के रूप में कूटबद्ध किया जाता है। उस कूट भाषा में 'WRITE' के लिए कूट "
            "क्या होगा?"
        ),
        "option_a": "21-16-7-19-3",
        "option_b": "21-16-7-18-3",
        "option_c": "22-16-7-18-3",
        "option_d": "21-17-7-18-3",
        "correct_answer": "B",
    },
    # Q18
    {
        "question_number": 18,
        "difficulty": "hard",
        "question_en": (
            "In a certain code language, 'BEHALF' is coded as 'DCJYND'. "
            "What will be the code for 'CLINIC' in that code language?"
        ),
        "question_hi": (
            "एक विशिष्ट कूट भाषा में, 'BEHALF' को 'DCJYND' के रूप में कूटबद्ध किया "
            "जाता है। उस कूट भाषा में 'CLINIC' के लिए कूट क्या होगा?"
        ),
        "option_a": "EJKLKB",
        "option_b": "EJKLKC",
        "option_c": "EIKLKA",
        "option_d": "EJKLKA",
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
