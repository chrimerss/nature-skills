# `nature-figure` Skill

`nature-figure` generates publication-grade scientific figures for Nature-level journals and high-impact academic scenarios, supporting both Python and R plotting workflows. When users explicitly request AI-generated schematics, mechanism diagrams, or graphical abstracts, it also supports generating conceptual schematic drafts via OpenRouter Images API (`openai/gpt-image-2`).

The skill starts with a "figure contract" rather than applying templates blindly. Before plotting, the core conclusion, evidence hierarchy, figure archetype, backend selection, journal/export constraints, statistical reporting, and source-data traceability must be defined. On the first use of the plotting workflow, the user's selection of Python or R is saved as the default preference; subsequent invocations default to this backend unless explicitly switched by the user. Plotting templates are applied only after the scientific logic is established.

The Python path primarily uses `matplotlib`, `seaborn`, `subplot_mosaic`, and `statsmodels`, ideal for fine-grained low-level layout control. The R path uses `ggplot2`, `patchwork`, `ComplexHeatmap`, `ggrepel`, `svglite`, `cairo_pdf`, and `ragg`. When using private template sets, private paths, filenames, or sourcing information must never be exposed in user-facing outputs.

This skill references production scripts from *Nature Machine Intelligence* and top machine learning/bioinformatics papers in [figures4papers](https://github.com/ChenLiu-1996/figures4papers). Original demo scripts and preview assets are also bundled in `assets/figures4papers/` for pattern-level adaptation.

---

## OpenRouter AI Schematic Generation

When the user explicitly requests "generate a schematic, mechanism diagram, or graphical abstract using OpenRouter / GPT Image 2", take the standalone AI-schematic route without asking for Python or R first.

```bash
export OPENROUTER_API_KEY="sk-or-..."
python skills/nature-figure/scripts/generate_openrouter_schematic.py \
  --title "Paper title" \
  --abstract-file abstract.txt \
  --panel-map "left: problem; center: proposed mechanism; right: validated outcome" \
  --outdir outputs/schematic \
  --basename graphical_abstract
```

This feature generates conceptual visual drafts and should not be used for quantitative data panels. Before formal submission, verify that scientific elements were not expanded through hallucination, and redraw key text, arrows, and labels as editable vector objects.

---

## Example Gallery

The images below are mock-data mockups generated according to this skill's rules: prioritizing editable SVG exports, restrained semantic color palettes, lowercase panel labels, and asymmetrical multi-panel information structures. PNG previews are shown in the README; formal usage should still export SVGs/PDFs from plotting scripts.

| Figure | Preview | Capabilities Shown |
|--------|---------|-----------------------------|
| Material design and physical validation | <a href="assets/gallery/fig1-material-mechanism-rich.png"><img src="assets/gallery/fig1-material-mechanism-rich.png" width="260" alt="Material design and physical validation"></a> | Mechanism-led composite figure, SEM-like image panels, rheology, release kinetics, retention maps, correlations, and endpoint quantification |
| Spatial retention and uptake | <a href="assets/gallery/fig2-spatial-imaging-rich.png"><img src="assets/gallery/fig2-spatial-imaging-rich.png" width="260" alt="Spatial retention and uptake"></a> | Dark microscopy plates, channel rows, local zoom-ins, depth profiles, uptake histograms, 3D penetration heatmaps, and image-derived correlations |
| In vivo efficacy and tolerability | <a href="assets/gallery/fig3-in-vivo-efficacy-rich.png"><img src="assets/gallery/fig3-in-vivo-efficacy-rich.png" width="260" alt="In vivo efficacy and tolerability"></a> | Experimental timeline, longitudinal tumor curves, individual growth trajectories, waterfall response, forest plot, histology, immune composition, and toxicity panels |
| Single-cell systems | <a href="assets/gallery/fig4-single-cell-systems-rich.png"><img src="assets/gallery/fig4-single-cell-systems-rich.png" width="260" alt="Single-cell systems figure"></a> | UMAP-style embedding, composition, marker heatmap, pseudotime, volcano plot, enrichment, ligand-receptor bubble matrix, and spatial neighborhood relationships |
| Perturbation validation | <a href="assets/gallery/fig5-validation-perturbation-rich.png"><img src="assets/gallery/fig5-validation-perturbation-rich.png" width="260" alt="Perturbation validation"></a> | Mechanistic perturbation timeline, recurrence endpoints, polar summary, dose-response, synergy matrix, biodistribution, cytokines, flow-like scatter, and safety scores |

**Gallery file policy**: Only lightweight PNG previews are kept in `assets/gallery/`. Large generated SVGs/PDFs are not committed unless strictly needed for tutorials, because real users should regenerate editable outputs from source data and scripts.

---

## Chart Family Atlas

The gallery below is categorized by chart family. Each preview is a compact 4 x 4 multi-panel atlas demonstrating the visual grammar range that can be assembled into Nature-style result figures.

| Type | Preview | Common Uses |
|------|---------|------------|
| Bar charts | <a href="assets/chart-atlas/atlas-01-bar-charts.png"><img src="assets/chart-atlas/atlas-01-bar-charts.png" width="240" alt="Bar chart atlas"></a> | Group comparisons, signed differences, within-group factorial designs, stacked composition |
| Line and trend charts | <a href="assets/chart-atlas/atlas-02-line-trends.png"><img src="assets/chart-atlas/atlas-02-line-trends.png" width="240" alt="Line chart atlas"></a> | Time courses, uncertainty bands, intervention markers, individual trajectories |
| Heatmaps | <a href="assets/chart-atlas/atlas-03-heatmaps.png"><img src="assets/chart-atlas/atlas-03-heatmaps.png" width="240" alt="Heatmap atlas"></a> | Z-score matrices, continuous abundance maps, annotated tables, clustering blocks |
| Scatter and bubble charts | <a href="assets/chart-atlas/atlas-04-scatter-bubble.png"><img src="assets/chart-atlas/atlas-04-scatter-bubble.png" width="240" alt="Scatter and bubble atlas"></a> | Correlations, clusters, volcano-style tests, quadrant summaries, third-variable encoding |
| Radar and polar charts | <a href="assets/chart-atlas/atlas-05-radar-polar.png"><img src="assets/chart-atlas/atlas-05-radar-polar.png" width="240" alt="Radar and polar atlas"></a> | Multi-axis benchmarking, circular summaries, polar histograms, directional density |
| Distribution plots | <a href="assets/chart-atlas/atlas-06-distributions.png"><img src="assets/chart-atlas/atlas-06-distributions.png" width="240" alt="Distribution plot atlas"></a> | Histograms, violin plots, box plots, ridgelines, and sample-level distributions |
| Forest and interval plots | <a href="assets/chart-atlas/atlas-07-forest-interval.png"><img src="assets/chart-atlas/atlas-07-forest-interval.png" width="240" alt="Forest and interval atlas"></a> | Effect sizes, confidence intervals, point ranges, paired slope comparisons |
| Area and stacked trends | <a href="assets/chart-atlas/atlas-08-area-stacked.png"><img src="assets/chart-atlas/atlas-08-area-stacked.png" width="240" alt="Area and stacked trend atlas"></a> | Filled trajectories, share stacking, cumulative curves, stream-like compositions |
| Image plates | <a href="assets/chart-atlas/atlas-09-image-plates.png"><img src="assets/chart-atlas/atlas-09-image-plates.png" width="240" alt="Image plate atlas"></a> | Microscopy channels, overlays, crops, scale bars, and dark panels |
| Network and matrix plots | <a href="assets/chart-atlas/atlas-10-network-matrix.png"><img src="assets/chart-atlas/atlas-10-network-matrix.png" width="240" alt="Network and matrix atlas"></a> | Bubble matrices, adjacency plots, node-link diagrams, and bipartite interaction panels |

---

## File Structure

This skill uses a router/static-dynamic structure: a short `SKILL.md` router combined with `manifest.yaml` loads the persistent core, the user-selected backend fragment, and on-demand references.

```text
nature-figure/
├── SKILL.md                     # Short router: backend gate, loads fragments
├── manifest.yaml                # always_load core + backend axis + on-demand references
├── README.md                    # This file
├── scripts/
│   ├── generate_openrouter_schematic.py
│   └── nature_figure_backend.py
├── static/
│   ├── core/                    # Always loaded
│   │   ├── contract.md          # Figure contract, backend gate, mutual exclusion, missing runtime handling
│   │   └── stance.md            # Color strategy, default stance, privacy, loading rules
│   └── fragments/
│       └── backend/             # Loaded after Python-or-R gate resolution
│           ├── python.md        # Python-only rules and matplotlib quick-start
│           └── r.md             # R-only rules and ggplot2 quick-start
├── assets/
│   ├── gallery/                 # Result figure preview PNGs
│   ├── chart-atlas/             # Chart family preview PNGs
│   └── figures4papers/          # Original demo scripts and preview assets
└── references/                  # Loaded on demand
    ├── figure-contract.md       # Core conclusions, evidence hierarchy, panel map
    ├── backend-selection.md     # Python vs R selection rules
    ├── r-workflow.md            # R scaffold, patchwork, ComplexHeatmap, export
    ├── r-template-index.md      # Local R template atlas
    ├── qa-contract.md           # Submission/revision QA checklist
    ├── api.md                   # PALETTE constants, helper function signatures
    ├── design-theory.md         # Typography, color theory, layout, export strategy
    ├── common-patterns.md       # Reusable code patterns
    ├── openrouter-image-generation.md
    ├── tutorials.md             # End-to-end tutorials
    ├── chart-types.md           # radar, 3D sphere, scatter, fill_between, log-scale
    └── demos.md                 # figures4papers demo map and routing guide
```

---

## Backend and Figure Contract Rules

Plotting tasks prioritize the backend already specified by the user; if none is specified, read the default preference saved by `scripts/nature_figure_backend.py`. When using the workflow for the first time without a saved preference, ask the user to choose **Python or R** and save the answer as the subsequent default backend. If the user requests a recommendation, refer to `references/backend-selection.md`.

Once a backend is selected, plotting, previewing, exporting, and visual QA must use ONLY that backend. If the selected runtime or package is missing, stop and report a blocker; do not substitute with another language temporarily. This rule applies bi-directionally: do not substitute R with Python, nor Python with R.

Before plotting, explicitly state or infer the core conclusion, figure archetype, panel map, evidence hierarchy, target output, statistical/source-data requirements, and export packages. Figures serve scientific logic first; aesthetics and template matching are secondary goals.

User-facing outputs must not expose private local paths, private filenames, internal reference documents, template identifiers, or private material sources unless the user explicitly requests an audit trail.

---

## Mandatory Python Rules

### 1. Three Required rcParams: Preserve SVG Editable Text

```python
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans']
plt.rcParams['svg.fonttype'] = 'none'
```

`svg.fonttype = 'none'` prevents matplotlib from converting every glyph into bezier curves by default. In the exported SVG, text remains as `<text>` nodes—selectable, searchable, and easily realigned in Illustrator or Inkscape.

The font stack includes `Arial`, `DejaVu Sans`, and `Liberation Sans`: `Arial` is standard on macOS/Windows, `DejaVu Sans` is bundled with matplotlib, and `Liberation Sans` is metrically compatible with Arial on RHEL/Ubuntu. This cascade improves cross-platform kerning consistency.

### 2. Primary Output Format is SVG

```python
fig.savefig('figure.svg', bbox_inches='tight')           # Primary output: editable text
fig.savefig('figure.png', dpi=300, bbox_inches='tight')  # Optional raster preview
```

When figures are intended for manuscripts or slide decks requiring late-stage text adjustments, do not export only PNGs.

### 3. Always Close Figures

```python
plt.close(fig)
```

---

## Quick-Start Template

```python
import matplotlib
matplotlib.use('Agg')                    # headless / server rendering
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# Required settings
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans']
plt.rcParams['svg.fonttype'] = 'none'

# Base styling
plt.rcParams.update({
    'font.size': 12,
    'axes.spines.right': False,
    'axes.spines.top': False,
    'axes.linewidth': 2.0,
    'legend.frameon': False,
    'xtick.major.width': 1.5,
    'ytick.major.width': 1.5,
})

# Figure setup
fig, ax = plt.subplots(figsize=(8, 5))
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

# ... Plotting code here ...

fig.tight_layout(pad=2)
fig.savefig('output.svg', bbox_inches='tight')
fig.savefig('output.png', dpi=300, bbox_inches='tight')
plt.close(fig)
```

---

## Color Palettes

```python
PALETTE = {
    # Main method / core series
    'blue_main':      '#0F4D92',
    'blue_secondary': '#3775BA',

    # Positive / improvement progression
    'green_1': '#DDF3DE',
    'green_2': '#AADCA9',
    'green_3': '#8BCF8B',

    # Baseline / control
    'red_1':      '#F6CFCB',
    'red_2':      '#E9A6A1',
    'red_strong': '#B64342',

    # Neutral accents
    'neutral_light': '#CFCECE',
    'neutral_mid':   '#767676',
    'neutral_dark':  '#4D4D4D',
    'neutral_black': '#272727',

    # Accent colors, use sparingly
    'gold':    '#FFD700',
    'teal':    '#42949E',
    'violet':  '#9A4D8E',
    'magenta': '#EA84DD',
}
```

Semantic mapping convention: `blue_main` represents the proposed method or core series, `green_3` represents positive variants, `red_strong` represents baselines, and `neutral_light` represents reference or background. Keep these consistent across all panels.

For dense multi-panel figures in the recent Nature Machine Intelligence style, a unified low-saturation palette is recommended: one coherent baseline family plus one coherent hero family, with green/red reserved strictly for delta markers or truly directional semantics.

```python
PALETTE_NMI_PASTEL = {
    # Baseline / control family
    'baseline_dark': '#484878',
    'baseline_mid':  '#7884B4',
    'baseline_soft': '#B4C0E4',

    # Proposed method family
    'ours_tiny':  '#E4E4F0',
    'ours_base':  '#E4CCD8',
    'ours_large': '#F0C0CC',

    # Overview / conceptual panel background blocks
    'bg_lilac': '#E0E0F0',
    'bg_aqua':  '#E0F0F0',
    'bg_peach': '#F0E0D0',

    # Neutral accents
    'neutral_light': '#D8D8D8',
    'neutral_mid':   '#A8A8A8',
    'neutral_dark':  '#606060',

    # Strictly for directional annotations
    'delta_up':   '#2E9E44',
    'delta_down': '#E53935',
}

DEFAULT_COLORS_NMI_PASTEL = [
    PALETTE_NMI_PASTEL['baseline_dark'],
    PALETTE_NMI_PASTEL['baseline_mid'],
    PALETTE_NMI_PASTEL['baseline_soft'],
    PALETTE_NMI_PASTEL['ours_tiny'],
    PALETTE_NMI_PASTEL['ours_base'],
    PALETTE_NMI_PASTEL['ours_large'],
]
```

Use cases:

- Comparing related model families such as `Tiny / Base / Large`.
- Building a 1-page result atlas requiring visual harmony across multiple panels.
- Pursuing a low-saturation editorial style rather than maximizing categorical distinction.

Practice rule: Keep the same method family in the same hue family across all panels. Do not change a blue-gray model in panel `a` into green in panel `d` just because a specific panel needs contrast.

---

## Supported Chart Types

| Chart | File | Key Pattern |
|-------|------|-------------|
| Grouped bar chart | `tutorials.md` | `ax.bar()` with `x + offset`, last panel dedicated to legend |
| Stacked bar chart | `common-patterns.md` | Iterate over `col_order`, accumulating `bottom` |
| Horizontal ablation bar | `tutorials.md` | `ax.barh()`, encoding completeness with alpha-gradients |
| Trend / line chart | `tutorials.md` + `api.md` | `make_trend()`, using `fill_between` for uncertainty |
| Continuous heatmap | `api.md` | `make_heatmap()`, `YlOrRd`, brightness-dependent cell annotation color |
| Diverging / z-score heatmap | `design-theory.md §11` | `RdBu_r`, `vmin=-2.5, vmax=2.5` |
| Bubble scatter plot | `design-theory.md §11` | x/y represent two dimensions, `s=` encodes third variable |
| Radar / polar chart | `chart-types.md` | `projection='polar'`, custom spokes, per-axis normalization |
| 3D sphere / illustration | `chart-types.md` | Lambertian shading via numpy grid ray-casting |
| Fill-between / stacked area | `chart-types.md` | Grayscale-print-safe using hatches |
| Log-scale bar | `chart-types.md` | `set_yscale('log')`, reserve headroom for annotations |
| Multi-panel GridSpec | `chart-types.md` | `GridSpec(rows, cols)`, full-width panel using `gs[0, :]` |

---

## Multi-Panel Information Structure

Each panel in a multi-panel figure must answer a **unique** scientific question. Covering any single panel should not allow other panels to fully replace it.

### Recommended Three-Tier Complexity Progression

| Tier | Question | Encoding Method |
|-------|----------|----------|
| Overview | "What is the overall landscape?" | Stacked bar, composition chart |
| Deviation | "What is unique about each group?" | Z-score heatmap, diverging colormap |
| Relationship | "How do variables co-vary?" | Bubble scatter, correlation plot |

### Common Redundancy Traps

| Trap | Example | Fix |
|------|---------|-----|
| Absolute + Absolute | Stacked bar percentages + heatmap of same percentages | Change heatmap to z-score deviation |
| Subset of Parent | Tumor-only ranked bar is just one column of stacked bar | Change to tumor % vs immune % scatter |
| Two Rankings | Ranked bars of two correlated metrics | Replace one with a bubble scatter plot |
| Same Data, Different Chart | Pie chart + stacked bar | Merge or replace with a relational chart |

### Z-score Deviation Heatmap

```python
z = (heat - heat.mean(axis=0)) / heat.std(axis=0)
im = ax.imshow(z.values, cmap='RdBu_r', aspect='auto', vmin=-2.5, vmax=2.5)
cbar.set_label('Z-score vs pan-cohort mean')
```

In `RdBu_r`, red indicates above-average enrichment and blue indicates below average. This provides orthogonal information to the absolute percentages shown in panel a.

### Bubble Scatter with Quadrant Labels

```python
ax.scatter(x, y, s=size_var * scale, c=colors, edgecolors='white', linewidth=0.8, alpha=0.9)
ax.axvline(np.median(x), lw=1.2, ls='--', color='#767676', alpha=0.6)
ax.axhline(np.median(y), lw=1.2, ls='--', color='#767676', alpha=0.6)
```

Place quadrant labels in corners using small gray italic text, e.g., `fontsize=7.5, color='#888888', style='italic'`.

---

## Layout Rules

### Figure Dimensions

| Type | `figsize` |
|------|-----------|
| Multi-metric bar chart (3-4 metrics + legend panel) | `(28-45, 6-12)` |
| Large multi-panel figure (3 panels, 2-row GridSpec) | `(22, 17)` |
| Compact single bar chart | `(9-16, 5-8)` |
| Trend / line multi-panel | `(14, 4)` or `(9, 8)` |
| Single heatmap | `(8-20, 5-9)` |
| Radar / polar plot | `(12, 10)` |

Rule: Comparative bar panels typically have a width roughly 3-4 times their height.

### Panel Labels

```python
ax.text(-0.05, 1.06, 'a', transform=ax.transAxes,
        fontsize=22, fontweight='bold', va='top', ha='right')
```

Use lowercase bold `a`, `b`, `c` in the top-left corner of each subplot, positioned via `transAxes`.

### Legend

- In multi-axis figures, give the legend a dedicated axis, e.g., `ax.set_axis_off()`.
- Always use `frameon=False`.
- If the legend is large, place it below the panels: `bbox_to_anchor=(0.5, -0.24), loc='upper center'`.

---

## Font Size Hierarchy

| Context | `font.size` |
|---------|-------------|
| Standard compact subplot | 12-16 |
| Large bar panel (figsize > 28 in) | 24 |
| Large panel axis title | 32-54, overriding per-label |
| In-bar / in-cell annotation | 6.5-12 |
| Panel letter label | 20-22 |
| Legend | 8-14 |

---

## Axes and Spine Rules

```python
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.rcParams['legend.frameon'] = False

ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
```

Avoid gridlines by default. Use sparse `set_yticks` to guide reading. Keep Y-axis ranges close to data limits; do not use `0-100` when all values fall between `80-95`.

---

## In-Cell / In-Bar Text Contrast

```python
def luminance_text_color(hex_color):
    c = hex_color.lstrip('#')
    r, g, b = int(c[0:2],16)/255, int(c[2:4],16)/255, int(c[4:6],16)/255
    return 'white' if 0.299*r + 0.587*g + 0.114*b < 0.5 else '#333333'
```

---

## Reproducibility Checklist

- [ ] Core conclusions and panel map are defined before styling.
- [ ] Backend is explicitly chosen as Python or R.
- [ ] **First 3 settings** include `font.family`, `font.sans-serif` 3-font stack, and `svg.fonttype = 'none'`.
- [ ] Primary output is **SVG**, saved with `bbox_inches='tight'`.
- [ ] Right and top spines are disabled; `legend.frameon = False`.
- [ ] Font sizes match intended use: dense journal figures typically use 5-7 pt, with larger sizes reserved for slide-sized panels.
- [ ] Colors come from a single coherent palette system: semantic `PALETTE` or unified `PALETTE_NMI_PASTEL`.
- [ ] Related model sizes or variants share the same hue family without assigning unrelated high-saturation colors to sibling series.
- [ ] Green / red are reserved strictly for increase, decrease, thresholds, or truly directional semantics.
- [ ] Y-axis range is close to data limits.
- [ ] In multi-panel figures, each panel answers a **different** question, verified against redundancy traps.
- [ ] Panel labels use bold lowercase `a`, `b`, `c`, sized appropriately for output.
- [ ] For manuscripts, statistical reporting, `n`, source data, and image integrity notes are documented.
- [ ] Call `tight_layout(pad=2)` before saving.
- [ ] Call `plt.close(fig)` after saving.
