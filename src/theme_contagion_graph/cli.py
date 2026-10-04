"""Offline foundation commands; no ingestion or scientific pipeline is wired yet."""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence

from .config import ConfigError, load_config, pending_decisions


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Theme Contagion Graph foundation (offline configuration only)."
    )
    parser.add_argument("--config", metavar="PATH", help="YAML file; defaults to packaged config.yaml")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("show-config", help="Print configuration and its exact-file SHA-256 as JSON")
    commands.add_parser("check-config", help="Validate configuration shape and list unresolved settings")
    args = parser.parse_args(argv)
    try:
        config = load_config(args.config)
    except ConfigError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 2

    result = {
        "config_source": config.source,
        "config_sha256": config.sha256,
        "pending_decisions": pending_decisions(config.values),
        "scope": "foundation_only; research pipeline is not implemented",
    }
    if args.command == "show-config":
        result["config"] = config.values
    else:
        result["configuration_valid"] = True
    print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))
    return 0
