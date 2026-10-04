# Theme Contagion Graph — decisions and prerequisites

Status: new-project foundation, 2026-10-04. The target repository was empty when
cloned. The user clarified that we are building it together from scratch. No
unresolved scientific defaults have been selected or applied.
“Retained” below means required by the supplied amendments, not independently
verified against the unavailable original specification.

## New-project clarification and foundation implementation choices

The user clarified “We are building them together :-)” after the empty repository
was reported. This supersedes the assumption that legacy source is available.
Accordingly, waiting for existing code is no longer a prerequisite to the first
step. The limits on later scientific implementation and approval before commits
remain unchanged.

The following routine engineering choices make the new foundation reviewable;
they are not claimed to come from the missing original specification:

- Python >= 3.11, setuptools packaging with a `src/theme_contagion_graph/` layout.
- A packaged `config.yaml` supplies defaults via `importlib.resources`, so the
  installed CLI works independently of the current directory.
- PyYAML safe loading with duplicate-key, shape, date and numeric validation;
  configuration-file SHA-256 includes the exact bytes, including comments.
- `cli.py`, the package module and the `theme-contagion` console script expose
  `check-config` and `show-config`. No placeholder pipeline commands pretend to run.
- Default study dates, layer names, label-queue counts, passage evaluation targets,
  anchor count and null repetitions come only from the supplied amendments.
- Missing theme definition, anchors, warm-up and retrieval/adoption settings stay
  unresolved; successful configuration validation is not scientific readiness.
- Empty `.env.example` values document anticipated FMP/PostgreSQL/SEC integration.
  These are newly proposed variable names; no environment loading or service use
  is implemented in this step.
- Tests use synthetic configuration values only. No source/API fixtures or human
  ground truth are invented. Later-phase regression tests remain deferred.
- Dependency bounds support installation; the foundation report records tested
  versions. Frozen models and complete future run/dependency lineage remain later
  work, and are not implied by the configuration checksum.

## Original requirements retained

| ID | Requirement | Verification still needed |
| --- | --- | --- |
| R01 | Theme Contagion Graph project name and theme-agnostic architecture | Original naming and interface conventions |
| R02 | Point-in-time S&P 500 study, 2021-01-01 through 2026-06-30 | Original membership implementation and historical fixtures |
| R03 | FMP earnings transcripts and SEC 10-K/10-Q filings | Original ingestion code and source contracts |
| R04 | Python, PostgreSQL, pgvector, original layout and coding conventions | Original package tree, dependencies and schema |
| R05 | AI data-center power theme and eight supplied anchors | Exact original definition, exclusions and all eight anchor strings |
| R06 | Supply, ownership, coverage and text_sim layers | Original edge definitions and acceptance checks |
| R07 | Substantive/peripheral/irrelevant primary labels; initial passage-threshold adoption policy | Exact threshold values and eligible-evidence rules |
| R08 | Initial 300-chunk label queue, including 100 below retrieval threshold; precision >= 0.85; retrieval loss < 10% | Original sampling allocation and evaluation specification |
| R09 | Complementary log-log first-adoption model and entity-clustered uncertainty | Original model interfaces and dependencies |
| R10 | Configurable 500 adoption-reassignment and 200 graph-rewiring repetitions | Original configuration constants and implementation, if any |
| R11 | Recognition lag and later GLP-1 portability test | Original event interface and theme-package contents |

## Changes explicitly required by the supplied amendments

These are requirements, not proposals needing to be reauthorized. Implementation
still follows the user's approval gates. References point to sections in
[revised_build_spec.md](revised_build_spec.md); its full supplied text controls.

