# Laboratorio 3

Plantilla del reporte de la Práctica 3 en formato IEEE. El documento principal es `main.tex`; el contenido se distribuye entre los archivos de `sections/`.

## Estructura

- `sections/`: resumen, introducción, metodología, análisis, discusión, conclusiones y declaración de IA.
- `images/`: fotografías y gráficas.
- `diagrams/`: esquemas del montaje.
- `tables/`: tablas separadas del cuerpo del documento.
- `appendix/`: material complementario.
- `referencias.bib`: bibliografía en formato BibTeX.
- `Plantilla_LATEX/`: clase y documentación oficial de IEEEtran.

## Compilación

Desde esta carpeta, ejecutar:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

También puede abrirse `main.tex` en Visual Studio Code y compilarse con LaTeX Workshop.
