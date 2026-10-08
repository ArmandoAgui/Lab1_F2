# Validación del equipo — Laboratorio 3

La Tabla 8 y su procedimiento están excluidos por indicación de la instructora. No se solicitan resultados de esa actividad.

La guía oficial suministrada se conserva en `references/guia_practica3_II2026.pdf`. La rúbrica de su página 5 es de preparación del cuaderno; no es la rúbrica del artículo científico. La evaluación utiliza provisionalmente los 17 criterios de la auditoría inicial.

## 1. Información indispensable para confirmar resultados

- **Barrido inicial:** el procedimiento de la guía prescribe 150–2150 Hz, 10 s y dos repeticiones; su Tabla 3 imprime 100–2300 Hz y 20 s. El reporte original repite esta última configuración. La captura `150_2150Hz.jpeg` muestra el analizador, sin controles del generador. Confirmar intervalo y duración reales; no se deducen del nombre del archivo.
- **Repeticiones:** confirmar cuántos barridos se realizaron en cada condición y si las frecuencias registradas son lecturas individuales o resultados de varias lecturas. Las dos repeticiones prescritas no se presentan como un hecho observado.
- **Volúmenes de agua:** confirmar que 0, 75, 150, 225, 300, 375 y 450 cm³ son los niveles realmente utilizados. Se conservaron las tablas originales, pero no existe una transcripción legible del cuaderno independiente de ellas. Confirmar si se añadieron incrementos de 75 cm³ hasta alcanzar esos volúmenes totales.
- **Nivel de 50 mL:** la guía lo menciona al inicio de la parte II, pero no está entre los siete datos. No se inventó una medición ni se alteraron los volúmenes existentes.
- **Diapasones (aclaración incorporada):** el equipo confirmó el uso de los cuatro diapasones de 256, 320, 384 y 480 Hz, con respuesta resonante audible y sin agregar agua adicional. La Tabla VII registra cuatro ceros de volumen adicional, sin asignarles una incerteza no confirmada. Falta un registro diferenciado del volumen total en cada prueba para contrastar cuantitativamente las predicciones.
- **Declaración de IA:** confirmar la descripción del apoyo realmente utilizado y realizar la revisión final del equipo. El reporte no afirma que esa validación ya ocurrió.
- **Rúbrica del artículo:** proporcionar el documento oficial si se dispone de él. La preparación y lista de cotejo del cuaderno no sustituyen los 17 criterios del artículo.

## 2. Información útil, pero no imprescindible para los cálculos actuales

- Nombre y versión del generador y analizador; el registro identifica el analizador como Spectroid.
- Modelo del teléfono, posición del micrófono y altavoz y grado de obstrucción de la abertura.
- Instrumento para dosificar agua, lectura del menisco y temperatura durante la práctica.
- Cuaderno legible, espectros originales y relación entre cada captura y nivel de agua.
- Edición del ejemplar de Young/Freedman efectivamente consultado. Su entrada original se conserva, pero no se cita en la versión revisada porque esa edición no se verificó; se emplean guía, Halliday y OpenStax.

## 3. Limitaciones declaradas si no existen registros

- Sin repeticiones documentadas, la diferencia entre series no estima reproducibilidad estadística.
- La respuesta resonante de los cuatro diapasones está confirmada cualitativamente; sin sus volúmenes totales diferenciados no puede calcularse el error relativo de volumen.
- Sin calibración no se interpretan los dB de la aplicación como nivel acústico absoluto.
- Sin posiciones y geometría documentadas no puede cuantificarse el efecto de la abertura parcialmente cubierta.

## Incertezas: alcance solicitado por el usuario

El usuario pidió pasar por alto información adicional de incertezas. La Tabla VI se conserva exactamente, incluidas las incertezas proporcionadas por el instructor y la fila de volumen cero. No se solicita reconstruirlas. Los errores estándar de regresión existentes se distinguen de la incertidumbre experimental total; en esta revisión no se recalcularon los ajustes.

## Respaldo y trazabilidad

- Respaldo completo anterior a las correcciones: `../respaldos/lab3_antes_correccion_20261008.tar.gz`.
- Las fotografías originales y la auditoría inicial no se modificaron.
- `data/armonicos.csv` y `data/agua.csv` transcriben las frecuencias y volúmenes de las tablas originales; no son nuevas mediciones.
- `scripts/recalcular.py` reproduce los ajustes ordinarios y genera las coordenadas de las gráficas.
- El resultado libre de agua se conserva como principal por el intercepto y los residuos; no se seleccionó el ajuste al origen para acercar artificialmente la velocidad al valor térmico.
