class Firebird:
    """Firebird database configuration class."""

    host: str = "172.25.10.10"
    port: str = "3050"
    user: str = "SYSDBA"
    password: str = "FirebirdRootPassword"
    database: str = "/var/lib/firebird/data/svduel.fdb"
    protocol: str = "INET"
    charset: str = "UTF8"
