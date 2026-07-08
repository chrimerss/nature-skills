# Experiment Log Example: Thermal Stability Testing

The following is a complete log example for a thermal stability experiment. All data is fictitious.

---

```yaml
---
exp_id: HY-T-260601-001
date: 2026-06-01
salt_system: Hybrid Salt System
salt_batch: HY-B1-B001
salt_composition: "*** (*** wt%)"
exp_type: Thermal Stability
furnace: Tube_Furnace_1
crucible: AL-005
total_salt_mass_g: 40.0
temperature_profile: "RT→200°C(4h, dehydration)→500°C(8h)→700°C(2h)→Furnace cool"
atmosphere: "Ar (100 mL/min)"
condensate: "Collected 2.3g colorless liquid"
absorption_solution: "0.1M NaOH 50mL"
anomaly: false
anomaly_ref:
tags: [Thermal Stability, Tube Furnace, Ar Atmosphere]
---

# Objective

Evaluate the thermal stability of candidate formulation B1 under protective Ar atmosphere, determining high-temperature mass loss and decomposition products.

# Procedure

1. Prepare 40.0g of B1 salt in the glovebox and transfer to an alumina crucible.
2. Place in tube furnace under Ar flow (100 mL/min) and dry at 200°C for 4h (to remove adsorbed water).
3. Heat to 500°C and hold isothermally for 8h, then heat to 700°C and hold for 2h.
4. Connect exhaust outlet to condenser + NaOH absorption flask.
5. Sample and record observations at each temperature stage; weigh after furnace cooling.

# Observations

- No noticeable change during the 200°C stage.
- At 500°C, condenser collected ~2.3g of colorless liquid (likely water of crystallization or low-boiling components).
- At 700°C, salt color changed from white to pale yellow, but no obvious decomposition occurred.
- Condensate pH was approximately 6 (slightly acidic).

# Results

- Total mass loss: 11.5% (based on initial mass).
- Mass loss occurred primarily in the 200-500°C range (dehydration); mass loss between 500-700°C was only 1.2%.
- Residual salt ICP-OES analysis showed no significant change in component ratios.
- Thermal stability qualified.

# Anomalies

None.

# Next Steps

- Compare thermal stability against candidate formulations B2 and B3.
- Extend 700°C isothermal holding time to 24h to verify long-term stability.
- Perform Karl Fischer titration to quantify residual moisture.

---

# Raw Materials

`raw/experiments/2026.06.01_B1_Thermal_Stability_HY-T-260601-001/`
