"""
rf_utils.py
===========
Funciones de apoyo para la clase y el laboratorio «Bosques Aleatorios (Random Forests)»
— Computación Inteligente, Universidad de los Llanos.

Convenciones compartidas con los materiales de Diseño de Experimentos y Reducción de Dimensionalidad:
* SEMILLA = 42.
* Breast Cancer Wisconsin se recodifica para que la clase positiva (1) sea «maligno».
* Los modelos que dependen de distancias o productos internos (LogReg, K-NN, SVM) se escalan dentro de un
  Pipeline; los árboles y Random Forest NO necesitan escalamiento.

Dependencias: numpy, pandas, scikit-learn (≥ 1.2).
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer, load_wine, make_moons, make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

SEMILLA = 42


# ---------------------------------------------------------------------------
# Datos reales
# ---------------------------------------------------------------------------
def cargar_datos(nombre: str = "breast_cancer"):
    """Retorna (X: DataFrame, y: Series, clases: list[str])."""
    if nombre == "breast_cancer":
        d = load_breast_cancer(as_frame=True)
        return d.data, (d.target == 0).astype(int).rename("maligno"), ["benigno", "maligno"]
    if nombre == "wine":
        d = load_wine(as_frame=True)
        return d.data, d.target.rename("cultivar"), [f"cultivar_{c}" for c in d.target_names]
    raise ValueError("nombre debe ser 'breast_cancer' o 'wine'")


# ---------------------------------------------------------------------------
# Datos sintéticos controlados
# ---------------------------------------------------------------------------
def datos_lunas(n: int = 500, ruido: float = 0.30, semilla: int = SEMILLA):
    """Dos «lunas» en 2D: frontera no lineal, ideal para visualizar fronteras de decisión."""
    X, y = make_moons(n_samples=n, noise=ruido, random_state=semilla)
    return pd.DataFrame(X, columns=["x1", "x2"]), pd.Series(y, name="clase")


def datos_lineales(n: int = 300, d: int = 20, semilla: int = SEMILLA):
    """Frontera LINEAL con muchas variables informativas y pocas observaciones:
    escenario favorable a modelos lineales (LogReg, SVM lineal)."""
    rng = np.random.default_rng(semilla)
    X = rng.normal(size=(n, d))
    w = rng.normal(size=d)
    y = (X @ w + 0.5 * rng.normal(size=n) > 0).astype(int)
    return pd.DataFrame(X, columns=[f"x{i}" for i in range(d)]), pd.Series(y, name="clase")


def datos_interaccion(n: int = 600, d_ruido: int = 8, semilla: int = SEMILLA):
    """Clase definida por una INTERACCIÓN tipo XOR entre x1 y x2 (sin efecto marginal), más ruido:
    escenario favorable a árboles y bosques, difícil para modelos lineales."""
    rng = np.random.default_rng(semilla)
    x1, x2 = rng.uniform(-1, 1, n), rng.uniform(-1, 1, n)
    y = ((x1 * x2) > 0).astype(int)
    voltear = rng.random(n) < 0.05                         # 5 % de etiquetas ruidosas
    y[voltear] = 1 - y[voltear]
    X = np.column_stack([x1, x2, rng.normal(size=(n, d_ruido))])
    return pd.DataFrame(X, columns=["x1", "x2"] + [f"ruido_{i}" for i in range(d_ruido)]), pd.Series(y, name="clase")


def datos_cardinalidad(n: int = 1000, semilla: int = SEMILLA):
    """Ejemplo controlado del SESGO DE CARDINALIDAD de la importancia MDI (cf. Strobl et al., 2007).
    Sólo 'senal_binaria' y 'senal_continua' influyen en la clase; las variables 'ruido_*' son
    independientes de y y tienen cardinalidad creciente (2, 4, 20 y ~n valores distintos)."""
    rng = np.random.default_rng(semilla)
    senal_bin = rng.integers(0, 2, n)
    senal_cont = rng.normal(size=n)
    logit = 1.5 * senal_bin + 1.0 * senal_cont - 0.75
    y = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)
    X = pd.DataFrame({
        "senal_binaria": senal_bin,
        "senal_continua": senal_cont,
        "ruido_binario": rng.integers(0, 2, n),
        "ruido_4_categorias": rng.integers(0, 4, n),
        "ruido_20_categorias": rng.integers(0, 20, n),
        "ruido_continuo": rng.normal(size=n),
    })
    return X, pd.Series(y, name="clase")


def agregar_copia_correlacionada(X: pd.DataFrame, columna: str, ruido: float = 0.05,
                                 semilla: int = SEMILLA) -> pd.DataFrame:
    """Añade una copia casi idéntica (correlación ≈ 1) de una columna para estudiar
    cómo se reparte la importancia entre variables correlacionadas."""
    rng = np.random.default_rng(semilla)
    X = X.copy()
    X[columna + "_copia"] = X[columna] + ruido * X[columna].std() * rng.normal(size=len(X))
    return X


# ---------------------------------------------------------------------------
# Modelos
# ---------------------------------------------------------------------------
def modelos_comparacion(semilla: int = SEMILLA, cv_interna: int = 3, n_arboles: int = 200) -> dict:
    """Los cinco clasificadores con un ajuste RAZONABLE y pequeño de hiperparámetros
    (GridSearchCV interno). Escalamiento sólo donde hace falta."""
    cv = StratifiedKFold(cv_interna, shuffle=True, random_state=semilla)
    esc = lambda clf: Pipeline([("escalar", StandardScaler()), ("clf", clf)])
    return {
        "Random Forest": GridSearchCV(
            Pipeline([("clf", RandomForestClassifier(n_estimators=n_arboles, random_state=semilla))]),
            {"clf__max_features": ["sqrt", 0.5], "clf__min_samples_leaf": [1, 5]}, cv=cv),
        "Árbol": GridSearchCV(Pipeline([("clf", DecisionTreeClassifier(random_state=semilla))]),
                              {"clf__max_depth": [3, 5, None], "clf__min_samples_leaf": [1, 5]}, cv=cv),
        "LogReg": GridSearchCV(esc(LogisticRegression(max_iter=5000)), {"clf__C": [0.01, 0.1, 1, 10]}, cv=cv),
        "K-NN": GridSearchCV(esc(KNeighborsClassifier()), {"clf__n_neighbors": [3, 7, 15]}, cv=cv),
        "SVM": GridSearchCV(esc(SVC(random_state=semilla)),
                            {"clf__C": [0.1, 1, 10], "clf__gamma": ["scale", 0.01]}, cv=cv),
    }


def complejidad_bosque(rf: RandomForestClassifier) -> dict:
    """Profundidad media, hojas medias y nodos totales de un bosque ajustado."""
    prof = [e.get_depth() for e in rf.estimators_]
    hojas = [e.get_n_leaves() for e in rf.estimators_]
    nodos = [e.tree_.node_count for e in rf.estimators_]
    return {"profundidad_media": float(np.mean(prof)), "hojas_media": float(np.mean(hojas)),
            "nodos_totales": int(np.sum(nodos))}


def correlacion_media_arboles(rf: RandomForestClassifier, X) -> float:
    """Correlación media de Pearson entre las probabilidades predichas (clase 1) por pares de árboles:
    mide la (falta de) diversidad del bosque."""
    X = np.asarray(X, dtype=np.float32)
    P = np.array([e.predict_proba(X)[:, 1] for e in rf.estimators_])
    C = np.corrcoef(P)
    n = C.shape[0]
    return float((np.nansum(C) - n) / (n * (n - 1)))
