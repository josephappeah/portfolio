import logging

from trader.data.source.cache.ServiceCache import TraderServiceDataCache
from trader.core.model.Data import Message, Position, AccountBalance
from trader.core.api.ApiHelper import ApiResponseGenerator, ApiResponseMessage


class TraderServiceModule:
    _dataSourceManager: TraderServiceDataCache = None
    Logger = logging.getLogger(__name__)

    def __init__(self, dataSourceManager: TraderServiceDataCache):
        self._dataSourceManager = dataSourceManager

    def handleGetPositions(self, message: Message):
        if not self._dataSourceManager:
            self.Logger.error("DataSourceCache Manager Is Not Initialized")
            return ApiResponseGenerator.InternalServerErrorResponse(
                message, ApiResponseMessage.GeneralServerError.value)
        positions: list[Position] = self._dataSourceManager.getPositionsForUser(message.getUser())
        return ApiResponseGenerator.successfulRequestResponse(message, [position.toJson() for position in positions])

    def handleUpdateAccountBalance(self, message: Message):
        if not self._dataSourceManager:
            self.Logger.error("DataSourceCache Manager Is Not Initialized")
            return ApiResponseGenerator.InternalServerErrorResponse(
                message, ApiResponseMessage.GeneralServerError.value)
        for accountBalance in message.getAccount().getAccountBalance():
            self._dataSourceManager.addAccountForUser(message.getUser(), accountBalance)
        return ApiResponseGenerator.successfulRequestResponse(
            message, ApiResponseMessage.AddAccountForUserCompleted.value)

    def handleGetAccountBalance(self, message: Message):
        if not self._dataSourceManager:
            self.Logger.error("DataSourceCache Manager Is Not Initialized")
            return ApiResponseGenerator.InternalServerErrorResponse(
                message, ApiResponseMessage.GeneralServerError.value)
        accounts: list[AccountBalance] = self._dataSourceManager.getAccountsForUser(message.getUser())
        return ApiResponseGenerator.successfulRequestResponse(message, [account.toJson() for account in accounts])

    def handleNewPosition(self, message: Message):
        if not self._dataSourceManager:
            self.Logger.error("DataSourceCache Manager Is Not Initialized")
            return ApiResponseGenerator.InternalServerErrorResponse(
                message, ApiResponseMessage.GeneralServerError.value)
        self._dataSourceManager.addPositionForUser(message.getUser(), message.getPositions()[0])
        return ApiResponseGenerator.successfulRequestResponse(
            message, ApiResponseMessage.AddPositionForUserCompleted.value)

