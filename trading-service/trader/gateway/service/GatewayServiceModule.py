from trader.core.model.Data import Message
from trader.gateway.model.IConnection import IConnection
from trader.gateway.model.IConnectionManager import IConnectionManager
from typing import Any, List, Optional
import logging
from trader.gateway.source.GatewayDataSourceManager import GatewayDataSourceManager
from trader.core.api.ApiHelper import ApiResponseGenerator, ApiResponseMessage


class GatewayServiceModule:
    _connectionManager: IConnectionManager = None
    _dataSourceManager: GatewayDataSourceManager = None
    Logger = logging.getLogger(__name__)

    def __init__(self, connectionManager: IConnectionManager):
        self._connectionManager = connectionManager
        self._dataSourceManager = GatewayDataSourceManager()

    def handleGetActiveConnections(self):
        if not self._connectionManager:
            self.Logger.error("Connection Manager Is Not Initialized")
            return ApiResponseGenerator.InternalServerErrorResponse(None, ApiResponseMessage.GeneralServerError.value)
        connectionNames: List[str] = self._connectionManager.getConnections().keys()
        return ApiResponseGenerator.successfulRequestResponse(None, list(connectionNames))

    def handleRequestForQuote(self, message: Message) -> Any:
        if not self._dataSourceManager.hasAsset(message.getQuote().getAssetName()):
            return ApiResponseGenerator.BadRequestResponse(message, ApiResponseMessage.AssetUnavailable.value)
        if not self._connectionManager:
            self.Logger.error("Connection Manager Is Not Initialized")
            return ApiResponseGenerator.InternalServerErrorResponse(
                message, ApiResponseMessage.GeneralServerError.value)
        if self._connectionManager.hasExceededMaxAllowedConnections(message.getUser().getOrigin()):
            return ApiResponseGenerator.BadRequestResponse(
                message, ApiResponseMessage.MaxConnectionsExceededError.value)

        connections: Optional[List[IConnection]] = self._connectionManager.getConnectionsByOrigin(
            message.getUser().getOrigin())
        if not connections:
            return ApiResponseGenerator.BadRequestResponse(
                message, ApiResponseMessage.NoActiveConnectionsForRequestor.value)
        for connection in connections:
            self._dataSourceManager.subscribe(message.getQuote().getAssetName(), connection.getDataSource())
        return ApiResponseGenerator.successfulRequestResponse(message, ApiResponseMessage.RFQRequestCompleted.value)

    def handleUnRequestForQuote(self, message: Message) -> Any:
        if not self._dataSourceManager.hasAsset(message.getQuote().getAssetName()):
            return ApiResponseGenerator.BadRequestResponse(message, ApiResponseMessage.AssetUnavailable.value)
        if not self._connectionManager:
            self.Logger.error("Connection Manager Is Not Initialized")
            return ApiResponseGenerator.InternalServerErrorResponse(
                message, ApiResponseMessage.GeneralServerError.value)
        connections: Optional[List[IConnection]] = self._connectionManager.getConnectionsByOrigin(
            message.getUser().getOrigin())
        if not connections:
            return ApiResponseGenerator.BadRequestResponse(
                message, ApiResponseMessage.NoActiveConnectionsForRequestor.value)
        for connection in connections:
            self._dataSourceManager.unSubscribe(message.getQuote().getAssetName(), connection.getDataSource())
        return ApiResponseGenerator.successfulRequestResponse(message, ApiResponseMessage.UnRFQRequestCompleted.value)

    def handleGetActiveConnectionsForHost(self, message: Message):
        if not self._connectionManager:
            self.Logger.error("Connection Manager Is Not Initialized")
            return ApiResponseGenerator.InternalServerErrorResponse(
                message, ApiResponseMessage.GeneralServerError.value)
        connections: Optional[List[IConnection]] = self._connectionManager.getConnectionsByOrigin(
            message.getUser().getOrigin())
        connectionNames: List[str] = [connection.getConnectionName() for connection in connections]
        return ApiResponseGenerator.successfulRequestResponse(message, list(connectionNames))
