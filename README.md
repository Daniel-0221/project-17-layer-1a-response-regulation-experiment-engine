# Project 17 — Layer 1.A Response Regulation Experiment Engine

## Project Goal

This project builds the experimental data structure and analysis pipeline for the Layer 1.A response-regulation study.

The goal is to translate the Layer 1.A manuscript framework into a reproducible black-box behavioral experiment workflow.

The project is designed to collect, store, code, analyze, and visualize model responses generated under controlled prompt perturbations. It focuses on observable response-regulation signatures such as hedging, refusal-like movement, legal caution, moral deflection, disclaimer insertion, factual narrowing, political neutrality, victim-protective framing, identity minimization, and interactional politeness.

This project does not attempt to inspect or infer hidden model internals. It analyzes only observable prompt-response behavior.

## Research Background

This project is based on the Layer 1.A framework from my LLM response-pattern research series.

Layer 1.A is defined as an interaction-level analytic construct for suppression-like response regulation in large language model interaction.

The framework organizes observable response-regulation behavior into two descriptor families:

```text
L-series descriptors:
L1 — Affective Tone Softening
L2 — Safety-Oriented Constraint Expression
L3 — Expression and Commitment Softening
L4 — Structural Reframing
L5 — Context-Error Bypass and Clarification
L6 — Political Neutralization
L7 — Moral-Judgment Deflection
L8 — Victim- and Vulnerability-Protective Framing
L9 — Interactional Politeness and User-Position Preservation

e-series descriptors:
e1 — Political Sensitivity
e2 — Emotional Balance
e3 — Factual Constraint
e4 — Bias and Protected-Group Sensitivity
e5 — Harm and Victim-Frame Protection
e6 — Legal Caution
e7 — Religious and Worldview Neutrality
e8 — Liability Diffusion and Disclaimer Insertion
e9 — Identity and Ontology Minimization
```

These descriptors are not treated as internal modules, hidden classifiers, policy components, or implementation-level mechanisms.

They are behavioral coding categories used to describe recurring input-output regularities under black-box conditions.

## Core Experiment Idea

The core idea is to test whether controlled prompt features are associated with observable response-regulation signatures.

The experiment varies prompt conditions such as:

```text
tone
form
certainty pressure
legal framing
moral pressure
political sensitivity
worldview framing
victim or vulnerability cues
decision-authority pressure
identity or ontology attribution
```

Each prompt variant is treated as a controlled interactional stimulus.

Each model response is treated as an observable behavioral output.

The analysis asks whether specific prompt conditions are associated with recurring response-regulation signatures, dominant and secondary descriptors, ordinal intensity scores, ambiguity flags, and failure-mode patterns.

## Relationship to Previous Projects

Projects 11–16 focused on the Layer 0 surface-stabilization study.

```text
Project 11:
Layer 0 pilot experiment engine

Project 12:
Layer 0.2–0.3 surface form and structural alignment batch

Project 13:
Layer 0.4–0.5 verification, flagging, and error containment batch

Project 14:
Layer 0.6 surface-to-inhibition mapping batch

Project 15:
Layer 0 cross-layer cascade analysis

Project 16:
Layer 0 intra-coder reliability and audit-preserved dataset
```

Project 17 begins the next experimental sequence.

It extends the portfolio from Layer 0 surface stabilization to Layer 1.A suppression-like response regulation.

The project keeps the same portfolio-level logic:

```text
theoretical framework
controlled prompt experiment
raw response collection
manual behavioral coding
analysis scripts
visualization
results summary
reliability support
```

However, the internal data structure is more complex than earlier Layer 0 projects because Layer 1.A requires descriptor-level coding across L1–L9 and e1–e9 categories.

## What This Project Does

This project:

