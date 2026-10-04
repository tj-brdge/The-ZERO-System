# Foundation report

Date: 2026-10-04. Target:
[`tj-brdge/The-ZERO-System`](https://github.com/tj-brdge/The-ZERO-System).

**New-project foundation approved for commit and push on 2026-10-04.** The user
approved the completed report with “it's good. you'll have a partner in this.”
This approval covers publication of the foundation; the next phase remains open
for coordination and separate authorization. The repository began empty. The user clarified,
“We are building them together :-)”. The first step therefore creates a foundation
from scratch rather than refactoring nonexistent code. No later research phase
has been implemented.

## Inspected inputs and starting state

- Read the complete supplied `pasted-text.txt` requirements and first-execution
  instructions. Its exact bytes and SHA-256 are preserved in the revised spec.
- Located and cloned the target repository. Git reported an empty repository;
  inspection found only `.git`, no refs and no commits on `main`.
- Checked applicable ancestor `AGENTS.md` locations; none were present. The empty
  checkout had no repository instructions, dependency files, schema or fixtures.
- The six required legacy files were absent: `001_schema.sql`,
  `002_schema_additions.sql`, `fmp_client.py`, `step2_universe.py`,
  `step3_transcripts.py`, `test_offline.py`. They could not be read or tested.
- Searched the workspace for those files and a project build specification. A
  broader filename search in Documents, Downloads and Desktop found no relevant
  source, but some locations were inaccessible; it was not an exhaustive search.
- The original specification referenced in the attachment was not supplied.
  Original step numbers, exact package layout, eight anchors, and unspecified
  scientific thresholds cannot be verified or reconstructed from the amendments.
- After the new-project clarification, inspected all newly authored package,
  configuration, test and documentation files and their package output.

## Files changed and why

All 15 files below are new in the approved foundation.

| File(s) | Purpose |
| --- | --- |
| `pyproject.toml` | Python >= 3.11, setuptools/src layout, PyYAML dependency, pytest extra, console script and packaged defaults |
| `src/theme_contagion_graph/__init__.py` | Importable package without external-service side effects |
| `src/theme_contagion_graph/config.yaml` | Supplied study dates, layers, label-queue counts, evaluation targets, eight-anchor count and null repetitions; explicit unresolved settings |
| `src/theme_contagion_graph/config.py` | Safe YAML parsing, duplicate-key/shape/date/numeric validation, exact-file SHA-256 and unresolved-setting reporting |
| `src/theme_contagion_graph/cli.py` | Offline `check-config` and `show-config` commands; clear errors and foundation-only scope |
| `src/theme_contagion_graph/__main__.py`, `cli.py` | Module and repository entry points sharing the same CLI |
| `tests/test_config.py`, `tests/test_cli.py` | Synthetic configuration and CLI tests; no fabricated API payloads or empirical labels |
| `.env.example`, `.gitignore` | Empty placeholders for later credentials/database/contact values; keep environment, caches and future data/artifacts local |
| `README.md` | Installation, offline commands, layout, scope and explicit limitations |
| `docs/revised_build_spec.md` | Complete supplied requirements, source hash, amendment-section acceptance crosswalk and new-project clarification |
| `docs/decisions.md` | Separate retained requirements, explicit amendments, routine engineering choices, unapproved scientific proposals and prerequisites |
| `docs/foundation_report.md` | This evidence and review report |

The actual research pipeline does not exist yet. The CLI does not connect to FMP,
SEC, PostgreSQL or any model, and does not create research runs. Configuration
validation is not measurement validation or readiness to fit a network model.

## Baseline versus final results

