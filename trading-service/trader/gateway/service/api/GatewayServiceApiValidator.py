from typing import Optional
from trader.core.model.Data import Message
# from trader.core.model.Message import MessageType


class GatewayServiceApiValidator:

    @staticmethod
    def isValidRequest(message: Optional[Message]) -> bool:
        if not message:
            return False
        return message.getUser().getOrigin() is not None

    @staticmethod
    def isValidRequestForQuote(message: Optional[Message]) -> bool:
        if not message:
            return False
        return GatewayServiceApiValidator.isValidRequest(message) and \
            message.getQuote().getAssetName() is not None and \
            message.getMessageType() == "RequestForQuote"
