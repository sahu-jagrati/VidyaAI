"""
seed_reasoning_jumbling_sheet3.py
====================================
Seeds Jumbling questions Q33-Q40 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Jumbling
Run     : python seed_reasoning_jumbling_sheet3.py

Two question sub-types:
  Type A (Q33-Q38): Arrange given words in meaningful (logical) order.
  Type B (Q39-Q40): Count meaningful English words formable from given letters
                    (each letter used mandatorily, only once per word).

Answer key (verified via Python):
  Q33  Windows/Walls/Floor/Foundation/Roof/Room   → B  4,2,1,5,3,6  (construction sequence)
  Q34  Police/Punishment/Crime/Justice/Judgement   → D  3,1,4,5,2    (criminal-justice process)
  Q35  Childhood/Adulthood/Infancy/Adolescence/    → B  3,5,1,4,2    (life stages, young→old)
       Babyhood
  Q36  Year/Fortnight/Month/Day/Week               → B  4,5,2,3,1    (time units, small→large)
  Q37  Presentation/Recommendation/Arrival/        → D  3,5,1,4,2    (meeting sequence)
       Discussion/Introduction
  Q38  Hexagon/Triangle/Pentagon/Square/Octagon    → B  2,4,3,1,5    (by side count 3→4→5→6→8)
  Q39  Y,P,R,A  → only PRAY qualifies             → A  One
  Q40  R,O,W,D,C → only CROWD qualifies           → B  One
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Jumbling_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Jumbling"

QUESTIONS = [
    # ── Q33 ── Building construction order ───────────────────────────────────────
    # (1)Windows (2)Walls (3)Floor (4)Foundation (5)Roof (6)Room
    # Order: Foundation→Walls→Windows→Roof→Floor→Room  →  4,2,1,5,3,6
    {
        "question_number": 33,
        "difficulty": "easy",
        "question_en": (
            "Arrange in meaningful order (building construction): "
            "(1)Windows  (2)Walls  (3)Floor  (4)Foundation  (5)Roof  (6)Room"
        ),
        "question_hi": (
            "निम्नलिखित को अर्थपूर्ण क्रम में व्यवस्थित कीजिए (भवन निर्माण): "
            "(1)Windows/खिड़की  (2)Walls/दीवार  (3)Floor/फर्श  "
            "(4)Foundation/नींव  (5)Roof/छत  (6)Room/कमरा"
        ),
        "option_a": "4,5,3,2,1,6",
        "option_b": "4,2,1,5,3,6",
        "option_c": "4,1,5,6,2,3",
        "option_d": "4,3,5,6,2,1",
        "correct_answer": "B",   # Foundation→Walls→Windows→Roof→Floor→Room
    },
    # ── Q34 ── Criminal-justice process ──────────────────────────────────────────
    # (1)Police (2)Punishment (3)Crime (4)Justice (5)Judgement
    # Order: Crime→Police→Justice→Judgement→Punishment  →  3,1,4,5,2
    {
        "question_number": 34,
        "difficulty": "easy",
        "question_en": (
            "Arrange in meaningful order (criminal justice process): "
            "(1)Police  (2)Punishment  (3)Crime  (4)Justice  (5)Judgement"
        ),
        "question_hi": (
            "निम्नलिखित को अर्थपूर्ण क्रम में व्यवस्थित कीजिए (न्याय प्रक्रिया): "
            "(1)Police/पुलिस  (2)Punishment/सजा  (3)Crime/अपराध  "
            "(4)Justice/न्याय  (5)Judgement/निर्णय"
        ),
        "option_a": "3,1,2,4,5",
        "option_b": "1,2,4,3,5",
        "option_c": "5,4,3,2,1",
        "option_d": "3,1,4,5,2",
        "correct_answer": "D",   # Crime→Police→Justice→Judgement→Punishment
    },
    # ── Q35 ── Human life stages (youngest → oldest) ─────────────────────────────
    # (1)Childhood (2)Adulthood (3)Infancy (4)Adolescence (5)Babyhood
    # Order: Infancy→Babyhood→Childhood→Adolescence→Adulthood  →  3,5,1,4,2
    {
        "question_number": 35,
        "difficulty": "easy",
        "question_en": (
            "Arrange in meaningful order (life stages, youngest to oldest): "
            "(1)Childhood  (2)Adulthood  (3)Infancy  (4)Adolescence  (5)Babyhood"
        ),
        "question_hi": (
            "निम्नलिखित को अर्थपूर्ण क्रम में व्यवस्थित कीजिए (जीवन अवस्थाएं, छोटे→बड़े): "
            "(1)Childhood/बचपन  (2)Adulthood/वयस्कता  (3)Infancy/शैशवावस्था  "
            "(4)Adolescence/किशोरावस्था  (5)Babyhood/बाल्यावस्था"
        ),
        "option_a": "4,1,3,2,5",
        "option_b": "3,5,1,4,2",
        "option_c": "2,5,1,4,3",
        "option_d": "5,4,2,3,1",
        "correct_answer": "B",   # Infancy→Babyhood→Childhood→Adolescence→Adulthood
    },
    # ── Q36 ── Time units (smallest → largest) ───────────────────────────────────
    # (1)Year (2)Fortnight (3)Month (4)Day (5)Week
    # Order: Day→Week→Fortnight→Month→Year  →  4,5,2,3,1
    {
        "question_number": 36,
        "difficulty": "easy",
        "question_en": (
            "Arrange in meaningful order (time units, smallest to largest): "
            "(1)Year  (2)Fortnight  (3)Month  (4)Day  (5)Week"
        ),
        "question_hi": (
            "निम्नलिखित को अर्थपूर्ण क्रम में व्यवस्थित कीजिए (समय इकाइयाँ, छोटी→बड़ी): "
            "(1)Year/वर्ष  (2)Fortnight/पखवाड़ा  (3)Month/महीना  (4)Day/दिन  (5)Week/सप्ताह"
        ),
        "option_a": "5,2,3,4,1",
        "option_b": "4,5,2,3,1",
        "option_c": "2,5,4,3,1",
        "option_d": "1,4,5,3,2",
        "correct_answer": "B",   # Day→Week→Fortnight→Month→Year
    },
    # ── Q37 ── Meeting/event sequence ────────────────────────────────────────────
    # (1)Presentation (2)Recommendation (3)Arrival (4)Discussion (5)Introduction
    # Order: Arrival→Introduction→Presentation→Discussion→Recommendation  →  3,5,1,4,2
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": (
            "Arrange in meaningful order (meeting sequence): "
            "(1)Presentation  (2)Recommendation  (3)Arrival  (4)Discussion  (5)Introduction"
        ),
        "question_hi": (
            "निम्नलिखित को अर्थपूर्ण क्रम में व्यवस्थित कीजिए (बैठक क्रम): "
            "(1)Presentation/प्रस्तुतीकरण  (2)Recommendation/सिफारिश  "
            "(3)Arrival/आगमन  (4)Discussion/बहस  (5)Introduction/परिचय"
        ),
        "option_a": "3,5,2,4,1",
        "option_b": "1,2,3,4,5",
        "option_c": "5,4,3,2,1",
        "option_d": "3,5,1,4,2",
        "correct_answer": "D",   # Arrival→Introduction→Presentation→Discussion→Recommendation
    },
    # ── Q38 ── Shapes ordered by number of sides (ascending) ─────────────────────
    # (1)Hexagon(6) (2)Triangle(3) (3)Pentagon(5) (4)Square(4) (5)Octagon(8)
    # Order: Triangle→Square→Pentagon→Hexagon→Octagon  →  2,4,3,1,5
    {
        "question_number": 38,
        "difficulty": "easy",
        "question_en": (
            "Arrange in logical order (by number of sides, ascending): "
            "(1)Hexagon  (2)Triangle  (3)Pentagon  (4)Square  (5)Octagon"
        ),
        "question_hi": (
            "निम्नलिखित को तार्किक क्रम में व्यवस्थित कीजिए (भुजाओं की संख्या के अनुसार, बढ़ते क्रम में): "
            "(1)Hexagon/षट्भुज  (2)Triangle/त्रिभुज  (3)Pentagon/पंचभुज  "
            "(4)Square/वर्ग  (5)Octagon/अष्टभुज"
        ),
        "option_a": "3,1,5,2,4",
        "option_b": "2,4,3,1,5",
        "option_c": "2,1,3,4,5",
        "option_d": "1,4,3,5,2",
        "correct_answer": "B",   # Triangle(3)→Square(4)→Pentagon(5)→Hexagon(6)→Octagon(8)
    },
    # ── Q39 ── Word formation: Y, P, R, A (all letters mandatory, each once) ─────
    # Only PRAY qualifies → One
    {
        "question_number": 39,
        "difficulty": "medium",
        "question_en": (
            "Letters Y, P, R, A — how many meaningful English words can be formed "
            "using each letter mandatorily but only once in each word?"
        ),
        "question_hi": (
            "Y, P, R और A अक्षरों से कितने सार्थक अंग्रेजी शब्द बनाए जा सकते हैं, "
            "जिनमें प्रत्येक अक्षर का अनिवार्य रूप से, लेकिन प्रत्येक शब्द में केवल एक बार प्रयोग किया जाए?"
        ),
        "option_a": "One",
        "option_b": "Two",
        "option_c": "More than two",
        "option_d": "None",
        "correct_answer": "A",   # PRAY is the only valid word
    },
    # ── Q40 ── Word formation: R, O, W, D, C (all letters mandatory, each once) ──
    # Only CROWD qualifies → One
    {
        "question_number": 40,
        "difficulty": "medium",
        "question_en": (
            "Letters R, O, W, D, C — how many meaningful English words can be formed "
            "using each letter mandatorily but only once in each word?"
        ),
        "question_hi": (
            "R, O, W, D और C अक्षरों से कितने सार्थक अंग्रेजी शब्द बनाए जा सकते हैं, "
            "जिनमें प्रत्येक अक्षर का अनिवार्य रूप से, लेकिन प्रत्येक शब्द में केवल एक बार उपयोग किया जाए?"
        ),
        "option_a": "None",
        "option_b": "One",
        "option_c": "More than two",
        "option_d": "Two",
        "correct_answer": "B",   # CROWD is the only valid word
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
            fp = d["question_en"][:80]
            if fp in existing_short:
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
