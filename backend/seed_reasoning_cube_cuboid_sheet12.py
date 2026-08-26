"""
seed_reasoning_cube_cuboid_sheet12.py
======================================
Seeds Reasoning → Cube & Cuboid  book Q14–Q18 (Piyush Varshney source).
Stored as question_numbers 65–69.

Answer key
──────────────────────────────────────────────────────────────────────
Q65 (book Q14)  B (64)  — 4×4×4 cm cube → 1 cm cuts = 4×4×4 = 64 small cubes.
Q66 (book Q15)  D (8)   — same cube; 3 surfaces coloured = corner cubes = 8.
Q67 (book Q16)  C (8)   — same cube; colourless = interior = (4−2)³ = 2³ = 8.
Q68 (book Q17)  A (32)  — same cube; at least 2 surfaces = edge(12×2=24) +
                          corner(8) = 32.
Q69 (book Q18)  C (16)  — Cuboid 4×3×3; Yellow=4×3 opp. pair, Red=4×3 opp.
                          pair, Green=3×3 opp. pair; cut into 1 cm cubes;
                          only 2 faces painted (edge cubes) =
                          4×(4−2) + 4×(3−2) + 4×(3−2) = 8+4+4 = 16.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"
SOURCE  = "Piyush_Varshney_Cube_Cuboid"

# ── Shared preamble for Q65–Q68 ───────────────────────────────────────────────
# 4×4×4 cm cube, all surfaces yellow, cut into 1 cm small cubes → 64 cubes.
PRE_4 = (
    "A cube of 4×4×4 cm. side colored with yellow. After that it is cut into "
    "1 cm small cubes. Then answer the following questions: "
)
PRE_4_HI = (
    "एक 4 × 4 × 4 सेमी का घन पीले रंग से रंगा है। इसके बाद 1 सेमी भुजा वाले "
    "छोटे घनों में काटा जाता है। फिर निम्नलिखित प्रश्न का उत्तर दें: "
)

QUESTIONS = [

    # ── Q65 (book Q14) ──────────────────────────────────────────────────────
    # Total small cubes = 4³ = 64.
    {
        "question_number": 65,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_4}"
            "How many total number of small cubes are there?"
        ),
        "question_hi": (
            f"{PRE_4_HI}"
            "छोटे घनों की कुल संख्या कितनी है?"
        ),
        "image_url": None,
        "option_a": "16",
        "option_b": "64",
        "option_c": "8",
        "option_d": "27",
        "correct_answer": "B",   # 64 = 4³
    },

    # ── Q66 (book Q15) ──────────────────────────────────────────────────────
    # Three surfaces coloured = corner cubes = 8.
    {
        "question_number": 66,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_4}"
            "The total number of small cubes of which three surfaces are coloured?"
        ),
        "question_hi": (
            f"{PRE_4_HI}"
            "छोटे घनों की कुल संख्या जिनमें तीन सतह रंगीन हैं?"
        ),
        "image_url": None,
        "option_a": "16",
        "option_b": "25",
        "option_c": "64",
        "option_d": "8",
        "correct_answer": "D",   # 8 corner cubes (always 8 regardless of n)
    },

    # ── Q67 (book Q16) ──────────────────────────────────────────────────────
    # Colourless (0 painted faces) = interior cubes = (n−2)³ = (4−2)³ = 2³ = 8.
    {
        "question_number": 67,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_4}"
            "The number of colourless cubes are?"
        ),
        "question_hi": (
            f"{PRE_4_HI}"
            "रंगहीन घनों की संख्या क्या है?"
        ),
        "image_url": None,
        "option_a": "25",
        "option_b": "4",
        "option_c": "8",
        "option_d": "27",
        "correct_answer": "C",   # 8 interior cubes = (4−2)³
    },

    # ── Q68 (book Q17) ──────────────────────────────────────────────────────
    # At least 2 surfaces painted:
    #   Edge cubes (2 faces): 12 × (n−2) = 12 × 2 = 24
    #   Corner cubes (3 faces): 8
    #   Total = 24 + 8 = 32.
    {
        "question_number": 68,
        "difficulty": "easy",
        "source_pdf": SOURCE,
        "question_en": (
            f"{PRE_4}"
            "How many small cubes have at least two surfaces painted?"
        ),
        "question_hi": (
            f"{PRE_4_HI}"
            "हमारे पास कुल कितने छोटे घन हैं जिनकी कम से कम दो सतह रंगीन हैं?"
        ),
        "image_url": None,
        "option_a": "32",
        "option_b": "1",
        "option_c": "64",
        "option_d": "36",
        "correct_answer": "A",   # 32 = 24 edge + 8 corner
    },

    # ── Q69 (book Q18) ──────────────────────────────────────────────────────
    # Cuboid 4×3×3 cm, cut into 1 cm cubes = 36 small cubes.
    # Face colours:
    #   Yellow: 2 opposite faces of size 4×3 (say top + bottom, z-axis pair)
    #   Red:    2 opposite faces of size 4×3 (say front + back, x-axis pair)
    #   Green:  2 opposite faces of size 3×3 (left + right, y-axis pair)
    #
    # "Only two faces coloured" = edge cubes (touching exactly 2 outer faces):
    #   4 edges along the 4 cm axis (x): each has (4−2) = 2 interior cubes → 4×2 = 8
    #   4 edges along one 3 cm axis (y): each has (3−2) = 1 interior cube  → 4×1 = 4
    #   4 edges along other 3 cm axis (z): each has (3−2) = 1 interior cube → 4×1 = 4
    #   Total = 8 + 4 + 4 = 16.
    {
        "question_number": 69,
        "difficulty": "medium",
        "source_pdf": SOURCE,
        "question_en": (
            "There is a cuboid whose dimensions are 4×3×3 cm. "
            "The opposite faces of dimensions 4×3 are coloured yellow. "
            "The opposite faces of other dimensions 4×3 are coloured red. "
            "The opposite faces of dimensions 3×3 are coloured green. "
            "Now the cuboid is cut into small cubes of side 1 cm. "
            "How many small cubes will have only two faces coloured?"
        ),
        "question_hi": (
            "एक घनाभ है जिसका परिमाण 4 × 3 × 3 सेमी है। "
            "परिमाण 4 × 3 के विपरीत चेहरे पीले रंग के होते हैं। "
            "अन्य परिमाण 4 × 3 के विपरीत चेहरे लाल रंग के होते हैं। "
            "परिमाण 3 × 3 के विपरीत चेहरे हरे रंग के होते हैं। "
            "अब घनाभ को 1 सेमी भुजा के छोटे घनों में काट दिया जाता है। "
            "कितने छोटे घनों में केवल दो सतह रंगी होंगी?"
        ),
        "image_url": None,
        "option_a": "12",
        "option_b": "24",
        "option_c": "16",
        "option_d": "21",
        "correct_answer": "C",   # 16 = 4×(4−2) + 4×(3−2) + 4×(3−2) = 8+4+4
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
            qn = d["question_number"]
            if qn in existing_qnums:
                print(f"  SKIP  Q{qn}: already in DB")
                skipped += 1
                continue
            db.add(Question(subject=SUBJECT, topic=TOPIC, **d))
            inserted += 1
            print(f"  INSERT Q{qn}  (book Q{qn - 51})")
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
