# Evidence and Source Policy

## Authoritative evidence

Authoritative evidence is limited to campaign_context, disclosure_rules, and the on-chain revision text. No validator fetches or selects an external source.

## Collection and provenance

The deployer and callers are responsible for collecting text lawfully, verifying provenance where it matters, and removing secrets or unnecessary personal data. On-chain storage proves which text was evaluated, not who authored it or whether it is true.

## Source selection and freshness

The contract performs no web request, search, browsing, API lookup, or hidden source selection. Therefore it makes no live-data or freshness claim. When facts or policies change, deploy a new appropriate instance or submit a new record through the documented workflow.

## Prompt-injection and output controls

Caller text is untrusted data. It is canonicalized into a delimited payload; the prompt forbids treating embedded text as instructions. Only the documented strict JSON shape and closed values can pass normalization and validator replay.

## Production boundary

It does not prove that the sponsorship facts are true and is not legal or regulatory certification. Higher-stakes applications need independent provenance, identity, privacy, appeal, and human-review processes proportionate to risk.
