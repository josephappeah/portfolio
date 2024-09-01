from abc import ABC, abstractmethod
from typing import Optional, List
from trader.core.constants.Constants import ConfigConstants
from trader.gateway.model.IConnection import IConnection
from trader.core.config.ConfigUtil import ConfigUtils
import logging


class IConnectionManager(ABC):
    Logger = logging.getLogger(__name__)
    _defaultConnectionPrefix: str = "Connections:"
    _connectionNameToConnection: dict[str:IConnection] = None
    _connectionKeyToConnectionNames: dict[str:set[str]] = None

    def __init__(self):
        self._connectionNameToConnection, self._connectionKeyToConnectionNames = {}, {}

    def cleanUpConnections(self):
        for name, connection in self._connectionNameToConnection.items():
            if not connection.isOpen():
                connectionKey = connection.getConnectionKey()
                del self._connectionNameToConnection[name]
                self._connectionKeyToConnectionNames[connectionKey].remove(name)
                connection.getDataSource().unSubscribeFromSource()

    def cleanUpConnection(self, connectionName: str):
        if connectionName and connectionName in self._connectionNameToConnection:
            connection: IConnection = self._connectionNameToConnection[connectionName]
            if not connection.isOpen():
                connectionKey = connection.getConnectionKey()
                del self._connectionNameToConnection[connectionName]
                self._connectionKeyToConnectionNames[connectionKey].remove(connectionName)
                connection.getDataSource().unSubscribeFromSource()

    def getConnectionPrefix(self):
        connectionPrefix: Optional[str] = ConfigUtils.getConfig(
            ConfigConstants.ConnectionSection, ConfigConstants.ConnectionNamePrefixKey)
        return connectionPrefix if connectionPrefix else self._defaultConnectionPrefix

    def removeConnection(self, connectionKey: str):
        self.Logger.debug("Removed Connection: {%s}", connectionKey)
        if connectionKey in self._connectionNameToConnection:
            del self._connectionNameToConnection[connectionKey]

    def getConnections(self) -> dict[str:IConnection]:
        return self._connectionNameToConnection

    def getConnectionsByOrigin(self, origin: str) -> Optional[List[IConnection]]:
        if origin not in self._connectionKeyToConnectionNames:
            return None
        connections: List[IConnection] = []
        for connectionName in self._connectionKeyToConnectionNames[origin]:
            if connectionName in self._connectionNameToConnection:
                connections.append(self._connectionNameToConnection[connectionName])
        return connections

    def hasExceededMaxAllowedConnections(self, origin: str) -> bool:
        if origin not in self._connectionKeyToConnectionNames:
            return False
        maxAllowedConnections: int = int(ConfigUtils.getConfig(
            ConfigConstants.ConnectionSection, ConfigConstants.MaxAllowedConnections))
        return len(self._connectionKeyToConnectionNames[origin]) > maxAllowedConnections

    @abstractmethod
    def getConnectionName(self) -> str:
        pass

    @abstractmethod
    def addConnection(self, connection: IConnection) -> Optional[str]:
        if connection:
            connectionName = self.getConnectionName()
            self._connectionNameToConnection[connectionName] = connection
            connectionNamesForConnectionKey: set[str] = self._connectionKeyToConnectionNames.get(
                connection.getConnectionKey(), set())
            connectionNamesForConnectionKey.add(connectionName)
            self._connectionKeyToConnectionNames[connection.getConnectionKey()] = connectionNamesForConnectionKey
            self.Logger.debug("Added New Connection: {%s}, Key:{%s}", connectionName, connection.getConnectionKey())
            return connectionName

