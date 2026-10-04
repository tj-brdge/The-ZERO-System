"""Offline CLI contract tests; no empirical data or service fixtures."""

import json
import os
from pathlib import Path
import subprocess
import sys

from theme_contagion_graph.cli import main
from theme_contagion_graph.config import load_config


def test_check_config_reports_unresolved_work(capsys):
    assert main(["check-config"]) == 0
    output = capsys.readouterr()
    result = json.loads(output.out)
    assert result["configuration_valid"] is True
    assert "theme.anchors" in result["pending_decisions"]
    assert "not implemented" in result["scope"]
    assert "config" not in result
    assert output.err == ""


def test_show_config_matches_loaded_file(capsys):
    assert main(["show-config"]) == 0
    result = json.loads(capsys.readouterr().out)
    loaded = load_config()
    assert result["config"] == loaded.values
    assert result["config_sha256"] == loaded.sha256


def test_bad_file_returns_error_without_success_output(tmp_path, capsys):
    path = tmp_path / "synthetic-invalid.yaml"
    path.write_text("[]", encoding="utf-8")
    assert main(["--config", str(path), "check-config"]) == 2
    output = capsys.readouterr()
    assert output.out == ""
    assert "Configuration error" in output.err


def test_module_and_repository_entrypoints_work_outside_checkout(tmp_path):
    root_cli = Path(__file__).resolve().parents[1] / "cli.py"
    # Deliberately do not pass credentials or other research environment variables.
    env = {"PATH": os.defpath, "PYTHONNOUSERSITE": "1"}
    outputs = []
    for command in ([sys.executable, "-m", "theme_contagion_graph"], [sys.executable, str(root_cli)]):
        process = subprocess.run(
            [*command, "check-config"], cwd=tmp_path, env=env,
            capture_output=True, text=True, timeout=10, check=True,
        )
        assert process.stderr == ""
        outputs.append(json.loads(process.stdout))
    assert outputs[0] == outputs[1]
