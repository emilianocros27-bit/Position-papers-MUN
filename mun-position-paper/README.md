# mun-position-paper

Skill de Claude para investigar y redactar position papers de Modelo de Naciones Unidas (MUN) de nivel competitivo: un país, un comité y un tema a la vez.

Investiga la postura real del país (voto en la ONU, tratados, declaraciones oficiales, legislación nacional) antes de escribir, sigue la estructura y los criterios de evaluación reales de conferencias como NMUN, THIMUN y modelos universitarios, y evita los vicios de escritura genérica (relleno, neutralidad de conveniencia, listas sin análisis) en vez de solo "camuflar" el texto.

## Qué hace

- Pide país, comité y tema, y el formato de la conferencia si se conoce.
- Investiga en internet la postura oficial, el historial de voto, los tratados ratificados y la acción previa de la ONU sobre el tema — nunca inventa datos.
- Redacta el paper en la estructura correcta (formato clásico de 1 tema, o el formato de 2 temas en 2 páginas de NMUN).
- Se autorrevisa contra un checklist basado en rúbricas reales de evaluación antes de entregar.
- Recuerda revisar la política de uso de IA de la conferencia (varias, como NMUN, exigen declararlo).

## Instalar en Claude Code

```bash
git clone https://github.com/<tu-usuario>/mun-position-paper.git ~/.claude/skills/mun-position-paper
```

Claude Code detecta automáticamente cualquier carpeta con un `SKILL.md` dentro de `~/.claude/skills/` (skills personales) o `.claude/skills/` dentro de un proyecto (skills de ese proyecto). Reinicia la sesión de Claude Code si ya estaba abierta.

## Instalar en Cowork / Claude.ai

1. Comprime la carpeta `mun-position-paper` en un `.zip` (o descarga el `.zip` que te compartieron).
2. En Cowork, sube el archivo o la carpeta como skill nueva desde la sección de skills, o pide a Claude "instala esta skill" adjuntando el archivo.

## Usar la skill

Una vez instalada, simplemente escribe algo como:

> "Necesito el position paper de México para DISEC sobre el uso de inteligencia artificial en sistemas de armas nucleares, para la conferencia [nombre]."

Claude va a investigar antes de escribir y te va a preguntar el formato de la conferencia si no lo mencionaste.

## Subir este repo a tu propio GitHub

Si recibiste esto como una carpeta (no como link de GitHub), para subirlo tú mismo:

```bash
cd mun-position-paper
git init                                   # si no tiene ya un repo git
git add -A
git commit -m "Initial commit: MUN position paper skill"
git branch -M main
git remote add origin https://github.com/<tu-usuario>/mun-position-paper.git
git push -u origin main
```

(Crea antes el repositorio vacío en GitHub desde github.com/new, sin README ni licencia, para que el `push` no choque con nada.)

## Estructura

```
mun-position-paper/
├── SKILL.md                       # instrucciones principales
└── references/
    ├── template.md                # estructuras de position paper
    ├── style-guide.md             # cómo escribir prosa diplomática natural
    ├── rubric-checklist.md        # checklist de autorrevisión
    └── research-sources.md        # dónde investigar cada tipo de dato
```
