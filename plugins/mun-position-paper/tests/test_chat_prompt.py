#!/usr/bin/env python3
"""Structural checks for the standalone normal-chat prompt."""

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PROMPT = REPO_ROOT / "PROMPT-CHAT-NORMAL.md"


def main() -> int:
    text = PROMPT.read_text(encoding="utf-8")
    required = (
        "## Comportamiento inicial obligatorio",
        "### Fase 2. Investigar antes de redactar",
        "### Fase 3. Confirmar la estrategia",
        "### Fase 4. Verificar el mandato",
        "## Documento descargable",
        "## Control de calidad",
        "## Instrucción de arranque",
    )
    for heading in required:
        assert heading in text, f"missing section: {heading}"
    assert len(text) > 8_000, "standalone prompt is unexpectedly incomplete"
    assert "No prometas superar detectores" in text
    assert "comienza ahora la entrevista" in text
    print("standalone chat prompt test: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
