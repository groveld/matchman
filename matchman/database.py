from firebird.driver import connect, driver_config

from matchman.config import FirebirdConfig

srv_cfg = f"""[server]
host = {FirebirdConfig.host}
port = {FirebirdConfig.port}
user = {FirebirdConfig.user}
password = {FirebirdConfig.password}
"""
driver_config.register_server("server", srv_cfg)

db_cfg = f"""[database]
server = server
database = {FirebirdConfig.database}
protocol = {FirebirdConfig.protocol}
charset = {FirebirdConfig.charset}
"""
driver_config.register_database("database", db_cfg)


def get_connection():
    return connect("database")
