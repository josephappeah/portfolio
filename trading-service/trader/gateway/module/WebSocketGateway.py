from abc import ABC

from trader.core.constants.Constants import ConfigConstants
from trader.gateway.model.IConnectionManager import IConnectionManager
from trader.gateway.model.IConnectionSource import IConnectionSource
from trader.gateway.module.IGateway import IGateway
from trader.gateway.socket.WebSocketConnectionManager import WebSocketConnectionManager
from trader.gateway.socket.WebSocketConnectionSource import WebSocketConnectionSource
from trader.core.config.ConfigUtil import ConfigUtils


class WebSocketGateway(IGateway, ABC):
    _connectionSource: IConnectionSource = None
    _connectionManager: IConnectionManager = None
    _host: str = None
    _port: int = None

    def __init__(self):
        self._connectionManager = WebSocketConnectionManager()
        self._host: str = ConfigUtils.getConfigs().get(ConfigConstants.WebSocketServerSection).get(
            ConfigConstants.ServerHostKey)
        self._port: int = int(ConfigUtils.getConfigs().get(
            ConfigConstants.WebSocketServerSection).get(ConfigConstants.ServerPortKey))
        self._connectionSource = WebSocketConnectionSource(
            host=self._host, port=self._port, connectionManager=self._connectionManager)
        super().__init__(self._connectionSource, self._connectionManager)
