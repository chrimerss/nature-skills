# Anomaly Log

Records all anomalies identified during experiments for quality control and troubleshooting.

## Format

```yaml
---
date: YYYY-MM-DD
related_exp: EXP-ID
anomaly_type: Equipment Failure / Operation Error / Abnormal Result / Safety Incident
severity: Low / Medium / High
status: Pending / Resolved / Needs Review
---

## Description

[Objective description of the anomaly]

## Impact

[Assessment of impact on experimental results]

## Action Taken

[Measures already implemented]

## Notes

[Recommendations for future runs]
```

## Usage

- Check for anomalies after every experiment.
- If found, append an entry to this file.
- Regularly review pending anomalies.
