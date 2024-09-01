from typing import Optional
from trader.core.model.Data import Message


class TradeServiceRequestValidator:

    @staticmethod
    def isValidAccountBalanceUpdateRequest(message: Optional[Message]) -> bool:
        return message is not None and \
               message.getUser() and message.getAccount() \
               and message.getAccount().getAccountBalance()

    @staticmethod
    def isValidNewPositionRequest(message: Optional[Message]) -> bool:
        return True

    @staticmethod
    def isValidPositionRequest(message: Optional[Message]) -> bool:
        return True
