from __future__ import annotations

import os
from typing import Any, Union

import joblib
import pandas as pd

from src.utils.preprocess import preprocess


def _load_model(model_path: str):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Pre-trained model not found: {model_path}")
    return joblib.load(model_path)


def predict_churn(data: pd.DataFrame) -> float:
    """Predict churn probability for a batch of customers.

    Args:
        data: pandas DataFrame containing raw customer features.

    Returns:
        churn probability as a float.

    Notes:
        - Loads `churn_model.pkl` from `MODEL_PATH` (default: `src/model/churn_model.pkl`).
        - Applies preprocessing from `src/utils/preprocess.py`.
        - Supports models that expose either:
          - `predict_proba(X)` (LightGBM/XGBoost style), using positive class prob
          - or `predict(X)` (fallback)
    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame")

    model_path = os.getenv(
        "MODEL_PATH", "src/model/churn_model.pkl"
    )

    model = _load_model(model_path)

    X = preprocess(data)

    # Prefer probability if model supports it
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(X)
        # binary classification: choose probability of churn class (usually class 1)
        if proba.ndim == 2 and proba.shape[1] >= 2:
            return float(proba[0, 1])
        return float(proba[0])

    # Fallback to predict
    pred = model.predict(X)
    # If predict returns probabilities or scores, take first row
    if hasattr(pred, "__len__"):
        return float(pred[0])
    return float(pred)

