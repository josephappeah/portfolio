from abc import ABC
from typing import Optional

from trader.core.constants.Constants import ConfigConstants
from trader.gateway.model.IConnectionManager import IConnectionManager
from trader.gateway.socket.WebSocketConnection import WebSocketConnection
import logging
from trader.core.config.ConfigUtil import ConfigUtils


class WebSocketConnectionManager(IConnectionManager, ABC):
    Logger = logging.getLogger(__name__)
    _defaultWSConnectionPrefix: str = "WSConnection:"

    def __init__(self):
        super().__init__()

    def addConnection(self, connection: WebSocketConnection) -> Optional[str]:
        return super().addConnection(connection)

    def getConnectionName(self) -> str:
        wsConnectionPrefix: Optional[str] = ConfigUtils.getConfig(
            ConfigConstants.WebSocketsSection, ConfigConstants.WebSocketConnectionNamePrefix)
        wsConnectionPrefix = wsConnectionPrefix if wsConnectionPrefix else self._defaultWSConnectionPrefix
        return super().getConnectionPrefix() + wsConnectionPrefix + str(len(self._connectionNameToConnection))
