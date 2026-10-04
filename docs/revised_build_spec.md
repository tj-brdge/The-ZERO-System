# Theme Contagion Graph requirements

## Research question and scope

Which company-relationship layers improve prediction of subsequent substantive
disclosure of an investment theme beyond a company's own prior language and its
industry's adoption pattern?

**Adoption** means the first observed crossing of a predefined threshold of
substantive, company-attributable discussion in the observed document corpus.
It does not date actual business exposure, economic adoption or strategic change.
Network coefficients, forecast improvements and null percentiles describe
predictive associations; they do not establish causal transmission.

- Study the point-in-time S&P 500 from **2021-01-01 through 2026-06-30**.
- Use FMP earnings transcripts and SEC 10-K/10-Q filings.
- Use the `supply`, `ownership`, `coverage` and `text_sim` layers, subject to
  feasibility assessment and explicit deferral in the minimum-version plan.
- Use Python, PostgreSQL and pgvector; follow the package layout and coding conventions.
- Start with AI data-center power demand and eight approved anchors. Substantive
  hyperscale data-center power demand qualifies without an explicit AI reference.
  Generic AI discussion without a power, generation, grid, electrical-equipment
  or cooling connection does not qualify.
- Keep the architecture theme-agnostic, with GLP-1 as a later portability test.

The expected industry sequence is a hypothesis, not ground truth. Labels and
thresholds must never be tuned to reproduce it. The exact theme definition,
anchors and initial passage/retrieval thresholds require source evidence or an
explicitly approved proposal; unspecified values must not be invented.

## Working method

Work one reviewable phase at a time: inspect applicable instructions, code, schema
and fixtures; state scope, missing prerequisites and acceptance checks; run the
applicable offline checks; open one draft PR and report actual results. Stop for
review before the next phase. Setup proceeds through repo hygiene, theme
definition, feasibility, then a minimum-version plan. Database and record-keeping
design follow feasibility results; these setup phases do not build the pipeline.

Never fabricate source data, identifiers, relationships, labels, API responses,
metrics or successful executions. Clearly label synthetic test fixtures and
separate them from source samples, empirical validation and production data.
If credentials, network, a database, model weights or human labels are unavailable,
mark affected checks **blocked** or **not run**, with the reason; finish independent
verifiable work without claiming blocked criteria passed. Report measured coverage
or row counts where applicable, failures, unresolved issues and review decisions.

Scientific choices require approval before implementation. Record proposals in
[decisions.md](decisions.md). Keep refactors behavior-preserving; report discovered
bugs separately rather than hiding scientific/parser/state/model changes in a
move. Use append-only schema migrations and preserve existing offline assertions.
Keep configuration outside code and credentials out of version control.

## Time, provenance and universe

Distinguish economic/effective time (`valid_from`, `valid_to`, `period_end` or
equivalent), `known_at` (public availability of that exact source version),
`ingested_at` (system acquisition) and `computed_at` (derived-artifact creation).
Preserve source versions and corrections; revised contents cannot overwrite an
older version while retaining its earlier `known_at`.

Historical identifiers, classifications, membership and entity attributes need
knowledge-time provenance. Never backdate current FMP attributes or identifiers.
For transcripts, keep call time distinct from verified text/version availability;
missing availability evidence needs an explicit policy and limitation, not a
silent substitution of call date.

Derived features and edges must record source dependencies and the maximum source
`known_at` across required inputs. Keep computation time separate, and select all
inputs using the applicable as-of cutoff. Every run must identify:

- Code commit or source-tree state and full configuration hash.
- Source snapshots and content hashes; parser and chunker versions.
- Theme-package and prompt versions; model and tokenizer revisions.
- Seeds, parameters, upstream run dependencies and training cutoffs.

Frozen modern models provide reproducibility, not historical deployability. Label
the study **retrospective measurement with frozen tools** unless historical model
availability is independently established.

Configure a pre-window warm-up sufficient for every lookback and prior-adoption
status. Flag pre-window adopters, uncertain histories and left-censored observations.
Neither study start nor index entry automatically establishes a first adoption.
Preserve exact membership intervals, distinguish securities from CIK-level
entities, and reconcile historical membership rather than checking only aggregate
counts. Security and company counts are not interchangeable.

Forecast eligibility uses the universe known at the origin. Define exit/censoring
without selecting companies using future membership. For cutoff T, features from
a complete database filtered as of T must match a rebuild after physically removing
source versions unavailable at T, using identical frozen configuration and fitted
artifacts and declared deterministic tolerances.

## Sources and ingestion

Before implementing an endpoint parser, verify current official documentation and
capture a sanitized real response. Check pagination, historical coverage, response
shape, entitlement, timestamp semantics and rate limits. Do not guess fields from
endpoint names or manufacture source fixtures. Keep live calls in ingestion paths;
unit tests need no network, paid APIs or model downloads.

SEC ingestion must follow additional historical submissions files, not just the
recent-filings array. Preserve acceptance timestamps, accession identifiers and raw
filing provenance, distinguish original and amended filings, and retain full filing
text for supply extraction as well as theme-scoring sections. Report failed section
extraction explicitly rather than representing it as empty content.

