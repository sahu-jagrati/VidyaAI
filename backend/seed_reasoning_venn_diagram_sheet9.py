"""
seed_reasoning_venn_diagram_sheet9.py
=======================================
Seeds Reasoning → Venn Diagram  Q65–Q69.

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_venn_diagram_image_urls_batch9.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q65 D  (Arts / Commerce / Economics Venn — Art OR Economics but NOT both)
     "Art or Economics but not both" = symmetric difference of Arts and
     Economics circles:
       • Art but NOT Economics: A (Arts only) + M (Arts∩Commerce, not Econ)
         → covered by region A
       • Economics but NOT Art: D (Economics only) + N (Econ∩Commerce, not Arts)
         → covered by region D and N
     Combined regions that appear in EITHER Arts OR Economics but NOT the
     intersection of both = A + N + D. → D.
     (Excludes the center/Arts∩Economics region and Commerce-only region C.)

Q66 D  (Kabaddi / Football / Cricket — students who play all 3 games)
     The Venn diagram shows Kabaddi (outer rectangle) containing the
     overlapping Football and Cricket circles. Regions inside the diagram:
       A, B, C = Kabaddi only (top row, outside Football/Cricket circles)
       D = Kabaddi ∩ Football ∩ Cricket (triple intersection — all 3 games)
       E = Football ∩ Kabaddi (not Cricket)
       F = Cricket ∩ Kabaddi (not Football)
       G = Football ∩ Cricket only (outside Kabaddi rectangle)
     "Students who play all 3 games" = region D (inside all three). → D.

Q67 C  (Indians / Dramatists / Agriculturists — three intersecting circles,
        regions 1–7. Statement: Indians who are Dramatists AND Agriculturists)
     Three circles: A = Indians (top-left), B = Dramatists (top-right),
     C = Agriculturists (bottom). Regions numbered 1–7.
     "Indians AND Dramatists AND Agriculturists" = triple intersection = region 3.
     → C.

Q68 A  (Employed / Girls / Married Venn — girls who are employed but unmarried)
     Three circles: Employed (left), Girls (right), Married (bottom).
     "Girls who are Employed but NOT Married" = Girls ∩ Employed region,
     excluding Married = region 1. → A.

Q69 B  (Educated / Employed / Rural Venn — rural uneducated people employed)
     Venn diagram: Educated (left circle), Employed (right circle), Rural
     (area outside/below both circles). Numbers: 10, 22, 6, 14, 34.
     "Rural uneducated people who are employed" = Employed ∩ Rural, NOT
     Educated = region labeled 6. → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Venn Diagram"

QUESTIONS = [

    # ── Q65 ──────────────────────────────────────────────────────────────────
    # Arts / Commerce / Economics three-circle Venn.
    # "Art OR Economics but NOT both" = A + N + D (symmetric difference).
    {
        "question_number": 65,
        "difficulty": "hard",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Study the diagram and identify the region which represents "
            "students who study Art or Economics but not both."
        ),
        "question_hi": (
            "आरेख का अध्ययन करें और उस क्षेत्र की पहचान करें जो "
            "कला या अर्थशास्त्र का अध्ययन करने वाले छात्रों का "
            "प्रतिनिधित्व करता है लेकिन दोनों का नहीं।"
        ),
        "image_url": None,
        "option_a": "A + D",
        "option_b": "A + M + D + C",
        "option_c": "A + M + N + C + D",
        "option_d": "A + N + D",
        "correct_answer": "D",
        # Symmetric difference of Arts and Economics:
        # A (Arts only) + N (Econ∩Commerce not Arts) + D (Economics only).
    },

    # ── Q66 ──────────────────────────────────────────────────────────────────
    # Kabaddi (rectangle) / Football (circle) / Cricket (circle).
    # "Students who play all 3 games" = triple intersection = region D.
    {
        "question_number": 66,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "The diagram below represents the students who play cricket, "
            "football and kabaddi. Seeing the diagram indicate the students "
            "who play all the 3 games."
        ),
        "question_hi": (
            "नीचे दिया गया चित्र उन छात्रों को दर्शाता है जो क्रिकेट, "
            "फुटबॉल और कबड्डी खेलते हैं। आरेख को देखकर उन विद्यार्थियों "
            "को दर्शाया गया जो सभी 3 खेल खेलते हैं।"
        ),
        "image_url": None,
        "option_a": "A + B + C",
        "option_b": "G + E",
        "option_c": "D + E + G",
        "option_d": "D",
        "correct_answer": "D",
        # Region D = Kabaddi ∩ Football ∩ Cricket (inside all three shapes).
    },

    # ── Q67 ──────────────────────────────────────────────────────────────────
    # Three circles: A=Indians, B=Dramatists, C=Agriculturists. Regions 1–7.
    # "Indians who are Dramatists AND Agriculturists" = triple intersection = 3.
    {
        "question_number": 67,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the given figure, there are three intersecting circles "
            "representing certain sections of people. Different sections are "
            "marked by numbers 1 to 7. Read the statement below and choose the "
            "number of the region which correctly represents the statement: "
            "Indians who are Dramatists as well as Agriculturists."
        ),
        "question_hi": (
            "दिए गए चित्र में, लोगों के कुछ वर्गों का प्रतिनिधित्व "
            "करने वाली तीन प्रतिच्छेदी वृत्त हैं। विभिन्न अनुभागों को "
            "1 से 7 तक संख्याओं द्वारा चिह्नित किया गया है। नीचे दिए "
            "गए कथन को पढ़ें और उस क्षेत्र की संख्या चुनें जो कथन का "
            "सही प्रतिनिधित्व करती है: "
            "भारतीय जो नाटककार होने के साथ-साथ कृषक भी हैं।"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "2",
        "option_c": "3",
        "option_d": "4",
        "correct_answer": "C",
        # Region 3 = Indians ∩ Dramatists ∩ Agriculturists (triple intersection).
    },

    # ── Q68 ──────────────────────────────────────────────────────────────────
    # Three circles: Employed (left), Girls (right), Married (bottom).
    # "Girls who are Employed but NOT Married" = Girls ∩ Employed, not Married = 1.
    {
        "question_number": 68,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Study the diagram given below and identify the region "
            "representing girls who are employed but unmarried."
        ),
        "question_hi": (
            "नीचे दिए गए चित्र का अध्ययन करें और उन लड़कियों का "
            "प्रतिनिधित्व करने वाले क्षेत्र की पहचान करें जो "
            "कार्यरत हैं लेकिन अविवाहित हैं।"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "2",
        "option_c": "4",
        "option_d": "5",
        "correct_answer": "A",
        # Region 1 = Girls ∩ Employed, outside Married circle.
    },

    # ── Q69 ──────────────────────────────────────────────────────────────────
    # Venn: Educated (left circle), Employed (right circle), Rural (outer).
    # Numbers: 10, 22, 6, 14, 34.
    # "Rural uneducated people who are employed" = Employed ∩ Rural, not Educated = 6.
    {
        "question_number": 69,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "How many rural uneducated people are employed?"
        ),
        "question_hi": (
            "कितने ग्रामीण अशिक्षित लोग कार्यरत हैं?"
        ),
        "image_url": None,
        "option_a": "10",
        "option_b": "6",
        "option_c": "12",
        "option_d": "14",
        "correct_answer": "B",
        # Region 6 = Employed ∩ Rural, NOT Educated (uneducated rural employed).
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Venn Diagram Q65–Q69 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload venn_65.png … venn_69.png to Supabase bucket "
                "'question_image_Venn_Diagram', then run:\n"
                "  python update_venn_diagram_image_urls_batch9.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
