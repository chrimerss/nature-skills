# Experiment Log Example: Electrochemical Testing

The following is a complete log example for an electrochemical characterization experiment. All data is fictitious.

---

```yaml
---
exp_id: OX-E-260615-001
date: 2026-06-15
salt_system: Oxide System
salt_batch: OX-A1-B001
salt_composition: "*** (*** wt%)"
exp_type: Electrochemistry
test_method: CV
working_electrode: Pt wire
counter_electrode: Pt mesh
reference_electrode: "Ag/Ag+ quasi-reference"
temperature: 500
atmosphere: Ar
potential_window_V: "-1.5 ~ +1.0"
scan_rate_mV_s: 50
evaluation_target: "Determine electrochemical window and detect impurity redox peaks"
anomaly: false
anomaly_ref:
tags: [Electrochemistry, CV, Window Test]
---

# Objective

Determine the electrochemical window of candidate formulation A1 at 500°C to confirm its suitability for subsequent corrosion experiments. Simultaneously detect whether impurity redox peaks are present.

# Procedure

1. Prepare 30g of A1 salt in the glovebox and transfer to an alumina crucible.
2. Dry in muffle furnace at 300°C for 2h (to remove adsorbed moisture).
3. Transfer to the electrochemical test station and heat to 500°C under Ar atmosphere.
4. Three-electrode setup: Pt wire working electrode, Pt mesh counter electrode, Ag/Ag+ quasi-reference electrode.
5. CV scan: -1.5V to +1.0V at a scan rate of 50 mV/s.
6. Record 3 cycles; take the 3rd cycle as steady-state data.

# Observations

- Salt melted into a transparent liquid with no visible suspended particles.
- CV curve exhibited minor peaks at -0.8V and +0.6V (suspected impurities).
- No visible corrosion on electrode surfaces.

# Results

- Electrochemical window is approximately 2.5V (-1.5 to +1.0V), suitable for subsequent corrosion testing.
- Further EIS testing required to confirm long-term system stability.
- Impurity peaks require standard addition method to identify chemical species.

# Anomalies

None.

# Next Steps

- Long-term EIS stability testing (100h).
- Use standard addition method to calibrate chemical species corresponding to impurity peaks.
- Compare window width against candidate formulations A2 and A3.

---

# Raw Materials

Raw image and audio records are archived at:
`raw/experiments/2026.06.15_A1_Electrochemical_Window_Test_OX-E-260615-001/`

- `Images/IMG_6151.jpg` — Three-electrode test setup layout
- `Images/IMG_6152.jpg` — CV curve screenshot
