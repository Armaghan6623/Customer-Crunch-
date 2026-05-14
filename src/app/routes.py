from __future__ import annotations

from flask import Blueprint, jsonify, request

from src.app.database import get_customer_data
from src.model.predictor import predict_churn

routes_bp = Blueprint("routes", __name__)


@routes_bp.get("/health")
def health():
    return jsonify({"status": "ok"})


@routes_bp.post("/predict")
def predict():
    """Inference endpoint.

    Expected JSON payload:
      {"customer_id": 123}

    Returns:
      {
        "customer_id": 123,
        "churn_probability": 0.42,
        "churn": false
      }
    """

    payload = request.get_json(silent=True) or {}
    customer_id = payload.get("customer_id")
    if customer_id is None:
        return jsonify({"error": "Missing 'customer_id' in request body."}), 400

    try:
        data = get_customer_data(int(customer_id))
    except KeyError:
        return jsonify({"error": f"Customer not found: customer_id={customer_id}"}), 404
    except Exception as e:
        return jsonify({"error": "Database error", "details": str(e)}), 500

    try:
        # predictor expects a DataFrame
        import pandas as pd

        df = pd.DataFrame([data])
        churn_probability = float(predict_churn(df))
        churn = churn_probability >= 0.5

    except Exception as e:
        return jsonify({"error": "Prediction error", "details": str(e)}), 500

    return jsonify(
        {
            "customer_id": int(customer_id),
            "churn_probability": churn_probability,
            "churn": churn,
        }
    )

