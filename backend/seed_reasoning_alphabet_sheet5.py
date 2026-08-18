"""
seed_reasoning_alphabet_sheet5.py
=========================================
Seeds Alphabet Q35-Q40 from Gagan Pratap Reasoning PDFs.
Subject : Reasoning
Topic   : Alphabet
Run     : python seed_reasoning_alphabet_sheet5.py

NOTE: Ordering questions use "Words: [list] — ..." format so first-80-char
fingerprints are unique (avoids collision with earlier questions sharing the
same long preamble text).

Answer key (solution verified):
  Q35  CAPSULE vowels→prev consonants→next → D  (Two/दो)
       C→D A→Z P→Q S→T U→T L→M E→D → DZQTTMD
       3rd-left=Q(17), 3rd-right=T(20); R,S = 2 between
  Q36  Tertiary/Terrace/Terrain/Termite/Territory/Terminate → C  (6,4,2,3,5,1)
       Terminate<Termite<Terrace<Terrain<Territory<Tertiary
       [CGL-14 July 2023 Shift 4]
  Q37  Strident/Student/Shirking/Stuffy/Spider/Spawn → A  (3,6,5,1,2,4)
       Shirking<Spawn<Spider<Strident<Student<Stuffy
       [CGL-14 July 2023 Shift 2]
  Q38  Salesman/Salvage/Salinity/Salary/Salmon/Salivate → B  (4,1,3,6,5,2)
       Salary<Salesman<Salinity<Salivate<Salmon<Salvage
       [CGL-17 July 2023 Shift 2]
  Q39  Refinery/Reflect/Reference/Refugee/Refillable/Reformist → A  (3,5,1,2,6,4)
       Reference<Refillable<Refinery<Reflect<Reformist<Refugee
       [CGL-17 July 2023 Shift 1]
       NOTE: PDF/user solution says C=(5,1,3,2,6,4) but that puts Refillable(Ref-i)
       before Reference(Ref-e); e<i so Reference MUST come first → stored A.
  Q40  Warriors/Warehouse/Warcraft/Warranty/Wardrobe/Wardenship → D  (3,6,5,2,4,1)
       Warcraft<Wardenship<Wardrobe<Warehouse<Warranty<Warriors
       [CGL-14 July 2023 Shift 1]
       NOTE: PDF/user solution says A=(3,6,5,2,1,4) but Warranty(War-r-A)
       comes before Warriors(War-r-I); A<I → stored D.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Alphabet_Sheet5"
SUBJECT = "Reasoning"
TOPIC   = "Alphabet"

QUESTIONS = [
    # ── Q35 ── CAPSULE: vowels→prev, consonants→next → DZQTTMD ──────────────
    # C→D, A→Z, P→Q, S→T, U→T, L→M, E→D → DZQTTMD
    # 3rd from left = Q (17th); 3rd from right = T (20th); R,S = 2 between
    {
        "question_number": 35,
        "difficulty": "hard",
        "question_en": (
            "Each vowel in the word 'CAPSULE' is changed to the previous letter in the "
            "English alphabetical series and each consonant is changed to the following "
            "letter in the English alphabetical series. In the newly formed word, how many "
            "alphabets are there in the English alphabetical series between the alphabet "
            "which is 3rd from the left and 3rd from the right? "
            "[CGL-18 July 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द 'CAPSULE' में प्रत्येक स्वर को अंग्रेजी वर्णमाला श्रृंखला में पिछले अक्षर से "
            "और प्रत्येक व्यंजन को अगले अक्षर से बदल दिया जाता है। "
            "नवगठित शब्द में, बाएं से तीसरे और दाएं से तीसरे अक्षर के बीच "
            "अंग्रेजी वर्णमाला श्रृंखला में कितने अक्षर हैं?"
        ),
        "option_a": "Three/तीन",
        "option_b": "Four/चार",
        "option_c": "One/एक",
        "option_d": "Two/दो",
        "correct_answer": "D",
        # CAPSULE → D,Z,Q,T,T,M,D; 3rd-left=Q(17), 3rd-right=T(20); R,S = 2 between
    },
    # ── Q36 ── Terminate<Termite<Terrace<Terrain<Territory<Tertiary → 6,4,2,3,5,1 ─
    {
        "question_number": 36,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Tertiary 2.Terrace 3.Terrain 4.Termite 5.Territory 6.Terminate — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CGL-14 July 2023 Shift 4]"
        ),
        "question_hi": (
            "शब्द: 1.Tertiary 2.Terrace 3.Terrain 4.Termite 5.Territory 6.Terminate — "
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "4, 6, 3, 2, 5, 1",
        "option_b": "4, 6, 2, 3, 1, 5",
        "option_c": "6, 4, 2, 3, 5, 1",
        "option_d": "6, 4, 3, 2, 5, 1",
        "correct_answer": "C",
        # Term-i-n(Terminate6) < Term-i-t(Termite4) < Terr-a-c(Terrace2) < Terr-a-i(Terrain3) < Terr-i(Territory5) < Tert(Tertiary1)
    },
    # ── Q37 ── Shirking<Spawn<Spider<Strident<Student<Stuffy → 3,6,5,1,2,4 ────
    {
        "question_number": 37,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Strident 2.Student 3.Shirking 4.Stuffy 5.Spider 6.Spawn — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CGL-14 July 2023 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Strident 2.Student 3.Shirking 4.Stuffy 5.Spider 6.Spawn — "
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "3, 6, 5, 1, 2, 4",
        "option_b": "3, 5, 6, 1, 2, 4",
        "option_c": "3, 6, 5, 1, 4, 2",
        "option_d": "3, 6, 1, 4, 2, 5",
        "correct_answer": "A",
        # Shi(Shirking3) < Spa(Spawn6) < Spi(Spider5) < Str(Strident1) < Stu-d(Student2) < Stu-f(Stuffy4)
    },
    # ── Q38 ── Salary<Salesman<Salinity<Salivate<Salmon<Salvage → 4,1,3,6,5,2 ──
    {
        "question_number": 38,
        "difficulty": "medium",
        "question_en": (
            "Words: 1.Salesman 2.Salvage 3.Salinity 4.Salary 5.Salmon 6.Salivate — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CGL-17 July 2023 Shift 2]"
        ),
        "question_hi": (
            "शब्द: 1.Salesman 2.Salvage 3.Salinity 4.Salary 5.Salmon 6.Salivate — "
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "4, 3, 1, 6, 5, 2",
        "option_b": "4, 1, 3, 6, 5, 2",
        "option_c": "4, 1, 6, 3, 5, 2",
        "option_d": "1, 4, 3, 6, 2, 5",
        "correct_answer": "B",
        # Sal-a(Salary4) < Sal-e(Salesman1) < Sal-i-n(Salinity3) < Sal-i-v(Salivate6) < Sal-m(Salmon5) < Sal-v(Salvage2)
    },
    # ── Q39 ── Reference<Refillable<Refinery<Reflect<Reformist<Refugee → 3,5,1,2,6,4 ─
    # NOTE: User's solution said C=(5,1,3,2,6,4) putting Refillable before Reference,
    # but Reference(Ref-e) must come before Refillable(Ref-i) since e<i → stored A.
    {
        "question_number": 39,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Refinery 2.Reflect 3.Reference 4.Refugee 5.Refillable 6.Reformist — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CGL-17 July 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Refinery 2.Reflect 3.Reference 4.Refugee 5.Refillable 6.Reformist — "
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "3, 5, 1, 2, 6, 4",
        "option_b": "5, 1, 3, 2, 4, 6",
        "option_c": "5, 1, 3, 2, 6, 4",
        "option_d": "2, 3, 1, 5, 2, 6",
        "correct_answer": "A",
        # Ref-e(Reference3) < Ref-i-l(Refillable5) < Ref-i-n(Refinery1) < Ref-l(Reflect2) < Ref-o(Reformist6) < Ref-u(Refugee4)
    },
    # ── Q40 ── Warcraft<Wardenship<Wardrobe<Warehouse<Warranty<Warriors → 3,6,5,2,4,1 ─
    # NOTE: User's solution said A=(3,6,5,2,1,4) putting Warriors before Warranty,
    # but Warranty(War-r-A) comes before Warriors(War-r-I) since A<I → stored D.
    {
        "question_number": 40,
        "difficulty": "hard",
        "question_en": (
            "Words: 1.Warriors 2.Warehouse 3.Warcraft 4.Warranty 5.Wardrobe 6.Wardenship — "
            "Select the option that represents the correct order of the given words "
            "as they would appear in an English dictionary. "
            "[CGL-14 July 2023 Shift 1]"
        ),
        "question_hi": (
            "शब्द: 1.Warriors 2.Warehouse 3.Warcraft 4.Warranty 5.Wardrobe 6.Wardenship — "
            "उस विकल्प का चयन कीजिए, जो दिए गए शब्दों के उस सही क्रम को दर्शाता है "
            "जिसमें वे अंग्रेजी शब्दकोश में दिखाई देते हैं।"
        ),
        "option_a": "3, 6, 5, 2, 1, 4",
        "option_b": "3, 5, 6, 2, 1, 4",
        "option_c": "3, 5, 6, 2, 4, 1",
        "option_d": "3, 6, 5, 2, 4, 1",
        "correct_answer": "D",
        # War-c(Warcraft3) < War-d-e(Wardenship6) < War-d-r(Wardrobe5) < War-e(Warehouse2) < War-r-a(Warranty4) < War-r-i(Warriors1)
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        # Use question_number-based dedup to avoid fingerprint collision issues
        existing_qnums = {
            row[0]
            for row in db.query(Question.question_number)
            .filter(Question.topic == TOPIC, Question.subject == SUBJECT)
            .all()
        }

        for d in QUESTIONS:
            if d["question_number"] in existing_qnums:
                print(f"  SKIP  Q{d['question_number']}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, source_pdf=SOURCE, **d))
            inserted += 1
            print(f"  INSERT Q{d['question_number']}")

        db.commit()
        print(f"\nDone -- inserted: {inserted}, skipped: {skipped}")

    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
