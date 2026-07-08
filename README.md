<div align="center">
  <h1>Nature Skills</h1>
  <h3>Reusable research skills for AI scholars worldwide</h3>
  <p>
    Literature Search · Paper Reading · Nature Writing · Reviewer Simulation · Figures · Citation Audit · Revision Response
  </p>
  <p>
    <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-2ea44f"></a>
    <a href="#installation"><img alt="Install" src="https://img.shields.io/badge/install-Claude%20Code%20%7C%20Codex%20%7C%20OpenClaw%20%7C%20OpenCode%20%7C%20Hermes-111827"></a>
    <a href="#skill-index"><img alt="Skills" src="https://img.shields.io/badge/skills-16-0ea5e9"></a>
  </p>
  <p>
    <a href="#installation">Install</a>
    · <a href="#skill-index">Skill Index</a>
    · <a href="docs/open-source-agent-frameworks.md">Other Install</a>
    · <a href="#shared-design-principles">Design Principles</a>
    · <a href="#adding-a-skill">Contributing</a>
  </p>
</div>



> **Credit**: This project is forked from [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills), originally created by **Yizhe Yuan** and **Xin-Rui Ma**. This fork provides an English-only version of the skill library.

---

## Installation

`nature-skills` is a collection of reusable skill packages organized around
`SKILL.md`. Each top-level skill directory under `skills/` is an installable unit,
such as `nature-*`; `skills/_shared/` contains shared content and should also be
kept when installing the complete repository.

### Claude Code Installation

Claude Code cannot use `scripts/update-codex-skills.sh` directly because that
script only syncs skills into Codex's `~/.codex/skills/`. For Claude Code, keep a
stable local clone and create a subagent or slash command wrapper that points to
the real `skills/*/SKILL.md`. This preserves the skill directory structure and
lets the workflow keep using `references/`, `static/`, `manifest.yaml`, scripts,
assets, and `skills/_shared/`.

If Claude Code is not installed yet:

```bash
npm install -g @anthropic-ai/claude-code
claude
```

Clone the repository to a stable path:

```bash
mkdir -p ~/ai-skills
cd ~/ai-skills
git clone https://github.com/chrimerss/nature-skills.git
```

Recommended method: create a Claude Code subagent wrapper for the skills you use
often. Example for `nature-reader`:

```bash
mkdir -p ~/.claude/agents
cat > ~/.claude/agents/nature-reader.md <<'EOF'
---
name: nature-reader
description: Use for structured paper reading, figure-aware extraction, and source-grounded paper notes.
---

When invoked, first read `~/ai-skills/nature-skills/skills/nature-reader/SKILL.md` and follow it as the governing workflow.
Read supporting files from `~/ai-skills/nature-skills/skills/nature-reader/` and `~/ai-skills/nature-skills/skills/_shared/` only when needed.
Do not replace this skill with a generic paper-reading response.
EOF
```

Then start a new Claude Code session and ask for the subagent explicitly:

```text
Use the nature-reader subagent to turn this paper into a structured Markdown reader.
```

If you prefer a slash command, create a command wrapper instead:

```bash
mkdir -p ~/.claude/commands
cat > ~/.claude/commands/nature-reader.md <<'EOF'
Read `~/ai-skills/nature-skills/skills/nature-reader/SKILL.md` first and follow it strictly.
Read directly needed supporting files from `~/ai-skills/nature-skills/skills/nature-reader/` and `~/ai-skills/nature-skills/skills/_shared/`.

$ARGUMENTS
EOF
```

Use it inside Claude Code:

```text
/nature-reader Turn this paper into a full source-grounded Markdown reader.
```

To install other skills, replace `nature-reader` with the target directory name,
such as `nature-polishing`, `nature-writing`, `nature-reviewer`,
`nature-response`, or `nature-figure`. To update later:

```bash
cd ~/ai-skills/nature-skills
git pull
```

As long as the wrapper still points to this stable clone path, no repeated file
copy is needed.

### Recommended Codex Installation

Use the repository script to install or update Codex skills. It syncs every
top-level skill directory under `skills/` and verifies the copied contents with
`diff`. It does not overwrite unrelated Codex skills.

```bash
git clone https://github.com/chrimerss/nature-skills.git
cd nature-skills
scripts/update-codex-skills.sh --pull
```

If you already have a clone:

```bash
cd nature-skills
scripts/update-codex-skills.sh --pull
```

Verify that the current Codex installation matches this checkout:

