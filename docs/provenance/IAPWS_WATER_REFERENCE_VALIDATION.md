# IAPWS Water Reference Validation

status: PASS

## Implementation

- package_name: iapws
- package_version: 1.5.5
- module_path: C:\Users\Administrator\AppData\Roaming\Python\Python311\site-packages\iapws\iapws95.py
- module_sha256: 89edb7c0e3b77533319d253819cdb4c1da50775d2e7b324249574607d6790520
- calculation_path: iapws.IAPWS95(T=temperature_K, x=0) for saturation cross-check; iapws.IAPWS95(T=temperature_K, P=pressure_MPa) for compressed-liquid external water reference fugacity

## Check Points

| check | value | status |
|---|---:|---|
| saturation_pressure_MPa at 353.15 K | 0.0474144740301651 | PASS |
| saturation_liquid_fugacity_MPa at 353.15 K | 0.0469787647672105 | PASS |
| compressed_liquid_density_kg_m3 at 353.15 K, 20 MPa | 980.493711002475 | PASS |
| compressed_liquid_fugacity_MPa at 353.15 K, 20 MPa | 0.053255717968868 | PASS |

Saturation pressure is close to the independent Antoine debug estimate near 0.047 MPa, while the production water fugacity uses IAPWS-95 compressed-liquid fugacity at the configured total pressure.
