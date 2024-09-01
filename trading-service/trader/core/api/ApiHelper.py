import json
from enum import Enum
from typing import Optional, Any, List

import bottle

from trader.core.model.Data import Message, Quote, User, Account, AccountBalance, Position


class ApiUtil:
    @staticmethod
    def extractRequestBodyAsMessage(request: bottle.Request):
        print(request.body.read().decode("utf-8"))

    @staticmethod
    def extractQuoteFromParams(params: dict) -> Quote:
        assetName, quote = None, None
        if "quote[assetName]" in params:
            assetName = params["quote[assetName]"]
        if "quote[quote]" in params:
            quote = params["quote[quote]"]
        return Quote(assetName=assetName, quote=quote)

    @staticmethod
    def extractPositionsFromParams(params: dict) -> List[Position]:
        positions: List[Position] = []
        for i in range(1):
            amountKey = "positions[" + str(i) + "][amount]"
            quoteKey = "positions[" + str(i) + "][quote][quote]"
            sideKey = "positions[" + str(i) + "][side]"
            statusKey = "positions[" + str(i) + "][status]"
            assetNameKey = "positions[" + str(i) + "][quote][assetName]"

            if amountKey in params and \
                quoteKey in params and sideKey in params and statusKey in params and assetNameKey in params:
                quote: Quote = Quote(assetName=params[assetNameKey], quote=params[quoteKey])
                position: Position = Position(quote=quote, status=params[statusKey],
                                              side=params[sideKey], amount=params[amountKey])
                positions.append(position)
        return positions

    @staticmethod
    def extractUserFromParams(params: dict) -> User:
        return User(origin=params["user[origin]"], username=params["user[username]"])

    @staticmethod
    def extractAccountFromParams(params: dict) -> Account:
        accountBalances: List[AccountBalance] = []
        for i in range(5):
            balanceKey = "account[accountBalance][" + str(i) + "][balance]"
            currencyKey = "account[accountBalance][" + str(i) + "][currency]"
            if balanceKey in params and currencyKey in params:
                accountBalances.append(AccountBalance(balance=params[balanceKey], currency=params[currencyKey]))
        account: Account = Account(accountId=params["account[accountId]"], accountBalance=accountBalances)
        return account

    @staticmethod
    def extractRequestParamsAsMessage(request: bottle.BaseRequest) -> Optional[Message]:
        params = dict(request.query)
        quote: Quote = ApiUtil.extractQuoteFromParams(params)
        positions: List[Position] = ApiUtil.extractPositionsFromParams(params)
        user: User = ApiUtil.extractUserFromParams(params)
        account: Account = ApiUtil.extractAccountFromParams(params)
        messageType: str = params["messageType"]
        message: Message = Message(quote=quote, user=user, account=account,
                                   messageType=messageType, positions=positions)
        return message


class ApiResponseMessage(Enum):
    MaxConnectionsExceededError = "Exceeded Max Allowed Connections"
    GeneralServerError = "Error Handling Request"
    AssetUnavailable = "Asset Is Unavailable"
    NoActiveConnectionsForRequestor = "Requestor Has No Active Connections"
    RFQRequestCompleted = "RFQ Request Completed"
    UnRFQRequestCompleted = "Un-RFQ Request Completed"
    InvalidRequestForQuote = "Invalid Request For Quote"
    AddAccountForUserCompleted = "Add User Account Completed"
    AddPositionForUserCompleted = "Add User Position Completed"
    InvalidAccountBalanceUpdate = "Invalid Account Balance Update"
    InvalidPositionFetch = "Invalid Account Balance Fetch"
    InvalidAccountBalanceFetch = "Invalid Account Balance Fetch"
    InvalidNewPositionRequest = "Invalid New Position Request"
    InvalidRequestForActiveConnections = "Invalid Request For Active Connections"


class ApiResponseGenerator:
    @staticmethod
    def unAuthorizedRequestResponse(message: Optional[Message], responseBody: Optional[Any]):
        responseBody: Any = ApiResponseGenerator.getResponseBody(message, responseBody)
        return ApiResponseGenerator.getHttpResponse(401, responseBody)

    @staticmethod
    def InternalServerErrorResponse(message: Optional[Message], responseBody: Optional[Any]):
        responseBody: Any = ApiResponseGenerator.getResponseBody(message, responseBody)
        return ApiResponseGenerator.getHttpResponse(500, responseBody)

    @staticmethod
    def BadRequestResponse(message: Optional[Message], responseBody: Optional[Any]):
        responseBody: Any = ApiResponseGenerator.getResponseBody(message, responseBody)
        return ApiResponseGenerator.getHttpResponse(400, responseBody)

    @staticmethod
    def successfulRequestResponse(message: Optional[Message], responseBody: Optional[Any]):
        responseBody: Any = ApiResponseGenerator.getResponseBody(message, responseBody)
        return ApiResponseGenerator.getHttpResponse(200, responseBody)

    @staticmethod
    def failedRequestResponse(message: Optional[Message], responseBody: Optional[Any]):
        responseBody: Any = ApiResponseGenerator.getResponseBody(message, responseBody)
        return ApiResponseGenerator.getHttpResponse(500, responseBody)

    @staticmethod
    def getResponseBody(message: Optional[Message], responseBody: Optional[Any]) -> Any:
        return json.dumps({
            "request": message.toJson() if message else {},
            "response": responseBody if responseBody else {}
        })

    @staticmethod
    def getHttpResponse(statusCode: int, responseBody: Any) -> bottle.HTTPResponse:
        response: bottle.HTTPResponse = bottle.HTTPResponse(status=statusCode, body=responseBody)
        response.set_header('Content-Type', 'application/json')
        response.set_header('Access-Control-Allow-Origin', '*')
        response.set_header(
            'Access-Control-Allow-Headers', 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token')
        response.set_header('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS')
        return response

