"""
Analyze Layer 1.A finalized coding batch.

This script reads the finalized master coding dataset and generates
analysis-ready result tables and figures for the Layer 1.A response-regulation experiment.

Expected input:
    data/coded/layer1a_master_coding_batch.csv

Generated outputs:
    results/tables/
    results/figures/
"""

from pathlib import Path
import json
import re
import pandas as pd
import matplotlib.pyplot as plt


def pf_key(pf: str) -> int:
    match = re.search(r"(\d+)", str(pf))
    return int(match.group(1)) if match else 999


def counts_as_string(series: pd.Series) -> str:
    counts = series.value_counts().sort_index()
    return "; ".join(f"{k}={v}" for k, v in counts.items() if str(k) != "")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    input_csv = repo_root / "data" / "coded" / "layer1a_master_coding_batch.csv"
    tables_dir = repo_root / "results" / "tables"
    figures_dir = repo_root / "results" / "figures"

    tables_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(input_csv)

    for col in [
        "dominant_signature",
        "secondary_signatures",
        "failure_mode_type",
        "prompt_family",
        "prompt_variant",
    ]:
        if col in df.columns:
            df[col] = df[col].fillna("").astype(str).str.strip()

    df["intensity_score"] = pd.to_numeric(df["intensity_score"], errors="coerce")
    df["failure_mode_flag"] = (
        pd.to_numeric(df["failure_mode_flag"], errors="coerce")
        .fillna(0)
        .astype(int)
    )

    pf_order = sorted(df["prompt_family"].unique(), key=pf_key)

    # Prompt-family overview
    pf_overview_rows = []
    for pf in pf_order:
        sub = df[df["prompt_family"] == pf]
        pf_overview_rows.append(
            {
                "prompt_family": pf,
                "rows": len(sub),
                "probe_type": sub["probe_type"].iloc[0],
                "primary_target": sub["primary_target"].iloc[0],
                "dominant_signature_counts": counts_as_string(sub["dominant_signature"]),
                "intensity_mean": round(sub["intensity_score"].mean(), 3),
                "intensity_counts": counts_as_string(sub["intensity_score"].astype(int)),
                "failure_mode_count": int(sub["failure_mode_flag"].sum()),
            }
        )

    pf_overview = pd.DataFrame(pf_overview_rows)
    pf_overview.to_csv(
        tables_dir / "table_01_prompt_family_overview.csv",
        index=False,
        encoding="utf-8-sig",
    )

    # Dominant signature counts
    dominant_counts = (
        df["dominant_signature"]
        .value_counts()
        .rename_axis("dominant_signature")
        .reset_index(name="count")
    )
    dominant_counts.to_csv(
        tables_dir / "table_02_dominant_signature_counts.csv",
        index=False,
        encoding="utf-8-sig",
    )

    # Secondary signature counts
    secondary_counter = {}
    for raw in df["secondary_signatures"]:
        if raw:
            for sig in [x.strip() for x in raw.split(",") if x.strip()]:
                secondary_counter[sig] = secondary_counter.get(sig, 0) + 1

    if secondary_counter:
        secondary_counts = pd.DataFrame(
            [
                {"secondary_signature": key, "count": value}
                for key, value in secondary_counter.items()
            ]
        ).sort_values(["count", "secondary_signature"], ascending=[False, True])
    else:
        secondary_counts = pd.DataFrame(columns=["secondary_signature", "count"])

    secondary_counts.to_csv(
        tables_dir / "table_03_secondary_signature_counts.csv",
        index=False,
        encoding="utf-8-sig",
    )

    # Combined signature counts
    all_signatures = sorted(
        set(dominant_counts["dominant_signature"])
        | set(secondary_counts["secondary_signature"] if not secondary_counts.empty else [])
    )

    combined_rows = []
    for signature in all_signatures:
        dominant_count = int((df["dominant_signature"] == signature).sum())
        secondary_count = int(secondary_counter.get(signature, 0))
        combined_rows.append(
            {
                "signature": signature,
                "dominant_count": dominant_count,
                "secondary_count": secondary_count,
                "total_observed_count": dominant_count + secondary_count,
            }
        )

    combined_counts = pd.DataFrame(combined_rows).sort_values(
        ["total_observed_count", "signature"],
        ascending=[False, True],
    )
    combined_counts.to_csv(
        tables_dir / "table_04_combined_signature_counts.csv",
        index=False,
        encoding="utf-8-sig",
    )

    # Intensity distribution
    intensity_distribution = (
        df["intensity_score"]
        .astype(int)
        .value_counts()
        .sort_index()
        .rename_axis("intensity_score")
        .reset_index(name="count")
    )
    intensity_distribution["percentage"] = (
        intensity_distribution["count"] / len(df) * 100
    ).round(2)
    intensity_distribution.to_csv(
        tables_dir / "table_05_intensity_distribution.csv",
        index=False,
        encoding="utf-8-sig",
    )

    # Matrices
    prompt_family_by_dominant_signature = pd.crosstab(
        df["prompt_family"],
        df["dominant_signature"],
    ).reindex(pf_order)
    prompt_family_by_dominant_signature.to_csv(
        tables_dir / "table_06_prompt_family_by_dominant_signature.csv",
        encoding="utf-8-sig",
    )

    prompt_family_by_intensity = pd.crosstab(
        df["prompt_family"],
        df["intensity_score"].astype(int),
    ).reindex(pf_order)
    prompt_family_by_intensity.to_csv(
        tables_dir / "table_07_prompt_family_by_intensity.csv",
        encoding="utf-8-sig",
    )

    # Failure modes
    failure_summary = (
        df[df["failure_mode_flag"] == 1]
        .groupby(["prompt_family", "prompt_variant", "failure_mode_type"], dropna=False)
        .size()
        .reset_index(name="count")
    )
    if failure_summary.empty:
        failure_summary = pd.DataFrame(
            columns=["prompt_family", "prompt_variant", "failure_mode_type", "count"]
        )
    failure_summary.to_csv(
        tables_dir / "table_08_failure_mode_summary.csv",
        index=False,
        encoding="utf-8-sig",
    )

    variant_counts = (
        pd.crosstab(df["prompt_family"], df["prompt_variant"])
        .reindex(pf_order)
        .fillna(0)
    )
    variant_cols = [col for col in ["v01", "v02", "v03", "v04", "v05"] if col in variant_counts.columns]
    all_variants_have_3 = bool(variant_counts[variant_cols].eq(3).to_numpy().all())

    validation_snapshot = {
        "total_rows": int(len(df)),
        "unique_trial_id": int(df["trial_id"].nunique()),
        "duplicate_trial_id_count": int(len(df) - df["trial_id"].nunique()),
        "prompt_family_count": int(df["prompt_family"].nunique()),
        "rows_per_prompt_family_expected": 15,
        "all_prompt_families_have_15_rows": bool(
            (df["prompt_family"].value_counts().reindex(pf_order) == 15).to_numpy().all()
        ),
        "all_variants_have_3_rows_per_family": all_variants_have_3,
        "failure_mode_rows": int(df["failure_mode_flag"].sum()),
        "dominant_signature_counts": dominant_counts.set_index(
            "dominant_signature"
        )["count"].to_dict(),
        "intensity_counts": {
            str(key): int(value)
            for key, value in intensity_distribution.set_index("intensity_score")["count"].to_dict().items()
        },
    }

    with open(tables_dir / "table_09_validation_snapshot.json", "w", encoding="utf-8") as file:
        json.dump(validation_snapshot, file, indent=2, ensure_ascii=False)

    # Figures
    plot_dominant = dominant_counts.sort_values("count", ascending=True)
    plt.figure(figsize=(10, 6))
    plt.barh(plot_dominant["dominant_signature"], plot_dominant["count"])
    plt.xlabel("Count")
    plt.ylabel("Dominant signature")
    plt.title("Dominant Signature Counts")
    plt.tight_layout()
    plt.savefig(figures_dir / "figure_01_dominant_signature_counts.png", dpi=300)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.bar(intensity_distribution["intensity_score"].astype(str), intensity_distribution["count"])
    plt.xlabel("Intensity score")
    plt.ylabel("Count")
    plt.title("Suppression-Intensity Distribution")
    plt.tight_layout()
    plt.savefig(figures_dir / "figure_02_intensity_distribution.png", dpi=300)
    plt.close()

    mean_intensity = (
        df.groupby("prompt_family")["intensity_score"]
        .mean()
        .reindex(pf_order)
        .reset_index()
    )
    plt.figure(figsize=(10, 5))
    plt.bar(mean_intensity["prompt_family"], mean_intensity["intensity_score"])
    plt.xlabel("Prompt family")
    plt.ylabel("Mean intensity score")
    plt.title("Mean Intensity by Prompt Family")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(figures_dir / "figure_03_prompt_family_mean_intensity.png", dpi=300)
    plt.close()

    failure_by_family = (
        df.groupby("prompt_family")["failure_mode_flag"]
        .sum()
        .reindex(pf_order)
        .reset_index()
    )
    plt.figure(figsize=(10, 5))
    plt.bar(failure_by_family["prompt_family"], failure_by_family["failure_mode_flag"])
    plt.xlabel("Prompt family")
    plt.ylabel("Failure-mode row count")
    plt.title("Failure-Mode Counts by Prompt Family")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(figures_dir / "figure_04_failure_mode_counts_by_prompt_family.png", dpi=300)
    plt.close()

    print("Layer 1.A coding analysis complete.")
    print(f"Input rows: {len(df)}")
    print(f"Tables written to: {tables_dir}")
    print(f"Figures written to: {figures_dir}")


if __name__ == "__main__":
    main()
