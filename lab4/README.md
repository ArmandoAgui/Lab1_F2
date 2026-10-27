# Laboratorio 4

Estructura inicial del reporte de la Práctica 4 de Física II. Conserva el formato IEEE de los laboratorios anteriores: clase IEEEtran en modo conferencia, dos columnas, autores en disposición de dos por dos, idioma español y secciones independientes.

El título y el contenido están marcados como pendientes hasta disponer de la guía y de las mediciones. No se han copiado resultados ni fuentes de otras prácticas.

## Estructura

- `main.tex`: título, autores, orden de secciones y bibliografía.
- `sections/`: preámbulo, resumen y palabras clave, introducción y objetivos, marco teórico, metodología, resultados y análisis, discusión, conclusiones y declaración de IA.
- `images/`: fotografías y gráficas exportadas.
- `diagrams/`: esquemas del montaje.
- `figures/`: figuras vectoriales en TikZ/PGFPlots.
- `tables/`: tablas en LaTeX para incluir mediante `\input`.
- `data/`: mediciones originales y datos procesados.
- `scripts/`: scripts de cálculo cuando sean necesarios.
- `references/`: guía de la práctica y documentos de consulta.
- `appendix/`: material complementario; incluirlo en `main.tex` cuando corresponda.
- `referencias.bib`: bibliografía propia de la Práctica 4, inicialmente sin entradas.
- `Plantilla_LATEX/`: clase IEEEtran, estilo BibTeX y manual, copiados del Lab 3.

## Compilación inicial

Desde `lab4/`, sin citas bibliográficas todavía:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Se genera `main.pdf`. Mientras no exista `main.bbl`, el documento muestra una indicación pendiente en Referencias. El aviso inicial `No file main.bbl` es esperable.

Cuando se agreguen entradas en `referencias.bib` y citas mediante `\cite{clave}`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

También puede abrirse `main.tex` en Visual Studio Code y compilar con LaTeX Workshop. El preámbulo conserva las herramientas de los reportes anteriores para ecuaciones, unidades con `siunitx`, tablas con `booktabs` y gráficas con TikZ/PGFPlots.

## Para completar el informe

1. Guardar la guía en `references/` y actualizar el título de `main.tex`.
2. Completar objetivos, teoría y procedimiento según la práctica asignada.
3. Incorporar mediciones, tablas, fotografías, gráficas y análisis.
4. Redactar discusión, conclusiones y resumen a partir de los resultados.
5. Añadir las fuentes consultadas y actualizar la declaración de IA.
