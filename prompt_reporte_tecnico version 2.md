# Prompt reutilizable · Reporte técnico de la Práctica 07 (Random Forests)

**Uso:** copie el bloque «PROMPT», complete lo que está entre `<< >>` y pegue al final el archivo
`resultados_lab07/evidencia_experimento.md` generado por `Lab07_Random_Forest.ipynb`, junto con las respuestas (A)
de su grupo. Si la herramienta lo permite, adjunte también las figuras PNG.

> La IA es una herramienta de **asistencia**: no reemplaza el análisis experimental ni la responsabilidad académica
> de los autores. Declare su uso en el reporte.

---

## PROMPT (versión 1)

```text
ROL
Actúa como coautor técnico de un reporte de Machine Learning con estilo de artículo científico corto, en español
académico claro, preciso y objetivo (términos técnicos en inglés entre paréntesis la primera vez).

CONTEXTO
Somos estudiantes de Ingeniería de Sistemas (Computación Inteligente, Universidad de los Llanos). Evaluamos un
Random Forest (RandomForestClassifier de scikit-learn) en Breast Cancer Wisconsin (Diagnostic) (clase positiva =
maligno), lo comparamos con un árbol de decisión, Logistic Regression, K-NN y SVM, ajustamos hiperparámetros con
validación cruzada y analizamos la importancia de características por MDI y por permutación, incluyendo dos
experimentos sintéticos (cardinalidad y copia correlacionada). Autores: <<nombres>>. Fecha: <<fecha>>.

EVIDENCIA (ÚNICA FUENTE PERMITIDA)
Al final está "evidencia_experimento.md" (configuración, entorno, hiperparámetros y tablas A–H) y nuestras
respuestas de análisis. 
Figuras disponibles: fig_comparacion.png, fig_matrices_arbol_bosque.png, fig_sensibilidad.png.
Tablas CSV en resultados_lab07

TAREA
Redacta un borrador con EXACTAMENTE estas secciones:
1. Título  2. Resumen (máx. 200 palabras)  3. Palabras clave (4–6)  4. Introducción
5. Descripción del conjunto de datos  6. Metodología y diseño experimental
7. Configuración de Random Forest y de los modelos de referencia  8. Protocolo de ajuste y validación
9. Métricas de desempeño  10. Resultados y visualizaciones  11. Análisis de importancia de características
12. Discusión  13. Limitaciones y amenazas a la validez  14. Conclusiones  15. Referencias verificables

REGLAS OBLIGATORIAS
R1. Usa EXCLUSIVAMENTE los números de la evidencia, con los mismos decimales. No inventes métricas,
    experimentos, conjuntos de datos, hiperparámetros, figuras ni tablas.
R2. Indica la fuente de cada número entre corchetes, p. ej. [Tabla D] o [configuración].
R3. Separa OBSERVACIONES (lo medido) de INTERPRETACIONES ("esto sugiere", "una posible explicación es").
R4. Describe los hiperparámetros (número de árboles, max_features, max_depth, min_samples_leaf, etc.), la
    partición, la validación cruzada, la semilla, la métrica de selección y el uso único del conjunto de prueba.
R5. Explica la diferencia entre MDI (disminución de impureza, calculada en entrenamiento, sesgada hacia variables
    con muchos valores) y la importancia por permutación (caída de la métrica en el conjunto de prueba, depende de
    la métrica y se diluye con variables correlacionadas). Indica conjunto, métrica y repeticiones.
R6. No interpretes la importancia como causalidad. Una importancia alta no implica causa; una baja no implica que la
    variable sea inútil (puede tener sustitutos correlacionados).
R7. No afirmes superioridad ni significancia estadística: la evidencia no incluye pruebas estadísticas. Compara las
    diferencias con la desviación entre pliegues y dilo explícitamente. El valor "ajustado" de la Tabla C es optimista.
R8. Incluye limitaciones: un solo conjunto real, tamaño de muestra, espacios de búsqueda pequeños, una sola partición
    de prueba, variables correlacionadas, entorno de cómputo, ausencia de pruebas estadísticas.
R9. Si falta un dato, escribe [DATO FALTANTE: ...]; si una conclusión no puede justificarse, [NO JUSTIFICABLE: ...].
R10. Tablas y figuras con título numerado, métrica y escala (proporción en [0, 1]) y leyenda; refiérelas en el texto.
     Para figuras, escribe sólo el pie y el nombre del archivo.
R11. Mantén consistencia: cada afirmación de Discusión y Conclusiones debe apoyarse en un resultado de las
     secciones 10 u 11.
R12. Usa ÚNICAMENTE estas referencias; si crees que falta una, escribe [REFERENCIA SUGERIDA – VERIFICAR] sin
     inventar autores, años ni DOI:
     - Breiman, L. (2001). Random forests. Machine Learning, 45(1), 5–32. https://doi.org/10.1023/A:1010933404324
     - Breiman, L. (1996). Bagging predictors. Machine Learning, 24(2), 123–140. https://doi.org/10.1007/BF00058655
     - Ho, T. K. (1995). Random decision forests. Proceedings of the 3rd ICDAR, 1, 278–282.
       https://doi.org/10.1109/ICDAR.1995.598994
     - Strobl, C., Boulesteix, A.-L., Zeileis, A., & Hothorn, T. (2007). Bias in random forest variable importance
       measures. BMC Bioinformatics, 8, 25. https://doi.org/10.1186/1471-2105-8-25
     - Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. JMLR, 12, 2825–2830.
     - <<otras referencias que el grupo haya leído y verificado>>

FORMATO DE SALIDA
Markdown con encabezados numerados. Al final agrega "Lista de verificación para los autores" con: (a) cada
afirmación cuantitativa y su fuente; (b) todos los [DATO FALTANTE] y [NO JUSTIFICABLE]; (c) las frases
interpretativas que los autores deben revisar.

<<pegue aquí evidencia_experimento.md y las respuestas (A)>>
```