Maintain idempotency, resumability, retries, compliant identification/rate limiting
and immutable raw-response caching.

## Theme measurement and validation

Use **substantive / peripheral / irrelevant** as the primary labels, retaining
section and speaker-role provenance. Store exact evidence spans and locations,
classification rationale, raw classifier response, parse/validation status and
model/prompt/theme-package versions. Invalid JSON, failed calls and missing text
are explicit errors, never fallback "irrelevant" labels.

Separately record impact (opportunity, adverse impact, mixed, unclear) and activity timing
(realized/current, forecast/planned, conditional risk, unclear). These attributes
must not silently change the adoption definition.

Embedding inputs must be token-aware and respect verified model limits. Character
limits do not guarantee token compatibility; long filing sections must not be
silently truncated. Deduplicate overlapping/repeated evidence before passage-count
thresholds, retaining repetition and source provenance for inspection. Arbitrary
chunk boundaries do not create independent evidence.

Start with a **300-chunk human-label queue, including 100 below the retrieval
threshold**. Save sampling strata, population sizes and inclusion probabilities;
weight population retrieval-loss estimates appropriately. Separate development
from held-out evaluation labels, extend labeling when uncertainty or subgroup
coverage is inadequate, and never treat illustrative prompt examples as held-out
ground truth.

Passage targets are **substantive precision >= 0.85** and **retrieval loss < 10% of
true substantive passages**. Report uncertainty rather than treating point
estimates as conclusive. Also audit company-quarter/events: inspect predicted
adopters and sampled non-adopters, measure adoption-event precision and date error,
audit early adopters carefully, and test sensitivity to chunking and adoption
thresholds. Obtain approval of event-level tolerances before fitting network
models. Measurement validation requires actual human labels.

## Adoption state and risk set

Keep historical adoption, current activity and observability separate. Store
`ever_adopted`, `first_adoption_at`, `first_adoption_quarter`, current-quarter
evidence/activity, source-specific observability/processing coverage and separate
analyst-question counts. Derive compatible state labels from these explicit fields
rather than relying on an ambiguous four-state variable.

Use the approved initial passage-threshold policy on deduplicated eligible evidence.
The event timestamp is when enough publicly available evidence crossed the
threshold: a two-evidence policy may cross at the second item's availability.
Do not automatically use the first passage time or quarter-end. Analyst-only
evidence cannot trigger company adoption.

First-adoption hazard eligibility uses status before the outcome quarter. Include
the first-adoption quarter, remove subsequent quarters, and never allow prior
adopters to re-enter, including companies whose activity has faded.

"Faded" describes activity, not a reversal of historical adoption. It requires two
consecutive sufficiently observed calendar quarters below threshold. Missing
documents are not quiet quarters. Insufficient observability means unknown/missing,
not non-adoption; make exclusion/censoring policy explicit.

## Graph layers

Record edge evidence, dependency lineage, temporal availability, staleness and
missingness. Specify self-edge exclusion, directed/undirected semantics,
union/mutual-neighbor symmetrization, tie handling, minimum similarities,
zero-denominator behavior, missing-layer indicators, expiry/staleness rules and
normalization before graph union. Apply top-k sparsification to similarity layers,
not automatically to observed supply relationships. Report coverage before and
after sparsification. Approve unresolved definitions before implementing them.

### Supply

Preserve supplier -> customer direction and separate upstream/downstream exposures.
Use a tiny directional fixture showing which adopter affects each exposure.
Observed revenue share is nullable; default modeling weights are separate from
observed disclosures. Preserve unresolved and outside-universe counterparties for
coverage reporting. Extract from full filing text, not only selected sections.
Document the licensed-data import hook but leave it unimplemented until a source
is supplied.

### Ownership

Define holder-vector weighting mathematically before implementation. Select the
largest filers using information available at the snapshot. Verify historical
units, amendments, reporting periods and identifier mappings. Use public
availability for `known_at`, not holdings quarter-end. Do not backfill historical
CUSIP mappings from current profiles without provenance. Report mapping coverage
and distinguish missing from zero holdings. Test broadly shared holders and
normalization choices in sensitivity analysis.

### Coverage

Broker ratings/target activity is an activity-overlap proxy unless actual coverage
rosters validate a stronger interpretation. Verify historical endpoints and account
entitlement, normalize broker identities while preserving aliases, and distinguish
absent activity from absent source coverage.

### Text similarity

Specify token-aware Item 1 chunking and deterministic document-vector aggregation.
Use the latest eligible filing at the cutoff. Include sensitivity analysis excluding
theme-bearing passages, and preserve aggregation/model configuration in run lineage.

## Models and nulls

All predictors must use information available at the prediction cutoff. Lag every
predictor, including document volume, own theme scores/peripheral discussion,
analyst-question evidence, industry adoption, exposure/activity indicators and
source-availability features. The strong non-network baseline includes own lagged
language, lagged industry adoption and observability controls.

