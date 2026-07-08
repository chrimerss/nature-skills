# Feishu Push Format

> Daily literature digest template delivered to the dedicated Feishu group.
> The `{placeholder}` values are filled by the fine-reading stage.

## Template

```markdown
📅 {YYYY-MM-DD} Literature Daily | Research Field Daily

━━━━━━━━━━━━━━━━━━━━

🏅 #{N} | {Title}
{Journal/Source}, {Year} | {Authors} et al. | {Institution} | ⭐ {score}/10 | Classification: {A-E tier}
DOI: {doi if available} | arXiv: {arxiv_id if available}

💡 Takeaway: {one-line takeaway — why this paper matters or why it is only deferred}

🔬 Methods: {experiment/simulation, system, temperature, alloy/coating, characterization techniques}

📊 Key Results: {specific data or conclusions, with units and test conditions; no vague summaries}

🧭 Critique: {value to the research mainline, limitations, whether worth full-text reading}

📎 {best available link: DOI / arXiv / PDF / repository}

━━━━━━━━━━━━━━━━━━━━

🏅 #{N+1} | ...
```

Daily pushes should NOT include a fixed "vault connection" field or forced wiki links; that's low-information. Vault/wiki connections belong in archival notes and later manual wiki integration. If a paper clearly hits a tracked author/network, mention it naturally in the commentary.

## Field Guidelines

| Field | Principle |
|-------|-----------|
| 💡 Takeaway | Can judge in 15 seconds whether to open the original text. Capture core contributions, avoid generic descriptions |
| 🔬 Methods | Experiment or simulation? What system? What characterization (CV/EIS/SEM/XRD/TEM)? What alloy? |
| 📊 Key Results | Must be specific data or clear conclusions. Avoid vague statements like "has important findings" or "provides new insights" |
| 🧭 Critique | Explain practical value to research thread, limitations, and whether worth full reading |
| ⭐ Score | Coarse filter score (0-10) to help judge priority; internal 6-dim scoring uses 0-100 and caps dimensions |

## Example

```markdown
📅 2026-05-09 Literature Daily | Research Field Daily

━━━━━━━━━━━━━━━━━━━━

🏅 #1 | Electrochemical monitoring of impurity X in compound A-B-C system via advanced voltammetry
Electrochimica Acta, 2026 | Zhang, Li, Wang et al. | CAS Institute | ⭐ 9.2/10 | Classification: A_Core_Thread
DOI: 10.xxxx/example | arXiv: 2405.12345

💡 Takeaway: First application of method X to system Y for impurity quantification, detection limit improved ~5× over prior art.

🔬 Methods: 500°C salt system; Pt working electrode, Ag/AgCl reference; Ar + different H₂O partial pressures; SWV quantification, cross-validated with titration.

📊 Key Results:
  · SWV detection limit 8 ppm O (vs. prior art CV method ~39 ppm)
  · Peak current linear with impurity concentration R²=0.997 (0-200 ppm range)
  · Peak shift <5 mV during 200 h stability testing

🧭 Critique: Category A candidate. Value lies in advancing monitoring sensitivity from CV to SWV, directly serving the monitoring-control verification loop; need full text to verify reference electrode stability and calibration method.

📎 https://arxiv.org/abs/2405.12345

━━━━━━━━━━━━━━━━━━━━

🏅 #2 | ...
```

## Delivery

```python
send_message(
    target="feishu:<chat_id>",
    message="<formatted_digest>"
)
```

Use `send_message(action='list')` to discover the chat_id if unknown. The target must be a group the Hermes bot has been added to as a member (Feishu group settings → bots → add).
