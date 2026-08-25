# Ad Disclosure Check

Runs a revision-based clearance workflow for sponsored-content disclosures under a campaign-specific rubric.

## Core workflow

- The deployer stores campaign context, disclosure rules, and the first post revision.
- Any caller may request consensus review of the current revision.
- A non-clear decision opens a creator-only revision slot; a clear decision closes the workflow.
- Every revision and review count remains readable on-chain.

## Reuse model

Deploy one instance per campaign or disclosure policy. Each instance supports up to five revisions, so it is reusable across drafts without erasing its audit trail.

## Why GenLayer

Whether a disclosure is prominent and understandable is a semantic judgment over natural-language context. GenLayer validators independently apply the same stored rubric and must agree on one strict category before state changes.

## Evidence and source boundary

Authoritative evidence is limited to campaign_context, disclosure_rules, and the on-chain revision text. No validator fetches or selects an external source.

## Safety boundary

It does not prove that the sponsorship facts are true and is not legal or regulatory certification. The contract holds no funds, has no upgrade hook, and never treats a model result as real-world certification.

## Verify locally

```text
python -m pip install -r requirements.txt
genvm-lint check contracts/ad_disclosure_check.py
genvm-lint typecheck contracts/ad_disclosure_check.py
pytest tests/direct -q
python tests/run_glsim.py --no-browser --seed 210821
gltest tests/integration/test_glsim_consensus.py -q --network localnet
```

Run the last two commands in separate terminals. The opt-in live test uses a dedicated StudioNet key outside this repository:

```text
gltest tests/integration/test_studionet_smoke.py -q -s --network studionet
```

Never commit a populated .env file, private key, keystore, or wallet password.

## Repository map

- contracts: deployable Intelligent Contract
- tests/direct: hardened direct-mode state, authorization, malformed-output, and validator tests
- tests/integration: five-validator GLSim and live StudioNet flows
- deployments: public deployment and transaction evidence only
- SOURCE_POLICY.md: evidence authority, collection, provenance, freshness, and privacy
- AUDIT.md: review-readiness checks and residual limitations
