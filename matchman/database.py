from firebird.driver import NetProtocol, connect, driver_config

from .config import Firebird

# Apply Firebird configuration
driver_config.server_defaults.host.value = Firebird.host
driver_config.server_defaults.port.value = Firebird.port
driver_config.server_defaults.user.value = Firebird.user
driver_config.server_defaults.password.value = Firebird.password
driver_config.db_defaults.protocol.value = NetProtocol[Firebird.protocol.upper()]
driver_config.db_defaults.charset.value = Firebird.charset.upper()


def get_connection():
    return connect(Firebird.database)
