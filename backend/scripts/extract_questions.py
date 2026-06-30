#!/usr/bin/env python3
"""
extract_questions.py — VidyaAi PDF Ingestion Pipeline · Stage 1
================================================================
Recursively scans data/questions/<subject>/<topic>/*.pdf.

For each PDF:
  1. Computes SHA-256 hash → checks processed_files DB table.
     If hash exists and PDF unchanged → SKIP (no re-processing).
  2. Extracts text with PyMuPDF.
  3. Parses numbered question blocks (English + Hindi separately).
  4. Saves one JSON per PDF  →  processed/<subject>/<topic>/<name>.json
  5. Saves invalid questions →  invalid/<subject>/<topic>/<name>_invalid.json
  6. Records the file hash in the processed_files table.

Usage:
    python scripts/extract_questions.py
    python scripts/extract_questions.py --exam "SSC CGL"
    python scripts/extract_questions.py --force          # reprocess even if unchanged
    python scripts/extract_questions.py --verbose
"""

import argparse
import hashlib
import json
import logging
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import fitz  # PyMuPDF

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.database.connection import SessionLocal
from app.models.processed_file_model import ProcessedFile

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR      = Path(__file__).resolve().parent.parent
DATA_DIR      = BASE_DIR / "data" / "questions"
PROCESSED_DIR = BASE_DIR / "processed"
INVALID_DIR   = BASE_DIR / "invalid"
LOGS_DIR      = BASE_DIR / "logs"

# ── Display name maps ──────────────────────────────────────────────────────────
SUBJECT_MAP: dict[str, str] = {
    "quant":             "Quant",
    "reasoning":         "Reasoning",
    "english":           "English",
    "general_awareness": "General Awareness",
}

