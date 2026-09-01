"""
seed_reasoning_non_verbal_sheet9.py
========================================
Seeds Reasoning → Non-Verbal  Q41–Q46.

All six are Classification questions:
"A series of figures is given which can be grouped into classes.
 Select the groups into which the figures can be classified."

Unlike previous Non-Verbal questions (where options were visual images),
these classification questions have TEXT answer options (figure-number
groupings), so option_a/b/c/d store the actual grouping strings.

NOTE: image_url = None; upload images to Supabase and run
      update_non_verbal_image_urls_batch9.py.

Bucket  : question_image_Non_Verbal
Pattern : non_verbal_{N}.png

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q41 B  8 house figures. Classified by window/door arrangement into
     matching pairs. Option (b): (1,4; 2,7; 3,5; 6,8). → B.

Q42 B  9 geometric shapes in 3×3 grid.
     Group 1 (plain outlines): 1-triangle, 5-circle, 6-rectangle.
     Group 2 (X-marked shapes): 2-X-triangle, 3-X-square, 4-X-circle.
     Group 3 (small/patterned): 7, 8, 9.
     Option (b): (1,5,6; 2,3,4; 7,8,9). → B.

Q43 B  9 angular/bent line figures. Classified by opening direction
     and angle type. Option (b): (1,6,9; 3,4,7; 2,5,8). → B.

Q44 B  9 polygon shapes. Classified by shape family:
     - Arrow/concave quadrilaterals: 1, 3, 2
     - Medium arrow-type pentagons: 4, 5, 7
     - Triangular/inverted shapes: 6, 8, 9
     Option (b): 132, 457, 689. → B.

Q45 C  9 mixed shapes (stars, triangles, squares, combined).
     Group 1 (compound/combined): 4 (triangle+circle), 6 (star+triangle),
                                   8 (arc/curved).
     Group 2 (square-family): 3 (square), 5 (complex star), 7 (solid square).
     Group 3 (simple pointed/star+triangle): 1 (4-pt star), 2 (triangle),
                                              9 (star).
     Option (c): (4,6,8; 3,5,7; 1,2,9). → C.

Q46 B  9 figures (3×3 layout). Classified by column/diagonal grouping.
     Option (b): (3,6,9; 1,5,8; 2,4,7). → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Non-Verbal"

QUESTIONS = [

    # ── Q41 ──────────────────────────────────────────────────────────────────
    # Classification. 8 house designs. → B.
    {
        "question_number": 41,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question a series of figures is given "
            "which can be grouped into classes. Select the groups into "
            "which the figures can be classified."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में आकृतियों की एक श्रृंखला दी गई है "
            "जिन्हें वर्गों में समूहीकृत किया जा सकता है। उन समूहों का "
            "चयन करें जिनमें आंकड़ों को वर्गीकृत किया जा सकता है।"
        ),
        "image_url": None,
        "option_a": "(1, 7; 2, 4; 3, 5; 6, 8)",
        "option_b": "(1, 4; 2, 7; 3, 5; 6, 8)",
        "option_c": "(1, 3; 2, 7; 6, 8; 4, 5)",
        "option_d": "(1, 4; 2, 6; 3, 5; 7, 8)",
        "correct_answer": "B",
    },

    # ── Q42 ──────────────────────────────────────────────────────────────────
    # Classification. 9 geometric shapes. Plain / X-marked / small. → B.
    {
        "question_number": 42,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question a series of figures is given "
            "which can be grouped into classes. Select the groups into "
            "which the figures can be classified."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में आकृतियों की एक श्रृंखला दी गई है "
            "जिन्हें वर्गों में समूहीकृत किया जा सकता है। उन समूहों का "
            "चयन करें जिनमें आंकड़ों को वर्गीकृत किया जा सकता है।"
        ),
        "image_url": None,
        "option_a": "(1, 2, 3; 4, 5, 8; 6, 7, 9)",
        "option_b": "(1, 5, 6; 2, 3, 4; 7, 8, 9)",
        "option_c": "(1, 3, 5; 2, 4, 8; 6, 7, 9)",
        "option_d": "(1, 4, 7; 2, 5, 8; 3, 6, 9)",
        "correct_answer": "B",
        # Group 1 plain outlines (1,5,6); Group 2 X-marked (2,3,4);
        # Group 3 small/patterned (7,8,9). → B.
    },

    # ── Q43 ──────────────────────────────────────────────────────────────────
    # Classification. 9 angular/bent line figures. → B.
    {
        "question_number": 43,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question a series of figures is given "
            "which can be grouped into classes. Select the groups into "
            "which the figures can be classified."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में आकृतियों की एक श्रृंखला दी गई है "
            "जिन्हें वर्गों में समूहीकृत किया जा सकता है। उन समूहों का "
            "चयन करें जिनमें आंकड़ों को वर्गीकृत किया जा सकता है।"
        ),
        "image_url": None,
        "option_a": "1, 6, 9; 2, 4, 7; 3, 5, 8",
        "option_b": "1, 6, 9; 3, 4, 7; 2, 5, 8",
        "option_c": "2, 6, 9; 1, 4, 3; 5, 7, 8",
        "option_d": "2, 9, 3; 1, 8, 7; 4, 5, 6",
        "correct_answer": "B",
        # Classified by opening direction / angle type:
        # (1,6,9); (3,4,7); (2,5,8). → B.
    },

    # ── Q44 ──────────────────────────────────────────────────────────────────
    # Classification. 9 polygon shapes. → B (132, 457, 689).
    {
        "question_number": 44,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question a series of figures is given "
            "which can be grouped into classes. Select the groups into "
            "which the figures can be classified."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में आकृतियों की एक श्रृंखला दी गई है "
            "जिन्हें वर्गों में समूहीकृत किया जा सकता है। उन समूहों का "
            "चयन करें जिनमें आंकड़ों को वर्गीकृत किया जा सकता है।"
        ),
        "image_url": None,
        "option_a": "789, 243, 156",
        "option_b": "132, 457, 689",
        "option_c": "168, 347, 259",
        "option_d": "169, 347, 258",
        "correct_answer": "B",
        # Arrow/concave (1,3,2); medium-arrow pentagons (4,5,7);
        # triangular/inverted (6,8,9). → B.
    },

    # ── Q45 ──────────────────────────────────────────────────────────────────
    # Classification. 9 mixed shapes (stars, triangles, squares). → C.
    {
        "question_number": 45,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question a series of figures is given "
            "which can be grouped into classes. Select the groups into "
            "which the figures can be classified."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में आकृतियों की एक श्रृंखला दी गई है "
            "जिन्हें वर्गों में समूहीकृत किया जा सकता है। उन समूहों का "
            "चयन करें जिनमें आंकड़ों को वर्गीकृत किया जा सकता है।"
        ),
        "image_url": None,
        "option_a": "3, 4, 9; 5, 7, 8; 1, 2, 6",
        "option_b": "1, 5, 6; 2, 4, 8; 3, 7, 9",
        "option_c": "4, 6, 8; 3, 5, 7; 1, 2, 9",
        "option_d": "1, 2, 7; 3, 5, 9; 4, 6, 8",
        "correct_answer": "C",
        # Combined shapes (4,6,8); square-family (3,5,7);
        # simple pointed/star+triangle (1,2,9). → C.
    },

    # ── Q46 ──────────────────────────────────────────────────────────────────
    # Classification. 9 figures (3×3 grid). Column/diagonal grouping. → B.
    {
        "question_number": 46,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question a series of figures is given "
            "which can be grouped into classes. Select the groups into "
            "which the figures can be classified."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में आकृतियों की एक श्रृंखला दी गई है "
            "जिन्हें वर्गों में समूहीकृत किया जा सकता है। उन समूहों का "
            "चयन करें जिनमें आंकड़ों को वर्गीकृत किया जा सकता है।"
        ),
        "image_url": None,
        "option_a": "(1, 2, 3); (4, 5, 6); (7, 8, 9)",
        "option_b": "(3, 6, 9); (1, 5, 8); (2, 4, 7)",
        "option_c": "(5, 6, 9); (4, 7, 8); (1, 2, 3)",
        "option_d": "(1, 5, 9); (3, 4, 8); (2, 6, 7)",
        "correct_answer": "B",
        # Column/diagonal-based grouping of the 3×3 figure grid. → B.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Non-Verbal Q41–Q46 into '{TOPIC}' / '{SUBJECT}'")

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
                "\n  Upload non_verbal_41.png – non_verbal_46.png to Supabase bucket "
                "'question_image_Non_Verbal', then run:\n"
                "  python update_non_verbal_image_urls_batch9.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
