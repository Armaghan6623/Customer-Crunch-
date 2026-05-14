from __future__ import annotations

import pandas as pd


def preprocess(data: pd.DataFrame) -> pd.DataFrame:
    """Preprocess raw customer features.

    This is a placeholder implementation.

    Expected input columns (for this project):
      - CreditScore
      - Age
      - Balance
      - Geography

    Replace this logic with your actual training-time preprocessing:
    - encoding Geography
    - scaling/normalization
    - column ordering
    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame")

    cols = ["CreditScore", "Age", "Balance", "Geography"]
    missing = [c for c in cols if c not in data.columns]
    if missing:
        raise KeyError(f"Missing required columns: {missing}")

    # Placeholder: return selected columns; real preprocessing should be applied.
    return data[cols].copy()

