#!/usr/bin/env python3
"""
validate_questions.py — VidyaAi PDF Ingestion Pipeline · Stage 2
=================================================================
Reads every JSON from processed/, re-validates each question,
generates a full validation report, and moves invalid questions to
invalid/validation_report.json.

Validation rules:
  ✓ question_en must exist and be at least 10 characters
  ✓ All four options (A, B, C, D) must be non-empty
  ✓ No duplicate questions within the same topic (by question_en[:100])

Usage:
    python scripts/validate_questions.py
    python scripts/validate_questions.py --verbose
"""

import argparse
import json
import logging
import sys
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR      = Path(__file__).resolve().parent.parent
PROCESSED_DIR = BASE_DIR / "processed"
INVALID_DIR   = BASE_DIR / "invalid"
LOGS_DIR      = BASE_DIR / "logs"


# ── Logging ────────────────────────────────────────────────────────────────────
def setup_logging(verbose: bool = False) -> logging.Logger:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_file = LOGS_DIR / f"validate_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    fmt = "%(asctime)s  %(levelname)-8s  %(message)s"
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format=fmt,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_file, encoding="utf-8"),
        ],
    )
    return logging.getLogger("validate")


# ── Validation rules ───────────────────────────────────────────────────────────
def validate_question(q: dict) -> list[str]:
    """Return a list of issue strings. Empty list means the question is valid."""
    issues = []

    en = (q.get("question_en") or "").strip()
    if not en:
        issues.append("question_en is empty")
    elif len(en) < 10:
        issues.append(f"question_en too short ({len(en)} chars)")

    for opt in ("option_a", "option_b", "option_c", "option_d"):
        if not (q.get(opt) or "").strip():
            issues.append(f"{opt} is empty")

    return issues


# ── Main ───────────────────────────────────────────────────────────────────────
def run(verbose: bool) -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    log = setup_logging(verbose)
    t0  = time.perf_counter()

    json_files = sorted(PROCESSED_DIR.rglob("*.json"))
    if not json_files:
        log.error("No JSON files found in %s — run extract_questions.py first.", PROCESSED_DIR)
        sys.exit(1)

    log.info("Validating %d JSON file(s) in %s", len(json_files), PROCESSED_DIR)

    total_checked  = 0
    total_valid    = 0
    total_invalid  = 0
    total_dupes    = 0
    all_invalid:   list[dict] = []

    # Track fingerprints per topic to detect duplicates
    seen: dict[str, set[str]] = defaultdict(set)

    file_stats: list[dict] = []

    for jf in json_files:
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
        except Exception as exc:
            log.error("Cannot read %s: %s", jf, exc)
            continue

        if not isinstance(data, list):
            log.warning("Skipping non-list JSON: %s", jf)
            continue

        file_valid   = 0
        file_invalid = 0
        file_dupes   = 0
        clean: list[dict] = []

        for q in data:
            total_checked += 1
            issues = validate_question(q)

            # Duplicate check within topic
            fingerprint = (q.get("question_en") or "")[:100].strip().lower()
            topic_key   = str(jf.relative_to(PROCESSED_DIR).parent)
            if fingerprint and fingerprint in seen[topic_key]:
                issues.append("duplicate question_en (within topic)")
                total_dupes  += 1
                file_dupes   += 1
            elif fingerprint:
                seen[topic_key].add(fingerprint)

            if issues:
                q["_invalid_reason"] = "; ".join(issues)
                q["_source_file"]    = str(jf.relative_to(BASE_DIR))
                all_invalid.append(q)
                file_invalid += 1
                total_invalid += 1
            else:
                clean.append(q)
                file_valid  += 1
                total_valid += 1

        # Rewrite JSON with only valid questions
        jf.write_text(json.dumps(clean, ensure_ascii=False, indent=2), encoding="utf-8")

        rel = jf.relative_to(PROCESSED_DIR)
        log.info(
            "  %-55s | valid=%-4d  invalid=%-4d  dupes=%-3d",
            str(rel)[:55],
            file_valid,
            file_invalid,
            file_dupes,
        )
        file_stats.append(
            {"file": str(rel), "valid": file_valid, "invalid": file_invalid, "dupes": file_dupes}
        )

    # ── Save invalid report ────────────────────────────────────────────────────
    INVALID_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "generated_at": datetime.now().isoformat(),
        "summary": {
            "files_checked":     len(json_files),
            "questions_checked": total_checked,
            "valid":             total_valid,
            "invalid":           total_invalid,
            "duplicates":        total_dupes,
        },
        "file_stats":        file_stats,
        "invalid_questions": all_invalid,
    }
    report_path = INVALID_DIR / "validation_report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    elapsed = time.perf_counter() - t0
    log.info("─" * 65)
    log.info("Done in %.1fs", elapsed)
    log.info("  Files checked    : %d", len(json_files))
    log.info("  Questions checked: %d", total_checked)
    log.info("  Valid            : %d", total_valid)
    log.info("  Invalid          : %d", total_invalid)
    log.info("  Duplicates       : %d", total_dupes)
    log.info("  Report saved     : %s", report_path.relative_to(BASE_DIR))
    log.info("Run next: python scripts/seed_from_json.py")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate extracted question JSONs (VidyaAi pipeline Stage 2)"
    )
    parser.add_argument("--verbose", action="store_true", help="Enable DEBUG logging")
    args = parser.parse_args()
    run(args.verbose)


if __name__ == "__main__":
    main()
