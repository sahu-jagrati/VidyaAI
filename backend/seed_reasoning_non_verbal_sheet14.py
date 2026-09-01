"""
seed_reasoning_non_verbal_sheet14.py
========================================
Seeds Reasoning → Non-Verbal  Q83, Q84, Q85, Q86, Q88, Q89, Q90.

(Q82 and Q87 not yet provided — gaps intentional.)

Question type: ALL are Dot Situation questions.
"Choose an alternative figure which has the same conditions of regions
 in which dot(s) must be placed as in the given figure (X)."

NOTE: image_url = None; upload images to Supabase and run
      update_non_verbal_image_urls_batch14.py.

Bucket  : question_image_Non_Verbal
Pattern : non_verbal_{N}.png

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q83 A  Figure (X): pentagon/house shape with a circle inside. The dot
     is in the region that is INSIDE the circle AND INSIDE the
     pentagon. Option (a) has a similar outer pentagon/house with a
     circle — the dot can occupy the same double-inside region. → A.

Q84 C  Figure (X): circle with a small square/rectangle inside, plus
     an overlapping triangle. The dot is inside the circle but OUTSIDE
     the inner square and OUTSIDE the triangle. Option (c) has the
     matching three-shape arrangement where that region exists. → C.

Q85 B  Figure (X): outer square with a circle inside. The dot is
     inside the circle AND inside the outer square (i.e. inside both).
     Option (b) has a square enclosing a circle — the dot can sit in
     the interior of the circle which is also inside the square. → B.

Q86 A  Figure (X): large circle containing a triangle AND a small
     square. The dot is inside the large circle but OUTSIDE both the
     triangle and the small square. Option (a) has the same three-shape
     arrangement (circle + triangle + square) where that region — inside
     circle only — exists. → A.

Q88 A  Figure (X): triangle overlapping with a circle, and a square.
     The dot is inside the triangle AND inside the circle, but OUTSIDE
     the square. Option (a) provides the same overlapping region of
     triangle ∩ circle that is also outside the square. → A.

Q89 D  Figure (X): circle overlapping with a square, plus an outer
     rectangle. The dot is inside the circle AND inside the square but
     OUTSIDE the outer rectangle. Option (d) has the matching
     arrangement where the circle-square intersection exists outside
     the larger enclosing shape. → D.

Q90 C  Figure (X): outer oval/large circle containing a smaller circle;
     a square is also present. The dot is inside the outer circle AND
     inside the inner circle (double-circle region), outside the square.
     Option (c) has the same nested-circle + square arrangement where
     the dot can sit inside both circles but outside the square. → C.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Non-Verbal"

QUESTIONS = [

    # ── Q83 ──────────────────────────────────────────────────────────────────
    # Dot inside pentagon AND inside circle. → A.
    {
        "question_number": 83,
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
        "correct_answer": "A",
        # (X): pentagon/house shape + circle. Dot = inside circle ∩ inside pentagon.
        # Option (a) has the same two-shape arrangement with that region. → A.
    },

    # ── Q84 ──────────────────────────────────────────────────────────────────
    # Dot inside circle, outside inner square and triangle. → C.
    {
        "question_number": 84,
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
        "correct_answer": "C",
        # (X): circle + inner square + triangle. Dot = inside circle, outside
        # square, outside triangle. Option (c) has matching three-shape region. → C.
    },

    # ── Q85 ──────────────────────────────────────────────────────────────────
    # Dot inside circle AND inside outer square. → B.
    {
        "question_number": 85,
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
        # (X): outer square containing a circle. Dot = inside circle ∩ inside square
        # (i.e. inside both). Option (b) has square enclosing circle → same region. → B.
    },

    # ── Q86 ──────────────────────────────────────────────────────────────────
    # Dot inside large circle, outside triangle AND outside inner square. → A.
    {
        "question_number": 86,
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
        "correct_answer": "A",
        # (X): large circle containing a triangle and a small square. Dot = inside
        # circle only (outside triangle, outside square). Option (a) has the same
        # three-shape arrangement with that exclusive-circle region. → A.
    },

    # ── Q88 ──────────────────────────────────────────────────────────────────
    # Dot inside triangle AND inside circle, outside square. → A.
    {
        "question_number": 88,
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
        "correct_answer": "A",
        # (X): triangle + circle overlapping + square. Dot = inside triangle ∩ circle,
        # outside square. Option (a) provides the same triangle∩circle region that
        # is also outside the square. → A.
    },

    # ── Q89 ──────────────────────────────────────────────────────────────────
    # Dot inside circle AND inside square, outside outer rectangle. → D.
    {
        "question_number": 89,
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
        "correct_answer": "D",
        # (X): circle overlapping with square, plus outer rectangle. Dot = inside
        # circle ∩ inside square, outside outer rectangle. Option (d) has the
        # matching arrangement where that circle-square intersection exists
        # outside the larger shape. → D.
    },

    # ── Q90 ──────────────────────────────────────────────────────────────────
    # Dot inside outer circle AND inside inner circle, outside square. → C.
    {
        "question_number": 90,
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
        "correct_answer": "C",
        # (X): outer large circle/oval + inner smaller circle + square. Dot = inside
        # outer circle ∩ inside inner circle (double-inside), outside square.
        # Option (c) has the same nested-circle + square arrangement. → C.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(
            f"Seeding Non-Verbal Q83–Q86, Q88–Q90 "
            f"into '{TOPIC}' / '{SUBJECT}'"
        )
        print("(Q82 and Q87 are gaps — not provided yet)")

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
                "\n  Upload non_verbal_83.png – non_verbal_86.png, "
                "non_verbal_88.png – non_verbal_90.png "
                "to Supabase bucket 'question_image_Non_Verbal', then run:\n"
                "  python update_non_verbal_image_urls_batch14.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
