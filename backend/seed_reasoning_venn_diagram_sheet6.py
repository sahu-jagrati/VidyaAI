"""
seed_reasoning_venn_diagram_sheet6.py
=======================================
Seeds Reasoning → Venn Diagram  Q39–Q46.
(Q38 not provided — skipped.)

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_venn_diagram_image_urls_batch6.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q39 D  (Tree, Plant, House)
     Tree ⊂ Plant (a tree is a plant).
     House ∩ Plant = ∅; House ∩ Tree = ∅.
     Diagram: Plant (large circle) with Tree (small circle inside)
              + House (completely separate circle). → D.

Q40 C  (Sun, Moon, Molecule)
     Sun (star), Moon (natural satellite), Molecule (chemical particle)
     are three completely unrelated categories.
     None is a subset of another; no overlap.
     Diagram: three completely separate, non-overlapping circles. → C.

Q41 B  (A = Doctors, B = Pianists, C = Writers, D = Singers)
     From the given Venn diagram: Pianists (B) ⊂ Doctors (A);
     Writers (C) ⊂ Doctors (A); Singers (D) is separate from all.
     → All writers and pianists are doctors.
     Statement (b) is correct. → B.

Q42 B  (Elephants, Lions, Animals)
     Elephants ⊂ Animals; Lions ⊂ Animals; Elephants ∩ Lions = ∅.
     Diagram: Animals (large circle) with Elephants and Lions as two
              separate non-overlapping smaller circles inside. → B.

Q43 A  (Boys, Students, Athletes)
     Boys ∩ Students ≠ ∅; Boys ∩ Athletes ≠ ∅; Students ∩ Athletes ≠ ∅.
     None is a strict subset of another.
     Diagram: three partially overlapping / intersecting circles. → A.

Q44 B  (Keyboard, Function keys, Letter keys)
     Function keys ⊂ Keyboard; Letter keys ⊂ Keyboard.
     Function keys ∩ Letter keys = ∅ (different key types).
     Diagram: Keyboard (large circle) with Function keys and Letter keys
              as two separate non-overlapping smaller circles inside. → B.

Q45 A  (Herbivores, Tigers, Animals)
     Herbivores ⊂ Animals; Tigers ⊂ Animals.
     Tigers ∩ Herbivores = ∅ (tigers are carnivores).
     Diagram: Animals (large circle) with Herbivores and Tigers as two
              separate non-overlapping smaller circles inside. → A.

Q46 A  (Humans, Birds, Animals)
     Humans ⊂ Animals; Birds ⊂ Animals; Humans ∩ Birds = ∅.
     Diagram: Animals (large circle) with Humans and Birds as two
              separate non-overlapping smaller circles inside. → A.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Venn Diagram"

QUESTIONS = [

    # ── Q39 ──────────────────────────────────────────────────────────────────
    # Tree ⊂ Plant; House completely separate.
    # Diagram: Plant (large) with Tree inside + House separate.
    {
        "question_number": 39,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Identify the figure which best represents the relationship "
            "among Tree, Plant, and House."
        ),
        "question_hi": (
            "उस आकृति को पहचानें जो पेड़, पौधे और घर के बीच "
            "संबंध को सबसे अच्छा दर्शाती है।"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "D",
        # Plant (large circle) with Tree inside + House completely separate.
    },

    # ── Q40 ──────────────────────────────────────────────────────────────────
    # Sun, Moon, Molecule — completely unrelated categories.
    # Diagram: three completely separate, non-overlapping circles.
    {
        "question_number": 40,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which figure represents the relationship among "
            "Sun, Moon, Molecule?"
        ),
        "question_hi": (
            "कौन सी आकृति सूर्य, चंद्रमा, अणु के बीच संबंध को दर्शाती है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "C",
        # Three completely separate, non-overlapping circles.
    },

    # ── Q41 ──────────────────────────────────────────────────────────────────
    # Given Venn diagram: A = Doctors (outer), B = Pianists (inside A),
    # C = Writers (inside A), D = Singers (separate).
    # → All pianists and writers are doctors; singers separate.
    {
        "question_number": 41,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "A represents doctors, B represents pianists and C represents "
            "writers while D represents singers. "
            "Which of the statements is most appropriate?"
        ),
        "question_hi": (
            "A डॉक्टरों का प्रतिनिधित्व करता है, B पियानोवादकों का "
            "प्रतिनिधित्व करता है और C लेखकों का प्रतिनिधित्व करता है, "
            "जबकि D गायकों का प्रतिनिधित्व करता है। "
            "इनमें से कौन सा कथन सर्वाधिक उपयुक्त है?"
        ),
        "image_url": None,
        "option_a": "All singers are doctors. / सभी गायक डॉक्टर हैं।",
        "option_b": (
            "All writers and pianists are doctors. / "
            "सभी लेखक और पियानोवादक डॉक्टर हैं।"
        ),
        "option_c": "All pianists are singers. / सभी पियानोवादक गायक हैं।",
        "option_d": "None of these / इनमें से कोई नहीं",
        "correct_answer": "B",
        # B (Pianists) ⊂ A (Doctors); C (Writers) ⊂ A (Doctors); D separate.
        # → All writers and pianists are doctors.
    },

    # ── Q42 ──────────────────────────────────────────────────────────────────
    # Elephants ⊂ Animals; Lions ⊂ Animals; Elephants ∩ Lions = ∅.
    # Diagram: Animals (large) with Elephants & Lions (two separate inside).
    {
        "question_number": 42,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Identify the diagram that best represents the relationship "
            "among classes given below: Elephants, Lions and Animals."
        ),
        "question_hi": (
            "उस आरेख को पहचानें जो नीचे दिए गए वर्गों के बीच संबंध को "
            "सबसे अच्छा दर्शाता है: हाथी, शेर और जानवर।"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
        # Animals (large circle) with Elephants and Lions as two separate
        # non-overlapping smaller circles inside.
    },

    # ── Q43 ──────────────────────────────────────────────────────────────────
    # Boys ∩ Students ≠ ∅; Boys ∩ Athletes ≠ ∅; Students ∩ Athletes ≠ ∅.
    # None is a subset of another — three partially overlapping circles.
    {
        "question_number": 43,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which one of the following diagrams best depicts the relationship "
            "among Boys, Students and Athletes?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा आरेख लड़कों, छात्रों और "
            "एथलीटों के बीच संबंध को सबसे अच्छी तरह दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Three partially overlapping / intersecting circles.
    },

    # ── Q44 ──────────────────────────────────────────────────────────────────
    # Function keys ⊂ Keyboard; Letter keys ⊂ Keyboard; F∩L = ∅.
    # Diagram: Keyboard (large) with Function keys & Letter keys (two separate inside).
    {
        "question_number": 44,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "For the given set of elements: "
            "Keyboard, function keys, letter keys — which figure given below "
            "will best represent the relationship among these three elements?"
        ),
        "question_hi": (
            "तत्वों के दिए गए सेट के लिए: "
            "कीबोर्ड, फंक्शन कुंजियाँ, अक्षर कुंजियाँ — नीचे दिया गया "
            "कौन सा चित्र इन तीन तत्वों के बीच संबंध को सबसे अच्छा दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "B",
        # Keyboard (large circle) with Function keys and Letter keys as two
        # separate non-overlapping smaller circles inside.
    },

    # ── Q45 ──────────────────────────────────────────────────────────────────
    # Herbivores ⊂ Animals; Tigers ⊂ Animals; Herbivores ∩ Tigers = ∅.
    # Diagram: Animals (large) with Herbivores & Tigers (two separate inside).
    {
        "question_number": 45,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the following diagrams represents the correct "
            "relationship between Herbivores, Tigers and Animals?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा आरेख शाकाहारी, बाघ और "
            "जानवरों के बीच सही संबंध को दर्शाता है?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Animals (large circle) with Herbivores and Tigers as two separate
        # non-overlapping smaller circles inside.
    },

    # ── Q46 ──────────────────────────────────────────────────────────────────
    # Humans ⊂ Animals; Birds ⊂ Animals; Humans ∩ Birds = ∅.
    # Diagram: Animals (large) with Humans & Birds (two separate inside).
    {
        "question_number": 46,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the following Venn diagrams best represents relation "
            "between given classes: Humans, Birds, Animals?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सा वेन आरेख दिए गए वर्गों के बीच "
            "संबंध को सबसे अच्छा दर्शाता है: मनुष्य, पक्षी, जानवर?"
        ),
        "image_url": None,
        "option_a": "Figure (a) / चित्र (a)",
        "option_b": "Figure (b) / चित्र (b)",
        "option_c": "Figure (c) / चित्र (c)",
        "option_d": "Figure (d) / चित्र (d)",
        "correct_answer": "A",
        # Animals (large circle) with Humans and Birds as two separate
        # non-overlapping smaller circles inside.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Venn Diagram Q39–Q46 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload venn_39.png … venn_46.png to Supabase bucket "
                "'question_image_Venn_Diagram', then run:\n"
                "  python update_venn_diagram_image_urls_batch6.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
