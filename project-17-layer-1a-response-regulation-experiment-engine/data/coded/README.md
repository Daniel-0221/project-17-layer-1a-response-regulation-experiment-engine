# Layer 1.A Coding Data

This directory contains the finalized coding data for the Layer 1.A response-regulation experiment.

The coding batch covers 14 prompt families, PF-01 through PF-14, with 15 annotated trials per prompt family.

## Files

| File | Description |
|---|---|
| `layer1a_master_coding_batch.csv` | Final master coding dataset combining PF-01 through PF-14. This is the primary dataset for analysis. |
| `layer1a_summary_by_prompt_family.csv` | Summary table by prompt family, including row counts, target descriptors, dominant-signature distributions, intensity distributions, and failure-mode counts. |
| `layer1a_signature_counts.csv` | Frequency table for dominant and secondary response-regulation signatures. |
| `layer1a_intensity_counts.csv` | Frequency table for ordinal suppression-intensity scores. |
| `layer1a_master_validation_report.txt` | Validation report for the final master coding batch. |
| `PF-01~14_coding_batch.zip` | Archived prompt-family coding batches for PF-01 through PF-14. |

## Dataset structure

The final master dataset contains:

```text
Prompt families: PF-01 to PF-14
Rows: 210
Rows per prompt family: 15
Prompt variants per family: v01 to v05
Repetitions per variant: r01 to r03
Coding pass: pass1
Coder ID: WJ
```

## Validation status

The final master coding batch passed validation with the following checks:

```text
Total rows: 210
Unique trial_id values: 210
Duplicate trial_id values: 0
Trailing-space issues: 0
Known internal-spacing issues: 0
Prompt-family row-count anomalies: none
Variant-count anomalies: none
Final validation: PASS
```

## Use in analysis

For statistical summaries, tables, and figures, use:

```text
layer1a_master_coding_batch.csv
```

The archived `PF-01~14_coding_batch.zip` file is included for traceability and backup of the individual prompt-family coding batches.

## Coding fields

Key annotation fields include:

| Field | Description |
|---|---|
| `trial_id` | Unique trial identifier. |
| `prompt_family` | Prompt family ID, PF-01 through PF-14. |
| `prompt_variant` | Variant ID within each prompt family. |
| `dominant_signature` | Primary observed Layer 1.A response-regulation signature. |
| `secondary_signatures` | Additional weaker but identifiable signatures, if present. |
| `intensity_score` | Ordinal response-regulation intensity score. |
| `ambiguity_flag` | Whether the row was marked as ambiguous. |
| `failure_mode_flag` | Whether a failure mode was observed. |
| `failure_mode_type` | Type of failure mode, if applicable. |
| `coder_notes` | Brief manual coding rationale. |
| `include_in_final` | Whether the row is included in the final analysis. |

## Notes

All claims derived from this dataset should be interpreted as black-box behavioral observations. The coding categories describe observable response patterns and do not imply access to internal model mechanisms, hidden modules, proprietary classifiers, or implementation-level architecture.
