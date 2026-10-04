# Theme Contagion Graph — revised build specification

Status: **new-project foundation prepared; original-specification reconciliation
remains open**. Prepared 2026-10-04 for
[`tj-brdge/The-ZERO-System`](https://github.com/tj-brdge/The-ZERO-System).

The repository cloned with no commits, refs, or working-tree files. The user then
clarified: “We are building them together :-)”. This authorizes treating the work
as a new project rather than waiting for nonexistent legacy source. The first
step therefore creates a minimal Python package, configuration, offline CLI and
new foundation tests. No legacy refactor or assertion-preservation claim is made.
The first-execution limit and approval-before-commit rule remain in effect.

The original build specification referenced in the attachment was not supplied.
Its exact package layout, eight anchors, original threshold values and original
step numbers cannot be recovered from the amendments. This document preserves
all supplied requirements, but does **not** claim integration with that missing
specification. Missing scientific inputs remain explicit, unimplemented settings.
The newly chosen layout is recorded separately in `docs/decisions.md`.

## Authority and provenance

1. The user designated The-ZERO-System as the target repository.
2. The supplied amendment text below takes precedence over conflicting original
   requirements; original requirements not explicitly changed remain required.
3. The original specification is unavailable. Its original step numbers and exact
   acceptance criteria cannot yet be mapped without inventing traceability.
4. Proposed choices in [decisions.md](decisions.md) are pending approval and do not
   amend the requirements.
5. The user's clarification supersedes the assumption that an existing implementation
   is available. The completed new-project foundation was approved for commit and
   push on 2026-10-04. Later steps still require separate authorization.

Source: user attachment `pasted-text.txt`, SHA-256
`c4033ec6cb906d5f77fed3f937d0ccd36c05df9c154dd9b223d4d2d434c6caa5`.
The text under “Supplied requirements” is reproduced without edits so its details,
including the first-execution scope, remain auditable.

## Traceability and acceptance changes

The section references in this table refer to the **supplied amendments**, not to
unknown original step numbers. Every row still requires reconciliation against the
original specification. The table is a navigation aid; the full requirements below
are authoritative.

| Amendment section | Retained requirement or intended scope | Explicit amendment / changed acceptance |
| --- | --- | --- |
| 1 | Name; point-in-time S&P 500, 2021-01-01 through 2026-06-30; FMP transcripts and SEC 10-K/10-Q; four layers; Python/PostgreSQL/pgvector; AI-power theme and eight original anchors; GLP-1 portability | Disclosure-threshold adoption; predictive association claims; hyperscale data-center power qualifies without explicit AI; expected industry sequence is a hypothesis |
| 2 | Incremental execution | One approved step at a time; inspect, state changes/checks, test and report; no commit before approval; no fabricated evidence |
| 3 | Historical study and reproducibility | Separate effective, knowledge, ingestion and computation times; immutable source versions and lineage; warm-up/censoring; security/entity distinction; origin-time universe; physical-truncation equivalence test |
| 4 | FMP and SEC ingestion | Official documentation and sanitized real responses before parsers; verify entitlement/coverage/pagination; historical SEC submissions and full text; explicit extraction failures; immutable caches and idempotency |
| 5 | Primary labels; initial 300-label queue with 100 below threshold; precision >= 0.85; retrieval loss < 10% | Weighted uncertainty-aware evaluation and held-out labels; exact evidence and explicit errors; deduplication/token limits; company-quarter/event audit and separately approved tolerances |
| 6 | Initial configurable passage threshold and compatible state labels | Separate historical adoption/activity/observability; threshold-crossing availability; analyst-only exclusion; include event quarter, exclude later quarters; observed-calendar-quarter fading |
| 7 | Supply, ownership, coverage, text_sim | Directional supply exposures; no blanket top-k for observed supply; as-of edge provenance and missingness; verified ownership units/mappings; activity-overlap coverage proxy; deterministic full-text aggregation; approve unresolved definitions |
| 8 | Complementary log-log model; entity-clustered uncertainty; 500/200 null defaults | Lag every predictor; strong baseline and ablations; common eligible observations; distinguish descriptive and forecast time specifications; full fitted artifacts; explicit valid nulls and failures; no causal claims |
| 9 | Emergence and forecasting objectives | Defined incidence/growth/source maturation/breadth; no identified reproduction number; as-of partitions; one-quarter forecast gate before cascades; rolling-origin metrics, censoring, uncertainty; four-quarter origins no later than 2025-06-30 |
| 10 | Recognition-lag interface and theme portability | Actor attribution and theme evidence; negative lags and censoring; versioned theme packages; independent GLP-1 calibration |
| 11 | Regression verification | Required leakage, state, direction, aggregation, missingness, forecast, ingestion, run immutability and truncated-database tests, in their relevant later phases |
| 12 | Foundation/refactor only | Inspect six named files; run baseline; integrate documents; preserve assertions/constants/behavior during layout/config/CLI move; no scientific or schema changes; report and stop for approval |

