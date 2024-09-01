from abc import ABC, abstractmethod
from trader.core.model.Data import Message


class IPublisher(ABC):

    @abstractmethod
    def publish(self, message: Message):
        pass

    @abstractmethod
    def getName(self) -> str:
        pass
