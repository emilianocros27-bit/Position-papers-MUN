# MUN Position Paper

Plugin y skill para investigar, redactar y producir position papers de Modelo de Naciones Unidas. El flujo comienza con una entrevista breve, comprueba la postura real de la delegación, adapta las propuestas al mandato del comité y termina con un documento Word revisado visualmente.

## ChatGPT o Claude sin Codex

Para un chat normal, usa el archivo autosuficiente [`PROMPT-CHAT-NORMAL.md`](PROMPT-CHAT-NORMAL.md). Descárgalo y adjúntalo al chat, o copia todo su contenido. Las instrucciones completas están en [`USAR-EN-CHATGPT-O-CLAUDE.md`](USAR-EN-CHATGPT-O-CLAUDE.md).

Enlace directo que un chat con navegación web puede intentar abrir:

```text
https://raw.githubusercontent.com/emilianocros27-bit/Position-papers-MUN/main/PROMPT-CHAT-NORMAL.md
```

Adjuntar el archivo es más fiable que pegar únicamente la URL del repositorio, porque un chat normal no necesariamente recorre todos sus archivos.

## Qué incluye

- Entrevista interactiva para obtener comité, delegación o personaje, tópico, conferencia, formato y postura del delegado.
- Investigación web con prioridad para fuentes oficiales, votos, tratados, legislación y declaraciones nacionales.
- Control de fecha para comités históricos y control de competencia para no proponer medidas fuera del mandato.
- Redacción diplomática basada en evidencia, sin inventar resoluciones, fechas, cifras o citas.
- Plantilla inspirada en un position paper ganador: identificación clara, contexto, postura nacional, soluciones y bibliografía.
- Generador reproducible de `.docx`, conversión opcional a PDF y validación del contenido de entrada.
- Rúbrica final para evaluar postura, investigación, viabilidad, voz, corrección y presentación.

La skill no intenta engañar detectores de IA. Ayuda a producir un trabajo original a partir de las ideas del delegado, exige revisión humana y recuerda comprobar la política de IA de la conferencia.

## Instalación en Codex

```bash
codex plugin marketplace add emilianocros27-bit/Position-papers-MUN
codex plugin add mun-position-paper@position-papers-mun
```

Después abre una tarea nueva y escribe:

> Usa $mun-position-paper y empieza la entrevista para crear mi position paper.

También puedes copiar el texto completo de [`PROMPT-DE-INSTALACION.md`](PROMPT-DE-INSTALACION.md) en un agente con acceso a terminal.

## Uso rápido

La skill pregunta primero por los datos indispensables. No redacta hasta conocer, como mínimo:

- delegación, país, organización o personaje;
- comité;
- tópico exacto;
- conferencia o reglas de formato disponibles;
- idioma y fecha de entrega.

Después investiga, muestra una síntesis de la postura encontrada y pide al delegado que confirme o matice sus prioridades antes de preparar el documento final.

## Estructura

```text
.agents/plugins/marketplace.json
plugins/mun-position-paper/
├── plugin.json
├── .codex-plugin/plugin.json
├── skills/mun-position-paper/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   ├── scripts/
│   └── assets/
└── tests/
```

`assets/example-position-paper.docx` es una muestra visual neutral marcada como demostración; no contiene datos del position paper usado como referencia.

## Generador de documentos

El script recibe un archivo JSON validado y genera el Word:

```bash
python plugins/mun-position-paper/skills/mun-position-paper/scripts/build_position_paper.py \
  plugins/mun-position-paper/skills/mun-position-paper/assets/example-input.json \
  --output position-paper.docx
```

Para intentar producir también PDF, añade `--pdf`. La conversión requiere LibreOffice o `soffice` disponible en el entorno.

## Compatibilidad

El repositorio usa el formato portátil de Agent Plugins y conserva el manifiesto de compatibilidad de Codex. Otros agentes capaces de leer skills pueden apuntar directamente a:

```text
plugins/mun-position-paper/skills/mun-position-paper/SKILL.md
```

La instalación exacta fuera de Codex depende de las funciones de cada producto.

## Desarrollo y pruebas

```bash
python plugins/mun-position-paper/tests/test_builder.py
python plugins/mun-position-paper/tests/test_chat_prompt.py
```

La prueba valida el JSON de ejemplo, genera un DOCX temporal y comprueba su estructura básica.
