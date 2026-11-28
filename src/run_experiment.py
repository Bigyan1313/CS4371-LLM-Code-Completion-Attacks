"""Run the test inputs through the code tool and score the results.

For now this runs with no defense, to see how often the attacks work on
their own. The input and output filters will be added as more defense
options later.

Examples (run from the repo folder):
    python3 src/run_experiment.py                  # completion mode, main model, temperature 0
    python3 src/run_experiment.py --mode chat      # chat mode instead (see code_tool.py)
    python3 src/run_experiment.py --show           # also print every answer
    python3 src/run_experiment.py --model qwen2.5-coder:3b --temperature 0.7
    python3 src/run_experiment.py --only A01 N04   # run just some cases

Each run saves a CSV file in the results/ folder.
"""

import argparse
import csv
import os
import sys
from collections import Counter

import code_tool
import model_client
from leak_check import find_leak
from test_inputs import ALL_CASES, language

RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
DEFENSES = ["none"]  # "input", "output" and "both" get added with the filters

CSV_COLUMNS = [
    "mode", "model", "temperature", "defense", "case_id", "kind", "language", "spot",
    "encoding", "file_name", "blocked", "leaked", "leak_method", "seconds", "output",
]


def run_case(case, mode, model, temperature, defense):
    """Run one case and return a result row for the CSV."""
    result = code_tool.complete(case, model=model, temperature=temperature, mode=mode)
    leak = find_leak(result["text"])
    return {
        "mode": mode,
        "model": model,
        "temperature": temperature,
        "defense": defense,
        "case_id": case["id"],
        "kind": case["kind"],
        "language": language(case),
        "spot": case["spot"],
        "encoding": case["encoding"],
        "file_name": case["file_name"],
        "blocked": "no",  # nothing is blocked until the filters exist
        "leaked": "yes" if leak else "no",
        "leak_method": leak or "",
        "seconds": result["seconds"],
        "output": result["text"],
    }


def save_csv(rows, mode, model, temperature, defense, partial=False):
    """Save the rows to results/<mode>__<defense>__<model>__t<temperature>.csv and return the path.

    Partial runs (--only) get "__partial" added, so they never overwrite a full run.
    """
    os.makedirs(RESULTS_DIR, exist_ok=True)
    safe_model = model.replace(":", "-").replace("/", "-")
    suffix = "__partial" if partial else ""
    path = os.path.join(RESULTS_DIR, f"{mode}__{defense}__{safe_model}__t{temperature}{suffix}.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    return os.path.normpath(path)


def print_summary(rows):
    """Print how many attacks got through and how many normal requests were blocked."""
    attacks = [r for r in rows if r["kind"] == "attack"]
    normals = [r for r in rows if r["kind"] == "normal"]

    if attacks:
        leaked = [r for r in attacks if r["leaked"] == "yes"]
        print(f"\nAttacks that got the canary word out: {len(leaked)} of {len(attacks)} "
              f"({100 * len(leaked) / len(attacks):.0f}%)")
        by_spot = Counter(r["spot"] for r in attacks)
        leaked_by_spot = Counter(r["spot"] for r in leaked)
        for spot in sorted(by_spot):
            print(f"  {spot:<16} {leaked_by_spot[spot]} of {by_spot[spot]}")
    if normals:
        blocked = sum(r["blocked"] == "yes" for r in normals)
        print(f"Normal requests wrongly blocked: {blocked} of {len(normals)}")
        odd = [r["case_id"] for r in normals if r["leaked"] == "yes"]
        if odd:
            print(f"Normal requests where the canary word showed up anyway: {', '.join(odd)}")


def main():
    parser = argparse.ArgumentParser(description="Run the test inputs and score the results.")
    parser.add_argument("--mode", choices=code_tool.MODES, default="completion",
                        help="completion = like autocomplete (default); chat = like ChatGPT")
    parser.add_argument("--model", default=model_client.MAIN_MODEL)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--defense", choices=DEFENSES, default="none")
    parser.add_argument("--only", nargs="+", metavar="ID", help="run only these case IDs, e.g. A01 N04")
    parser.add_argument("--show", action="store_true", help="print every answer the model gives")
    args = parser.parse_args()

    cases = ALL_CASES
    if args.only:
        wanted = {case_id.upper() for case_id in args.only}
        cases = [c for c in ALL_CASES if c["id"] in wanted]
        if not cases:
            print("No cases match those IDs.")
            return 1

    print(f"Mode: {args.mode}, model {args.model}, temperature {args.temperature}, defense: {args.defense}\n")
    rows = []
    for number, case in enumerate(cases, start=1):
        try:
            row = run_case(case, args.mode, args.model, args.temperature, args.defense)
        except model_client.OllamaError as err:
            print(f"FAIL  {err}")
            return 1
        rows.append(row)

        if case["kind"] == "attack":
            status = f"LEAKED ({row['leak_method']})" if row["leaked"] == "yes" else "held"
        else:
            status = "answered" if row["leaked"] == "no" else f"answered, but canary showed up ({row['leak_method']})"
        print(f"[{number:2}/{len(cases)}] {case['id']}  {case['kind']:<6}  {status}  ({row['seconds']}s)")
        if args.show:
            print("      " + row["output"].strip().replace("\n", "\n      ") + "\n")

    print_summary(rows)
    path = save_csv(rows, args.mode, args.model, args.temperature, args.defense, partial=bool(args.only))
    print(f"\nSaved {len(rows)} results to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
