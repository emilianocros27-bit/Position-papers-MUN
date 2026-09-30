---
name: mun-position-paper
description: Entrevista, investiga, redacta, revisa y genera position papers de Modelo de Naciones Unidas para una delegación, personaje o actor específico. Úsala cuando el usuario pida un position paper, postura nacional para MUN, preparación escrita de comité, revisión de un borrador MUN o un documento Word/PDF listo para conferencia. No la uses para discursos o resoluciones aislados salvo que formen parte del mismo proyecto de position paper.
---

# MUN Position Paper

Convierte las ideas del delegado y evidencia verificable en un position paper competitivo. El usuario conserva la autoría intelectual: pide su estrategia, refleja sus prioridades y exige su revisión antes de considerar final el documento.

## Principios no negociables

- Prioriza las reglas de la conferencia y su background guide sobre cualquier plantilla genérica.
- Separa hechos comprobados, inferencias y preferencias del delegado. No presentes una inferencia como política oficial.
- Nunca inventes votos, resoluciones, tratados, citas, fechas, cifras, programas o competencias institucionales.
- Investiga antes de redactar. Para un comité histórico, no uses información posterior a la fecha de corte.
- Propón únicamente medidas que el comité pueda adoptar o impulsar razonablemente.
- No prometas superar detectores de IA ni modifiques el texto para engañarlos. Busca originalidad mediante investigación, decisiones del delegado y edición humana.
- Indica al usuario que revise las reglas de su conferencia sobre asistencia de IA y que haga cualquier declaración exigida.

## Flujo

### 1. Entrevista al delegado

En la primera respuesta, saluda brevemente y pregunta solo por los datos que falten. Agrupa un máximo de cinco preguntas fáciles de contestar:

1. Comité y conferencia.
2. Delegación, país, organización, bloque o personaje que interpreta.
3. Tópico exacto y, si aplica, fecha de corte del comité histórico.
4. Guía de formato, extensión, idioma y fecha de entrega.
5. Ideas propias: prioridades, líneas rojas, soluciones favoritas y tono deseado.

Después pregunta por nombre del delegado, escuela y bandera solo si el formato los requiere. Pide la guía o el borrador cuando exista. Lee `references/intake.md` para resolver casos incompletos, personajes de crisis y múltiples tópicos.

No redactes el paper completo en este punto. Resume lo entendido y señala qué investigarás.

### 2. Investiga y construye la postura

Lee `references/research-protocol.md`. Busca información actual o históricamente válida en este orden:

1. Documentos y bases de datos de la ONU.
2. Gobierno, cancillería, misión permanente, parlamento y legislación de la delegación.
3. Tratados, votos y organizaciones regionales.
4. Organismos internacionales especializados.
5. Investigación académica y periodismo reputado para contexto o contradicciones.

Mantén un registro de afirmaciones con fuente, fecha, enlace y nivel de confianza. Abre las páginas utilizadas; no cites fragmentos de resultados de búsqueda. Contrasta los datos que definan la postura. Si la evidencia oficial es ambigua, dilo y formula una inferencia prudente.

Lee `references/committee-mandate.md` para comprobar que cada solución encaja con las atribuciones del comité.

### 3. Confirma la estrategia

Antes de escribir la versión final, presenta al usuario una síntesis breve:

- postura oficial encontrada;
- intereses y vulnerabilidades de la delegación;
- dos o tres líneas rojas;
- aliados o bloques plausibles;
- tres a seis soluciones viables;
- dudas o conflictos entre fuentes.

Pide que confirme o corrija la estrategia. Si no responde pero pidió continuar de forma autónoma, conserva las ideas que ya proporcionó y marca las inferencias con cautela.

### 4. Redacta

Lee `references/format-and-style.md`. Usa el formato exigido por la conferencia. Si no hay reglas, aplica el perfil `ganador-clasico` descrito allí:

- bloque de identificación;
- introducción o saludo breve solo si la conferencia lo permite;
- contexto relevante;
- experiencia y postura de la delegación;
- soluciones concretas;
- bibliografía verificable.

La estructura debe avanzar como argumento: problema relevante -> interés de la delegación -> postura -> mecanismo propuesto. Cada solución debe identificar actor, acción, mecanismo y propósito. Evita listas de resoluciones sin análisis.

Adapta la voz a las respuestas o muestra de escritura del delegado, pero corrige errores involuntarios. No introduzcas faltas, rarezas o vaguedad para simular escritura humana.

### 5. Genera y revisa el documento

Para Word o PDF, lee `references/document-generation.md`. Prepara un JSON conforme al esquema y ejecuta `scripts/build_position_paper.py`. Si el entorno dispone de herramientas de documentos, renderiza el DOCX a imágenes, revisa todas las páginas y corrige defectos antes de entregar.

El archivo final no debe contener comentarios internos, marcadores sin rellenar, citas técnicas del sistema ni datos personales no autorizados.

### 6. Control de calidad

Lee `references/rubric.md` y evalúa el borrador. Corrige antes de entregar si ocurre cualquiera de estos fallos críticos:

- una afirmación central no tiene respaldo;
- la postura podría pertenecer indistintamente a cualquier país;
- una solución está fuera del mandato;
- falta el vínculo entre propuesta e interés nacional;
- se excede la extensión;
- hay errores de gramática, nombres oficiales o formato;
- el render muestra cortes, solapamientos, páginas casi vacías o URLs ilegibles.

Entrega el documento, una lista o anexo de fuentes y una nota breve de los puntos que el delegado debe verificar personalmente. Invita a una última revisión de voz y estrategia.

## Modos adicionales

- **Revisión de borrador:** conserva las ideas del usuario, identifica afirmaciones que requieren fuente y explica cambios sustantivos.
- **Múltiples tópicos:** investiga y redacta cada tópico por separado, respetando el límite total de páginas.
- **Comité histórico o crisis:** congela la investigación en la fecha establecida y diferencia conocimiento del personaje, conocimiento de la delegación y conocimiento del participante.
- **Sin acceso web:** no inventes investigación. Produce un esquema, lista de búsquedas pendientes y borrador explícitamente provisional.

## Recursos

- `references/intake.md`: entrevista y decisiones de alcance.
- `references/research-protocol.md`: fuentes, verificación y registro de evidencia.
- `references/committee-mandate.md`: competencia y diseño de soluciones.
- `references/format-and-style.md`: estructura, formato y voz.
- `references/document-generation.md`: esquema JSON, DOCX, PDF y QA visual.
- `references/rubric.md`: evaluación final.
- `references/reference-paper-analysis.md`: lecciones extraídas del paper ganador usado como referencia.
