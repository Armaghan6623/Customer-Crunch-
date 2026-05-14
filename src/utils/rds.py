"""Placeholder RDS connection utility."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class RDSConfig:
    host: str
    port: int = 5432
    user: str = ""
    password: str = ""
    dbname: str = ""


def load_rds_config_from_env() -> RDSConfig:
    # Environment variables expected (placeholders)
    return RDSConfig(
        host=os.getenv("RDS_HOST", ""),
        port=int(os.getenv("RDS_PORT", "5432")),
        user=os.getenv("RDS_USER", ""),
        password=os.getenv("RDS_PASSWORD", ""),
        dbname=os.getenv("RDS_DBNAME", ""),
    )