## Foundation acceptance status

- Target repository located and cloned; empty starting state confirmed.
- Applicable repository instructions: none present in the checkout or checked
  ancestor `AGENTS.md` locations.
- Baseline tests, source moves, old-assertion preservation and unchanged-constant
  comparisons: **not applicable to the confirmed new project**.
- New minimal foundation: `src/theme_contagion_graph/`, packaged `config.yaml`,
  `cli.py`, module/console entry points, `.env.example`, pytest tests and packaging.
- The configuration includes only supplied values and explicit unresolved
  scientific inputs. CLI commands inspect/validate configuration only.
- Original-specification integration and exact original step/layout/anchor
  recovery: **unresolved**, not a claim of completed reconciliation.
- No database migration, source ingestion, embedding, classifier, state machine,
  graph construction, fitted model or simulation has been implemented.
- Foundation commit/push approved on 2026-10-04; subsequent implementation still
  requires step authorization and coordination with the user's incoming partner.

See [foundation_report.md](foundation_report.md) for actual checks and results.

## Supplied requirements

You are implementing the “Theme Contagion Graph” research prototype in an existing repository.

Read the attached original build specification and the actual repository before making changes. Treat the requirements below as explicit amendments: where they conflict with the original specification, this prompt takes precedence. Preserve all original requirements not explicitly changed here.

Your job is to build a defensible, reproducible research system—not merely produce plausible-looking results.

Do not implement the entire project in one pass. Your first execution is limited to the foundation/refactor task described at the end of this prompt.

# 1. Research objective and claim boundaries

The primary research question is:

“Which company-relationship layers improve prediction of subsequent substantive disclosure of an investment theme, beyond a company’s own prior language and its industry’s adoption pattern?”

Use “adoption” internally to mean:

“The first observed crossing of a predefined threshold of substantive, company-attributable discussion in the observed document corpus.”

Do not equate this with the first date of actual business exposure, economic adoption, or strategic change.

Retain the project name, but describe network-model results as predictive associations. Do not claim that coefficients, null-model percentiles, or forecast improvements establish causal transmission.

Retain the original:
- Point-in-time S&P 500 study window: 2021-01-01 through 2026-06-30.
- Documents: FMP earnings transcripts and SEC 10-K/10-Q filings.
- Layers: supply, ownership, coverage, text_sim.
- Python/PostgreSQL/pgvector stack, repository layout, and coding conventions.
- AI data-center power demand definition and eight supplied anchors.
- Theme-agnostic architecture, with GLP-1 as a later portability test.

For the first theme, substantive hyperscale data-center power demand qualifies even without an explicit AI reference. Generic AI discussion without the defined power, generation, grid, electrical-equipment, or cooling connection does not qualify.

The expected industry sequence is a hypothesis to investigate, not ground truth to reproduce. Never tune labels or thresholds to force that sequence.

# 2. Execution discipline

Work one approved step at a time.

Before implementing a step:
- Inspect the relevant existing code, schema, fixtures, and repository instructions.
- State the intended changes and acceptance checks.
- Identify prerequisites that are missing.

