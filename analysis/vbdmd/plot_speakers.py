"""Plot verified speaker-subset results from a refreshed Mimas chapter report."""
import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path
from statistics import mean

import matplotlib.pyplot as plt

METRICS = dict(PESQ="PESQ", ESTOI="ESTOI", SI_SDR="SI-SDR (dB)",
               DNSMOS_P808="DNSMOS P.808", WhiSQA_MOS="WhiSQA")
SUBSETS = dict(single=1, very_low=3, low=7, medium=13, full=26)
FAMILIES = [
    ("icfm", "ode50", "ICFM (50 NFE)"),
    ("sbve", "ode50", "SB-VE (50 NFE)"),
    ("sgmseplus", "pc50", "SGMSE+ (100 NFE)"),
]


def load_csv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    scores = defaultdict(dict)
    for row in load_csv(args.report / "per_utterance.csv"):
        items = scores[row["configuration"]]
        if row["rel"] in items:
            raise ValueError(f"Duplicate score: {row['configuration']} {row['rel']}")
        items[row["rel"]] = row
    coverage = {r["configuration"]: r for r in load_csv(args.report / "coverage.csv")}
    noisy = scores["noisy"]
    if len(noisy) != 824:
        raise ValueError("Expected 824 noisy test utterances")
    fig, axes = plt.subplots(2, 3, figsize=(9, 4.8), layout="constrained")
    for ax, (metric, title) in zip(axes.flat, METRICS.items()):
        for family, sampler, label in FAMILIES:
            changes = []
            for subset in SUBSETS:
                key = f"stanage_data_{family}_{subset}_{sampler}"
                if coverage[key]["status"] != "verified":
                    changes.append(math.nan)
                    continue
                if scores[key].keys() != noisy.keys():
                    raise ValueError(f"Test IDs do not match: {key}")
                deltas = [float(scores[key][uid][metric]) - float(row[metric])
                          for uid, row in noisy.items()]
                if not all(map(math.isfinite, deltas)):
                    raise ValueError(f"Non-finite score: {key} {metric}")
                changes.append(mean(deltas))
            ax.plot(list(SUBSETS.values()), changes, "o-", label=label)
        ax.set(title=title, xticks=list(SUBSETS.values()))
        if not any(math.isfinite(y) for line in ax.lines for y in line.get_ydata()):
            ax.set_yticks([])
            ax.text(.5, .5, "Evaluation pending", transform=ax.transAxes,
                    ha="center", va="center")
        ax.grid(alpha=.2)
    axes.flat[-1].axis("off")
    axes.flat[-1].legend(*axes.flat[0].get_legend_handles_labels(),
                         loc="center", frameon=False)
    fig.supxlabel("Training speakers")
    fig.supylabel("Mean paired change from noisy speech")
    fig.savefig(args.output)


if __name__ == "__main__":
    main()