- defines Layer 1.A prompt families and prompt variants
- organizes prompt-family-level coding data for PF-01 through PF-14
- stores finalized manual annotations
- creates a trial-level master coding dataset
- supports coding of dominant and secondary response-regulation signatures
- codes ordinal suppression-like response-regulation intensity
- marks ambiguity and failure-mode cases
- generates descriptor-level summary tables
- generates intensity-distribution tables
- generates prompt-family-level matrices
- generates manuscript-ready figures
- preserves validation outputs
- supports manuscript-level empirical reporting

## Repository Structure

```text
project-17-layer-1a-response-regulation-experiment-engine/
├── README.md
├── notes.md
├── results.md
├── requirements.txt
│
├── prompts/
│   ├── prompt_registry_core.csv
│   ├── prompt_registry_extended.csv
│   ├── prompt_registry_future.csv
│   └── prompt_conditions.json
│
├── data/
│   ├── metadata/
│   │   ├── execution_settings.json
│   │   └── model_run_log.csv
│   │
│   ├── raw/
│   │   ├── raw_responses_core.csv
│   │   ├── raw_responses_extended.csv
│   │   └── raw_responses_future.csv
│   │
│   ├── processed/
│   │   ├── trial_master.csv
│   │   └── response_cleaned.csv
│   │
│   ├── coded/
│   │   ├── README.md
│   │   ├── layer1a_master_coding_batch.csv
│   │   ├── layer1a_summary_by_prompt_family.csv
│   │   ├── layer1a_signature_counts.csv
│   │   ├── layer1a_intensity_counts.csv
│   │   ├── layer1a_master_validation_report.txt
│   │   └── PF-01~14_coding_batch.zip
│   │
│   └── reliability/
│       ├── reliability_sample.csv
│       ├── pass2_blind_recoding_sheet.csv
│       ├── pass2_completed_recoding.csv
│       └── reliability_results.csv
│
├── analysis/
│   └── analyze_layer1a_coding_batch.py
│
├── results/
│   ├── README.md
│   │
│   ├── tables/
│   │   ├── table_01_prompt_family_overview.csv
│   │   ├── table_02_dominant_signature_counts.csv
│   │   ├── table_03_secondary_signature_counts.csv
│   │   ├── table_04_combined_signature_counts.csv
│   │   ├── table_05_intensity_distribution.csv
│   │   ├── table_06_prompt_family_by_dominant_signature.csv
│   │   ├── table_07_prompt_family_by_intensity.csv
│   │   ├── table_08_failure_mode_summary.csv
│   │   └── table_09_validation_snapshot.json
│   │
│   └── figures/
│       ├── figure_01_dominant_signature_counts.png
│       ├── figure_02_intensity_distribution.png
│       ├── figure_03_prompt_family_mean_intensity.png
│       └── figure_04_failure_mode_counts_by_prompt_family.png
│
└── supplementary/
    ├── annotation_codebook.md
    ├── prompt_family_protocols.md
    └── reliability_protocol.md
```

## Finalized Empirical Outputs

The finalized Layer 1.A coding dataset and analysis outputs are available in this project.

### Coding Data

The finalized coding data are stored in:

```text
data/coded/
```

Main files:

```text
layer1a_master_coding_batch.csv
layer1a_summary_by_prompt_family.csv
layer1a_signature_counts.csv
layer1a_intensity_counts.csv
layer1a_master_validation_report.txt
PF-01~14_coding_batch.zip
```

The primary analysis dataset is:

```text
data/coded/layer1a_master_coding_batch.csv
```

The archived `PF-01~14_coding_batch.zip` file preserves the individual prompt-family coding batches for PF-01 through PF-14.

### Analysis Script

The analysis script is stored in:

```text
analysis/analyze_layer1a_coding_batch.py
```

To regenerate the empirical tables and figures, run:

```bash
python analysis/analyze_layer1a_coding_batch.py
```

### Result Tables

Generated result tables are stored in:

```text
results/tables/
```

The generated tables include:

```text
table_01_prompt_family_overview.csv
table_02_dominant_signature_counts.csv
table_03_secondary_signature_counts.csv
table_04_combined_signature_counts.csv
table_05_intensity_distribution.csv
table_06_prompt_family_by_dominant_signature.csv
table_07_prompt_family_by_intensity.csv
table_08_failure_mode_summary.csv
table_09_validation_snapshot.json
```

