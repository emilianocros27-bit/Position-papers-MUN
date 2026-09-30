#!/usr/bin/env python3
"""Smoke tests for the position-paper document builder."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import zipfile
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = PLUGIN_ROOT / "skills" / "mun-position-paper"
SCRIPT = SKILL_ROOT / "scripts" / "build_position_paper.py"
EXAMPLE = SKILL_ROOT / "assets" / "example-input.json"


def load_builder():
    spec = importlib.util.spec_from_file_location("mun_position_paper_builder", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load the builder module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    builder = load_builder()
    with EXAMPLE.open("r", encoding="utf-8") as handle:
        payload = builder.validate_payload(json.load(handle))

    with tempfile.TemporaryDirectory(prefix="mun-position-paper-test-") as temp_dir:
        output = Path(temp_dir) / "example.docx"
        builder.build_document(payload, output)
        assert output.is_file() and output.stat().st_size > 10_000
        with zipfile.ZipFile(output) as archive:
            names = set(archive.namelist())
            assert "word/document.xml" in names
            xml = archive.read("word/document.xml").decode("utf-8")
            assert "Comité de demostración" in xml
            assert "Soluciones" in xml

    invalid = dict(payload)
    invalid["topic"] = ""
    try:
        builder.validate_payload(invalid)
    except builder.InputError:
        pass
    else:
        raise AssertionError("Empty required fields must fail validation")

    print("builder smoke test: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
