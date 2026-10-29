# Revisión de marco teórico y conclusiones

## Integración

Se revisó e integró el texto aportado por el equipo. Se mantuvo la propagación conservadora mediante suma de contribuciones absolutas y se retiró la propuesta de suma en cuadratura. La incertidumbre se expresa como una magnitud no negativa; el signo ± se utiliza al presentar resultados.

Se corrigieron unidades, subíndices y condiciones de validez. La temperatura inicial del hielo de la fórmula corresponde a su temperatura de fusión: si estuviera por debajo de ella, faltaría el calentamiento previo del sólido. Se sustituyó «hielo seco» por hielo de agua con la humedad superficial retirada, para evitar confusión con dióxido de carbono sólido.

Las ecuaciones de calibración, calor del hielo, temperaturas teóricas y error porcentual se trasladaron del análisis al marco teórico, conservando sus etiquetas. En el análisis se mantienen sus sustituciones numéricas y referencias cruzadas. También se sustituyeron las referencias manuales a números de ecuaciones y tabla en la discusión. No se incluyó la tabla de símbolos porque las variables y unidades están definidas en el texto y la tabla recibida duplicaba información.

Se incorporaron las entradas `serway` y `taylor` a partir de los metadatos ya disponibles en `lab1/referencias.bib`, sin añadir ediciones, años ni páginas supuestos. Se conservó la entrada de la guía. No se modificaron el título, los autores, la metodología, las fotografías, la gráfica, las tablas experimentales, la declaración de IA, el resumen ni la introducción.

## Confirmaciones e hipótesis vigentes

1. **Masa de agua fría del tercer ensayo confirmada:** el usuario confirmó 69.4 g, coincidente con la tabla actual. Se retiraron las advertencias sobre la discrepancia con 64.4 g. No fue necesario modificar los cálculos por este dato.
2. El usuario estableció que la guía adopta Tₕ=0 °C como hipótesis del modelo, con ΔTₕ=0. Se corrigió la Tabla II para identificarla como «Fijo por modelo». La incertidumbre del calor del hielo es 16.3 cal y su incertidumbre relativa es 2.6 %. Una desviación real de Tₕ constituye una limitación del modelo, no una incertidumbre instrumental medida.
3. Se mantuvo el método conservador de suma de contribuciones absolutas. La hipótesis de temperatura de fusión indicada por el usuario se explicitó en el marco teórico y el análisis. El archivo completo de la guía no está en `references/`.

## Observaciones científicas y aritméticas

- Los ensayos 1 y 2 tienen T=T₁, de modo que el cociente de calibración no se puede evaluar. El resultado 51.2 ± 208.4 cal/°C procede únicamente del tercero; no es un promedio de tres determinaciones.
- La diferencia T−T₁ del tercer ensayo es −2 °C y su incertidumbre conservadora es 2 °C. Su intervalo alcanza cero. La propagación lineal de un cociente en estas condiciones no proporciona una cota rigurosa; la incertidumbre reportada se conserva como aproximación, sin interpretarla como validación precisa o estimación robusta del orden de magnitud.
- Con Tₕ fijo, la expresión dimensionalmente consistente es ΔQₕ=[L_f+c_a(Texp−Tₕ)]Δmₕ+mₕc_aΔTexp. La sustitución 101(0.10)+6.2(1) da 16.3 cal; se actualizó la Tabla IV y la discusión. Los 22.5 cal correspondían al supuesto descartado de ΔTₕ=1 °C.
- Se verificaron las derivadas de la función completa de temperatura, evitando tratar como independientes las apariciones de una misma variable en numerador y denominador. Con ΔC=208.35 cal/°C antes del redondeo, las contribuciones con calorímetro suman 5.1733833354 °C y sin calorímetro, 1.0306876064 °C. Se conservan 5.17 °C y 1.03 °C. La propagación directa de la calibración usa sus cinco entradas originales y reproduce 208.35 cal/°C. Las lecturas de calibración y las de la segunda parte son distintas; no se introdujo una segunda incertidumbre por los calores intermedios.
- Las cifras centrales del calor del hielo (626.2 cal), calor de fusión (496 cal) y residuo (105.1 cal) son aritméticamente coherentes con la transcripción actual. El residuo depende del calor del calorímetro y su interpretación sigue limitada por la incertidumbre de la calibración.
- Los errores 2.86 % y 10.59 % coinciden al utilizar temperaturas teóricas sin redondear. La sustitución impresa con 20.42 °C daría 2.84 %, diferencia de redondeo que se aclara en el texto sin alterar el resultado. El error relativo basado en Celsius depende del origen de la escala; se mantiene como indicador convencional del informe.
- El menor error central al incluir el calorímetro no demuestra una validación precisa. Los posibles efectos del ambiente y de la humedad se presentan como hipótesis, sin atribuciones causales cuantitativas no demostradas.

## Criterios de la rúbrica

| Criterio | Estado de la revisión |
| --- | --- |
| Formato y estructura (10 %) | Se conserva la plantilla IEEE y se utilizan referencias automáticas. |
| Marco teórico (15 %) | Conceptos, ecuaciones, unidades, incertidumbres e hipótesis integrados y vinculados al análisis. |
| Metodología (10 %) | Conservada; contraste directo con la guía pendiente. |
| Análisis (35 %) | Masa confirmada en 69.4 g. Hipótesis de Tₕ fijo y propagación verificadas; persiste la limitada precisión de la calibración. |
| Discusión (15 %) | Incertidumbre del calor del hielo y porcentaje coherentes con Tₕ fijo; se mantienen las limitaciones físicas de la calibración. |
| Conclusiones (10 %) | Resultados coherentes con la propagación verificada; límites y mejoras experimentales conservados. |
| Bibliografía (5 %) | Entradas de Serway y Taylor recuperadas del proyecto, con citas IEEE. |

No se asigna una nota. Las incertidumbres son estimaciones lineales condicionadas al modelo; la diferencia de temperatura de calibración sigue siendo comparable a su incertidumbre. El resumen, la introducción y los objetivos ya están completos.

## Reproducción de la verificación

Ejecutar `python3 scripts/verificar_incertidumbres.py` desde `lab4/`. El script contrasta las derivadas de temperatura con diferencias centrales y guarda los valores sin redondear en `data/incertidumbres_verificadas.json`. No modifica mediciones ni archivos LaTeX.