After implementing a step:
- Run applicable offline tests.
- Report changes, actual test results, data coverage or row counts where applicable, unresolved issues, and decisions needing review.
- Stop for approval.

Do not commit until the completed step is approved. Do not start the next step without authorization.

Never fabricate source data, identifiers, relationships, labels, API responses, metrics, test results, or successful executions.

Synthetic fixtures are allowed for unit tests when clearly labeled as synthetic. They must never be presented as real API fixtures, empirical validation, or production data.

If credentials, network access, a database, model weights, or human labels are unavailable, report the affected work as blocked or not run. Complete independent work that can be verified, but do not claim the blocked acceptance criteria passed.

# 3. Point-in-time and provenance contracts

Implement explicit distinctions between:
- Economic/effective time: valid_from, valid_to, period_end, or equivalent.
- known_at: when that exact source version became publicly available.
- ingested_at: when this system acquired it.
- computed_at: when a derived artifact was produced.

Preserve source versions and corrections. Do not overwrite an earlier record and retain its earlier known_at for revised contents.

Add knowledge-time provenance to historical identifiers, classifications, membership information, and entity attributes. Do not silently backdate present-day FMP attributes or identifiers into history.

For transcripts, distinguish the call timestamp from verified availability of the transcript text/version. Missing availability evidence requires an explicit policy and limitation; do not silently substitute the call date.

For derived features and edges:
- Record source dependencies.
- Record the maximum source known_at across required inputs.
- Keep computation time separate from source availability.
- Select all inputs using the relevant as-of cutoff.

Every run must identify:
- Code commit or source-tree state.
- Full configuration hash.
- Source snapshots and content hashes.
- Parser and chunker versions.
- Theme-package and prompt versions.
- Model and tokenizer revisions.
- Seeds and parameters.
- Upstream run dependencies and training cutoffs.

Pinning a modern model makes the analysis reproducible, not historically deployable. Label the study as retrospective measurement with frozen tools unless historical model availability is separately established.

Add a configurable pre-window warm-up sufficient to initialize every lookback and prior-adoption status. Flag pre-window adopters, uncertain histories, and left-censored observations. Do not treat index entry or the study start as an automatic first adoption.

Preserve exact membership intervals and distinguish securities from CIK-level entities. Validate membership with historical reconciliation, not only aggregate counts. Do not assume that security counts and company counts are interchangeable.

For forecasts, use the universe known and eligible at the forecast origin. Specify exit/censoring treatment without selecting companies using future membership.

Required point-in-time regression test:
For cutoff T, compare features built from the complete database with as-of filtering against features rebuilt after physically removing source versions unavailable at T. With the same frozen configuration and fitted artifacts, results must match within declared deterministic tolerances.

# 4. Ingestion and external API requirements

Verify current official documentation and capture a sanitized real response before implementing a parser for an external endpoint. Verify pagination, historical coverage, response shape, entitlement, timestamp semantics, and rate limits.

Do not guess an endpoint’s fields from its name or manufacture a fixture.

Keep live calls in ingestion paths. Unit tests must not require network access, paid APIs, or model downloads.

SEC ingestion must:
- Follow additional historical submissions files, not only the recent-filings array.
- Preserve acceptance timestamps, accession identifiers, and raw filing provenance.
- Distinguish original and amended filings.
- Retain full filing text for supply-chain extraction, in addition to the sections used for theme scoring.
- Report failed section extractions rather than treating them as empty content.

Maintain idempotency, resumability, retries, compliant identification/rate limiting, and immutable raw-response caching.

# 5. Theme measurement and evaluation

Preserve substantive/peripheral/irrelevant as the primary labels and retain section and speaker-role provenance.

Store:
- Exact evidence spans and source locations.
- Classification rationale.
- Raw classifier response.
- Parse/validation status.
- Model, prompt, and theme-package versions.

Invalid JSON, failed model calls, or missing text must be explicit error states—not converted to “irrelevant.”