TOPIC_MAP: dict[str, str] = {
    # Quant — canonical snake_case keys
    "profit_loss":             "Profit & Loss",
    "percentage":              "Percentage",
    "ratio":                   "Ratio",
    "ratio_and_proportion":    "Ratio & Proportion",
    "average":                 "Average",
    "time_and_work":           "Time & Work",
    "pipe_cistern":            "Pipe & Cistern",
    "train_sheet":             "Train Sheet",
    "simple_interest":         "Simple Interest",
    "compound_interest":       "Compound Interest",
    "mixture_alligation":      "Mixture & Alligation",
    "partnership":             "Partnership",
    "discount":                "Discount",
    "data_interpretation":     "Data Interpretation",
    "probability":             "Probability",
    "permutation_combination": "Permutation & Combination",
    "boat_stream":             "Boat & Stream",
    "coordinate_geometry":     "Coordinate Geometry",
    "number_system":           "Number System",
    "speed_time_distance":     "Speed, Time & Distance",
    "geometry":                "Geometry",
    "mensuration_2d":          "Mensuration 2D",
    "mensuration_3d":          "Mensuration 3D",
    "algebra":                 "Algebra",
    # Quant — PascalCase / alternate spellings found on disk
    "profit_and_loss":                "Profit & Loss",
    "boat_and_stream":                "Boat & Stream",
    "mixture_and_alligation":         "Mixture & Alligation",
    "permutation_and_combination":    "Permutation & Combination",
    "pipes_and_cistern":              "Pipe & Cistern",
    "problem_on_ages_sheet":          "Problem on Ages",
    "simple_interes":                 "Simple Interest",   # folder typo
    "surf_and_indices":               "Surds & Indices",
    "trignometry":                    "Trigonometry",      # folder typo
    "maxima_and_minima":              "Maxima & Minima",
    "time_speed_distance":            "Speed, Time & Distance",
    "height_and_distance":            "Height & Distance",
    "lcm_hcf":                        "LCM & HCF",
    "quadratic_equations":            "Quadratic Equations",
    "race_sheet":                     "Race",
    "simplification":                 "Simplification",
    "statistics":                     "Statistics",
    "trigonometry":            "Trigonometry",
    "lcm_hcf":                 "LCM & HCF",
    "simplification":          "Simplification",
    "statistics":              "Statistics",
    "quadratic_equations":     "Quadratic Equations",
    "surds_indices":           "Surds & Indices",
    "ap_gp_hp":                "AP, GP & HP",
    "height_distance":         "Height & Distance",
    "maxima_minima":           "Maxima & Minima",
    "race_sheet":              "Race",
    "problem_on_ages":         "Problem on Ages",
    "dishonest_shopkeeper":    "Dishonest Shopkeeper",
    # Reasoning
    "analogy":                 "Analogy",
    "classification":          "Classification",
    "series":                  "Series",
    "blood_relation":          "Blood Relation",
    "direction_distance":      "Direction & Distance",
    "coding_decoding":         "Coding-Decoding",
    "alphabet":                "Alphabet",
    "syllogism":               "Syllogism",
    "inequality":              "Inequality",
    "ranking":                 "Ranking",
    "seating_arrangement":     "Seating Arrangement",
    "puzzle":                  "Puzzle",
    "calendar":                "Calendar",
    "clock":                   "Clock",
    "dice":                    "Dice",
    "cube_cuboid":             "Cube & Cuboid",
    "venn_diagram":            "Venn Diagram",
    "non_verbal":              "Non-Verbal Reasoning",
    "counting_figures":        "Counting Figures",
    "number_series":           "Number Series",
    "letter_series":           "Letter Series",
    "missing_number":          "Missing Number",
    "pair_formation":          "Pair Formation",
    "analytical_reasoning":    "Analytical Reasoning",
    "assertion_reason":        "Assertion & Reason",
    "statement_argument":      "Statement & Argument",
    "assumptions":             "Assumptions",
    "cause_effect":            "Cause & Effect",
    "course_of_action":        "Course of Action",
    "decision_making":         "Decision Making",
    "data_sufficiency":        "Data Sufficiency",
    "coded_equation":          "Coded Equation",
    "word_based":              "Word-Based Problems",
    # Reasoning — PascalCase / alternate folder names found on disk
    "assertion_and_reason":               "Assertion & Reason",
    "cause_and_effect":                   "Cause & Effect",
    "cube_and_cuboid":                    "Cube & Cuboid",
    "direction_and_distance":             "Direction & Distance",
    "dictionary_jumbling_wordformation":  "Dictionary & Word Formation",
    "police_dice_cube_cuboid":            "Cube & Cuboid",
    "teaching_dice_cube_cuboid":          "Cube & Cuboid",
    "upsc_csat_dice_cube_cuboid":         "Cube & Cuboid",
    "statement_assumption_and_conclusion":"Statement & Assumption",
    "coding_decoding":                    "Coding-Decoding",
    "blood_relation":                     "Blood Relation",
    # English
    "synonym":                 "Synonym",
    "antonym":                 "Antonym",
    "idioms":                  "Idioms & Phrases",
    "error_detection":         "Error Detection",
    "fill_blanks":             "Fill in the Blanks",
    "reading_comprehension":   "Reading Comprehension",
    "sentence_improvement":    "Sentence Improvement",
    "one_word_substitution":   "One Word Substitution",
    "spelling":                "Spelling",
    "cloze_test":              "Cloze Test",
    # General Awareness
    "history":                 "History",
    "polity":                  "Polity",
    "geography":               "Geography",
    "science":                 "Science",
    "current_affairs":         "Current Affairs",
    "economy":                 "Economy",
    "static_gk":               "Static GK",
    "sports":                  "Sports",
    "art_culture":             "Art & Culture",
}

# ── Regex patterns ─────────────────────────────────────────────────────────────
DEVANAGARI_RE = re.compile(r"[ऀ-ॿ]")
QUESTION_RE   = re.compile(r"(?m)^\s*(\d{1,3})[.)]\s+")
# Match first option marker (A / a) to find where options begin
OPT_FIRST_RE  = re.compile(r"(?:^|\n)\s*\(?[Aa]\)?[).]\s", re.MULTILINE)
# Extract individual option values
OPT_EACH_RE   = re.compile(
    r"\(?([A-Da-d])\)?[).]\s*(.+?)(?=\s*\(?[A-Da-d]\)?[).]|\Z)",
    re.DOTALL,
)
# Lines to discard (solutions, headers, watermarks, page numbers)
NOISE_RE      = re.compile(
    r"(?i)^(solution|answer\s*key|page\s*\d+|\d+\s*$|©|www\.|http|tel:|adda247)",
    re.MULTILINE,
)


