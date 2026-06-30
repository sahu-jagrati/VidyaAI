#!/usr/bin/env python3
"""
seed_from_json.py — VidyaAi PDF Ingestion Pipeline · Stage 3
=============================================================
Reads every JSON from processed/, inserts valid questions into PostgreSQL.

Seed rules:
  • correct_answer = NULL   (filled later via solve_questions.py)
  • difficulty     = NULL   (filled later)
  • created_at     = current timestamp

Duplicate detection: (question_en[:200], topic) pair already in DB → skip.

Logging per PDF:
  • PDF name
  • Questions in JSON
  • Inserted
  • Skipped (duplicates)
  • Invalid (missing fields)
  • Time taken

Usage:
    python scripts/seed_from_json.py
    python scripts/seed_from_json.py --verbose
"""

import argparse
import json
import logging
import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.database.connection import SessionLocal
from app.models.question_model import Question
from sqlalchemy import text

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR      = Path(__file__).resolve().parent.parent
PROCESSED_DIR = BASE_DIR / "processed"
LOGS_DIR      = BASE_DIR / "logs"


# ── Logging ────────────────────────────────────────────────────────────────────
def setup_logging(verbose: bool = False) -> logging.Logger:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_file = LOGS_DIR / f"seed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    fmt = "%(asctime)s  %(levelname)-8s  %(message)s"
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format=fmt,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_file, encoding="utf-8"),
        ],
    )
    return logging.getLogger("seed")


# ── Per-file seeder ────────────────────────────────────────────────────────────
def seed_file(
    jf:       Path,
    existing: set[tuple[str, str]],
    db,
    log:      logging.Logger,
) -> tuple[int, int, int]:
    """
    Seed one JSON file.  Returns (inserted, skipped, invalid).
    Updates `existing` in-place so subsequent files don't repeat duplicates.
    """
    try:
        data = json.loads(jf.read_text(encoding="utf-8"))
    except Exception as exc:
        log.error("Cannot read %s: %s", jf.name, exc)
        return 0, 0, 0

    if not isinstance(data, list):
        return 0, 0, 0

    inserted = skipped = invalid = 0
    objs: list[Question] = []

    MAX_OPT = 800   # options longer than this are almost certainly parse errors

    for q in data:
        en    = (q.get("question_en") or "").strip()
        topic = (q.get("topic") or "").strip()

        # Field-level check
        opts = {f: (q.get(f) or "").strip() for f in ("option_a", "option_b", "option_c", "option_d")}
        missing = [f for f, v in opts.items() if not v]
        if not en or missing:
            invalid += 1
            continue

        # Discard questions where any option is absurdly long (parser merged multiple questions)
        if any(len(v) > MAX_OPT for v in opts.values()):
            invalid += 1
            continue

        # Duplicate check
        key = (en[:200], topic)
        if key in existing:
            skipped += 1
            continue
        existing.add(key)

        objs.append(
            Question(
                exam            = q.get("exam"),
                subject         = q.get("subject", ""),
                topic           = topic or None,
                question_number = q.get("question_number"),
                question_en     = en[:2000],
                question_hi     = (q.get("question_hi") or None),
                option_a        = opts["option_a"][:800],
                option_b        = opts["option_b"][:800],
                option_c        = opts["option_c"][:800],
                option_d        = opts["option_d"][:800],
                correct_answer  = None,
                difficulty      = None,
                source_pdf      = q.get("source_pdf"),
            )
        )

    if objs:
        db.bulk_save_objects(objs)
        db.commit()
        inserted = len(objs)

    return inserted, skipped, invalid


# ── Main ───────────────────────────────────────────────────────────────────────
def run(verbose: bool) -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    log = setup_logging(verbose)
    t_start = time.perf_counter()

    json_files = sorted(PROCESSED_DIR.rglob("*.json"))
    if not json_files:
        log.error("No JSON files in %s — run extract_questions.py first.", PROCESSED_DIR)
        sys.exit(1)

    log.info("Found %d JSON file(s) in %s", len(json_files), PROCESSED_DIR)

    db = SessionLocal()
    try:
        # Pre-load fingerprints already in DB
        log.info("Loading existing question fingerprints from DB...")
        existing: set[tuple[str, str]] = set(
            db.execute(
                text("SELECT LEFT(question_en, 200), topic FROM questions")
            ).fetchall()
        )
        log.info("  %d questions already in DB", len(existing))

        grand_inserted = grand_skipped = grand_invalid = 0

        for jf in json_files:
            t0  = time.perf_counter()
            rel = jf.relative_to(PROCESSED_DIR)
            try:
                ins, skp, inv = seed_file(jf, existing, db, log)
            except Exception as exc:
                db.rollback()
                log.error("  SKIPPED %s — %s", rel, exc)
                ins = skp = inv = 0
            elapsed = time.perf_counter() - t0

            log.info(
                "  %-55s | inserted=%-4d  skipped=%-4d  invalid=%-4d  (%.2fs)",
                str(rel)[:55],
                ins, skp, inv,
                elapsed,
            )
            grand_inserted += ins
            grand_skipped  += skp
            grand_invalid  += inv

    except Exception as exc:
        db.rollback()
        log.exception("Fatal error: %s", exc)
        raise
    finally:
        db.close()

    total_elapsed = time.perf_counter() - t_start
    log.info("─" * 65)
    log.info("Done in %.1fs", total_elapsed)
    log.info("  Inserted : %d", grand_inserted)
    log.info("  Skipped  : %d (already in DB)", grand_skipped)
    log.info("  Invalid  : %d (missing fields)", grand_invalid)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Seed processed JSONs into PostgreSQL (VidyaAi pipeline Stage 3)"
    )
    parser.add_argument("--verbose", action="store_true", help="Enable DEBUG logging")
    args = parser.parse_args()
    run(args.verbose)


if __name__ == "__main__":
    main()
