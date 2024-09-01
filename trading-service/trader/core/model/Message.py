from enum import Enum
import json
from typing import Optional, Any


class MessageType(Enum):
    RequestForQuote = "RequestForQuote"
    Quote = "Quote"
    Trade = "Trade"

    @staticmethod
    def fromString(messageType: str):
        if messageType == "RequestForQuote":
            return MessageType.RequestForQuote
        elif messageType == "Quote":
            return MessageType.Quote
        elif messageType == "Trade":
            return MessageType.Trade


class MessageKeys:
    MessageType = "messageType"
    AssetName = "assetName"
    Quote = "quote"
    TimeStamp = "timeStamp"
    Origin = "origin"


class DeprecatedMessage:
    _message: str = None
    _messageType: MessageType = None
    _assetName: str = None
    _origin: str = None
    _quote: float = None

    def __init__(self, message: Optional[str]):
        if message:
            message = message
            self.fromString(message)

    def fromString(self, messageString: str):
        messageAsJson = json.loads(messageString)
        if MessageKeys.MessageType in messageAsJson:
            self._messageType = MessageType.fromString(messageAsJson[MessageKeys.MessageType])
        if MessageKeys.Quote in messageAsJson:
            self._quote = messageAsJson[MessageKeys.Quote]
        if MessageKeys.AssetName in messageAsJson:
            self._assetName = messageAsJson[MessageKeys.AssetName]

    def getOrigin(self) -> Optional[str]:
        return self._origin

    def setOrigin(self, origin):
        self._origin = origin

    def getQuote(self) -> Optional[float]:
        return self._quote

    def setQuote(self, quote: float):
        self._quote = quote

    def setAssetName(self, assetName: str):
        self._assetName = assetName

    def getAssetName(self) -> Optional[str]:
        return self._assetName

    def setMessageType(self, messageType: MessageType):
        self._messageType = messageType

    def getMessageType(self) -> MessageType:
        return self._messageType

    def toString(self) -> Optional[str]:
        return str(self.toJson())

    def toJson(self) -> Any:
        return {
            "messageType": self.sanitizeForJSON(self._messageType.value),
            "assetName": self.sanitizeForJSON(self._assetName),
            "quote": self.sanitizeForJSON(self._quote),
            "origin": self.sanitizeForJSON(self._origin)
        }

    def sanitizeForJSON(self, value: Optional[Any]) -> str:
        return str(value) if value else ""
