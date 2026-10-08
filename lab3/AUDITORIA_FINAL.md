# Auditoría final — Laboratorio 3 de Física II

## Resultado y alcance

**Estimación inicial: 5,65/10. Estimación de la versión revisada: 8,65/10. Mejora estimada: 3,00 puntos.** No es una calificación oficial ni una garantía de 10/10. Los puntos restantes dependen principalmente de trazabilidad experimental, resultados de diapasones y tratamiento de incertidumbre que el usuario dejó fuera del alcance actual.

La guía oficial de cinco páginas se revisó completa. Sus cuatro objetivos y cuestionario se incorporaron al análisis. Su página 5 contiene la rúbrica de preparación del cuaderno, no la rúbrica del artículo científico. Se utilizan provisionalmente los 17 criterios de la solicitud original, cuya suma es 10 puntos. Los criterios 15–16 se interpretan como criterios de conclusiones, como en la auditoría inicial.

La Tabla 8 está excluida por indicación de la instructora, sin penalización. La exclusión no se extiende a la Tabla 7.

## A. Evaluación por criterio

| N.º | Criterio | Máximo | Estimado | Estado | Evidencia y pendiente |
|---:|---|---:|---:|---|---|
| 1 | Plantilla, organización y numeración | 0,60 | 0,60 | Cumple | IEEEtran en dos columnas, siete tablas y nueve figuras con etiquetas automáticas; citas y referencias resueltas. |
| 2 | Redacción, nomenclatura y unidades | 0,40 | 0,38 | Cumple parcialmente | Se distingue orden de resonancia, armónico y cociente; ejes físicos, unidades corregidas y separador decimal uniforme. Quedan refinamientos menores sujetos a criterio docente. |
| 3 | Principios físicos y variables | 0,70 | 0,70 | Cumple | Condiciones de presión/desplazamiento, modos de ambos tubos, temperatura, longitud efectiva, volumen y Fourier. |
| 4 | Relación teoría–experimento | 0,40 | 0,40 | Cumple | Gráficas f–L' y f–1/L'; análisis del intercepto y distinción entre predicción y ajuste. |
| 5 | Fuentes y citas | 0,40 | 0,40 | Cumple | Guía suministrada, Halliday verificado, OpenStax y fuente del autor sobre DFT; claves válidas y citas resueltas. |
| 6 | Procedimiento e instrumentos | 0,70 | 0,40 | Cumple parcialmente | Se describen etapas y se separa prescripción de guía de observación registrada. Faltan barrido inicial inequívoco, repeticiones, dosificación y procedimiento completo de diapasones. |
| 7 | Esquema experimental | 0,30 | 0,28 | Cumple parcialmente | Esquema distingue longitud física, efectiva, corrección y agua. Ubicación exacta de transductores no confirmada. |
| 8 | Datos e incertidumbres | 0,80 | 0,50 | Cumple parcialmente | Se conservan frecuencias, volúmenes e incertezas originales; redondeos y unidades legibles. Faltan incertidumbres de frecuencia y validación del origen de las ya tabuladas; Tabla 7 sin resultados verificables. |
| 9 | Gráficas, ajustes y propagación | 1,00 | 0,70 | Cumple parcialmente | Tres gráficas vectoriales, OLS reproducible, parámetros, errores estándar y comparación de restricciones. El usuario dejó fuera la reconstrucción de incertidumbres; no hay propagación experimental total de agua ni barras inventadas. |
| 10 | Interpretación cuantitativa | 0,90 | 0,80 | Cumple parcialmente | Tres determinaciones, errores relativos y residuos analizados. No puede calcularse el error de volúmenes experimentales de diapasones. |
| 11 | Comparación y fuentes de error | 0,80 | 0,72 | Cumple parcialmente | Dos mecanismos sistemáticos y dos aleatorios explicados, intercepto y limitaciones. Sus contribuciones no están cuantificadas. |
| 12 | Significado físico y objetivos | 0,60 | 0,55 | Cumple parcialmente | Objetivos oficiales identificados y evaluación prudente de cumplimiento. La verificación con diapasones permanece limitada. |
| 13 | Discrepancias y limitaciones | 0,50 | 0,45 | Cumple parcialmente | Se discute sesgo aparente de agua, geometría y diferencia entre series; no se discrimina experimentalmente su causa. |
| 14 | Afirmaciones respaldadas | 0,40 | 0,35 | Cumple parcialmente | Se eliminó atenuación y comprobaciones no demostradas; se aclaran registros incompletos. La fuente primaria legible del cuaderno aún no está disponible. |
| 15 | Resultados y objetivos en conclusiones | 0,60 | 0,55 | Cumple parcialmente | Conclusiones cuantitativas y coherentes; algunos aspectos experimentales no verificables limitan cumplimiento completo. |
| 16 | Conclusiones y mejoras | 0,40 | 0,37 | Cumple parcialmente | Mejoras específicas del montaje y registro, sin resultados nuevos. Validación final del equipo pendiente. |
| 17 | Bibliografía IEEE | 0,50 | 0,50 | Cumple | Cuatro referencias citadas, datos verificables y estilo IEEEtran local; entradas originales no citadas se preservan sin publicarlas como bibliografía utilizada. |
| | **Total** | **10,00** | **8,65** | | |

