"""
seed_reasoning_cube_cuboid_sheet2.py
========================================
Seeds Reasoning → Cube & Cuboid  Q8–Q11.

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_cube_cuboid_image_urls_batch2.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q8  A  (UPSC CSAT 2018)
     3 cm cube → 3³ = 27 unit cubes (1 cm side each).
     Exactly 2 painted faces = edge cubes (not corners):
       12 edges × (3-2) cubes per edge = 12. → A.

Q9  A  (UPSC CSAT 2017)
     4 cm cube → 4³ = 64 unit cubes. Outer surface fully painted.
     Cubes with NO painted face = interior cubes = (4-2)³ = 2³ = 8. → A.

Q10 B  (UPSC CSAT 2016)
     Small cube side = (1/4) × big cube side → n = 4 (cuts per axis).
     Total small cubes = 4³ = 64.
     Cubes with exactly 1 face painted = 6 faces × (4-2)² = 6 × 4 = 24. → B.

Q11 C  (UPSC CSAT 2015)
     Faces: V, I, B, G, Y, O. Clues:
       1) Y, O, B adjacent  2) I, G, Y adjacent
       3) B, G, Y adjacent  4) O, V, B adjacent
     From clues, {Y,O,B} can't be opposite each other → each pairs with {V,I,G}.
     Clue 4: O ≠ opposite V   → O is opposite I or G.
     Clue 4: V ≠ opposite B   → B is opposite I or G.
     Clue 3: B ≠ opposite G   → B is NOT opposite G → B is opposite I.
     Then O is opposite G (only one left from {I,G} after B takes I).
     Then Y is opposite V.
     Opposite pairs: Y↔V, O↔G, B↔I.
     Face opposite to O = G. → C.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"

QUESTIONS = [

    # ── Q8 ───────────────────────────────────────────────────────────────────
    # 3 cm cube painted all faces → 27 unit cubes.
    # Exactly 2 painted faces = edge cubes = 12 × (3-2) = 12.
    # Source: UPSC CSAT 2018
    {
        "question_number": 8,
        "difficulty": "medium",
        "source_pdf": "UPSC_CSAT_2018",
        "question_en": (
            "A solid cube of 3 cm side, painted on all its faces, is cut up "
            "into small cubes of 1 cm side. How many of the small cubes will "
            "have exactly two painted faces?"
        ),
        "question_hi": (
            "3 cm भुजा वाले एक ठोस गहकन के सभी फलकों को रंग कर उसे 1 cm "
            "भुजा वाले छोटे घनों में काटा गया है। छोटे घनों में से कितने "
            "घनों के केवल दो फलक रंगे हुए होंगे?"
        ),
        "image_url": None,
        "option_a": "12",
        "option_b": "8",
        "option_c": "6",
        "option_d": "4",
        "correct_answer": "A",
        # Edge cubes (exactly 2 painted faces) = 12 edges × (3-2) = 12.
    },

    # ── Q9 ───────────────────────────────────────────────────────────────────
    # 4×4×4 cm cube painted red all over → 64 unit cubes.
    # No-paint cubes = interior = (4-2)³ = 8.
    # Source: UPSC CSAT 2017
    {
        "question_number": 9,
        "difficulty": "medium",
        "source_pdf": "UPSC_CSAT_2017",
        "question_en": (
            "The outer surface of a 4 cm × 4 cm × 4 cm cube is painted "
            "completely in red. It is sliced parallel to the faces to yield "
            "sixty four 1 cm × 1 cm × 1 cm small cubes. How many small cubes "
            "do not have faces painted?"
        ),
        "question_hi": (
            "4 cm × 4 cm × 4 cm के एक घन के बाह्य पृष्ठ को पूरी तरह लाल रंग "
            "में रंगा गया है। इसे फलकों के समान्तर 1 cm × 1 cm × 1 cm के "
            "चौंसठ छोटे घनों में काटा गया है। कितने छोटे घनों की फलकें "
            "रंगी हुई नहीं होंगी?"
        ),
        "image_url": None,
        "option_a": "8",
        "option_b": "16",
        "option_c": "24",
        "option_d": "36",
        "correct_answer": "A",
        # Interior (no paint) = (4-2)³ = 2³ = 8.
    },

    # ── Q10 ──────────────────────────────────────────────────────────────────
    # Small cube side = 1/4 of big cube → n = 4 cuts per axis.
    # Exactly 1 painted face = 6 × (4-2)² = 6 × 4 = 24.
    # Source: UPSC CSAT 2016
    {
        "question_number": 10,
        "difficulty": "medium",
        "source_pdf": "UPSC_CSAT_2016",
        "question_en": (
            "A cube has all its faces painted with different colours. It is cut "
            "into smaller cubes of equal sizes such that the size of the small "
            "cube is one-fourth the big cube. The number of small cubes with "
            "only one of the sides painted is:"
        ),
        "question_hi": (
            "किसी घन के सभी फलक विभिन्न रंगों से रंगे गए हैं। उसे समान आमाप "
            "के छोटे-छोटे घनों में इस प्रकार काट गया है कि छोटे घन की भुजा "
            "बड़े घन की एक चौथाई हो। केवल एक ही रंगे फलक वाले छोटे घनों की "
            "संख्या कितनी होगी?"
        ),
        "image_url": None,
        "option_a": "32",
        "option_b": "24",
        "option_c": "16",
        "option_d": "8",
        "correct_answer": "B",
        # n = 4 (small side = big/4). Face-only cubes = 6 × (4-2)² = 6×4 = 24.
    },

    # ── Q11 ──────────────────────────────────────────────────────────────────
    # 6 faces: V,I,B,G,Y,O. Four adjacency clues → find face opposite to O.
    # Opposite pairs: Y↔V, O↔G, B↔I.  Opposite of O = G.
    # Source: UPSC CSAT 2015
    {
        "question_number": 11,
        "difficulty": "hard",
        "source_pdf": "UPSC_CSAT_2015",
        "question_en": (
            "Each of the six different faces of a cube has been coated with a "
            "different colour i.e., V, I, B, G, Y and O. Following information "
            "is given:\n"
            "1. Colours Y, O and B are on adjacent faces.\n"
            "2. Colours I, G and Y are on adjacent faces.\n"
            "3. Colours B, G and Y are on adjacent faces.\n"
            "4. Colours O, V and B are on adjacent faces.\n"
            "Which is the colour of the face opposite to the face coloured "
            "with O?"
        ),
        "question_hi": (
            "एक घन के छः विभिन्न फलकों में से प्रत्येक को भिन्न रंग अर्थात् "
            "V, I, B, G, Y और O से रंगा गया है।\n"
            "निम्नलिखित सूचना दी गई है:\n"
            "1. रंग Y, O और B संलग्न फलकों पर हैं।\n"
            "2. रंग I, G और Y संलग्न फलकों पर हैं।\n"
            "3. रंग B, G और Y संलग्न फलकों पर हैं।\n"
            "4. रंग O, V और B संलग्न फलकों पर हैं।\n"
            "O रंग वाले फलक के विपरीत फलक का रंग कौन सा है?"
        ),
        "image_url": None,
        "option_a": "B",
        "option_b": "V",
        "option_c": "G",
        "option_d": "I",
        "correct_answer": "C",
        # Clue 4: O≠opp V → O opp I or G. Clue 3: B≠opp G → B opp I.
        # ∴ O opp G (only remaining), Y opp V. Opposite of O = G.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Cube & Cuboid Q8–Q11 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload cube_8.png … cube_11.png to the Supabase Cube & Cuboid "
                "bucket, then run:\n"
                "  python update_cube_cuboid_image_urls_batch2.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
