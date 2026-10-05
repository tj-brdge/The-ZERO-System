# Open decisions

Record proposals here before implementing affected work. None of these choices
is settled by passing configuration checks. Requirements live in
[the specification](revised_build_spec.md).

- **Naming:** is ZERO an umbrella for studies or the same project's name?
  Awaiting the owner's answer; current repository/package names are unchanged.
- **Theme source:** does a separate original specification exist? If unavailable,
  agree the definition, eight authored draft anchors, examples and adoption rule
  in Phase 2. Do not infer exact missing values.
- **Access:** FMP plan/key availability and a real SEC User-Agent are unconfirmed.
  Phase 3 probes must distinguish unavailable access from missing source coverage.
- **Measurement:** approve retrieval/adoption parameters, duplicate rules,
  label sampling, event precision/date-error tolerances and subgroup coverage.
  - **P04 — Draft proposal (not approved):** Deduplicate by source-location overlap and repeated content before applying the unchanged initial threshold; timestamp the threshold crossing using eligible evidence availability.
    **Needs:** Approve exact duplicate rules, evidence window and event audit precision/date-error tolerances before network fitting.
- **Time and eligibility:** approve warm-up, transcript-availability policy,
  historical membership/identifier reconciliation, observability and exit censoring.
  - **P01 — Draft proposal (not approved):** Exclude versions with unverified public availability from the primary point-in-time analysis; report them separately.
    **Needs:** Verify source evidence and quantify coverage impact before considering a sensitivity policy.
  - **P02 — Draft proposal (not approved):** Derive minimum warm-up from the maximum registered lookback; independently flag incomplete prior-adoption history rather than assuming it is resolved by a fixed duration.
    **Needs:** Approve actual duration after lookbacks and historical source coverage are known.
  - **P03 — Draft proposal (not approved):** Treat insufficiently observed outcomes as unknown; define origin eligibility and exit censoring without consulting future index membership.
    **Needs:** Approve source-specific sufficiency rules and partial-quarter/exit treatment.
- **Graph choices:** approve per-layer similarity/normalization/tie/expiry rules;
  supply weights/direction denominators; mathematical ownership weights, filer
  selection and mappings; broker activity windows/aliases; text aggregation/model
  revisions and theme-exclusion sensitivity. Source feasibility must inform these.
  - **P05 — Draft proposal (not approved):** Evaluate deterministic tie breaking and explicit self-edge exclusion; document minimum similarity and union-versus-mutual symmetrization for each layer.
    **Needs:** Select k, minimum similarity, zero-denominator and symmetrization rules; approve normalization and coverage reporting.
  - **P06 — Draft proposal (not approved):** Keep supplier -> customer edges and separately named upstream/downstream exposure features; preserve null observed revenue share.
    **Needs:** Approve exposure denominator, default modeling weights, expiry and unresolved-counterparty handling; validate direction with a tiny synthetic fixture.
  - **P07 — Draft proposal (not approved):** Compare holder-vector and normalization definitions in a decision memo before selecting a formula.
    **Needs:** Approve mathematical weights, largest-filer selection, shared-holder sensitivity, amendment rules and historical mapping policy after source verification.
  - **P08 — Draft proposal (not approved):** Label the layer an activity-overlap proxy unless rosters validate actual coverage.
    **Needs:** Approve activity windows, alias normalization, historical endpoint and missing-source treatment after entitlement verification.
  - **P09 — Draft proposal (not approved):** Use token-aware Item 1 chunks and a deterministic documented aggregation of every eligible chunk from the latest as-of filing.
    **Needs:** Approve model/tokenizer revisions, token limits, overlap/weighting and theme-passage exclusion sensitivity.
- **Models and evaluation:** approve transformations, origin schedule, event-based
  model size, uncertainty sensitivities, null constraints and deterministic tolerances.
  - **P10 — Draft proposal (not approved):** Begin with the required intercept and strictly lagged features; use the strong non-network baseline before assessing graph additions.
    **Needs:** Approve transformations, tuning, origin schedule, uncertainty and shared-time/sector sensitivity design using only training information.
  - **P11 — Draft proposal (not approved):** Specify constrained adoption reassignment and directed rewiring before writing either algorithm.
    **Needs:** Approve feasible sector-quarter event constraints, degree/weight/sector/temporal rules, failed-draw handling and sensitivity nulls.
  - **P13 — Draft proposal (not approved):** Compare complete-as-of and physically truncated builds using identical frozen configuration and fitted artifacts.
    **Needs:** Approve numeric tolerance by output type before testing; exact equality where data are discrete.
- **Emergence:** approve growth/acceleration/breadth formulas, denominator behavior
  and community comparability.
  - **P12 — Draft proposal (not approved):** Report new adopters and incidence with explicit observed eligible-risk-set denominators.
    **Needs:** Approve growth/acceleration/breadth formulas, zero-denominator handling and partition comparability; do not use an identified reproduction-number claim.
- **Later data:** licensed supply imports and attributed internal recognition
  events lack supplied sources; model weights and human labels are also pending.

Next is Phase 2 after review of the Phase 1 draft PR. Feasibility is Phase 3;
minimum-version choices and decision ownership are Phase 4. Database and
record-keeping design follow feasibility, not the other way around.
