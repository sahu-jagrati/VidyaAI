"""
seed_reasoning_non_verbal_sheet13.py
========================================
Seeds Reasoning → Non-Verbal  Q74, Q75, Q76, Q78, Q79, Q80, Q81.

(Q77 not yet provided — gap intentional.)

Question types:
  Q74–Q76, Q78–Q80  = Odd One Out ("find the odd figure from alternatives")
  Q81               = Dot Situation ("find alt figure with same dot conditions")

NOTE: image_url = None; upload images to Supabase and run
      update_non_verbal_image_urls_batch13.py.

Bucket  : question_image_Non_Verbal
Pattern : non_verbal_{N}.png

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q74 C  Odd one out. Options (a),(b),(d) all have a SQUARE as the
     outermost enclosing shape (containing a triangle+circle, nested
     rectangles, and a hexagon respectively). Option (c) has a CIRCLE
     as the outermost shape (containing concentric circles).
     → C is the odd one out.

Q75 A  Odd one out. Options (b),(c),(d) all have 4-sided outer shapes
     (square/rectangle) with internal line patterns. Option (a) is a
     HEXAGON (6-sided) with an internal star/web pattern.
     → A is the odd one out.

Q76 B  Odd one out. Options (a),(c),(d) each have an enclosing
     square/rectangle containing internal bracket/L-shapes or lines.
     Option (b) shows only parallel vertical lines with NO enclosing
     outer shape. → B is the odd one out.

Q78 D  Odd one out. Options (a),(b),(c) all show overlapping or
     adjacent rectangles/squares. Option (d) shows triangle/line
     shapes — a completely different figure type.
     → D is the odd one out.

Q79 D  Odd one out. Options (a),(b),(c) each show a circle with a
     triangular flag/marker in the same relative orientation. Option
     (d) has the flag/marker rotated to a different position.
     → D is the odd one out.

Q80 B  Odd one out. Options (a),(c),(d) each show one shape containing
     another (triangle+square, triangle+oval, square+circle — a
     "shape-within-shape" pattern). Option (b) is a hatched/striped
     parallelogram — not a shape-within-shape figure.
     → B is the odd one out.

Q81 B  Dot situation. Question figure (X): large outer square + circle
     + inner small square. The dot is placed in the region that is
     inside the circle AND inside the outer square but OUTSIDE the
     inner small square. Option (b) has the same three-region
     arrangement where that intersection region exists.
     → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Non-Verbal"

QUESTIONS = [

    # ── Q74 ──────────────────────────────────────────────────────────────────
    # Odd one out. (a)(b)(d) = square outer shape; (c) = circle outer. → C.
    {
        "question_number": 74,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question find the odd figure "
            "from the given alternatives."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में दिए गए विकल्पों में से बेजोड़ आकृति "
            "ज्ञात कीजिए।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "C",
        # (a) square→triangle+circle, (b) nested rectangles, (d) square→hexagon
        # all have square as outermost; (c) circle→concentric circles → odd. → C.
    },

    # ── Q75 ──────────────────────────────────────────────────────────────────
    # Odd one out. (a) hexagon; (b)(c)(d) = 4-sided outer shapes. → A.
    {
        "question_number": 75,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question find the odd figure "
            "from the given alternatives."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में दिए गए विकल्पों में से बेजोड़ आकृति "
            "ज्ञात कीजिए।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "A",
        # (b),(c),(d) have 4-sided (square/rectangle) outer shapes with internal
        # lines; (a) is a 6-sided hexagon with star pattern — the odd one. → A.
    },

    # ── Q76 ──────────────────────────────────────────────────────────────────
    # Odd one out. (a)(c)(d) have enclosing shape; (b) = parallel lines only. → B.
    {
        "question_number": 76,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question find the odd figure "
            "from the given alternatives."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में दिए गए विकल्पों में से बेजोड़ आकृति "
            "ज्ञात कीजिए।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # (a),(c),(d) each have a square/rectangle enclosing internal bracket or
        # L-shapes; (b) shows only parallel vertical lines, no outer enclosure. → B.
    },

    # ── Q78 ──────────────────────────────────────────────────────────────────
    # Odd one out. (a)(b)(c) = overlapping rectangles; (d) = triangle/lines. → D.
    {
        "question_number": 78,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question find the odd figure "
            "from the given alternatives."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में दिए गए विकल्पों में से बेजोड़ आकृति "
            "ज्ञात कीजिए।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "D",
        # (a),(b),(c) all show overlapping/adjacent rectangles or squares;
        # (d) shows triangle and line shapes — completely different. → D.
    },

    # ── Q79 ──────────────────────────────────────────────────────────────────
    # Odd one out. (a)(b)(c) = circle+flag same orientation; (d) different. → D.
    {
        "question_number": 79,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question find the odd figure "
            "from the given alternatives."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में दिए गए विकल्पों में से बेजोड़ आकृति "
            "ज्ञात कीजिए।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "D",
        # (a),(b),(c) each show a circle with a triangular flag/marker in the
        # same relative orientation; (d) has the flag rotated differently. → D.
    },

    # ── Q80 ──────────────────────────────────────────────────────────────────
    # Odd one out. (a)(c)(d) = shape-within-shape; (b) = hatched parallelogram. → B.
    {
        "question_number": 80,
        "difficulty": "easy",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question find the odd figure "
            "from the given alternatives."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में दिए गए विकल्पों में से बेजोड़ आकृति "
            "ज्ञात कीजिए।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # (a) triangle containing square, (c) triangle containing oval,
        # (d) square containing circle — all "shape within shape";
        # (b) hatched/striped parallelogram — no inner shape → odd. → B.
    },

    # ── Q81 ──────────────────────────────────────────────────────────────────
    # Dot situation. Dot inside circle + outer square, outside inner square. → B.
    {
        "question_number": 81,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In the following question, a figure (X) consisting of dot(s) is "
            "given. Choose an alternative figure which has the same conditions "
            "of regions in which dot(s) must be placed as in the given figure (X)."
        ),
        "question_hi": (
            "निम्नलिखित प्रश्न में, बिंदुओं से युक्त एक आकृति (X) दी गई है। "
            "एक वैकल्पिक आकृति चुनें जिसमें उन क्षेत्रों की समान स्थितियाँ "
            "हों जिनमें बिंदु दिए जाने चाहिए जैसा कि दिए गए चित्र (X) में है।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Figure (X): outer square + circle + inner small square.
        # Dot is inside the circle AND inside the outer square but outside
        # the inner small square. Option (b) has the same three-region
        # arrangement where that intersection exists. → B.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(
            f"Seeding Non-Verbal Q74–Q76, Q78–Q81 "
            f"into '{TOPIC}' / '{SUBJECT}'"
        )
        print("(Q77 is a gap — not provided yet)")

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
                "\n  Upload non_verbal_74.png – non_verbal_76.png, "
                "non_verbal_78.png – non_verbal_81.png "
                "to Supabase bucket 'question_image_Non_Verbal', then run:\n"
                "  python update_non_verbal_image_urls_batch13.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
