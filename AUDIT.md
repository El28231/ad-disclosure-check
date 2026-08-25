# Audit Record

Audit date: 2026-08-25

Scope: contracts/ad_disclosure_check.py, ABI/schema, direct tests, five-validator GLSim, live StudioNet flow, source policy, security boundaries, dependencies, CI, repository hygiene, wallet isolation, and workspace-wide duplicate analysis.

## Automated evidence

- GenVM lint and validation: PASS; no errors
- ABI schema extraction: PASS
- Pyright contract typecheck: PASS; 0 errors and 0 warnings
- Hardened direct tests: PASS (3/3)
- Five-validator GLSim workflow: PASS
- Live StudioNet deployment, nondeterministic write, execution-success assertion, and persisted-state read: PASS
- Observed StudioNet result: CLEAR_DISCLOSURE
- StudioNet contract address: 0xD1B9E65802C559d9c711D48199590e04C808e9d3
- Pinned dependency consistency: PASS
- Secret scan: PASS; no populated environment values or wallet files
- Workspace semantic and structural duplicate review: PASS

## Manual review

Reviewed state reachability, replay prevention, role checks, input bounds, model-output normalization, validator independence, prompt-injection boundaries, evidence authority, privacy, source freshness, fund custody, and product-specific certification claims.

## Findings and residual risk

No known high-, medium-, or submission-blocking defect remains. It does not prove that the sponsorship facts are true and is not legal or regulatory certification. Validator disagreement can leave a transaction unresolved, and third-party review is discretionary; this audit cannot guarantee acceptance.

The concrete runner pin matches the runner documented for GenLayer contract examples. The linter's newer-runner notice is informational; the pinned source passed live StudioNet.
