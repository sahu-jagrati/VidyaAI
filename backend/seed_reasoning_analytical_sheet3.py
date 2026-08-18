"""
seed_reasoning_analytical_sheet3.py
=========================================
Seeds Analytical Reasoning Q7-Q9 from Gagan Pratap Reasoning PDFs (Sheet 3).
Subject : Reasoning
Topic   : Analytical Reasoning
Run     : python seed_reasoning_analytical_sheet3.py

NOTE: Q7 and Q8 already exist in the DB with correct content but
      correct_answer=None. This script will SKIP them (dedup by question_number).
      Their answers and options were patched separately. Q9 was deleted and will
      be re-inserted with the correct content.

Answer key (solutions verified):
  Q7  Statement A: City X banned drug XYZ due to misuse by youth.
      Statement B: City Y lifted its ban on drug XYZ after a rise in Glaucoma cases.
      (a) Drug XYZ is only used for Glaucoma  → FALSE (youth misuse shows other uses)
      (b) Glaucoma patients in X will increase → FALSE (cannot predict future)
      (c) Used by sports persons               → FALSE (sports not mentioned)
      (d) Drug XYZ can be used in Glaucoma treatment → TRUE ✓ (City Y lifted ban for this)
      Answer: D

  Q8  Statements:
        I.   All X-brand cars parked here are white.
        II.  Some of them (parked X-brand cars) have radial tyres.
        III. All X-brand cars made after 1986 have radial tyres.
        IV.  All cars are not X-brand.
      From I + II: Some white X-brand cars parked here have radial tyres.
      → "Some white X-brand cars with radial tyres are parked here."
      Answer: B

  Q9  Premises:
        (1) Teacher → College Graduate
        (2) Poet → Poor
        (3) Some Mathematicians are Poets
        (4) College Graduate → Not Poor  (i.e., no college graduate is poor)
      Question: Which one is NOT a valid conclusion?
      (a) Some Mathematicians are not teachers → VALID
          (Poet → not college grad → not teacher; some Math are Poets → those Math ≠ teachers)
      (b) Some teachers are not Mathematicians → INVALID ✗
          (Nothing in the premises establishes any link between teachers and
           Mathematicians outside of the poet-chain; cannot be derived)
      (c) Teachers are not poor → VALID  (Teacher → Grad → Not Poor)
      (d) Poets are not teachers → VALID (Poet → Poor → Not Grad → Not Teacher)
      Answer: B  (b is NOT a valid conclusion)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SOURCE  = "Gagan_Pratap_Reasoning_Analytical_Sheet3"
SUBJECT = "Reasoning"
TOPIC   = "Analytical Reasoning"

QUESTIONS = [
    # ── Q7 ── Infer from two city statements; drug XYZ and Glaucoma ───────────
    # (Q7 already in DB with correct content; correct_answer patched separately)
    {
        "question_number": 7,
        "difficulty": "medium",
        "question_en": (
            "Statement A: City X has recently banned the sale of a drug XYZ, citing its "
            "misuse by youths for other activities.\n"
            "Statement B: City Y is going to lift its ban on the sale of drug XYZ "
            "following a sharp rise in the number of cases of Glaucoma.\n\n"
            "Which of the following can be inferred from the above statements?"
        ),
        "question_hi": (
            "कथन A: शहर X ने हाल ही में एक दवा XYZ की बिक्री पर प्रतिबंध लगाया, "
            "यह देखते हुए कि युवाओं द्वारा अन्य गतिविधियों के लिए इसका दुरुपयोग "
            "किया जा रहा है।\n"
            "कथन B: शहर Y में ग्लूकोमा के मामलों की संख्या में तेजी से वृद्धि के बाद "
            "दवा XYZ की बिक्री पर प्रतिबंध हटाने वाला है।\n\n"
            "उपरोक्त कथनों से निम्नलिखित में से कौन सा निष्कर्ष निकाला जा सकता है?"
        ),
        "option_a": "Drug XYZ is only used in the treatment of Glaucoma / दवा XYZ का उपयोग केवल ग्लूकोमा के उपचार में किया जाता है",
        "option_b": "The number of Glaucoma patients in City X is going to increase in the future / भविष्य में शहर X में ग्लूकोमा के मरीजों की संख्या बढ़ने वाली है",
        "option_c": "Drug XYZ is also used by sports persons to enhance their athletic performance / दवा XYZ का उपयोग खिलाड़ियों द्वारा एथलेटिक प्रदर्शन को बढ़ाने के लिए भी किया जाता है",
        "option_d": "Drug-XYZ can be used in the treatment of Glaucoma / दवा-XYZ का उपयोग ग्लूकोमा के उपचार में किया जा सकता है",
        "correct_answer": "D",
        # City Y lifted ban specifically to treat Glaucoma → XYZ treats Glaucoma ✓
        # (a) "only" too strong — youth misuse shows other uses
        # (b) City X ≠ City Y; future predictions not valid
        # (c) sports performance nowhere mentioned
    },
    # ── Q8 ── Syllogism with 4 statements about X-brand cars ──────────────────
    {
        "question_number": 8,
        "difficulty": "medium",
        "question_en": (
            "Consider the following statements:\n"
            "I.   All X-brand cars parked here are white.\n"
            "II.  Some of them have radial tyres.\n"
            "III. All X-brand cars manufactured after 1986 have radial tyres.\n"
            "IV.  All cars are not X-brand.\n\n"
            "Which one of the following conclusions can be drawn from the above statements?"
        ),
        "question_hi": (
            "निम्नलिखित कथनों पर विचार कीजिए:\n"
            "I.   यहाँ खड़ी सभी X-ब्रांड कारें सफेद हैं।\n"
            "II.  उनमें से कुछ में रेडियल टायर हैं।\n"
            "III. 1986 के बाद निर्मित सभी X-ब्रांड कारों में रेडियल टायर हैं।\n"
            "IV.  सभी कारें X-ब्रांड नहीं हैं।\n\n"
            "उपरोक्त कथनों से निम्नलिखित में से कौन सा निष्कर्ष निकाला जा सकता है?"
        ),
        "option_a": "Only white cars are parked here / यहाँ केवल सफेद कारें खड़ी हैं",
        "option_b": "Some white X-brand cars with radial tyres are parked here / रेडियल टायर वाली कुछ सफेद X-ब्रांड कारें यहाँ खड़ी हैं",
        "option_c": "Cars other than X-brand cannot have radial tyres / X-ब्रांड के अलावा अन्य कारों में रेडियल टायर नहीं हो सकते",
        "option_d": "Most of the X-brand cars are manufactured before 1986 / अधिकांश X-ब्रांड कारें 1986 से पहले निर्मित की गई हैं",
        "correct_answer": "B",
        # I: parked X-brand cars are white. II: some parked X-brand cars have radial tyres.
        # Combined → Some white X-brand cars with radial tyres are parked here ✓
    },
    # ── Q9 ── Logic: find the INVALID conclusion from teacher/poet premises ────
    {
        "question_number": 9,
        "difficulty": "hard",
        "question_en": (
            "To be a teacher one must graduate from college. All poets are poor. "
            "Some Mathematicians are Poets. No college graduate is poor.\n\n"
            "Which one of the following is NOT a valid conclusion that can be drawn "
            "from the above statements?"
        ),
        "question_hi": (
            "शिक्षक बनने के लिए कॉलेज से स्नातक होना आवश्यक है। सभी कवि गरीब होते हैं। "
            "कुछ गणितज्ञ कवि हैं। कोई भी कॉलेज स्नातक गरीब नहीं है।\n\n"
            "उपरोक्त तर्कों के संबंध में निम्नलिखित में से कौन सा एक वैध निष्कर्ष "
            "नहीं है?"
        ),
        "option_a": "Some Mathematicians are not teachers / कुछ गणितज्ञ शिक्षक नहीं हैं",
        "option_b": "Some teachers are not Mathematicians / कुछ शिक्षक गणितज्ञ नहीं हैं",
        "option_c": "Teachers are not poor / शिक्षक गरीब नहीं हैं",
        "option_d": "Poets are not teachers / कवि शिक्षक नहीं हैं",
        "correct_answer": "B",
        # Premises: Teacher→Grad; Poet→Poor; Some Math=Poet; Grad→NotPoor
        # (a) Some Math are Poets → Poor → not Grad → not Teacher → VALID ✓
        # (b) "Some teachers are not Mathematicians" — nothing in premises links
        #     teachers to mathematicians outside the poet chain → NOT derivable → INVALID ✓
        # (c) Teacher→Grad→NotPoor → Teachers are not poor → VALID ✓
        # (d) Poet→Poor→notGrad→notTeacher → Poets not teachers → VALID ✓
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
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
