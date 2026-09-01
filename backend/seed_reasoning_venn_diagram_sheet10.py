"""
seed_reasoning_venn_diagram_sheet10.py
========================================
Seeds Reasoning → Venn Diagram  Q70–Q76.

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_venn_diagram_image_urls_batch10.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q70 D  (Circle / Rectangle / Triangle diagram with regions A–F)
     Regions: F, D = triangle only; C = triangle∩rectangle (not circle);
       A = circle∩triangle (not rectangle); B = all three (circle∩rect∩triangle);
       E = rectangle∩triangle (not circle).
     "In all three shapes" = region B only (triple intersection). → D.

Q71 C  (Cricket=25, Tennis=22, Both=16, Total=72)
     People playing at least one game = 25 + 16 + 22 = 63.
     People playing NO game = 72 − 63 = 9. → C.

Q72 A  (Same Cricket/Tennis diagram — students who play ONLY cricket)
     The number in the Cricket-only region (not Tennis) = 25. → A.

Q73 C  (△=40-50 yrs, □=60-70 yrs, ▭=30-40 yrs — Regions 1–7)
     "All three age groups" = triple intersection of triangle, square,
     and rectangle = region 4. → C.

Q74 A  (Educated / Employed / Rural Venn)
     Numbers in diagram: Educated only=16, Educated∩Employed=12,
       Rural∩Educated=22, all three=6, Rural∩Employed=14, Employed only=10,
       Rural only=34.
     "Rural people who are educated" = Rural∩Educated (all subsets)
       = 22 (Rural∩Educated, not Employed) + 6 (all three) = 28. → A.

Q75 D  (Chess / Carrom / Tennis — 60 persons total)
     Regions: Chess only=9, Carrom only=10, Tennis only=12,
       Chess∩Carrom=8, Chess∩Tennis=11, Carrom∩Tennis=some value, center=7.
     Sum of all who play = 9 + 10 + 12 + 8 + 11 + 7 = 57  (approx).
     People playing no game = 60 − 57 = 3. → D.

Q76 C  (Circle=professionals, Square=dancers, Triangle=musicians,
        Rectangle=Europeans — Regions 1–11)
     "Not a musician but a European" = inside Rectangle (European) but
     outside Triangle (musicians) = region 11. → C.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Venn Diagram"

QUESTIONS = [

    # ── Q70 ──────────────────────────────────────────────────────────────────
    # Diagram: circle + rectangle + triangle with regions A, B, C, D, E, F.
    # "In all three shapes" = only region B (triple intersection).
    {
        "question_number": 70,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Study the following diagram consisting of a circle, a rectangle "
            "and a triangle and answer the question given below it. "
            "Which one of the following statements is correct with regard to "
            "the given diagram?"
        ),
        "question_hi": (
            "एक वृत्त, एक आयत और एक त्रिभुज से बने निम्नलिखित आरेख का "
            "अध्ययन करें और नीचे दिए गए प्रश्न का उत्तर दें। "
            "दिए गए आरेख के संबंध में निम्नलिखित में से कौन सा "
            "कथन सही है?"
        ),
        "image_url": None,
        "option_a": (
            "A and B are in all the three shapes / "
            "A और B तीनों आकृतियों में हैं"
        ),
        "option_b": (
            "E, A, B and C are in all the three shapes / "
            "E, A, B और C तीनों आकृतियों में हैं"
        ),
        "option_c": (
            "F, C, D, B and A are in all the three shapes / "
            "F, C, D, B और A तीनों आकृतियों में हैं"
        ),
        "option_d": (
            "Only B is in all the three shapes / "
            "तीनों आकृतियों में केवल B ही है"
        ),
        "correct_answer": "D",
        # Region B is the only region inside all three shapes (triple intersection).
    },

    # ── Q71 ──────────────────────────────────────────────────────────────────
    # Cricket players=25, Tennis players=22, Both=16, Total=72.
    # People playing no game = 72 − (25 + 16 + 22) = 9.
    {
        "question_number": 71,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Find out the number of people who do not play any game."
        ),
        "question_hi": (
            "उन लोगों की संख्या ज्ञात कीजिए जो कोई खेल नहीं खेलते हैं।"
        ),
        "image_url": None,
        "option_a": "18",
        "option_b": "15",
        "option_c": "9",
        "option_d": "24",
        "correct_answer": "C",
        # Total = 72; Cricket only=25, Both=16, Tennis only=22; sum=63.
        # No game = 72 − 63 = 9.
    },

    # ── Q72 ──────────────────────────────────────────────────────────────────
    # Same Cricket/Tennis diagram.
    # "Students who play ONLY cricket" = Cricket-only region = 25.
    {
        "question_number": 72,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Find out the number of students who play only cricket."
        ),
        "question_hi": (
            "उन विद्यार्थियों की संख्या ज्ञात कीजिए जो केवल क्रिकेट खेलते हैं।"
        ),
        "image_url": None,
        "option_a": "25",
        "option_b": "18",
        "option_c": "9",
        "option_d": "24",
        "correct_answer": "A",
        # Cricket-only region = 25 (not in Tennis overlap).
    },

    # ── Q73 ──────────────────────────────────────────────────────────────────
    # Triangle=40-50 yrs, Square=60-70 yrs, Rectangle=30-40 yrs. Regions 1–7.
    # "All three age groups" = triple intersection = region 4.
    {
        "question_number": 73,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Triangle represents people in the first age group i.e. 40-50 years, "
            "Square represents the second age group i.e. 60-70 years and "
            "Rectangle represents the third age group i.e. 30-40 years. "
            "The portion which represents all the three age groups is:"
        ),
        "question_hi": (
            "त्रिभुज पहले आयु वर्ग यानी 40-50 वर्ष के लोगों को दर्शाता है, "
            "वर्ग दूसरे आयु वर्ग यानी 60-70 वर्ष को दर्शाता है और आयत "
            "तीसरे आयु वर्ग यानी 30-40 वर्ष को दर्शाता है। वह भाग जो "
            "तीनों आयु समूहों का प्रतिनिधित्व करता है:"
        ),
        "image_url": None,
        "option_a": "2",
        "option_b": "7",
        "option_c": "4",
        "option_d": "6",
        "correct_answer": "C",
        # Region 4 = triple intersection of triangle (40-50), square (60-70),
        # and rectangle (30-40) — represents all three age groups.
    },

    # ── Q74 ──────────────────────────────────────────────────────────────────
    # Educated (circle), Employed (circle), Rural (outer area).
    # Numbers: 16, 12, 22, 6, 14, 10, 34.
    # "Rural people who are educated" = 22 + 6 = 28.
    {
        "question_number": 74,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "How many rural people are educated?"
        ),
        "question_hi": (
            "कितने ग्रामीण लोग शिक्षित हैं?"
        ),
        "image_url": None,
        "option_a": "28",
        "option_b": "56",
        "option_c": "16",
        "option_d": "44",
        "correct_answer": "A",
        # Rural ∩ Educated = 22 (Rural∩Educated, not Employed) +
        # 6 (Rural∩Educated∩Employed) = 28.
    },

    # ── Q75 ──────────────────────────────────────────────────────────────────
    # Interview of 60 persons — Chess, Carrom, Tennis.
    # Sum of all playing = 9+10+12+8+11+7 = 57. No game = 60 − 57 = 3.
    {
        "question_number": 75,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "An interview of 60 persons to know whether they play Tennis, "
            "Chess or Carrom was conducted. The data so obtained has been "
            "summarized in a pictorial diagram as shown. Study the diagram "
            "and answer the question. How many persons do not play any games?"
        ),
        "question_hi": (
            "यह जानने के लिए कि वे टेनिस, शतरंज या कैरम खेलते हैं, "
            "60 व्यक्तियों का साक्षात्कार लिया गया। इस प्रकार प्राप्त "
            "आंकड़ों को चित्रात्मक आरेख में संक्षिप्त किया गया है जैसा कि "
            "दिखाया गया है। आरेख का अध्ययन करें और प्रश्न का उत्तर दें। "
            "कितने व्यक्ति कोई खेल नहीं खेलते?"
        ),
        "image_url": None,
        "option_a": "28",
        "option_b": "7",
        "option_c": "4",
        "option_d": "3",
        "correct_answer": "D",
        # Total = 60; sum of all regions in circles = 57; no game = 60 − 57 = 3.
    },

    # ── Q76 ──────────────────────────────────────────────────────────────────
    # Circle=professionals, Square=dancers, Triangle=musicians,
    # Rectangle=Europeans. Regions numbered 1–11.
    # "Not a musician but a European" = Rectangle not Triangle = region 11.
    {
        "question_number": 76,
        "difficulty": "hard",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the given diagram, Circle represents professionals, Square "
            "represents dancers, Triangle represents musicians and Rectangle "
            "represents Europeans. Different regions in the diagram are "
            "numbered 1 to 11. "
            "Who among the following is not a musician but a European?"
        ),
        "question_hi": (
            "दिए गए आरेख में, वृत्त पेशेवर को दर्शाता है, वर्ग नर्तकों "
            "को दर्शाता है, त्रिभुज संगीतकारों को दर्शाता है और आयत "
            "यूरो-पीन को दर्शाता है। आरेख में विभिन्न क्षेत्रों को "
            "1 से 11 तक क्रमांकित किया गया है। "
            "निम्नलिखित में से कौन संगीतकार नहीं बल्कि यूरोपीय है?"
        ),
        "image_url": None,
        "option_a": "10",
        "option_b": "9",
        "option_c": "11",
        "option_d": "8",
        "correct_answer": "C",
        # Region 11 = inside Rectangle (Europeans), outside Triangle (musicians).
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Venn Diagram Q70–Q76 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload venn_70.png … venn_76.png to Supabase bucket "
                "'question_image_Venn_Diagram', then run:\n"
                "  python update_venn_diagram_image_urls_batch10.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
