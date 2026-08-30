# Lab1_F2

Proyecto LaTeX para reporte de laboratorio de física en formato IEEE.

## Estructura

- `main.tex`: archivo principal del reporte.
- `sections/`: contenido dividido por secciones.
- `tables/`: tablas reutilizables del reporte.
- `images/`: imagenes y graficas exportadas.
- `diagrams/`: esquemas del montaje experimental.
- `appendix/`: anexos.
- `referencias.bib`: bibliografia en formato BibTeX.
- `Plantilla_LATEX/`: plantilla original proporcionada por el catedratico.

## Compilacion

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```
