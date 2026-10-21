# Evidencia del experimento — Práctica 07 (generada automáticamente; no editar)

## Configuración
```json
{
  "entorno": {
    "python": "3.14.5",
    "sklearn": "1.9.1",
    "numpy": "2.5.4",
    "plataforma": "Windows-11-10.0.26100-SP0",
    "cpu": 4,
    "modo_ligero": false,
    "semilla": 42,
    "n_arboles": 300
  },
  "datos": "Breast Cancer Wisconsin (Diagnostic), scikit-learn; 1 = maligno",
  "particion": "75/25 estratificada, semilla 42",
  "cv": "StratifiedKFold(5, shuffle=True, 42) en entrenamiento",
  "cv_comparacion": "RepeatedStratifiedKFold(5, 2) externa + GridSearchCV interno de 3 pliegues",
  "metrica_seleccion": "f1",
  "busqueda": "RandomizedSearchCV n_iter=20, tiempo 78.0 s",
  "mejores_parametros": {
    "criterion": "entropy",
    "max_depth": "5",
    "max_features": "log2",
    "max_samples": "0.5",
    "min_samples_leaf": "2"
  },
  "permutacion": "conjunto de prueba (143 casos), n_repeats=20",
  "umbral_agrupamiento": 0.7,
  "complejidad_modelo_final": {
    "profundidad_media": 4.846666666666667,
    "hojas_media": 10.076666666666666,
    "nodos_totales": 5746
  }
}
```

### Tabla A. Árbol vs. Random Forest (CV 5-fold en entrenamiento)

```
               accuracy CV  precision CV  recall CV  f1 CV  roc_auc CV  accuracy de  f1 de  accuracy entren.  t_ajuste (s)
modelo                                                                                                                    
Árbol                0.915         0.883      0.900  0.889       0.912        0.033  0.038               1.0         0.009
Random Forest        0.962         0.962      0.937  0.949       0.988        0.021  0.029               1.0         0.658
```

### Tabla B. Estabilidad ante submuestras (10 re-entrenamientos; accuracy en prueba)

```
               accuracy media     de  % predicciones inestables
Árbol                   0.934  0.014                     20.280
Random Forest           0.969  0.007                      2.797
```

### Tabla C. Base vs. ajustado (F1 CV; el ajustado es optimista)

```
                                            F1 CV  de CV
Base (por defecto)                          0.949  0.029
Ajustado (mejor de la búsqueda; optimista)  0.946  0.026
```

### Tabla D. Comparación de clasificadores (CV anidada; medias)

```
               accuracy  precision  recall     f1  roc_auc  de accuracy  t_ajuste (s)
modelo                                                                               
Random Forest     0.956      0.949   0.934  0.941    0.990        0.017        17.499
Árbol             0.923      0.898   0.896  0.895    0.923        0.027         0.408
LogReg            0.975      0.986   0.946  0.965    0.995        0.013         0.368
K-NN              0.968      0.986   0.927  0.955    0.985        0.015         0.239
SVM               0.975      0.976   0.955  0.965    0.995        0.016         0.503
```

### Tabla E. Importancias: MDI y permutación (top 10 por MDI)

```
                        MDI  perm_prueba_accuracy  de_acc  perm_prueba_auc  perm_entrenamiento_acc
worst area            0.127                 0.011   0.008        4.400e-03               2.200e-03
worst perimeter       0.121                 0.009   0.009        2.900e-03               2.000e-04
worst concave points  0.096                 0.009   0.007        3.300e-03               3.800e-03
mean concave points   0.076                 0.004   0.008        9.000e-04               2.800e-03
worst radius          0.074                 0.001   0.008        1.600e-03              -8.000e-04
mean perimeter        0.061                 0.002   0.005        2.000e-04              -2.000e-04
mean area             0.060                -0.000   0.008        5.000e-04              -7.000e-04
mean radius           0.057                 0.001   0.005       -0.000e+00              -1.100e-03
mean concavity        0.046                 0.009   0.004        1.000e-04               2.700e-03
area error            0.041                 0.004   0.004        2.000e-04               6.000e-04
```

### Tabla F. Permutación con una variable por grupo de correlación

```
                        perm_prueba     de  tamaño del grupo
mean radius                   0.169  0.035                 6
mean compactness              0.037  0.014                 9
mean texture                  0.026  0.014                 2
mean smoothness               0.023  0.010                 2
mean symmetry                 0.013  0.008                 2
texture error                 0.011  0.008                 3
radius error                  0.010  0.008                 3
mean fractal dimension        0.003  0.003                 3
```

### Tabla G. Experimento de cardinalidad (sintético)

```
                     valores distintos    MDI  perm_prueba
senal_binaria                        2  0.130    7.650e-02
senal_continua                    1000  0.358    1.190e-01
ruido_binario                        2  0.028   -5.300e-03
ruido_4_categorias                   4  0.070    5.000e-04
ruido_20_categorias                 20  0.165   -2.700e-03
ruido_continuo                    1000  0.249   -2.800e-03
```

### Tabla H. Experimento de copia correlacionada

```
                    MDI  perm_prueba
worst area        0.093        0.005
worst area_copia  0.097        0.006
```

### Figuras
- fig_matrices_arbol_bosque.png
- fig_sensibilidad.png
- fig_comparacion.png
