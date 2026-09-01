"""
seed_reasoning_cube_cuboid_sheet1.py
========================================
Seeds Reasoning → Cube & Cuboid  Q1–Q4.

NOTE: image_url = None for all rows; upload images to Supabase later and run
      update_cube_cuboid_image_urls_batch1.py.

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q1  B  (UPSC CSAT 2024)
     To cut a cube into 64 = 4³ identical pieces, we need 4 layers per
     axis → 3 cuts per axis × 3 axes = 9 minimum cuts (rearranging pieces
     between cuts does not reduce the count below 9). → B.

Q2  A  (UPSC CSAT 2023)
     125 = 5³ block. Cubes "surrounded by other cubes from each side"
     (i.e., not touching any outer face) = interior cubes =
     (5-2)³ = 3³ = 27. → A.

Q3  A  (UPSC CSAT 2023)
     Cuboid 7 cm × 5 cm × 3 cm painted:
       7×5 cm faces → RED ; 5×3 cm faces → GREEN ; 7×3 cm faces → BLUE.
     Cut into 1 cm unit cubes (total = 7×5×3 = 105).

     Statement 1 — "Exactly 15 cubes with no paint":
       Interior cubes = (7-2)×(5-2)×(3-2) = 5×3×1 = 15.  TRUE ✓

     Statement 2 — "Exactly 6 cubes with exactly 2 faces (1 blue + 1 green)":
       Blue∩Green edges run along the 3-cm (z) axis at the 4 corners
       where x ∈ {0,7} meets y ∈ {0,5}.  Each such edge has 3 unit cubes;
       the 2 end cubes are also on a RED face (3 painted faces), leaving
       1 middle cube with exactly BLUE + GREEN per edge.
       Total = 4 edges × 1 cube = 4, NOT 6.  FALSE ✗

     Only Statement 1 is correct → (a) 1 only. → A.

Q4  C  (UPSC CSAT 2019)
     Original cube side = 4 (volume = 64).
     4 big cubes (2×2×2, volume = 8 each) + 32 small cubes (1³) = 64. ✓
     "None of the bigger cubes faces painted blue" → big cubes sit at
       y = 1–3 (away from both blue faces at y=0 and y=4).
     They occupy the 4×2×4 interior band, leaving 32 small cubes in the
     y=0–1 and y=3–4 strips (each a 4×1×4 = 16-cube layer).

     Big cubes each touch 1 yellow face (z=0 or z=4) AND 1 black face
     (x=0 or x=4) → 2 painted faces each; 0 big cubes with exactly 1 face.

     Small cubes with exactly 1 face (blue only, interior of their strip):
       x ∈ {1–2, 2–3}, z ∈ {1–2, 2–3} → 4 cubes per strip × 2 strips = 8.
     Total cubes with exactly 1 painted face = 8. → C.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Cube & Cuboid"

QUESTIONS = [

    # ── Q1 ───────────────────────────────────────────────────────────────────
    # Min cuts to get 64 identical pieces = 3 axes × 3 cuts = 9.
    # Source: UPSC CSAT 2024
    {
        "question_number": 1,
        "difficulty": "medium",
        "source_pdf": "UPSC_CSAT_2024",
        "question_en": (
            "What is the least possible number of cuts required to cut a cube "
            "into 64 identical pieces?"
        ),
        "question_hi": (
            "एक घन को 64 समरूप टुकड़ों में काटने के लिए आवश्यक काटों की "
            "न्यूनतम संभावित संख्या क्या है?"
        ),
        "image_url": None,
        "option_a": "8",
        "option_b": "9",
        "option_c": "12",
        "option_d": "16",
        "correct_answer": "B",
        # 64 = 4³ → need (4-1)=3 cuts along each of 3 axes → 3×3 = 9 minimum.
    },

    # ── Q2 ───────────────────────────────────────────────────────────────────
    # 125 = 5³ block. Cubes with all 6 sides covered = inner cube = (5-2)³ = 27.
    # Source: UPSC CSAT 2023
    {
        "question_number": 2,
        "difficulty": "medium",
        "source_pdf": "UPSC_CSAT_2023",
        "question_en": (
            "125 identical cubes are arranged in the form of a cubical block. "
            "How many cubes are surrounded by other cubes from each side?"
        ),
        "question_hi": (
            "125 सर्वसम घन एक घनाकार खंड के रूप में व्यवस्थित किए गए हैं। "
            "कितने घन हर पाश से अन्य घनों द्वारा घिरे हुए हैं?"
        ),
        "image_url": None,
        "option_a": "27",
        "option_b": "25",
        "option_c": "21",
        "option_d": "18",
        "correct_answer": "A",
        # 125 = 5³; interior (completely surrounded) = (5-2)³ = 3³ = 27.
    },

    # ── Q3 ───────────────────────────────────────────────────────────────────
    # 7×5×3 cuboid: 7×5 faces=RED, 5×3 faces=GREEN, 7×3 faces=BLUE.
    # Cut into 1 cm unit cubes. Statements:
    # 1) 15 cubes no paint (interior = 5×3×1 = 15). TRUE.
    # 2) 6 cubes with exactly 2 faces (1 blue + 1 green). FALSE (only 4).
    # Source: UPSC CSAT 2023
    {
        "question_number": 3,
        "difficulty": "hard",
        "source_pdf": "UPSC_CSAT_2023",
        "question_en": (
            "A cuboid of dimensions 7 cm × 5 cm × 3 cm is painted red, green "
            "and blue colour on each pair of opposite faces of dimensions "
            "7 cm × 5 cm, 5 cm × 3 cm, 7 cm × 3 cm respectively. Then the "
            "cuboid is cut and separated into various cubes each of side length "
            "1 cm. Which of the following statements is/are correct?\n"
            "1. There are exactly 15 small cubes with no paint on any face.\n"
            "2. There are exactly 6 small cubes with exactly two faces, one "
            "painted with blue and the other with green."
        ),
        "question_hi": (
            "7 cm × 5 cm × 3 cm विमाओं वाले एक घनाभ के क्रमशः 7 cm × 5 cm, "
            "5 cm × 3 cm, 7 cm × 3 cm वाले सम्मुख फलकों के प्रत्येक युग्म "
            "को लाल, हरे, और नीले रंग से रंगा गया है। तब इस घनाभ को काटकर "
            "प्रत्येक 1 cm भुजा के विभिन्न घन अलग कर दिए जाते हैं। "
            "निम्नलिखित कथनों में से कौन-सा/से सही है/हैं?\n"
            "1. ऐसे ठीक-ठाक 15 छोटे घन हैं जिनके किसी भी फलक पर कोई रंग "
            "नहीं है।\n"
            "2. ऐसे ठीक-ठाक 6 छोटे घन हैं जिनके ठीक-ठाक दो फलक, एक नीले "
            "और दूसरा हरे रंग से, रंगे हुए हैं।"
        ),
        "image_url": None,
        "option_a": "1 only / केवल 1",
        "option_b": "2 only / केवल 2",
        "option_c": "Both 1 and 2 / 1 और 2 दोनों",
        "option_d": "Neither 1 nor 2 / न तो 1 और न ही 2",
        "correct_answer": "A",
        # Statement 1: interior = (7-2)(5-2)(3-2) = 5×3×1 = 15. TRUE.
        # Statement 2: Blue∩Green edges (z-axis, 4 edges) each yield 1
        # middle cube (not on RED face) → 4 cubes total, not 6. FALSE.
    },

    # ── Q4 ───────────────────────────────────────────────────────────────────
    # Solid cube: yellow/blue/black pairs. Cut into 36 = 4 big (2³) + 32 small (1³).
    # Big cubes avoid blue faces → placed at y=1-3.
    # Cubes with exactly 1 face painted = 8 (interior small cubes on blue-only strips).
    # Source: UPSC CSAT 2019
    {
        "question_number": 4,
        "difficulty": "hard",
        "source_pdf": "UPSC_CSAT_2019",
        "question_en": (
            "A solid cube is painted yellow, blue and black such that opposite "
            "faces are of same colour. The cube is then cut into 36 cubes of "
            "two different sizes such that 32 cubes are small and the other "
            "four cubes are big. None of the faces of the bigger cubes is "
            "painted blue. How many cubes have only one face painted?"
        ),
        "question_hi": (
            "एक ठोस घन को पीला, नीला और काला इस प्रकार रंगा गया है कि इसके "
            "विपरीत फलक एक ही रंग के हैं। तब इस घन को दो भिन्न आमापों के "
            "36 घनों में इस प्रकार काटा गया है कि 32 घन छोटे हैं और अन्य "
            "4 घन बड़े हैं। बड़े घनों का कोई भी फलक नीला नहीं रंगा गया है। "
            "कितने घनों में केवल एक फलक रंगा हुआ है?"
        ),
        "image_url": None,
        "option_a": "4",
        "option_b": "6",
        "option_c": "8",
        "option_d": "10",
        "correct_answer": "C",
        # Original cube = 4³ = 64 unit volume.
        # 4 big (2³) cubes placed at y=1–3 (no blue face), 32 small (1³) in strips.
        # Big cubes each have 2 painted faces → 0 big cubes with 1 face.
        # Small cubes interior to each blue-face strip (away from x and z bounds):
        #   2×2 = 4 cubes per strip × 2 strips = 8 cubes with only 1 (blue) face.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Cube & Cuboid Q1–Q4 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload cube_1.png … cube_4.png to the Supabase bucket "
                "for Cube & Cuboid images, then run:\n"
                "  python update_cube_cuboid_image_urls_batch1.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
