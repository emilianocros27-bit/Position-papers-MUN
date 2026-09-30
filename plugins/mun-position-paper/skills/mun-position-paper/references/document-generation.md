# Generación del documento

## Esquema de entrada

El generador acepta UTF-8 JSON. Campos obligatorios:

```json
{
  "committee": "Nombre oficial del comité",
  "delegation": "Nombre oficial de la delegación",
  "topic": "Nombre exacto del tópico",
  "background": ["Párrafo verificado"],
  "national_position": ["Párrafo de postura"],
  "solutions": ["Solución concreta"],
  "bibliography": [
    {
      "author": "Organismo o autor",
      "date": "2026-01-31",
      "title": "Título",
      "url": "https://example.org/fuente"
    }
  ]
}
```

Campos opcionales:

- `delegate`
- `school`
- `conference`
- `opening`
- `language`
- `flag_path`
- `include_page_numbers`
- `bibliography_title`

`background` y `national_position` pueden contener uno o varios párrafos. `solutions` requiere al menos una entrada. `bibliography` puede quedar vacía únicamente para un borrador explícitamente provisional.

## Comando

```bash
python scripts/build_position_paper.py input.json --output position-paper.docx
```

Opciones:

```bash
python scripts/build_position_paper.py input.json \
  --output position-paper.docx \
  --pdf \
  --pdf-output position-paper.pdf
```

La conversión a PDF busca `libreoffice` o `soffice`. Si el entorno ofrece una herramienta de documentos administrada, úsala de preferencia y conserva el DOCX como fuente editable.

## Preparación de la bandera

Descarga solo una imagen cuya procedencia sea confiable o usa un archivo proporcionado por el usuario. Respeta la proporción y comprueba que la conferencia permita imágenes. Si no hay bandera válida, omítela; no la inventes ni uses un emoji.

## Revisión estructural

Antes de generar:

- no debe haber campos obligatorios vacíos;
- cada párrafo debe ser una cadena completa;
- las soluciones no deben contener viñetas prefijadas, porque el script las añade;
- las URLs deben usar `https://` o `http://`;
- no deben quedar marcadores como `[PAÍS]`, `TODO` o `por confirmar` en una versión final.

## Revisión visual

Renderiza el DOCX a PNG o PDF y examina todas las páginas. Comprueba:

- bandera nítida y sin deformación;
- encabezado equilibrado;
- texto legible y sin cortes;
- viñetas alineadas;
- encabezados unidos al contenido siguiente;
- bibliografía legible y URLs ajustadas;
- ausencia de una última página casi vacía;
- numeración correcta.

Si hay una página casi vacía, no reduzcas todo el documento automáticamente. Ajusta primero espacios, saltos, longitud de URLs o distribución de la bibliografía.

## Archivos de salida

Usa nombres descriptivos sin datos sensibles innecesarios, por ejemplo:

```text
Pakistan_UNSC_Forced_Displacement_Position_Paper.docx
```

Entrega también un expediente de fuentes cuando el formato del paper no permita bibliografía completa.
