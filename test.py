import json

for path in [
    "data/MMLongBench/samples.json",
    "data/MMLongBench/sample-with-retrieval-results.json",
    "results/MMLongBench/mmlb-MDocAgent/2026-04-26-03-13_results.json",
]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("\n", path)
    print("num samples:", len(data))
    print("has page_ids:", sum("page_ids" in x for x in data))
    print("has evidence_pages:", sum("evidence_pages" in x for x in data))
    print("keys example:", data[0].keys())