"""
scripts/solve_questions.py
Sends every unsolved question through the Anthropic Batch API (50% cheaper),
writes correct_answer + explanation back to the extracted_text JSON files.

Usage:
    set ANTHROPIC_API_KEY=sk-...
    python scripts/solve_questions.py

Estimated cost at default model (claude-opus-4-8) for 16 000 questions:
    ~$28 with Batch API 50% discount.
    Change MODEL to "claude-haiku-4-5" for ~$3 if you prefer cost over quality.
"""

import sys
import os
import json
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── model ─────────────────────────────────────────────────────────────────────
MODEL = "claude-opus-4-8"          # change to "claude-haiku-4-5" for ~10× cheaper

MAX_PER_BATCH = 10_000             # Batch API limit is 100 000; keep slices small
POLL_INTERVAL = 30                  # seconds between status polls

BASE_DIR = Path(__file__).parent.parent
EXTRACTED_DIR = BASE_DIR / "extracted_text"

PROMPT = """\
You are solving a multiple-choice question from an Indian competitive exam (SSC / UPSC / Banking / RRB).

Question: {question}

A) {a}
B) {b}
C) {c}
D) {d}

Reply with ONLY valid JSON — no markdown, no prose:
{{"answer": "A", "explanation": "One concise sentence."}}

The "answer" field must be exactly one letter: A, B, C, or D.\
"""


# ── helpers ───────────────────────────────────────────────────────────────────

def collect_unsolved():
    """Return list of dicts: {path, idx, q} for every question with correct_answer == null."""
    items = []
    for json_path in sorted(EXTRACTED_DIR.rglob("*.json")):
        try:
            data = json.loads(json_path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, list):
            continue
        for i, q in enumerate(data):
            if (
                q.get("correct_answer") is None
                and len(q.get("question_text", "")) > 10
                and q.get("option_a")
                and q.get("option_b")
            ):
                items.append({"path": str(json_path), "idx": i, "q": q})
    return items


def build_requests(items, offset):
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request

    reqs = []
    for i, item in enumerate(items):
        q = item["q"]
        content = PROMPT.format(
            question=q.get("question_text", ""),
            a=q.get("option_a", ""),
            b=q.get("option_b", ""),
            c=q.get("option_c", ""),
            d=q.get("option_d", ""),
        )
        reqs.append(
            Request(
                custom_id=f"q{offset + i}",
                params=MessageCreateParamsNonStreaming(
                    model=MODEL,
                    max_tokens=200,
                    messages=[{"role": "user", "content": content}],
                ),
            )
        )
    return reqs


def wait_for_batch(client, batch_id):
    while True:
        b = client.messages.batches.retrieve(batch_id)
        if b.processing_status == "ended":
            return b
        counts = b.request_counts
        print(
            f"  [{b.processing_status}] "
            f"processing={counts.processing} "
            f"succeeded={counts.succeeded} "
            f"errored={counts.errored}",
            flush=True,
        )
        time.sleep(POLL_INTERVAL)


def apply_results(client, batch_id, items, offset):
    """Pull results and write correct_answer/explanation back to JSON files."""
    by_id = {f"q{offset + i}": item for i, item in enumerate(items)}

    # pre-load every file we might touch
    file_cache = {}
    for item in items:
        p = item["path"]
        if p not in file_cache:
            file_cache[p] = json.loads(Path(p).read_text(encoding="utf-8"))

    ok = err = 0
    for result in client.messages.batches.results(batch_id):
        cid = result.custom_id
        if cid not in by_id:
            continue

        item = by_id[cid]

        if result.result.type == "succeeded":
            text = next(
                (b.text for b in result.result.message.content if b.type == "text"),
                "",
            ).strip()
            try:
                parsed = json.loads(text)
                answer = str(parsed.get("answer", "")).strip().upper()
                expl = str(parsed.get("explanation", "")).strip()
                if answer in ("A", "B", "C", "D"):
                    row = file_cache[item["path"]][item["idx"]]
                    row["correct_answer"] = answer
                    row["explanation"] = expl[:600]
                    ok += 1
                    continue
            except (json.JSONDecodeError, KeyError, TypeError):
                pass

        err += 1

    # persist changes
    for p, data in file_cache.items():
        Path(p).write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    return ok, err


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: set the ANTHROPIC_API_KEY environment variable first.")
        sys.exit(1)

    import anthropic
    client = anthropic.Anthropic(api_key=api_key)

    print(f"Model : {MODEL}")
    print(f"Dir   : {EXTRACTED_DIR}")
    print("Scanning for unsolved questions...")
    items = collect_unsolved()
    total = len(items)
    print(f"Found : {total} unsolved questions\n")

    if not total:
        print("Nothing to solve. Run seed_from_json.py next.")
        return

    chunks = [items[s : s + MAX_PER_BATCH] for s in range(0, total, MAX_PER_BATCH)]
    grand_ok = grand_err = 0

    for n, chunk in enumerate(chunks, 1):
        offset = (n - 1) * MAX_PER_BATCH
        print(f"=== Batch {n}/{len(chunks)}: {len(chunk)} questions ===")

        reqs = build_requests(chunk, offset)
        print("  Submitting...", flush=True)
        batch = client.messages.batches.create(requests=reqs)
        print(f"  Batch ID : {batch.id}", flush=True)

        print(f"  Polling every {POLL_INTERVAL}s...", flush=True)
        done = wait_for_batch(client, batch.id)
        c = done.request_counts
        print(f"  Complete : succeeded={c.succeeded}  errored={c.errored}", flush=True)

        ok, err = apply_results(client, batch.id, chunk, offset)
        grand_ok += ok
        grand_err += err
        print(f"  Written  : {ok} answers  |  {err} parse failures\n", flush=True)

    print(f"All done. {grand_ok} answers filled, {grand_err} failures.")
    print("Next step: python scripts/seed_from_json.py")


if __name__ == "__main__":
    main()
