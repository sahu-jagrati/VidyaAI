"""
assign_difficulty.py
====================
Assigns a difficulty level to every question that has difficulty = NULL.

Distribution (deterministic by question id so re-runs are idempotent):
  easy   ~33%   (id % 3 == 0)
  medium ~34%   (id % 3 == 1)
  hard   ~33%   (id % 3 == 2)

Run:
    python assign_difficulty.py
    python assign_difficulty.py --default medium   # set all NULL to one level
    python assign_difficulty.py --dry-run          # preview only
"""

import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from app.database.connection import SessionLocal
from app.models.question_model import Question

LEVELS = ["easy", "medium", "hard"]


def assign(default: str | None, dry_run: bool) -> None:
    db = SessionLocal()
    try:
        questions = db.query(Question).filter(Question.difficulty == None).all()
        print(f"Found {len(questions)} questions with difficulty = NULL")

        if not questions:
            print("Nothing to do.")
            return

        counts = {"easy": 0, "medium": 0, "hard": 0}
        for q in questions:
            if default:
                level = default
            else:
                level = LEVELS[q.id % 3]

            if not dry_run:
                q.difficulty = level
            counts[level] += 1

        if not dry_run:
            db.commit()
            print("Committed.")
        else:
            print("[DRY RUN — no changes written]")

        print(f"  easy   : {counts['easy']}")
        print(f"  medium : {counts['medium']}")
        print(f"  hard   : {counts['hard']}")

    finally:
        db.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--default", choices=["easy", "medium", "hard"],
                        help="Set all NULL questions to this level instead of distributing")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print counts without writing to DB")
    args = parser.parse_args()
    assign(args.default, args.dry_run)


if __name__ == "__main__":
    main()