These tables summarize prompt-family-level patterns, dominant signatures, secondary signatures, combined signature counts, intensity distributions, failure-mode observations, and validation information.

### Result Figures

Generated figures are stored in:

```text
results/figures/
```

The generated figures include:

```text
figure_01_dominant_signature_counts.png
figure_02_intensity_distribution.png
figure_03_prompt_family_mean_intensity.png
figure_04_failure_mode_counts_by_prompt_family.png
```

These figures provide manuscript-ready visual summaries of dominant-signature frequencies, suppression-intensity distributions, prompt-family-level mean intensity, and failure-mode counts.

## Final Coding Dataset

The finalized master coding dataset contains:

```text
Prompt families: PF-01 to PF-14
Rows: 210
Rows per prompt family: 15
Prompt variants per family: v01 to v05
Repetitions per variant: r01 to r03
Coding pass: pass1
Coder ID: WJ
```

The final master coding batch passed validation:

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

## Data Schema

The final master coding dataset includes columns such as:

```text
trial_id
prompt_id
prompt_family
protocol_source
prompt_variant
probe_type
primary_target
secondary_targets
repetition
prompt_text
response_text
dominant_signature
secondary_signatures
intensity_score
ambiguity_flag
failure_mode_flag
failure_mode_type
coder_notes
coding_pass
coder_id
coding_date
include_in_final
_source_file
```

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

## Trial ID Convention

Trial IDs follow a structured convention:

```text
L1A_PF01_v01_r01
L1A_PF01_v01_r02
L1A_PF01_v01_r03
```

The format is:

```text
L1A_[prompt_family]_[variant]_[repetition]
```

Example:

```text
trial_id: L1A_PF01_v01_r01
prompt_family: PF-01
prompt_variant: v01
repetition: r01
```

This convention allows each trial to be traced back to its prompt family, prompt variant, and repetition number.

## Analysis

The analysis examines:

- descriptor frequency by prompt family
- dominant-signature distribution
- secondary-signature co-occurrence
- combined signature counts
- intensity-score distribution
- prompt-family by dominant-signature matrix
- prompt-family by intensity-score matrix
- ambiguity-flag frequency
- failure-mode frequency
- validation status of the master coding batch

The analysis remains descriptive and behavioral.

It does not claim to identify internal mechanisms.

## Visualizations

This project currently includes figures for:

- dominant-signature counts
- suppression-intensity distribution
- mean intensity by prompt family
- failure-mode counts by prompt family

These figures are intended to support manuscript-level reporting and portfolio-level reproducibility.

## Current Status

This project has moved beyond the initial structure-initialization stage.

Current completed items:

```text
PF-01 through PF-14 coding batches completed
Final master coding batch created
Master coding batch validation completed
GitHub data/coded directory updated
Analysis script added
Empirical result tables generated
Empirical figures generated
Results documentation added
```

Current remaining items:

```text
Manuscript Results section integration
Methods section update with actual data counts and analysis procedure
Discussion and Limitations update based on empirical outputs
Data availability statement refinement
Final manuscript polishing
Submission package preparation
```

## Methodological Limits

This project uses a black-box behavioral methodology.

It does not inspect:

- model weights
- hidden activations
- system prompts
- training data
- proprietary safety classifiers
- internal routing mechanisms
- implementation-level architecture

All claims should be interpreted as claims about observable response behavior under controlled prompt perturbation.

The project does not use human participant data.

The project does not claim that Layer 1.A is a real internal layer inside any deployed model.

Layer 1.A is treated as an interaction-level analytic construct for organizing suppression-like response-regulation signatures.

## Interpretation Note

All claims derived from this dataset should be interpreted as black-box behavioral observations.

The coding categories describe observable response patterns and do not imply access to internal model mechanisms, hidden modules, proprietary classifiers, or implementation-level architecture.
