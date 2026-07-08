# Experiment Log Example

The following is a complete log example for a materials immersion corrosion experiment. All data is fictitious and intended solely to demonstrate formatting and recording standards.

---

```yaml
---
exp_id: CL-M-260529-001
date: 2026-05-29
salt_system: Chloride Salt
salt_batch: CL-Q1-B001
salt_composition: "Q1 (*** mol%)"
exp_type: Corrosion Verification
furnace: Muffle_Furnace_1
crucible: AL-001
total_salt_mass_g: 50.0
temperature_profile: "RT→300°C(2h, drying)→500°C(300h)→Furnace cool"
atmosphere: Ar
material: 316L
material_category: Austenitic Stainless Steel
sample_id: 316L-2026-001
sample_dimensions_mm: "20×10×2"
sample_surface: "SiC 1200 grit"
pre_mass_g: 3.4521
post_mass_g: 3.4489
mass_loss_g: 0.0032
corrosion_rate_um_year: ***
anomaly: false
anomaly_ref:
tags: [Chloride, Corrosion Verification, 316L, Q1]
---

# Objective

Verify the corrosion behavior of candidate formulation Q1 on 316L austenitic stainless steel at 500°C as a baseline experiment for screening quaternary chloride salt systems.

# Procedure

1. Prepare 50.0g of Q1 salt mixture and mix uniformly inside the glovebox.
2. Polish 316L sample with SiC 1200 grit paper, ultrasonically clean in acetone, dry, and weigh.
3. Dry in muffle furnace under Ar atmosphere at 300°C for 2h (to remove adsorbed moisture).
4. Heat to 500°C and maintain isothermally for 300h.
5. Furnace cool to room temperature and retrieve sample.
6. Ultrasonically clean in deionized water, dry, and weigh.
7. Calculate mass loss and corrosion rate.

# Observations

- Upon cooling, the salt formed a pale yellow transparent glassy state with no obvious phase separation.
- Sample surface lost its metallic luster and turned uniform dark gray.
- No visible corrosion marks on the inner wall of the crucible.
- No abnormal gas release or splashing observed.

# Results

- Sample mass loss: 0.0032 g (0.09%).
- No obvious localized corrosion or pitting on the surface.
- XRD and SEM-EDS pending to confirm corrosion product composition.

# Anomalies

None.

# Next Steps

- Perform SEM-EDS cross-sectional analysis to confirm corrosion layer structure and Cr depletion.
- Conduct XRD analysis to identify corrosion product phases.
- Run parallel comparison experiments with candidate formulations Q2 and Q3.

---

# Raw Materials

Raw image and audio records are archived at:
`raw/experiments/2026.05.29_Q1_Corrosion_Verification_316L_CL-M-260529-001/`

- `Images/IMG_5291.jpg` — Pre-corrosion sample surface
- `Images/IMG_5292.jpg` — Post-corrosion sample surface
- `Images/IMG_5293.jpg` — Crucible interior after salt cooling
