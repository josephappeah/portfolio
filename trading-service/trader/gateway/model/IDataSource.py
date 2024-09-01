from abc import abstractmethod, ABC
from collections import deque

from trader.core.model.Data import Message
from trader.core.model.publisher import IPublisher
from trader.core.model.subscriber.ISubscriber import ISubscriber
from trader.core.thread.StoppableThread import StoppableThread


class IDataSource(ISubscriber, ABC):
    _publishers: dict[str:IPublisher] = None
    _messageQueue: deque[Message] = None
    _messageWorker: StoppableThread = None
    _connectionKey: str = None
    _defaultDataSourceNamePrefix: str = "DataSource:"

    def __init__(self):
        self._messageQueue, self._publishers = deque(), {}

    def consume(self, message: Message):
        while True:
            if self._messageQueue and self._publishers:
                message: Message = self._messageQueue.popleft()
                for publisher in self._publishers.values():
                    publisher.publish(message)

    @abstractmethod
    def publish(self, message: Message):
        if message:
            self._messageQueue.append(message)

    @abstractmethod
    def addPublisher(self, publisher: IPublisher):
        if publisher:
            self._publishers[publisher.getName()] = publisher

    @abstractmethod
    def removePublisher(self, publisher: IPublisher):
        if publisher and publisher.getName() in self._publishers:
            del self._publishers[publisher.getName()]

    def hasMessages(self):
        return len(self._messageQueue) > 0

    def getMessageQueue(self):
        return self._messageQueue

    def setConnectionKey(self, connectionKey: str):
        if connectionKey:
            self._connectionKey = connectionKey

    def start(self):
        self._messageWorker = StoppableThread(name=self.getName(), target=self.consume)
        self._messageWorker.start()

    def getName(self) -> str:
        if self._connectionKey:
            return self._defaultDataSourceNamePrefix + self._connectionKey
        return self._defaultDataSourceNamePrefix