| ID | Sections | Required change |
| --- | --- | --- |
| A01 | 1 | Interpret adoption as first observed substantive-disclosure threshold crossing, not economic adoption; describe network results as predictive associations; accept hyperscale power demand without explicit AI; do not force an industry sequence |
| A02 | 2, 12 | Restrict this execution to foundation/refactor; preserve existing logic and constants; record bugs rather than fixing them; require approval before commits and subsequent steps |
| A03 | 3 | Separate effective/known/ingested/computed times; preserve corrections and exact source versions; provenance for identifiers, classifications, membership and attributes; never substitute call date silently for transcript availability |
| A04 | 3 | Record code/config/input/model/theme/parser/tokenizer/prompt/seed/upstream lineage; label frozen modern tools as retrospective; add sufficient warm-up, uncertain histories and left censoring; origin-time eligibility and exact security/entity membership |
| A05 | 4 | Verify official endpoint documentation and a sanitized real response before parser work; verify coverage, entitlement and timestamp semantics; preserve immutable raw data, retries, resumability and idempotency; follow historical SEC submission files and preserve full filing text/amendments/extraction failures |
| A06 | 5 | Preserve evidence spans, rationale, raw response and versioned error states; add separate impact/activity attributes; token-aware inputs, no silent truncation; deduplicate evidence; weighted uncertainty-aware held-out evaluation and event/date audit |
| A07 | 6 | Separate historical adoption, current activity and observability; use threshold-crossing public availability; exclude analyst-only triggers; retain event quarter in risk set; no re-entry; fading requires two adequately observed calendar quarters |
| A08 | 7 | Preserve supply direction and unresolved counterparties; separate observed revenue share from model weight; top-k only similarity layers; as-of lineage, missingness, staleness and coverage; approve unresolved graph definitions before implementation |
| A09 | 8 | Strictly lag all predictors; compare sector, strong non-network, text, all-layer and ablation models; comparable observations; forecast without unseen quarter fixed effects; full fitted artifacts, diagnostics and valid explicitly specified nulls |
| A10 | 9 | Defined descriptive emergence metrics and cutoff-available partitions; rolling-origin one-quarter forecasts before cascades; correct censoring and full metrics; four-quarter evaluation origins <= 2025-06-30; simultaneous future simulation updates using the complete fitted predictor without realized future covariates |
| A11 | 10 | Attributed recognition events with theme evidence, negative lags and censoring; versioned theme packages and theme-specific calibration; no position-change-only recognition |
| A12 | 11 | Add required regression tests in the relevant implementation phases, including complete-as-of versus physically truncated database feature equivalence |

## Proposed defaults requiring later approval

These are review candidates for the affected later steps. They are **not adopted
defaults**, executable configuration, or permission to start those steps. Numeric
thresholds from the original specification must first be recovered and preserved.

| ID | Topic | Proposal for review | Approval/check needed before implementation |
| --- | --- | --- | --- |
| P01 | Missing transcript availability | Exclude versions with unverified public availability from the primary point-in-time analysis; report them separately | Verify source evidence and quantify coverage impact before considering a sensitivity policy |
| P02 | Warm-up | Derive minimum warm-up from the maximum registered lookback; independently flag incomplete prior-adoption history rather than assuming it is resolved by a fixed duration | Approve actual duration after lookbacks and historical source coverage are known |
| P03 | Observability and exits | Treat insufficiently observed outcomes as unknown; define origin eligibility and exit censoring without consulting future index membership | Approve source-specific sufficiency rules and partial-quarter/exit treatment |
| P04 | Evidence and event timing | Deduplicate by source-location overlap and repeated content before applying the unchanged initial threshold; timestamp the threshold crossing using eligible evidence availability | Approve exact duplicate rules, evidence window and event audit precision/date-error tolerances before network fitting |
| P05 | Similarity graphs | Evaluate deterministic tie breaking and explicit self-edge exclusion; document minimum similarity and union-versus-mutual symmetrization for each layer | Select k, minimum similarity, zero-denominator and symmetrization rules; approve normalization and coverage reporting |
| P06 | Supply exposure | Keep supplier -> customer edges and separately named upstream/downstream exposure features; preserve null observed revenue share | Approve exposure denominator, default modeling weights, expiry and unresolved-counterparty handling; validate direction with a tiny synthetic fixture |
| P07 | Ownership | Compare holder-vector and normalization definitions in a decision memo before selecting a formula | Approve mathematical weights, largest-filer selection, shared-holder sensitivity, amendment rules and historical mapping policy after source verification |
| P08 | Broker activity | Label the layer an activity-overlap proxy unless rosters validate actual coverage | Approve activity windows, alias normalization, historical endpoint and missing-source treatment after entitlement verification |
| P09 | Text similarity | Use token-aware Item 1 chunks and a deterministic documented aggregation of every eligible chunk from the latest as-of filing | Approve model/tokenizer revisions, token limits, overlap/weighting and theme-passage exclusion sensitivity |
| P10 | Forecast specification | Begin with the required intercept and strictly lagged features; use the strong non-network baseline before assessing graph additions | Approve transformations, tuning, origin schedule, uncertainty and shared-time/sector sensitivity design using only training information |
| P11 | Nulls | Specify constrained adoption reassignment and directed rewiring before writing either algorithm | Approve feasible sector-quarter event constraints, degree/weight/sector/temporal rules, failed-draw handling and sensitivity nulls |
| P12 | Emergence | Report new adopters and incidence with explicit observed eligible-risk-set denominators | Approve growth/acceleration/breadth formulas, zero-denominator handling and partition comparability; do not use an identified reproduction-number claim |
| P13 | Determinism | Compare complete-as-of and physically truncated builds using identical frozen configuration and fitted artifacts | Approve numeric tolerance by output type before testing; exact equality where data are discrete |

