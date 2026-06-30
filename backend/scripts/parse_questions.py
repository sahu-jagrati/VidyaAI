"""
Parses extracted .txt files into structured JSON.
Output: extracted_text/<subject>/<topic>/<file>.json

Run: python scripts/parse_questions.py
"""
import os
import re
import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTRACTED_DIR = os.path.join(BASE_DIR, "extracted_text")

DEVANAGARI_RE = re.compile(r"[ऀ-ॿ]+")

OPTION_PATTERNS = [
    re.compile(r"^\s*\(?([AaBbCcDd])\)?[).\s]\s*(.+)", re.MULTILINE),
]

QUESTION_SPLIT_RE = re.compile(r"(?m)^\s*(\d+)[.)]\s+")

SOURCE_RE = re.compile(r"\(([A-Z][A-Z0-9 &/\-]{3,60})\)")


def is_mostly_devanagari(line):
    devs = len(DEVANAGARI_RE.findall(line))
    total = len(line.strip())
    if total == 0:
        return False
    return devs / total > 0.3


def clean_english(text):
    lines = text.splitlines()
    kept = []
    for line in lines:
        if is_mostly_devanagari(line):
            continue
        stripped = line.strip()
        if stripped:
            kept.append(stripped)
    return " ".join(kept)


def parse_options(block):
    options = {}
    opt_re = re.compile(
        r"(?:^|\s)\(?([AaBbCcDd])\)?[).]\s*(.+?)(?=\s*\(?[AaBbCcDd]\)?[).]|\Z)",
        re.DOTALL,
    )
    for m in opt_re.finditer(block):
        letter = m.group(1).upper()
        val = clean_english(m.group(2)).strip()
        if val and letter in "ABCD":
            options[letter] = val
    return options


def extract_source(text):
    matches = SOURCE_RE.findall(text)
    known_exams = [
        "SSC", "UPSC", "RRB", "ICAR", "IB ", "DP ", "MTS", "CISF", "CHSL",
        "CPO", "CGL", "GD ", "NDA", "CAT", "BANK",
    ]
    for m in reversed(matches):
        if any(k in m.upper() for k in known_exams):
            return m.strip()
    return None


def split_into_questions(text):
    parts = QUESTION_SPLIT_RE.split(text)
    questions = []
    i = 1
    while i + 1 < len(parts):
        num = int(parts[i])
        body = parts[i + 1]
        questions.append((num, body))
        i += 2
    return questions


def parse_file(txt_path):
    with open(txt_path, encoding="utf-8") as f:
        content = f.read()

    raw_questions = split_into_questions(content)
    parsed = []

    for num, body in raw_questions:
        options = parse_options(body)
        if len(options) < 2:
            continue

        option_block_start = min(
            (body.find(f"({k})") if f"({k})" in body else len(body)) for k in "ABCD"
        )
        opt_starts = [
            body.find(f"({k})") for k in "ABCD" if f"({k})" in body
        ] + [
            body.find(f"{k})") for k in "ABCD" if f"{k})" in body
        ]
        opt_start = min((x for x in opt_starts if x >= 0), default=len(body))

        question_body = body[:opt_start].strip()
        question_en = clean_english(question_body)
        source = extract_source(body)

        if not question_en or len(question_en) < 10:
            continue

        parsed.append(
            {
                "number": num,
                "question_text": question_en,
                "option_a": options.get("A", ""),
                "option_b": options.get("B", ""),
                "option_c": options.get("C", ""),
                "option_d": options.get("D", ""),
                "correct_answer": None,
                "explanation": None,
                "source": source,
            }
        )

    return parsed


def process_all():
    total_files = 0
    total_questions = 0

    for root, dirs, files in os.walk(EXTRACTED_DIR):
        for file in files:
            if not file.endswith(".txt"):
                continue

            txt_path = os.path.join(root, file)
            json_path = txt_path.replace(".txt", ".json")

            try:
                questions = parse_file(txt_path)
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(questions, f, ensure_ascii=False, indent=2)

                rel = os.path.relpath(txt_path, BASE_DIR)
                print(f"  {rel}: {len(questions)} questions → saved JSON")
                total_files += 1
                total_questions += len(questions)
            except Exception as e:
                print(f"  ERROR {file}: {e}")

    print(f"\nDone. {total_files} files, {total_questions} questions parsed.")
    print("Next: run scripts/solve_questions.py to get correct answers via Claude API.")


if __name__ == "__main__":
    process_all()
