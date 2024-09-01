from typing import Optional, List

from trader.core.constants.Constants import ConfigConstants
from trader.core.model.subscriber.ISubscriber import ISubscriber
from trader.pricing.model.AssetPriceConfig import PriceConfig
from trader.pricing.module.PriceEngine import PriceEngine
import logging

from trader.pricing.module.PriceGenerator import PriceGenerator
from trader.core.config.ConfigUtil import ConfigUtils


class PriceModule:
    """
        Here we hold a map of asset name to asset publisher
        consumers will subscribe to assets here
        PricingEngine class represents the asset publisher - one per asset
        subscribers will subscribe and unsubscribe to pricing on this class
    """
    Logger = logging.getLogger(__name__)
    _assetMap: dict[str:PriceEngine] = None

    def __init__(self):
        self._assetMap = {}

    def hasAsset(self, assetName: str) -> bool:
        return self._assetMap and assetName in self._assetMap

    def subscribeToAsset(self, assetName: str, subscriber: ISubscriber):
        if assetName in self._assetMap:
            self._assetMap[assetName].subscribe(subscriber)
            subscriber.setUnSubscribeHook(self.unSubscribe)

    def unSubscribeFromAsset(self, assetName: str, subscriber: ISubscriber):
        if assetName in self._assetMap:
            self._assetMap[assetName].unSubscribe(subscriber)

    def unSubscribe(self, subscriber: ISubscriber):
        if subscriber:
            for priceEngine in self._assetMap.values():
                priceEngine.unSubscribe(subscriber)

    def _configureFxPricing(self):
        fxPricingConfig: Optional[str] = ConfigUtils.getConfig(ConfigConstants.PricingSection,
                                                               ConfigConstants.PricingFxConfig)
        fxPricingDelimiter: Optional[str] = ConfigUtils.getConfig(ConfigConstants.PricingSection,
                                                                  ConfigConstants.PricingConfigDelimiter)
        fxPricingConfigsByAsset: List[str] = fxPricingConfig.split(fxPricingDelimiter)
        self.Logger.info("Configuring Fx Pricing From Config: {%s}", fxPricingConfig)
        for fxPriceConfig in fxPricingConfigsByAsset:
            priceConfig: PriceConfig = PriceConfig(fxPriceConfig)
            priceGenerator: PriceGenerator = PriceGenerator(priceConfig)
            priceEngine: PriceEngine = PriceEngine(priceConfig.getAssetName(), priceGenerator)
            self._assetMap[priceConfig.getAssetName()] = priceEngine

    def start(self):
        self._configureFxPricing()
        #
        for pricingEngine in self._assetMap.values():
            pricingEngine.start()
