"""
seed_permcomb_sheet4.py
========================
Seeds questions 28–37 (visible) from Permutation & Combination,
Gagan Pratap Sir PDFs.
Subject : Quant
Topic   : Permutation & Combination
Run     : python seed_permcomb_sheet4.py

Answer key verification:
  Q28: ARRANGE (A×2,R×2): total=7!/(2!×2!)=1260;
       (1)R together=6!/2!=360; (2)R not together=900; (3)R&A together=5!=120  → A
  Q29: PUZZLE (Z×2), vowels(U,E) together: 5!/2!×2!=120                        → D
  Q30: SOFTWARE all-distinct, vowels(O,A,E) together: 6!×3!=4320               → A
  Q31: ADJUST total=720; vowels(A,U) together=5!×2!=240; NOT together=480      → D
  Q33: PRACTICE (C×2), 3 vowels at even positions: C(4,3)×3!×5!/2!=1440       → B
  Q36: 7 students, 2 English not together: 7!−6!×2!=3600                       → C
  Q37: 8 candidates(3 Math), no two Math adjacent: 5!×C(6,3)×3!=14400         → a
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

SOURCE  = "Gagan_Pratap_PermComb_Sheet4"
SUBJECT = "Quant"
TOPIC   = "Permutation & Combination"

QUESTIONS = [
    # Q28 — multi-part (no MCQ options in PDF; answers encoded in option text)
    {
        "question_number": 28,
        "difficulty": "hard",
        "question_en": (
            "How many ways can the letters of the word 'ARRANGE' be arranged? "
            "Also find: (1) both R's come together, "
            "(2) both R's do not come together, "
            "(3) both R's and both A's come together."
        ),
        "question_hi": (
            "'ARRANGE' शब्द के अक्षरों को कितने तरीकों से व्यवस्थित किया जा सकता है? "
            "उनमें से कितनी व्यवस्थाएँ हैं जिनमें: "
            "(1) दो R एक साथ आते हैं, "
            "(2) दो R एक साथ नहीं आते हैं, "
            "(3) दो R और दो A एक साथ आते हैं?"
        ),
        "option_a": "Total=1260; (1) R together=360; (2) R not together=900; (3) R & A together=120",
        "option_b": "Total=1260; (1) R together=480; (2) R not together=780; (3) R & A together=60",
        "option_c": "Total=2520; (1) R together=720; (2) R not together=1800; (3) R & A together=240",
        "option_d": "Total=5040; (1) R together=1440; (2) R not together=3600; (3) R & A together=120",
        "correct_answer": "A",
    },
    # Q29
    {
        "question_number": 29,
        "difficulty": "medium",
        "question_en": "In what ways can the letters of the word 'PUZZLE' be arranged to form different new words so that the vowels always come together?",
        "question_hi": "'PUZZLE' शब्द के अक्षरों को अलग-अलग नए शब्द बनाने के लिए किस प्रकार व्यवस्थित किया जा सकता है ताकि स्वर हमेशा एक साथ आएं?",
        "option_a": "280",
        "option_b": "450",
        "option_c": "630",
        "option_d": "120",
        "correct_answer": "D",
    },
    # Q30
    {
        "question_number": 30,
        "difficulty": "medium",
        "question_en": "In how many different ways can the letters of the word 'SOFTWARE' be arranged in such a way that the vowels come together?",
        "question_hi": "'SOFTWARE' शब्द के अक्षरों को कितने अलग-अलग तरीकों से इस प्रकार व्यवस्थित किया जा सकता है कि स्वर एक साथ आ जाएँ?",
        "option_a": "4320",
        "option_b": "1440",
        "option_c": "360",
        "option_d": "120",
        "correct_answer": "A",
    },
    # Q31
    {
        "question_number": 31,
        "difficulty": "medium",
        "question_en": "In how many ways can the letters of the word ADJUST be arranged so that vowels do not come together?",
        "question_hi": "ADJUST शब्द के अक्षरों को कितने तरीकों से व्यवस्थित किया जा सकता है ताकि स्वर एक साथ न आएं?",
        "option_a": "720",
        "option_b": "240",
        "option_c": "360",
        "option_d": "480",
        "correct_answer": "D",
    },
    # Q33
    {
        "question_number": 33,
        "difficulty": "hard",
        "question_en": "How many words can be formed with the letters of the word 'PRACTICE' so that vowels always occupy the even places?",
        "question_hi": "'PRACTICE' शब्द के अक्षरों से कितने शब्द बनाए जा सकते हैं ताकि स्वर हमेशा सम स्थानों पर हों?",
        "option_a": "4320",
        "option_b": "1440",
        "option_c": "360",
        "option_d": "120",
        "correct_answer": "B",
    },
    # Q36
    {
        "question_number": 36,
        "difficulty": "medium",
        "question_en": "7 students take an exam. Two of them are from English medium. Find the possible number of ways when both English medium students do not sit together?",
        "question_hi": "7 छात्र परीक्षा देते हैं। इनमें से दो अंग्रेजी माध्यम से हैं। उन तरीकों की संभावित संख्या ज्ञात कीजिए जब दोनों अंग्रेजी माध्यम के छात्र एक साथ नहीं बैठते हैं?",
        "option_a": "2400",
        "option_b": "1200",
        "option_c": "3600",
        "option_d": "4800",
        "correct_answer": "C",
    },
    # Q37
    {
        "question_number": 37,
        "difficulty": "hard",
        "question_en": "8 candidates are to be examined, 3 in Mathematics and the remaining in different subjects. In how many ways can they be seated in a row so that no two Mathematics candidates sit together?",
        "question_hi": "8 अभ्यर्थियों की परीक्षा होनी है, 3 गणित में और शेष अन्य विषयों में। उन्हें कितने प्रकार से एक पंक्ति में बैठाया जा सकता है ताकि गणित के दो परीक्षार्थी एक साथ न बैठें?",
        "option_a": "14400",
        "option_b": "7200",
        "option_c": "3600",
        "option_d": "10800",
        "correct_answer": "A",
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
        print(f"\nDone — inserted: {inserted}, skipped (duplicate): {skipped}")
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
