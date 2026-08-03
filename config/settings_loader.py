"""Load OntoChimpWeb configuration from local or deployed settings."""

from __future__ import annotations

import os
from dataclasses import dataclass

# 8/3 added  kw_only!
@dataclass(frozen=True, kw_only=True)
class Settings:
    mysql_host: str
    mysql_port: int
    mysql_user: str
    mysql_password: str
    mysql_database: str


def _load_local_settings() -> Settings | None:
    try:
        import local_settings
    except ImportError:
        return None

    return Settings(
        mysql_host=local_settings.MYSQL_HOST,
        mysql_port=int(getattr(local_settings, "MYSQL_PORT", 3306)),
        mysql_user=local_settings.MYSQL_USER,
        mysql_password=local_settings.MYSQL_PASSWORD,
        mysql_database=local_settings.MYSQL_DATABASE,
    )


def _load_environment_settings() -> Settings:
    required = [
        "MYSQL_HOST",
        "MYSQL_PORT",
        "MYSQL_USER",
        "MYSQL_PASSWORD",
        "MYSQL_DATABASE",
    ]

    missing = [name for name in required if not os.getenv(name)]

    if missing:
        raise RuntimeError(
            "Missing required configuration: " + ", ".join(missing)
        )

    return Settings(
        mysql_host=os.environ["MYSQL_HOST"],
        mysql_port=int(os.getenv("MYSQL_PORT", "3306")),
        mysql_user=os.environ["MYSQL_USER"],
        mysql_password=os.environ["MYSQL_PASSWORD"],
        mysql_database=os.environ["MYSQL_DATABASE"],
    )


settings = _load_local_settings() or _load_environment_settings()