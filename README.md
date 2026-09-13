# Reportes de Física II

El repositorio contiene un directorio independiente para cada práctica:

- `lab1/`: reporte final de la Práctica 1, con su fuente LaTeX, imágenes, tablas, bibliografía y plantilla IEEE.
- `lab2/`: estructura inicial para desarrollar el nuevo reporte.

Cada laboratorio se compila desde su propia carpeta, por lo que las rutas relativas a imágenes, secciones y bibliografía permanecen separadas.

## Compilación

Se recomienda instalar la extensión **LaTeX Workshop** en Visual Studio Code. Para compilar, abre `lab1/main.tex` o `lab2/main.tex` y utiliza el botón **Build LaTeX project** de la extensión. También puede ejecutarse desde la terminal:

```bash
cd lab1
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Para el segundo reporte, sustituye `lab1` por `lab2`.
