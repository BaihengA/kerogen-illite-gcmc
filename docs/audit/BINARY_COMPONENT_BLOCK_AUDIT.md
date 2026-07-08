# Binary Component Block Audit

Scope: DIAGNOSTIC_ONLY audit of the validated binary carrier component blocks.

## Component 0 MoleculeName methane
- MoleculeName: methane
- MoleculeDefinition: ExampleDefinitions
- MolFraction: 0.997636645934322
- FugacityCoefficient: 0.8439459552
- TranslationProbability: 0.5
- RotationProbability: NOT_PRESENT
- ReinsertionProbability: 0.5
- SwapProbability: 1.0
- IdentityChangeProbability: NOT_PRESENT
- NumberOfIdentityChanges: NOT_PRESENT
- IdentityChangesList: NOT_PRESENT

## Component 1 MoleculeName H2O
- MoleculeName: H2O
- MoleculeDefinition: Local
- MolFraction: 0.0023633540656784
- FugacityCoefficient: 1.1266978304747
- TranslationProbability: 0.5
- RotationProbability: 0.5
- ReinsertionProbability: 0.5
- SwapProbability: 1.0
- IdentityChangeProbability: NOT_PRESENT
- NumberOfIdentityChanges: NOT_PRESENT
- IdentityChangesList: NOT_PRESENT

Findings:
- No identity-change directives are present in the binary carrier.
- Backtrace does not point to identity-change setup.
- The singular matrix is generated during post-simulation per-component heat-of-adsorption reporting, not during component definition parsing.