Add separate attributes for:
- Opportunity, adverse impact, mixed, or unclear.
- Realized/current activity, forecast/planned activity, conditional risk, or unclear.

These attributes must not silently change the primary adoption definition.

Use token-aware embedding inputs and verify the selected model’s actual limits. Never assume a character limit guarantees token compatibility or embed an entire long filing section through silent truncation.

Deduplicate overlapping and repeated evidence before applying passage-count thresholds. Preserve repetition and source provenance for inspection. Arbitrary chunk boundaries must not create independent evidence.

Retain the initial 300-chunk human-label queue, including 100 below the retrieval threshold, but:
- Save sampling strata, population sizes, and inclusion probabilities.
- Use appropriate weighting for population-level retrieval-loss estimates.
- Separate development labels from held-out evaluation.
- Extend labeling when uncertainty or subgroup coverage is inadequate.
- Never use illustrative prompt examples as held-out ground truth.

Retain the original passage-level acceptance targets:
- Substantive precision at least 0.85.
- Retrieval loss below 10% of true substantive passages.

Report uncertainty rather than treating point estimates as conclusive.

Also require a company-quarter/event audit:
- Inspect predicted adopters and sampled non-adopters.
- Measure adoption-event precision and adoption-date error.
- Audit early adopters particularly carefully.
- Test sensitivity to chunking and adoption thresholds.

Propose event-level tolerances for approval before fitting the network model. Do not claim measurement validation without actual human labels.

# 6. State model and risk-set construction

Separate historical adoption, current activity, and observability.

Store at least:
- ever_adopted.
- first_adoption_at.
- first_adoption_quarter.
- current-quarter evidence/activity.
- source-specific observability and processing coverage.
- separate analyst-question evidence counts.

Keep the original passage-threshold rule as the initial configurable policy, but apply it to deduplicated, eligible evidence.

The adoption timestamp is when enough publicly available evidence existed to cross the threshold. For a two-evidence rule, this may be the availability of the second qualifying item. Do not automatically use the first passage timestamp or quarter-end.

Analyst-only evidence must not trigger company adoption.

For the first-adoption hazard:
- Determine eligibility using status before the outcome quarter.
- Include the quarter in which first adoption occurs.
- Remove subsequent quarters from the first-adoption risk set.
- Do not allow faded companies to re-enter as first-time adopters.

“Faded” is a descriptive activity status, not reversal of historical adoption. It requires two consecutive sufficiently observed calendar quarters below threshold. Missing documents must not count as quiet quarters.

Insufficient observability is unknown/missing, not evidence of non-adoption. Make the exclusion/censoring policy explicit.

Preserve the original state labels where useful for compatibility, but derive them from explicit fields rather than relying on an ambiguous four-state variable.

# 7. Graph-layer contracts

Record edge evidence, dependency lineage, temporal availability, staleness, and missingness.

Apply top-k sparsification to similarity layers, not automatically to observed supply relationships.

Specify:
- Self-edge exclusion.
- Directed versus undirected semantics.
- Union versus mutual-neighbor symmetrization.
- Tie handling.
- Minimum similarity thresholds.
- Zero-denominator behavior.
- Missing-layer indicators.
- Edge expiry/staleness rules.
- Layer normalization before graph union.

Report coverage before and after sparsification.

Supply:
- Preserve commercial direction as supplier -> customer.
- Implement separate upstream and downstream exposure features.
- Add a tiny directional fixture proving which adopter affects which exposure.
- Keep observed revenue share nullable.
- Store any default modeling weight separately from observed disclosures.
- Preserve unresolved and outside-universe counterparties for coverage reporting.
- Extract from full filing text, not only selected sections.
- Keep the licensed-data import hook documented and unimplemented until a source is supplied.

Ownership:
- Define the holder-vector weighting mathematically before implementation.
- Select the largest filers using only information available at the snapshot.
- Verify historical units, amendments, reporting periods, and identifier mappings.
- Use public availability, not quarter-end holdings dates, for known_at.
- Do not backfill historical CUSIP mappings from current profiles without provenance.
- Report mapping coverage and missing holdings separately from zero holdings.
- Test sensitivity to broadly shared holders and normalization choices.

