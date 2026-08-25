# Architecture

## Responsibility boundary

The application may collect inputs and display state. AdDisclosureCheck owns the bounded on-chain record, authorization rules, semantic consensus call, and consequential state transition. There is no hidden backend or autonomous source collector.

## State machine

READY_FOR_REVIEW -> NEEDS_REVISION -> READY_FOR_REVIEW, or READY_FOR_REVIEW -> CLEARED.

## Storage model

The contract stores creator, campaign context, disclosure rules, an append-only revision array, phase, last decision, and review count. Text is line-ending-normalized and length-bounded before storage.

## Consensus boundary

The leader serializes only stored case data into canonical JSON and requests an exact JSON schema. Validators independently run the same prompt and normalization path. A validator accepts only an allowed, structurally valid value that exactly matches its own result. Exceptions and malformed model output fail closed.

## Authorization and invariants

Only the creator can append a requested revision. Review is permissionless; a revision can be reviewed only once in its current phase.

## Reuse and distinctness

Deploy one instance per campaign or disclosure policy. Each instance supports up to five revisions, so it is reusable across drafts without erasing its audit trail.

This is a revision-and-clearance lifecycle, not a renamed one-shot classifier: it preserves multiple drafts, gates who may revise, and terminates only on a clear disclosure.
