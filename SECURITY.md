# Security

## Threat model

Callers may submit malicious, incomplete, contradictory, oversized, or prompt-injection text. A model may return malformed JSON or an unauthorized category. Callers may attempt duplicate writes, invalid phase transitions, or role bypasses.

## Mitigations

- Field-specific normalization and size bounds
- Explicit untrusted-data delimiters and fixed response schemas
- Independent validator replay with exact normalized equality
- Fail-closed exceptions and malformed output
- Phase checks, bounded collections, and role checks
- No payable methods, fund custody, upgrades, or hidden administrator override

## Domain boundary

It does not prove that the sponsorship facts are true and is not legal or regulatory certification.

## Privacy and operations

All constructor and write calldata is public. Remove secrets and unnecessary personal data before submission. Keep wallet material and populated environment files outside the repository. StudioNet addresses and transaction hashes are public disposable evidence.

Report vulnerabilities through the repository's private security-advisory channel; never place secrets in an issue.
