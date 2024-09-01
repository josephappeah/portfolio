from typing import Any, List
from trader.core.model.Data import Message
from trader.core.model.publisher.IPublisher import IPublisher


class Publisher(IPublisher):
    subscribers: List[Any] = None  # predicates
    PublisherNamePrefix: str = "Publisher:"
    _name: str = None

    def publish(self, message: Message):
        for consume in self.subscribers:
            consume(message)

    def getName(self) -> str:
        if not self._name:
            self._name = self.PublisherNamePrefix
        return self._name