## Blocked prerequisites and unresolved source questions

| ID | Missing input or unresolved question | Consequence / next evidence required |
| --- | --- | --- |
| B01 — resolved | The repository began empty | User confirmed new-project construction; no legacy source is required for scaffolding and no refactor equivalence is claimed |
| B02 — open | Original build specification is absent | Obtain it if it exists, or explicitly agree the remaining definitions together; exact original-step reconciliation cannot be claimed and missing anchors/thresholds remain unimplemented |
| B03 — superseded | The six named legacy files are absent | No baseline/assertion-preservation comparison applies; new source ingestion and schema still wait for later approved steps |
| B04 — resolved for foundation | No prior package/configuration/environment contract existed | New minimal packaging, config, environment placeholders and CLI were created as engineering choices; no old constants or behavior were moved |
| B05 | FMP endpoint documentation, sanitized real responses, account entitlement and historical/timestamp semantics are unverified | Later ingestion/parser implementation blocked until verified; no credentials were requested or used for this documentation work |
| B06 | SEC source snapshots, historical submissions, provenance and local database are unverified | Later SEC integration and database acceptance checks remain unrun; schema changes must be later append-only migrations |
| B07 | Historical security identifiers, classifications, membership reconciliation and transcript-version availability evidence are not supplied | No point-in-time coverage or leakage claim can be made |
| B08 | Human labels, adopted event-level tolerances, model/tokenizer revisions and weights are not supplied | No measurement validation, model score, calibration, or event-quality claim can be made |
| B09 | Licensed supply data and real internal recognition events are not supplied | Keep the import hook unimplemented; use only clearly marked synthetic recognition fixtures when that later step is authorized |

## Bug backlog

No legacy code-level bug backlog exists because the repository began empty. Do
not interpret the amendments as proof of a bug in unavailable code. Record future
findings with file/line, observed behavior, reproduction and proposed correction;
keep scope changes distinct from routine foundation defects.

## Next proposed step and approval gates

The user approved the foundation for commit and push on 2026-10-04 after reviewing
the report, and indicated that a partner will join the work. The partner's role and
next-phase ownership are not yet specified. No later implementation step has been
authorized by this approval.

The proposed next implementation step is a point-in-time provenance and immutable
run/source contract, using Python/PostgreSQL/pgvector as required. Before editing,
inspect the approved foundation and propose the exact schema, source-version
identity, timestamp/null policies and migration acceptance checks. Define those
choices in this log for approval before implementing affected scientific logic.

Keep that step separate from API parsers, embeddings, classification, graph
construction and models. Official endpoint evidence, human labels, theme anchors
and later scientific choices remain independent prerequisites for their phases.
