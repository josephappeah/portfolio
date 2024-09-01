from trader.gateway.model.IConnectionManager import IConnectionManager
from trader.gateway.model.IConnectionSource import IConnectionSource
from abc import ABC
import logging


class IGateway(ABC):
    Logger = logging.getLogger(__name__)
    _connectionSource: IConnectionSource = None
    _connectionManager: IConnectionManager = None

    def __init__(self, connectionSource, connectionManager):
        self._connectionSource, self._connectionManager = connectionSource, connectionManager

    def start(self):
        # only trying so we can log the exception
        try:
            self._connectionSource.start()
        except Exception as e:
            self.Logger.error("Failed to start Connection Source: {%s}", self._connectionSource.getName(), e)

    def getConnectionManager(self) -> IConnectionManager:
        return self._connectionManager
