# Lab1_F2

Proyecto LaTeX para elaborar un reporte de laboratorio de fisica en formato IEEE. La estructura esta organizada por archivos separados para que sea mas facil editar cada parte del documento sin trabajar todo dentro de un solo archivo grande.

## Requisitos

Para editar y compilar el reporte se recomienda usar Visual Studio Code con la extension **LaTeX Workshop**.

Tambien es necesario tener instalada una distribucion de LaTeX, por ejemplo:

- **TeX Live** en Linux.
- **MiKTeX** en Windows.
- **MacTeX** en macOS.

## Estructura del proyecto

```text
Lab1_F2/
├── appendix/
├── diagrams/
├── images/
├── Plantilla_LATEX/
├── sections/
├── tables/
├── .gitignore
├── main.tex
├── referencias.bib
├── reporte_fisica_ieee.tex
└── README.md
```

## Descripcion de carpetas y archivos

- `main.tex`: archivo principal del reporte. Desde aqui se cargan las secciones, tablas, imagenes y bibliografia.
- `reporte_fisica_ieee.tex`: archivo secundario que carga `main.tex`. Se deja por compatibilidad si ya se estaba trabajando con ese nombre.
- `sections/`: contiene las partes principales del reporte.
- `sections/00_preamble.tex`: paquetes, configuraciones generales y rutas de imagenes.
- `sections/01_resumen.tex`: resumen y palabras clave.
- `sections/02_introduccion.tex`: introduccion y marco teorico.
- `sections/03_metodologia.tex`: metodologia, materiales, instrumentos y montaje experimental.
- `sections/04_analisis.tex`: datos, procesamiento, incertidumbre, graficas y comparacion con el modelo fisico.
- `sections/05_discusion.tex`: interpretacion de resultados, discrepancias, limitaciones y fuentes de error.
- `sections/06_conclusiones.tex`: conclusiones del experimento.
- `sections/07_agradecimientos.tex`: agradecimientos opcionales.
- `tables/`: tablas separadas del cuerpo principal del documento.
- `tables/instrumentos.tex`: tabla de instrumentos, resoluciones e incertidumbres.
- `tables/datos_experimentales.tex`: tabla base para los datos medidos.
- `images/`: imagenes y graficas usadas en el reporte.
- `diagrams/`: esquemas del montaje experimental.
- `appendix/`: anexos o material complementario.
- `referencias.bib`: bibliografia en formato BibTeX.
- `Plantilla_LATEX/`: plantilla IEEE original proporcionada por el catedratico.
- `.gitignore`: evita guardar archivos temporales generados por LaTeX.

## Como editar el reporte

El archivo recomendado para trabajar es `main.tex`. Sin embargo, la mayoria del contenido se escribe dentro de los archivos de `sections/`.

Por ejemplo:

- Para cambiar el resumen, editar `sections/01_resumen.tex`.
- Para agregar teoria y ecuaciones, editar `sections/02_introduccion.tex`.
- Para modificar el procedimiento, editar `sections/03_metodologia.tex`.
- Para agregar datos, graficas y calculos, editar `sections/04_analisis.tex`.
- Para agregar referencias, editar `referencias.bib` y citar con `\cite{clave}`.

## Compilar con LaTeX Workshop

1. Abrir la carpeta del proyecto `Lab1_F2` en Visual Studio Code.
2. Abrir el archivo `main.tex`.
3. Presionar `Ctrl + Alt + B` para compilar.
4. La extension LaTeX Workshop generara el archivo `main.pdf`.
5. Para ver el PDF dentro de VS Code, usar el boton de vista previa de LaTeX Workshop o ejecutar el comando:

```text
LaTeX Workshop: View LaTeX PDF
```

Si el PDF no muestra cambios despues de editar la bibliografia, compilar dos veces mas o usar la receta completa de LaTeX Workshop.

## Compilar desde la terminal

Desde la carpeta principal del proyecto, ejecutar:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

El resultado sera el archivo:

```text
main.pdf
```

## Notas sobre bibliografia

Las referencias se guardan en `referencias.bib`. Cada entrada tiene una clave, por ejemplo:

```bibtex
@book{serway2018,
  author    = {Serway, Raymond A. and Jewett, John W.},
  title     = {Physics for Scientists and Engineers},
  edition   = {10},
  publisher = {Cengage Learning},
  year      = {2018}
}
```

Para citar esa fuente dentro del texto:

```latex
\cite{serway2018}
```

La bibliografia se genera automaticamente en formato IEEE al compilar con BibTeX.
