# Submission Checklist

## Contract

- [x] One clearly named deployable AdDisclosureCheck
- [x] Concrete GenVM runner hash; no floating dependency
- [x] Bounded inputs and bounded collections
- [x] Versioned policy schema: ad-disclosure-check/policy/v2
- [x] Independent validator replay and fail-closed model errors
- [x] Authorization and phase-transition tests
- [x] No payable method or fund custody
- [x] Reuse model and limitations documented
- [x] Architecture differs materially from other workspace contracts

## Evidence

- [x] Evidence authority, collection, provenance, freshness, and privacy documented
- [x] No autonomous web search or undisclosed source selection
- [x] Prompt-injection boundary documented and tested
- [x] Live StudioNet deployment and consensus-write receipt recorded
- [x] Local source SHA-256 recorded in deployments/studionet.json
- [x] Dedicated El28231 test wallet used; no cross-owner wallet reuse

## Quality

- [x] GenVM lint, ABI schema, and contract typecheck pass
- [x] 3 hardened direct tests pass
- [x] Five-validator GLSim workflow passes
- [x] Live StudioNet workflow passes with execution success
- [x] Exact Python dependency pins and pip check pass
- [x] Least-privilege GitHub Actions workflow included
- [x] Secret scan passes
- [x] MIT license, architecture, audit, security, and source-policy documents included

Repository URL: https://github.com/El28231/ad-disclosure-check

StudioNet contract: 0xD1B9E65802C559d9c711D48199590e04C808e9d3