Compare the sector-only baseline, strong non-network baseline, strong baseline plus
text similarity, strong baseline plus all available layers, individual-layer
additions and leave-one-layer-out ablations. Use identical eligible observations
or explicitly report coverage-induced differences. The feasible minimum version
may defer layers, but must document those deferrals.

Use a complementary log-log first-adoption model. Separate retrospective descriptive
models (which may include quarter fixed effects) from forecasts for unseen quarters.
The initial forecast uses an intercept and strictly lagged features, without an
unseen-quarter fixed effect. Any alternative time baseline must be documented,
versioned and trained on available history only.

Save the complete fitted model, link function, parameter ordering, transformations,
feature definitions, training lineage and diagnostics, not just network coefficients.
Report event counts, convergence, separation, collinearity, coefficient stability
and uncertainty. Include entity-clustered uncertainty and document relevant
shared-time/sector sensitivity checks.

The **adoption reassignment null** must state its hypothesis, reassign identities
among eligible observable companies, preserve declared sector-quarter event counts
and first-adoption consistency, rebuild affected histories/exposures, and
reject/report infeasible draws rather than produce invalid panels.

The **graph rewiring null** must preserve directedness and declared degree
constraints, specify weight/sector-mixing/temporal-persistence treatment, diagnose
what it preserves and destroys, and include stricter sensitivity nulls where feasible.
Keep **500 reassignment and 200 rewiring repetitions** as configurable defaults;
report usable repetitions and failed fits. Null percentiles are diagnostics, not
causal identification.

## Emergence, forecasts and later simulations

Initial emergence reporting includes new adopters, explicitly defined adoption
growth/acceleration, incidence relative to the eligible observed risk set, source
maturation and defined network breadth. Do not present a growth ratio as an
identified reproduction number; provide a descriptive label and explicit formula.

Historical features must not use end-of-study communities. Use a cutoff-available
or previously frozen partition and explain comparability when partitions change.
Validate one-quarter-ahead prediction before multi-quarter Monte Carlo cascades;
first report whether it adds stable value over the strong non-network baseline.

Backtests use rolling origins. Fit/tune every learned component on training
information only, preserve development/held-out label separation, use origin-time
membership and explicit censoring, and report by origin and horizon. Unobserved
future quarters are not negatives. With outcomes ending **2026-06-30**, complete
four-quarter evaluation requires origins no later than **2025-06-30**.

Report ROC AUC when defined, precision-recall metrics, precision at 20 and lift over
the eligible-population rate, Brier score, calibration plots, coverage, event counts
and uncertainty.

Later simulations use the full fitted predictor and inverse complementary log-log
link `p = 1 - exp(-exp(eta))`. Specify frozen/evolving future graphs and exogenous
features; never insert realized future covariates. Update entities simultaneously
within each simulated quarter, record seeds/assumptions, and distinguish process
randomness from parameter/model uncertainty. Listing simulations as a goal does
not authorize proceeding without the one-quarter forecast evidence.

## Recognition lag and portability

Recognition events need actor identity and role, analyst/PM/team attribution,
attribution-effective dates where needed, and evidence connecting the event to a
theme. A position change alone cannot establish recognition. Preserve negative
lags; absent internal events are censored, not zero lag. Use clearly labeled
synthetic fixtures only until real platform data is supplied.

A versioned theme package contains the definition/exclusions, anchors, labeled
prompt examples, retrieval settings, adoption-policy parameters and evaluation
metadata. GLP-1 must work without pipeline code changes and receive its own
calibration/validation rather than inheriting AI-power thresholds without testing.

## Required regression tests

Add these in the relevant implementation phases:

- Future documents, identifiers, classifications and corrections cannot affect earlier features.
- The first-adoption event quarter remains in the hazard risk set; prior adopters never re-enter.
- Missing documents do not cause fading; analyst-only evidence does not cause adoption.
- Duplicate/overlapping evidence does not inflate thresholds.
- Supply exposure direction is correct.
- Long-text aggregation does not silently truncate documents.
- Undefined similarities and missing layers are handled explicitly.
- All forecast predictors respect cutoffs; forecasts do not need unseen quarter fixed effects.
- Later unobserved outcomes are not coded as negatives.
- Repeated ingestion is idempotent and new runs do not overwrite old runs.
- Physically truncated and as-of-filtered feature builds agree within declared tolerances.

## Editorial changes in this revision

- Removed assistant-directed prompt framing, the completed refactor checklist,
  obsolete file references and repository-creation narrative. They were execution
  history rather than standing research requirements; Git retains that history.
- Removed amendment crosswalk tables, duplicate status reports and instructions
  to reconcile an unavailable document. Unspecified scientific values remain open.
- Reworded references to "original" definitions/rules as approved initial policies;
  no missing anchor or threshold was selected or replaced.
- Replaced the old pre-commit approval ceremony with the requested draft-PR phase
  review boundary. Scientific choices still require approval before implementation.
- Placed schema design after feasibility and made layer deferral explicit for the
  minimum version, as requested. The full research/evaluation requirements remain.
- Consolidated repeated prose and lists. No substantive research requirement,
  quantitative target or regression-test obligation was removed.
