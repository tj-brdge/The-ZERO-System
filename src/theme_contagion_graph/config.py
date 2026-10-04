"""Load and validate configuration without accessing external research inputs.

Validation checks the foundation configuration's shape, not research readiness.
Scientific definitions and later-phase source contracts are deliberately absent.
"""

from __future__ import annotations

import hashlib
import math
import re
from dataclasses import dataclass
from datetime import date
from importlib.resources import files
from pathlib import Path
from typing import Any

import yaml


class ConfigError(ValueError):
    """A configuration could not be read or violates the foundation contract."""


class _UniqueKeyLoader(yaml.SafeLoader):
    """Keep duplicate YAML keys from silently overriding a configuration value."""

    def construct_mapping(self, node: yaml.MappingNode, deep: bool = False) -> dict:
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str):
                raise ConfigError("Configuration mapping keys must be strings")
            if key in result:
                raise ConfigError("Duplicate configuration key")
            result[key] = self.construct_object(value_node, deep=deep)
        return result


@dataclass(frozen=True)
class LoadedConfig:
    values: dict[str, Any]
    source: str
    sha256: str


def _mapping(value: Any, name: str) -> dict[str, Any]:
    if not isinstance(value, dict) or not all(isinstance(key, str) for key in value):
        raise ConfigError(f"{name} must be a mapping with string keys")
    return value


def _fields(mapping: dict[str, Any], expected: set[str], name: str) -> None:
    if set(mapping) != expected:
        raise ConfigError(f"{name} has missing or unsupported fields; use the packaged config.yaml as the template")


def _integer(value: Any, name: str, minimum: int = 1) -> int:
    if type(value) is not int or value < minimum:
        raise ConfigError(f"{name} must be an integer >= {minimum}")
    return value


def _text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ConfigError(f"{name} must be a nonempty string")
    return value


def _date(value: Any, name: str) -> date:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ConfigError(f'{name} must be a quoted date in YYYY-MM-DD format')
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ConfigError(f"{name} must be a valid calendar date") from exc


def _probability(value: Any, name: str) -> None:
    if type(value) not in (int, float) or not math.isfinite(value) or not 0 < value <= 1:
        raise ConfigError(f"{name} must be finite and in (0, 1]")


def _validate(config: dict[str, Any]) -> None:
    _fields(config, {"schema_version", "project_name", "study", "layers", "theme", "measurement", "null_models"}, "configuration")
    if type(config.get("schema_version")) is not int or config["schema_version"] != 1:
        raise ConfigError("schema_version must be 1")
    _text(config.get("project_name"), "project_name")
    study = _mapping(config.get("study"), "study")
    _fields(study, {"start", "end", "warmup_start"}, "study")
    start = _date(study.get("start"), "study.start")
    end = _date(study.get("end"), "study.end")
    if start > end:
        raise ConfigError("study.start must be on or before study.end")
    if study.get("warmup_start") is not None:
        if _date(study["warmup_start"], "study.warmup_start") >= start:
            raise ConfigError("study.warmup_start must precede study.start")

    layers = config.get("layers")
    if not isinstance(layers, list) or not layers:
        raise ConfigError("layers must be a nonempty list")
    for layer in layers:
        _text(layer, "layers entry")
    if len(set(layers)) != len(layers):
        raise ConfigError("layers must not contain duplicates")

    theme = _mapping(config.get("theme"), "theme")
    _fields(theme, {"name", "definition", "anchors", "required_anchor_count"}, "theme")
    _text(theme.get("name"), "theme.name")
    if theme.get("definition") is not None:
        _text(theme["definition"], "theme.definition")
    required = _integer(theme.get("required_anchor_count"), "theme.required_anchor_count")
    anchors = theme.get("anchors")
    if not isinstance(anchors, list):
        raise ConfigError("theme.anchors must be a list")
    for anchor in anchors:
        _text(anchor, "theme.anchors entry")
    if anchors and len(anchors) != required:
        raise ConfigError("theme.anchors must be empty (unresolved) or match required_anchor_count")
    if len(set(anchors)) != len(anchors):
        raise ConfigError("theme.anchors must not contain duplicates")

    measurement = _mapping(config.get("measurement"), "measurement")
    _fields(measurement, {"human_label_queue_size", "below_retrieval_threshold_count", "substantive_precision_min", "retrieval_loss_max_exclusive", "retrieval_threshold", "adoption_policy"}, "measurement")
    queue_size = _integer(measurement.get("human_label_queue_size"), "measurement.human_label_queue_size")
    below = _integer(measurement.get("below_retrieval_threshold_count"), "measurement.below_retrieval_threshold_count", 0)
    if below > queue_size:
        raise ConfigError("measurement.below_retrieval_threshold_count exceeds human_label_queue_size")
    for key in ("substantive_precision_min", "retrieval_loss_max_exclusive"):
        _probability(measurement.get(key), f"measurement.{key}")
    # No scientific semantics for these settings have been approved yet.
    for key in ("retrieval_threshold", "adoption_policy"):
        if measurement.get(key) is not None:
            raise ConfigError(f"measurement.{key} must remain null until its implementation step is approved")

    nulls = _mapping(config.get("null_models"), "null_models")
    _fields(nulls, {"adoption_reassignment_repetitions", "graph_rewiring_repetitions"}, "null_models")
    for key in ("adoption_reassignment_repetitions", "graph_rewiring_repetitions"):
        _integer(nulls.get(key), f"null_models.{key}")


def pending_decisions(config: dict[str, Any]) -> list[str]:
    """List unresolved settings, without implying that other readiness gates passed."""
    pending = []
    if config["study"].get("warmup_start") is None:
        pending.append("study.warmup_start")
    if config["theme"].get("definition") is None:
        pending.append("theme.definition")
    if not config["theme"]["anchors"]:
        pending.append("theme.anchors")
    for key in ("retrieval_threshold", "adoption_policy"):
        if config["measurement"].get(key) is None:
            pending.append(f"measurement.{key}")
    return pending


def load_config(path: str | Path | None = None) -> LoadedConfig:
    """Read an explicit YAML file or the packaged defaults, hashing exact bytes."""
    source = Path(path) if path is not None else files("theme_contagion_graph").joinpath("config.yaml")
    try:
        raw = source.read_bytes()
        parsed = yaml.load(raw.decode("utf-8"), Loader=_UniqueKeyLoader)
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        # Do not echo file contents: accidental credentials should stay out of errors.
        raise ConfigError(f"Cannot read configuration from {source}: {type(exc).__name__}") from exc
    config = _mapping(parsed, "configuration")
    _validate(config)
    return LoadedConfig(config, str(source), hashlib.sha256(raw).hexdigest())
