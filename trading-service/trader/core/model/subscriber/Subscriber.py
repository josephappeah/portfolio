from trader.core.model.Data import Message
from trader.core.model.subscriber.ISubscriber import ISubscriber
from trader.core.model.subscriber.MessageConsumer import Consumer


class Subscriber(ISubscriber):
    SubscriberNamePrefix: str = "Subscriber:"
    _consumer: Consumer = None
    _name: str = None

    def __init__(self, consumer: Consumer):
        self._consumer = consumer

    def getName(self) -> str:
        if not self._name:
            self._name = self.SubscriberNamePrefix + self._consumer.getName()
        return self._name

    def consume(self, message: Message):
        self._consumer.consume(message)
