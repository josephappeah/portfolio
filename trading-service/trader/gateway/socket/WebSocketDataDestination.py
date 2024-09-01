import logging
from abc import ABC
from typing import Optional

from trader.core.model.Data import Message
from trader.gateway.model.IDataDestination import IDataDestination
from trader.core.model.subscriber import ISubscriber


class WebSocketDataDestination(IDataDestination, ABC):
    Logger = logging.getLogger(__name__)

    def __init__(self):
        super().__init__()

    def consume(self, message: Optional[Message]):
        self.Logger.debug("Consuming Message: {%s}", message.toString())
        super().consume(message)

    def addSubscriber(self, subscriber: ISubscriber):
        self.Logger.debug("Adding New Subscriber: {%s}", subscriber.getName())
        super().addSubscriber(subscriber)

    def removeSubscriber(self, subscriber: ISubscriber):
        self.Logger.debug("Removing Subscriber: {%s}", subscriber.getName())
        super().removeSubscriber(subscriber)
