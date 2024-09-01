import random
from trader.pricing.model.AssetPriceConfig import PriceConfig


class PriceGenerator:
    _priceConfig: PriceConfig = None

    def __init__(self, configs: PriceConfig):
        self._priceConfig = configs

    def generatePrice(self) -> float:
        return random.randint(self._priceConfig.getLowerBoundary(),
                              self._priceConfig.getUpperBoundary()) / self._priceConfig.getScaleFactor()
