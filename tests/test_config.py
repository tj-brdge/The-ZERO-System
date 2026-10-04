"""Synthetic configuration cases only; these are not source/API or human labels."""

import hashlib

import pytest
import yaml

from theme_contagion_graph.config import ConfigError, load_config, pending_decisions


def write_config(tmp_path, values):
    path = tmp_path / "synthetic-config.yaml"
    path.write_text(yaml.safe_dump(values), encoding="utf-8")
    return path


def test_supplied_defaults_and_explicit_gaps():
    values = load_config().values
    assert values["study"] == {
        "start": "2021-01-01", "end": "2026-06-30", "warmup_start": None
    }
    assert values["layers"] == ["supply", "ownership", "coverage", "text_sim"]
    assert values["theme"]["required_anchor_count"] == 8
    assert values["measurement"] == {
        "human_label_queue_size": 300,
        "below_retrieval_threshold_count": 100,
        "substantive_precision_min": 0.85,
        "retrieval_loss_max_exclusive": 0.1,
        "retrieval_threshold": None,
        "adoption_policy": None,
    }
    assert values["null_models"] == {
        "adoption_reassignment_repetitions": 500,
        "graph_rewiring_repetitions": 200,
    }
    assert pending_decisions(values) == [
        "study.warmup_start", "theme.definition", "theme.anchors",
        "measurement.retrieval_threshold", "measurement.adoption_policy",
    ]


def test_explicit_path_hashes_exact_bytes_and_does_not_modify_file(tmp_path):
    values = load_config().values
    values["project_name"] = "Synthetic configuration test"
    path = write_config(tmp_path, values)
    raw = path.read_bytes()
    result = load_config(path)
    assert result.values == values
    assert result.sha256 == hashlib.sha256(raw).hexdigest()
    assert path.read_bytes() == raw
    path.write_bytes(raw + b"\n# Synthetic comment\n")
    changed = load_config(path)
    assert changed.values == result.values
    assert changed.sha256 != result.sha256


@pytest.mark.parametrize(("section", "key", "value", "error"), [
    ("study", "start", "2026-07-01", "on or before"),
    ("study", "start", "2021-02-30", "valid calendar date"),
    ("study", "end", "20260630", "YYYY-MM-DD"),
    ("study", "warmup_start", "2021-01-01", "precede"),
    ("theme", "anchors", ["SYNTHETIC: one anchor"], "required_anchor_count"),
    ("theme", "anchors", ["SYNTHETIC: duplicate"] * 8, "duplicates"),
    ("theme", "required_anchor_count", True, "integer"),
    ("measurement", "human_label_queue_size", 0, "integer"),
    ("measurement", "below_retrieval_threshold_count", 301, "exceeds"),
    ("measurement", "substantive_precision_min", float("nan"), "finite"),
    ("measurement", "retrieval_loss_max_exclusive", float("inf"), "finite"),
    ("measurement", "substantive_precision_min", 1.1, "finite"),
    ("measurement", "adoption_policy", {"synthetic": 2}, "remain null"),
    ("measurement", "retrieval_threshold", 0.5, "remain null"),
    ("null_models", "graph_rewiring_repetitions", -1, "integer"),
])
def test_invalid_configuration_is_rejected(tmp_path, section, key, value, error):
    values = load_config().values
    values[section][key] = value
    with pytest.raises(ConfigError, match=error):
        load_config(write_config(tmp_path, values))


@pytest.mark.parametrize("raw", [
    "", "- synthetic-list\n", "{bad yaml", "schema_version: 1\nschema_version: 2\n",
    "!!python/object/apply:os.system ['echo should-not-run']",
    "1: synthetic-non-string-key\n",
])
def test_invalid_yaml_or_shape_is_rejected(tmp_path, raw):
    path = tmp_path / "synthetic-config.yaml"
    path.write_text(raw, encoding="utf-8")
    with pytest.raises(ConfigError):
        load_config(path)


@pytest.mark.parametrize("mutation", ["unknown", "missing", "duplicate_layer", "bool_version"])
def test_configuration_mistakes_are_not_silently_ignored(tmp_path, mutation):
    values = load_config().values
    if mutation == "unknown":
        values["unexpected"] = "synthetic"
    elif mutation == "missing":
        del values["study"]["warmup_start"]
    elif mutation == "duplicate_layer":
        values["layers"].append(values["layers"][0])
    else:
        values["schema_version"] = True
    with pytest.raises(ConfigError):
        load_config(write_config(tmp_path, values))


def test_missing_file_is_explicit_error(tmp_path):
    with pytest.raises(ConfigError, match="Cannot read configuration"):
        load_config(tmp_path / "missing.yaml")


def test_parse_error_does_not_echo_file_contents(tmp_path):
    path = tmp_path / "synthetic-config.yaml"
    path.write_text("token: [SYNTHETIC-PRIVATE-TOKEN", encoding="utf-8")
    with pytest.raises(ConfigError) as error:
        load_config(path)
    assert "SYNTHETIC-PRIVATE-TOKEN" not in str(error.value)
