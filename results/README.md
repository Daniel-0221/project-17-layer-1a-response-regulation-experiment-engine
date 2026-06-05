# Layer 1.A Results

This directory contains analysis outputs generated from the finalized Layer 1.A master coding dataset.

## Tables

The `tables/` directory contains CSV and JSON summaries derived from:

```text
data/coded/layer1a_master_coding_batch.csv
```

Generated tables include prompt-family summaries, dominant-signature counts, secondary-signature counts, combined signature counts, intensity distributions, prompt-family matrices, failure-mode summaries, and a validation snapshot.

## Figures

The `figures/` directory contains PNG figures for manuscript-level reporting:

```text
figure_01_dominant_signature_counts.png
figure_02_intensity_distribution.png
figure_03_prompt_family_mean_intensity.png
figure_04_failure_mode_counts_by_prompt_family.png
```

## Reproducibility

To regenerate the tables and figures, run:

```bash
python analysis/analyze_layer1a_coding_batch.py
```

All outputs are based on black-box behavioral annotations of observable model responses. The result tables and figures do not imply access to internal model mechanisms, hidden modules, proprietary classifiers, or implementation-level architecture.
