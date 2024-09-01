from typing import Optional

from trader.core.model.subscriber.ISubscriber import ISubscriber
from trader.pricing.PriceModule import PriceModule


class GatewayDataSourceManager:
    _priceModule: PriceModule = None

    def __init__(self):
        self._priceModule = PriceModule()
        self._priceModule.start()

    def subscribe(self, assetName: str, connectionSubscriber: ISubscriber):
        self._priceModule.subscribeToAsset(assetName, connectionSubscriber)

    def unSubscribe(self, assetName: Optional[str], connectionSubscriber: ISubscriber):
        if assetName:
            self._priceModule.unSubscribeFromAsset(assetName, connectionSubscriber)

    def hasAsset(self, assetName: str) -> bool:
        return self._priceModule.hasAsset(assetName)
