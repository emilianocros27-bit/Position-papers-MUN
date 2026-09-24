---
name: mun-position-paper
description: Investiga y redacta position papers de Modelo de Naciones Unidas (MUN) de nivel competitivo, un país + comité + tema a la vez. Úsala siempre que el usuario pida ayuda con un "position paper", "MUN", "Modelo de Naciones Unidas", un comité tipo ECOSOC, DISEC, Security Council, Human Rights Council, la postura de un país en Naciones Unidas sobre un tema, o quiera preparar a un delegado para una conferencia MUN, incluso si solo da el país y el tema sin decir "position paper" explícitamente.
---

# MUN Position Paper Writer

Esta skill convierte una investigación real (no inventada) sobre un país, un comité y un tema en un position paper con la estructura, el tono y el nivel de detalle que esperan los jueces de un Modelo de Naciones Unidas.

## Antes de escribir una sola línea

Un position paper vale por lo que dice sobre el país real, no por sonar elocuente. Los tres errores que más bajan la calificación (según las rúbricas de NMUN, THIMUN, Best Delegate y conferencias universitarias) son: (1) inventar o adivinar la postura del país en vez de investigarla, (2) listar resoluciones sin analizarlas, y (3) proponer soluciones genéricas que cualquier país podría firmar. Esta skill existe para evitar exactamente esos tres errores, no solo para producir texto con buen formato.

**Aviso importante sobre uso de IA:** varias conferencias (NMUN es el caso explícito que se documentó al construir esta skill) exigen ahora una declaración de uso de IA en una página aparte, y consideran que un position paper redactado por IA sin declararlo es una falta de originalidad que puede excluir el paper de revisión. Antes de entregar cualquier paper generado con esta skill, dile al usuario que revise el reglamento específico de su conferencia y, si se requiere, incluya la declaración correspondiente. No es tarea de esta skill ayudar a ocultar que se usó IA; es tarea de esta skill que el paper sea genuinamente bueno.

## Flujo de trabajo

### 1. Reunir los datos mínimos

Antes de investigar, confirma con el usuario (una sola vez, no interrogatorio):
- País/delegación asignada
- Comité (ej. ECOSOC, DISEC/GA1, Security Council, Human Rights Council, comité especializado)
- Tema o temas exactos (el nombre tal cual aparece en la guía de estudio o "background guide" del comité, si existe)
- Conferencia y, si la tiene, su guía de formato específica (algunas piden 1 tema, otras 2; algunas piden citas, otras las prohíben — ver `references/template.md`)
- Si no hay guía de formato conocida, usa el formato clásico de 1 tema (sección "Formato B" en `references/template.md`), que es el más extendido.

Si el usuario no tiene la guía de formato de su conferencia a la mano, dile que lo confirme antes de imprimir/entregar el paper final — el formato incorrecto resta puntos aunque el contenido sea excelente.

### 2. Investigar de verdad (no improvisar)

Usa búsqueda web para cada tema antes de escribir. No redactes ninguna postura de política exterior sin haberla buscado. Como mínimo, busca:

- Postura oficial del país: declaraciones del Ministerio/Secretaría de Relaciones Exteriores, discursos en la Asamblea General o el comité correspondiente, comunicados de la misión permanente ante la ONU.
- Historial de voto: cómo votó el país en resoluciones relevantes de la Asamblea General o el Consejo de Seguridad sobre el tema.
- Tratados y marcos ratificados o rechazados por el país relacionados con el tema (¿firmó? ¿ratificó? ¿tiene reservas?).
- Acción nacional: leyes, programas o políticas internas del país relacionadas con el tema.
- Acción previa de la ONU sobre el tema: resoluciones clave, programas, órganos subsidiarios, y qué tan efectivos fueron o por qué fallaron.

`references/research-sources.md` tiene una lista de fuentes confiables por tipo de dato (voto, tratados, declaraciones, contexto regional).

**Regla dura: nunca inventes un número de resolución, una cita textual, una fecha o una cifra.** Si no encuentras el dato exacto, describe la postura en términos generales y verificables ("México ha respaldado consistentemente las resoluciones de desarme nuclear en la Asamblea General") en vez de fabricar un dato específico que suene autoritativo pero sea falso. Un dato inventado que un juez o un delegado rival detecta es más dañino que una frase genérica.

### 3. Redactar

Sigue la plantilla de `references/template.md` para la estructura y `references/style-guide.md` para el tono y la prosa. Los dos puntos que más importan:

- **Argumenta, no enumeres.** Cada resolución o dato mencionado debe ir acompañado de por qué importa para la postura del país, no solo el hecho de que existe.
- **Postura propia, no neutralidad de conveniencia.** Un país que "reconoce ambos lados del problema" sin comprometerse a nada es la queja número uno de los jueces. Si la investigación real del país no da una postura clara, dilo — no lo disimules con lenguaje ambiguo.

### 4. Autorrevisión antes de entregar

Antes de dar el paper por terminado, revísalo contra `references/rubric-checklist.md` en voz alta (como una lista, no solo mentalmente) y corrige lo que falle. Confirma también: formato correcto para la conferencia indicada, extensión correcta, y que ningún dato quede sin verificar.

### 5. Entrega

Entrega siempre dos cosas juntas, nunca solo el texto del paper: (1) el paper, en el formato que haya indicado (Word, PDF, texto plano), y (2) una lista de fuentes con cada dato verificado durante la investigación (ver "Formato de la lista de fuentes" en `references/template.md`). Esto aplica aunque el texto del paper en sí no lleve citas formales — el propio delegado necesita esa lista para defender sus datos si un juez o un rival lo cuestiona en comité, y varias rúbricas (Georgia Tech MUN, por ejemplo) califican "Referencias" como categoría aparte. Recuérdale también, en una línea, revisar la política de IA de su conferencia antes de enviarlo (ver aviso arriba).

## Archivos de referencia

- `references/template.md` — estructuras de position paper (formato de 1 tema y de 2 temas), con encabezados exactos.
- `references/style-guide.md` — cómo escribir prosa diplomática natural y evitar los tics de escritura que delatan un texto genérico o mal editado.
- `references/rubric-checklist.md` — checklist de autorrevisión basado en criterios reales de evaluación de MUN.
- `references/research-sources.md` — dónde buscar postura, votos, tratados y acción previa de la ONU.

Cada uno de esos archivos se lee cuando corresponde en el flujo de arriba — no hace falta cargarlos todos de una vez.
