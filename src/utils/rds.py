"""RDS connection utility.

This file is optional; the app currently uses `src/app/database.py` directly.
Kept here so infrastructure/pipeline logic has a single place to evolve.
"""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class RDSConfig:
    host: str
    port: int = 5432
    dbname: str = ""
    user: str = ""
    password: str = ""


def load_rds_config_from_env() -> RDSConfig:
    return RDSConfig(
        host=os.getenv("RDS_HOST", ""),
        port=int(os.getenv("RDS_PORT", "5432")),
        dbname=os.getenv("RDS_DBNAME", ""),
        user=os.getenv("RDS_USER", ""),
        password=os.getenv("RDS_PASSWORD", ""),
    )


