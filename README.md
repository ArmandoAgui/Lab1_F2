# Reportes de Física II

El repositorio contiene un directorio independiente para cada práctica:

- `lab1/`: reporte final de la Práctica 1, con su fuente LaTeX, imágenes, tablas, bibliografía y plantilla IEEE.
- `lab2/`: reporte de la Práctica 2.
- `lab3/`: estructura inicial para desarrollar el reporte de la Práctica 3.

Cada laboratorio se compila desde su propia carpeta, por lo que las rutas relativas a imágenes, secciones y bibliografía permanecen separadas.

## Compilación

Se recomienda instalar la extensión **LaTeX Workshop** en Visual Studio Code. Para compilar, abre el archivo `main.tex` del laboratorio correspondiente y utiliza el botón **Build LaTeX project** de la extensión. También puede ejecutarse desde la terminal:

```bash
cd lab1
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Para otro reporte, sustituye `lab1` por `lab2` o `lab3`.
