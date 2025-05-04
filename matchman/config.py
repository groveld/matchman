"""Flask Configuration."""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration class."""


class FirebirdConfig:
    """Configuration for Firebird database connection."""

    host: str = os.getenv("FIREBIRD_HOST", "172.25.10.10")
    port: str = os.getenv("FIREBIRD_PORT", "3050")
    user: str = os.getenv("FIREBIRD_USER", "SYSDBA")
    password: str = os.getenv("FIREBIRD_PASSWORD", "FirebirdRootPassword")
    database: str = os.getenv("FIREBIRD_DATABASE", "/var/lib/firebird/data/svduel.fdb")
    protocol: str = os.getenv("FIREBIRD_PROTOCOL", "INET")
    charset: str = os.getenv("FIREBIRD_CHARSET", "UTF8")
