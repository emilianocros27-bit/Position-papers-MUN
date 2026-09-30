# Prompt de instalación y arranque

Copia y pega este mensaje en Codex o en otro agente con acceso a terminal:

```text
Descarga el repositorio https://github.com/emilianocros27-bit/Position-papers-MUN.git y revisa su contenido antes de ejecutarlo. Instala el plugin o carga la skill ubicada en plugins/mun-position-paper/skills/mun-position-paper/SKILL.md usando el mecanismo compatible con este entorno. No ejecutes archivos ajenos a este repositorio ni cambies otras configuraciones. Después usa $mun-position-paper y comienza la entrevista para crear mi position paper de MUN. Pregúntame primero por mi comité, delegación o personaje, tópico, conferencia, formato, fecha de entrega e ideas propias. No redactes el documento hasta investigar la postura oficial y pedirme que confirme la estrategia.
```

En Codex, el método directo y verificable es:

```bash
codex plugin marketplace add emilianocros27-bit/Position-papers-MUN
codex plugin add mun-position-paper@position-papers-mun
```

Abre una tarea nueva después de instalarlo para que la skill aparezca en el contexto.