| Check | Baseline | Final result |
| --- | --- | --- |
| Offline tests | No test suite in empty repository; not run, no pre-existing test failures measured | **33 passed in 1.23s** using `.venv/bin/python -m pytest -q` |
| Assertion/constant/behavior parity | Not applicable to new project | No legacy assertions or code were moved; supplied values checked in new tests |
| Editable package installation | No package | Passed offline with `pip install --no-index --no-build-isolation --no-deps -e .` |
| Dependency consistency | No dependency manifest | `pip check`: **No broken requirements found** |
| Wheel build | No package | Passed with `pip wheel --no-index --no-build-isolation --no-deps --wheel-dir dist .` |
| Wheel contents | Not applicable | Packaged `config.yaml` byte-identical to source; no environment files or tests shipped |
| Installed-wheel behavior | Not applicable | Installed to an isolated temporary target; module and console commands passed outside checkout using the wheel's own configuration |
| Module/repository CLI behavior | Not applicable | Entry-point outputs agree outside checkout with credentials omitted from subprocess environment; included in pytest results |
| Configuration failure behavior | Not applicable | Invalid syntax/dates/ranges, unsafe YAML tags, duplicate/unknown/missing fields, incomplete anchors and unresolved-policy values rejected; included in pytest results |
| Configuration integrity | Not applicable | Exact-byte checksum changes when file content changes; reading leaves file unchanged; included in pytest results |
| Requirements integrity | Not applicable | Complete amendment bytes match the attachment; SHA-256 verified |
| Documentation links/whitespace | Not applicable | Relative link targets exist; all 15 authored files checked for trailing whitespace |
| Local-only artifacts | Not applicable | `git check-ignore` confirms `.env`, virtual environment and future data files are ignored; `.env.example` appears in the reviewable untracked set |

The system Python initially lacked pytest and PyYAML. The first dependency
installation failed because sandbox network resolution was unavailable. After
network approval, dependencies were installed in the repository's `.venv`.
Tests, editable installation, wheel build and wheel smoke checks then ran offline.
That environment setup failure was not an application test failure.

Tested runtime: **Python 3.12.8**. Tested versions: pytest 9.1.1, PyYAML 6.0.3,
setuptools 84.0.0, wheel 0.48.0, pip 24.3.1. Other supported Python versions were
not tested. Dependency bounds are not a frozen research environment; complete
run manifests and model/dependency freezing remain later work.

## Behavior differences and work not run

The only executable behavior is new offline configuration loading/validation and
inspection. There is no earlier implementation against which to claim behavior
preservation. The new minimal package layout is an engineering choice documented
in the decision log, not a recovered original layout.

No schema or migrations, membership reconstruction, transcript parser, state
logic, source ingestion, embeddings, classifier, graph construction, network
model or simulation was added. No `.env` loading or source credential checks were
run. No live API responses, PostgreSQL/pgvector checks, model downloads, human-label
evaluation, temporal-leakage integration tests or empirical backtests were run.
They require later implementation and evidence outside this first-step scope.

No production row counts, external-source coverage metrics or model-performance
results were measured. Empty local contents are not evidence of zero source
coverage. Tests use clearly marked synthetic configurations only.

## Unresolved decisions

- The original specification is unavailable. Its exact steps and unaffected
  requirements cannot be fully reconciled. The revised document explicitly
  preserves this limitation and retains all supplied amendment text.
- Exact theme definition/anchors and initial retrieval/adoption-policy parameters
  must be supplied or agreed together before measurement work. No anchors or
  passage threshold have been invented.
- Adequate warm-up, transcript availability evidence/policy, historical universe
  reconciliation, source/version semantics and censoring need later review.
- Graph definitions, event-level audit tolerances, ownership/coverage source
  evidence, model/tokenizer revisions and human labels are not resolved.
- The foundation has been approved for commit/push. Another implementation step
  still needs authorization under the supplied prompt; partner coordination is pending.

## Proposed next step and acceptance checks

After foundation approval, propose the point-in-time provenance and immutable
source/run contracts in detail before implementing them. Keep that bounded step
separate from source parsers and all measurement/modeling work.

Acceptance checks to agree before implementation:

1. Define effective time, exact-version `known_at`, `ingested_at`, and derived
   `computed_at`, with explicit unknown-time policy; never backdate a correction.
2. Define immutable source-version identities, raw-content hashes and dependency
   lineage, including maximum source availability and as-of input selection.
3. Define a run manifest covering code/source-tree state, full configuration,
   snapshots, parser/chunker/theme/prompt/model/tokenizer revisions, seeds,
   parameters, upstream runs and training cutoffs. Unavailable fields must be
   explicit rather than invented.
4. Propose PostgreSQL/pgvector schema and append-only migration procedure, keeping
   securities distinct from CIK entities and reserving exact temporal intervals.
5. Use labeled synthetic fixtures to test same-version idempotency, corrected
   version preservation, future-version exclusion and non-overwriting run IDs.
   Separate offline contract tests from real database migration/integration tests.
6. Run database acceptance checks only against an available test PostgreSQL/pgvector
   instance; report them as not run if unavailable. Report actual results and stop
   for approval before any following step.

The full complete-as-of versus physically truncated feature-build regression
remains required when feature construction exists; contract-only tests cannot
substitute for it.