## B. Comparación antes/después

- Resumen, palabras clave, introducción y conclusiones: de instrucciones de plantilla a contenido científico completo.
- Teoría: se conservan las explicaciones correctas y se añaden limitaciones, figura comparativa de modos y explicación de Fourier.
- Armónicos: se conserva cada frecuencia y se distinguen orden, cociente y número entero asignado.
- Agua: se sustituye la interpretación de atenuación por el modelo inverso y se realiza la tercera determinación requerida por el cuestionario.
- Diapasones: los ceros no confirmados se identifican como datos no verificables; no se inventa un error experimental.
- Presentación: Tabla I legible, gráficas con ejes/unidades, citas y referencias resueltas y columnas finales equilibradas.
- Incertezas: por instrucción posterior del usuario, se conservan las existentes sin reconstruir información no disponible. Esta decisión limita la puntuación; no convierte el requisito académico en cumplido.

## C. Resultados recalculados

Se usaron frecuencias y volúmenes transcritos de las tablas del reporte original; las longitudes se calcularon sin redondeo intermedio. `scripts/recalcular.py` guarda resultados completos en `data/resultados_ajustes.json`.

| Determinación | Resultado | Alcance de la cifra ± | Discrepancia frente a vT |
|---|---|---|---|
| Referencia térmica | 345,875 m/s, publicada como 345,9 ± 0,6 m/s | Incerteza original conservada | Referencia |
| Armónicos | 341,3085 m/s, publicada como 341,3 ± 7,7 m/s | Incerteza original conservada; error estadístico de pendiente 4,7976 Hz | 1,32027 % |
| Agua, intercepto libre | 361,2655 m/s, publicada como 361,3 m/s con error estándar 4,3 m/s | Solo error estándar condicional del ajuste | 4,44974 % |
| Agua, al origen; contraste | 340,5829 m/s, error estándar 3,0 m/s | Solo error estándar condicional, no resultado principal | 1,53006 % |

Armónicos: m = 227,539 Hz; b = −13,017 Hz; R² = 0,998668.

Agua libre: m = 90,31638 m/s; b = −24,21519 Hz; s_m = 1,08152 m/s; s_b = 4,81427 Hz; R² = 0,9992835. SSE = 78,32065 Hz².

Agua al origen: m = 85,14573 m/s; SSE = 474,61826 Hz². El aumento de residuos y su patrón justifican no seleccionarlo solo por cercanía térmica.

El porcentaje de armónicos cambia de 1,34 % a 1,32 % porque ahora se usa la pendiente sin redondear al calcular velocidad y discrepancia. No se cambió ninguna frecuencia experimental.

Volúmenes teóricos recalculados: 73,10377; 205,74517; 294,17277 y 382,60037 cm³ para 256, 320, 384 y 480 Hz. Las incertezas teóricas preexistentes se conservaron.

## D. Registro de modificaciones

### Archivos actualizados

