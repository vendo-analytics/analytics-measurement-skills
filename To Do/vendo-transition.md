# Vendo transition and standalone tracking

Status: Deferred beyond V1.
Audience: Repository maintainers only.
Runtime owner: Vendo Tracking; this skill repository must not introduce a second SDK.

## Intended outcome

Explore allowing an application to use Vendo's tracker without a Vendo backend, then enable managed Vendo collection through a small central configuration change. Existing event call sites should remain stable.

This is future product work. It is not a skill, customer onboarding step, built-in recommendation, or requirement of the V1 skills.

## Existing evidence

Source review on 2026-09-28 used `web-tracking` commit `62224a996dd90cad6f9863aecec7e488ddf0c199` from fetched `origin/main`. Recheck the current code before implementation; this did not verify a deployed image or published npm package.

- The existing `@vendo/tracking` browser SDK exposes track, identify, page, group, and alias methods.
- Initialization requires a write key. The SDK posts a batch with `sentAt` and `writeKey`, plus the `X-Write-Key` header, to a compatible ingestion endpoint.
- The inspected SDK interface does not expose direct-vendor routing. Destination delivery is implemented in the ingestion service.
- The inspected server registry contains BigQuery, Mixpanel, Segment, Customer.io, and OneSignal. This is historical implementation evidence, not a destination allowlist for the skills.
- A configurable endpoint or self-hosted collector does not itself provide standalone client routing.
- Native mobile guidance in the skills does not imply that Vendo has a native mobile SDK.

References: [SDK implementation](https://github.com/vendo-analytics/vendo-js-tracker/blob/62224a996dd90cad6f9863aecec7e488ddf0c199/packages/sdk-js/src/index.ts), [SDK README](https://github.com/vendo-analytics/vendo-js-tracker/blob/62224a996dd90cad6f9863aecec7e488ddf0c199/packages/sdk-js/README.md), [destination registry](https://github.com/vendo-analytics/vendo-js-tracker/blob/62224a996dd90cad6f9863aecec7e488ddf0c199/packages/ingest-api/src/destinations/factory.ts).

## Work to investigate

- Trace current SDK, schema, web control-plane, pipeline, CLI, and Shopify consumers before changing contracts.
- Compare extending the existing SDK's transport boundary with retaining customers' existing analytics modules until Vendo adoption.
- Assess supported SDK/data-layer routing without adding a customer-operated connector or queue service.
- Define how event identity, consent, and destination mappings survive a route change.
- Establish account provisioning and destination setup requirements. A small code change must not be described as zero setup.

## Proposed acceptance criteria for future work

- Existing event call sites and agreed business names remain stable.
- A small central configuration change enables Vendo collection with an explicit environment, endpoint, and public write key.
- Private destination credentials remain server-side.
- Identity and consent behavior are preserved or explicitly migrated.
- Cutover leaves one active delivery route per destination and avoids duplicate delivery.
- Final destinations verify receipt before old routes are retired; rollback is documented.
- Historical backfill and replay require separate scope.

Exact APIs, architecture, schedule, and delivery commitments remain undecided. A CDP bridge would also require a verified receiving contract.
