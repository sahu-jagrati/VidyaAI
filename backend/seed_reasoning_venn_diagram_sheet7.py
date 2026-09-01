"""
seed_reasoning_venn_diagram_sheet7.py
=======================================
Seeds Reasoning → Venn Diagram  Q47–Q55.

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_venn_diagram_image_urls_batch7.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q47 D  (Fruits, Apples, Oranges)
     Apples ⊂ Fruits; Oranges ⊂ Fruits; Apples ∩ Oranges = ∅.
     Diagram: Fruits (large circle) with Apples and Oranges as two
              separate non-overlapping smaller circles inside. → D.

Q48 D  (Atmosphere, Oxygen, Carbon dioxide)
     Oxygen ⊂ Atmosphere; CO₂ ⊂ Atmosphere; O₂ ∩ CO₂ = ∅.
     Diagram: Atmosphere (large circle) with Oxygen and Carbon dioxide
              as two separate non-overlapping smaller circles inside. → D.

Q49 B  (Class teacher, Girls and Boys of Standard VIII)
     In the context of Standard VIII:
       Girls (students) ∩ Boys (students) = ∅.
       Class teacher ∩ Girls = ∅; Class teacher ∩ Boys = ∅
       (the teacher is not a student).
     Diagram: three completely separate, non-overlapping circles. → B.

Q50 A  (Human Society, Youth Club, Political Party, Youths)
     Youths ⊂ Human Society.
     Youth Club ⊂ Youths (youth clubs are made of youths).
     Political Party ⊂ Human Society; Political Party ∩ Youths ≠ ∅
     (some political party members are youths; some are not).
     Diagram: Human Society (outermost) → Youths (inner circle)
              → Youth Club (innermost circle inside Youths) +
              Political Party (circle inside Human Society that
              partially overlaps with Youths). → A.

Q51 C  (Region representing rural literate in given Venn diagram)
     Venn diagram has three overlapping ovals: Rural (left),
     Women (top-right), Literate (bottom-right). Numbered regions:
       1 = Rural only
       2 = Rural ∩ Women (not Literate)
       3 = Women only
       4 = Rural ∩ Literate (not Women)     ← rural literate, not women
       5 = Rural ∩ Women ∩ Literate          ← rural, literate, also women
       6 = Women ∩ Literate (not Rural)
       7 = Literate only
     Rural literate = Rural ∩ Literate = regions {4, 5}. → C (5, 4).

Q52 A  (Pollution control board: Engineers = circle, Legal = square,
        Environmentalists = triangle)
     In the given figure the triangle (Environmentalists) is the
     largest shape, covering the greatest area and encompassing
     parts of both the circle and the square.
     → Environmentalists are most represented. → A.

Q53 D  (Venn diagram: Indian / Leader / Singer — find region that
        is Leader but NOT Singer and NOT Indian)
     Three overlapping circles labeled Indian, Leader, Singer.
     Seven regions: a (Indian only), b (Indian∩Leader), c (all three),
       d (Indian∩Singer), e (Leader∩Singer), f (Leader only),
       g (Singer only).
     "Leader but not Singer, not Indian" = region f. → D.

Q54 D  (Same diagram — find region that is Indian AND Singer but NOT Leader)
     "Indian AND Singer but NOT Leader" = region d
     (overlap of Indian and Singer circles, excluding Leader). → D.

Q55 B  (Same diagram — find region that is only Singer, NOT Indian/Leader)
     "Only Singer, not Indian, not Leader" = region g
     (Singer circle portion that doesn't overlap with Indian or Leader). → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Venn Diagram"

QUESTIONS = [

    # ── Q47 ──────────────────────────────────────────────────────────────────
    # Apples ⊂ Fruits; Oranges ⊂ Fruits; Apples ∩ Oranges = ∅.
    # Diagram: Fruits (large) with Apples & Oranges (two separate inside).
    {
        "question_number": 47,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the following Venn diagrams best represents relation "
            "between given classes? Fruits, Apples, Oranges."
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा वेन आरेख दिए गए वर्गों के बीच "
            "संबंध को सबसे अच्छा दर्शाता है? फल, सेब, संतरे।"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "D",
        # Fruits (large circle) with Apples and Oranges as two separate
        # non-overlapping smaller circles inside.
    },

    # ── Q48 ──────────────────────────────────────────────────────────────────
    # Oxygen ⊂ Atmosphere; CO₂ ⊂ Atmosphere; O₂ ∩ CO₂ = ∅.
    # Diagram: Atmosphere (large) with O₂ & CO₂ (two separate inside).
    {
        "question_number": 48,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Identify the diagram that best represents the relationship among "
            "Atmosphere, Oxygen and Carbon dioxide the classes given below."
        ),
        "question_hi": (
            "उस आरेख को पहचानें जो नीचे दिए गए वर्गों में वायुमंडल, "
            "ऑक्सीजन और कार्बन डाइऑक्साइड के बीच संबंध को "
            "सबसे अच्छा दर्शाता है।"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "D",
        # Atmosphere (large circle) with Oxygen and Carbon dioxide as two
        # separate non-overlapping smaller circles inside.
    },

    # ── Q49 ──────────────────────────────────────────────────────────────────
    # Teacher ∩ Girls = ∅; Teacher ∩ Boys = ∅; Girls ∩ Boys = ∅.
    # Diagram: three completely separate circles.
    {
        "question_number": 49,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which one of the following diagrams represents the correct "
            "relationship with the Class teacher, Girls and Boys of standard VIII?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा आरेख आठवीं कक्षा के कक्षा "
            "शिक्षक, लड़कियों और लड़कों के साथ सही संबंध को दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
        # Three completely separate, non-overlapping circles for
        # Class teacher, Girls, and Boys.
    },

    # ── Q50 ──────────────────────────────────────────────────────────────────
    # Youth Club ⊂ Youths ⊂ Human Society; Political Party ⊂ Human Society,
    # partially overlapping with Youths.
    {
        "question_number": 50,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which one of the following diagrams best depicts the relationship "
            "among Human Society, Youth Club, Political Party and Youths?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा चित्र मानव समाज युवा क्लब, "
            "राजनीतिक दल और युवाओं के बीच संबंध को सबसे अच्छी "
            "तरह दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Human Society (outermost) containing Youths, Youths containing
        # Youth Club, and Political Party partially overlapping Youths,
        # all within Human Society.
    },

    # ── Q51 ──────────────────────────────────────────────────────────────────
    # Venn diagram: Rural (left), Women (top-right), Literate (bottom-right).
    # Regions 1-7 labeled. Rural literate = regions 4 (Rural∩Literate, not Women)
    # and 5 (Rural∩Women∩Literate). Answer = 5, 4.
    {
        "question_number": 51,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Study the diagram below and identify the region representing "
            "rural literate."
        ),
        "question_hi": (
            "नीचे दिए गए चित्र का अध्ययन करें और ग्रामीण साक्षर "
            "क्षेत्र का प्रतिनिधित्व करने वाले क्षेत्र की पहचान करें।"
        ),
        "image_url": None,
        "option_a": "5, 6",
        "option_b": "4, 5, 2",
        "option_c": "5, 4",
        "option_d": "4, 5, 7",
        "correct_answer": "C",
        # Rural ∩ Literate = regions 4 (not Women) and 5 (all three).
    },

    # ── Q52 ──────────────────────────────────────────────────────────────────
    # Engineers = circle, Legal experts = square, Environmentalists = triangle.
    # Triangle (Environmentalists) is the largest shape in the diagram.
    {
        "question_number": 52,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In an organisation of pollution control board, engineers are "
            "represented by a circle, legal experts by a square, and "
            "environmentalists by a triangle. Who is most represented in "
            "the board as shown in the following figure?"
        ),
        "question_hi": (
            "प्रदूषण नियंत्रण बोर्ड के एक संगठन में, इंजीनियरों को "
            "एक वृत्त द्वारा, कानूनी विशेषज्ञों को एक वर्ग द्वारा, और "
            "पर्यावरणविदों को एक त्रिकोण द्वारा दर्शाया जाता है। "
            "जैसा कि निम्नलिखित चित्र में दिखाया गया है, बोर्ड में "
            "सबसे अधिक प्रतिनिधित्व किसका है?"
        ),
        "image_url": None,
        "option_a": "Environmentalists / पर्यावरणविद",
        "option_b": "Legal experts / कानूनी विशेषज्ञ",
        "option_c": (
            "Engineers with legal background / "
            "कानूनी पृष्ठभूमि वाले इंजीनियर"
        ),
        "option_d": (
            "Environmentalists with engineering background / "
            "इंजीनियरिंग पृष्ठभूमि वाले पर्यावरणविद"
        ),
        "correct_answer": "A",
        # Triangle (Environmentalists) has the largest area in the figure.
    },

    # ── Q53 ──────────────────────────────────────────────────────────────────
    # Venn diagram: Indian (left), Leader (right), Singer (bottom).
    # Regions: a=Indian only, b=Indian∩Leader, c=all three,
    #          d=Indian∩Singer, e=Leader∩Singer, f=Leader only, g=Singer only.
    # "Leader but NOT singer, NOT Indian" = region f.
    {
        "question_number": 53,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Study the figure carefully and answer the questions. "
            "Which symbol indicates leader but not a singer, or an Indian?"
        ),
        "question_hi": (
            "चित्र का ध्यानपूर्वक अध्ययन करें और प्रश्नों के उत्तर दें। "
            "कौन सा प्रतीक नेता को दर्शाता है लेकिन गायक या "
            "भारतीय को नहीं?"
        ),
        "image_url": None,
        "option_a": "g",
        "option_b": "c",
        "option_c": "b",
        "option_d": "f",
        "correct_answer": "D",
        # Region f = Leader only (not Indian, not Singer).
    },

    # ── Q54 ──────────────────────────────────────────────────────────────────
    # Same Venn diagram (Indian / Leader / Singer).
    # "Indian AND Singer but NOT Leader" = region d
    # (Indian∩Singer overlap, excluding Leader).
    {
        "question_number": 54,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Study the figure carefully and answer the questions. "
            "Which symbol indicates Indian, a singer but not a leader?"
        ),
        "question_hi": (
            "चित्र का ध्यानपूर्वक अध्ययन करें और प्रश्नों के उत्तर दें। "
            "कौन सा प्रतीक भारतीय को दर्शाता है, एक गायक को "
            "लेकिन एक नेता को नहीं?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "f",
        "option_d": "d",
        "correct_answer": "D",
        # Region d = Indian ∩ Singer, excluding Leader.
    },

    # ── Q55 ──────────────────────────────────────────────────────────────────
    # Same Venn diagram (Indian / Leader / Singer).
    # "Only Singer, NOT Indian, NOT Leader" = region g.
    {
        "question_number": 55,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Study the figure carefully and answer the questions. "
            "Which symbol indicates only singer, but not an Indian or a leader?"
        ),
        "question_hi": (
            "चित्र का ध्यानपूर्वक अध्ययन करें और प्रश्नों के उत्तर दें। "
            "कौन सा प्रतीक केवल गायक को दर्शाता है, भारतीय या "
            "नेता को नहीं?"
        ),
        "image_url": None,
        "option_a": "b",
        "option_b": "g",
        "option_c": "f",
        "option_d": "d",
        "correct_answer": "B",
        # Region g = Singer only (not Indian, not Leader).
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Venn Diagram Q47–Q55 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload venn_47.png … venn_55.png to Supabase bucket "
                "'question_image_Venn_Diagram', then run:\n"
                "  python update_venn_diagram_image_urls_batch7.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