```bash
scripts/update-codex-skills.sh --check
```

If you use this script for long-term updates and want to remove directories that
were previously managed by this installer but no longer exist upstream:

```bash
scripts/update-codex-skills.sh --pull --prune
```

`--prune` only removes directories recorded by this installer. It will not guess
or delete unrelated skills.

You can also ask Codex to install the repository for you:

```text
Install Codex skills from this repository:
https://github.com/chrimerss/nature-skills.git

Clone the repository, run scripts/update-codex-skills.sh --pull, and then run
scripts/update-codex-skills.sh --check to verify the installation. Keep complete
skill directories under skills/; do not copy only SKILL.md.
```

To install only one skill, specify the skill name:

```text
Install only nature-reader from this repository:
https://github.com/chrimerss/nature-skills.git

If the skill needs shared files, install skills/_shared as well.
```

Key rule: keep the full directory structure. Many skills depend on
`references/`, `static/`, `manifest.yaml`, scripts, assets, or shared files.

The installer does not install Python dependencies automatically. Install them
only when you need the corresponding scripts or MCP services:

```bash
python -m pip install -r skills/nature-paper-to-patent/requirements.txt
python -m pip install -r skills/nature-academic-search/mcp-server/requirements.txt
```

`nature-academic-search` also requires `PUBMED_EMAIL`. Optional Scopus,
ScienceDirect, and other provider credentials should be configured locally and
must not be committed to the repository.

After installation, start a new Codex session and describe your task naturally,
for example:

```text
Turn this paper into a full source-grounded Markdown reader.
```

```text
Create a presentation slide deck from this paper.
```

For OpenClaw, OpenCode, Hermes, and other open-source agent frameworks, see the [OpenClaw / OpenCode / Hermes integration guide](docs/open-source-agent-frameworks.md).

### Directory Layout

```text
skills/
├── _shared/              # keep this when skills reference ../_shared
├── nature-<topic>/
│   ├── README.md
│   ├── SKILL.md
│   ├── manifest.yaml     # present in router-style skills
│   ├── static/           # present in router-style skills
│   └── references/...
└── nature-proposal-writer/
    ├── README.md
    ├── SKILL.md
    ├── scripts/...
    ├── templates/...
    └── references/...
```

### Other Agent Scenarios

For OpenClaw, OpenCode, and Hermes, see the dedicated [integration guide](docs/open-source-agent-frameworks.md).

For other agents, keep a stable repository clone and create a lightweight
subagent, slash command, or custom prompt wrapper that points to the real
`skills/*/SKILL.md` files. Preserve `skills/_shared/`.

For manual or other-agent use:

1. Copy complete skill directories into your prompt library or project.
2. Preserve `SKILL.md`, `manifest.yaml`, `static/`, `references/`, scripts,
   assets, and required `skills/_shared/` files.
3. If the target agent has its own format requirements, adjust the frontmatter
   and body structure.

## Skill Index

The current `skills/` directory contains the following triggerable skills.
`skills/_shared/` is shared content and is not counted in the skill index.

