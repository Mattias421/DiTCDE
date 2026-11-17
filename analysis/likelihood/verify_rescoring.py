"""Reproduce Grad-TTS rescoring WER and compare it with uniform selection.

Uses only the Python standard library. Inputs are pinned repository CSVs, not
fresh synthesis runs. Optional SCTK executables provide the MAPSSWE test.
"""

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import re
import subprocess
import urllib.request

REVISION = "0461902c90b1ed85980f7174f325e1a9a6a6ee7a"
INPUTS = {
    "wav2vec2": ("wav2vec2/gtts_ll_w2v.csv", "w2v_hyp", "w2v_score"),
    "whisper_base": ("wspr/gtts_ll_base.csv", "wspr_hyp", "wspr_prob"),
}


def edit_distance(reference, hypothesis):
    previous = list(range(len(hypothesis) + 1))
    for i, word in enumerate(reference, 1):
        current = [i]
        for j, other in enumerate(hypothesis, 1):
            current.append(min(previous[j] + 1, current[j - 1] + 1,
                               previous[j - 1] + (word != other)))
        previous = current
    return previous[-1]


def analyse(name, raw, hyp_key, score_key, out_dir, sctk_bin):
    groups = defaultdict(list)
    for row in csv.DictReader(io.StringIO(raw.decode())):
        groups[row["audio_path"]].append(row)
    records = []
    # Integer convolution counts all independent uniform candidate selections
    # exactly. Duplicate transcript rows retain their multiplicity.
    random_counts = Counter({0: 1})
    denominator = 1
    for audio_path, candidates in sorted(groups.items()):
        reference = candidates[0]["reference"]
        assert all(row["reference"] == reference for row in candidates)
        for row in candidates:
            row["errors"] = edit_distance(reference.split(), row[hyp_key].split())
        am = max(candidates, key=lambda row: float(row[score_key]))
        ll = max(candidates, key=lambda row: float(row["gtts_ll"]))
        histogram = Counter(row["errors"] for row in candidates)
        new_counts = Counter()
        for total, count in random_counts.items():
            for errors, frequency in histogram.items():
                new_counts[total + errors] += count * frequency
        denominator *= len(candidates)
        random_counts = new_counts
        records.append({
            "id": Path(audio_path).stem, "reference": reference,
            "words": len(reference.split()), "candidate_count": len(candidates),
            "am_hypothesis": am[hyp_key], "ll_hypothesis": ll[hyp_key],
            "am_errors": am["errors"], "ll_errors": ll["errors"],
            "oracle_best_errors": min(histogram),
            "oracle_worst_errors": max(histogram),
            "stored_wer_oracle_best_errors": min(candidates, key=lambda row: float(row["wer"]))["errors"],
            "stored_wer_oracle_worst_errors": max(candidates, key=lambda row: float(row["wer"]))["errors"],
            "random_expected_errors": sum(e * n for e, n in histogram.items()) / len(candidates),
        })
    assert sum(random_counts.values()) == denominator
    words = sum(row["words"] for row in records)
    totals = {key: sum(row[key] for row in records) for key in (
        "am_errors", "ll_errors", "oracle_best_errors", "oracle_worst_errors",
        "stored_wer_oracle_best_errors", "stored_wer_oracle_worst_errors",
        "random_expected_errors")}
    # Lower tail: how often does uniform selection achieve as few or fewer
    # total word errors than the likelihood-selected hypotheses?
    exact_p = sum(count for e, count in random_counts.items()
                  if e <= totals["ll_errors"]) / denominator
    result = {
        "repository_revision": REVISION,
        "input_sha256_lf": hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest(),
        "normalisation": "Whitespace tokenisation of saved reference and hypothesis strings; no further text normalisation.",
        "tie_break": "First row in original CSV for tied maximum scores.",
        "recordings": len(records), "reference_words": words,
        "candidate_rows": sum(row["candidate_count"] for row in records),
        "candidate_count_histogram": dict(sorted(Counter(row["candidate_count"] for row in records).items())),
        "errors": totals,
        "wer_percent": {key.removesuffix("_errors"): value / words * 100
                        for key, value in totals.items()},
        "uniform_random_test": {
            "null": "Independent uniform selection of one saved candidate row per recording.",
            "alternative": "Likelihood selection has fewer total word errors.",
            "tail": "P(E_random <= E_likelihood), including ties", "p": exact_p,
        },
        "recording_results": records,
    }
    report_dir = out_dir / name
    report_dir.mkdir(parents=True, exist_ok=True)
    for label, key in (("ref", "reference"), ("am", "am_hypothesis"), ("ll", "ll_hypothesis")):
        with (report_dir / f"{label}.trn").open("w") as stream:
            for row in records:
                stream.write(f"{row[key]} (speaker_{row['id']})\n")
    if sctk_bin:
        for label in ("am", "ll"):
            cmd = [str(sctk_bin / "sclite"), "-r", str(report_dir / "ref.trn"), "trn",
                   "-h", str(report_dir / f"{label}.trn"), "trn", "-i", "wsj",
                   "-o", "sgml", "-O", str(report_dir), "-n", label]
            subprocess.run(cmd, check=True, capture_output=True, text=True)
        sgml = "".join((report_dir / f"{label}.sgml").read_text() for label in ("am", "ll"))
        cmd = [str(sctk_bin / "sc_stats"), "-p", "-t", "mapsswe", "-v",
               "-n", str(report_dir / "comparison")]
        process = subprocess.run(cmd, input=sgml, capture_output=True, text=True, check=True)
        (report_dir / "sc_stats.stdout.txt").write_text(process.stdout)
        (report_dir / "sc_stats.stderr.txt").write_text(process.stderr)
        result["sctk"] = {"command": cmd, "report": str(report_dir / "comparison.stats.mapsswe")}
        report = (report_dir / "comparison.stats.mapsswe").read_text()
        result["sctk"]["summary_lines"] = [line for line in report.splitlines()
                                           if re.search(r"MTCH_PR|Z_stat|Z-stat|Significant|segm", line)]
        match = re.search(r"\(Z Stat:\s*([-\d.]+)\)", report)
        if match:
            z = float(match[1])
            result["sctk"]["z_reported"] = z
            result["sctk"]["two_sided_p_approx_from_rounded_z"] = math.erfc(abs(z) / math.sqrt(2))
        # Check SCTK's independently aligned error totals against the Python
        # word edit distances before using the comparison's significance.
        totals_match = re.search(r"Totals\s+(\d+)\s+(\d+)\s+(\d+)", report)
        assert totals_match is not None
        assert int(totals_match[2]) == totals["am_errors"]
        assert int(totals_match[3]) == totals["ll_errors"]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--sctk-bin", type=Path)
    args = parser.parse_args()
    args.data_dir.mkdir(parents=True, exist_ok=True)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    results = {}
    for name, (path, hyp_key, score_key) in INPUTS.items():
        local_path = args.data_dir / Path(path).name
        if not local_path.exists():
            url = f"https://raw.githubusercontent.com/Mattias421/diff_ll_audio/{REVISION}/{path}"
            local_path.write_bytes(urllib.request.urlopen(url, timeout=60).read())
        results[name] = analyse(name, local_path.read_bytes(), hyp_key, score_key,
                                args.output_dir.resolve(), args.sctk_bin)
        results[name]["source_path"] = path
    (args.output_dir / "rescoring_verification.json").write_text(json.dumps(results, indent=2) + "\n")
    for name, result in results.items():
        print(name, json.dumps({"wer_percent": result["wer_percent"],
                                "p_uniform": result["uniform_random_test"]["p"],
                                "sctk": result.get("sctk")}, indent=2))


if __name__ == "__main__":
    main()
