from __future__ import annotations

import os
from typing import Any, Dict, Optional

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine


def _build_engine() -> Engine:
    """Create a SQLAlchemy engine for Amazon RDS (PostgreSQL).

    Environment variables expected:
      - RDS_HOST
      - RDS_PORT (optional, default 5432)
      - RDS_DBNAME
      - RDS_USER
      - RDS_PASSWORD
    """

    host = os.getenv("RDS_HOST")
    port = os.getenv("RDS_PORT", "5432")
    dbname = os.getenv("RDS_DBNAME")
    user = os.getenv("RDS_USER")
    password = os.getenv("RDS_PASSWORD")

    if not all([host, dbname, user, password]):
        missing = [
            k
            for k, v in {
                "RDS_HOST": host,
                "RDS_DBNAME": dbname,
                "RDS_USER": user,
                "RDS_PASSWORD": password,
            }.items()
            if not v
        ]
        raise RuntimeError(
            "Missing required environment variables for RDS: " + ", ".join(missing)
        )

    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
    return create_engine(url, pool_pre_ping=True, pool_recycle=3600)


def get_customer_data(customer_id: int) -> Dict[str, Any]:
    """Fetch customer features for a given customer_id.

    If `LOCAL_TEST=True` is set, returns a hardcoded mock record instead of
    connecting to RDS.

    Reads from table `customers` and returns a dict with features:
      - CreditScore
      - Age
      - Balance
      - Geography

    Raises:
      - KeyError if customer_id is not found
      - RuntimeError if DB env vars are missing (when not in mock mode)
    """

    if os.getenv("LOCAL_TEST", "False").lower() in {"1", "true", "yes", "y"}:
        # Deterministic mock output for local testing
        return {
            "CreditScore": 600,
            "Age": 30,
            "Balance": 1000,
            "Geography": "France",
            "customer_id": customer_id,
        }

    engine = _build_engine()

    query = text(
        """
        SELECT
          "CreditScore",
          "Age",
          "Balance",
          "Geography"
        FROM customers
        WHERE customer_id = :customer_id
        LIMIT 1
        """
    )

    with engine.connect() as conn:
        row = conn.execute(query, {"customer_id": customer_id}).mappings().first()

    if row is None:
        raise KeyError(f"Customer not found for customer_id={customer_id}")

    # Convert SQLAlchemy RowMapping to a plain dict
    return dict(row)


