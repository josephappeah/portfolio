from abc import ABC, abstractmethod
from typing import Any
from trader.core.model.Data import Message


class ISubscriber(ABC):
    _unSubscribeHook: Any = None

    @abstractmethod
    def consume(self, message: Message):
        pass

    @abstractmethod
    def getName(self) -> str:
        pass

    def setUnSubscribeHook(self, unSubscribeHook: Any):
        if unSubscribeHook:
            self._unSubscribeHook = unSubscribeHook

    def unSubscribeFromSource(self):
        if self._unSubscribeHook:
            self._unSubscribeHook(self)
