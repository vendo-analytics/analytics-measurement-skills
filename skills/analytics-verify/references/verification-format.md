# Verification records

Create `verification/<run-id>/report.md` and evidence files in the customer's analytics workspace when the run starts. Choose a unique timestamp-based run ID. Do not overwrite earlier results.

## Run header

Record run ID, time with UTC offset, application/build revision, tracking-plan revision or saved snapshot/hash, environment, target accounts/routes, browser/device/OS, test identity references, configuration versions when available, and access limitations. A native simulator run and a physical-device run are different evidence.

## Results

Use a compact table: case ID, event/route, status, actual observation, and evidence link. Give detailed cases their own stable headings.

| Status | Meaning |
| --- | --- |
| Pass | The case's actual assertion is supported by the recorded evidence |
| Fail | An evaluable observation contradicts the expected outcome |
| Blocked | Required access/evidence is unavailable, or delivery cannot yet be determined within the bounded window |
| Not run | The case was not attempted |

For each case record steps, expected values, actual values, relevant emission/transport/receipt observations, correlation identifiers, observation window, and timestamps. Keep receipt checks per final destination. One destination's failure must not erase another's result. A negative test records observable absence and its window instead of pretending there is a receipt.

Use relative evidence links, such as `evidence/TC-001-destination.png` or `evidence/TC-001-receipt.json`, only when those files exist. Prefer sanitized structured API output for API evidence and a screenshot for UI evidence. Record query/filter context needed to interpret the result. Exclude tokens and unrelated customer records; preserve the minimum correlation needed to prove the assertion.

## Summary and follow-up

Count actual case results. Identify failures, blocked prerequisites, untested scope, affected code/configuration owners, and the next bounded action. Separate what the agent observed from what a person reported. Explain which cases changed since the previous comparable run and why.

Evidence belongs to the recorded revision. Never rewrite an old Pass to imply it proves a newly changed implementation. Corrections to a past report are explicit annotations; reruns have new IDs. Link the latest relevant run from the workspace README without maintaining a competing copy of the results.