# ── Logging ────────────────────────────────────────────────────────────────────
def setup_logging(verbose: bool = False) -> logging.Logger:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_file = LOGS_DIR / f"extract_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    fmt = "%(asctime)s  %(levelname)-8s  %(message)s"
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format=fmt,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_file, encoding="utf-8"),
        ],
    )
    return logging.getLogger("extract")


# ── Hash helper ────────────────────────────────────────────────────────────────
def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ── Text extraction ────────────────────────────────────────────────────────────
def extract_pdf_text(pdf_path: Path) -> str:
    doc   = fitz.open(str(pdf_path))
    pages = [page.get_text() for page in doc]
    doc.close()
    return "\n".join(pages)


# ── Parsing helpers ────────────────────────────────────────────────────────────
def is_devanagari_line(line: str, threshold: float = 0.3) -> bool:
    chars = [c for c in line if not c.isspace()]
    if not chars:
        return False
    deva = sum(1 for c in chars if DEVANAGARI_RE.match(c))
    return deva / len(chars) > threshold


def separate_en_hi(text: str) -> tuple[str, str]:
    """Split mixed text into (english, hindi) strings."""
    en_lines: list[str] = []
    hi_lines: list[str] = []
    for line in text.splitlines():
        s = line.strip()
        if not s or NOISE_RE.match(s):
            continue
        if is_devanagari_line(s):
            hi_lines.append(s)
        else:
            en_lines.append(s)
    return " ".join(en_lines).strip(), " ".join(hi_lines).strip()


def parse_options(options_text: str) -> dict[str, str]:
    """Extract A–D option values from the options section of a question block."""
    options: dict[str, str] = {}
    for m in OPT_EACH_RE.finditer(options_text):
        letter = m.group(1).upper()
        if letter not in "ABCD":
            continue
        raw    = m.group(2)
        en, _  = separate_en_hi(raw)         # keep English only
        val    = " ".join(en.split())         # normalize whitespace
        if val:
            options[letter] = val
    return options


def parse_block(num: int, block: str) -> dict | None:
    """Parse a single question block into a structured dict. Returns None if unparseable."""
    # Find where options section begins
    opt_match = OPT_FIRST_RE.search(block)
    if not opt_match:
        return None

    body_text    = block[: opt_match.start()]
    options_text = block[opt_match.start():]

    question_en, question_hi = separate_en_hi(body_text)
    options                  = parse_options(options_text)

    return {
        "question_number": num,
        "question_en":     question_en,
        "question_hi":     question_hi or None,
        "option_a":        options.get("A", ""),
        "option_b":        options.get("B", ""),
        "option_c":        options.get("C", ""),
        "option_d":        options.get("D", ""),
    }


def parse_questions(text: str) -> list[dict]:
    """Split full PDF text into numbered blocks and parse each one."""
    parts   = QUESTION_RE.split(text)
    results = []
    i = 1
    while i + 1 < len(parts):
        try:
            num   = int(parts[i])
            block = parts[i + 1]
        except (ValueError, IndexError):
            i += 2
            continue
        parsed = parse_block(num, block)
        if parsed:
            results.append(parsed)
        i += 2
    return results


# ── Validation ─────────────────────────────────────────────────────────────────
def validate(q: dict) -> list[str]:
    """Return list of missing/invalid fields. Empty list = valid."""
    issues = []
    if not q.get("question_en"):
        issues.append("missing question_en")
    for opt in ("option_a", "option_b", "option_c", "option_d"):
        if not q.get(opt):
            issues.append(f"missing {opt}")
    return issues


