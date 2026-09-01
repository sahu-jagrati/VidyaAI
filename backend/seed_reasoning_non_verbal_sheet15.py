"""
seed_reasoning_non_verbal_sheet15.py
========================================
Seeds Reasoning → Non-Verbal  Q91–Q98, Q100.

(Q99 not yet provided — gap intentional.)

Question type: ALL are Figure Formation questions.
"Find out which of the answer figures can be formed from the pieces
 given in the problem figure."

NOTE: image_url = None; upload images to Supabase and run
      update_non_verbal_image_urls_batch15.py.

Bucket  : question_image_Non_Verbal
Pattern : non_verbal_{N}.png

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q91 B  Pieces: X-pattern cut + triangular piece inside a square frame.
     When assembled, the pieces form a square with a triangle fitted
     inside the X-cut region. Option (b) shows this correctly. → B.

Q92 D  Pieces: two curved oval/leaf-shaped pieces + a triangle-like
     curved piece. When assembled they form a full circle divided into
     three curved sections. Option (d) shows the oval with matching
     curved internal cuts. → D.

Q93 C  Pieces: multiple M-shaped / zigzag line pieces forming a jagged
     pattern. When assembled they tile into a rectangle with the
     matching zigzag/M pattern visible. Option (c) shows this
     arrangement. → C.

Q94 D  Pieces: a small triangle, a dot/circle, a diamond/rhombus, and
     a small rectangle. When assembled these four pieces fit together
     into the figure shown in option (d) — diamond arrangement with
     dot and triangle. → D.

Q95 B  Pieces: irregular jagged/polygon cut pieces from a square.
     When assembled they form a square with an X-diagonal internal
     pattern. Option (b) matches this X-pattern square. → B.

Q96 D  Pieces: four curved arc segments (like slices of a circle with
     concave cuts). When assembled they form a circle with two
     horizontal hourglass-style dividing elements inside. Option (d)
     shows this circle with internal horizontal curved dividers. → D.

Q97 D  Pieces: a large triangle, a K/angular shape, a backward-angular
     shape, and a small triangle piece. When assembled they fit into a
     square forming a triangle + line arrangement. Option (d) shows the
     correct assembled pattern of triangles and lines within a square. → D.

Q98 C  Pieces: an irregular quadrilateral (trapezoid-like), a D-shaped
     half-circle, and another curved piece. When assembled they form a
     circle divided into three sections (like a pie chart with one
     large and two smaller sections). Option (c) shows this circle
     divided into the correct sections. → C.

Q100 B  Pieces: arrow/chevron shapes and angular pieces (pentagons and
      triangular cuts). When assembled they form a square with diagonal
      line arrangements inside. Option (b) shows the correct assembled
      figure with diagonal segments. → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Non-Verbal"

QUESTIONS = [

    # ── Q91 ──────────────────────────────────────────────────────────────────
    # Figure formation. X-cut + triangle pieces → square with triangle inside. → B.
    {
        "question_number": 91,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions, find out which of the answer "
            "figures can be formed from the pieces given in problem figure."
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में, पता लगाएँ कि समस्या आकृति में "
            "दिए गए टुकड़ों से कौन सी उत्तर आकृतियाँ बनाई जा सकती हैं।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Pieces: X-pattern cut and triangular piece from a square.
        # Assembled → square with triangle inside X region → option (b). → B.
    },

    # ── Q92 ──────────────────────────────────────────────────────────────────
    # Figure formation. Curved oval + leaf pieces → circle in 3 sections. → D.
    {
        "question_number": 92,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions, find out which of the answer "
            "figures can be formed from the pieces given in problem figure."
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में, पता लगाएँ कि समस्या आकृति में "
            "दिए गए टुकड़ों से कौन सी उत्तर आकृतियाँ बनाई जा सकती हैं।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "D",
        # Pieces: two curved oval/leaf shapes + triangle-curved piece.
        # Assembled → full circle with 3 curved internal sections → (d). → D.
    },

    # ── Q93 ──────────────────────────────────────────────────────────────────
    # Figure formation. M-shape / zigzag pieces → rectangle with zigzag. → C.
    {
        "question_number": 93,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions, find out which of the answer "
            "figures can be formed from the pieces given in problem figure."
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में, पता लगाएँ कि समस्या आकृति में "
            "दिए गए टुकड़ों से कौन सी उत्तर आकृतियाँ बनाई जा सकती हैं।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "C",
        # Pieces: M/zigzag line-cut shapes from a rectangle.
        # Assembled → rectangle with matching zigzag/M pattern → (c). → C.
    },

    # ── Q94 ──────────────────────────────────────────────────────────────────
    # Figure formation. Triangle + dot + diamond + rectangle → assembled figure. → D.
    {
        "question_number": 94,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions, find out which of the answer "
            "figures can be formed from the pieces given in problem figure."
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में, पता लगाएँ कि समस्या आकृति में "
            "दिए गए टुकड़ों से कौन सी उत्तर आकृतियाँ बनाई जा सकती हैं।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "D",
        # Pieces: small triangle, dot/circle, diamond/rhombus, rectangle.
        # Assembled → diamond arrangement with dot and triangle → (d). → D.
    },

    # ── Q95 ──────────────────────────────────────────────────────────────────
    # Figure formation. Jagged irregular pieces → square with X-diagonal. → B.
    {
        "question_number": 95,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions, find out which of the answer "
            "figures can be formed from the pieces given in problem figure."
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में, पता लगाएँ कि समस्या आकृति में "
            "दिए गए टुकड़ों से कौन सी उत्तर आकृतियाँ बनाई जा सकती हैं।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Pieces: irregular jagged/polygon cuts from a square.
        # Assembled → square with X-diagonal internal pattern → (b). → B.
    },

    # ── Q96 ──────────────────────────────────────────────────────────────────
    # Figure formation. Curved arc segments → circle with hourglass dividers. → D.
    {
        "question_number": 96,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions, find out which of the answer "
            "figures can be formed from the pieces given in problem figure."
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में, पता लगाएँ कि समस्या आकृति में "
            "दिए गए टुकड़ों से कौन सी उत्तर आकृतियाँ बनाई जा सकती हैं।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "D",
        # Pieces: four curved arc/concave segments (like slices of a circle).
        # Assembled → circle with internal horizontal hourglass-style dividers
        # → option (d). → D.
    },

    # ── Q97 ──────────────────────────────────────────────────────────────────
    # Figure formation. Triangle + K-shape + angular + small triangle pieces. → D.
    {
        "question_number": 97,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions, find out which of the answer "
            "figures can be formed from the pieces given in problem figure."
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में, पता लगाएँ कि समस्या आकृति में "
            "दिए गए टुकड़ों से कौन सी उत्तर आकृतियाँ बनाई जा सकती हैं।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "D",
        # Pieces: large triangle, K/angular shape, backward-angular piece, small
        # triangle. Assembled → square with triangle + line arrangement → (d). → D.
    },

    # ── Q98 ──────────────────────────────────────────────────────────────────
    # Figure formation. Trapezoid + half-circle pieces → circle divided in 3. → C.
    {
        "question_number": 98,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions, find out which of the answer "
            "figures can be formed from the pieces given in problem figure."
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में, पता लगाएँ कि समस्या आकृति में "
            "दिए गए टुकड़ों से कौन सी उत्तर आकृतियाँ बनाई जा सकती हैं।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "C",
        # Pieces: irregular quadrilateral (trapezoid), D-shaped half-circle, curved
        # piece. Assembled → circle divided into 3 sections (pie-chart style) → (c). → C.
    },

    # ── Q100 ─────────────────────────────────────────────────────────────────
    # Figure formation. Arrow/chevron + angular pieces → square with diagonals. → B.
    {
        "question_number": 100,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "In each of the following questions, find out which of the answer "
            "figures can be formed from the pieces given in problem figure."
        ),
        "question_hi": (
            "निम्नलिखित प्रत्येक प्रश्न में, पता लगाएँ कि समस्या आकृति में "
            "दिए गए टुकड़ों से कौन सी उत्तर आकृतियाँ बनाई जा सकती हैं।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "B",
        # Pieces: arrow/chevron shapes + angular/pentagonal cut pieces.
        # Assembled → square with diagonal line arrangement inside → (b). → B.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(
            f"Seeding Non-Verbal Q91–Q98, Q100 "
            f"into '{TOPIC}' / '{SUBJECT}'"
        )
        print("(Q99 is a gap — not provided yet)")

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
                "\n  Upload non_verbal_91.png – non_verbal_98.png and "
                "non_verbal_100.png "
                "to Supabase bucket 'question_image_Non_Verbal', then run:\n"
                "  python update_non_verbal_image_urls_batch15.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
