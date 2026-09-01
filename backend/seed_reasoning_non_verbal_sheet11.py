"""
seed_reasoning_non_verbal_sheet11.py
========================================
Seeds Reasoning → Non-Verbal  Q56, Q57, Q58, Q59, Q60, Q61.

All six are Series Completion questions:
"Find the missing figure of the series from the given answer figures."
(Q58-Q59 phrased as: "a series is given with one term missing")
(Q61 phrased as: "select the related figure from the given alternatives")

NOTE: image_url = None; upload images to Supabase and run
      update_non_verbal_image_urls_batch11.py.

Bucket  : question_image_Non_Verbal
Pattern : non_verbal_{N}.png

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q56 B  Question figure: 2×3 grid with triangle and circle shapes in
     varying fills. The series pattern requires the missing bottom-right
     cell to contain a plain triangle outline. Option (b) shows this. → B.

Q57 B  Question figure: 4-frame sequence — circles on top increase
     while S-symbols below decrease each frame (frame1: 1○+4S,
     frame2: 2○+3S, frame3: 2○+2S, frame4: ?).
     Option (b) completes the progression with 2 circles and 1 S. → B.

Q58 D  Question figure: Star/asterisk shapes with lines decreasing per
     frame: Star of David (6-line) → 5-line star → double-X (4 lines)
     → single-X (2 lines) → ?. Next step = 2 parallel diagonal lines
     (// pattern). Option (d) shows //. → D.

Q59 C  Question figure: Bracket/L-shaped figure rotates 90° clockwise
     each frame. 3 frames shown; 4th frame = 270° total rotation from
     starting position. Option (c) shows the correct orientation. → C.

Q60 A  Question figure: Row of symbols following a repeating pattern:
     □◆≡ | □●◇ | □◆≡ | □●◇ | □… The next group starts with ◆,
     making option (a) (showing ◆ □ ≡ or similar) the continuation. → A.

Q61 D  Question figure: 3×3 matrix of symbol clusters. Each row/column
     contains the same set of symbols rearranged. The missing cell
     requires the symbols not yet placed in that row/column.
     Option (d) shows the correct remaining symbol combination. → D.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Non-Verbal"

QUESTIONS = [

    # ── Q56 ──────────────────────────────────────────────────────────────────
    # Series completion. 2×3 grid, triangle/circle shapes. → B.
    {
        "question_number": 56,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Find the missing figure in the series from the given answer figures."
        ),
        "question_hi": (
            "दी गई उत्तर आकृतियों से श्रृंखला की लुप्त आकृति ज्ञात कीजिए।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # 2×3 grid with triangle and circle shapes (outline vs filled varying).
        # Missing bottom-right = plain triangle outline → option (b). → B.
    },

    # ── Q57 ──────────────────────────────────────────────────────────────────
    # Series completion. Circles increase, S-symbols decrease per frame. → B.
    {
        "question_number": 57,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Which of the following answer figures can complete the given series?"
        ),
        "question_hi": (
            "निम्नलिखित में से कौन सी उत्तर आकृतियाँ दी गई श्रृंखला को "
            "पूरा कर सकती है?"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Frame 1: 1 circle + 4 S-symbols; Frame 2: 2 circles + 3 S-symbols;
        # Frame 3: 2 circles + 2 S-symbols; Frame 4: 2 circles + 1 S → (b). → B.
    },

    # ── Q58 ──────────────────────────────────────────────────────────────────
    # Series completion. Star lines reduce each frame; 5th frame = //. → D.
    {
        "question_number": 58,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions a series is given with one "
            "term missing. Choose the correct alternative from the given ones "
            "that will complete the series."
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में एक श्रृंखला दी गई है जिसमें "
            "एक पद लुप्त है। दिए गए विकल्पों में से वह सही विकल्प चुनें "
            "जो श्रृंखला को पूरा करेगा।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "D",
        # Star/asterisk lines reduce per frame: ✡(6-line) → 5-line →
        # ✗✗(double-X) → ✗(single-X) → // (two parallel diagonals) → (d). → D.
    },

    # ── Q59 ──────────────────────────────────────────────────────────────────
    # Series completion. Bracket/L-shape rotates 90° CW each frame. → C.
    {
        "question_number": 59,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions a series is given with one "
            "term missing. Choose the correct alternative from the given ones "
            "that will complete the series."
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में एक श्रृंखला दी गई है जिसमें "
            "एक पद लुप्त है। दिए गए विकल्पों में से वह सही विकल्प चुनें "
            "जो श्रृंखला को पूरा करेगा।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "C",
        # Bracket/L-shape rotates 90° clockwise per frame; after 3 frames
        # (270° total rotation) the 4th frame = option (c). → C.
    },

    # ── Q60 ──────────────────────────────────────────────────────────────────
    # Series completion. Row of symbols in repeating pattern. → A.
    {
        "question_number": 60,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In following questions, find the missing figure of the series "
            "from the given answer figures."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्नों में, दी गई उत्तर आकृतियों से श्रृंखला की "
            "लुप्त आकृति ज्ञात कीजिए।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "A",
        # Row of symbols: □◆≡ | □●◇ | □◆≡ | □●◇ | □…
        # Next group continues with ◆ → option (a). → A.
    },

    # ── Q61 ──────────────────────────────────────────────────────────────────
    # Series completion / matrix analogy. Symbol clusters; ? = remaining set. → D.
    {
        "question_number": 61,
        "difficulty": "hard",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions select the related figure "
            "from the given alternatives."
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में, दिए गए विकल्पों में से संबंधित "
            "आकृति का चयन करें।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "D",
        # 3×3 matrix of symbol clusters; each row contains the same set of
        # symbols rearranged. Missing cell = option (d) with the correct
        # remaining symbol combination. → D.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Non-Verbal Q56–Q61 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload non_verbal_56.png – non_verbal_61.png to Supabase bucket "
                "'question_image_Non_Verbal', then run:\n"
                "  python update_non_verbal_image_urls_batch11.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
