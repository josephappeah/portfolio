from abc import ABC, abstractmethod
from typing import Optional
from trader.gateway.model.IDataDestination import IDataDestination
from trader.gateway.model.IDataSource import IDataSource


class IConnection(ABC):
    """
        Represents a Many-To-Many connection. This Interface holds/facilitates the relationship between
        Sources and Destinations.
        Sends source out with the Destination. Receives source with the Source
    """
    _connectionKey: Optional[str] = None
    _dataDestination: IDataDestination = None
    _dataSource: IDataSource = None
    _connectionName: Optional[str] = None

    def __init__(self, dataSource: IDataSource, dataDestination: IDataDestination):
        self._dataDestination, self._dataSource = dataDestination, dataSource

    @abstractmethod
    async def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def isOpen(self) -> bool:
        pass

    def setConnectionKey(self, connectionKey: str):
        if not self._connectionKey:
            self._connectionKey = connectionKey

    def setConnectionName(self, connectionName: str):
        if not self._connectionName:
            self._connectionName = connectionName

    def getConnectionKey(self) -> Optional[str]:
        return self._connectionKey

    def getConnectionName(self) -> Optional[str]:
        return self._connectionName

    def getDataSource(self) -> IDataSource:
        return self._dataSource

    def getDataDestination(self) -> IDataDestination:
        return self._dataDestination
