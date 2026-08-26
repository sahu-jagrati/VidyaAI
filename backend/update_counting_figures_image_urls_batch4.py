"""
update_counting_figures_image_urls_batch4.py
=============================================
Sets image_url for ALL Counting Figures questions added in sheets 8–14
(Q52 through Q80 and all their sub-question DB rows).

Naming convention in Supabase Storage bucket
    question_image_Counting_figure:
        figure_52.png … figure_80.png

Sub-questions share the SAME image as their parent question:
    5302, 5303  → figure_53.png   (Q53 sub-parts)
    5402        → figure_54.png   (Q54 sub-part)
    5502        → figure_55.png   (Q55 sub-part)
    5702        → figure_57.png   (Q57 sub-part)
    5802, 5803  → figure_58.png   (Q58 sub-parts)
    5902        → figure_59.png   (Q59 sub-part)
    6502        → figure_65.png   (Q65 sub-part)
    6602        → figure_66.png   (Q66 sub-part)
    6702        → figure_67.png   (Q67 sub-part)
    8002, 8003  → figure_80.png   (Q80 sub-parts)

Run from backend/ directory:
    python update_counting_figures_image_urls_batch4.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from app.models import subscription_model  # noqa: F401

SUBJECT = "Reasoning"
TOPIC   = "Counting Figures"

BASE_URL = (
    "https://mlzcmlopkddsdwcmiujq.supabase.co"
    "/storage/v1/object/public/question_image_Counting_figure"
)

# ── question_number → image filename ────────────────────────────────────────
# Single questions map directly to their own figure file.
# Sub-questions (encoded question_numbers) map to their parent's figure file.

IMAGE_MAP = {
    # ── Sheet 8: Q52–Q57 ────────────────────────────────────────────────────
    52:   "figure_52.png",
    53:   "figure_53.png",
    5302: "figure_53.png",
    5303: "figure_53.png",
    54:   "figure_54.png",
    5402: "figure_54.png",
    55:   "figure_55.png",
    5502: "figure_55.png",
    56:   "figure_56.png",
    57:   "figure_57.png",
    5702: "figure_57.png",

    # ── Sheet 9: Q58–Q59 ────────────────────────────────────────────────────
    58:   "figure_58.png",
    5802: "figure_58.png",
    5803: "figure_58.png",
    59:   "figure_59.png",
    5902: "figure_59.png",

    # ── Sheet 10: Q60–Q62 ───────────────────────────────────────────────────
    60:   "figure_60.png",
    61:   "figure_61.png",
    62:   "figure_62.png",

    # ── Sheet 11: Q63–Q65 ───────────────────────────────────────────────────
    63:   "figure_63.png",
    64:   "figure_64.png",
    65:   "figure_65.png",
    6502: "figure_65.png",

    # ── Sheet 12: Q66–Q68 ───────────────────────────────────────────────────
    66:   "figure_66.png",
    6602: "figure_66.png",
    67:   "figure_67.png",
    6702: "figure_67.png",
    68:   "figure_68.png",

    # ── Sheet 13: Q69–Q76 ───────────────────────────────────────────────────
    69:   "figure_69.png",
    70:   "figure_70.png",
    71:   "figure_71.png",
    72:   "figure_72.png",
    73:   "figure_73.png",
    74:   "figure_74.png",
    75:   "figure_75.png",
    76:   "figure_76.png",

    # ── Sheet 14: Q77–Q80 ───────────────────────────────────────────────────
    77:   "figure_77.png",
    78:   "figure_78.png",
    79:   "figure_79.png",
    80:   "figure_80.png",
    8002: "figure_80.png",
    8003: "figure_80.png",
}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    db = SessionLocal()
    updated = not_found = already_set = 0
    try:
        for qnum, filename in sorted(IMAGE_MAP.items()):
            url = f"{BASE_URL}/{filename}"
            row = (
                db.query(Question)
                .filter(
                    Question.subject         == SUBJECT,
                    Question.topic           == TOPIC,
                    Question.question_number == qnum,
                )
                .first()
            )
            if row is None:
                print(f"  NOT FOUND  Q{qnum}")
                not_found += 1
                continue
            if row.image_url == url:
                already_set += 1
                continue
            row.image_url = url
            updated += 1
            print(f"  UPDATED  Q{qnum:5}  →  {filename}")

        db.commit()
        print(
            f"\nDone — updated: {updated}, "
            f"already set: {already_set}, "
            f"not found: {not_found}"
        )
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