- `main.tex`: conserva íntegros título y bloque de autoría; carga el estilo bibliográfico local y equilibra las columnas finales.
- `sections/00_preamble.tex`: compatibilidad de TikZ con babel, balance y formato decimal uniforme.
- `sections/01_resumen.tex`: resumen cuantitativo y seis palabras clave.
- `sections/02_introduccion.tex`: fenómeno, importancia y objetivos oficiales.
- `sections/02_marco_teorico.tex`: conserva fundamentos correctos; cita guía y añade limitaciones, comparación modal y DFT.
- `sections/03_metodologia.tex`: separa información registrada, parámetros prescritos y datos no confirmados; preserva fotografías.
- `sections/04_analisis.tex`: siete tablas revisadas, cálculos y OLS, tres determinaciones, gráficas físicas y tratamiento explícito de diapasones no verificables.
- `sections/05_discusion.tex`: interpreta pendientes, interceptos, discrepancias y calidad sin confundir exactitud, precisión y reproducibilidad.
- `sections/06_conclusiones.tex`: conclusiones respaldadas por resultados existentes.
- `sections/07_declaracion_ia.tex`: describe el apoyo efectivamente realizado sin afirmar validación final del equipo.
- `referencias.bib`: agrega guía, OpenStax y fuente DFT; conserva entradas originales.
- `README.md`: instrucciones de reproducción y trazabilidad.
- `main.pdf`: PDF compilado actualizado.

### Archivos añadidos

- `data/armonicos.csv`, `data/agua.csv`: transcripción de datos existentes.
- `scripts/recalcular.py`: ajuste ordinario reproducible sin dependencias externas.
- `data/resultados_ajustes.json`, `data/parametros.tex`, `data/*_plot.dat`: resultados y coordenadas calculados.
- `figures/armonicos.tex`, `figures/agua_longitud.tex`, `figures/agua_inversa.tex`: gráficas vectoriales con datos y modelos.
- `figures/modos_tubos.tex`, `figures/montaje.tex`: comparación ideal de modos y geometría acústica.
- `references/guia_practica3_II2026.pdf`: copia de la guía suministrada.
- `Plantilla_LATEX/IEEEtran.bst`: estilo oficial obtenido de CTAN, necesario para compilar bibliografía en este entorno.
- `PENDIENTES_VALIDACION.md`: registros necesarios y limitaciones, separados por importancia.
- `AUDITORIA_FINAL.md`: esta evaluación.
- `../respaldos/lab3_antes_correccion_20261008.tar.gz`: copia completa anterior a la edición.

Las fotografías, capturas y auditoría inicial no fueron modificadas. Se verificó su identidad con el respaldo, junto con la preservación literal del título y datos de autoría. No se modificaron lab1 ni lab2.

## E. Pendientes del equipo

**Indispensables:** barrido inicial real, repeticiones, volúmenes empleados, significado de ceros y resultados de diapasones, revisión de declaración IA y rúbrica oficial del artículo.

**Útiles:** instrumentos de dosificación, geometría del teléfono, configuración del analizador, registros primarios legibles y temperatura durante mediciones.

**Limitaciones si no existen registros:** no estimar reproducibilidad ni error de volumen experimental; no tratar dB como absolutos; no atribuir posiciones o pruebas no documentadas. No se solicitan ahora incertezas adicionales, conforme a la instrucción del usuario.

La lista detallada está en `PENDIENTES_VALIDACION.md`.

## F. Compilación y control de calidad

- Secuencia completa: pdflatex → bibtex → pdflatex → pdflatex; salidas exitosas.
- Inspección visual de las siete páginas: texto y ecuaciones completos, gráficos vectoriales legibles, tablas con unidades y columna final equilibrada.
- Bibliografía de cuatro referencias; siete tablas y nueve figuras con numeración automática.
- Sin referencias `??`, citas `[?]`, errores de compilación ni advertencias Overfull.
- Se mantienen avisos benignos: la ruta local de clase declara el nombre interno IEEEtran; una caja vertical y una línea de pie de figura producen Underfull. Se revisaron visualmente, sin recortes ni superposiciones.
- Sin instrucciones de plantilla ni referencias manuales a numeración fija.
- Los registros no confirmados se declaran como limitaciones, no como resultados verificados.

El proyecto y PDF quedan en sus ubicaciones habituales. El artículo está sustancialmente mejorado, pero los pendientes experimentales no se ocultan ni se resuelven mediante valores inventados.
