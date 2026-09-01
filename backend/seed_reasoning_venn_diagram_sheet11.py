"""
seed_reasoning_venn_diagram_sheet11.py
========================================
Seeds Reasoning → Venn Diagram  Q77–Q84.

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_venn_diagram_image_urls_batch11.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q77 D  (Marathi/English/Hindi Venn — 1000 persons — only Hindi)
     Diagram shows exclusive counts per region:
       Marathi only=170, M∩E not H=105, English only=180,
       M∩H not E=85, E∩H not M=78, Hindi only=200, center=X.
     "Knew only Hindi" = Hindi-only region = 200. → D.

Q78 A  (Rectangle=English newspaper, Circle=Urban, Triangle=Kannada)
     "Non-urban people who read English newspaper" =
     inside Rectangle (English) but OUTSIDE Circle (urban).
     From labeled regions N, M, O, P — region N lies in the Rectangle
     but outside the Circle. → A.

Q79 D  (Circle=Strong men, Square=Short men, Triangle=Military officers)
     "Military officers who are short but NOT strong" =
     inside Triangle (military) AND Square (short), OUTSIDE Circle (strong).
     From numbered regions 1–4 = region 2. → D.

Q80 B  (Same Marathi/English/Hindi Venn — know ALL THREE languages)
     "Know all three languages" = triple intersection (center region) = 85.
     → B.

Q81 A  (Same Venn — 105 people know ___ languages)
     Region with 105 = Marathi ∩ English overlap (not Hindi).
     → 105 people know Marathi and English (not Hindi). → A.

Q82 B  (Triangle=Mysore, Circle=Ooty, Square=Munnar — visited Mysore AND Ooty)
     "Visited BOTH Mysore AND Ooty" = Triangle ∩ Circle region.
     From labeled regions A, B, C, D, E, F, G — region G represents
     the overlap of Triangle (Mysore) and Circle (Ooty). → B.

Q83 B  (Three circles — students studying three different subjects)
     "Students who study all three subjects" = triple intersection = 3.
     → B.

Q84 B  (Mathematics / Biology / Computer circles — regions 1–7)
     "Students studying Biology AND Computer NOT Mathematics" =
     Biology ∩ Computer, outside Mathematics circle = region 7. → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Venn Diagram"

QUESTIONS = [

    # ── Q77 ──────────────────────────────────────────────────────────────────
    # Marathi(170)/English(180)/Hindi(200) Venn; 1000 persons.
    # "Only Hindi" = Hindi-only region = 200.
    {
        "question_number": 77,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "The above diagram shows the survey on a sample of 1000 persons "
            "with reference to their knowledge of English, Hindi and Marathi. "
            "How many knew only Hindi?"
        ),
        "question_hi": (
            "उपरोक्त चित्र अंग्रेजी, हिंदी और मराठी के उनके ज्ञान के "
            "संदर्भ में 1000 व्यक्तियों के नमूने पर सर्वेक्षण दिखाता है। "
            "कितने लोग केवल हिंदी जानते थे?"
        ),
        "image_url": None,
        "option_a": "85",
        "option_b": "175",
        "option_c": "78",
        "option_d": "200",
        "correct_answer": "D",
        # Hindi-only region in the Venn diagram = 200.
    },

    # ── Q78 ──────────────────────────────────────────────────────────────────
    # Rectangle=English newspaper, Circle=Urban, Triangle=Kannada newspaper.
    # "Non-urban English readers" = Rectangle not Circle = region N.
    {
        "question_number": 78,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following diagram, rectangle represents people who read "
            "English newspaper, circle represents urban, and triangle represents "
            "people who read Kannada newspaper. Which region represents "
            "non-urban people who read English newspaper?"
        ),
        "question_hi": (
            "निम्नलिखित आरेख में, आयत अंग्रेजी अखबार पढ़ने वाले लोगों "
            "को दर्शाती है, वृत्त शहरी को दर्शाता है, और त्रिकोण कन्नड़ "
            "अखबार पढ़ने वाले लोगों को दर्शाता है। कौन सा क्षेत्र अंग्रेजी "
            "अखबार पढ़ने वाले गैर-शहरी लोगों का प्रतिनिधित्व करता है?"
        ),
        "image_url": None,
        "option_a": "N",
        "option_b": "M",
        "option_c": "P",
        "option_d": "O",
        "correct_answer": "A",
        # Region N = inside Rectangle (English) but outside Circle (urban).
    },

    # ── Q79 ──────────────────────────────────────────────────────────────────
    # Circle=Strong men, Square=Short men, Triangle=Military officers.
    # "Short military NOT strong" = Square ∩ Triangle, outside Circle = region 2.
    {
        "question_number": 79,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the given diagram, Circle represents strong men and Square "
            "represents short men and Triangle represents military officers. "
            "Which region represents military officers who are short but not strong?"
        ),
        "question_hi": (
            "दिए गए आरेख में, वृत्त मजबूत पुरुषों को दर्शाता है, वर्ग "
            "छोटे कद वाले पुरुषों को दर्शाता है और त्रिभुज सैन्य "
            "अधिकारियों को दर्शाता है। कौन सा क्षेत्र उन सैन्य "
            "अधिकारियों का प्रतिनिधित्व करता है जो छोटे हैं लेकिन "
            "मजबूत नहीं हैं?"
        ),
        "image_url": None,
        "option_a": "3",
        "option_b": "4",
        "option_c": "1",
        "option_d": "2",
        "correct_answer": "D",
        # Region 2 = Square (short) ∩ Triangle (military), outside Circle (strong).
    },

    # ── Q80 ──────────────────────────────────────────────────────────────────
    # Same Marathi/English/Hindi Venn (1000 persons).
    # "Know ALL THREE languages" = triple intersection (center) = 85.
    {
        "question_number": 80,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Study the following diagram carefully and answer the questions "
            "based on it. The diagram shows the survey on a sample of 1000 "
            "persons with reference to their knowledge of English, Hindi and "
            "Marathi. How many know all the languages?"
        ),
        "question_hi": (
            "निम्नलिखित आरेख का ध्यानपूर्वक अध्ययन करें और उस पर "
            "आधारित प्रश्नों के उत्तर दें। आरेख अंग्रेजी, हिंदी और "
            "मराठी के उनके ज्ञान के संदर्भ में 1000 व्यक्तियों के नमूने "
            "पर सर्वेक्षण दिखाता है। कितने लोग सभी भाषाएँ जानते हैं?"
        ),
        "image_url": None,
        "option_a": "105",
        "option_b": "85",
        "option_c": "78",
        "option_d": "175",
        "correct_answer": "B",
        # Center region (Marathi ∩ English ∩ Hindi) = 85.
    },

    # ── Q81 ──────────────────────────────────────────────────────────────────
    # Same Venn. "105 people know ___ languages."
    # 105 is in the Marathi ∩ English region (not Hindi) → Marathi + English.
    {
        "question_number": 81,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Study the following diagram carefully and answer the questions "
            "based on it. 105 people know ___ languages."
        ),
        "question_hi": (
            "निम्नलिखित आरेख का ध्यानपूर्वक अध्ययन करें और उस पर "
            "आधारित प्रश्नों के उत्तर दें। 105 लोग ___ भाषाएँ जानते हैं।"
        ),
        "image_url": None,
        "option_a": "Marathi, English / मराठी, अंग्रेजी",
        "option_b": "Hindi, Marathi, English / हिंदी, मराठी, अंग्रेजी",
        "option_c": "Marathi, Hindi / मराठी, हिंदी",
        "option_d": "English, Hindi / अंग्रेजी, हिंदी",
        "correct_answer": "A",
        # Region with 105 = Marathi ∩ English overlap (not Hindi).
    },

    # ── Q82 ──────────────────────────────────────────────────────────────────
    # Triangle=Mysore visitors, Circle=Ooty visitors, Square=Munnar visitors.
    # "Visited BOTH Mysore AND Ooty" = Triangle ∩ Circle = region G.
    {
        "question_number": 82,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the given figure the triangle represents people who visited "
            "Mysore, the circle represents people who visited Ooty, the square "
            "represents people who visited Munnar. The portion which represents "
            "people who visited both Mysore and Ooty is?"
        ),
        "question_hi": (
            "दिए गए चित्र में त्रिभुज उन लोगों को दर्शाता है जो मैसूर "
            "गए थे, वृत्त उन लोगों को दर्शाता है जो ऊटी गए थे, वर्ग "
            "उन लोगों को दर्शाता है जो मुन्नार गए थे। वह भाग जो मैसूर "
            "और ऊटी दोनों का दौरा करने वाले लोगों का प्रतिनिधित्व करता है?"
        ),
        "image_url": None,
        "option_a": "D",
        "option_b": "G",
        "option_c": "B",
        "option_d": "C",
        "correct_answer": "B",
        # Region G = Triangle (Mysore) ∩ Circle (Ooty) overlap area.
    },

    # ── Q83 ──────────────────────────────────────────────────────────────────
    # Three circles represent students studying three different subjects.
    # "Students who study all three subjects" = triple intersection = 3.
    {
        "question_number": 83,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the given figure, circles represent students studying three "
            "different subjects. How many students study all the three subjects?"
        ),
        "question_hi": (
            "दिए गए चित्र में, वृत्त तीन अलग-अलग विषयों का अध्ययन "
            "करने वाले छात्रों को दर्शाते हैं। कितने छात्र तीनों विषय पढ़ते हैं?"
        ),
        "image_url": None,
        "option_a": "2",
        "option_b": "3",
        "option_c": "4",
        "option_d": "1",
        "correct_answer": "B",
        # Triple intersection (center) of the three subject circles = 3.
    },

    # ── Q84 ──────────────────────────────────────────────────────────────────
    # Three circles: Mathematics Students (left), Biology Students (right),
    # Computer Students (bottom). Regions numbered 1–7.
    # "Biology AND Computer NOT Mathematics" = Biology∩Computer outside Math = 7.
    {
        "question_number": 84,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Identify the region that represents students studying Biology "
            "and Computer not Mathematics."
        ),
        "question_hi": (
            "उस क्षेत्र की पहचान करें जो गणित का नहीं बल्कि जीव "
            "विज्ञान और कंप्यूटर का अध्ययन करने वाले छात्रों का "
            "प्रतिनिधित्व करता है।"
        ),
        "image_url": None,
        "option_a": "2",
        "option_b": "7",
        "option_c": "4",
        "option_d": "6",
        "correct_answer": "B",
        # Region 7 = Biology ∩ Computer, outside Mathematics circle.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Venn Diagram Q77–Q84 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload venn_77.png … venn_84.png to Supabase bucket "
                "'question_image_Venn_Diagram', then run:\n"
                "  python update_venn_diagram_image_urls_batch11.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
