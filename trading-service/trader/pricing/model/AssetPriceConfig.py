from trader.core.constants.Constants import ConfigConstants
from trader.core.config.ConfigUtil import ConfigUtils


class PriceConfig:
    _lowerBoundary: int = None
    _upperBoundary: int = None
    _scaleFactor: int = None
    _assetName: str = None
    _config: str = None

    def __init__(self, config):
        self._config = config
        self._parseConfig()

    def _parseConfig(self):
        configDelimiter: str = ConfigUtils.getConfig(ConfigConstants.PricingSection,
                                                     ConfigConstants.PricingAssetConfigDelimiter)
        configParts = self._config.split(configDelimiter)
        self._assetName = configParts[0]
        self._lowerBoundary = int(configParts[1])
        self._upperBoundary = int(configParts[2])
        self._scaleFactor = int(configParts[3])

    def getLowerBoundary(self) -> int:
        return self._lowerBoundary

    def getUpperBoundary(self) -> int:
        return self._upperBoundary

    def getConfig(self) -> str:
        return self._config

    def getAssetName(self) -> str:
        return self._assetName

    def getScaleFactor(self) -> int:
        return self._scaleFactor
