import logging
from typing import Optional, Any
import bottle

from trader.core.api.ApiHelper import ApiResponseGenerator, ApiResponseMessage, ApiUtil
from trader.core.model.Data import Message
from trader.data.api.ServiceRequestValidator import TradeServiceRequestValidator
from trader.data.module.DataServiceModule import TraderServiceModule


class TraderServiceApi:
    traderServiceApi = bottle.Bottle()
    Logger = logging.getLogger(__name__)
    traderServiceModule: Optional[TraderServiceModule] = None

    @staticmethod
    @traderServiceApi.get("/update-account-balance", method=["GET", "OPTIONS"])
    def updateAccountBalance():
        if TraderServiceApi.traderServiceModule:
            try:
                message: Message = ApiUtil.extractRequestParamsAsMessage(bottle.request)
                if not TradeServiceRequestValidator.isValidAccountBalanceUpdateRequest(message):
                    return ApiResponseGenerator.BadRequestResponse(
                        message, ApiResponseMessage.InvalidAccountBalanceUpdate.value)
                res: Any = TraderServiceApi.traderServiceModule.handleUpdateAccountBalance(message)
            except Exception as e:
                TraderServiceApi.Logger.error("Failed To Handle AccountBalanceUpdate With Error: ", e)
                return ApiResponseGenerator.InternalServerErrorResponse(
                    None, ApiResponseMessage.GeneralServerError.value)
            return res

    @staticmethod
    @traderServiceApi.get("/get-positions")
    def getPositions():
        if TraderServiceApi.traderServiceModule:
            try:
                message: Message = ApiUtil.extractRequestParamsAsMessage(bottle.request)
                if not TradeServiceRequestValidator.isValidPositionRequest(message):
                    return ApiResponseGenerator.BadRequestResponse(
                        message, ApiResponseMessage.InvalidPositionFetch.value)
                res: Any = TraderServiceApi.traderServiceModule.handleGetPositions(message)
            except Exception as e:
                TraderServiceApi.Logger.error("Failed To Handle PositionsFetch With Error: ", e)
                return ApiResponseGenerator.InternalServerErrorResponse(
                    None, ApiResponseMessage.GeneralServerError.value)
            return res

    @staticmethod
    @traderServiceApi.get("/get-account-balance", method=["GET", "OPTIONS"])
    def getAccountBalance():
        if TraderServiceApi.traderServiceModule:
            try:
                message: Message = ApiUtil.extractRequestParamsAsMessage(bottle.request)
                if not TradeServiceRequestValidator.isValidAccountBalanceUpdateRequest(message):
                    return ApiResponseGenerator.BadRequestResponse(
                        message, ApiResponseMessage.InvalidAccountBalanceFetch.value)
                res: Any = TraderServiceApi.traderServiceModule.handleGetAccountBalance(message)
            except Exception as e:
                TraderServiceApi.Logger.error("Failed To Handle AccountBalanceFetch With Error: ", e)
                return ApiResponseGenerator.InternalServerErrorResponse(
                    None, ApiResponseMessage.GeneralServerError.value)
            return res

    @staticmethod
    @traderServiceApi.get("/new-position", method=["GET", "OPTIONS"])
    def newPosition():
        if TraderServiceApi.traderServiceModule:
            try:
                message: Message = ApiUtil.extractRequestParamsAsMessage(bottle.request)
                if not TradeServiceRequestValidator.isValidNewPositionRequest(message):
                    return ApiResponseGenerator.BadRequestResponse(
                        message, ApiResponseMessage.InvalidAccountBalanceFetch.value)
                res: Any = TraderServiceApi.traderServiceModule.handleGetAccountBalance(message)
            except Exception as e:
                TraderServiceApi.Logger.error("Failed To Handle AccountBalanceFetch With Error: ", e)
                return ApiResponseGenerator.InternalServerErrorResponse(
                    None, ApiResponseMessage.GeneralServerError.value)
            return res
