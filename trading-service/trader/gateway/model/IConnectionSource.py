from abc import ABC, abstractmethod
from trader.gateway.model.IConnectionManager import IConnectionManager


class IConnectionSource(ABC):
    _connectionManager: IConnectionManager = None

    def __init__(self, connectionManager):
        self._connectionManager = connectionManager

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def getName(self) -> str:
        pass
