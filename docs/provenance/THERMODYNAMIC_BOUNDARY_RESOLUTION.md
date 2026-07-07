# Thermodynamic Boundary Resolution

status: PASS

| boundary | status | method |
|---|---|---|
| CH4 reservoir chemical potential | PASS | RASPA internal EOS methane fugacity coefficient proven by 0-cycle probe |
| H2O reservoir chemical potential | PASS | IAPWS-95 external compressed-liquid water fugacity, scaled by water_activity |
| RASPA fugacity mapping | PASS | parsed generated simulation.input and reconstructed fugacity |

production is still gated by the RMS_0p300 smoke test.