| Skill | Status | Purpose | Example Triggers |
|---|---|---|---|
| [`nature-figure`](skills/nature-figure/README.md) | Stable | Submission-grade Python or R scientific figure workflow for Nature / high-impact journals, with a figures4papers-style demo and OpenRouter GPT Image 2 schematic-draft generation | "Nature figure", "submission-grade figure", "publication plot", "scientific figure", "figures4papers", "paper schematic", "GPT Image 2" |
| [`nature-polishing`](skills/nature-polishing/README.md) | Stable | Polish, restructure, or translate academic prose into Nature-style English | "Nature style", "polishing", "academic writing", "English manuscript" |
| [`nature-writing`](skills/nature-writing/README.md) | Draft | Draft Nature-style manuscript sections and rebuild a paper argument | "Nature writing", "write an abstract", "write introduction", "manuscript draft", "paper writing" |
| [`nature-reviewer`](skills/nature-reviewer/README.md) | Draft | Simulate Nature-style reviewer assessment from the reviewer perspective, returning three reviewer reports and a synthesis | "Nature reviewer", "pre-submission review", "reviewer report", "reviewer-perspective assessment" |
| [`nature-citation`](skills/nature-citation/README.md) | Beta | Search support literature strictly within Nature / CNS families and export ENW, RIS, or Zotero RDF | "Nature citation", "CNS citation", "segmented citation", "supporting references", "Zotero RDF" |
| [`nature-data`](skills/nature-data/README.md) | Draft | Prepare Data Availability statements, data repository plans, and FAIR checks | "Data Availability", "data availability", "repository", "FAIR metadata" |
| [`nature-reader`](skills/nature-reader/README.md) | Beta | Generate full-paper Markdown readers with source anchors and figure-text alignment | "nature reader", "full Markdown", "source-aligned text", "figure-text alignment" |
| [`nature-response`](skills/nature-response/README.md) | Beta | Parse revision emails; draft, audit, and revise revision cover letters, point-by-point response letters, red-marked manuscripts, and LaTeX templates | "response to reviewers", "rebuttal letter", "cover letter", "major revision", "revision email", "reviewer-comment response", "LaTeX template" |
| [`nature-paper2ppt`](skills/nature-paper2ppt/README.md) | Beta | Generate PPTX journal-club or paper-presentation decks from research papers | "paper PPT", "journal club", "paper to slides", "paper presentation" |
| [`nature-paper-to-patent`](skills/nature-paper-to-patent/README.md) | Beta | Generate evidence-constrained invention patent drafts from papers, technical reports, or project materials | "paper to patent", "patent draft", "paper-to-patent", "claims drafting" |
| [`nature-academic-search`](skills/nature-academic-search/README.md) | Beta | Multi-source literature search, citation verification, strict other-citation audits, article-level citation metric tables, influential citer profiling, and reference management | "search papers", "find articles", "literature search", "literature lookup", "verify DOI", "strict other citation", "article citation table", "influential citer" |
| [`nature-downloader`](skills/nature-downloader/README.md) | Beta | Legally obtain academic full text/PDFs through library access, Chrome login state, and open-access routes | "download papers", "library paper download", "CARSI", "Web of Science", "PDF download" |
| [`nature-literature-pipeline`](skills/nature-literature-pipeline/README.md) | Stable | Automated literature discovery pipeline: multi-source retrieval, six-axis scoring, deep-reading delivery, and local archiving | "literature pipeline", "daily literature", "literature push", "daily literature push", "cron" |
| [`nature-experiment-log`](skills/nature-experiment-log/README.md) | Draft | Standardize experiment images, voice, and text into Obsidian experiment logs with YAML frontmatter and archived source materials | "experiment log", "record experiment", "Obsidian vault", "Feishu research group" |
| [`nature-proposal-writer`](skills/nature-proposal-writer/README.md) | Beta | Proposal-first research writing state machine: establish evidence, argument, and section contracts before drafting or reviewing text | "researchwrite", "proposal", "opening report", "research plan", "research writing QA" |

---

## Shared Design Principles

1. **Prefer primary sources**: rules should be grounded in published Nature
   content, official journal guidance, or explicit local sources rather than
   generic taste.
2. **Make rules explicit**: explain the reason behind each rule instead of
   giving unsupported assertions.
3. **Respect section and task context**: writing, figures, citations, and
   responses depend on the manuscript section and task.
4. **Output first**: every skill should produce something directly usable, such
   as paste-ready text, `.svg`, `.pptx`, `.docx`, or concrete instructions.
5. **Keep skills extensible**: each skill should be self-contained, and adding a
   new skill should not require modifying existing skills.

---

## Adding a Skill

When adding a skill to this repository, follow this process.

### 1. Create Directory

```text
skills/nature-<topic>/
```

### 2. Minimum Files

| File | Required | Purpose |
|---|---:|---|
| `SKILL.md` | Yes | Frontmatter (`name`, `description`) plus rules and workflow loaded by the agent |
| `README.md` | Yes | Human-facing documentation |
| `references/*.md` | Recommended for complex skills | Modular rule files, API references, design theory, tutorials, chart types, and similar material |

### 3. `SKILL.md` Frontmatter Template

```yaml
---
name: nature-<topic>
description: >-
  One sentence explaining what the skill does, when it should trigger, primary
  outputs, and core use cases.
---
```

### 4. Update Skill Index

After adding a skill, update the [Skill Index](#skill-index) table:

```markdown
| [`nature-<topic>`](skills/nature-<topic>/README.md) | Draft / Stable | One-sentence purpose | Trigger terms |
```

### 5. Status Labels

| Status | Meaning |
|---|---|
| `Draft` | Rules are defined but not yet tested on real cases |
| `Beta` | Tested on examples, with possible edge-case issues |
| `Stable` | Validated on real academic content and relatively stable |

---
