import logging
import os

from trader.core.constants.Constants import ConfigConstants
from trader.data.api.ServiceApi import TraderServiceApi
from trader.data.module.DataServiceModule import TraderServiceModule
from trader.core.config.ConfigUtil import ConfigUtils
from trader.core.thread.StoppableThread import StoppableThread


class DataServer:
    _logger = logging.getLogger(__name__)
    _server: StoppableThread = None
    _traderServiceModule: TraderServiceModule = None

    def __init__(self, traderServiceModule: TraderServiceModule):
        self._traderServiceModule = traderServiceModule

    @staticmethod
    def handleStartServer():
        host = ConfigUtils.getConfig(ConfigConstants.GatewayServerSection, ConfigConstants.GatewayServerHost)
        port = 8081
        server = ConfigUtils.getConfig(ConfigConstants.GatewayServerSection, ConfigConstants.GatewayServerWindows)
        if os.name == "nt":
            server = ConfigUtils.getConfig(ConfigConstants.GatewayServerSection, ConfigConstants.GatewayServerWindows)

        TraderServiceApi.traderServiceApi.run(
            host=host,
            port=int(port),
            server=server,
            debug=True
        )

    def start(self):
        self._server = StoppableThread(name="DataService", target=DataServer.handleStartServer)
        self._server.start()
