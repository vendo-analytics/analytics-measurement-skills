# Create a local tracking library

Status: Candidate for V1; not implemented or a committed release requirement.
Audience: Repository maintainers.

## Task and customer outcome

Create a local tracking library that centralizes application tracking and sends events to multiple destinations. Application code emits an agreed event once; a central configuration owns routing and destination mappings. Adding or changing a destination should not require editing every event call site.

This is why the library is being considered for V1: it could give customers and coding agents a consistent implementation boundary from their first tracked event. The task is useful independently of any hosted platform or migration.

## Scope to evaluate

- One application-facing tracking interface with explicit event, identity, and consent semantics.
- Central destination selection and mappings, using supported SDKs or an existing CDP/tag layer where appropriate.
- Environment-aware initialization, isolated destination failures, and prevention of duplicate bindings or parallel delivery to the same destination.
- Local debugging that shows what was emitted and routed, without claiming destination receipt from a local log.
- A small setup surface that agents can inspect, configure, and test in the customer's actual codebase.

A local library runs within the application; it does not require customers to operate a separate collector, scheduler, or queue service. Direct client delivery is appropriate only where the destination supports it. Private credentials remain server-side, including for native apps. An existing supported backend route can be used when necessary; unsupported direct delivery must be explicit.

## Reuse investigation

Inspect the existing tracking SDK and real callers before choosing a package or creating another implementation. Compare extending its public interface and delivery boundary with extracting reusable behavior. Trace affected consumers before changing any exported contract.

Historical source review on 2026-09-28 examined tracker commit `62224a996dd90cad6f9863aecec7e488ddf0c199`: the browser SDK exposes event and identity methods, requires a write key, and posts batches to an ingestion endpoint. Destination routing was in that service, not a local direct-destination interface. This establishes a gap to investigate, not a verified capability of a deployed or published package.

Sources: [existing SDK](https://github.com/vendo-analytics/vendo-js-tracker/blob/62224a996dd90cad6f9863aecec7e488ddf0c199/packages/sdk-js/src/index.ts), [SDK documentation](https://github.com/vendo-analytics/vendo-js-tracker/blob/62224a996dd90cad6f9863aecec7e488ddf0c199/packages/sdk-js/README.md), and [existing destination registry](https://github.com/vendo-analytics/vendo-js-tracker/blob/62224a996dd90cad6f9863aecec7e488ddf0c199/packages/ingest-api/src/destinations/factory.ts).

## Proposed acceptance criteria

- One real application action produces one canonical event routed to two selected, supported destinations; each final destination independently verifies receipt.
- Adding or removing a destination changes central configuration, while business-event call sites remain stable.
- Existing CDP/tag-manager paths retain one delivery owner per event and destination.
- Identity changes, consent denial/revocation, logout, and environment separation preserve the agreed contract.
- A failed destination does not prevent the business action or another independent destination's delivery.
- No private destination credential appears in web or native bundles.
- Supported SDK retry/buffering behavior is documented and tested; the library does not promise global exactly-once delivery or guaranteed background flushing.
- Setup, local debugging, and an actionable unsupported-destination result are demonstrated in the chosen application runtime.

## Decisions before implementation

- Which application runtime should validate the first slice? The skills' broad platform coverage does not require one library to support every runtime on day one.
- Which existing module should own the interface and packaging? Confirm this with the Tracking owner after tracing the implementation.
- Which real destinations demonstrate direct delivery and an existing routed path? Evaluation choices must not become an allowlist for the generalized skills.
- Which capabilities justify a maintained library over a small existing application analytics module?
- Does the demonstrated benefit justify inclusion in V1, and who maintains compatibility with supported SDK versions?

These are open decisions, not assumed architecture. Keep this task outside installed skills and customer onboarding until its scope is agreed and the implementation is verified.