---

## Guía breve para mejorar el prompt de forma iterativa

Registre cada versión (v1, v2, v3…), el cambio realizado y el efecto observado.

1. **Números ajenos a la evidencia** → refuerce R1 y pida listar primero las tablas que usará.
2. **Lenguaje causal** («la textura causa…», «determina») → cite R6 y pida reescribir como «el modelo depende de…».
3. **MDI y permutación tratadas como equivalentes** → cite R5 y pida una tabla comparativa con sus diferencias.
4. **«Random Forest es superior»** sin prueba → cite R7 y pida comparar con la desviación entre pliegues.
5. **Hiperparámetros omitidos o inventados** → pida copiar literalmente los de [configuración].
6. **Discusión genérica** → proporcione sus respuestas (A) y pida construir la discusión sólo con ellas.
7. **Referencias desconocidas** → elimínelas, refuerce R12 y verifique cada una (DOI o catálogo de la biblioteca).
8. **Autocrítica** → «Revisa tu borrador contra R1–R12 y lista cada incumplimiento con la frase exacta».

## Tabla de verificación (inclúyala en el reporte final)

| # | Afirmación del borrador (cita textual) | Fuente (tabla, celda, figura) | Tipo (cuantitativa / interpretativa / referencia) | Estado (correcta / corregida / eliminada) | Corrección |
|---|---|---|---|---|---|
| 1 | | | | | |
| … | | | | | |

Verifique **todas** las afirmaciones cuantitativas, **todas** las referencias y al menos **cinco** interpretaciones,
incluidas todas las frases sobre importancia de características.

## Declaración de uso de IA

> Herramienta y versión: ______. Fecha: ______. Uso: redacción de un borrador a partir de la evidencia generada por
> los autores. Todas las cifras, referencias e interpretaciones fueron verificadas y corregidas por los autores, que
> asumen la responsabilidad del contenido.
