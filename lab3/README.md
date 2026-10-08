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

## Revisión científica y reproducción de los ajustes

La guía suministrada se conserva en `references/guia_practica3_II2026.pdf`.
Los datos de `data/armonicos.csv` y `data/agua.csv` transcriben las tablas del reporte anterior; no representan nuevas mediciones. Para recalcular ajustes y coordenadas:

```bash
python3 scripts/recalcular.py
```

`data/resultados_ajustes.json` conserva los parámetros sin redondear, residuos y discrepancias. Los errores estándar son condicionales al ajuste ordinario; no son incertidumbres experimentales completas. Las figuras vectoriales en `figures/` se compilan con PGFPlots/TikZ. Las fotografías originales permanecen intactas.

El estilo bibliográfico `Plantilla_LATEX/IEEEtran.bst` se obtuvo de CTAN: https://mirrors.ctan.org/macros/latex/contrib/IEEEtran/bibtex/IEEEtran.bst

Consultar `PENDIENTES_VALIDACION.md` y `AUDITORIA_FINAL.md` antes de entregar. La Tabla 8 no se realizó por indicación de la instructora. Las incertezas no disponibles se dejaron fuera del alcance de corrección por indicación posterior del usuario.

Respaldo anterior a la edición: `../respaldos/lab3_antes_correccion_20261008.tar.gz`.
