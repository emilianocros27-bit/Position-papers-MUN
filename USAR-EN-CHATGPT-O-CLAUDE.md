# Usar en un chat normal de ChatGPT o Claude

Pegar únicamente la URL del repositorio no garantiza que un chat lea todos sus archivos. El método más fiable es usar el archivo autosuficiente [`PROMPT-CHAT-NORMAL.md`](PROMPT-CHAT-NORMAL.md).

## Opción 1: un chat aislado

1. Descarga `PROMPT-CHAT-NORMAL.md` desde GitHub.
2. Adjunta el archivo al chat.
3. Envía este mensaje:

```text
Lee completamente el archivo PROMPT-CHAT-NORMAL.md antes de responder. Trátalo como las instrucciones de trabajo para esta conversación y comienza la entrevista inicial. Pregunta únicamente por los datos que todavía no te haya dado.
```

También puedes pegar el contenido completo del archivo directamente en el chat. Esto es más fiable que pedirle al modelo que recorra todo el repositorio.

## Opción 2: ChatGPT Project

1. Crea un proyecto nuevo.
2. Añade `PROMPT-CHAT-NORMAL.md` como archivo del proyecto.
3. En las instrucciones del proyecto pega:

```text
Para cualquier solicitud de position paper, lee y aplica completamente PROMPT-CHAT-NORMAL.md. Comienza siempre con la entrevista y no redactes antes de investigar y confirmar la estrategia.
```

4. Inicia un chat nuevo dentro del proyecto y escribe:

```text
Quiero crear mi position paper. Empieza las preguntas.
```

## Opción 3: Claude Project

1. Crea un proyecto en Claude.ai.
2. Sube `PROMPT-CHAT-NORMAL.md` al conocimiento del proyecto.
3. En las instrucciones del proyecto pega el mismo texto breve de la opción anterior.
4. Inicia una conversación nueva dentro de ese proyecto.

## Opción solo con enlace

Si el chat tiene navegación web, puedes enviar el enlace directo al archivo sin formato de GitHub:

```text
https://raw.githubusercontent.com/emilianocros27-bit/Position-papers-MUN/main/PROMPT-CHAT-NORMAL.md
```

Mensaje sugerido:

```text
Abre y lee completamente este archivo. Confirma que pudiste acceder a él y luego aplica sus instrucciones para comenzar la entrevista de mi position paper. Si no puedes abrirlo, dímelo y te lo adjunto; no improvises su contenido.
```

Este método depende de que el producto tenga acceso web y permita abrir GitHub. Adjuntar el archivo sigue siendo la opción más confiable.

## Limitaciones reales

- Ningún modelo puede garantizar un resultado “perfecto” sin conocer la guía, investigar fuentes y recibir revisión del delegado.
- Un chat sin búsqueda web no puede verificar una postura nacional actual.
- La creación directa de DOCX o PDF depende de las herramientas habilitadas en esa cuenta y conversación.
- Ningún método puede garantizar el resultado de detectores de IA. La guía busca originalidad auténtica mediante participación del delegado y revisión humana, no evasión técnica.
