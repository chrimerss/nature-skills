# Experiment Index

Dataview query dashboard that automatically summarizes all experiment logs.

```dataview
TABLE date, salt_system, exp_type, material, anomaly
FROM "Experiment-Logs"
WHERE exp_id
SORT date DESC
```

## Usage

1. Place this file in your vault's `Experiment-Logs/` directory.
2. Ensure all log files contain YAML frontmatter (fields like `exp_id`, `date`, `salt_system`, `exp_type`).
3. Open this file in Obsidian to view an interactive list of experiments.

## Customization

Adjust query fields according to your research systems. Common extensions:
- Filter by system: `WHERE salt_system = "Chloride"`
- Filter by anomaly: `WHERE anomaly = true`
- Filter by date range: `WHERE date >= date(2026-01-01)`
