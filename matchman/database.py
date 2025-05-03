from firebird.driver import connect, driver_config

# Register Firebird server
srv_cfg = """[docker]
host = 172.25.10.10
user = SYSDBA
password = FirebirdRootPassword
"""
driver_config.register_server("docker", srv_cfg)

# Register database
db_cfg = """[matchmanager]
server = docker
database = /var/lib/firebird/data/svduel.fdb
protocol = inet
charset = utf8
"""
driver_config.register_database("matchmanager", db_cfg)


def get_connection():
    return connect("matchmanager")
