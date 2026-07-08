# nature-literature-pipeline

Literature discovery engine + daily push application layer. A complete automated literature discovery and tracking system.

## What It Is

Not just a simple "search for a few papers" tool—it is a structured pipeline: Multi-source search → Six-dimensional scoring & screening → Detailed reading → Formatted push → Archiving. Supports daily automatic execution via cron.

## Relationship with nature-academic-search

`nature-academic-search` is for **on-demand search** ("find me a few papers on XX right now"), while this skill is for **automated subscription** ("keep an eye on this field daily and push new papers to me"). They are complementary, and installing both is recommended.

## Pipeline Architecture

```
Multi-source search (30 candidates)
  arXiv / OpenAlex / Crossref / Semantic Scholar (automatic degradation)
       ↓
Six-dimensional screening (30 → 5 papers)
  Topic match × 35 + Methodology × 20 + Journal quality × 15
  + Network relevance × 10 + Applied value × 10 + Archival value × 10
       ↓
Detailed reading (top 5)
  Source tagging: Full-text / Abstract only / Metadata only
       ↓
Push delivery
  🏅 Rank | Title | Journal | ⭐ Score | 💡 One-liner | 🔬 Methods | 📊 Key data | 🧭 Commentary
       ↓
Archiving
  DOI/arXiv deduplication → Classification → Notes → Update index
```

## Installation

```bash
# Codex
Install nature-literature-pipeline from this repository:
https://github.com/Yuan1z0825/nature-skills.git
Please install skills/nature-literature-pipeline/ completely, including references/ and templates/

# Hermes / Claude Code
git clone https://github.com/Yuan1z0825/nature-skills.git
cp -r nature-skills/skills/nature-literature-pipeline ~/.hermes/skills/research/
# Restart session or /reload-skills
```

## Initial Configuration

After installation, tell the agent:

```
My research field is perovskite solar cells, keywords: perovskite solar cell, PSC stability,
hole transport layer, interface passivation,
push literature to messaging group "Daily Literature", archive to ~/research/literature/
```

The agent will configure the keywords, push target, and archive path. Then set up cron:

```
Set up a daily literature push at 8:30 AM, 30 candidates, pushing top 5
```

## File Structure

```
nature-literature-pipeline/
├── SKILL.md                                ← Skill entry point
├── README.md                               ← This file
├── references/
│   ├── scoring-system.md                   ← Six-dimensional scoring rubric
│   ├── gap-analysis.md                     ← Literature gap analysis methodology
│   ├── note-template.md                    ← Standardized literature note template
│   ├── push-format.md                      ← Push message formatting specification
│   ├── cron-setup.md                       ← Cron creation/verification/recovery
│   └── review-compilation-workflow.md      ← Review compilation workflow
└── templates/
    └── literature-push-template.md         ← Shareable general configuration template
```

## Built-in Safeguards

- **Score validation**: Each dimension cannot exceed its cap; total score is automatically recalculated.
- **Triple deduplication**: DOI / arXiv ID / OpenAlex ID.
- **Automatic degradation**: If Semantic Scholar is unavailable → automatically switch to OpenAlex + Crossref + arXiv.
- **Read-only archive**: The daily pipeline only writes to the `raw/` directory and will not automatically modify the wiki/knowledge base.

## FAQ

**Q: How does it work with nature-citation?**
The pipeline discovers new papers → use nature-citation to export CNS-formatted citations for insertion into manuscripts.

**Q: What models are required?**
DeepSeek V3 or higher is recommended. For daily cron jobs, faster/lighter models can be used to reduce costs.

**Q: What if my field is not materials/chemistry?**
Everything is configurable. Simply replace the keywords with those from your field—it works equally well for medicine, biology, CS, and social sciences.

## Author

Shiwu (JL Lab) — Built on real scientific research workflows, running stably in production.