Coverage:
- Treat broker ratings/target activity as an activity-overlap proxy unless actual coverage rosters validate the stronger interpretation.
- Verify usable historical endpoints and account entitlement.
- Normalize broker identities and preserve aliases.
- Distinguish absent activity from absent source coverage.

Text similarity:
- Specify token-aware Item 1 chunking and deterministic document-vector aggregation.
- Use the latest eligible filing as of the cutoff.
- Add a sensitivity analysis excluding theme-bearing passages.
- Preserve the aggregation/model configuration in run lineage.

Do not silently select unresolved scientific definitions. Propose them in the decision log for approval before implementing the affected step.

# 8. Modeling and nulls

Construct all predictors using information available at the prediction cutoff.

Lag every predictor—not only network exposure—including:
- Document volume.
- Own theme scores and peripheral discussion.
- Analyst-question evidence.
- Industry adoption rates.
- Exposure/activity indicators.
- Source-availability features.

Build a strong non-network baseline using the company’s own lagged language, lagged industry adoption, and observability controls.

Then compare:
1. Sector-only baseline.
2. Strong non-network baseline.
3. Strong baseline plus text similarity.
4. Strong baseline plus all available layers.
5. Individual-layer additions and leave-one-layer-out ablations.

Use identical eligible observations for comparable models, or explicitly report coverage-induced differences.

Keep the complementary log-log first-adoption model.

Separate:
- A retrospective descriptive specification that may include quarter fixed effects.
- A forecasting specification that can be evaluated at an unseen future quarter.

For the initial forecast specification, use an intercept and strictly lagged features; do not require an unseen quarter fixed effect. Any alternative time baseline must be documented, versioned, and trained using only available history.

Save the complete fitted model, link function, parameter ordering, transformations, feature definitions, training data lineage, and diagnostics—not just network coefficients.

Report event counts, convergence, separation, collinearity, coefficient stability, and uncertainty. Include the original entity-clustered uncertainty estimate and document relevant shared-time/sector sensitivity checks.

Rewrite the nulls explicitly:

Adoption reassignment null:
- Define the hypothesis being tested.
- Reassign adopter identities among eligible, observable companies.
- Preserve declared sector-quarter event counts and first-adoption consistency.
- Rebuild affected histories and exposures.
- Reject/report infeasible draws rather than producing invalid panels.

Graph rewiring null:
- Preserve directedness and the declared degree constraints.
- Specify treatment of weights, sector mixing, and temporal persistence.
- Diagnose what the null preserves and destroys.
- Include stricter sensitivity nulls where feasible.

Retain 500 and 200 repetitions as configurable defaults, but report usable repetitions and failed fits.

Null percentiles are diagnostics, not causal identification.

# 9. Emergence and forecasting

For initial emergence reporting, use:
- New adopters.
- Explicitly defined adoption growth and acceleration.
- Incidence relative to the eligible observed risk set.
- Source maturation.
- Clearly defined network breadth.

Do not present the originally proposed R_t as an identified reproduction number. Use a descriptive label and explicit formula for any growth ratio.

Historical as-of features must not use end-of-study communities. Use a partition available at the relevant cutoff or a previously frozen partition. Explain comparability when partitions change.

Implement and validate one-quarter-ahead prediction before multi-quarter Monte Carlo cascades.

Backtesting must:
- Use rolling origins.
- Fit/tune all learned components only on training information.
- Preserve label-development/held-out separation.
- Use origin-time membership and explicit censoring.
- Report metrics by origin and horizon.
- Avoid labeling unobserved future quarters as non-adoption.

With outcomes ending 2026-06-30, complete four-quarter evaluation requires origins no later than 2025-06-30.

Report:
- ROC AUC when defined.
- Precision-recall metrics.
- Precision at 20 and lift over the eligible-population rate.
- Brier score.
- Calibration plots.
- Coverage, event counts, and uncertainty.

