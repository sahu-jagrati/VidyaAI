"""
seed_reasoning_venn_diagram_sheet12.py
========================================
Seeds Reasoning → Venn Diagram  Q85–Q90.

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_venn_diagram_image_urls_batch12.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q85 B  (Kannada=11, Tamil=20, Telugu=11; 2 speak exactly two languages,
        1 speaks all three)
     Using inclusion-exclusion:
       |A∪B∪C| = |A|+|B|+|C| - Σ|pairwise| + |all three|
     "Two persons speak two languages" → Σ|pairwise intersections| = 2
     (the sum of all two-language overlaps including the triple is 2).
     Total = 11+20+11 − 2 + 1 = 41. → B.

Q86 C  (Triangle=Graduates, Rectangle=Married Persons, Circle=Women)
     Numbers in diagram: 87(Graduates only), 47(Married only),
       43(Women only), 21(Grad∩Married excl), 37(Women∩Married excl),
       32(Women∩Grad excl, NOT Married), 14(all three).
     "Women who are Graduates but NOT Married" =
     Circle ∩ Triangle, outside Rectangle = 32. → C.

Q87 B  (Circle, Triangle, Rectangle with numbers 1–6)
     "Number present ONLY in circle AND triangle" =
     the region inside Circle AND Triangle but outside Rectangle = 3. → B.

Q88 C  (Tamil=180, Telugu=35, English=27; overlap numbers 12, 9, 13, 19)
     "People who speak Tamil AND Telugu" =
     Tamil∩Telugu region (exclusive) + all three = 12 + 9 = 21. → C.

Q89 A  (Circle=business, Triangle=educated, Rectangle=income>Rs.10,000)
     "Educated business people with income more than Rs.10,000" =
     Circle ∩ Triangle ∩ Rectangle (all three) = region 7. → A.

Q90 B  (Students/Teachers/Parents Venn: given overlapping %s)
     Given: S∩P=10%, S∩T∩P=10%, T∩P=15%, S∩T=35%.
     Exclusive-region percentages: Only Students=40%, Only Teachers=65%,
     Only Parents=45%. → B (40, 65, 45).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Venn Diagram"

QUESTIONS = [

    # ── Q85 ──────────────────────────────────────────────────────────────────
    # Kannada=11, Tamil=20, Telugu=11. 2 speak two langs, 1 speaks all 3.
    # Total = 11+20+11 − 2 + 1 = 41.
    {
        "question_number": 85,
        "difficulty": "hard",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In a group of persons, 11 persons speak Kannada, 20 persons speak "
            "Tamil and 11 persons speak Telugu. In that group, if two persons "
            "speak two languages and one person speaks all the languages, then "
            "how many persons are there in the group?"
        ),
        "question_hi": (
            "व्यक्तियों के एक समूह में, 11 व्यक्ति कन्नड़ बोलते हैं, 20 "
            "व्यक्ति तमिल बोलते हैं और 11 व्यक्ति तेलुगू बोलते हैं। उस "
            "समूह में, यदि दो व्यक्ति दो भाषाएं बोलते हैं और एक व्यक्ति "
            "सभी भाषाएं बोलता है, तो समूह में कितने व्यक्ति हैं?"
        ),
        "image_url": None,
        "option_a": "40",
        "option_b": "41",
        "option_c": "42",
        "option_d": "43",
        "correct_answer": "B",
        # 11+20+11 − (pairwise sum=2) + 1 = 41.
    },

    # ── Q86 ──────────────────────────────────────────────────────────────────
    # Triangle=Graduates, Rectangle=Married, Circle=Women.
    # "Women Graduates NOT Married" = Circle∩Triangle, outside Rectangle = 32.
    {
        "question_number": 86,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the given figure, the triangle represents Graduates, rectangle "
            "represents Married Persons and circle represents Women. What is "
            "the number of those Women who are Graduates but not Married?"
        ),
        "question_hi": (
            "दिए गए चित्र में, त्रिभुज स्नातकों को दर्शाता है, आयत "
            "विवाहित व्यक्तियों को दर्शाती है और वृत्त महिलाओं को "
            "दर्शाता है। उन महिलाओं की संख्या क्या है जो स्नातक हैं "
            "लेकिन विवाहित नहीं हैं?"
        ),
        "image_url": None,
        "option_a": "21",
        "option_b": "14",
        "option_c": "32",
        "option_d": "37",
        "correct_answer": "C",
        # Region = Women∩Graduates, outside Married = 32.
    },

    # ── Q87 ──────────────────────────────────────────────────────────────────
    # Diagram: overlapping circle, triangle, rectangle with numbers 1–6.
    # "Number only in circle AND triangle" = Circle∩Triangle, not Rectangle = 3.
    {
        "question_number": 87,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the following number is present only in the circle "
            "and the triangle?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सी संख्या केवल वृत्त और त्रिभुज "
            "में मौजूद है?"
        ),
        "image_url": None,
        "option_a": "5",
        "option_b": "3",
        "option_c": "4",
        "option_d": "6",
        "correct_answer": "B",
        # Region 3 = Circle ∩ Triangle, outside Rectangle.
    },

    # ── Q88 ──────────────────────────────────────────────────────────────────
    # Tamil=180, Telugu=35, English=27. Overlaps: T∩Te=12, all three=9,
    # Te∩E=13, T∩E=19.
    # "Speak Tamil AND Telugu" = 12 + 9 = 21.
    {
        "question_number": 88,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Find out the number of all those people who can speak "
            "Tamil and Telugu."
        ),
        "question_hi": (
            "उन सभी लोगों की संख्या ज्ञात कीजिए जो तमिल और "
            "तेलुगू बोल सकते हैं।"
        ),
        "image_url": None,
        "option_a": "3",
        "option_b": "59",
        "option_c": "21",
        "option_d": "112",
        "correct_answer": "C",
        # Tamil∩Telugu (exclusive) + all three = 12 + 9 = 21.
    },

    # ── Q89 ──────────────────────────────────────────────────────────────────
    # Circle=business people, Triangle=educated, Rectangle=income>Rs.10,000.
    # "Educated business people with income>10k" = all three (triple) = 7.
    {
        "question_number": 89,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the figure, circle represents business people, triangle the "
            "educated persons and the rectangle stands for persons with income "
            "more than Rs.10,000 per month. The number standing for educated "
            "business people with income more than Rs.10,000 per month is:"
        ),
        "question_hi": (
            "चित्र में, वृत्त व्यावसायिक लोगों को दर्शाता है, त्रिभुज "
            "शिक्षित व्यक्तियों को दर्शाता है और आयत 10,000 रुपये प्रति "
            "माह से अधिक आय वाले व्यक्तियों को दर्शाता है। 10,000 रुपये "
            "से अधिक आय वाले शिक्षित व्यावसायी लोगों की संख्या है:"
        ),
        "image_url": None,
        "option_a": "7",
        "option_b": "10",
        "option_c": "3",
        "option_d": "4",
        "correct_answer": "A",
        # Region 7 = Circle (business) ∩ Triangle (educated) ∩ Rectangle (income>10k).
    },

    # ── Q90 ──────────────────────────────────────────────────────────────────
    # Students / Teachers / Parents Venn.
    # Given: S∩P=10%, S∩T∩P=10%, T∩P=15%, S∩T=35%.
    # Exclusive regions: Only Students=40%, Only Teachers=65%, Only Parents=45%.
    {
        "question_number": 90,
        "difficulty": "hard",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the given figure 10% are students and parents, and the 10% are "
            "students, teachers and parents. 15% are teachers and parents. 35% "
            "are students and teachers. How many percentage are only teachers, "
            "parents and students?"
        ),
        "question_hi": (
            "दिए गए आंकड़े में 10% छात्र और माता-पिता हैं, और 10% छात्र, "
            "शिक्षक और माता-पिता हैं। 15% शिक्षक और माता-पिता हैं। 35% "
            "छात्र और शिक्षक हैं। केवल शिक्षक, अभिभावक और छात्र कितने "
            "प्रतिशत हैं?"
        ),
        "image_url": None,
        "option_a": "45, 40, 65",
        "option_b": "40, 65, 45",
        "option_c": "40, 45, 65",
        "option_d": "65, 40, 45",
        "correct_answer": "B",
        # Only Students=40%, Only Teachers=65%, Only Parents=45%.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Venn Diagram Q85–Q90 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload venn_85.png … venn_90.png to Supabase bucket "
                "'question_image_Venn_Diagram', then run:\n"
                "  python update_venn_diagram_image_urls_batch12.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
