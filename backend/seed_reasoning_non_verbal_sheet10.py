"""
seed_reasoning_non_verbal_sheet10.py
========================================
Seeds Reasoning → Non-Verbal  Q47, Q48, Q49, Q51, Q52, Q53, Q54.

(Q50 not yet provided — gap intentional.)

Question types:
  Q47–Q49  = Classification
  Q51–Q54  = Series Completion ("Find the missing figure of the series")

NOTE: image_url = None; upload images to Supabase and run
      update_non_verbal_image_urls_batch10.py.

Bucket  : question_image_Non_Verbal
Pattern : non_verbal_{N}.png

Answer key & derivations
──────────────────────────────────────────────────────────────────────
Q47 A  9 objects (clothes, stationery, geometric shapes).
     Group 1 — clothing     : 1 (shirt), 4 (shorts), 9 (sweater) → (1,4,9)
     Group 2 — stationery   : 2 (pencil), 5 (book), 7 (ABC book)  → (2,5,7)
     Group 3 — plain shapes : 3 (rectangle), 6 (circle), 8 (triangle) → (3,6,8)
     Option (a): (1,4,9; 2,5,7; 3,6,8). → A.

Q48 C  9 capital letters A M B H W D E N U.
     Group 1 (two-vertical-stroke letters) : A(1), H(4), N(8) → (1,4,8)
     Group 2 (multi-peak / zigzag letters) : M(2), W(5), E(7) → (2,5,7)
     Group 3 (letters with curves only)    : B(3), D(6), U(9) → (3,6,9)
     Option (c): 148, 257, 369. → C.

Q49 A  9 household / everyday objects.
     Group 1 (circular / disc-shaped): 1 (fan/wheel), 4 (plate), 7 (clock) → (1,4,7)
     Group 2 (tall / elongated shapes): 2 (screw), 5 (pencil), 8 (house) → (2,5,8)
     Group 3 (hollow / container shapes): 3 (cup), 6 (ice-cream cone), 9 (hat) → (3,6,9)
     Option (a): {1,4,7; 2,5,8; 3,6,9}. → A.

Q51 C  Series completion. Question figure: X mark moves from upper-right →
     upper-center → upper-left across 3 frames; a dash/line shifts in
     parallel. The 4th frame continues the sequence: X moves to the
     bottom-left area while the line element completes its shift.
     Option (c) shows this position. → C.

Q52 B  Series completion. Question figure: tree/plant figures that shrink
     and rotate (or flip) each successive frame. The 4th frame should
     show the next stage of the size/rotation progression.
     Option (b) shows the correctly sized and oriented tree piece. → B.

Q53 B  Series completion. Question figure: 4 small icons (house, swastika,
     circle O, X mark) rotate 90° clockwise from frame to frame.
     Tracking each icon's position through frames 1-3, the 4th frame
     places each icon in the next clockwise position.
     Option (b) shows the correct arrangement. → B.

Q54 B  Series completion. Question figure: circles (filled/half/empty) in a
     square that increase in number and change fill across frames.
     Frame progression: 2 → 3 → 4 circles; fills follow a pattern.
     The 4th frame is completed by option (b): large filled circle +
     small circle at the correct position. → B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Non-Verbal"

QUESTIONS = [

    # ── Q47 ──────────────────────────────────────────────────────────────────
    # Classification. 9 objects: clothes / stationery / geometric shapes. → A.
    {
        "question_number": 47,
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
        "option_a": "(1, 4, 9; 2, 5, 7; 3, 6, 8)",
        "option_b": "(1, 4, 9; 2, 3, 8; 5, 6, 7)",
        "option_c": "(1, 4, 9; 2, 5, 8; 3, 6, 7)",
        "option_d": "(1, 4, 9; 2, 6, 3; 5, 7, 8)",
        "correct_answer": "A",
        # Clothes(1,4,9) / Stationery(2,5,7) / Shapes(3,6,8). → A.
    },

    # ── Q48 ──────────────────────────────────────────────────────────────────
    # Classification. 9 capital letters. Curved / two-stroke / multi-peak. → C.
    {
        "question_number": 48,
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
        "option_a": "136, 289, 475",
        "option_b": "148, 236, 579",
        "option_c": "148, 257, 369",
        "option_d": "147, 358, 269",
        "correct_answer": "C",
        # Two-vertical-stroke (A,H,N)=1,4,8; zigzag/multi-peak (M,W,E)=2,5,7;
        # curved only (B,D,U)=3,6,9. → C.
    },

    # ── Q49 ──────────────────────────────────────────────────────────────────
    # Classification. 9 everyday objects. Circular / tall / container. → A.
    {
        "question_number": 49,
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
        "option_a": "1,4,7 / 2,5,8 / 3,6,9",
        "option_b": "1,3,6 / 2,5,8 / 4,7,9",
        "option_c": "1,2,4 / 3,5,8 / 6,7,9",
        "option_d": "1,4,9 / 2,5,8 / 3,6,7",
        "correct_answer": "A",
        # Circular (fan,plate,clock)=1,4,7; tall/thin (screw,pencil,house)=2,5,8;
        # hollow/container (cup,ice-cream,hat)=3,6,9. → A.
    },

    # ── Q51 ──────────────────────────────────────────────────────────────────
    # Series completion. X mark shifts L→R then down; dash shifts. → C.
    {
        "question_number": 51,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Find the missing figure of the series from the given answer figures."
        ),
        "question_hi": (
            "दी गई उत्तर आकृतियों से श्रृंखला की लुप्त आकृति ज्ञात कीजिए।"
        ),
        "image_url": None,
        "option_a": "a",
        "option_b": "b",
        "option_c": "c",
        "option_d": "d",
        "correct_answer": "C",
        # X mark moves: upper-right → upper-center → upper-left → bottom-left.
        # Dash/line shifts in parallel. 4th frame → option (c). → C.
    },

    # ── Q52 ──────────────────────────────────────────────────────────────────
    # Series completion. Tree/plant shrinks and rotates each frame. → B.
    {
        "question_number": 52,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Find the missing figure of the series from the given answer figures."
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
        # Tree figures shrink and rotate (or flip) successively;
        # 4th frame = option (b) at the correct size and orientation. → B.
    },

    # ── Q53 ──────────────────────────────────────────────────────────────────
    # Series completion. 4 icons rotate 90° clockwise each frame. → B.
    {
        "question_number": 53,
        "difficulty": "medium",
        "source_pdf": "Practice_Set",
        "question_en": (
            "Find the missing figure of the series from the given answer figures."
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
        # 4 icons (house, swastika, circle O, X) rotate 90° clockwise per frame.
        # Frame 4 arrangement → option (b). → B.
    },

    # ── Q54 ──────────────────────────────────────────────────────────────────
    # Series completion. Circles accumulate and fill changes per frame. → B.
    {
        "question_number": 54,
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
        # Circles increase in number per frame with changing fills;
        # 4th frame = large filled circle + small circle → option (b). → B.
    },
]


def main() -> None:
    if hasattr(__import__("sys").stdout, "reconfigure"):
        __import__("sys").stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    inserted = skipped = 0
    try:
        print(f"Seeding Non-Verbal Q47–Q49, Q51–Q54 into '{TOPIC}' / '{SUBJECT}'")
        print("(Q50 is a gap — not provided yet)")

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
                "\n  Upload non_verbal_47.png, non_verbal_48.png, non_verbal_49.png, "
                "non_verbal_51.png – non_verbal_54.png "
                "to Supabase bucket 'question_image_Non_Verbal', then run:\n"
                "  python update_non_verbal_image_urls_batch10.py"
            )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
