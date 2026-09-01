"""
seed_reasoning_venn_diagram_sheet14.py
========================================
Seeds Reasoning → Venn Diagram  Q96–Q100.

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_venn_diagram_image_urls_batch14.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q96 D  (Three-subject Venn; 500 students)
     Diagram numbers (exclusive regions):
       47(sub1 only), 12(sub1∩sub2 excl), 42(sub2 only), 13(sub1∩sub3 excl),
       11(all three = center), 15(sub2∩sub3 excl), 50(sub3 only).
     "Distinction in ALL subjects" = center = 11.
     Percentage = (11 / 500) × 100 = 2.2%. → D.

Q97 A  (Players circle / Teachers circle / Singers circle)
     Diagram numbers:
       12(Players only), 5(Players∩Teachers excl), 10(Teachers only),
       17(Players∩Singers excl), 9(Teachers∩Singers excl), 28(Singers only).
     "Teachers who are neither Players nor Singers" =
     Teachers-only region = 10. → A.

Q98 D  (Physics circle / Chemistry circle / Mathematics circle;
        regions labeled R, T, A, S, U, P, C)
     "Students who study both Physics AND Chemistry but NOT Mathematics" =
     Physics ∩ Chemistry, outside Mathematics = region T. → D.

Q99 B  (Triangle=Healthy, Square=Old, Circle=Men; regions numbered 1–7)
     Region mapping:
       1(Triangle only — healthy not old not men),
       2(Triangle∩Circle excl — healthy∩men, not old),
       7(Circle only — men only, not healthy not old),
       4(Triangle∩Square excl — healthy∩old, not men),
       3(triple center — healthy∩old∩men),
       5(Circle∩Square excl — men∩old, not healthy),
       6(Square only — old only).
     "Men who are healthy but NOT old" =
     Circle ∩ Triangle, outside Square = region 2. → B.

Q100 D (Circle=Urban People, outer Rectangle=Civil Staff,
        Square=Male, Triangle=Educated; numbers 3,10,7,12,6,8,9,11,5)
     "Educated males but NOT urban" =
     Triangle (Educated) ∩ Square (Male), outside Circle (Urban) = 9. → D.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Venn Diagram"

QUESTIONS = [

    # ── Q96 ──────────────────────────────────────────────────────────────────
    # 3-subject Venn; 500 students.
    # Diagram: 47,12,42,13,11,15,50. Center = 11.
    # Percentage with distinction in ALL = 11/500 × 100 = 2.2%.
    {
        "question_number": 96,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "The diagram given below shows number of students who got "
            "distinction in three subjects out of 500 students. What is the "
            "percentage of students who got distinction in all subjects?"
        ),
        "question_hi": (
            "नीचे दिया गया चित्र 500 छात्रों में से तीन विषयों में "
            "विशिष्टता प्राप्त करने वाले छात्रों की संख्या दर्शाता है। "
            "सभी विषयों में विशिष्टता प्राप्त करने वाले छात्रों का "
            "प्रतिशत क्या है?"
        ),
        "image_url": None,
        "option_a": "10.2",
        "option_b": "8",
        "option_c": "10",
        "option_d": "2.2",
        "correct_answer": "D",
        # Center (all three subjects) = 11 students.
        # Percentage = (11 / 500) × 100 = 2.2%.
    },

    # ── Q97 ──────────────────────────────────────────────────────────────────
    # Players circle, Teachers circle, Singers circle.
    # Numbers: 12(Players only), 5(P∩T excl), 10(Teachers only),
    #           17(P∩S excl), 9(T∩S excl), 28(Singers only).
    # "Teachers neither Players nor Singers" = Teachers only = 10.
    {
        "question_number": 97,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "How many teachers are neither players nor singers?"
        ),
        "question_hi": (
            "कितने शिक्षक न तो खिलाड़ी हैं और न ही गायक हैं?"
        ),
        "image_url": None,
        "option_a": "10",
        "option_b": "2",
        "option_c": "4",
        "option_d": "5",
        "correct_answer": "A",
        # Teachers-only region (outside Players and Singers circles) = 10.
    },

    # ── Q98 ──────────────────────────────────────────────────────────────────
    # Physics / Chemistry / Mathematics circles.
    # Regions labeled: R(Physics only), T(Phys∩Chem excl), A(Chem only),
    #   S(Phys∩Math excl), U(all three), P(Chem∩Math excl), C(Math only).
    # "Both Physics AND Chemistry but NOT Mathematics" = region T.
    {
        "question_number": 98,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "The diagram below represents the students who study Physics, "
            "Chemistry and Mathematics. Study the diagram and identify the "
            "region which represents students who study both Physics and "
            "Chemistry but not Mathematics?"
        ),
        "question_hi": (
            "नीचे दिया गया चित्र उन छात्रों को दर्शाता है जो भौतिकी, "
            "रसायन विज्ञान और गणित का अध्ययन करते हैं। आरेख का अध्ययन "
            "करें और उस क्षेत्र की पहचान करें जो उन छात्रों को दर्शाता है "
            "जो भौतिकी और रसायन विज्ञान दोनों पढ़ते हैं लेकिन गणित नहीं?"
        ),
        "image_url": None,
        "option_a": "T + S + U + P",
        "option_b": "C",
        "option_c": "R + T + A + U + P + S",
        "option_d": "T",
        "correct_answer": "D",
        # Region T = Physics ∩ Chemistry, strictly outside Mathematics circle.
    },

    # ── Q99 ──────────────────────────────────────────────────────────────────
    # Triangle = Healthy, Square = Old, Circle = Men. Regions 1–7.
    # "Men who are healthy but NOT old" =
    # Circle ∩ Triangle, outside Square = region 2.
    {
        "question_number": 99,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the given figure, triangle represents the healthy, square "
            "represents the old, and circle represents the men. Find out the "
            "area of the figure which represents the 'men who are healthy "
            "but not old'."
        ),
        "question_hi": (
            "दिए गए चित्र में, त्रिभुज स्वस्थ को दर्शाता है, वर्ग बूढ़े को "
            "दर्शाता है, और वृत्त पुरुषों को दर्शाता है। इस आकृति का "
            "क्षेत्रफल ज्ञात कीजिए जो 'उन पुरुषों को दर्शाता है जो "
            "स्वस्थ हैं लेकिन बूढ़े नहीं हैं'।"
        ),
        "image_url": None,
        "option_a": "1",
        "option_b": "2",
        "option_c": "3",
        "option_d": "7",
        "correct_answer": "B",
        # Region 2 = Circle (Men) ∩ Triangle (Healthy), outside Square (Old).
    },

    # ── Q100 ─────────────────────────────────────────────────────────────────
    # Circle = Urban People, outer Rectangle = Civil Staff,
    # Square = Male, Triangle = Educated.
    # Numbers: 3,10,7,12,6,8,9,11,5.
    # "Educated males NOT in urban area" =
    # Triangle ∩ Square, outside Circle = region 9.
    {
        "question_number": 100,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Who are educated males but who do not live in urban area?"
        ),
        "question_hi": (
            "वे कौन से शिक्षित पुरुष हैं जो शहरी क्षेत्र में नहीं रहते हैं?"
        ),
        "image_url": None,
        "option_a": "4",
        "option_b": "11",
        "option_c": "5",
        "option_d": "9",
        "correct_answer": "D",
        # Region 9 = Triangle (Educated) ∩ Square (Male), outside Circle (Urban People).
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Venn Diagram Q96–Q100 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload venn_96.png … venn_100.png to Supabase bucket "
                "'question_image_Venn_Diagram', then run:\n"
                "  python update_venn_diagram_image_urls_batch14.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
