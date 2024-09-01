import pathlib
import logging
from typing import Optional

from trader.core.constants.Constants import Constants
from configparser import ConfigParser


class ConfigUtils:
    Logger = logging.getLogger(__name__)
    Configs = None

    @staticmethod
    def getConfigFilePath() -> pathlib.Path:
        configFilePath = pathlib.Path(__file__).parent.parent.parent.parent.absolute() / Constants.ConfigFilePath
        if not configFilePath.exists():
            raise Exception("Config File Doesnt Exist")
        ConfigUtils.Logger.info("Config File Path Is: {%s}", configFilePath)
        return configFilePath

    @staticmethod
    def parseConfigs() -> dict:
        configFilePath = ConfigUtils.getConfigFilePath()
        configParser = ConfigParser()
        configParser.read([configFilePath])

        parsedConfigs = {}
        for section in configParser.sections():
            parsedConfigs[section] = {}
            for k, v in configParser.items(section):
                parsedConfigs[section][k] = v
        ConfigUtils.Logger.info("Parsed Configs: {%s}", str(parsedConfigs))
        ConfigUtils.Configs = parsedConfigs
        return parsedConfigs

    @staticmethod
    def getConfig(section: str, key: str) -> Optional[str]:
        try:
            config: str = ConfigUtils.getConfigs().get(section).get(key)
            return config
        except Exception as e:
            ConfigUtils.Logger.debug("Config [Section: {%s}, Key: {%s}] Does Not Exist", section, key, e)
            return None

    @staticmethod
    def getConfigs() -> dict:
        if not ConfigUtils.Configs:
            ConfigUtils.parseConfigs()
        return ConfigUtils.Configs
