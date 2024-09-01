import json
from typing import Optional, Any
import logging
import bottle
from bottle import Bottle

from trader.core.model.Data import Message
from trader.gateway.service.GatewayServiceModule import GatewayServiceModule
from trader.gateway.service.api.GatewayServiceApiValidator import GatewayServiceApiValidator
from trader.core.api.ApiHelper import ApiUtil, ApiResponseGenerator, ApiResponseMessage


class GatewayServiceApi:
    Logger = logging.getLogger(__name__)
    gatewayServiceApi: Bottle = Bottle()
    gatewayServiceModule: Optional[GatewayServiceModule] = None

    @staticmethod
    @gatewayServiceApi.hook('after_request')
    def enable_cors():
        """
        You need to add some headers to each request.
        Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
        """
        bottle.response.headers['Access-Control-Allow-Origin'] = '*'
        bottle.response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
        bottle.response.headers[
            'Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

    @staticmethod
    @gatewayServiceApi.get("/request-for-quote", method=["GET", "OPTIONS"])
    def requestForQuote():
        if GatewayServiceApi.gatewayServiceModule:
            try:
                message: Message = ApiUtil.extractRequestParamsAsMessage(bottle.request)
                if not GatewayServiceApiValidator.isValidRequestForQuote(message):
                    return ApiResponseGenerator.BadRequestResponse(
                        message, ApiResponseMessage.InvalidRequestForQuote.value)
                res: Any = GatewayServiceApi.gatewayServiceModule.handleRequestForQuote(message)
            except Exception as e:
                GatewayServiceApi.Logger.error("Failed To Handle RequestForQuote With Error: ", e)
                return ApiResponseGenerator.InternalServerErrorResponse(
                    None, ApiResponseMessage.GeneralServerError.value)
            return res

    @staticmethod
    @gatewayServiceApi.route("/un-request-for-quote", method=["POST", "OPTIONS"])
    def unRequestForQuote():
        if GatewayServiceApi.gatewayServiceModule:
            try:
                message: Message = ApiUtil.extractRequestParamsAsMessage(bottle.request.params)
                if not GatewayServiceApiValidator.isValidRequestForQuote(message):
                    return ApiResponseGenerator.BadRequestResponse(
                        message, ApiResponseMessage.InvalidRequestForQuote.value)
                res: Any = GatewayServiceApi.gatewayServiceModule.handleUnRequestForQuote(message)
            except Exception as e:
                GatewayServiceApi.Logger.error("Failed To Handle UnRequestForQuote With Error: ", e)
                return ApiResponseGenerator.InternalServerErrorResponse(
                    None, ApiResponseMessage.GeneralServerError.value)
            return res

    @staticmethod
    @gatewayServiceApi.route("/get-hosts-active-connections", method=["GET", "OPTIONS"])
    def activeConnectionsForHost():
        if GatewayServiceApi.gatewayServiceModule:
            try:
                message: Message = ApiUtil.extractRequestParamsAsMessage(bottle.request.params)
                if not GatewayServiceApiValidator.isValidRequest(message):
                    return ApiResponseGenerator.BadRequestResponse(
                        message, ApiResponseMessage.InvalidRequestForActiveConnections.value)
                res: Any = GatewayServiceApi.gatewayServiceModule.handleGetActiveConnectionsForHost(message)
            except Exception as e:
                GatewayServiceApi.Logger.error("Failed To Handle GetActiveConnections With Error: ", e)
                return ApiResponseGenerator.InternalServerErrorResponse(
                    None, ApiResponseMessage.GeneralServerError.value)
            return res

    @staticmethod
    @gatewayServiceApi.route("/get-active-connections", method=["GET", "OPTIONS"])
    def activeConnections():
        if GatewayServiceApi.gatewayServiceModule:
            try:
                res: Any = GatewayServiceApi.gatewayServiceModule.handleGetActiveConnections()
            except Exception as e:
                GatewayServiceApi.Logger.error("Failed To Handle GetActiveConnections With Error: ", e)
                return ApiResponseGenerator.InternalServerErrorResponse(
                    None, ApiResponseMessage.GeneralServerError.value)
            return res

