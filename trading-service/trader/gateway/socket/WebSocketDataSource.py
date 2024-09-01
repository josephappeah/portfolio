from abc import ABC
from trader.gateway.model.IDataSource import IDataSource
from trader.core.model.publisher import IPublisher


class WebSocketDataSource(IDataSource, ABC):

    def __init__(self):
        super().__init__()

    def publish(self, message):
        super().publish(message)

    def addPublisher(self, publisher: IPublisher):
        super().addPublisher(publisher)

    def removePublisher(self, publisher: IPublisher):
        super().removePublisher(publisher)



