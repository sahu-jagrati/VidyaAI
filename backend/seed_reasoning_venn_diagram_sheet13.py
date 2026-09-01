"""
seed_reasoning_venn_diagram_sheet13.py
========================================
Seeds Reasoning → Venn Diagram  Q91–Q95.

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_venn_diagram_image_urls_batch13.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q91 B  (Circle=Graduates, Triangle=Sub-Inspector of Police,
        Parallelogram=Women; regions labeled 2,7,5,6,3)
     "Women Graduates and Sub-Inspector" = all three shapes overlapping.
     Triple intersection = region 5. → B.

Q92 D  (Square=Doctors, Circle=Players, Rectangle=Artists; regions 1–7)
     "Doctors who are Players as well as Artists" =
     Square ∩ Circle ∩ Rectangle (triple intersection) = region 6. → D.

Q93 C  (Triangle=Qualified Doctors, Rectangle=Experienced Doctors,
        Circle=Doctors Working in Village; regions 1–6)
     "Qualified AND Experienced Doctors working in villages" =
     Triple intersection of all three shapes = region 5. → C.

Q94 B  (Youth / Graduates / Employed Venn)
     Diagram numbers (exclusive regions):
       Youth only=100, Youth∩Grad excl=20, Grad only=500,
       Youth∩Emp excl=40, triple=10, Grad∩Emp excl=50, Emp only=30.
     "Youth Graduates" = Youth ∩ Graduates = 20 + 10 = 30. → B.

Q95 C  (Four-circle Venn: Biology, Physics, Math, Chemistry seminars)
     Diagram numbers: 6(Bio∩Phys), 8(Physics only), 5(Bio∩Math),
       7(Bio∩Chem), 14(triple Bio∩Phys∩Math), 10(Math∩Chem),
       10(Phys∩Chem), 13(Chemistry only).
     "Exactly two seminars" = sum of all exactly-two-circle regions:
       6 + 5 + 7 + 10 + 10 = 38. → C.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Venn Diagram"

QUESTIONS = [

    # ── Q91 ──────────────────────────────────────────────────────────────────
    # Circle=Graduates, Triangle=Sub-Inspector of Police, Parallelogram=Women.
    # "Women Graduates and Sub-Inspector" = triple intersection = region 5.
    {
        "question_number": 91,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following figure, circle represents Graduates, triangle "
            "represents Sub-Inspector of Police, and parallelogram represents "
            "Women. Then, which number space represents Women Graduate and "
            "Sub-Inspector of Police?"
        ),
        "question_hi": (
            "निम्नलिखित आकृति में, वृत्त स्नातकों को दर्शाता है, त्रिभुज "
            "पुलिस उप-निरीक्षक को दर्शाता है, और समानांतर चतुर्भुज "
            "महिलाओं को दर्शाता है। फिर, कौन सा अंक स्थान महिला "
            "स्नातक और पुलिस उप-निरीक्षक को दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "2",
        "option_b": "5",
        "option_c": "7",
        "option_d": "6",
        "correct_answer": "B",
        # Region 5 = Circle (Graduates) ∩ Triangle (Sub-Inspector) ∩
        # Parallelogram (Women) — the triple intersection.
    },

    # ── Q92 ──────────────────────────────────────────────────────────────────
    # Square=Doctors, Circle=Players, Rectangle=Artists. Regions 1–7.
    # "Doctors AND Players AND Artists" = triple intersection = region 6.
    {
        "question_number": 92,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following diagram, Square represents Doctors, Circle "
            "represents Players and Rectangle represents Artists. Which number "
            "represents those Doctors who are Players as well as Artists?"
        ),
        "question_hi": (
            "निम्नलिखित आरेख में, वर्ग डॉक्टरों को दर्शाता है, वृत्त "
            "खिलाड़ियों को दर्शाता है और आयत कलाकारों को दर्शाती है। "
            "कौन सी संख्या उन डॉक्टरों को दर्शाती है जो खिलाड़ी होने "
            "के साथ-साथ कलाकार भी हैं?"
        ),
        "image_url": None,
        "option_a": "7",
        "option_b": "2",
        "option_c": "3",
        "option_d": "6",
        "correct_answer": "D",
        # Region 6 = Square (Doctors) ∩ Circle (Players) ∩ Rectangle (Artists)
        # = triple intersection of all three shapes.
    },

    # ── Q93 ──────────────────────────────────────────────────────────────────
    # Triangle=Qualified Doctors, Rectangle=Experienced Doctors,
    # Circle=Doctors Working in Village. Regions 1–6.
    # "Qualified AND Experienced AND Village" = triple intersection = region 5.
    {
        "question_number": 93,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Study the diagram given below and answer the question. The "
            "qualified and experienced doctors working in villages are "
            "represented by:"
        ),
        "question_hi": (
            "नीचे दिए गए चित्र का अध्ययन करें और प्रश्न का उत्तर दें। "
            "गाँवों में काम करने वाले योग्य और अनुभवी डॉक्टरों की "
            "प्रतिनिधि निम्नलिखित द्वारा किया जाता है:"
        ),
        "image_url": None,
        "option_a": "6",
        "option_b": "4",
        "option_c": "5",
        "option_d": "2",
        "correct_answer": "C",
        # Region 5 = Triangle (Qualified) ∩ Rectangle (Experienced) ∩
        # Circle (Village) — triple intersection = qualified+experienced+village.
    },

    # ── Q94 ──────────────────────────────────────────────────────────────────
    # Youth / Graduates / Employed Venn diagram.
    # Numbers: Youth only=100, Youth∩Grad excl=20, Grad only=500,
    #           Youth∩Emp excl=40, triple=10, Grad∩Emp excl=50, Emp only=30.
    # "Youth Graduates" = Youth ∩ Graduates = 20 + 10 = 30.
    {
        "question_number": 94,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "If the number indicates the number of persons, then how many "
            "youth graduates are there?"
        ),
        "question_hi": (
            "यदि संख्या व्यक्तियों की संख्या दर्शाती है, तो कितने युवा "
            "स्नातक हैं?"
        ),
        "image_url": None,
        "option_a": "20",
        "option_b": "30",
        "option_c": "40",
        "option_d": "50",
        "correct_answer": "B",
        # Youth∩Graduates = 20 (excl, not Employed) + 10 (all three) = 30.
    },

    # ── Q95 ──────────────────────────────────────────────────────────────────
    # Four-circle Venn: Biology, Physics, Math, Chemistry seminars.
    # Numbers: 6(Bio∩Phys), 8(Physics only), 5(Bio∩Math), 7(Bio∩Chem),
    #           14(triple), 10(Math∩Chem), 10(Phys∩Chem), 13(Chem only).
    # "Exactly two seminars" = 6 + 5 + 7 + 10 + 10 = 38.
    {
        "question_number": 95,
        "difficulty": "hard",
        "source_pdf": "Practice_Set",
        "question_en": (
            "The Venn diagram below shows the number of people who attended "
            "seminars on Physics, Chemistry, Maths and Biology. What is the "
            "number of people who attended exactly any two seminars?"
        ),
        "question_hi": (
            "नीचे दिया गया वेन आरेख भौतिकी, रसायन विज्ञान, गणित और जीव "
            "विज्ञान पर सेमिनार में भाग लेने वाले लोगों की संख्या दर्शाता "
            "है। किन्हीं दो सेमिनारों में भाग लेने वाले लोगों की संख्या क्या है?"
        ),
        "image_url": None,
        "option_a": "21",
        "option_b": "36",
        "option_c": "38",
        "option_d": "42",
        "correct_answer": "C",
        # Exactly-two overlap regions: 6(Bio∩Phys) + 5(Bio∩Math) +
        # 7(Bio∩Chem) + 10(Math∩Chem) + 10(Phys∩Chem) = 38.
        # (14 = triple overlap, 8 = Physics only, 13 = Chemistry only — excluded.)
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Venn Diagram Q91–Q95 into '{TOPIC}' / '{SUBJECT}'")

        for d in QUESTIONS:
            qn = d["question_number"]
            exists = (
                db.query(Question)
                .filter(
                    Question.subject == SUBJECT,
                    Question.topic == TOPIC,
                    Question.question_number == qn,
                )
                .first()
            )
            if exists:
                print(f"  SKIP  Q{qn}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
            inserted += 1
            print(f"  INSERT Q{qn}")

        db.commit()
        print(f"\nDone — inserted: {inserted}, skipped: {skipped}")
        if inserted:
            print(
                "\n  Upload venn_91.png … venn_95.png to Supabase bucket "
                "'question_image_Venn_Diagram', then run:\n"
                "  python update_venn_diagram_image_urls_batch13.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
