from abc import abstractmethod, ABC
from collections import deque
from typing import Optional
from trader.core.model.Data import Message
from trader.core.model.publisher import IPublisher
from trader.core.model.subscriber import ISubscriber
from trader.core.thread.StoppableThread import StoppableThread


class IDataDestination(ABC):
    _messageQueue: deque[Message] = None
    _messageWorker: StoppableThread = None
    _subscribers: dict[str:ISubscriber] = None
    _connectionKey: str = None
    _defaultDataDestinationNamePrefix: str = "DataDestination:"

    def __init__(self):
        self._messageQueue, self._subscribers = deque(), {}

    @abstractmethod
    def consume(self, message: Optional[Message]):
        if message:
            self._messageQueue.append(message)

    @abstractmethod
    def addSubscriber(self, subscriber: ISubscriber):
        if subscriber:
            self._subscribers[subscriber.getName()].append(subscriber)

    @abstractmethod
    def removeSubscriber(self, subscriber: ISubscriber):
        if subscriber and subscriber.getName() in self._subscribers:
            del self._subscribers[subscriber.getName()]

    def setConnectionKey(self, connectionKey: str):
        if connectionKey:
            self._connectionKey = connectionKey

    def getName(self) -> str:
        if self._connectionKey:
            return self._defaultDataDestinationNamePrefix + self._connectionKey
        return self._defaultDataDestinationNamePrefix

    def publish(self):
        while True:
            if self._messageQueue and self._subscribers:
                message: Message = self._messageQueue.popleft()
                for subscriber in self._subscribers.values():
                    subscriber.consume(message)

    def start(self):
        self._messageWorker = StoppableThread(name=self.getName(), target=self.publish)
        self._messageWorker.start()