For later simulations:
- Use the full fitted predictor and inverse complementary log-log link:
  p = 1 - exp(-exp(eta)).
- Specify which future graphs and exogenous features are frozen or evolved.
- Never insert realized future covariates.
- Update entities simultaneously within each simulated quarter.
- Record seeds and simulation assumptions.
- Distinguish process randomness from parameter/model uncertainty.

Do not proceed to cascades merely because they were listed in the original spec. First report whether one-quarter forecasts add stable value over the strong non-network baseline.

# 10. Recognition lag and theme portability

Extend the recognition-event interface to include actor identity, actor role, analyst/PM/team attribution, attribution-effective dates where needed, and evidence linking an event to a theme.

A position change alone must not automatically establish theme recognition.

Preserve negative recognition lags. Treat no observed internal event as censored, not zero lag. Use clearly labeled synthetic fixtures only until real platform data is supplied.

Define a versioned theme package containing:
- Definition and scope exclusions.
- Anchors.
- Labeled prompt examples.
- Retrieval settings.
- Adoption-policy parameters.
- Evaluation metadata.

GLP-1 must run without pipeline code changes, but must receive theme-specific calibration and validation rather than inheriting AI-power thresholds unquestioningly.

# 11. Required regression tests, added in the relevant phases

Include tests proving that:
- Future documents, identifiers, classifications, and corrections cannot affect earlier features.
- A first-adoption event remains in the hazard risk set.
- Prior adopters never re-enter as first adopters.
- Missing documents do not trigger fading.
- Analyst-only evidence does not trigger adoption.
- Duplicate/overlapping evidence does not inflate thresholds.
- Supply exposure direction is correct.
- Long-text aggregation does not silently truncate the document.
- Undefined similarities and missing graph layers are handled explicitly.
- All forecasting predictors respect the cutoff.
- Forecasts do not depend on unseen quarter fixed effects.
- Later unobserved outcomes are not coded as negatives.
- Repeated ingestion is idempotent.
- A new run does not overwrite an old run.
- Truncated-database and as-of-filtered feature builds agree.

# 12. First execution: foundation/refactor only

Do the following now, and nothing from later implementation phases:

1. Read applicable repository instructions and inspect the actual files, especially:
   - 001_schema.sql
   - 002_schema_additions.sql
   - fmp_client.py
   - step2_universe.py
   - step3_transcripts.py
   - test_offline.py

2. Establish a baseline by running the existing offline tests when feasible. Report pre-existing failures separately.

3. Create docs/revised_build_spec.md integrating the original specification with these explicit amendments. Preserve traceability to the original steps and identify changed acceptance criteria.

4. Create docs/decisions.md distinguishing:
   - Original requirements retained.
   - Changes explicitly required by this prompt.
   - Proposed defaults requiring later approval.
   - Blocked prerequisites and unresolved source questions.

5. Perform the original behavior-preserving refactor:
   - Move code into the requested package layout.
   - Convert offline tests to pytest while preserving their assertions.
   - Move existing constants into config.yaml without changing their values or behavior.
   - Add/update .env.example without including secrets.
   - Wire the existing functionality through cli.py.
   - Add only the packaging/import/configuration support needed for this refactor.

6. Do not alter scientific logic, membership reconstruction, transcript parsing, state definitions, database semantics, or model behavior during this move.
   - Record discovered bugs in the backlog.
   - Do not hide bug fixes inside the refactor.
   - Keep schema changes for later append-only migrations.

7. Run the refactored offline tests and relevant import/configuration checks.

8. Stop and report:
   - Files inspected.
   - Files changed and why.
   - Baseline versus final test results.
   - Any behavior differences.
   - What was not run and why.
   - Unresolved decisions.
   - The proposed next step and its acceptance checks.

Do not implement new ingestion, embeddings, classification, graph construction, modeling, or simulations in this first execution. Do not claim data coverage or model performance that has not been measured. Wait for approval after the refactor report.
