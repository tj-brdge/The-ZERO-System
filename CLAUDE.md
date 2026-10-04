# Working on The-ZERO-System

For humans and AI agents. Theme Contagion Graph studies whether company
relationships improve prediction of substantive investment-theme disclosure.
The Python package is `theme_contagion_graph`; PostgreSQL/pgvector is planned.
Only package/configuration/CLI scaffolding exists; the pipeline is not built.

## Ground rules

- Read README.md, docs/*.md, relevant code and tests before editing.
- Research requirements live in docs/revised_build_spec.md; do not duplicate them.
- Never invent source data, API responses, anchors, labels, metrics or test results.
- Mark test-only values synthetic. Mark authored proposals as drafts, not sources.
- Report unavailable checks as "not run" or "blocked", with the missing prerequisite.
- Describe results as predictive associations; never claim causal effects.
- Keep docs short. Code and tests are the record; no spec-change mapping tables.
- Keep credentials and raw samples out of Git. Offline checks require no secrets.
- Log unresolved choices and proposals in docs/decisions.md before affected work.
- Inspect current main and partner changes; do not overwrite another contributor's work.

## Setup and checks

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[test]'
python -m pytest
theme-contagion check-config
```

Installation may download dependencies; tests and config checks run offline.
CI checks Python 3.11 and 3.12 with networking disabled after installation.

## What counts as a step

A step is one reviewable phase with a stated scope, missing inputs and acceptance
checks. Branch from main, complete the phase, run its checks, open one draft PR,
and summarize actual results and unresolved items. Stop for review before the
next phase; do not merge the PR yourself. Opening the requested draft PR includes
permission to commit and push that phase branch.

Current phases: (1) repo hygiene, (2) theme definition, (3) feasibility probes,
(4) minimum-version roadmap. These phases do not build the research pipeline.
Schema and record-keeping design follow feasibility results. Draft scientific
values stay out of config.yaml until approved; later work needs its own scope.
