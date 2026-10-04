# Theme Contagion Graph

Research foundation in **The-ZERO-System** for asking which company-relationship
layers improve prediction of subsequent substantive theme disclosure beyond a
company's prior language and industry adoption pattern. Results will describe
predictive associations. Disclosure adoption does not establish the start of
economic exposure or causal transmission.

This repository started empty. The first step provides packaging, configuration,
an offline CLI and foundation tests. Ingestion, database schema, embeddings,
classification, graph construction, modeling and simulations are **not implemented**.
The study is planned as retrospective measurement with frozen tools.

## Local setup

Python 3.11 or newer:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[test]'
theme-contagion check-config
theme-contagion show-config
python -m pytest
```

Dependency installation may need network access. Tests and CLI commands run
offline and do not need API keys, PostgreSQL, human labels or model downloads.

Equivalent entry points are `python cli.py` and
`python -m theme_contagion_graph`, followed by the same command. All entry points
require the package to be installed. For a separate configuration file:

```bash
theme-contagion --config /path/to/config.yaml check-config
```

The canonical defaults are in
[`src/theme_contagion_graph/config.yaml`](src/theme_contagion_graph/config.yaml)
and ship inside the installed package, so commands work outside the checkout.
The CLI prints the SHA-256 of the exact configuration bytes. This is a file
integrity aid, not a complete scientific run manifest. No research runs are
created by these commands.

`check-config` validates configuration structure, not research readiness. Null
settings and the empty anchor list mark pending inputs. The exact original theme
definition, eight anchors, retrieval/adoption policy and adequate warm-up remain
unresolved. The CLI names these gaps; it does not generate substitute values.

[`.env.example`](.env.example) contains empty placeholders for later source and
database work. This step does not load `.env` files or use those variables.

## Layout and scope

```text
cli.py                         repository CLI entry point
src/theme_contagion_graph/     package, packaged config.yaml, offline CLI
tests/                        synthetic configuration and CLI tests
docs/revised_build_spec.md     requirements and changed acceptance criteria
docs/decisions.md              retained requirements, amendments, open choices
docs/foundation_report.md      actual work, tests, limitations, next step
```

This is a new minimal layout chosen for the foundation; no legacy code, tests or
constants were moved. All populated research values come from the supplied
amendments. The original specification referenced in that prompt was not supplied;
its step numbers, exact anchors and other unspecified details remain open.

See the [revised specification](docs/revised_build_spec.md),
[decision log](docs/decisions.md), and [foundation report](docs/foundation_report.md).
The foundation was approved for commit and push on 2026-10-04. Subsequent phases
require separate authorization; partner coordination is pending.
