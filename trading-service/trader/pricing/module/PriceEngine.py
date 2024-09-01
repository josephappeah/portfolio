import time
from collections import deque

from trader.core.constants.Constants import ConfigConstants
from trader.core.model.Data import Message, Quote
from trader.core.model.subscriber.ISubscriber import ISubscriber
from trader.core.model.subscriber.Subscriber import Subscriber
from trader.pricing.module.PriceGenerator import PriceGenerator
from trader.core.config.ConfigUtil import ConfigUtils
from trader.core.thread.StoppableThread import StoppableThread


class PriceEngine:
    _priceGenerator: PriceGenerator = None
    _assetName: str = None
    _priceGeneratorThread: StoppableThread = None
    _subscribers: dict[str:ISubscriber] = None

    def __init__(self, assetName, priceGenerator):
        self._priceGenerator, self._assetName = priceGenerator, assetName
        self._outGoingMessageQueue, self._subscribers = deque(), {}

    def start(self):
        self._priceGeneratorThread = StoppableThread(name=self._getThreadName(), target=self.pricingHandlerLoop)
        self._priceGeneratorThread.start()

    def pricingHandlerLoop(self):
        priceFrequency: int = int(ConfigUtils.getConfig(
            ConfigConstants.PricingSection, ConfigConstants.PriceFrequency))
        while True:
            quote: Message = self._getQuote()
            for subscriber in self._subscribers.values():
                subscriber.publish(quote)
            time.sleep(priceFrequency)

    def subscribe(self, subscriber: ISubscriber):
        if subscriber:
            self._subscribers[subscriber.getName()] = subscriber

    def unSubscribe(self, subscriber: Subscriber):
        if subscriber and subscriber.getName() in self._subscribers:
            del self._subscribers[subscriber.getName()]

    def _getThreadName(self) -> str:
        return self._assetName + ":" + "PricingGeneratorThread"

    def _getPrice(self) -> float:
        if self._priceGenerator:
            return self._priceGenerator.generatePrice()

    def _getTimestamp(self):
        pass

    def _getQuote(self) -> Message:
        quote: Quote = Quote(self._assetName, str(self._getPrice()))
        message: Message = Message()
        message.setQuote(quote)
        return message



