# Theme Contagion Graph

Python package: `theme-contagion-graph` in the `The-ZERO-System` repository.
The relationship between the two project names is awaiting the owner's decision.

## Setup

Python 3.11 or newer:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[test]'
```

## Commands

```bash
python -m pytest
theme-contagion check-config
theme-contagion show-config
theme-contagion --config /path/to/config.yaml check-config
```

After installation, `python cli.py` and `python -m theme_contagion_graph` accept
the same commands. Defaults ship in
[`config.yaml`](src/theme_contagion_graph/config.yaml); the CLI reports the exact
file's SHA-256. `.env.example` contains placeholders; the CLI does not load `.env`.

Installation may download dependencies. Tests and configuration checks need no
network, API keys, database or models. CI runs both checks on Python 3.11 and 3.12
with networking disabled after installation.

## Current status

Package, configuration validation, CLI and offline tests are implemented.
The research pipeline is not. Theme definition, anchors, retrieval/adoption
parameters and warm-up remain unresolved; `check-config` validates structure,
not research readiness. Work proceeds one phase and draft PR at a time.

Read the [requirements](docs/revised_build_spec.md),
[open decisions](docs/decisions.md), [contributor guide](CLAUDE.md),
[Codex instructions](AGENTS.md), and [changelog](CHANGELOG.md).