# ── PDF processor ──────────────────────────────────────────────────────────────
def process_pdf(
    pdf_path:    Path,
    exam:        str,
    subject_key: str,
    topic_key:   str,
    log:         logging.Logger,
) -> tuple[int, int]:
    """
    Extract, validate, and save questions from one PDF.
    Returns (n_valid, n_invalid).
    """
    subject = SUBJECT_MAP.get(subject_key, subject_key.replace("_", " ").title())
    topic   = TOPIC_MAP.get(topic_key,   topic_key.replace("_", " ").title())

    text      = extract_pdf_text(pdf_path)
    questions = parse_questions(text)

    valid:   list[dict] = []
    invalid: list[dict] = []

    for q in questions:
        q.update(
            exam=exam,
            subject=subject,
            topic=topic,
            source_pdf=pdf_path.name,
            correct_answer=None,
            difficulty=None,
        )
        issues = validate(q)
        if issues:
            q["_invalid_reason"] = "; ".join(issues)
            invalid.append(q)
        else:
            valid.append(q)

    # ── Save valid JSON ────────────────────────────────────────────────────────
    out_dir  = PROCESSED_DIR / subject_key / topic_key
    out_dir.mkdir(parents=True, exist_ok=True)
    out_name = re.sub(r"[^\w]+", "_", pdf_path.stem).strip("_").lower() + ".json"
    out_path = out_dir / out_name
    out_path.write_text(
        json.dumps(valid, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # ── Save invalid JSON ──────────────────────────────────────────────────────
    if invalid:
        inv_dir  = INVALID_DIR / subject_key / topic_key
        inv_dir.mkdir(parents=True, exist_ok=True)
        (inv_dir / out_name.replace(".json", "_invalid.json")).write_text(
            json.dumps(invalid, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    log.info(
        "  %-52s | extracted=%d  valid=%d  invalid=%d",
        pdf_path.name[:52],
        len(questions),
        len(valid),
        len(invalid),
    )
    return len(valid), len(invalid)


# ── Main ───────────────────────────────────────────────────────────────────────
def run(exam: str, force: bool, verbose: bool) -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    log = setup_logging(verbose)
    t0  = time.perf_counter()

    if not DATA_DIR.exists():
        log.error("DATA_DIR not found: %s", DATA_DIR)
        sys.exit(1)

    pdfs = sorted(DATA_DIR.rglob("*.pdf"))
    if not pdfs:
        log.error("No PDFs found under %s", DATA_DIR)
        sys.exit(1)

    log.info("Exam      : %s", exam)
    log.info("PDFs found: %d", len(pdfs))

    # Load already-processed hashes from DB
    db = SessionLocal()
    try:
        known_hashes: set[str] = {
            row.file_hash
            for row in db.query(ProcessedFile.file_hash).all()
        }
    finally:
        db.close()

    total_valid = total_invalid = skipped = 0

    for pdf in pdfs:
        # Determine subject/topic from folder hierarchy
        # Expected layout: data/questions/<subject>/<topic>/<file>.pdf
        parts = pdf.relative_to(DATA_DIR).parts
        if len(parts) < 3:
            log.warning("Skipping (unexpected path depth): %s", pdf)
            continue
        subject_key = parts[0].lower()
        topic_key   = parts[1].lower()

        # Hash-based skip check
        file_hash = sha256_file(pdf)
        if not force and file_hash in known_hashes:
            log.debug("SKIP (unchanged): %s", pdf.name)
            skipped += 1
            continue

        log.info("Processing: %s/%s/%s", subject_key, topic_key, pdf.name)
        try:
            v, i = process_pdf(pdf, exam, subject_key, topic_key, log)
            total_valid   += v
            total_invalid += i
        except Exception:
            log.exception("ERROR: %s", pdf)
            continue

        # Record hash in DB
        db = SessionLocal()
        try:
            existing = db.query(ProcessedFile).filter_by(file_hash=file_hash).first()
            if existing:
                existing.file_name    = pdf.name
                existing.processed_at = __import__("datetime").datetime.now(
                    __import__("datetime").timezone.utc
                )
            else:
                db.add(ProcessedFile(file_name=pdf.name, file_hash=file_hash))
            db.commit()
        except Exception:
            db.rollback()
            log.warning("Could not record hash for %s", pdf.name)
        finally:
            db.close()

    elapsed = time.perf_counter() - t0
    log.info("─" * 65)
    log.info(
        "Done in %.1fs — valid=%d  invalid=%d  skipped(unchanged)=%d",
        elapsed, total_valid, total_invalid, skipped,
    )
    log.info("JSON saved to : %s", PROCESSED_DIR)
    log.info("Invalid saved : %s", INVALID_DIR)
    log.info("Run next      : python scripts/validate_questions.py")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract questions from PDFs into JSON (VidyaAi pipeline Stage 1)"
    )
    parser.add_argument(
        "--exam",    default="SSC CGL",
        help="Exam name tag written to every question (default: SSC CGL)",
    )
    parser.add_argument(
        "--force",   action="store_true",
        help="Reprocess PDFs even if their hash is already in the DB",
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Enable DEBUG-level logging",
    )
    args = parser.parse_args()
    run(args.exam, args.force, args.verbose)


if __name__ == "__main__":
    main()
