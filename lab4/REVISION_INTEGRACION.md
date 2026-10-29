# Revisión de marco teórico y conclusiones

## Integración

Se revisó e integró el texto aportado por el equipo. Se mantuvo la propagación conservadora mediante suma de contribuciones absolutas y se retiró la propuesta de suma en cuadratura. La incertidumbre se expresa como una magnitud no negativa; el signo ± se utiliza al presentar resultados.

Se corrigieron unidades, subíndices y condiciones de validez. La temperatura inicial del hielo de la fórmula corresponde a su temperatura de fusión: si estuviera por debajo de ella, faltaría el calentamiento previo del sólido. Se sustituyó «hielo seco» por hielo de agua con la humedad superficial retirada, para evitar confusión con dióxido de carbono sólido.

Las ecuaciones de calibración, calor del hielo, temperaturas teóricas y error porcentual se trasladaron del análisis al marco teórico, conservando sus etiquetas. En el análisis se mantienen sus sustituciones numéricas y referencias cruzadas. También se sustituyeron las referencias manuales a números de ecuaciones y tabla en la discusión. No se incluyó la tabla de símbolos porque las variables y unidades están definidas en el texto y la tabla recibida duplicaba información.

Se incorporaron las entradas `serway` y `taylor` a partir de los metadatos ya disponibles en `lab1/referencias.bib`, sin añadir ediciones, años ni páginas supuestos. Se conservó la entrada de la guía. No se modificaron el título, los autores, la metodología, las fotografías, la gráfica, las tablas experimentales, la declaración de IA, el resumen ni la introducción.

## Confirmaciones pendientes

1. **Masa de agua fría del tercer ensayo confirmada:** el usuario confirmó 69.4 g, coincidente con la tabla actual. Se retiraron las advertencias sobre la discrepancia con 64.4 g. No fue necesario modificar los cálculos por este dato.
2. La confirmación de la masa resuelve la discrepancia de transcripción; se corrigió la incertidumbre del calor del hielo a 22.5 cal por confirmación del usuario. Sigue pendiente aclarar el tratamiento de la temperatura inicial del hielo en las incertidumbres teóricas.
3. La guía oficial de la Práctica 4 no está en `references/`; no se pudo comprobar directamente qué convención de incertidumbre prescribe. Se mantuvo el método efectivamente utilizado en el informe.

## Observaciones científicas y aritméticas

- Los ensayos 1 y 2 tienen T=T₁, de modo que el cociente de calibración no se puede evaluar. El resultado 51.2 ± 208.4 cal/°C procede únicamente del tercero; no es un promedio de tres determinaciones.
- La diferencia T−T₁ del tercer ensayo es −2 °C y su incertidumbre conservadora es 2 °C. Su intervalo alcanza cero. La propagación lineal de un cociente en estas condiciones no proporciona una cota rigurosa; la incertidumbre reportada se conserva como aproximación, sin interpretarla como validación precisa o estimación robusta del orden de magnitud.
- Se restituyeron los factores de calor específico en la ecuación de incertidumbre del calor del hielo. Con c=1 cal/(g·°C), Δmₕ=0.10 g y ΔTexp=ΔTₕ=1 °C, la expresión produce 22.5 cal, frente a 16.3 cal consignadas. El usuario confirmó la corrección a 22.5 cal: se actualizó la tabla, la discusión y la incertidumbre relativa a 3.6 %, se incluyó la sustitución numérica en el análisis y se retiró la advertencia correspondiente de las conclusiones.
- Las incertidumbres teóricas reportadas de 5.17 °C y 1.03 °C se reproducen aproximadamente al omitir la contribución de Tₕ. La tabla declara ΔTₕ=1 °C. Debe aclararse si Tₕ se trata como condición fija de fusión o como entrada medida con incertidumbre. No se cambió ese supuesto automáticamente ni se sustituyeron resultados afectados por la calibración pendiente.
- Las cifras centrales del calor del hielo (626.2 cal), calor de fusión (496 cal) y residuo (105.1 cal) son aritméticamente coherentes con la transcripción actual. El residuo depende del calor del calorímetro y su interpretación sigue limitada por la incertidumbre de la calibración.
- Los errores 2.86 % y 10.59 % coinciden al utilizar temperaturas teóricas sin redondear. La sustitución impresa con 20.42 °C daría 2.84 %, diferencia de redondeo que se aclara en el texto sin alterar el resultado. El error relativo basado en Celsius depende del origen de la escala; se mantiene como indicador convencional del informe.
- El menor error central al incluir el calorímetro no demuestra una validación precisa. Los posibles efectos del ambiente y de la humedad se presentan como hipótesis, sin atribuciones causales cuantitativas no demostradas.

## Criterios de la rúbrica

| Criterio | Estado de la revisión |
| --- | --- |
| Formato y estructura (10 %) | Se conserva la plantilla IEEE y se utilizan referencias automáticas. |
| Marco teórico (15 %) | Conceptos, ecuaciones, unidades, incertidumbres e hipótesis integrados y vinculados al análisis. |
| Metodología (10 %) | Conservada; contraste directo con la guía pendiente. |
| Análisis (35 %) | Masa del tercer ensayo confirmada en 69.4 g. Incertidumbres pendientes de revisión. |
| Discusión (15 %) | Conservada con ajustes de referencias y nomenclatura; sus cifras provisionales requieren revisión posterior. |
| Conclusiones (10 %) | Integradas con límites explícitos, mejoras experimentales y carácter provisional. |
| Bibliografía (5 %) | Entradas de Serway y Taylor recuperadas del proyecto, con citas IEEE. |

No se asigna una nota: las discrepancias pendientes impiden afirmar una verificación científica definitiva. El resumen y la introducción permanecen pendientes por instrucción del usuario.
