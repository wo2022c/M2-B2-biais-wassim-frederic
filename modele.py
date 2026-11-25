"""Réentraînement de la recette v2.1 sur un choix de colonnes, et mesures par groupe."""

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import FixedThresholdClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder, StandardScaler

from features import CATEGORICAL_FEATURES, NUMERICAL_FEATURES, ajouter_variables

CIBLE = "is_canceled"
SEUIL = 0.2


def entrainer(train: pd.DataFrame, colonnes: list[str]) -> Pipeline:
    """Même recette que la v2.1, sur `colonnes`. Seules des colonnes catégorielles peuvent être retirées."""
    cat = [c for c in CATEGORICAL_FEATURES if c in colonnes]
    preparation = ColumnTransformer(
        [
            ("cat", Pipeline([
                ("impute", SimpleImputer(strategy="constant", fill_value="Unknown")),
                ("encode", OneHotEncoder(handle_unknown="infrequent_if_exist", min_frequency=50)),
            ]), cat),
            ("num", Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]),
            NUMERICAL_FEATURES),
        ],
        sparse_threshold=0,
    )
    modele = Pipeline([
        ("variables", FunctionTransformer(ajouter_variables)),
        ("preprocessing", preparation),
        ("classifier", FixedThresholdClassifier(
            LogisticRegression(C=1.0, max_iter=2000), threshold=SEUIL, response_method="predict_proba")),
    ])
    return modele.fit(train[colonnes], train[CIBLE])


def mesures_par_groupe(modele, donnees: pd.DataFrame, colonnes: list[str], groupe: pd.Series) -> pd.DataFrame:
    """Une ligne par groupe : effectif, taux réel d'annulation, taux d'alertes, rappel, fausses alertes, précision."""
    pred = pd.Series(modele.predict(donnees[colonnes]), index=donnees.index)
    reel = donnees[CIBLE]
    lignes = {}
    for nom in groupe.unique():
        k = groupe == nom
        p, y = pred[k], reel[k]
        lignes[nom] = {
            "effectif": int(k.sum()),
            "annulations_reelles": y.mean(),
            "taux_alertes": p.mean(),
            "rappel": p[y == 1].mean(),
            "fausses_alertes": p[y == 0].mean(),
            "precision": y[p == 1].mean(),
        }
    return pd.DataFrame(lignes).T.round(3)
